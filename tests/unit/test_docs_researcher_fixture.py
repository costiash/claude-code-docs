"""The commands the docs-researcher agent quotes work against a docs root.

Six invented pages (placeholder words, no documentation text) form a manifest,
a search index, and a cache. Every content-search, fuzzy-search, and jq
command written in plugin/agents/docs-researcher.md is extracted from the
prompt, pointed at that root, and executed; a prompt that quotes a command
that does not run, or names a field that does not exist, fails here.
"""

import hashlib
import json
import os
import re
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent.parent
AGENT = ROOT / "plugin" / "agents" / "docs-researcher.md"

pytestmark = pytest.mark.skipif(
    not shutil.which("jq") or not shutil.which("bash") or not shutil.which("git"),
    reason="requires jq + bash + git",
)

# A curl stand-in that "downloads" a page by copying it out of the fixture
# cache, so the quoted `fetch-docs.sh get` line runs offline.
FAKE_CURL = """#!/usr/bin/env python3
import json, os, shutil, sys
args = sys.argv[1:]
out = args[args.index("-o") + 1]
url = [a for a in args if a.startswith("https://")][0]
root = os.environ["FIXTURE_ROOT"]
pages = json.load(open(os.path.join(root, "paths_manifest.json")))["pages"]
page = next(p for p in pages if p["md_url"] == url)
shutil.copy(os.path.join(root, "pages", page["filename"]), out)
"""

PAGES = [  # (id, host, category, title, body words)
    ("claude-code/widget-hooks", "code.claude.com", "claude_code", "Widget hooks", "hook widget gadget"),
    ("claude-code/widget-config", "code.claude.com", "claude_code", "Widget configuration", "config widget sprocket"),
    ("claude-code/agent-sdk/widget", "code.claude.com", "agent_sdk", "Widget SDK", "sdk widget"),
    ("docs/en/api/widget-messages", "platform.claude.com", "api_reference", "Widget messages API", "api widget message"),
    ("docs/en/build-with-claude/gadgets", "platform.claude.com", "core_documentation", "Gadget guide", "gadget guide"),
    ("docs/en/about-claude/sprockets", "platform.claude.com", "about_claude", "Sprocket overview", "sprocket overview"),
]


@pytest.fixture()
def docs_root(tmp_path):
    root = tmp_path / "docs-root"
    (root / "cache").mkdir(parents=True)
    (root / "pages").mkdir()  # what the fake curl "downloads" from
    manifest, index = [], []
    for pid, host, category, title, words in PAGES:
        filename = pid.replace("/", "__") + ".md"
        body = f"# {title}\n\nplaceholder {words} placeholder\n"
        (root / "cache" / filename).write_text(body)
        (root / "pages" / filename).write_text(body)
        url = f"https://{host}/{pid}"
        manifest.append({"id": pid, "filename": filename, "url": url, "md_url": url + ".md",
                         "title": title, "category": category, "lastmod": None,
                         "sha256": hashlib.sha256(body.encode()).hexdigest(), "fetch_status": "ok"})
        index.append({"filename": filename, "id": pid, "title": title, "category": category,
                      "url": url, "headings": [{"text": title, "level": 1}],
                      "terms": {w: 3 for w in words.split()}, "word_count": 5})
    (root / "paths_manifest.json").write_text(json.dumps({"schema_version": 2, "pages": manifest}))
    (root / "search_index.json").write_text(json.dumps({"schema_version": 2, "pages": index}))
    (root / "plugin").symlink_to(ROOT / "plugin")
    bindir = root / "bin"
    bindir.mkdir()
    (bindir / "curl").write_text(FAKE_CURL)
    (bindir / "curl").chmod(0o755)
    # One commit so manifest-diff.sh has a history to diff against.
    env = {"GIT_CONFIG_GLOBAL": "/dev/null", "GIT_CONFIG_SYSTEM": "/dev/null",
           "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
           "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t", "PATH": "/usr/bin:/bin"}
    for args in (["init", "-q"], ["add", "paths_manifest.json", "search_index.json"], ["commit", "-qm", "fixture"]):
        subprocess.run(["git", *args], cwd=root, env=env, check=True, capture_output=True)
    return root


def env_for(root):
    return {
        "PATH": f"{root / 'bin'}{os.pathsep}/usr/bin:/bin",
        "FIXTURE_ROOT": str(root),
        "CLAUDE_DOCS_CLONE": str(root),
        "CLAUDE_DOCS_MANIFEST": str(root / "paths_manifest.json"),
        "CLAUDE_DOCS_INDEX": str(root / "search_index.json"),
        "CLAUDE_DOCS_CACHE_DIR": str(root / "cache"),
    }


def quoted_commands():
    """Every backticked command in the agent prompt that names a plugin
    script or jq: the two search scripts, fetch-docs get, manifest-diff."""
    body = AGENT.read_text().split("---\n", 2)[2]
    cmds = re.findall(r"`((?:bash ~/\.claude-code-docs/plugin/[^`]*\.sh|jq )[^`]*)`", body)
    assert len(cmds) >= 5, cmds
    assert any("fetch-docs.sh get" in c for c in cmds) and any("manifest-diff.sh" in c for c in cmds)
    return cmds


def run(root, cmd):
    cmd = cmd.replace("~/.claude-code-docs", str(root))
    for ph, val in (('"<keyword>" "<keyword>"', '"widget" "hooks"'), ('"<term>"', '"widget hooks"'),
                    ('"<filename>"', '"claude-code__widget-hooks.md"')):
        cmd = cmd.replace(ph, val)
    return subprocess.run(["bash", "-c", cmd], env=env_for(root), capture_output=True, text=True, timeout=60)


class TestQuotedCommandsRun:
    def test_every_quoted_command_runs_against_the_root(self, docs_root):
        for cmd in quoted_commands():
            r = run(docs_root, cmd)
            assert r.returncode == 0, f"{cmd!r}\nstderr: {r.stderr}"
            if "fetch-docs.sh get" not in cmd:  # get is silent on success
                assert r.stdout.strip(), f"{cmd!r} produced no output"

    def test_quoted_get_refetches_the_page_by_manifest_url(self, docs_root):
        cmd = next(c for c in quoted_commands() if "fetch-docs.sh get" in c)
        target = docs_root / "cache" / "claude-code__widget-hooks.md"
        target.unlink()  # a cache miss, as the prompt describes
        r = run(docs_root, cmd)
        assert r.returncode == 0, r.stderr
        assert target.read_text().startswith("# Widget hooks")

    def test_quoted_manifest_diff_yields_the_json_shape(self, docs_root):
        cmd = next(c for c in quoted_commands() if "manifest-diff.sh" in c)
        r = run(docs_root, cmd)
        data = json.loads(r.stdout)
        assert set(data) >= {"added", "changed", "removed"}

    def test_content_search_ranks_the_hooks_page_first(self, docs_root):
        cmd = next(c for c in quoted_commands() if "content-search.sh" in c)
        r = run(docs_root, cmd)
        first = r.stdout.splitlines()[0].split("\t")
        assert first[0] == "claude-code__widget-hooks.md" and first[1] == "Widget hooks"
        assert r.stderr == ""

    def test_fuzzy_search_finds_by_name(self, docs_root):
        cmd = next(c for c in quoted_commands() if "fuzzy-search.sh" in c)
        r = run(docs_root, cmd)
        assert "claude-code__widget-hooks" in r.stdout.splitlines()[0]

    def test_manifest_lookup_spans_both_hosts(self, docs_root):
        """The agent is told to read across both hosts; the manifest fields it
        relies on (category, filename, url) exist and separate the hosts."""
        cmd = next(c for c in quoted_commands() if "jq -r" in c and "category" in c)
        r = run(docs_root, cmd)
        assert r.stdout.split() == ["claude-code__widget-hooks.md", "claude-code__widget-config.md"]
        hosts = subprocess.run(
            ["jq", "-r", '.pages[].url | split("/")[2]', str(docs_root / "paths_manifest.json")],
            capture_output=True, text=True,
        ).stdout.split()
        assert set(hosts) == {"code.claude.com", "platform.claude.com"}

    def test_cache_read_and_url_copy(self, docs_root):
        """Reading a cached page by filename and citing its verbatim url works
        for every fixture page, on both hosts."""
        manifest = json.loads((docs_root / "paths_manifest.json").read_text())["pages"]
        for entry in manifest:
            text = (docs_root / "cache" / entry["filename"]).read_text()
            assert text.startswith(f"# {entry['title']}")
            assert entry["url"].startswith("https://") and "<" not in entry["url"]
