"""Tests for llms.txt parsing and the discovery union (fully offline)."""

import sys
from pathlib import Path
from unittest.mock import MagicMock

import pytest
import requests

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

import fetcher.discovery
from fetcher.llms_txt import parse_llms_txt, discover_from_llms_txt
from fetcher.discovery import merge_discovery, discover_pages


# Real-format samples (trimmed) from the two properties, verified 2026-07.
CODE_LLMS_TXT = """# Claude Code Docs

> Official documentation for Claude Code.

## Docs

- [Use Claude Code with a screen reader](https://code.claude.com/docs/en/accessibility.md): Set up Claude Code for screen readers such as VoiceOver and NVDA.
- [How the agent loop works](https://code.claude.com/docs/en/agent-sdk/agent-loop.md): Understand the message lifecycle, tool execution, and architecture.
- [Agent SDK reference - Python](https://code.claude.com/docs/en/agent-sdk/python.md): Complete API reference for the Python Agent SDK.
"""

PLATFORM_LLMS_TXT = """# Anthropic Developer Documentation

## Available Languages on Website

- English (en) - 549 pages - /docs - Content included below
- German (Deutsch) (de) - 201 pages - /docs/de - Visit website for content

## Root URL

https://platform.claude.com

---

## English

### Messages

- [Overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.md) - Agent Skills
- [Features overview](https://platform.claude.com/docs/en/build-with-claude/overview.md)
"""


class TestParseLlmsTxt:
    def test_code_format_colon_separator(self):
        recs = parse_llms_txt(CODE_LLMS_TXT)
        assert len(recs) == 3
        first = recs[0]
        assert first["url"] == "https://code.claude.com/docs/en/accessibility"
        assert first["md_url"] == "https://code.claude.com/docs/en/accessibility.md"
        assert first["title"] == "Use Claude Code with a screen reader"
        assert first["description"].startswith("Set up Claude Code for screen readers")

    def test_url_is_md_stripped(self):
        recs = parse_llms_txt(CODE_LLMS_TXT)
        for r in recs:
            assert r["md_url"].endswith(".md")
            assert r["url"] + ".md" == r["md_url"]

    def test_platform_dash_separator_and_missing_description(self):
        recs = parse_llms_txt(PLATFORM_LLMS_TXT)
        by_url = {r["url"]: r for r in recs}

        overview = by_url["https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview"]
        assert overview["title"] == "Overview"
        assert overview["description"] == "Agent Skills"  # after " - " separator

        features = by_url["https://platform.claude.com/docs/en/build-with-claude/overview"]
        assert features["description"] is None  # no description present

    def test_non_link_preamble_is_ignored(self):
        # The language table ("- English (en) - 549 pages - /docs") and the bare
        # "Root URL" line are not [text](url.md) links and must not be parsed.
        recs = parse_llms_txt(PLATFORM_LLMS_TXT)
        assert len(recs) == 2
        for r in recs:
            assert r["md_url"].endswith(".md")
            assert r["url"].startswith("https://")

    def test_agent_sdk_pages_are_on_code_host(self):
        # Regression: agent-sdk lives on code.claude.com, not platform. This is the
        # coverage the old sitemap-only fetch lost (130 failures).
        recs = parse_llms_txt(CODE_LLMS_TXT)
        py = [r for r in recs if r["url"].endswith("/agent-sdk/python")]
        assert len(py) == 1
        assert py[0]["url"].startswith("https://code.claude.com/")


class TestMergeDiscovery:
    def test_union_merges_title_and_lastmod(self):
        llms = parse_llms_txt(CODE_LLMS_TXT)
        sitemap = [
            {"url": "https://code.claude.com/docs/en/accessibility", "lastmod": "2026-07-16T00:00:00Z"},
            {"url": "https://code.claude.com/docs/en/sitemap-only", "lastmod": "2026-07-01T00:00:00Z"},
        ]
        merged = merge_discovery(llms, sitemap)
        by_url = {p["url"]: p for p in merged}

        # Page in both sources: title from llms.txt, lastmod from sitemap.
        both = by_url["https://code.claude.com/docs/en/accessibility"]
        assert both["title"] == "Use Claude Code with a screen reader"
        assert both["lastmod"] == "2026-07-16T00:00:00Z"

        # llms-only page: no lastmod.
        llms_only = by_url["https://code.claude.com/docs/en/agent-sdk/python"]
        assert llms_only["lastmod"] is None
        assert llms_only["title"] is not None

        # sitemap-only page: present, title None, md_url synthesized.
        sm_only = by_url["https://code.claude.com/docs/en/sitemap-only"]
        assert sm_only["title"] is None
        assert sm_only["md_url"] == "https://code.claude.com/docs/en/sitemap-only.md"

    def test_union_size_and_sorted(self):
        llms = parse_llms_txt(CODE_LLMS_TXT)  # 3 pages
        sitemap = [
            {"url": "https://code.claude.com/docs/en/accessibility", "lastmod": None},  # overlap
            {"url": "https://code.claude.com/docs/en/extra", "lastmod": None},          # new
        ]
        merged = merge_discovery(llms, sitemap)
        urls = [p["url"] for p in merged]
        assert len(merged) == 4  # 3 llms + 1 sitemap-only
        assert urls == sorted(urls)

    def test_trailing_slash_normalized(self):
        llms = [{"url": "https://code.claude.com/docs/en/a/",
                 "md_url": "https://code.claude.com/docs/en/a.md", "title": "A", "description": None}]
        sitemap = [{"url": "https://code.claude.com/docs/en/a", "lastmod": "2026-01-01"}]
        merged = merge_discovery(llms, sitemap)
        assert len(merged) == 1  # same page despite trailing slash
        assert merged[0]["lastmod"] == "2026-01-01"


class TestAllowedDomains:
    """merge_discovery is the choke point: non-https / non-allowlisted records drop."""

    @staticmethod
    def _llms_record(url):
        return {"url": url, "md_url": url + ".md", "title": "T", "description": None}

    def test_http_url_dropped(self):
        merged = merge_discovery([self._llms_record("http://code.claude.com/docs/en/hooks")], [])
        assert merged == []

    def test_disallowed_host_dropped(self):
        merged = merge_discovery([self._llms_record("https://evil.example/docs/en/hooks")], [])
        assert merged == []

    def test_disallowed_sitemap_entry_dropped(self):
        merged = merge_discovery([], [{"url": "https://evil.example/docs/en/x", "lastmod": None}])
        assert merged == []

    def test_allowed_hosts_pass(self):
        records = [
            self._llms_record("https://code.claude.com/docs/en/hooks"),
            self._llms_record("https://platform.claude.com/docs/en/api/messages"),
            self._llms_record("https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG"),
        ]
        merged = merge_discovery(records, [])
        assert len(merged) == 3

    def test_bad_md_url_drops_record_even_with_good_url(self):
        rec = {"url": "https://code.claude.com/docs/en/hooks",
               "md_url": "https://evil.example/docs/en/hooks.md", "title": "T", "description": None}
        assert merge_discovery([rec], []) == []


class TestDiscoveryFailClosed:
    """A dead/empty discovery source must abort the run, not silently shrink the union."""

    @staticmethod
    def _session_for(responses):
        """Map url -> (status, text); anything else raises ConnectionError."""
        session = MagicMock()

        def get(url, **kwargs):
            if url not in responses:
                raise requests.ConnectionError(f"no route to {url}")
            status, text = responses[url]
            resp = MagicMock()
            resp.status_code = status
            resp.text = text
            resp.content = text.encode("utf-8")
            if status >= 400:
                resp.raise_for_status.side_effect = requests.HTTPError(f"{status}")
            else:
                resp.raise_for_status.return_value = None
            return resp

        session.get.side_effect = get
        return session

    def test_llms_source_error_aborts(self):
        session = self._session_for({"https://a.example/llms.txt": (200, CODE_LLMS_TXT)})
        with pytest.raises(RuntimeError, match="Discovery source failed"):
            discover_from_llms_txt(
                session, urls=["https://a.example/llms.txt", "https://b.example/llms.txt"]
            )

    def test_llms_source_http_error_aborts(self):
        session = self._session_for({"https://a.example/llms.txt": (500, "oops")})
        with pytest.raises(RuntimeError, match="Discovery source failed"):
            discover_from_llms_txt(session, urls=["https://a.example/llms.txt"])

    def test_llms_source_zero_entries_aborts(self):
        # File fetched fine but parsed to zero link entries (format drift) -> abort.
        session = self._session_for({"https://a.example/llms.txt": (200, "no links here " * 50)})
        with pytest.raises(RuntimeError, match="0 entries"):
            discover_from_llms_txt(session, urls=["https://a.example/llms.txt"])

    def test_all_llms_sources_healthy_passes(self):
        session = self._session_for({
            "https://a.example/llms.txt": (200, CODE_LLMS_TXT),
            "https://b.example/llms.txt": (200, PLATFORM_LLMS_TXT),
        })
        records = discover_from_llms_txt(
            session, urls=["https://a.example/llms.txt", "https://b.example/llms.txt"]
        )
        assert len(records) == 5  # 3 code + 2 platform

    def test_discover_pages_propagates_sitemap_failure(self, monkeypatch):
        # The old code swallowed sitemap failure and continued llms-only.
        monkeypatch.setattr(
            fetcher.discovery, "discover_from_llms_txt",
            lambda session: parse_llms_txt(CODE_LLMS_TXT),
        )

        def boom(session):
            raise RuntimeError("Discovery source failed: sitemap down")

        monkeypatch.setattr(fetcher.discovery, "discover_sitemap_entries", boom)
        with pytest.raises(RuntimeError, match="sitemap down"):
            discover_pages(MagicMock())
