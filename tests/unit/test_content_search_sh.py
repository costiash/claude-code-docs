"""Contract tests for plugin/skills/claude-docs/scripts/content-search.sh (offline).

The fixture index is invented: titles, headings and terms are placeholder words
written for this test, never documentation text.
"""

import json
import shutil
import subprocess
from pathlib import Path

import pytest

SEARCH = (
    Path(__file__).parent.parent.parent
    / "plugin" / "skills" / "claude-docs" / "scripts" / "content-search.sh"
)

pytestmark = pytest.mark.skipif(
    not shutil.which("jq") or not shutil.which("bash"), reason="requires jq + bash"
)


def _page(i: int, title: str, terms: dict) -> dict:
    return {
        "filename": f"claude-code__fixture-page-{i:04d}.md",
        "id": f"claude-code/fixture-page-{i:04d}",
        "title": title,
        "category": "claude_code",
        "url": f"https://code.claude.com/docs/en/fixture-page-{i:04d}",
        "headings": [{"text": title, "level": 1}],
        "terms": terms,
        "word_count": 100,
    }


@pytest.fixture()
def env(tmp_path):
    """A big index: every page matches the query, and the candidate list the
    inner sort emits is far larger than a pipe buffer, so `head -20` closes
    the pipe long before sort has finished writing."""
    pages = [
        _page(i, f"Widget gadget {i:04d} " + "filler " * 12, {"widget": 5, "gadget": 2})
        for i in range(1500)
    ]
    pages.append(_page(9999, "Lonely sprocket page", {"sprocket": 3}))
    index = tmp_path / "search_index.json"
    index.write_text(json.dumps({"schema_version": 2, "pages": pages}))
    cache = tmp_path / "cache"  # absent: strategy 1 only
    return {
        "PATH": "/usr/bin:/bin",
        "CLAUDE_DOCS_INDEX": str(index),
        "CLAUDE_DOCS_CACHE_DIR": str(cache),
    }


def run_search(env, *args):
    return subprocess.run(
        ["bash", str(SEARCH), *args], env=env, capture_output=True, text=True, timeout=60
    )


class TestQuietPipelines:
    def test_broad_query_emits_no_stderr(self, env):
        r = run_search(env, "widget")
        assert r.returncode == 0
        assert r.stderr == "", r.stderr
        lines = r.stdout.splitlines()
        assert len(lines) == 20
        assert all(line.count("\t") == 2 for line in lines)

    def test_reader_closing_early_emits_no_stderr(self, env, tmp_path):
        err = tmp_path / "stderr.txt"
        r = subprocess.run(
            ["bash", "-c", f'"$0" widget 2>"{err}" | head -c 1 >/dev/null; echo "${{PIPESTATUS[0]}}"',
             str(SEARCH)],
            env=env, capture_output=True, text=True, timeout=60,
        )
        assert r.stdout.strip() == "0", r.stdout
        assert err.read_text() == "", err.read_text()

    def test_narrow_query_still_finds_the_page(self, env):
        r = run_search(env, "sprocket")
        assert r.returncode == 0 and r.stderr == ""
        assert r.stdout.splitlines() == [
            "claude-code__fixture-page-9999.md\tLonely sprocket page\t"
            + r.stdout.splitlines()[0].split("\t")[2]
        ]


class TestGrepFallback:
    def test_fallback_over_cache_is_quiet(self, tmp_path):
        cache = tmp_path / "cache"
        cache.mkdir()
        for i in range(30):
            (cache / f"claude-code__fixture-{i:02d}.md").write_text(
                "placeholder line about widgets\n" * 3
            )
        env = {
            "PATH": "/usr/bin:/bin",
            "CLAUDE_DOCS_INDEX": str(tmp_path / "missing.json"),
            "CLAUDE_DOCS_CACHE_DIR": str(cache),
        }
        r = run_search(env, "widgets")
        assert r.returncode == 0
        assert r.stderr == "", r.stderr
        lines = r.stdout.splitlines()
        assert len(lines) == 20 and all(line.split("\t")[1] == "" for line in lines)
