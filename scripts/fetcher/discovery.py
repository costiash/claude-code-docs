"""
Union discovery: merge llms.txt + sitemap into one canonical page set.

The v2 page set is the **union** of two sources, keyed by canonical URL:

- ``llms.txt`` (:mod:`fetcher.llms_txt`) supplies ``title`` and the verbatim
  ``.md`` URL, and covers pages the old sitemap-only fetch missed.
- the sitemaps (:func:`fetcher.sitemap.discover_sitemap_entries`) supply
  ``lastmod``, and any page not listed in llms.txt.

Producing the *discovery result* (not a successful-fetches-only list) is what
lets A2's manifest carry forward stale entries instead of dropping pages that
briefly fail to fetch.

Each record is intentionally minimal — ``{url, md_url, title, lastmod}``.
Filename / id / category enrichment and content hashing happen in the manifest
build (A2), keeping this module purely about *which pages exist*.
"""

from typing import Dict, List, Optional
from urllib.parse import urlparse

import requests

from .config import ALLOWED_DOMAINS, logger
from .llms_txt import discover_from_llms_txt
from .sitemap import discover_sitemap_entries


def _canonical(url: str) -> str:
    """Normalize a page URL for use as the union key (drop trailing slash)."""
    return url.rstrip("/")


def _url_allowed(url: Optional[str]) -> bool:
    """True if the URL is https and its host is in ``ALLOWED_DOMAINS``."""
    if not url:
        return False
    parsed = urlparse(url)
    return parsed.scheme == "https" and parsed.hostname in ALLOWED_DOMAINS


def _filter_allowed(pages: List[Dict[str, Optional[str]]]) -> List[Dict[str, Optional[str]]]:
    """
    Enforce ``ALLOWED_DOMAINS`` at the single choke point where records enter
    the pipeline: drop (loudly) any record whose ``url`` or ``md_url`` is not
    https on an allowed host. A poisoned upstream source (llms.txt/sitemap
    injection) must never make the fetcher request — or the manifest publish —
    an attacker-controlled URL.
    """
    kept = []
    for page in pages:
        if _url_allowed(page.get("url")) and _url_allowed(page.get("md_url")):
            kept.append(page)
        else:
            logger.error(
                f"DROPPED disallowed discovery record: url={page.get('url')!r} "
                f"md_url={page.get('md_url')!r} — scheme must be https and host "
                f"in ALLOWED_DOMAINS {ALLOWED_DOMAINS}."
            )
    return kept


def merge_discovery(
    llms_records: List[Dict], sitemap_entries: List[Dict]
) -> List[Dict[str, Optional[str]]]:
    """
    Union llms.txt records with sitemap entries, keyed by canonical URL.

    Args:
        llms_records: Output of :func:`fetcher.llms_txt.parse_llms_txt` /
            ``discover_from_llms_txt`` (each has ``url``, ``md_url``, ``title``).
        sitemap_entries: Output of
            :func:`fetcher.sitemap.discover_sitemap_entries` (each has ``url``,
            ``lastmod``).

    Returns:
        Sorted list of ``{url, md_url, title, lastmod}`` dicts. ``title`` is
        ``None`` for pages present only in the sitemap; ``lastmod`` is ``None``
        for pages present only in llms.txt (or whose sitemap omitted it).
        Records with a non-https or non-``ALLOWED_DOMAINS`` url/md_url are
        dropped (and logged) — see :func:`_filter_allowed`.
    """
    pages: Dict[str, Dict[str, Optional[str]]] = {}

    for record in llms_records:
        url = _canonical(record["url"])
        # llms.txt is the richer source; if a URL appears twice, keep the first title.
        if url not in pages:
            pages[url] = {
                "url": url,
                "md_url": record.get("md_url") or url + ".md",
                "title": record.get("title"),
                "lastmod": None,
            }

    for entry in sitemap_entries:
        url = _canonical(entry["url"])
        if url in pages:
            pages[url]["lastmod"] = entry.get("lastmod")
        else:
            pages[url] = {
                "url": url,
                "md_url": url + ".md",
                "title": None,
                "lastmod": entry.get("lastmod"),
            }

    return _filter_allowed([pages[url] for url in sorted(pages)])


def discover_pages(session: requests.Session) -> List[Dict[str, Optional[str]]]:
    """
    Run full v2 discovery: fetch both sources and return their union.

    FAIL CLOSED: any configured discovery source (llms.txt or sitemap) that
    errors or yields zero pages aborts the run (RuntimeError → non-zero exit
    before any write). Tolerating a dead source silently shrinks the union by
    that source's exclusive pages — a loss the 10% deletion threshold cannot
    reliably catch.

    Args:
        session: Requests session for connection pooling.

    Returns:
        The canonical page set as ``{url, md_url, title, lastmod}`` dicts.

    Raises:
        RuntimeError: If any discovery source fails or comes back empty.
    """
    llms_records = discover_from_llms_txt(session)
    sitemap_entries = discover_sitemap_entries(session)
    merged = merge_discovery(llms_records, sitemap_entries)
    logger.info(
        f"Discovery union: {len(llms_records)} llms.txt + "
        f"{len(sitemap_entries)} sitemap -> {len(merged)} unique pages"
    )
    return merged
