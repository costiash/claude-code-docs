"""v2 fetcher unit tests: paths, manifest, carry-forward, collisions, safeguards."""

import json
import sys
from pathlib import Path
from unittest.mock import MagicMock

import pytest
import requests

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from fetcher.paths import url_to_filename, categorize_from_url, page_id_from_filename
from fetcher.manifest import load_manifest, pages_by_url, build_manifest, save_manifest
from fetcher.content import validate_markdown_content, extract_title, fetch_markdown
from fetcher.safeguards import validate_discovery_threshold, validate_manifest_transition
from fetcher.cli import build_page_entry, check_no_filename_collisions


class TestUrlToFilename:
    def test_code_host_flat_page(self):
        assert url_to_filename("https://code.claude.com/docs/en/hooks") == "claude-code__hooks.md"

    def test_code_host_nested_uses_full_subpath(self):
        # Full sub-path, not last segment — prevents agent-sdk/overview vs overview collision.
        assert (
            url_to_filename("https://code.claude.com/docs/en/agent-sdk/python")
            == "claude-code__agent-sdk__python.md"
        )

    def test_platform_host(self):
        assert (
            url_to_filename("https://platform.claude.com/docs/en/api/messages")
            == "docs__en__api__messages.md"
        )

    def test_trailing_slash_stripped(self):
        assert url_to_filename("https://code.claude.com/docs/en/hooks/") == "claude-code__hooks.md"

    def test_no_collision_between_nested_and_flat(self):
        a = url_to_filename("https://code.claude.com/docs/en/agent-sdk/overview")
        b = url_to_filename("https://code.claude.com/docs/en/overview")
        assert a != b

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            url_to_filename("https://code.claude.com/docs/en/")


class TestCategorizeFromUrl:
    @pytest.mark.parametrize("url,expected", [
        ("https://code.claude.com/docs/en/hooks", "claude_code"),
        ("https://code.claude.com/docs/en/agent-sdk/python", "agent_sdk"),
        ("https://platform.claude.com/docs/en/api/messages", "api_reference"),
        ("https://platform.claude.com/docs/en/agents-and-tools/mcp-connector", "agents_and_tools"),
        ("https://platform.claude.com/docs/en/about-claude/models", "about_claude"),
        ("https://platform.claude.com/docs/en/build-with-claude/vision", "core_documentation"),
        ("https://platform.claude.com/docs/en/test-and-evaluate/eval-tool", "test_and_evaluate"),
        ("https://platform.claude.com/docs/en/resources/prompt-library/code-clarifier", "prompt_library"),
        ("https://platform.claude.com/docs/en/resources/overview", "resources"),
        ("https://platform.claude.com/docs/en/release-notes/api", "release_notes"),
        ("https://platform.claude.com/docs/en/get-started", "get_started"),
    ])
    def test_routing(self, url, expected):
        assert categorize_from_url(url) == expected


class TestPageId:
    def test_derived_from_filename(self):
        assert page_id_from_filename("claude-code__hooks.md") == "claude-code/hooks"
        assert page_id_from_filename("docs__en__api__messages.md") == "docs/en/api/messages"


class TestManifest:
    def test_load_missing_returns_empty_v2(self, tmp_path):
        m = load_manifest(tmp_path / "nope.json")
        assert m["schema_version"] == 2
        assert m["pages"] == []

    def test_load_v1_treated_as_empty(self, tmp_path):
        # Legacy {metadata, categories} must NOT be read as v2 (first-run-safe).
        p = tmp_path / "paths_manifest.json"
        p.write_text(json.dumps({"metadata": {}, "categories": {"api_reference": ["/en/api/x"]}}))
        m = load_manifest(p)
        assert m["pages"] == []

    def test_load_v2_roundtrip(self, tmp_path):
        p = tmp_path / "paths_manifest.json"
        pages = [
            {"id": "claude-code/hooks", "filename": "claude-code__hooks.md",
             "url": "https://code.claude.com/docs/en/hooks", "md_url": "https://code.claude.com/docs/en/hooks.md",
             "title": "Hooks", "category": "claude_code", "sha256": "abc", "lastmod": None, "fetch_status": "ok"},
        ]
        save_manifest(p, build_manifest(pages, sources=["s1"]))
        loaded = load_manifest(p)
        assert loaded["schema_version"] == 2
        assert len(loaded["pages"]) == 1
        assert loaded["sources"] == ["s1"]

    def test_build_manifest_sorts_by_id(self):
        pages = [{"id": "b", "url": "u2"}, {"id": "a", "url": "u1"}]
        m = build_manifest(pages, sources=[])
        assert [p["id"] for p in m["pages"]] == ["a", "b"]

    def test_pages_by_url(self):
        m = {"pages": [{"url": "u1", "id": "a"}, {"url": "u2", "id": "b"}]}
        idx = pages_by_url(m)
        assert set(idx) == {"u1", "u2"}


class TestContentValidation:
    def test_rejects_html(self):
        with pytest.raises(ValueError):
            validate_markdown_content("<!DOCTYPE html><html>...", "x.md")

    def test_rejects_too_short(self):
        with pytest.raises(ValueError):
            validate_markdown_content("# Hi", "x.md")

    def test_accepts_markdown(self):
        md = "# Title\n\nSome **content** about claude code.\n\n## Section\n\n- item\n- item\n"
        validate_markdown_content(md, "x.md")  # no raise

    def test_extract_title(self):
        assert extract_title("# Hooks\n\nbody") == "Hooks"
        assert extract_title("no heading here") == "Untitled"


class TestFetchMarkdown:
    def _session(self, status=200, text="# Doc\n\nlots of **markdown** content about claude code here\n\n- a\n- b"):
        session = MagicMock()
        resp = MagicMock()
        resp.status_code = status
        resp.text = text
        if status >= 400:
            resp.raise_for_status.side_effect = requests.HTTPError(f"{status}")
        else:
            resp.raise_for_status.return_value = None
        session.get.return_value = resp
        return session

    def test_success(self):
        content = fetch_markdown("https://code.claude.com/docs/en/hooks.md", self._session(), "hooks")
        assert "markdown" in content

    def test_failure_raises_after_retries(self, monkeypatch):
        monkeypatch.setattr("time.sleep", lambda *_: None)  # no real backoff
        with pytest.raises(Exception):
            fetch_markdown("https://code.claude.com/docs/en/x.md", self._session(status=404), "x")


class TestCarryForward:
    """build_page_entry: fetch fail + prev entry -> stale; no prev -> failed."""

    def _failing_session(self, monkeypatch):
        monkeypatch.setattr("time.sleep", lambda *_: None)
        session = MagicMock()
        resp = MagicMock()
        resp.status_code = 500
        resp.raise_for_status.side_effect = requests.HTTPError("500")
        session.get.return_value = resp
        return session

    def test_fetch_fail_with_prev_is_stale(self, monkeypatch, tmp_path):
        session = self._failing_session(monkeypatch)
        raw = {"url": "https://code.claude.com/docs/en/hooks",
               "md_url": "https://code.claude.com/docs/en/hooks.md", "title": "Hooks", "lastmod": None}
        old_by_url = {"https://code.claude.com/docs/en/hooks": {"sha256": "OLDHASH", "title": "Hooks"}}
        entry = build_page_entry(raw, "claude-code__hooks.md", session, tmp_path, old_by_url)
        assert entry["fetch_status"] == "stale"
        assert entry["sha256"] == "OLDHASH"

    def test_fetch_fail_no_prev_is_failed(self, monkeypatch, tmp_path):
        session = self._failing_session(monkeypatch)
        raw = {"url": "https://code.claude.com/docs/en/newpage",
               "md_url": "https://code.claude.com/docs/en/newpage.md", "title": "New", "lastmod": None}
        entry = build_page_entry(raw, "claude-code__newpage.md", session, tmp_path, {})
        assert entry["fetch_status"] == "failed"
        assert entry["sha256"] is None


class TestCollisionCheck:
    def test_raises_on_collision(self):
        # The v2 scheme is collision-free by construction; simulate by duplicating a URL.
        pages = [
            {"url": "https://code.claude.com/docs/en/hooks"},
            {"url": "https://code.claude.com/docs/en/hooks"},
        ]
        with pytest.raises(ValueError, match="collision"):
            check_no_filename_collisions(pages)

    def test_no_collision_ok(self):
        pages = [
            {"url": "https://code.claude.com/docs/en/hooks"},
            {"url": "https://code.claude.com/docs/en/mcp"},
        ]
        assert check_no_filename_collisions(pages) == ["claude-code__hooks.md", "claude-code__mcp.md"]


class TestSafeguards:
    def test_discovery_threshold_ok(self):
        pages = [{"url": f"u{i}"} for i in range(250)]
        assert validate_discovery_threshold(pages) is pages

    def test_discovery_threshold_aborts(self):
        with pytest.raises(SystemExit):
            validate_discovery_threshold([{"url": "u"}])

    def test_transition_first_run_passes(self):
        new = [{"url": f"u{i}"} for i in range(300)]
        validate_manifest_transition({"pages": []}, new)  # no raise

    def test_transition_mass_removal_aborts(self):
        old = {"pages": [{"url": f"u{i}"} for i in range(300)]}
        new = [{"url": f"u{i}"} for i in range(260)]  # removed 40/300 = 13% > 10%
        with pytest.raises(SystemExit):
            validate_manifest_transition(old, new)

    def test_transition_below_floor_aborts(self):
        old = {"pages": [{"url": f"u{i}"} for i in range(300)]}
        new = [{"url": f"u{i}"} for i in range(240)]  # < 250 floor
        with pytest.raises(SystemExit):
            validate_manifest_transition(old, new)
