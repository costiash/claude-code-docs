"""
Safety safeguards for the v2 pipeline.

v1 guarded against mass deletion of tracked ``docs/*.md`` files. v2 commits no
prose — the thing worth protecting is now the **manifest**. Two gates:

1. :func:`validate_discovery_threshold` — refuse to proceed if discovery found
   fewer than ``MIN_DISCOVERY_THRESHOLD`` pages (a broken sitemap/llms.txt).
2. :func:`validate_manifest_transition` — refuse to write a new manifest that
   drops more than ``MAX_DELETION_PERCENT`` of the previous pages, or leaves
   fewer than ``MIN_EXPECTED_FILES`` total. The first v2 run (no predecessor)
   always passes.
"""

import sys
from typing import Dict, List

from .config import (
    MIN_DISCOVERY_THRESHOLD,
    MAX_DELETION_PERCENT,
    MIN_EXPECTED_FILES,
    logger,
)


def validate_discovery_threshold(pages: List) -> List:
    """
    Ensure discovery returned enough pages; abort otherwise.

    Args:
        pages: Discovered page records (any list; only the count matters).

    Returns:
        The same list, unchanged, when the count is sufficient.

    Raises:
        SystemExit: If fewer than ``MIN_DISCOVERY_THRESHOLD`` pages were found.
    """
    if len(pages) < MIN_DISCOVERY_THRESHOLD:
        logger.critical("=" * 70)
        logger.critical("🚨 SAFEGUARD TRIGGERED: Insufficient pages discovered!")
        logger.critical(
            f"   Only {len(pages)} discovered (minimum: {MIN_DISCOVERY_THRESHOLD})."
        )
        logger.critical("   Likely a sitemap/llms.txt discovery failure. Aborting.")
        logger.critical("=" * 70)
        sys.exit(1)

    logger.info(f"✅ Discovery validated: {len(pages)} pages")
    return pages


def validate_manifest_transition(old_manifest: Dict, new_pages: List[Dict]) -> None:
    """
    Guard the old→new manifest transition against mass removal.

    Args:
        old_manifest: The previously-loaded v2 manifest (``{pages: [...]}``).
        new_pages: The page entries about to be written.

    Raises:
        SystemExit: If the transition would remove > ``MAX_DELETION_PERCENT`` of
            the previous pages, or leave < ``MIN_EXPECTED_FILES`` pages actually
            fetched this run (``fetch_status == "ok"``) — the latter catches a
            run where discovery is fine but most per-page fetches failed.
            Counting sha256 here would be meaningless: carry-forward copies old
            hashes into ``stale`` entries, so even a 100%-failed run has them set.
    """
    old_urls = {p["url"] for p in old_manifest.get("pages", []) if p.get("url")}
    new_urls = {p["url"] for p in new_pages if p.get("url")}

    # First v2 run (or unreadable predecessor): nothing to compare — pass.
    if not old_urls:
        logger.info("No prior v2 manifest — skipping transition check (clean start).")
    else:
        removed = old_urls - new_urls
        removed_percent = (len(removed) / len(old_urls)) * 100
        if removed_percent > MAX_DELETION_PERCENT:
            logger.critical("=" * 70)
            logger.critical("🚨 SAFEGUARD TRIGGERED: Mass page removal prevented!")
            logger.critical(
                f"   Would remove {len(removed)} of {len(old_urls)} pages "
                f"({removed_percent:.1f}%, threshold {MAX_DELETION_PERCENT}%)."
            )
            logger.critical("   Likely a discovery failure. Aborting before write.")
            logger.critical("=" * 70)
            sys.exit(1)

    # Count pages actually fetched THIS run. sha256 alone is not evidence of a
    # live fetch — carry-forward copies old hashes into "stale" entries, so an
    # all-stale (100%-failed) run would pass a sha256-based count.
    fetched_ok = [p for p in new_pages if p.get("fetch_status") == "ok"]
    if len(fetched_ok) < MIN_EXPECTED_FILES:
        logger.critical("=" * 70)
        logger.critical("🚨 SAFEGUARD TRIGGERED: Too few successfully fetched pages!")
        logger.critical(
            f"   Only {len(fetched_ok)} of {len(new_pages)} pages fetched OK this run "
            f"(fetch_status == \"ok\"; minimum {MIN_EXPECTED_FILES}). "
            f"Most fetches failed/stale — aborting."
        )
        logger.critical("=" * 70)
        sys.exit(1)

    logger.info(
        f"✅ Manifest transition validated: {len(new_pages)} pages "
        f"({len(fetched_ok)} fetched ok)"
    )
