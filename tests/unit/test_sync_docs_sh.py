"""Contract tests for plugin/hooks/sync-docs.sh (offline: file:// fixture origin).

Covers issue #27: hook time budget, macOS run_with_timeout watchdog fallback,
rename-swap self-heal, and dead-PID swap-orphan pruning with user-data rescue.
"""

import json
import os
import shutil
import subprocess
import time
from pathlib import Path

import pytest

HOOK = Path(__file__).parent.parent.parent / "plugin" / "hooks" / "sync-docs.sh"

pytestmark = pytest.mark.skipif(
    not shutil.which("jq") or not shutil.which("bash") or not shutil.which("git"),
    reason="requires jq + bash + git",
)


def _git(*args, cwd):
    subprocess.run(
        ["git", *args], cwd=cwd, check=True,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        env={**os.environ, "GIT_CONFIG_GLOBAL": "/dev/null", "GIT_CONFIG_SYSTEM": "/dev/null",
             "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
             "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"},
    )


@pytest.fixture()
def origin(tmp_path):
    """A local 'upstream' repo with a manifest, cloneable via file://."""
    repo = tmp_path / "origin"
    repo.mkdir()
    (repo / "paths_manifest.json").write_text(json.dumps({"pages": [{"id": "p1"}]}))
    _git("init", "-q", "-b", "main", cwd=repo)
    _git("add", ".", cwd=repo)
    _git("commit", "-qm", "init", cwd=repo)
    return repo


def run_hook(home: Path, origin: Path, budget="40", extra_env=None, path=None):
    env = {
        **os.environ,
        "HOME": str(home),
        "CLAUDE_DOCS_TEST": "1",  # sentinel: REPO_URL override is honored only with it
        "CLAUDE_DOCS_REPO_URL": f"file://{origin}",
        "CLAUDE_DOCS_HOOK_BUDGET": budget,
        "GIT_CONFIG_GLOBAL": "/dev/null",
        "GIT_CONFIG_SYSTEM": "/dev/null",
    }
    if path is not None:
        env["PATH"] = path
    if extra_env:
        env.update(extra_env)
    return subprocess.run(
        ["bash", str(HOOK)], env=env, capture_output=True, text=True, timeout=120
    )


def context_of(result) -> str:
    return json.loads(result.stdout)["hookSpecificOutput"]["additionalContext"]


class TestFirstRunAndUpdate:
    def test_first_run_installs(self, tmp_path, origin):
        home = tmp_path / "home"
        home.mkdir()
        r = run_hook(home, origin)
        assert r.returncode == 0
        assert "installed" in context_of(r)
        assert (home / ".claude-code-docs" / "paths_manifest.json").exists()

    def test_healthy_clone_reports_up_to_date(self, tmp_path, origin):
        home = tmp_path / "home"
        home.mkdir()
        run_hook(home, origin)
        r = run_hook(home, origin)
        assert "up-to-date" in context_of(r) or "updated" in context_of(r)


class TestRepoUrlSentinel:
    def test_override_ignored_without_sentinel(self, tmp_path, origin):
        """A stray CLAUDE_DOCS_REPO_URL alone must never repoint a real install."""
        home = tmp_path / "home"
        home.mkdir()
        log = tmp_path / "git-args.log"
        fake = tmp_path / "bin"
        fake.mkdir()
        (fake / "git").write_text(
            "#!/bin/bash\n" f'echo "$@" >> "{log}"\n' "exit 1\n"
        )
        (fake / "git").chmod(0o755)
        r = run_hook(
            home, origin,
            extra_env={"CLAUDE_DOCS_TEST": ""},  # sentinel absent
            path=f"{fake}:{os.environ['PATH']}",
        )
        assert r.returncode == 0
        assert "github.com/costiash/claude-code-docs" in log.read_text()
        assert str(origin) not in log.read_text()


class TestBudget:
    def test_hung_git_cannot_exceed_budget(self, tmp_path, origin):
        """A git that hangs forever must be killed within the budget — even
        without timeout(1) on PATH (the macOS case, via the watchdog)."""
        home = tmp_path / "home"
        home.mkdir()
        run_hook(home, origin)  # healthy install
        # Fake bin dir: git hangs on fetch/reset, real binaries otherwise.
        fake = tmp_path / "bin"
        fake.mkdir()
        real_git = shutil.which("git")
        (fake / "git").write_text(
            "#!/bin/bash\n"
            f'case "$1" in fetch|reset|clone) sleep 300 ;; *) exec {real_git} "$@" ;; esac\n'
        )
        (fake / "git").chmod(0o755)
        # PATH without timeout(1): shim dir + a minimal dir set that lacks it.
        stripped = tmp_path / "noto"
        stripped.mkdir()
        for tool in ("bash", "jq", "sleep", "kill", "mv", "rm", "mkdir", "find", "cat", "nohup", "sh", "dirname", "basename", "grep", "pwd", "env"):
            src = shutil.which(tool)
            if src:
                (stripped / tool).symlink_to(src)
        assert shutil.which("timeout", path=str(stripped)) is None
        start = time.monotonic()
        r = run_hook(home, origin, budget="4", path=f"{fake}:{stripped}")
        elapsed = time.monotonic() - start
        assert r.returncode == 0
        # budget 4s + watchdog granularity + interpreter overhead << 300s hang
        assert elapsed < 30, f"hook ran {elapsed:.1f}s — watchdog did not fire"

    def test_sigterm_trapping_git_killed_by_escalation(self, tmp_path, origin):
        """A command that ignores SIGTERM must still die: TERM -> 2s grace -> KILL."""
        home = tmp_path / "home"
        home.mkdir()
        run_hook(home, origin)
        fake = tmp_path / "bin"
        fake.mkdir()
        real_git = shutil.which("git")
        (fake / "git").write_text(
            "#!/bin/bash\n"
            'case "$1" in\n'
            "  fetch|reset|clone) trap '' TERM; sleep 300 ;;\n"
            f'  *) exec {real_git} "$@" ;;\n'
            "esac\n"
        )
        (fake / "git").chmod(0o755)
        stripped = tmp_path / "noto"
        stripped.mkdir()
        for tool in ("bash", "jq", "sleep", "kill", "mv", "rm", "mkdir", "find", "cat", "nohup", "sh", "grep", "pwd", "env", "rmdir", "chmod"):
            src = shutil.which(tool)
            if src:
                (stripped / tool).symlink_to(src)
        assert shutil.which("timeout", path=str(stripped)) is None
        start = time.monotonic()
        r = run_hook(home, origin, budget="4", path=f"{fake}:{stripped}")
        elapsed = time.monotonic() - start
        assert r.returncode == 0
        assert elapsed < 40, f"hook ran {elapsed:.1f}s — KILL escalation did not fire"

    def test_remaining_never_reaches_zero(self, tmp_path, origin):
        """Budget already exhausted -> caps clamp to 1s, script still completes."""
        home = tmp_path / "home"
        home.mkdir()
        run_hook(home, origin)
        r = run_hook(home, origin, budget="0")
        assert r.returncode == 0
        assert "pages indexed" in context_of(r)


class TestSelfHealSwap:
    def _corrupt(self, home: Path):
        docs = home / ".claude-code-docs"
        shutil.rmtree(docs / ".git")
        (docs / "paths_manifest.json").unlink()
        (docs / "cache").mkdir(exist_ok=True)
        (docs / "cache" / "page.md").write_text("cached")
        (docs / "courses").mkdir(exist_ok=True)
        (docs / "courses" / "c.html").write_text("course")
        return docs

    def test_rename_swap_heals_and_preserves_user_data(self, tmp_path, origin):
        home = tmp_path / "home"
        home.mkdir()
        run_hook(home, origin)
        docs = self._corrupt(home)
        r = run_hook(home, origin)
        assert r.returncode == 0
        assert (docs / "paths_manifest.json").exists()
        assert (docs / ".git").exists()
        assert (docs / "cache" / "page.md").read_text() == "cached"
        assert (docs / "courses" / "c.html").read_text() == "course"
        leftovers = list(home.glob(".claude-code-docs.new.*")) + list(home.glob(".claude-code-docs.old.*"))
        assert leftovers == []

    def test_failed_heal_offline_keeps_old_dir(self, tmp_path, origin):
        home = tmp_path / "home"
        home.mkdir()
        run_hook(home, origin)
        docs = self._corrupt(home)
        bad_origin = tmp_path / "gone"
        r = run_hook(home, bad_origin)
        assert r.returncode == 0
        assert "could not be repaired" in context_of(r)
        # Old dir untouched: user data still in place.
        assert (docs / "cache" / "page.md").exists()
        assert (docs / "courses" / "c.html").exists()


class TestOrphanPrune:
    def test_dead_pid_orphan_pruned_and_data_rescued(self, tmp_path, origin):
        home = tmp_path / "home"
        home.mkdir()
        run_hook(home, origin)
        docs = home / ".claude-code-docs"
        # PID 4194304 is above kernel default pid_max on Linux; certainly dead.
        orphan = home / ".claude-code-docs.new.4194304"
        (orphan / "courses").mkdir(parents=True)
        (orphan / "courses" / "rescued.html").write_text("rescued")
        old_orphan = home / ".claude-code-docs.old.4194303"
        old_orphan.mkdir()
        (old_orphan / "junk").write_text("x")
        r = run_hook(home, origin)
        assert r.returncode == 0
        assert not orphan.exists()
        assert not old_orphan.exists()
        assert (docs / "courses" / "rescued.html").read_text() == "rescued"

    def test_live_pid_orphan_left_alone(self, tmp_path, origin):
        home = tmp_path / "home"
        home.mkdir()
        run_hook(home, origin)
        live = home / f".claude-code-docs.new.{os.getpid()}"
        live.mkdir()
        (live / "marker").write_text("x")
        r = run_hook(home, origin)
        assert r.returncode == 0
        assert (live / "marker").exists()  # concurrent session's swap untouched

    def test_nonnumeric_suffix_never_touched(self, tmp_path, origin):
        """A user backup like ~/.claude-code-docs.old.bak must never be eaten."""
        home = tmp_path / "home"
        home.mkdir()
        run_hook(home, origin)
        backup = home / ".claude-code-docs.old.bak"
        (backup / "courses").mkdir(parents=True)
        (backup / "courses" / "precious.html").write_text("precious")
        r = run_hook(home, origin)
        assert r.returncode == 0
        assert (backup / "courses" / "precious.html").read_text() == "precious"

    def test_stale_live_pid_orphan_pruned_by_age_backstop(self, tmp_path, origin):
        """kill -0 can lie (recycled PID): dirs older than ~60 min prune anyway."""
        home = tmp_path / "home"
        home.mkdir()
        run_hook(home, origin)
        docs = home / ".claude-code-docs"
        stale = home / f".claude-code-docs.new.{os.getpid()}"  # 'alive' PID
        (stale / "courses").mkdir(parents=True)
        (stale / "courses" / "old-session.html").write_text("rescued")
        two_hours_ago = time.time() - 7200
        os.utime(stale, (two_hours_ago, two_hours_ago))
        r = run_hook(home, origin)
        assert r.returncode == 0
        assert not stale.exists()
        assert (docs / "courses" / "old-session.html").read_text() == "rescued"

    def test_empty_recreated_dir_does_not_block_rescue(self, tmp_path, origin):
        """A background fetch's empty mkdir must not beat a populated parked cache."""
        home = tmp_path / "home"
        home.mkdir()
        run_hook(home, origin)
        docs = home / ".claude-code-docs"
        (docs / "cache").mkdir()  # empty — recreated by a racing background fetch
        orphan = home / ".claude-code-docs.new.4194301"
        (orphan / "cache").mkdir(parents=True)
        (orphan / "cache" / "page.md").write_text("full corpus")
        r = run_hook(home, origin)
        assert r.returncode == 0
        assert (docs / "cache" / "page.md").read_text() == "full corpus"
        assert not orphan.exists()

    def test_heal_lock_defers_concurrent_repair(self, tmp_path, origin):
        home = tmp_path / "home"
        home.mkdir()
        run_hook(home, origin)
        docs = home / ".claude-code-docs"
        shutil.rmtree(docs / ".git")
        (docs / "paths_manifest.json").unlink()
        (home / ".claude-code-docs.heal.lock").mkdir()  # fresh: other session healing
        r = run_hook(home, origin)
        assert r.returncode == 0
        assert "another session" in context_of(r)
        assert not (docs / ".git").exists()  # untouched — deferred, not healed

    def test_rescue_never_overwrites_existing_data(self, tmp_path, origin):
        home = tmp_path / "home"
        home.mkdir()
        run_hook(home, origin)
        docs = home / ".claude-code-docs"
        (docs / "courses").mkdir()
        (docs / "courses" / "mine.html").write_text("current")
        orphan = home / ".claude-code-docs.old.4194302"
        (orphan / "courses").mkdir(parents=True)
        (orphan / "courses" / "stale.html").write_text("stale")
        r = run_hook(home, origin)
        assert r.returncode == 0
        assert (docs / "courses" / "mine.html").read_text() == "current"
        assert not (docs / "courses" / "stale.html").exists()
        assert not orphan.exists()
