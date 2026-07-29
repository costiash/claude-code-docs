"""Contract tests for plugin/scripts/fetch-docs.sh using a fake curl on PATH (offline)."""

import hashlib
import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest

FETCH = Path(__file__).parent.parent.parent / "plugin" / "scripts" / "fetch-docs.sh"

pytestmark = pytest.mark.skipif(
    not shutil.which("jq") or not shutil.which("bash"),
    reason="requires jq + bash",
)


def sha(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()


# filename -> (md_url, content)  — all allowed hosts.
PAGES = {
    "claude-code__hooks.md": ("https://code.claude.com/docs/en/hooks.md", "# Hooks\n\ncontent about hooks\n"),
    "docs__en__api__messages.md": ("https://platform.claude.com/docs/en/api/messages.md", "# Messages\n\napi content\n"),
    "changelog.md": ("https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md", "# Changelog\n\nchanges\n"),
}
# A page whose manifest sha256 is deliberately WRONG (hash-mismatch / stale test).
STALE = ("docs__en__stale.md", "https://platform.claude.com/docs/en/stale.md", "# Stale\n\nlive content\n")
# A page on a disallowed host (allowlist test only).
EVIL = ("evil.md", "https://evil.example.com/docs/en/evil.md", "# Evil\n")
# A page on an ALLOWED host but with an insecure http:// scheme (https-only guard test).
INSECURE = ("insecure.md", "http://code.claude.com/docs/en/insecure.md", "# Insecure\n")

FAKE_CURL = r'''#!/usr/bin/env python3
import sys, os, json
args = sys.argv[1:]
out = None; url = None
i = 0
while i < len(args):
    a = args[i]
    if a == "-o":
        out = args[i + 1]; i += 2; continue
    if a == "--max-time":
        i += 2; continue
    if a.startswith("-"):
        i += 1; continue
    url = a; i += 1

cmap = json.load(open(os.environ["CONTENT_MAP"]))
fail_once = os.environ.get("CURL_FAIL_ONCE", "")
if url and url in fail_once.split(","):
    marker = os.path.join(os.environ["FAIL_DIR"], url.replace("/", "_"))
    if not os.path.exists(marker):
        open(marker, "w").close()
        sys.exit(7)

content = cmap.get(url)
if content is None:
    sys.exit(22)  # 404
if out:
    open(out, "w").write(content)
else:
    sys.stdout.write(content)
sys.exit(0)
'''


def _entry(filename, url, content, manifest_sha=None, category="claude_code"):
    return {"id": filename[:-3].replace("__", "/"), "filename": filename, "url": url[:-3],
            "md_url": url, "title": filename, "category": category,
            "sha256": manifest_sha if manifest_sha is not None else sha(content),
            "lastmod": None, "fetch_status": "ok"}


@pytest.fixture
def harness(tmp_path):
    clone = tmp_path / "clone"; clone.mkdir()
    cache = tmp_path / "cache"
    faildir = tmp_path / "fail"; faildir.mkdir()

    pages = [_entry(fn, url, c) for fn, (url, c) in PAGES.items()]
    content_map = {url: c for _, (url, c) in PAGES.items()}
    # stale page: manifest sha != content sha
    sfn, surl, sc = STALE
    pages.append(_entry(sfn, surl, sc, manifest_sha="0" * 64, category="core_documentation"))
    content_map[surl] = sc
    # evil content available too (used only when a test adds the evil page to the manifest)
    content_map[EVIL[1]] = EVIL[2]
    # insecure http page available too — the guard must block BEFORE curl is ever reached
    content_map[INSECURE[1]] = INSECURE[2]

    manifest_path = clone / "paths_manifest.json"
    manifest_path.write_text(json.dumps({"schema_version": 2, "pages": pages}))

    bindir = tmp_path / "bin"; bindir.mkdir()
    (bindir / "curl").write_text(FAKE_CURL)
    (bindir / "curl").chmod(0o755)
    cmap_file = tmp_path / "content_map.json"
    cmap_file.write_text(json.dumps(content_map))

    env = os.environ.copy()
    env["PATH"] = f"{bindir}{os.pathsep}{env['PATH']}"
    env["CLAUDE_DOCS_MANIFEST"] = str(manifest_path)
    env["CLAUDE_DOCS_CACHE_DIR"] = str(cache)
    env["CONTENT_MAP"] = str(cmap_file)
    env["FAIL_DIR"] = str(faildir)
    return env, cache, manifest_path


def run(env, *args):
    return subprocess.run([str(FETCH), *args], env=env, capture_output=True, text=True)


def add_evil(manifest_path):
    data = json.loads(manifest_path.read_text())
    data["pages"].append(_entry(EVIL[0], EVIL[1], EVIL[2], category="core_documentation"))
    manifest_path.write_text(json.dumps(data))


def add_insecure(manifest_path):
    data = json.loads(manifest_path.read_text())
    data["pages"].append(_entry(INSECURE[0], INSECURE[1], INSECURE[2], category="core_documentation"))
    manifest_path.write_text(json.dumps(data))


class TestSync:
    def test_fresh_sync_fetches_all_syncable(self, harness):
        env, cache, _ = harness
        r = run(env, "sync")
        assert r.returncode == 0, r.stderr
        for fn in list(PAGES) + [STALE[0]]:
            assert (cache / fn).exists(), fn

    def test_second_sync_is_noop(self, harness):
        env, cache, _ = harness
        run(env, "sync")
        r = run(env, "sync")
        assert r.returncode == 0
        assert "0 fetches" in r.stdout or "up to date" in r.stdout, r.stdout

    def test_hash_mismatch_marks_stale_not_failure(self, harness):
        env, cache, _ = harness
        run(env, "sync")
        meta = json.loads((cache / ".meta" / "docs__en__stale.md.json").read_text())
        assert meta["stale_manifest"] is True
        assert (cache / "docs__en__stale.md").exists()

    def test_stale_page_not_refetched_next_sync(self, harness):
        env, cache, _ = harness
        run(env, "sync")
        r = run(env, "sync")  # stale page must NOT re-fetch (synced against same manifest sha)
        assert "0 fetches" in r.stdout or "up to date" in r.stdout, r.stdout

    def test_good_page_not_stale(self, harness):
        env, cache, _ = harness
        run(env, "sync")
        meta = json.loads((cache / ".meta" / "claude-code__hooks.md.json").read_text())
        assert meta["stale_manifest"] is False


class TestGet:
    def test_get_by_filename(self, harness):
        env, cache, _ = harness
        r = run(env, "get", "claude-code__hooks.md")
        assert r.returncode == 0, r.stderr
        assert (cache / "claude-code__hooks.md").exists()

    def test_get_by_id(self, harness):
        env, cache, _ = harness
        r = run(env, "get", "claude-code/hooks")
        assert r.returncode == 0, r.stderr
        assert (cache / "claude-code__hooks.md").exists()

    def test_get_disallowed_host_refused(self, harness):
        env, cache, manifest_path = harness
        add_evil(manifest_path)
        r = run(env, "get", "evil.md")
        assert r.returncode != 0
        assert "disallowed host" in r.stderr
        assert not (cache / "evil.md").exists()

    def test_get_non_https_refused(self, harness):
        env, cache, manifest_path = harness
        add_insecure(manifest_path)
        r = run(env, "get", "insecure.md")
        assert r.returncode != 0
        assert "non-https" in r.stderr
        assert not (cache / "insecure.md").exists()


class TestRetry:
    def test_retry_once_then_succeeds(self, harness):
        env, cache, _ = harness
        env = dict(env)
        env["CURL_FAIL_ONCE"] = "https://code.claude.com/docs/en/hooks.md"
        r = run(env, "get", "claude-code__hooks.md")
        assert r.returncode == 0, r.stderr
        assert (cache / "claude-code__hooks.md").exists()


class TestStatusPrune:
    def test_status_exit_codes(self, harness):
        env, _, _ = harness
        r = run(env, "status")
        assert r.returncode == 2  # pending before sync
        run(env, "sync")
        r2 = run(env, "status")
        assert r2.returncode == 0  # nothing pending after sync
        assert "cached" in r2.stdout

    def test_prune_removes_unlisted(self, harness):
        env, cache, _ = harness
        run(env, "sync")
        (cache / "orphan.md").write_text("not in manifest")
        r = run(env, "prune")
        assert r.returncode == 0
        assert not (cache / "orphan.md").exists()
        assert (cache / "claude-code__hooks.md").exists()
