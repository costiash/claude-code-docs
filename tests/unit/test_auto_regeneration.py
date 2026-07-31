"""v2 manifest-regeneration invariants: determinism, uniqueness, category vocabulary."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from fetcher.discovery import merge_discovery
from fetcher.paths import url_to_filename, page_id_from_filename, categorize_from_url
from fetcher.manifest import build_manifest

# The closed category vocabulary (mirrors plugin/skills/claude-docs/manifest-reference.md).
CATEGORY_VOCAB = {
    "claude_code", "agent_sdk", "api_reference", "agents_and_tools", "about_claude",
    "core_documentation", "get_started", "test_and_evaluate", "prompt_library",
    "resources", "release_notes",
}

SAMPLE_URLS = [
    "https://code.claude.com/docs/en/hooks",
    "https://code.claude.com/docs/en/agent-sdk/python",
    "https://code.claude.com/docs/en/agent-sdk/overview",
    "https://platform.claude.com/docs/en/api/messages",
    "https://platform.claude.com/docs/en/agents-and-tools/mcp-connector",
    "https://platform.claude.com/docs/en/about-claude/models",
    "https://platform.claude.com/docs/en/build-with-claude/vision",
    "https://platform.claude.com/docs/en/resources/prompt-library/code-clarifier",
]


def _enrich(url):
    """Mirror cli.py enrichment without the network fetch."""
    filename = url_to_filename(url)
    return {
        "id": page_id_from_filename(filename),
        "filename": filename,
        "url": url,
        "md_url": url + ".md",
        "title": None,
        "category": categorize_from_url(url),
        "sha256": None,
        "lastmod": None,
        "fetch_status": "failed",
    }


class TestRegeneration:
    def _manifest(self):
        pages = [_enrich(u) for u in SAMPLE_URLS]
        return build_manifest(pages, sources=["s"])

    def test_sorted_by_id(self):
        m = self._manifest()
        ids = [p["id"] for p in m["pages"]]
        assert ids == sorted(ids)

    def test_unique_ids_and_filenames(self):
        m = self._manifest()
        ids = [p["id"] for p in m["pages"]]
        filenames = [p["filename"] for p in m["pages"]]
        assert len(ids) == len(set(ids))
        assert len(filenames) == len(set(filenames))

    def test_categories_within_vocabulary(self):
        m = self._manifest()
        for p in m["pages"]:
            assert p["category"] in CATEGORY_VOCAB, f"{p['url']} -> {p['category']}"

    def test_required_fields_present(self):
        m = self._manifest()
        required = {"id", "filename", "url", "md_url", "title", "category", "sha256", "lastmod", "fetch_status"}
        for p in m["pages"]:
            assert required <= set(p.keys())

    def test_deterministic_ignoring_timestamp(self):
        a = self._manifest()
        b = self._manifest()
        assert a["pages"] == b["pages"]  # generated_at differs, pages identical

    def test_nested_and_flat_do_not_collide(self):
        # agent-sdk/overview and (a hypothetical) top-level overview stay distinct.
        m = self._manifest()
        filenames = {p["filename"] for p in m["pages"]}
        assert "claude-code__agent-sdk__overview.md" in filenames


class TestDiscoveryUnionRegen:
    def test_union_then_manifest(self):
        llms = [
            {"url": u, "md_url": u + ".md", "title": f"T{i}", "description": None}
            for i, u in enumerate(SAMPLE_URLS)
        ]
        sitemap = [{"url": SAMPLE_URLS[0], "lastmod": "2026-07-01"}]
        merged = merge_discovery(llms, sitemap)
        assert len(merged) == len(SAMPLE_URLS)
        # lastmod flows from sitemap onto the matching page.
        hooks = next(p for p in merged if p["url"] == SAMPLE_URLS[0])
        assert hooks["lastmod"] == "2026-07-01"
