"""
Manifest v2 read/write.

The v2 manifest lives at the repo root (``paths_manifest.json``) and is the
single source of truth. Shape::

    {
      "schema_version": 2,
      "generated_at": "2026-07-29T...Z",
      "sources": ["https://code.claude.com/docs/llms.txt", ...],
      "pages": [
        { "id": "claude-code/hooks", "filename": "claude-code__hooks.md",
          "url": "https://code.claude.com/docs/en/hooks",
          "md_url": "https://code.claude.com/docs/en/hooks.md",
          "title": "Hooks", "category": "claude_code",
          "sha256": "...", "lastmod": "2026-07-...Z", "fetch_status": "ok" },
        ...
      ]
    }

``pages`` is the *discovery result*, not a successful-fetches-only list: a page
whose fetch fails is carried forward (``fetch_status: "stale"``) rather than
dropped, so a transient network error never deletes a page from the manifest.
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

from .config import MANIFEST_SCHEMA_VERSION, PATHS_MANIFEST_FILE, logger


def manifest_path(repo_root: Path) -> Path:
    """Path to the v2 manifest at the repo root."""
    return repo_root / PATHS_MANIFEST_FILE


def load_manifest(path: Path) -> Dict:
    """
    Load the existing v2 manifest, or return an empty one.

    A missing file, or a valid-JSON but non-v2 (e.g. legacy ``{metadata,
    categories}``) manifest yields an empty ``{schema_version, pages: []}`` — so
    the first v2 run has nothing to carry forward and is treated as a clean start
    (not a mass removal).

    An *existing* file that will not parse is corruption, not a clean start:
    returning empty would make it indistinguishable from a first run and let
    :func:`validate_manifest_transition` skip the mass-deletion guard. That case
    fails closed (``SystemExit``) so a truncated manifest can never wave through a
    catastrophic page loss.
    """
    if path.exists():
        try:
            data = json.loads(path.read_text())
            if not isinstance(data, dict):
                raise ValueError(f"top-level JSON is {type(data).__name__}, not an object")
        except Exception as e:
            logger.critical("=" * 70)
            logger.critical(f"🚨 SAFEGUARD: existing manifest {path} is unreadable: {e}")
            logger.critical("   Refusing to proceed — a corrupt manifest must not read as a")
            logger.critical("   clean first run and skip the mass-deletion guard.")
            logger.critical("   Fix or remove the file to start clean.")
            logger.critical("=" * 70)
            sys.exit(1)
        if data.get("schema_version") == MANIFEST_SCHEMA_VERSION and isinstance(
            data.get("pages"), list
        ):
            return data
        logger.info(
            f"{path.name} is not a v2 manifest (schema_version="
            f"{data.get('schema_version')!r}); treating as empty for this run."
        )
    return {"schema_version": MANIFEST_SCHEMA_VERSION, "pages": []}


def pages_by_url(manifest: Dict) -> Dict[str, Dict]:
    """Index a manifest's pages by canonical URL (for carry-forward lookup)."""
    return {p["url"]: p for p in manifest.get("pages", []) if p.get("url")}


def build_manifest(pages: List[Dict], sources: List[str], generated_at: Optional[str] = None) -> Dict:
    """Assemble a v2 manifest dict from page entries (pages sorted by id)."""
    if generated_at is None:
        generated_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    return {
        "schema_version": MANIFEST_SCHEMA_VERSION,
        "generated_at": generated_at,
        "sources": sources,
        "pages": sorted(pages, key=lambda p: p["id"]),
    }


def save_manifest(path: Path, manifest: Dict) -> None:
    """Write a v2 manifest to disk (pretty-printed, trailing newline)."""
    path.write_text(json.dumps(manifest, indent=2) + "\n")
    logger.info(f"Wrote v2 manifest: {len(manifest.get('pages', []))} pages -> {path}")
