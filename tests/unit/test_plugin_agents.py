"""Contract tests for the plugin's shipped subagents (plugin/agents/*.md).

Every agent must parse as YAML frontmatter + markdown body, use only the
frontmatter fields Claude Code supports for plugin agents, pin the model the
maintainer chose, and carry the docs-access, citation, and locality contract
that makes its answers grounded in the live documentation.
"""

from pathlib import Path

import pytest
import yaml

AGENTS_DIR = Path(__file__).parent.parent.parent / "plugin" / "agents"
CLAUDE_DOCS_SKILL = (
    Path(__file__).parent.parent.parent / "plugin" / "skills" / "claude-docs" / "SKILL.md"
)

ALLOWED_FIELDS = {
    "name", "description", "model", "effort", "maxTurns", "tools", "disallowedTools",
    "skills", "memory", "background", "omitClaudeMd", "isolation",
}
FORBIDDEN_FIELDS = {"hooks", "mcpServers", "permissionMode"}
PINNED_MODEL = "opus"

# The docs-access primitives every agent must name (spec 0.2).
PRIMITIVES = [
    "plugin/skills/claude-docs/scripts/content-search.sh",
    "plugin/skills/claude-docs/scripts/fuzzy-search.sh",
    "plugin/scripts/fetch-docs.sh get",
    "plugin/scripts/manifest-diff.sh",
    "paths_manifest.json",
]
LOCALITY_SENTENCE = "You run locally."
SOURCES_HEADING = "## Sources"

# Per-agent contract phrases. The set of rows must equal the set of shipped
# agents: a new agent without a row, or a row whose agent was removed, fails
# test_every_agent_is_registered.
REQUIRED_PHRASES = {}


def _agent_files():
    if not AGENTS_DIR.is_dir():
        return []
    return sorted(p for p in AGENTS_DIR.glob("*.md"))


def load_agent(path: Path):
    text = path.read_text()
    assert text.startswith("---\n"), f"{path.name}: no frontmatter"
    _, front, body = text.split("---\n", 2)
    meta = yaml.safe_load(front)
    assert isinstance(meta, dict), f"{path.name}: frontmatter is not a mapping"
    return meta, body


AGENTS = _agent_files()
_params = [pytest.param(p, id=p.stem) for p in AGENTS] or [
    pytest.param(None, id="none", marks=pytest.mark.skip(reason="no agents shipped yet"))
]


def test_agents_dir_is_scaffolded():
    assert AGENTS_DIR.is_dir()


def test_every_agent_is_registered():
    shipped = {p.stem for p in AGENTS}
    unregistered = shipped - set(REQUIRED_PHRASES)
    assert not unregistered, f"agents without a REQUIRED_PHRASES row: {unregistered}"
    orphaned = set(REQUIRED_PHRASES) - shipped
    assert not orphaned, f"REQUIRED_PHRASES rows without an agent file: {orphaned}"


@pytest.mark.parametrize("path", _params)
class TestAgentContract:
    def test_frontmatter_fields(self, path):
        meta, _ = load_agent(path)
        assert meta["name"] == path.stem
        assert meta.get("description", "").strip()
        assert meta.get("model") == PINNED_MODEL
        # Forbidden first, so a field Claude Code rejects for plugin agents gets
        # its own message; anything else outside the supported set fails next.
        assert not (set(meta) & FORBIDDEN_FIELDS), (
            f"unsupported for plugin agents: {set(meta) & FORBIDDEN_FIELDS}"
        )
        assert set(meta) <= ALLOWED_FIELDS, f"unknown fields: {set(meta) - ALLOWED_FIELDS}"
        # type() not isinstance(): bool is an int subclass and must not pass.
        assert type(meta.get("maxTurns")) is int and meta["maxTurns"] > 0
        raw = meta.get("disallowedTools", "")
        # Comma-separated string is the documented form; a YAML list is tolerated.
        disallowed = {str(t).strip() for t in (raw if isinstance(raw, list) else str(raw).split(","))}
        assert {"Write", "Edit", "NotebookEdit"} <= disallowed

    def test_docs_access_contract(self, path):
        _, body = load_agent(path)
        for primitive in PRIMITIVES:
            assert primitive in body, f"{path.name} does not name {primitive}"
        assert "cache/" in body  # reads the local cache first
        assert "WebFetch" in body  # the never-WebFetch-a-manifest-page rule
        assert SOURCES_HEADING in body
        assert LOCALITY_SENTENCE in body
        assert "unverified" in body  # failure-honesty flag

    def test_agent_specific_phrases(self, path):
        _, body = load_agent(path)
        if path.stem not in REQUIRED_PHRASES:
            pytest.fail(f"{path.name} has no REQUIRED_PHRASES row")
        for phrase in REQUIRED_PHRASES[path.stem]:
            assert phrase in body, f"{path.name} lacks required phrase {phrase!r}"


class TestDelegationRule:
    """The claude-docs skill delegates multi-page work to docs-researcher."""

    @pytest.mark.skipif(
        not (AGENTS_DIR / "docs-researcher.md").exists(), reason="docs-researcher not shipped yet"
    )
    def test_skill_documents_the_heuristic(self):
        text = CLAUDE_DOCS_SKILL.read_text()
        section = text.split("## Delegation", 1)
        assert len(section) == 2, "claude-docs SKILL.md has no ## Delegation section"
        rule = section[1].split("\n## ", 1)[0]
        assert "claude-docs:docs-researcher" in rule
        for trigger in ("3 pages", "API", "comparison", "everything about"):
            assert trigger in rule, f"delegation rule lacks trigger {trigger!r}"
