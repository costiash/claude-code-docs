"""Contract tests for plugin/scripts/fetch-docs.sh using a fake curl on PATH (offline)."""

import hashlib
import json
import os
import shutil
import subprocess
import time
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
# A raw-github URL a naive prefix-glob ALLOWS (curl squashes the ../ before sending) but
# the exact-match pin must refuse — the traversal bypass that fetched a third-party repo.
RAWEVIL = ("rawevil.md", "https://raw.githubusercontent.com/anthropics/claude-code/../../attacker/evil/main/x.md", "# RawEvil\n")

FAKE_CURL = r'''#!/usr/bin/env python3
import sys, os, json, time
# Deterministic hold-open: block while the sentinel file exists (lock tests).
_blk = os.environ.get("CURL_BLOCK_FILE", "")
while _blk and os.path.exists(_blk):
    time.sleep(0.02)
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
    # non-anthropic raw-github page available too (the raw-github pin must block it)
    content_map[RAWEVIL[1]] = RAWEVIL[2]

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


def add_rawevil(manifest_path):
    data = json.loads(manifest_path.read_text())
    data["pages"].append(_entry(RAWEVIL[0], RAWEVIL[1], RAWEVIL[2], category="core_documentation"))
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


class TestSyncLock:
    """Issue #28: cmd_sync must lock (every caller), reap only dead owners,
    and never remove a lock it no longer owns (the EXIT-trap cascade)."""

    @staticmethod
    def lock_dir(cache: Path) -> Path:
        return cache / ".sync.lock"

    def make_lock(self, cache: Path, pid=None, age_secs=0):
        cache.mkdir(parents=True, exist_ok=True)
        lock = self.lock_dir(cache)
        lock.mkdir()
        if pid is not None:
            (lock / "pid").write_text(f"{pid}\n")
        if age_secs:
            old = time.time() - age_secs
            os.utime(lock, (old, old))
        return lock

    def test_sync_defers_when_lock_held_by_live_process(self, harness):
        env, cache, _ = harness
        self.make_lock(cache, pid=os.getpid())  # pytest itself: definitely alive
        r = run(env, "sync")
        assert r.returncode == 0, r.stderr
        assert "already running" in r.stdout, r.stdout
        assert not list(cache.glob("*.md"))  # nothing fetched
        assert self.lock_dir(cache).is_dir()  # foreign lock untouched

    def test_sync_defers_on_fresh_pidless_lock(self, harness):
        # A pidless lock can be an owner inside its mkdir->pid-write window:
        # fresh means live, do not reap.
        env, cache, _ = harness
        self.make_lock(cache)
        r = run(env, "sync")
        assert r.returncode == 0, r.stderr
        assert "already running" in r.stdout, r.stdout
        assert not list(cache.glob("*.md"))
        assert self.lock_dir(cache).is_dir()

    def test_sync_reaps_dead_owner_lock(self, harness):
        env, cache, _ = harness
        p = subprocess.Popen(["true"], stdout=subprocess.DEVNULL)
        p.wait()  # reaped: kill -0 on this pid now fails
        self.make_lock(cache, pid=p.pid)
        r = run(env, "sync")
        assert r.returncode == 0, r.stderr
        for fn in list(PAGES) + [STALE[0]]:
            assert (cache / fn).exists(), fn
        assert not self.lock_dir(cache).exists()  # released its own lock

    def test_sync_reaps_ancient_lock_despite_live_pid(self, harness):
        # Recycled-PID backstop: a live sync refreshes the lock mtime every
        # batch, so a lock untouched for 30+ minutes belongs to no live sync
        # even when kill -0 says otherwise.
        env, cache, _ = harness
        self.make_lock(cache, pid=os.getpid(), age_secs=3600)
        r = run(env, "sync")
        assert r.returncode == 0, r.stderr
        for fn in list(PAGES) + [STALE[0]]:
            assert (cache / fn).exists(), fn
        assert not self.lock_dir(cache).exists()

    def test_sync_reaps_stale_plain_file_at_lock_path(self, harness):
        # Poison-file regression: a heartbeat racing a lock removal can leave
        # a plain FILE at the lock path. Treating non-dir as "vanished"
        # forever would silently disable sync permanently — a stale file must
        # be reaped like any stale lock.
        env, cache, _ = harness
        cache.mkdir(parents=True, exist_ok=True)
        poison = self.lock_dir(cache)
        poison.write_text("")
        old = time.time() - 7200
        os.utime(poison, (old, old))
        r = run(env, "sync")
        assert r.returncode == 0, r.stderr
        for fn in list(PAGES) + [STALE[0]]:
            assert (cache / fn).exists(), fn
        assert not poison.exists()

    def test_sync_defers_on_fresh_plain_file_at_lock_path(self, harness):
        # Fresh non-dir obstruction: same grace as a fresh pidless lock.
        env, cache, _ = harness
        cache.mkdir(parents=True, exist_ok=True)
        poison = self.lock_dir(cache)
        poison.write_text("")
        r = run(env, "sync")
        assert r.returncode == 0, r.stderr
        assert "already running" in r.stdout, r.stdout
        assert not list(cache.glob("*.md"))
        assert poison.exists()

    def test_sync_removes_own_lock_on_completion(self, harness):
        env, cache, _ = harness
        r = run(env, "sync")
        assert r.returncode == 0, r.stderr
        assert not self.lock_dir(cache).exists()

    def test_finishing_sync_leaves_stolen_lock_alone(self, harness):
        # The #28 cascade: sync A's EXIT trap must not rmdir a lock that was
        # (wrongly or rightly) reaped and re-acquired by a successor. The
        # fake curl blocks on a sentinel file, so the steal happens inside a
        # deterministically held-open window (no sleeps, no timing).
        env, cache, manifest_path = harness
        env = dict(env)
        block = manifest_path.parent / "curl.block"
        block.write_text("")
        env["CURL_BLOCK_FILE"] = str(block)
        a = subprocess.Popen([str(FETCH), "sync"], env=env,
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        lock = self.lock_dir(cache)
        deadline = time.time() + 10
        while time.time() < deadline and not (lock / "pid").exists():
            time.sleep(0.02)
        assert (lock / "pid").exists(), "sync A never took the lock"
        # Steal the lock mid-sync (simulates the mtime reaper of a second session).
        shutil.rmtree(lock)
        self.make_lock(cache, pid=os.getpid())
        block.unlink()  # release the held-open fetches; A finishes
        a.wait(timeout=60)
        assert lock.is_dir(), "finishing sync removed a lock it no longer owns"
        assert (lock / "pid").read_text().strip() == str(os.getpid())


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

    def test_get_non_changelog_rawgithub_refused(self, harness):
        # raw.githubusercontent.com serves exactly one file to the client (the anthropics
        # changelog); a ../ traversal URL that a prefix glob would allow must be refused.
        env, cache, manifest_path = harness
        add_rawevil(manifest_path)
        r = run(env, "get", "rawevil.md")
        assert r.returncode != 0
        assert "non-changelog raw.githubusercontent.com" in r.stderr
        assert not (cache / "rawevil.md").exists()


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


def test_changelog_pin_agrees_across_files():
    """The raw.githubusercontent.com changelog URL is hardcoded as the client exact-match
    pin (fetch-docs.sh) and in the CI fetcher (cli.py, content.py). They MUST stay byte-
    identical: a drift (e.g. a CI-side branch/repo rename) would silently stop the client
    from fetching the changelog with no other test failing."""
    import re
    root = Path(__file__).resolve().parents[2]
    pat = re.compile(r'https://raw\.githubusercontent\.com/[^\s"\')]*CHANGELOG\.md')
    urls = set()
    for rel in ("plugin/scripts/fetch-docs.sh", "scripts/fetcher/cli.py", "scripts/fetcher/content.py"):
        found = pat.findall((root / rel).read_text())
        assert found, f"no raw-github CHANGELOG URL found in {rel}"
        urls.update(found)
    assert len(urls) == 1, f"changelog pin drifted across files: {sorted(urls)}"
