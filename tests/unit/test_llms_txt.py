"""Tests for llms.txt parsing and the discovery union (fully offline)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from fetcher.llms_txt import parse_llms_txt
from fetcher.discovery import merge_discovery


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
        llms = [{"url": "https://x/docs/en/a/", "md_url": "https://x/docs/en/a.md", "title": "A", "description": None}]
        sitemap = [{"url": "https://x/docs/en/a", "lastmod": "2026-01-01"}]
        merged = merge_discovery(llms, sitemap)
        assert len(merged) == 1  # same page despite trailing slash
        assert merged[0]["lastmod"] == "2026-01-01"
