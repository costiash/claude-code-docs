# Claude Code Documentation Index

This repository indexes Claude documentation from two Anthropic sources but **commits no
documentation prose** — only metadata. End users fetch the actual `.md` pages from
Anthropic's servers at runtime into a local cache.

- **Platform docs**: https://platform.claude.com (API, guides, Agent SDK, etc.)
- **Claude Code docs**: https://code.claude.com/docs (CLI-specific documentation)

The metadata (`paths_manifest.json` + `search_index.json`) is regenerated via GitHub
Actions every 3 hours with safeguards against catastrophic manifest changes.

> **Read `ARCHITECTURE.md` first** for the full v2 design (manifest schema, index schema,
> fetch pipeline, safeguards, cache layout, and the no-committed-content invariant).

## Architecture: Plugin-Based Documentation System

This repository delivers documentation via a **Claude Code plugin**. The plugin provides:

- **`/docs` command** — Routes queries to the appropriate skill
- **`claude-docs/` skill** — Auto-discovery + search (content search, fuzzy matching, direct lookups)
- **`claude-docs-validate/` skill** — Documentation health checks and freshness validation
- **SessionStart hook** — Auto-updates docs via `git reset --hard origin/main` on each session start

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
│   ├── claude-docs-validate/     # Validation skill
│   │   ├── SKILL.md              # Health check instructions
│   │   ├── examples/             # Worked examples
│   │   └── scripts/              # validate-paths.sh
│   ├── claude-docs-course/       # Interactive course generator
│   │   ├── SKILL.md              # Course generation workflow (Obsidian & Amber theme)
│   │   ├── references/           # design-system.md, interactive-elements.md
│   │   └── examples/             # Worked examples
│   └── claude-docs-changelog/    # Changelog report generator (SKILL.md + examples/)
└── hooks/                        # SessionStart auto-sync
```

Search intelligence lives in the skills, not in CLAUDE.md. See `plugin/skills/claude-docs/SKILL.md` for search strategy details.

## For /docs Command

The `/docs` command is handled by the plugin's lean router at `plugin/commands/docs.md`. It delegates to:

- **`claude-docs` skill** — For all documentation lookups, questions, and searches
- **`claude-docs-validate` skill** — For freshness checks (`-t`) and health validation
- **`claude-docs-course` skill** — For interactive course generation (`--course <topic>`)
- **`claude-docs-changelog` skill** — For HTML changelog reports (`--report`)
- **Inline git log** — For "what's new" queries

Search intelligence, synthesis rules, and URL generation live in `plugin/skills/claude-docs/SKILL.md`. Category mappings are in `plugin/skills/claude-docs/manifest-reference.md` (single source of truth).

## CI/CD Scripts (Python, repo-only)

The `scripts/` directory contains Python modules that run in GitHub Actions — they are **not** user-facing and are **not** installed with the plugin:

- `scripts/fetcher/` — Discovers pages (llms.txt ∪ sitemaps), fetches `.md` verbatim into the gitignored `.doc_fetch/` scratch, and writes the v2 `paths_manifest.json` (every 3 hours). Modules: `llms_txt`, `sitemap`, `discovery`, `paths`, `content`, `manifest`, `safeguards`, `config`, `cli`.
- `scripts/build_search_index.py` — Generates the prose-free root `search_index.json` from the scratch dir + manifest
- `scripts/fetch_claude_docs.py` — Thin wrapper for the fetcher package

These require Python 3.9+ and are only executed in GitHub Actions workflows. The legacy
`scripts/lookup/` search package was removed — client search is now shell-only (see plugin).

## Repository Structure

```
/
├── paths_manifest.json     # v2 manifest — single source of truth (committed)
├── search_index.json       # v2 prose-free search index (committed)
├── .doc_fetch/             # ephemeral CI fetch scratch (gitignored, never committed)
├── docs/                   # legacy/scratch only — gitignored, not tracked
├── scripts/                # CI-only Python scripts
│   ├── fetch_claude_docs.py        # Thin wrapper for fetcher
│   ├── build_search_index.py       # v2 index builder (scratch + manifest -> index)
│   └── fetcher/                    # Fetching package: llms_txt, sitemap, discovery,
│                                   #   paths, content, manifest, safeguards, config, cli
├── plugin/                 # Claude Code Plugin
│   ├── .claude-plugin/plugin.json  # Plugin metadata
│   ├── commands/docs.md            # /docs slash command (lean router)
│   ├── scripts/                    # Client shell layer (bash+curl+jq, zero Python)
│   │   ├── fetch-docs.sh           #   sync/get/status/prune -> cache
│   │   └── manifest-diff.sh        #   git-history diff for what's-new/changelog
│   ├── skills/
│   │   ├── claude-docs/            # Search skill + scripts (content-search, fuzzy-search)
│   │   ├── claude-docs-validate/   # Validation skill + validate-paths.sh
│   │   ├── claude-docs-course/     # Interactive course generator + references
│   │   └── claude-docs-changelog/  # Changelog report generator + examples
│   └── hooks/                      # SessionStart hook (reset --hard + background sync)
├── .claude-plugin/marketplace.json # Marketplace registration
├── ARCHITECTURE.md         # v2 design (read this first)
├── IMPLEMENTATION_PLAN.md  # Redistribution rework checklist
├── pyproject.toml          # Python project configuration
├── CHANGELOG.md            # Version history
├── tests/                  # Test suite (CI-only)
├── install.sh              # Metadata-clone + cache sync (non-plugin fallback)
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
- `plugin/skills/claude-docs-course/SKILL.md` - Interactive course generator (Obsidian & Amber theme)
- `plugin/skills/claude-docs-course/references/design-system.md` - Course visual design tokens
- `plugin/skills/claude-docs-course/references/interactive-elements.md` - HTML/CSS/JS patterns for course elements
- `plugin/skills/claude-docs-changelog/SKILL.md` - Changelog report generator (Obsidian & Amber theme)
- `plugin/skills/claude-docs-validate/scripts/validate-paths.sh` - HTTP reachability checks
- `plugin/hooks/hooks.json` + `sync-docs.sh` - SessionStart hook (auto-update docs)
- `.claude-plugin/marketplace.json` - Marketplace registration

### CI/CD Scripts (Python)
- `scripts/fetch_claude_docs.py` - Documentation fetcher entry point (thin wrapper)
- `scripts/fetcher/` - Fetching package: `llms_txt`, `sitemap`, `discovery`, `paths`, `content`, `manifest`, `safeguards`, `config`, `cli`
- `scripts/build_search_index.py` - v2 prose-free index builder
- `paths_manifest.json` - v2 manifest (single source of truth)
- `search_index.json` - v2 prose-free search index
- `plugin/scripts/fetch-docs.sh` - Client cache fetcher (sync/get/status/prune)
- `plugin/scripts/manifest-diff.sh` - Manifest git-history diff (what's-new/changelog)
- `tests/` - Test suite (covers CI scripts + shell scripts via mocked-curl harness)

### Automation
- `.github/workflows/` - Auto-update workflows (runs every 3 hours)

## Documentation Deletion Safeguards

The automated sync system includes multiple safeguards to prevent catastrophic documentation loss. These were implemented after a critical bug where 80%+ of documentation was deleted due to broken sitemap URLs.

### Safety Thresholds (in `scripts/fetcher/config.py`)

| Constant | Value | Purpose |
|----------|-------|---------|
| `MIN_DISCOVERY_THRESHOLD` | 200 | Minimum pages that must be discovered (llms.txt ∪ sitemaps) |
| `MAX_DELETION_PERCENT` | 10 | Max % of manifest entries a single sync may remove |
| `MIN_EXPECTED_FILES` | 250 | Minimum pages that must remain in the manifest |

### How Safeguards Work (`scripts/fetcher/safeguards.py`)

1. **Discovery Validation**: `validate_discovery_threshold()` aborts if discovery found < 200 pages
2. **Transition Guard**: `validate_manifest_transition(old, new)` aborts if > 10% of entries are removed or < 250 remain — first-run-safe (no v2 predecessor = clean start)
3. **Carry-forward**: a page that fails to fetch is kept in the manifest (`fetch_status: stale`), never dropped on a transient error
4. **Workflow Validation**: `update-docs.yml` repeats the ≥250 floor as a jq check before committing

### Discovery Sources

Pages are discovered from the **union** of two llms.txt files and two sitemaps (keyed by
canonical URL; llms.txt supplies titles/coverage, sitemaps supply `lastmod`):
- `https://code.claude.com/docs/llms.txt` + `https://code.claude.com/docs/sitemap.xml`
- `https://platform.claude.com/llms.txt` + `https://platform.claude.com/sitemap.xml`

### Filename Conventions

Files are named based on their source:
- Claude Code CLI docs: `claude-code__<page>.md` (e.g., `claude-code__hooks.md`) → `https://code.claude.com/docs/en/<page>`
- Platform docs: `docs__en__<section>__<page>.md` (e.g., `docs__en__agent-sdk__python.md`) → `https://platform.claude.com/docs/en/<section>/<page>`

## Working on This Repository

### Development Setup
```bash
# Install Python dependencies for CI scripts (uses uv)
uv sync --group dev
```

### Testing
```bash
# Test plugin search scripts manually (they resolve the manifest/index from the repo root)
./plugin/skills/claude-docs/scripts/content-search.sh hooks matcher
./plugin/skills/claude-docs/scripts/fuzzy-search.sh agent sdk python
./plugin/skills/claude-docs-validate/scripts/validate-paths.sh --quick

# Regenerate metadata locally (fetches into gitignored .doc_fetch/, then builds the index)
DOCS_FETCH_LIMIT=8 python3 scripts/fetch_claude_docs.py   # fast preview (writes .preview manifest to scratch)
python3 scripts/fetch_claude_docs.py                      # full run (~10 min; writes real paths_manifest.json)
python3 scripts/build_search_index.py                     # build search_index.json from scratch

# Run the test suite
pytest tests/ -q -m "not network"
```
