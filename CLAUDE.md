# Claude Code Documentation Mirror - Enhanced Edition

> **⛔ CRITICAL: UPSTREAM ISOLATION ⛔**
>
> **This repository is COMPLETELY INDEPENDENT. Do NOT:**
> - Push to, pull from, or sync with the upstream repo (ericbuess/claude-code-docs)
> - Create PRs to the upstream repo
> - Add upstream as a remote
> - Reference upstream in any git operations
>
> **All git operations must target `origin` (costiash/claude-code-docs) ONLY.**

This repository contains local copies of Claude documentation from multiple Anthropic sources:
- **Platform docs**: https://platform.claude.com (API, guides, Agent SDK, etc.)
- **Claude Code docs**: https://code.claude.com/docs (CLI-specific documentation)

The docs are periodically updated via GitHub Actions with safeguards to prevent mass deletion.

## Architecture: Plugin-Based Documentation System

This repository delivers documentation via a **Claude Code plugin**. The plugin provides:

- **`/docs` command** — Routes queries to the appropriate skill
- **`claude-docs/` skill** — Auto-discovery + search (content search, fuzzy matching, direct lookups)
- **`claude-docs-validate/` skill** — Documentation health checks and freshness validation
- **SessionStart hook** — Auto-updates docs via `git pull` on each session start

### Plugin Structure

```
plugin/
├── commands/docs.md              # /docs command (lean router)
├── skills/
│   ├── claude-docs/              # Search skill (auto-discovery)
│   │   ├── SKILL.md              # Search strategy and synthesis rules
│   │   ├── manifest-reference.md # Category-to-label mapping (single source of truth)
│   │   ├── examples/             # Worked examples for Claude
│   │   └── scripts/              # content-search.sh, fuzzy-search.sh
│   └── claude-docs-validate/     # Validation skill
│       ├── SKILL.md              # Health check instructions
│       ├── examples/             # Worked examples
│       └── scripts/              # validate-paths.sh
└── hooks/                        # SessionStart auto-sync
```

Search intelligence lives in the skills, not in CLAUDE.md. See `plugin/skills/claude-docs/SKILL.md` for search strategy details.

## For /docs Command

The `/docs` command is handled by the plugin's lean router at `plugin/commands/docs.md`. It delegates to:

- **`claude-docs-search` skill** — For all documentation lookups, questions, and searches
- **`claude-docs-validate` skill** — For freshness checks (`-t`) and health validation
- **Inline git log** — For "what's new" queries

Search intelligence, synthesis rules, and URL generation live in `plugin/skills/claude-docs/SKILL.md`. Category mappings are in `plugin/skills/claude-docs/manifest-reference.md` (single source of truth).

## CI/CD Scripts (Python, repo-only)

The `scripts/` directory contains Python modules that run in GitHub Actions — they are **not** user-facing and are **not** installed with the plugin:

- `scripts/fetcher/` — Fetches docs from Anthropic sitemaps (every 3 hours)
- `scripts/lookup/` — Path validation for CI checks (daily)
- `scripts/build_search_index.py` — Generates `.search_index.json` consumed by the plugin's content search
- `scripts/fetch_claude_docs.py` — Thin wrapper for fetcher package
- `scripts/lookup_paths.py` — Thin wrapper for lookup package

These require Python 3.9+ and are only executed in GitHub Actions workflows.

## Repository Structure

```
/
├── docs/                   # Documentation files (.md format)
│   ├── docs_manifest.json  # File tracking manifest
│   └── .search_index.json  # Full-text search index (CI-generated)
├── scripts/                # CI-only Python scripts
│   ├── fetch_claude_docs.py        # Thin wrapper for fetcher
│   ├── lookup_paths.py             # Thin wrapper for lookup
│   ├── build_search_index.py       # Index builder
│   ├── fetcher/                    # Documentation fetching package (8 modules)
│   └── lookup/                     # Search and validation package (7 modules)
├── plugin/                 # Claude Code Plugin (v1.0.0)
│   ├── .claude-plugin/plugin.json  # Plugin metadata
│   ├── commands/docs.md            # /docs slash command (lean router)
│   ├── skills/
│   │   ├── claude-docs/            # Search skill + examples + scripts
│   │   └── claude-docs-validate/   # Validation skill + examples + scripts
│   └── hooks/                      # SessionStart hook (auto-update docs)
├── .claude-plugin/marketplace.json # Marketplace registration
├── paths_manifest.json     # Active paths manifest (6 categories)
├── pyproject.toml          # Python project configuration
├── CHANGELOG.md            # Version history
├── tests/                  # Test suite (CI-only, covers Python scripts)
├── reports/                # Coverage and test reports
├── install.sh              # Migration wrapper (routes to plugin install)
├── uninstall.sh            # Points to plugin uninstall
├── index.html              # GitHub Pages landing page
└── CLAUDE.md               # This file (AI context)
```

## Key Files

When working on this repository, read these files as needed (not auto-loaded to save context):

### Plugin Files
- `plugin/.claude-plugin/plugin.json` - Plugin metadata (version, hooks)
- `plugin/commands/docs.md` - `/docs` command (lean router)
- `plugin/skills/claude-docs/SKILL.md` - Search skill (auto-discovery, search strategy, synthesis rules)
- `plugin/skills/claude-docs/manifest-reference.md` - Category-to-label mapping (single source of truth)
- `plugin/skills/claude-docs/scripts/content-search.sh` - Full-text keyword search
- `plugin/skills/claude-docs/scripts/fuzzy-search.sh` - Fuzzy filename matching
- `plugin/skills/claude-docs/examples/` - Worked examples for search workflows
- `plugin/skills/claude-docs-validate/SKILL.md` - Validation skill instructions
- `plugin/skills/claude-docs-validate/scripts/validate-paths.sh` - HTTP reachability checks
- `plugin/hooks/hooks.json` + `sync-docs.sh` - SessionStart hook (auto-update docs)
- `.claude-plugin/marketplace.json` - Marketplace registration

### CI/CD Scripts (Python)
- `scripts/fetch_claude_docs.py` - Documentation fetcher entry point
- `scripts/lookup_paths.py` - Search & validation entry point
- `scripts/fetcher/` - Documentation fetching package (8 modules)
- `scripts/lookup/` - Search & validation package (7 modules)
- `scripts/build_search_index.py` - Full-text search indexing
- `paths_manifest.json` - Active paths manifest (6 categories)
- `tests/` - Test suite (covers CI scripts)

### Automation
- `.github/workflows/` - Auto-update workflows (runs every 3 hours)

## Documentation Deletion Safeguards

The automated sync system includes multiple safeguards to prevent catastrophic documentation loss. These were implemented after a critical bug where 80%+ of documentation was deleted due to broken sitemap URLs.

### Safety Thresholds (in `scripts/fetcher/config.py`)

| Constant | Value | Purpose |
|----------|-------|---------|
| `MIN_DISCOVERY_THRESHOLD` | 200 | Minimum paths that must be discovered from sitemaps |
| `MAX_DELETION_PERCENT` | 10 | Maximum percentage of files that can be deleted in one sync |
| `MIN_EXPECTED_FILES` | 250 | Minimum files that must remain after sync |

### How Safeguards Work

1. **Discovery Validation**: Before fetching, validates that sitemap discovery found enough paths
2. **Deletion Limiting**: `cleanup_old_files()` refuses to delete more than 10% of existing files
3. **File Count Validation**: Refuses to proceed if result would have fewer than 250 files
4. **Workflow Validation**: GitHub Actions validates sync success before committing

### Sitemap Sources

Documentation is discovered from two sitemaps:
- `https://platform.claude.com/sitemap.xml` - Platform documentation (API, guides, etc.)
- `https://code.claude.com/docs/sitemap.xml` - Claude Code CLI documentation

### Filename Conventions

Files are named based on their source:
- Claude Code CLI docs: `claude-code__<page>.md` (e.g., `claude-code__hooks.md`) → `https://code.claude.com/docs/en/<page>`
- Platform docs: `docs__en__<section>__<page>.md` (e.g., `docs__en__agent-sdk__python.md`) → `https://platform.claude.com/en/docs/<section>/<page>`

## Working on This Repository

### Development Setup
```bash
# Install Python dependencies for CI scripts (uses uv)
uv sync --group dev
```

### Testing
```bash
# Test plugin search scripts manually
DOCS_DIR=./docs ./plugin/skills/claude-docs/scripts/content-search.sh "hooks"
DOCS_DIR=./docs ./plugin/skills/claude-docs/scripts/fuzzy-search.sh "agent sdk"
DOCS_DIR=./docs ./plugin/skills/claude-docs-validate/scripts/validate-paths.sh --quick

# Test CI Python scripts
python3 scripts/lookup_paths.py --search "mcp"
pytest tests/ -v

# Run full CI test suite
pytest tests/ -q
```

## Upstream Compatibility

This enhanced edition maintains compatibility with upstream (ericbuess/claude-code-docs):
- Same installation location (~/.claude-code-docs)
- Same `/docs` command interface
- Plugin features are additive, not breaking
