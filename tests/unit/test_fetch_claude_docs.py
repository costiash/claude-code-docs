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
from fetcher.content import (
    validate_markdown_content,
    extract_title,
    fetch_markdown,
    save_markdown_file,
    _retry_after_seconds,
)
from fetcher.safeguards import validate_discovery_threshold, validate_manifest_transition
from fetcher.cli import (
    build_page_entry,
    map_pages_to_filenames,
    count_ok_doc_pages,
    validate_fetch_success,
    parse_fetch_limit,
)


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

    def test_load_corrupt_fails_closed(self, tmp_path):
        # A truncated/unparseable EXISTING manifest must abort, not read as a clean
        # first run (which would skip the mass-deletion transition guard).
        p = tmp_path / "paths_manifest.json"
        p.write_text('{"schema_version": 2, "pages": [')  # truncated JSON
        with pytest.raises(SystemExit):
            load_manifest(p)

    def test_load_non_object_fails_closed(self, tmp_path):
        # Valid JSON that isn't an object (null / array) is malformed, not clean-start.
        for bad in ("null", "[1, 2, 3]"):
            p = tmp_path / "paths_manifest.json"
            p.write_text(bad)
            with pytest.raises(SystemExit):
                load_manifest(p)

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
    GOOD_MD = b"# Doc\n\nlots of **markdown** content about claude code here\n\n- a\n- b"

    def _response(self, status=200, content=GOOD_MD, headers=None):
        resp = MagicMock()
        resp.status_code = status
        resp.content = content
        resp.text = content.decode("utf-8", errors="replace")
        resp.headers = headers or {}
        if status >= 400:
            resp.raise_for_status.side_effect = requests.HTTPError(f"{status}")
        else:
            resp.raise_for_status.return_value = None
        return resp

    def _session(self, status=200, content=GOOD_MD, headers=None):
        session = MagicMock()
        session.get.return_value = self._response(status, content, headers)
        return session

    def test_success_returns_raw_bytes(self):
        session = self._session()
        content = fetch_markdown("https://code.claude.com/docs/en/hooks.md", session, "hooks")
        assert isinstance(content, bytes)
        assert b"markdown" in content
        # Redirects must not be followed (client fetches with --max-redirs 0).
        assert session.get.call_args.kwargs.get("allow_redirects") is False

    def test_failure_raises_after_retries(self, monkeypatch):
        monkeypatch.setattr("time.sleep", lambda *_: None)  # no real backoff
        with pytest.raises(Exception):
            fetch_markdown("https://code.claude.com/docs/en/x.md", self._session(status=404), "x")

    def test_redirect_307_treated_as_failure(self, monkeypatch):
        # A 3xx must fail (through retry/carry-forward), never publish as ok:
        # the shell client uses --max-redirs 0, so a redirecting URL is
        # permanently unfetchable client-side.
        monkeypatch.setattr("time.sleep", lambda *_: None)
        session = self._session(
            status=307, headers={"Location": "https://code.claude.com/docs/en/moved.md"}
        )
        with pytest.raises(Exception, match="redirect 307"):
            fetch_markdown("https://code.claude.com/docs/en/x.md", session, "x")

    def test_retry_after_http_date_no_crash_and_clamped(self, monkeypatch):
        # HTTP allows an HTTP-date Retry-After; int() must not blow up the page.
        sleeps = []
        monkeypatch.setattr("time.sleep", lambda s: sleeps.append(s))
        session = MagicMock()
        rate_limited = self._response(
            status=429, headers={"Retry-After": "Wed, 21 Oct 2026 07:28:00 GMT"}
        )
        session.get.side_effect = [rate_limited, self._response()]
        content = fetch_markdown("https://code.claude.com/docs/en/x.md", session, "x")
        assert b"markdown" in content
        assert sleeps == [60]  # unparseable -> default 60s (well under the 300s cap)

    def test_retry_after_seconds_parsing(self):
        def resp(headers):
            r = MagicMock()
            r.headers = headers
            return r

        assert _retry_after_seconds(resp({"Retry-After": "5"})) == 5
        assert _retry_after_seconds(resp({})) == 60                       # absent -> default
        assert _retry_after_seconds(resp({"Retry-After": "nonsense"})) == 60
        assert _retry_after_seconds(resp({"Retry-After": "9999"})) == 300  # clamped
        assert _retry_after_seconds(resp({"Retry-After": "-3"})) == 0      # floor


class TestSaveMarkdownFile:
    def test_writes_exact_bytes_and_hashes_them(self, tmp_path):
        import hashlib
        raw = "# Título\n\ncafé content\n".encode("utf-8")
        digest = save_markdown_file(tmp_path, "x.md", raw)
        assert (tmp_path / "x.md").read_bytes() == raw
        assert digest == hashlib.sha256(raw).hexdigest()

    def test_str_input_encoded_utf8(self, tmp_path):
        import hashlib
        digest = save_markdown_file(tmp_path, "y.md", "# Hi\n")
        assert (tmp_path / "y.md").read_bytes() == b"# Hi\n"
        assert digest == hashlib.sha256(b"# Hi\n").hexdigest()


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
            map_pages_to_filenames(pages)

    def test_no_collision_ok(self):
        pages = [
            {"url": "https://code.claude.com/docs/en/hooks"},
            {"url": "https://code.claude.com/docs/en/mcp"},
        ]
        assert [fn for _, fn in map_pages_to_filenames(pages)] == [
            "claude-code__hooks.md", "claude-code__mcp.md"
        ]

    def test_unmappable_url_skipped(self):
        # One bad upstream URL (empty page slug) must be skipped, not abort the run.
        pages = [
            {"url": "https://code.claude.com/docs/en/hooks"},
            {"url": "https://code.claude.com/docs/en/"},  # empty slug -> skipped
        ]
        assert [fn for _, fn in map_pages_to_filenames(pages)] == ["claude-code__hooks.md"]


class TestSafeguards:
    @staticmethod
    def _ok_pages(n, start=0):
        return [
            {"url": f"u{i}", "sha256": f"h{i}", "fetch_status": "ok"}
            for i in range(start, start + n)
        ]

    def test_discovery_threshold_ok(self):
        pages = [{"url": f"u{i}"} for i in range(250)]
        assert validate_discovery_threshold(pages) is pages

    def test_discovery_threshold_aborts(self):
        with pytest.raises(SystemExit):
            validate_discovery_threshold([{"url": "u"}])

    def test_transition_first_run_passes(self):
        validate_manifest_transition({"pages": []}, self._ok_pages(300))  # no raise

    def test_transition_mass_removal_aborts(self):
        old = {"pages": [{"url": f"u{i}"} for i in range(300)]}
        new = self._ok_pages(260)  # removed 40/300 = 13% > 10%
        with pytest.raises(SystemExit):
            validate_manifest_transition(old, new)

    def test_transition_below_floor_aborts(self):
        # First run (no removal check) with too few ok pages -> floor aborts.
        new = self._ok_pages(240)  # 240 ok < 250
        with pytest.raises(SystemExit):
            validate_manifest_transition({"pages": []}, new)

    def test_transition_too_few_ok_aborts(self):
        # Discovery fine (300) but only 200 fetched OK (rest failed) -> abort (#2).
        new = self._ok_pages(200) + [
            {"url": f"u{i}", "sha256": None, "fetch_status": "failed"} for i in range(200, 300)
        ]
        with pytest.raises(SystemExit):
            validate_manifest_transition({"pages": []}, new)

    def test_transition_all_stale_aborts(self):
        # 100%-failed run: carry-forward sets sha256 on every "stale" entry, so a
        # sha256-based count would pass. The guard must count fetch_status == "ok".
        old = {"pages": [{"url": f"u{i}"} for i in range(300)]}
        new = [
            {"url": f"u{i}", "sha256": f"h{i}", "fetch_status": "stale"} for i in range(300)
        ]
        with pytest.raises(SystemExit):
            validate_manifest_transition(old, new)

    def test_transition_missing_fetch_status_is_not_ok(self):
        # sha256 set but no fetch_status at all must not count as fetched.
        new = [{"url": f"u{i}", "sha256": f"h{i}"} for i in range(300)]
        with pytest.raises(SystemExit):
            validate_manifest_transition({"pages": []}, new)


class TestPreSaveFetchGuard:
    """cli.validate_fetch_success: abort BEFORE any manifest write on a failed run."""

    @staticmethod
    def _pages(ok_docs, other=0, other_status="stale", with_changelog_ok=True):
        pages = [
            {"id": f"p{i}", "url": f"u{i}", "fetch_status": "ok"} for i in range(ok_docs)
        ]
        pages += [
            {"id": f"q{i}", "url": f"v{i}", "fetch_status": other_status} for i in range(other)
        ]
        if with_changelog_ok:
            pages.append({"id": "changelog", "url": "cl", "fetch_status": "ok"})
        return pages

    def test_count_excludes_changelog(self):
        assert count_ok_doc_pages(self._pages(ok_docs=3)) == 3
        assert count_ok_doc_pages(self._pages(ok_docs=0)) == 0  # changelog ok alone -> 0

    def test_count_ignores_stale_failed_and_missing_status(self):
        pages = self._pages(ok_docs=2, other=5, with_changelog_ok=False)
        pages.append({"id": "x", "url": "ux"})  # no fetch_status -> not ok
        assert count_ok_doc_pages(pages) == 2

    def test_passes_at_threshold(self):
        validate_fetch_success(self._pages(ok_docs=250))  # no raise

    def test_total_outage_aborts_even_with_changelog_ok(self):
        # GitHub-hosted changelog succeeds during a docs-site outage; the old
        # `stats["ok"] == 0` check passed with ok==1. The guard must abort.
        with pytest.raises(SystemExit):
            validate_fetch_success(self._pages(ok_docs=0, other=300))

    def test_below_threshold_aborts(self):
        with pytest.raises(SystemExit):
            validate_fetch_success(self._pages(ok_docs=249, other=60))


class TestParseFetchLimit:
    def test_valid_values(self):
        assert parse_fetch_limit("8") == 8
        assert parse_fetch_limit("0") == 0
        assert parse_fetch_limit("") == 0
        assert parse_fetch_limit(None) == 0

    def test_invalid_value_exits_with_clear_error(self):
        with pytest.raises(SystemExit):
            parse_fetch_limit("eight")
