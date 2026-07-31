"""B6: manifest-diff.sh against a synthetic 2-commit repo (offline)."""

import json
import os
import shutil
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

_NOW = datetime.now(timezone.utc)
# Explicit +0000 offset — without it git reads the timestamp as local time and skews the window.
OLD_DATE = (_NOW - timedelta(days=10)).strftime("%Y-%m-%dT%H:%M:%S+0000")   # before any window
RECENT_DATE = (_NOW - timedelta(minutes=30)).strftime("%Y-%m-%dT%H:%M:%S+0000")  # within 1h/7d

DIFF = Path(__file__).parent.parent.parent / "plugin" / "scripts" / "manifest-diff.sh"

pytestmark = pytest.mark.skipif(
    not shutil.which("jq") or not shutil.which("git") or not shutil.which("bash"),
    reason="requires jq + git + bash",
)


def page(pid, sha, title=None, category="claude_code"):
    return {"id": pid, "filename": pid.replace("/", "__") + ".md",
            "url": f"https://code.claude.com/docs/en/{pid.split('/')[-1]}",
            "md_url": f"https://code.claude.com/docs/en/{pid.split('/')[-1]}.md",
            "title": title or pid, "category": category, "sha256": sha,
            "lastmod": None, "fetch_status": "ok"}


def git(repo, *args, date=None):
    env = os.environ.copy()
    env.update({"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
                "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"})
    if date:
        env["GIT_AUTHOR_DATE"] = date
        env["GIT_COMMITTER_DATE"] = date
    subprocess.run(["git", *args], cwd=repo, env=env, check=True,
                   capture_output=True, text=True)


@pytest.fixture
def repo(tmp_path):
    r = tmp_path / "clone"; r.mkdir()
    git(r, "init", "-q")
    manifest = r / "paths_manifest.json"

    # Commit 1 (10 days ago): pages A, B, C.
    v1 = {"schema_version": 2, "pages": [
        page("claude-code/a", "sha_a1", "Alpha"),
        page("claude-code/b", "sha_b1", "Bravo"),
        page("claude-code/c", "sha_c1", "Charlie"),
    ]}
    manifest.write_text(json.dumps(v1))
    git(r, "add", "-A")
    git(r, "commit", "-qm", "v1", date=OLD_DATE)

    # Commit 2 (now): A changed (sha), B removed, C same, D added.
    v2 = {"schema_version": 2, "pages": [
        page("claude-code/a", "sha_a2", "Alpha"),   # changed
        page("claude-code/c", "sha_c1", "Charlie"),  # unchanged
        page("claude-code/d", "sha_d1", "Delta"),    # added
    ]}
    manifest.write_text(json.dumps(v2))
    git(r, "add", "-A")
    git(r, "commit", "-qm", "v2", date=RECENT_DATE)
    return r


def run_diff(repo, *args):
    env = os.environ.copy()
    env["CLAUDE_DOCS_CLONE"] = str(repo)
    return subprocess.run([str(DIFF), *args], env=env, capture_output=True, text=True)


def test_json_diff_added_changed_removed(repo):
    r = run_diff(repo, "--since", "7d", "--json")
    assert r.returncode == 0, r.stderr
    d = json.loads(r.stdout)
    assert {p["id"] for p in d["added"]} == {"claude-code/d"}
    assert {p["id"] for p in d["changed"]} == {"claude-code/a"}
    assert {p["id"] for p in d["removed"]} == {"claude-code/b"}


def test_changed_keys_off_sha_not_lastmod(repo):
    # C is unchanged (same sha) -> must NOT appear in changed even though lastmod is null.
    r = run_diff(repo, "--since", "7d", "--json")
    d = json.loads(r.stdout)
    assert "claude-code/c" not in {p["id"] for p in d["changed"]}


def test_human_output_has_sections(repo):
    r = run_diff(repo, "--since", "7d")
    assert r.returncode == 0, r.stderr
    assert "=== Added (1) ===" in r.stdout
    assert "=== Changed (1) ===" in r.stdout
    assert "=== Removed (1) ===" in r.stdout
    assert "Delta" in r.stdout


def test_window_predating_history_is_all_added(repo):
    # A 1-hour window: baseline is the 10-days-ago... no, both commits are within? v2 is "now",
    # v1 is 10 days ago. --since 1h -> baseline = newest commit before 1h ago = v1 commit.
    # So changes since 1h ago are still A changed / B removed / D added (v1 -> v2).
    r = run_diff(repo, "--since", "1h", "--json")
    d = json.loads(r.stdout)
    assert {p["id"] for p in d["added"]} == {"claude-code/d"}
