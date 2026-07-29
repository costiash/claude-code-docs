"""Validation: the real v2 manifest is internally consistent with discovery + mapping."""

import json
import sys
from pathlib import Path
from urllib.parse import urlparse

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from fetcher.paths import url_to_filename

PROJECT_ROOT = Path(__file__).parent.parent.parent
MANIFEST = PROJECT_ROOT / "paths_manifest.json"

PAGE_HOSTS = {"code.claude.com", "platform.claude.com"}
MD_HOSTS = {"code.claude.com", "platform.claude.com", "raw.githubusercontent.com"}


@pytest.fixture(scope="module")
def manifest():
    if not MANIFEST.exists():
        pytest.skip("paths_manifest.json not present")
    data = json.loads(MANIFEST.read_text())
    if data.get("schema_version") != 2:
        pytest.skip("paths_manifest.json is not v2 yet")
    return data


@pytest.mark.integration
class TestManifestConsistency:
    def test_sources_are_the_expected_discovery_urls(self, manifest):
        sources = set(manifest["sources"])
        assert "https://code.claude.com/docs/llms.txt" in sources
        assert "https://platform.claude.com/llms.txt" in sources
        assert "https://code.claude.com/docs/sitemap.xml" in sources
        assert "https://platform.claude.com/sitemap.xml" in sources

    def test_page_url_hosts_allowed(self, manifest):
        for p in manifest["pages"]:
            if p["id"] == "changelog":
                continue
            assert urlparse(p["url"]).netloc in PAGE_HOSTS, p["url"]

    def test_md_url_hosts_allowed(self, manifest):
        for p in manifest["pages"]:
            assert urlparse(p["md_url"]).netloc in MD_HOSTS, p["md_url"]

    def test_filename_matches_mapping(self, manifest):
        """Every non-changelog page's filename must equal url_to_filename(url)."""
        for p in manifest["pages"]:
            if p["id"] == "changelog":
                continue
            assert p["filename"] == url_to_filename(p["url"]), p["url"]

    def test_id_matches_filename(self, manifest):
        for p in manifest["pages"]:
            stem = p["filename"][:-3] if p["filename"].endswith(".md") else p["filename"]
            assert p["id"] == stem.replace("__", "/"), p["filename"]

    def test_fetch_status_values(self, manifest):
        for p in manifest["pages"]:
            assert p["fetch_status"] in {"ok", "stale", "failed"}
