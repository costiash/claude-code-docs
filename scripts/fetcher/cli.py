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
from typing import Dict, List

import requests

from .config import (
    RATE_LIMIT_DELAY,
    SITEMAP_URLS,
    LLMS_TXT_URLS,
    DEFAULT_SCRATCH_DIR,
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


def check_no_filename_collisions(raw_pages: List[Dict]) -> List[str]:
    """
    Map every page to its filename and abort on any collision (fail fast, no network).

    Two URLs mapping to one filename would silently drop a page from the manifest
    and overwrite one cached file with another. This makes that bug loud.

    Returns:
        The list of filenames, parallel to ``raw_pages``.

    Raises:
        ValueError: On the first collision found.
    """
    seen: Dict[str, str] = {}
    filenames: List[str] = []
    for raw in raw_pages:
        filename = url_to_filename(raw["url"])
        if filename in seen:
            raise ValueError(
                f"Filename collision: {filename!r} from {raw['url']} and {seen[filename]}"
            )
        seen[filename] = raw["url"]
        filenames.append(filename)
    return filenames


def main():
    """Run the v2 fetch pipeline."""
    start_time = datetime.now()
    repo_root = Path(__file__).parent.parent.parent

    scratch = Path(os.environ.get("DOCS_SCRATCH_DIR", str(repo_root / DEFAULT_SCRATCH_DIR)))
    scratch.mkdir(parents=True, exist_ok=True)
    logger.info(f"Fetch scratch dir: {scratch}")

    limit = int(os.environ.get("DOCS_FETCH_LIMIT", "0") or "0")

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

        filenames = check_no_filename_collisions(raw_pages)

        for i, (raw, filename) in enumerate(zip(raw_pages, filenames), 1):
            logger.info(f"[{i}/{len(raw_pages)}] {filename}")
            entry = build_page_entry(raw, filename, session, scratch, old_by_url)
            stats[entry["fetch_status"]] = stats.get(entry["fetch_status"], 0) + 1
            pages.append(entry)
            if i < len(raw_pages):
                time.sleep(RATE_LIMIT_DELAY)

        changelog = build_changelog_entry(session, scratch, old_by_url)
        stats[changelog["fetch_status"]] = stats.get(changelog["fetch_status"], 0) + 1
        pages.append(changelog)

    sources = list(SITEMAP_URLS) + list(LLMS_TXT_URLS)
    manifest = build_manifest(pages, sources)

    if limit:
        out_path = scratch / "paths_manifest.preview.json"
    else:
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
        logger.error("No pages were fetched successfully!")
        sys.exit(1)


if __name__ == "__main__":
    main()
