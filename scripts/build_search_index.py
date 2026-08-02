#!/usr/bin/env python3
"""
Build the v2 search index (prose-free) from the fetch scratch dir + manifest.

Output: repo-root ``search_index.json``. Per page::

    { "filename": "claude-code__hooks.md", "id": "claude-code/hooks",
      "title": "Hooks", "category": "claude_code",
      "url": "https://code.claude.com/docs/en/hooks",
      "headings": [ {"text": "Configuration", "level": 2}, ... ],  # anchor = slugify(text), not stored
      "terms": { "hook": 12, "matcher": 5, ... },   # stemmed word -> frequency, capped
      "word_count": 1234 }

FORBIDDEN (spec): ``content_preview``, sentence fragments, token positions,
n-grams, or any absolute ``file_path`` — nothing from which prose can be
reconstructed. Only titles, headings, and a capped bag of stemmed word counts.

Title / category / url come from the manifest (the source of truth); headings /
terms / word_count come from the fetched ``.md`` content in the scratch dir. A
manifest page whose content is missing (fetch failed/stale) is still indexed by
title so it stays findable.

STEMMING CONTRACT (must be mirrored EXACTLY on the shell query side, B3):
strip the first matching suffix from the ordered list ("ing", "ed", "es", "s")
only if at least 3 characters remain; casefold first; applied AFTER stop-word
filtering. B6 cross-checks the Python and shell implementations over a word list.
"""

import json
import math
import os
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

REPO_ROOT = Path(__file__).resolve().parent.parent
INDEX_SCHEMA_VERSION = 2
MAX_TERMS = 50
# Minimum fraction of indexed pages that must carry non-empty terms; below this
# the build refuses to overwrite the committed index (partial-outage guard).
DEFAULT_MIN_CONTENT_SHARE = 0.90

STOP_WORDS = {
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from',
    'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the',
    'to', 'was', 'will', 'with', 'or', 'but', 'not', 'can', 'this',
    'we', 'you', 'all', 'if', 'have', 'do', 'use', 'your', 'how',
    'when', 'which', 'what', 'they', 'their', 'them', 'these', 'those',
    'there', 'then', 'than', 'into', 'out', 'over', 'more', 'may',
}

_SUFFIXES = ("ing", "ed", "es", "s")
_MIN_STEM = 3


def stem(word: str) -> str:
    """Light suffix stemmer — see the STEMMING CONTRACT in the module docstring."""
    w = word.lower()
    for suffix in _SUFFIXES:
        if w.endswith(suffix) and len(w) - len(suffix) >= _MIN_STEM:
            return w[: -len(suffix)]
    return w


def slugify(text: str) -> str:
    """GitHub-style heading anchor: lowercase, non-alphanumerics → '-', collapsed."""
    s = text.lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"[\s-]+", "-", s)
    return s.strip("-")


def _strip_code_blocks(content: str) -> str:
    """Remove fenced code blocks so their contents don't pollute headings/terms."""
    return re.sub(r"```[\s\S]*?```", " ", content)


def extract_headings(content: str) -> List[Dict]:
    """
    Extract markdown headings (levels 1-6) as ``{text, level}``, excluding code blocks.

    Anchors are intentionally NOT stored: ``anchor == slugify(text)`` deterministically,
    so a consumer that needs a deep-link fragment recomputes it. Storing them doubled
    the heading payload (~435 KB on 725 pages) for zero added information.
    """
    body = _strip_code_blocks(content)
    headings = []
    for match in re.finditer(r"^(#{1,6})\s+(.+?)\s*#*\s*$", body, re.MULTILINE):
        text = match.group(2).strip()
        if not text:
            continue
        headings.append({"text": text, "level": len(match.group(1))})
    return headings


def extract_terms(content: str, cap: int = MAX_TERMS) -> Dict[str, int]:
    """Extract a capped bag of stemmed word frequencies (stop-words removed)."""
    text = _strip_code_blocks(content)
    text = re.sub(r"`[^`]+`", " ", text)                       # inline code
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)       # links -> link text
    text = re.sub(r"[^a-zA-Z\s]", " ", text)                   # drop non-alpha

    counter: Counter = Counter()
    for raw in re.findall(r"\b[a-z]{3,}\b", text.lower()):
        if raw in STOP_WORDS:
            continue
        counter[stem(raw)] += 1
    return dict(counter.most_common(cap))


def index_page(entry: Dict, content: str) -> Dict:
    """Build one index record from a manifest entry + (possibly empty) content."""
    return {
        "filename": entry["filename"],
        "id": entry.get("id", entry["filename"]),
        "title": entry.get("title") or "Untitled",
        "category": entry.get("category", "core_documentation"),
        "url": entry.get("url", ""),
        "headings": extract_headings(content) if content else [],
        "terms": extract_terms(content) if content else {},
        "word_count": len(content.split()) if content else 0,
    }


def _record_has_content(record: Optional[Dict]) -> bool:
    """True if an old index record carries real search data worth preserving."""
    if not record:
        return False
    return bool(record.get("terms") or record.get("headings") or record.get("word_count"))


def load_existing_index(path: Path) -> Dict[str, Dict]:
    """
    Load the committed search index (if any) keyed by filename, for carry-forward.

    A missing or unreadable index yields ``{}`` — carry-forward is then simply
    unavailable (the content-share guard still protects the write).
    """
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text())
        return {p["filename"]: p for p in data.get("pages", []) if p.get("filename")}
    except Exception as e:
        print(f"  ! could not read existing index {path}: {e}", file=sys.stderr)
        return {}


def build_index(manifest: Dict, scratch_dir: Path, old_pages: Optional[Dict[str, Dict]] = None) -> Dict:
    """
    Build the full v2 index from a manifest and the scratch content dir.

    ``old_pages`` (filename -> old index record) enables carry-forward: a manifest
    page whose scratch ``.md`` is missing (fetch failed/stale this run) keeps its
    previous headings/terms/word_count instead of being silently erased to an
    empty record — the index-side mirror of the manifest's ``fetch_status: stale``
    carry-forward.
    """
    old_pages = old_pages or {}
    pages = []
    with_content = 0
    carried = 0
    for entry in manifest.get("pages", []):
        md_path = scratch_dir / entry["filename"]
        content = ""
        if md_path.exists():
            try:
                content = md_path.read_text(encoding="utf-8", errors="ignore")
                with_content += 1
            except Exception as e:
                print(f"  ! could not read {md_path}: {e}", file=sys.stderr)

        page = index_page(entry, content)
        if not content:
            old = old_pages.get(entry["filename"])
            if _record_has_content(old):
                # Carry forward the old search data; metadata stays manifest-fresh.
                page["headings"] = old.get("headings", [])
                page["terms"] = old.get("terms", {})
                page["word_count"] = old.get("word_count", 0)
                carried += 1
                print(f"  ~ carried forward search data for {entry['filename']} (scratch file missing)")
        pages.append(page)

    print(
        f"Indexed {len(pages)} pages ({with_content} with content, "
        f"{carried} carried forward) from {scratch_dir}"
    )
    return {
        "schema_version": INDEX_SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "pages": pages,
    }


def check_content_share(index: Dict, min_share: float) -> None:
    """
    Guard: refuse an index where too few pages have real terms.

    Exits 1 if the fraction of pages with non-empty ``terms`` is below
    ``min_share`` — a mostly-empty index means a broken fetch run and must not
    overwrite the committed one. Set ``DOCS_INDEX_MIN_CONTENT_SHARE=0`` to disable.
    """
    pages = index.get("pages", [])
    total = len(pages)
    with_terms = sum(1 for p in pages if p.get("terms"))
    share = (with_terms / total) if total else 0.0
    if share < min_share:
        print(
            f"ERROR: only {with_terms}/{total} indexed pages ({share:.1%}) have search terms "
            f"(minimum {min_share:.0%}). Refusing to overwrite the committed index with a "
            f"mostly-empty one. Fix the fetch run, or set DOCS_INDEX_MIN_CONTENT_SHARE=0 "
            f"to force a partial build.",
            file=sys.stderr,
        )
        sys.exit(1)


def _parse_env_number(name: str, default, cast):
    """
    Parse a numeric guard threshold from the environment with a clear error.

    An unset OR empty-string variable falls back to the default (the old
    ``or "0"`` idiom silently DISABLED the guard on empty values); a
    non-numeric, non-finite (nan/inf would silently disable the ``<``
    comparison), or negative value exits with an actionable message instead
    of a raw traceback. Explicit ``=0`` still disables the guard, documented
    behavior.
    """
    raw = os.environ.get(name)
    if raw is None or raw.strip() == "":
        return default
    try:
        value = cast(raw)
        if not math.isfinite(value) or value < 0:
            raise ValueError
        return value
    except ValueError:
        print(
            f"ERROR: invalid {name}={raw!r}: must be a finite non-negative number "
            f"(e.g. {name}={default}; set {name}=0 to disable the guard).",
            file=sys.stderr,
        )
        sys.exit(1)


def save_index(index: Dict, path: Path) -> None:
    path.write_text(json.dumps(index, indent=2) + "\n")
    size_kb = path.stat().st_size / 1024
    print(f"Wrote v2 search index: {len(index['pages'])} pages, {size_kb:.1f} KB -> {path}")


def main() -> None:
    scratch_dir = Path(
        os.environ.get("DOCS_SCRATCH_DIR", str(REPO_ROOT / ".doc_fetch"))
    )
    manifest_path = REPO_ROOT / "paths_manifest.json"
    index_path = REPO_ROOT / "search_index.json"
    # Floor guard: refuse to build over an empty/tiny scratch (fail loudly, don't
    # silently commit a content-less index). Set DOCS_INDEX_MIN_FILES=0 to disable.
    min_files = _parse_env_number(
        "DOCS_INDEX_MIN_FILES", default=250, cast=int
    )
    min_content_share = _parse_env_number(
        "DOCS_INDEX_MIN_CONTENT_SHARE", default=DEFAULT_MIN_CONTENT_SHARE, cast=float
    )

    if not manifest_path.exists():
        print(f"ERROR: manifest not found at {manifest_path}", file=sys.stderr)
        sys.exit(1)

    md_count = len(list(scratch_dir.glob("*.md"))) if scratch_dir.exists() else 0
    if md_count < min_files:
        print(
            f"ERROR: scratch dir {scratch_dir} has {md_count} .md files "
            f"(minimum {min_files}). Refusing to build a content-less index. "
            f"Run the fetcher first, or set DOCS_INDEX_MIN_FILES=0 for a partial build.",
            file=sys.stderr,
        )
        sys.exit(1)

    manifest = json.loads(manifest_path.read_text())
    old_pages = load_existing_index(index_path)
    index = build_index(manifest, scratch_dir, old_pages)
    check_content_share(index, min_content_share)
    save_index(index, index_path)


if __name__ == "__main__":
    main()
