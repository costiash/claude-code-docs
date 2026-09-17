"""
Safety safeguards for the v2 pipeline.

v1 guarded against mass deletion of tracked ``docs/*.md`` files. v2 commits no
prose — the thing worth protecting is now the **manifest**. Two gates:

1. :func:`validate_discovery_threshold` — refuse to proceed if discovery found
   fewer than ``MIN_DISCOVERY_THRESHOLD`` pages (a broken sitemap/llms.txt).
2. :func:`validate_manifest_transition` — refuse to write a new manifest that
   drops more than ``MAX_DELETION_PERCENT`` of the previously-live pages
   (entries already ``stale``/``failed`` may leave freely), or leaves fewer
   than ``MIN_EXPECTED_FILES`` pages fetched OK this run, or whose share of
   ``stale``/``failed`` entries exceeds ``MAX_STALE_PERCENT``. The first v2
   run (no predecessor) always passes the removal check.

The stale ceiling closes the gap the stale-exclusion rule opens: without it, a
partial fetch outage could commit a manifest that is mostly carry-forward
entries (only the 250-ok floor applies), and a discovery drop on the next run
could then remove all of them "for free". Capping the stale share per commit
bounds that two-run loss at ``MAX_STALE_PERCENT`` dropped free plus the
ordinary ``MAX_DELETION_PERCENT`` live-removal allowance.
"""

import sys
from typing import Dict, List

from .manifest import has_url as _has_url
from .config import (
    MIN_DISCOVERY_THRESHOLD,
    MAX_DELETION_PERCENT,
    MIN_EXPECTED_FILES,
    MAX_STALE_PERCENT,
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


def count_ok_doc_pages(pages: List[Dict]) -> int:
    """
    Count documentation pages fetched OK this run (changelog excluded).

    The changelog is GitHub-hosted, so it succeeds even during a total docs-site
    outage — counting it would let ``ok == 1`` pass for a run where every real
    documentation fetch failed. Single owner of the floor semantics: both the
    transition guard below and any caller share this count.
    """
    return sum(
        1
        for p in pages
        if p.get("fetch_status") == "ok" and p.get("id") != "changelog"
    )


def count_doc_pages(pages: List[Dict]) -> int:
    """Count documentation pages (changelog excluded) regardless of status."""
    return sum(1 for p in pages if p.get("id") != "changelog")


def validate_manifest_transition(
    old_manifest: Dict, new_pages: List[Dict], confirm_removals: bool = False
) -> None:
    """
    Guard the old→new manifest transition against mass removal.

    Args:
        old_manifest: The previously-loaded v2 manifest (``{pages: [...]}``).
        new_pages: The page entries about to be written.
        confirm_removals: Operator override for ONE run (``workflow_dispatch``
            input → ``DOCS_CONFIRM_REMOVALS=1``). When set, a removal share over
            ``MAX_DELETION_PERCENT`` is logged with the full list of removed
            live URLs and allowed instead of aborting. The stale-share ceiling
            and the fetched-OK floor still apply. This is the unwedge lever for
            an upstream move that lands the redirect and the delisting in the
            same deploy: those pages go ``ok`` → absent in a single run, the
            stale-exclusion rule never sees them, and without an override the
            guard re-trips every run because the committed manifest never
            advances. Never set on scheduled runs.

    Raises:
        SystemExit: If the transition would remove > ``MAX_DELETION_PERCENT`` of
            the previous pages, leave < ``MIN_EXPECTED_FILES`` pages actually
            fetched this run (``fetch_status == "ok"``) — the latter catches a
            run where discovery is fine but most per-page fetches failed — or
            leave > ``MAX_STALE_PERCENT`` of documentation pages not ``ok``
            (a partial outage must not commit a mostly-carry-forward manifest).
            Counting sha256 here would be meaningless: carry-forward copies old
            hashes into ``stale`` entries, so even a 100%-failed run has them set.

    ``old_manifest`` is expected to come from :func:`fetcher.manifest.load_manifest`,
    which already rejects a corrupt file (unparsable, non-object, or a v2 page
    list holding a non-object); this function does not re-validate structure.

    Removal accounting: a page the previous manifest already marked ``stale``
    or ``failed`` does not count toward the deletion percentage. Those entries
    survived only by carry-forward — their fetch already failed — so discovery
    dropping them *confirms* an upstream removal rather than signalling a
    broken discovery source. Without this, a real upstream reorganisation that
    redirects a >10% block of pages (Admin API reference, 2026-09-10: 133 of
    965) wedges the pipeline permanently: the manifest can never advance, so
    every later run re-trips the guard. Only pages that were ``ok`` (or carry
    no status at all — treated as live, conservatively) count as removals,
    measured against the previously-live population so dead entries cannot pad
    the denominator. A URL is dead only when every row carrying it is
    ``stale``/``failed``; one live row keeps it live.
    """
    old_pages = [p for p in old_manifest.get("pages", []) if _has_url(p)]
    old_urls = {p["url"] for p in old_pages}
    new_urls = {p["url"] for p in new_pages if _has_url(p)}

    # First v2 run (or unreadable predecessor): nothing to compare — pass.
    if not old_urls:
        logger.info("No prior v2 manifest — skipping transition check (clean start).")
    else:
        removed = old_urls - new_urls
        # A URL is live if ANY of its rows is not stale/failed; it is dead only
        # when every row is. Duplicate rows cannot come from the fetcher (discovery
        # is keyed by canonical URL), but if a hand-edited manifest ever carried
        # them, the conservative reading keeps a still-ok URL under the guard.
        live_urls = {
            p["url"] for p in old_pages if p.get("fetch_status") not in ("stale", "failed")
        }
        already_dead = old_urls - live_urls
        removed_live = removed - already_dead
        # Denominator is the previously-live population, not the whole manifest:
        # dead entries must not pad the base and dilute a real discovery drop.
        old_live = len(old_urls - already_dead)
        removed_percent = (len(removed_live) / old_live) * 100 if old_live else 0.0
        if removed & already_dead:
            logger.info(
                f"Dropping {len(removed & already_dead)} page(s) that were already "
                f"stale/failed in the previous manifest (not counted as removals)."
            )
        if removed_percent > MAX_DELETION_PERCENT and confirm_removals:
            logger.warning("=" * 70)
            logger.warning("⚠️  Removal share over threshold — allowed by operator override.")
            logger.warning(
                f"   Removing {len(removed_live)} previously-live pages of {old_live} "
                f"({removed_percent:.1f}%, threshold {MAX_DELETION_PERCENT}%); "
                f"DOCS_CONFIRM_REMOVALS=1 for this run only."
            )
            for url in sorted(removed_live):
                logger.warning(f"   removed: {url}")
            logger.warning("=" * 70)
        elif removed_percent > MAX_DELETION_PERCENT:
            logger.critical("=" * 70)
            logger.critical("🚨 SAFEGUARD TRIGGERED: Mass page removal prevented!")
            logger.critical(
                f"   Would remove {len(removed_live)} previously-live pages of "
                f"{old_live} ({removed_percent:.1f}%, threshold "
                f"{MAX_DELETION_PERCENT}%)."
            )
            logger.critical("   Likely a discovery failure. Aborting before write.")
            logger.critical(
                "   If this is a confirmed upstream removal, re-run the workflow "
                "manually with confirm_removals=true (DOCS_CONFIRM_REMOVALS=1)."
            )
            logger.critical("=" * 70)
            sys.exit(1)

    # Count pages actually fetched THIS run. sha256 alone is not evidence of a
    # live fetch — carry-forward copies old hashes into "stale" entries, so an
    # all-stale (100%-failed) run would pass a sha256-based count. The changelog
    # is excluded (GitHub-hosted; succeeds even in a total docs-site outage).
    ok_count = count_ok_doc_pages(new_pages)
    if ok_count < MIN_EXPECTED_FILES:
        logger.critical("=" * 70)
        logger.critical("🚨 SAFEGUARD TRIGGERED: Too few successfully fetched pages!")
        logger.critical(
            f"   Only {ok_count} of {len(new_pages)} documentation pages fetched OK "
            f"this run (fetch_status == \"ok\", changelog excluded; minimum "
            f"{MIN_EXPECTED_FILES}). Most fetches failed/stale — aborting."
        )
        logger.critical("=" * 70)
        sys.exit(1)

    # Stale-share ceiling. The ok-floor alone lets a run commit with hundreds of
    # carry-forward entries; the removal check above then treats those entries
    # as free to drop next run. Bounding the non-ok share per commit keeps the
    # two rules from combining into a silent mass loss across two runs.
    doc_count = count_doc_pages(new_pages)
    not_ok = doc_count - ok_count
    stale_percent = (not_ok / doc_count) * 100 if doc_count else 0.0
    if stale_percent > MAX_STALE_PERCENT:
        logger.critical("=" * 70)
        logger.critical("🚨 SAFEGUARD TRIGGERED: Too many stale/failed pages!")
        logger.critical(
            f"   {not_ok} of {doc_count} documentation pages are not ok "
            f"({stale_percent:.1f}%, ceiling {MAX_STALE_PERCENT}%). "
            f"Partial fetch outage — aborting before write."
        )
        logger.critical("=" * 70)
        sys.exit(1)

    logger.info(
        f"✅ Manifest transition validated: {len(new_pages)} pages "
        f"({ok_count} documentation pages fetched ok, {stale_percent:.1f}% stale/failed)"
    )
