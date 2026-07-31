"""
Parse Anthropic llms.txt files into discovery records.

Both properties publish an llms.txt (a markdown list, one link per page):

    ## Docs
    - [Title](https://code.claude.com/docs/en/hooks.md): Description text.
    - [Overview](https://platform.claude.com/docs/en/build-with-claude/overview.md) - Agent Skills
    - [Features overview](https://platform.claude.com/docs/en/build-with-claude/overview.md)

Notes on the real-world format (verified 2026-07):
- code.claude.com uses a ``: `` separator before the description.
- platform.claude.com uses a `` - `` separator, and some entries have no description.
- URLs point directly at the ``.md`` twin, with the correct host. This is why we
  store URLs verbatim from here instead of reconstructing them from a base_url:
  it structurally fixes the old CLI-URL bug and covers agent-sdk pages the
  sitemap-only fetch failed on.
- platform's llms.txt contains non-link preamble (a language table, a "Root URL"
  block). Those lines are not ``[text](url.md)`` links, so the regex ignores them.

The pure parser (:func:`parse_llms_txt`) is offline-testable; the network wrapper
(:func:`discover_from_llms_txt`) fetches the real files.
"""

import re
from typing import Dict, List, Optional

import requests

from .config import HEADERS, LLMS_TXT_URLS, logger

# A markdown list entry linking to a .md page, with an optional description that
# may follow either a ":" (code.claude.com) or "-" (platform.claude.com) separator.
_ENTRY_RE = re.compile(
    r"^\s*[-*]\s*"                              # list bullet
    r"\[(?P<title>[^\]]+)\]"                    # [title]
    r"\((?P<md_url>https?://[^)\s]+\.md)\)"     # (https://host/path.md)
    r"\s*(?:[:\-]\s*(?P<desc>.*\S))?\s*$"       # optional ": desc" or "- desc"
)


def parse_llms_txt(text: str) -> List[Dict[str, Optional[str]]]:
    """
    Parse llms.txt content into a list of page records.

    Args:
        text: Raw llms.txt file content.

    Returns:
        List of ``{url, md_url, title, description}`` dicts, one per link entry.
        ``url`` is the canonical page URL (the ``.md`` stripped). ``description``
        is ``None`` when the entry has none. Non-link lines are ignored.
    """
    records: List[Dict[str, Optional[str]]] = []
    for line in text.splitlines():
        m = _ENTRY_RE.match(line)
        if not m:
            continue
        md_url = m.group("md_url")
        url = md_url[:-3] if md_url.endswith(".md") else md_url
        desc = (m.group("desc") or "").strip() or None
        records.append(
            {
                "url": url,
                "md_url": md_url,
                "title": m.group("title").strip(),
                "description": desc,
            }
        )
    return records


def discover_from_llms_txt(
    session: requests.Session, urls: Optional[List[str]] = None
) -> List[Dict[str, Optional[str]]]:
    """
    Fetch and parse the configured llms.txt files.

    A failure on one source is logged and skipped (the sitemap union still
    provides coverage); it does not abort discovery.

    Args:
        session: Requests session for connection pooling.
        urls: Override list of llms.txt URLs (defaults to ``LLMS_TXT_URLS``).

    Returns:
        Combined list of page records across all sources (may contain
        duplicates across sources; de-duplication happens in the discovery union).
    """
    if urls is None:
        urls = LLMS_TXT_URLS

    records: List[Dict[str, Optional[str]]] = []
    for url in urls:
        try:
            response = session.get(url, headers=HEADERS, timeout=30)
            response.raise_for_status()
            parsed = parse_llms_txt(response.text)
            if not parsed and len(response.text.strip()) > 200:
                # The file downloaded fine but matched zero link entries — almost
                # certainly upstream format drift. Without this, discovery silently
                # degrades to sitemap-only (llms-only pages drop, titles -> Untitled).
                logger.warning(
                    f"llms.txt {url}: 0 entries parsed from {len(response.text)} bytes "
                    "— possible format drift; the _ENTRY_RE regex may need updating."
                )
            logger.info(f"llms.txt {url}: parsed {len(parsed)} entries")
            records.extend(parsed)
        except Exception as e:
            logger.warning(f"Failed to fetch/parse llms.txt {url}: {e}")
    return records
