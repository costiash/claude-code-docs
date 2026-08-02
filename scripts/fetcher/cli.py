"""
Command-line interface for the v2 documentation fetcher.

Pipeline: discover (llms.txt ∪ sitemap) → fail-fast filename-collision check →
fetch each page's verbatim ``.md`` into an ephemeral scratch dir → hash →
carry forward pages that fail to fetch → safeguard the transition → write the
v2 manifest at the repo root.

The scratch dir (``.doc_fetch/`` by default, ``$DOCS_SCRATCH_DIR`` to override)
is gitignored and never committed — its only jobs are to hold content for
hashing and to feed the search-index builder. The tracked ``docs/`` tree is
never written, so a full run leaves ``git status docs/`` clean.

Set ``DOCS_FETCH_LIMIT=N`` for a fast local smoke run: it caps discovery to N
pages, skips the count-based safeguards, and writes a throwaway
``paths_manifest.preview.json`` inside the scratch dir instead of the real one.
"""

import os
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

import requests

from .config import (
    RATE_LIMIT_DELAY,
    SITEMAP_URLS,
    LLMS_TXT_URLS,
    DEFAULT_SCRATCH_DIR,
    MIN_EXPECTED_FILES,
    logger,
)
from .discovery import discover_pages
from .paths import url_to_filename, page_id_from_filename, categorize_from_url
from .content import fetch_markdown, fetch_changelog, save_markdown_file, extract_title
from .manifest import (
    manifest_path,
    load_manifest,
    pages_by_url,
    build_manifest,
    save_manifest,
)
from .safeguards import validate_discovery_threshold, validate_manifest_transition

CHANGELOG_URL = "https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md"
CHANGELOG_MD_URL = "https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md"


def build_page_entry(
    raw: Dict, filename: str, session: requests.Session, scratch: Path, old_by_url: Dict
) -> Dict:
    """
    Build one v2 manifest entry: enrich the discovery record, fetch, hash.

    On fetch failure, carry forward the previous entry's hash/title with
    ``fetch_status: "stale"``; if there is no previous entry, mark ``"failed"``.
    Either way the page stays in the manifest (discovery result, not
    successful-fetches-only).
    """
    url = raw["url"]
    entry = {
        "id": page_id_from_filename(filename),
        "filename": filename,
        "url": url,
        "md_url": raw["md_url"],
        "title": raw.get("title"),
        "category": categorize_from_url(url),
        "sha256": None,
        "lastmod": raw.get("lastmod"),
        "fetch_status": "ok",
    }

    try:
        content = fetch_markdown(raw["md_url"], session, filename)
        entry["sha256"] = save_markdown_file(scratch, filename, content)
        if not entry["title"]:
            entry["title"] = extract_title(content)
        entry["fetch_status"] = "ok"
    except Exception as e:
        logger.warning(f"Fetch failed for {filename}: {e}")
        prev = old_by_url.get(url)
        if prev and prev.get("sha256"):
            entry["sha256"] = prev["sha256"]
            entry["title"] = entry["title"] or prev.get("title")
            entry["fetch_status"] = "stale"
        else:
            entry["fetch_status"] = "failed"

    return entry


def build_changelog_entry(session: requests.Session, scratch: Path, old_by_url: Dict) -> Dict:
    """Build the changelog manifest entry (special-cased: GitHub raw md_url, no lastmod)."""
    entry = {
        "id": "changelog",
        "filename": "changelog.md",
        "url": CHANGELOG_URL,
        "md_url": CHANGELOG_MD_URL,
        "title": "Claude Code Changelog",
        "category": "release_notes",
        "sha256": None,
        "lastmod": None,
        "fetch_status": "ok",
    }
    try:
        _, content = fetch_changelog(session)
        entry["sha256"] = save_markdown_file(scratch, "changelog.md", content)
        entry["fetch_status"] = "ok"
    except Exception as e:
        logger.warning(f"Changelog fetch failed: {e}")
        prev = old_by_url.get(CHANGELOG_URL)
        if prev and prev.get("sha256"):
            entry["sha256"] = prev["sha256"]
            entry["fetch_status"] = "stale"
        else:
            entry["fetch_status"] = "failed"
    return entry


def map_pages_to_filenames(raw_pages: List[Dict]) -> List[Tuple[Dict, str]]:
    """
    Map every page to its filename; skip unmappable URLs, abort on collision.

    A single malformed discovery URL (e.g. an empty page slug from a bad upstream
    llms.txt line) is logged and skipped rather than crashing the whole 3-hourly
    run. A genuine *collision* (two URLs -> one filename) still raises, since
    silently dropping one would corrupt the manifest/cache.

    Returns:
        ``(raw, filename)`` pairs for the pages that map cleanly (parallel, aligned).

    Raises:
        ValueError: On the first filename collision.
    """
    seen: Dict[str, str] = {}
    result: List[Tuple[Dict, str]] = []
    for raw in raw_pages:
        try:
            filename = url_to_filename(raw["url"])
        except ValueError as e:
            logger.warning(f"Skipping page with unmappable URL {raw['url']!r}: {e}")
            continue
        if filename in seen:
            raise ValueError(
                f"Filename collision: {filename!r} from {raw['url']} and {seen[filename]}"
            )
        seen[filename] = raw["url"]
        result.append((raw, filename))
    return result


def count_ok_doc_pages(pages: List[Dict]) -> int:
    """
    Count documentation pages fetched OK this run (changelog excluded).

    The changelog is GitHub-hosted, so it succeeds even during a total docs-site
    outage — counting it would let ``ok == 1`` pass for a run where every real
    documentation fetch failed. Pure function so the pre-save guard is testable.
    """
    return sum(
        1
        for p in pages
        if p.get("fetch_status") == "ok" and p.get("id") != "changelog"
    )


def validate_fetch_success(pages: List[Dict], min_ok: int = MIN_EXPECTED_FILES) -> None:
    """
    Pre-save guard: abort (before any manifest write) if too few pages fetched OK.

    Raises:
        SystemExit: If fewer than ``min_ok`` documentation pages (changelog
            excluded) have ``fetch_status == "ok"``.
    """
    ok_count = count_ok_doc_pages(pages)
    if ok_count < min_ok:
        logger.critical("=" * 70)
        logger.critical("🚨 SAFEGUARD TRIGGERED: Too few pages fetched successfully!")
        logger.critical(
            f"   Only {ok_count} documentation pages fetched OK this run "
            f"(minimum {min_ok}; changelog excluded). Likely a docs-site outage."
        )
        logger.critical("   Refusing to write the manifest. Aborting.")
        logger.critical("=" * 70)
        sys.exit(1)
    logger.info(f"✅ Fetch success validated: {ok_count} documentation pages ok")


def parse_fetch_limit(raw: str) -> int:
    """Parse ``DOCS_FETCH_LIMIT`` with a clear error instead of a raw traceback."""
    raw = raw or "0"
    try:
        return int(raw)
    except ValueError:
        logger.error(
            f"Invalid DOCS_FETCH_LIMIT={raw!r}: must be an integer "
            f"(e.g. DOCS_FETCH_LIMIT=8 for a preview run, or unset for a full run)."
        )
        sys.exit(1)


def main():
    """Run the v2 fetch pipeline."""
    start_time = datetime.now()
    repo_root = Path(__file__).parent.parent.parent

    scratch = Path(os.environ.get("DOCS_SCRATCH_DIR", str(repo_root / DEFAULT_SCRATCH_DIR)))
    scratch.mkdir(parents=True, exist_ok=True)
    logger.info(f"Fetch scratch dir: {scratch}")

    limit = parse_fetch_limit(os.environ.get("DOCS_FETCH_LIMIT", "0"))

    manifest_file = manifest_path(repo_root)
    old_manifest = load_manifest(manifest_file)
    old_by_url = pages_by_url(old_manifest)

    stats = {"ok": 0, "stale": 0, "failed": 0}
    pages: List[Dict] = []

    with requests.Session() as session:
        raw_pages = discover_pages(session)

        if limit:
            raw_pages = raw_pages[:limit]
            logger.warning(
                f"DOCS_FETCH_LIMIT={limit}: preview mode — safeguards skipped, "
                f"writing throwaway manifest to scratch."
            )
        else:
            raw_pages = validate_discovery_threshold(raw_pages)

        page_pairs = map_pages_to_filenames(raw_pages)

        for i, (raw, filename) in enumerate(page_pairs, 1):
            logger.info(f"[{i}/{len(page_pairs)}] {filename}")
            entry = build_page_entry(raw, filename, session, scratch, old_by_url)
            stats[entry["fetch_status"]] = stats.get(entry["fetch_status"], 0) + 1
            pages.append(entry)
            if i < len(page_pairs):
                time.sleep(RATE_LIMIT_DELAY)

        changelog = build_changelog_entry(session, scratch, old_by_url)
        stats[changelog["fetch_status"]] = stats.get(changelog["fetch_status"], 0) + 1
        pages.append(changelog)

    sources = list(SITEMAP_URLS) + list(LLMS_TXT_URLS)
    manifest = build_manifest(pages, sources)

    if limit:
        out_path = scratch / "paths_manifest.preview.json"
    else:
        # Both guards run BEFORE the write: a failed run must never overwrite
        # the committed manifest (the changelog alone must not count as success).
        validate_fetch_success(pages)
        validate_manifest_transition(old_manifest, pages)
        out_path = manifest_file

    save_manifest(out_path, manifest)

    duration = datetime.now() - start_time
    logger.info("=" * 50)
    logger.info(f"Fetch completed in {duration}")
    logger.info(
        f"Pages: {len(pages)} | ok={stats['ok']} stale={stats['stale']} failed={stats['failed']}"
    )
    logger.info(f"Manifest: {out_path}")

    if stats["ok"] == 0:
        # Preview-mode backstop (full runs are guarded by validate_fetch_success
        # before the write above).
        logger.error("No pages were fetched successfully!")
        sys.exit(1)


if __name__ == "__main__":
    main()
