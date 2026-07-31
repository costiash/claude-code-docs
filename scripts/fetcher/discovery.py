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

import requests

from .config import logger
from .llms_txt import discover_from_llms_txt
from .sitemap import discover_sitemap_entries


def _canonical(url: str) -> str:
    """Normalize a page URL for use as the union key (drop trailing slash)."""
    return url.rstrip("/")


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

    return [pages[url] for url in sorted(pages)]


def discover_pages(session: requests.Session) -> List[Dict[str, Optional[str]]]:
    """
    Run full v2 discovery: fetch both sources and return their union.

    Args:
        session: Requests session for connection pooling.

    Returns:
        The canonical page set as ``{url, md_url, title, lastmod}`` dicts.
    """
    llms_records = discover_from_llms_txt(session)
    try:
        sitemap_entries = discover_sitemap_entries(session)
    except Exception as e:
        # A sitemap outage must not abort the run when llms.txt carried the union
        # (symmetric with discover_from_llms_txt, which already tolerates failure).
        # If BOTH sources come back empty, validate_discovery_threshold aborts.
        logger.warning(f"Sitemap discovery failed ({e}); continuing with llms.txt only.")
        sitemap_entries = []
    merged = merge_discovery(llms_records, sitemap_entries)
    logger.info(
        f"Discovery union: {len(llms_records)} llms.txt + "
        f"{len(sitemap_entries)} sitemap -> {len(merged)} unique pages"
    )
    return merged
