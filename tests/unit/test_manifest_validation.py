"""Structural validation of the real committed v2 manifest + search index."""

import json
from pathlib import Path
from urllib.parse import urlparse

import pytest

PROJECT_ROOT = Path(__file__).parent.parent.parent
MANIFEST = PROJECT_ROOT / "paths_manifest.json"
SEARCH_INDEX = PROJECT_ROOT / "search_index.json"

CATEGORY_VOCAB = {
    "claude_code", "agent_sdk", "api_reference", "agents_and_tools", "about_claude",
    "core_documentation", "get_started", "test_and_evaluate", "prompt_library",
    "resources", "release_notes",
}
REQUIRED_PAGE_FIELDS = {"id", "filename", "url", "md_url", "title", "category", "sha256", "lastmod", "fetch_status"}
FORBIDDEN_INDEX_FIELDS = {"content_preview", "preview", "file_path", "keywords", "positions", "ngrams"}


@pytest.fixture(scope="module")
def manifest():
    if not MANIFEST.exists():
        pytest.skip("paths_manifest.json not present (run the fetcher first)")
    data = json.loads(MANIFEST.read_text())
    if data.get("schema_version") != 2:
        pytest.skip("paths_manifest.json is not v2 yet (run the v2 fetcher first)")
    return data


class TestManifestV2:
    def test_schema_and_sources(self, manifest):
        assert manifest["schema_version"] == 2
        assert isinstance(manifest["pages"], list)
        assert manifest.get("sources")

    def test_min_pages(self, manifest):
        assert len(manifest["pages"]) >= 250

    def test_required_fields(self, manifest):
        for p in manifest["pages"]:
            assert REQUIRED_PAGE_FIELDS <= set(p.keys()), p.get("filename")

    def test_categories_in_vocabulary(self, manifest):
        for p in manifest["pages"]:
            assert p["category"] in CATEGORY_VOCAB, f"{p['url']} -> {p['category']}"

    def test_no_duplicate_ids_or_filenames_or_urls(self, manifest):
        for key in ("id", "filename", "url"):
            values = [p[key] for p in manifest["pages"]]
            assert len(values) == len(set(values)), f"duplicate {key}"

    def test_code_host_pages_have_code_urls(self, manifest):
        """Regression: pages on code.claude.com must record code.claude.com URLs
        (the old CLI-URL bug wrote platform.claude.com URLs for them)."""
        for p in manifest["pages"]:
            if p["filename"].startswith("claude-code__"):
                host = urlparse(p["url"]).netloc
                assert host == "code.claude.com", f"{p['filename']} -> {host}"

    def test_hooks_spot_check(self, manifest):
        hooks = [p for p in manifest["pages"] if p["id"] == "claude-code/hooks"]
        assert hooks, "claude-code/hooks missing"
        assert hooks[0]["url"] == "https://code.claude.com/docs/en/hooks"
        assert hooks[0]["md_url"] == "https://code.claude.com/docs/en/hooks.md"

    def test_agent_sdk_present_on_code_host(self, manifest):
        agent = [p for p in manifest["pages"] if p["category"] == "agent_sdk"]
        assert len(agent) >= 20, "agent-sdk block should be recovered via llms.txt union"
        for p in agent[:5]:
            assert urlparse(p["url"]).netloc == "code.claude.com"


class TestSearchIndexV2:
    @pytest.fixture(scope="class")
    def index(self):
        if not SEARCH_INDEX.exists():
            pytest.skip("search_index.json not present (run build_search_index.py first)")
        data = json.loads(SEARCH_INDEX.read_text())
        if data.get("schema_version") != 2:
            pytest.skip("search_index.json is not v2 yet")
        return data

    def test_schema(self, index):
        assert index["schema_version"] == 2
        assert isinstance(index["pages"], list)

    def test_no_forbidden_fields(self, index):
        for p in index["pages"]:
            assert not (set(p.keys()) & FORBIDDEN_INDEX_FIELDS), p.get("filename")

    def test_covers_manifest(self, index, manifest):
        assert len(index["pages"]) == len(manifest["pages"])
