"""
Sitemap discovery and parsing functionality.

This module handles:
- Discovering sitemaps from multiple URLs
- Parsing XML sitemaps safely (XXE prevention)
- Extracting English documentation paths
"""

import re
import xml.etree.ElementTree as ET
from typing import Dict, List, Optional
from urllib.parse import urlparse

import requests

from .config import SITEMAP_URLS, logger
from .content import discovery_get


def discover_sitemap_entries(
    session: requests.Session, urls: Optional[List[str]] = None
) -> List[Dict[str, Optional[str]]]:
    """
    Discover English documentation pages from all sitemaps as full URLs + lastmod.

    Keeps the verbatim ``<loc>`` URL so the host is preserved (unlike the
    mirror-era path-only discovery this replaced), and captures ``<lastmod>``
    when present. This is the v2 discovery primitive.

    FAIL CLOSED per source: each configured sitemap must fetch, parse, and yield
    at least one English page, or the whole run aborts. Silently tolerating a
    dead source would shrink the union by that source's exclusive pages — a loss
    the 10% deletion threshold cannot always catch.

    Args:
        session: Requests session for connection pooling.
        urls: Override list of sitemap URLs (defaults to ``SITEMAP_URLS``).

    Returns:
        List of ``{url, lastmod}`` dicts (``lastmod`` is ``None`` when the sitemap
        omits it — platform.claude.com's sitemap has no lastmod). De-duplicated by
        canonical URL and sorted.

    Raises:
        RuntimeError: If any configured sitemap fails or yields zero pages.
    """
    if urls is None:
        urls = SITEMAP_URLS

    namespace = {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    entries: Dict[str, Optional[str]] = {}

    for sitemap_url in urls:
        try:
            logger.info(f"Discovering sitemap entries from: {sitemap_url}")
            # Retried GET (same budget as page fetches): fail-closed stays, but a
            # single transient blip no longer aborts the whole 3-hourly run.
            response = discovery_get(session, sitemap_url)
            root = _parse_xml_safely(response.content)
        except Exception as e:
            raise RuntimeError(
                f"Discovery source failed: sitemap {sitemap_url}: {e} — "
                f"aborting the run (a dead source must not silently drop its pages)."
            ) from e

        source_pages = 0
        url_elems = root.findall(".//ns:url", namespace) or root.findall(".//url")
        for url_elem in url_elems:
            loc_elem = url_elem.find("ns:loc", namespace)
            if loc_elem is None:
                loc_elem = url_elem.find("loc")
            if loc_elem is None or not loc_elem.text:
                continue

            parsed = urlparse(loc_elem.text.strip())
            path = parsed.path
            if path.endswith(".html"):
                path = path[:-5]
            path = path.rstrip("/")

            # English documentation pages only (exclude /de/, /fr/, ... and non-doc URLs)
            if not (path.startswith("/docs/en/") or path.startswith("/en/")):
                continue
            if any(skip in path for skip in ("/examples/", "/legacy/")):
                continue

            canonical = f"{parsed.scheme}://{parsed.netloc}{path}"

            lastmod_elem = url_elem.find("ns:lastmod", namespace)
            if lastmod_elem is None:
                lastmod_elem = url_elem.find("lastmod")
            lastmod = (
                lastmod_elem.text.strip()
                if lastmod_elem is not None and lastmod_elem.text
                else None
            )

            # First occurrence wins, but prefer a real lastmod over None.
            if canonical not in entries or (entries[canonical] is None and lastmod):
                entries[canonical] = lastmod
            source_pages += 1

        if source_pages == 0:
            raise RuntimeError(
                f"Discovery source failed: sitemap {sitemap_url} yielded zero English "
                f"documentation pages — aborting the run (fail closed)."
            )
        logger.info(f"  {sitemap_url}: {source_pages} English pages")

    if not entries:
        raise RuntimeError("Could not discover any entries from sitemaps")

    result = [{"url": url, "lastmod": entries[url]} for url in sorted(entries)]
    logger.info(f"Discovered {len(result)} English sitemap entries (with lastmod where available)")
    return result


def _parse_xml_safely(content: bytes) -> ET.Element:
    """
    Parse XML content safely, rejecting DTD/entity declarations (XXE / billion
    laughs defense).

    Stdlib ``ET.XMLParser`` has no ``forbid_dtd``-style kwargs (those belong to
    defusedxml), so the defense is a pre-parse content check: any ``<!DOCTYPE``
    or ``<!ENTITY`` anywhere in the document rejects it outright. The scan must
    cover the FULL content, not a fixed-size prefix: XML permits arbitrary
    comments before the DOCTYPE, so a bounded prefix check is bypassable with
    padding. Neither token can appear legitimately in a sitemap (``<`` inside
    element text/attributes must be escaped as ``&lt;``), so this loses nothing.

    Args:
        content: Raw XML content bytes

    Returns:
        Parsed XML root element

    Raises:
        ValueError: If the content contains a DTD or entity declaration.
    """
    if re.search(rb'<!(?:doctype|entity)', content, re.IGNORECASE):
        logger.error(
            "Rejecting XML containing a DTD/ENTITY declaration "
            "(possible XXE / billion-laughs payload) — sitemaps never declare DTDs."
        )
        raise ValueError("XML contains DTD/ENTITY declaration; refusing to parse")
    return ET.fromstring(content)
