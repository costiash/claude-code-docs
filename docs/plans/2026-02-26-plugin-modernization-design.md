# Design: Plugin Modernization — Pure Claude Code Architecture

**Date**: 2026-02-26
**Status**: Approved
**Author**: @costiash + Claude

## Problem Statement

The claude-code-docs project currently serves 338+ active users (24 unique cloners/day) via a shell-script-based architecture (`curl | bash` installation). While functional, the project has:

1. **Broken features masked by Claude's intelligence** — `paths_manifest.json` never committed by CI/CD (stale since Dec 2025), `.search_index.json` never auto-generated, issue #15 (absolute path bug)
2. **Architecture misaligned with Claude Code's native extensibility** — Uses shell wrappers and Python scripts where Claude Code now offers Skills, Plugins, Hooks, and Commands natively

## Goal

Transform the project from a shell-script-based tool into a native Claude Code Plugin, while:
- Fixing current bugs immediately (no disruption to existing users)
- Providing a gradual migration path (no breaking changes until v1.0)
- Eliminating shell/Python dependencies for end users entirely

## Design Decisions

### Decision 1: Eliminate Shell Scripts Entirely (for Users)

**Rationale**: Claude Code's native tools (Read, Grep, Glob) do what the shell wrapper scripts do. Claude IS the search engine — it doesn't need pre-built search wrappers.

**What stays**: Python scripts for CI/CD only (fetcher pipeline, search index builder).
**What goes**: `claude-docs-helper.sh`, `claude-docs-helper.sh.template`, `install.sh`, `uninstall.sh`, `scripts/lookup/` (for local use).

### Decision 2: Python for CI/CD Only

**Rationale**: The heavy work (sitemap discovery, bulk fetching, safety validation) already runs in GitHub Actions. Users never need Python locally. This eliminates the biggest UX friction ("requires Python 3.9+").

### Decision 3: Plugin-Based Distribution

**Rationale**: Claude Code's plugin system is the native distribution mechanism. Plugins bundle commands, skills, and hooks together with clean install/uninstall.

### Decision 4: Separate Plugin (Logic) from Docs (Data)

**Rationale**: Docs update every 3 hours via CI/CD. Plugins are static snapshots. Bundling volatile data inside a static plugin is architecturally wrong. The plugin provides logic (Skill, Command, Hook); the docs live in a git clone at `~/.claude-code-docs/`.

### Decision 5: Dual Interface (Command + Skill)

**Rationale**: `/docs` for explicit access (users expect it), Skill for auto-discovery (Claude finds relevant docs when user asks about Claude Code features).

### Decision 6: Phased Migration (Not Breaking)

**Rationale**: 338+ active users installed via `curl | bash`. A clean break would disrupt them. Four phases allow gradual transition.

### Decision 7: No Hardcoded Doc Counts

**Rationale**: The actual number of docs drifts constantly (571 in local repo, 586 in installed copy, 574 on remote). All references must use dynamic discovery.

## Architecture

### Two-Layer System

```
LAYER 1: Plugin (static, distributed via marketplace)
  commands/docs.md     → /docs slash command
  skills/SKILL.md      → auto-discovery by Claude
  hooks/hooks.json     → SessionStart: git pull docs

LAYER 2: Docs Data (dynamic, git-cloned separately)
  ~/.claude-code-docs/docs/       → markdown files (CI/CD updated)
  ~/.claude-code-docs/docs/docs_manifest.json  → file tracking
  ~/.claude-code-docs/paths_manifest.json      → path categories
```

### Data Flow

```
Anthropic Sitemaps (platform.claude.com, code.claude.com)
    ↓ CI/CD every 3 hours
scripts/fetcher/ → discovers paths, fetches markdown, updates manifests
    ↓ git commit + push
docs/*.md + docs_manifest.json + paths_manifest.json on main
    ↓ SessionStart hook (user's session)
git pull → ~/.claude-code-docs/ stays fresh
    ↓ User interaction
/docs command or Skill → Claude reads docs via Read/Grep/Glob
    ↓
Synthesized answer with sources
```

### Plugin Structure (Phase 2+)

```
costiash/claude-code-docs/
├── .claude-plugin/
│   └── marketplace.json
├── plugin/
│   ├── .claude-plugin/
│   │   └── plugin.json
│   ├── commands/
│   │   └── docs.md
│   ├── skills/
│   │   └── claude-docs/
│   │       ├── SKILL.md
│   │       └── manifest-reference.md
│   └── hooks/
│       └── hooks.json
├── docs/                    (unchanged — CI/CD managed)
├── scripts/                 (CI/CD only)
├── tests/                   (CI/CD only)
├── .github/workflows/       (unchanged)
├── install.sh               (kept through Phase 3, removed Phase 4)
└── paths_manifest.json      (fixed commit bug)
```

## Branch Strategy

Two development branches, isolated by scope:

### `fix/phase1-bug-fixes`
- **Purpose**: Phase 1 only — fix broken functionality
- **Branches from**: `main` (current)
- **Merges to**: `main` (fast, low risk)
- **Scope**: CI/CD fixes, no structural changes

### `feat/plugin-modernization`
- **Purpose**: Phases 2-4 — plugin structure, migration, cleanup
- **Branches from**: `main` (after Phase 1 merged)
- **Merges to**: `main` (via PR, after testing)
- **Scope**: New plugin directory, Skills, Commands, Hooks

## Phased Implementation

### Phase 1: v0.5.1 — Bug Fixes (Branch: `fix/phase1-bug-fixes`)

**Zero disruption to existing users.**

1. **Fix `paths_manifest.json` commit bug**
   - File: `.github/workflows/update-docs.yml`
   - Change: `git add -A docs/` → `git add -A docs/ paths_manifest.json`
   - Effect: Manifest stays in sync with actual files

2. **Auto-generate `.search_index.json` in CI/CD**
   - File: `.github/workflows/update-docs.yml`
   - Add step: `python scripts/build_search_index.py` after fetch
   - Add to staging: `git add -A docs/ paths_manifest.json`
   - Effect: Content search works for all users

3. **Fix issue #15** — content search with absolute paths
   - Investigate `scripts/lookup/search.py` and `scripts/lookup/cli.py`
   - Fix path handling for installed location

4. **Update hardcoded counts** in documentation
   - Replace static "571 files" / "573 paths" with dynamic language
   - Files: `README.md`, `CLAUDE.md`, `install.sh`, helper scripts

### Phase 2: v0.6.0 — Plugin Addition (Branch: `feat/plugin-modernization`)

**Additive only — nothing removed.**

1. **Create marketplace manifest**
   - File: `.claude-plugin/marketplace.json`
   - Lists the plugin with source pointing to `./plugin`

2. **Create plugin manifest**
   - File: `plugin/.claude-plugin/plugin.json`
   - Name: `claude-docs`
   - Description, version, author metadata

3. **Create `/docs` command (plugin version)**
   - File: `plugin/commands/docs.md`
   - AI-powered routing using Claude's native Read/Grep/Glob
   - No shell script calls — Claude reads docs directly
   - Supports: topic lookup, content search, freshness check, what's new

4. **Create documentation Skill**
   - File: `plugin/skills/claude-docs/SKILL.md`
   - Auto-discovery when user asks about Claude Code features
   - Instructions for filename-based category inference
   - Search strategy using native tools
   - Synthesis instructions (read multiple docs, combine, cite sources)

5. **Create SessionStart hook**
   - File: `plugin/hooks/hooks.json`
   - Script: checks/clones/pulls `~/.claude-code-docs/`
   - Reports available doc count on session start

6. **Update README** with dual installation instructions
   - Plugin method (recommended for new users)
   - Legacy `curl | bash` (still supported)

### Phase 3: v0.7.0 — Migration Nudges

1. **`install.sh` detects plugin availability**
   - If Claude Code plugin system detected, recommend plugin install
   - Still performs legacy install if user proceeds

2. **Legacy `/docs` command shows migration notice**
   - One-time notice suggesting plugin version
   - Non-intrusive, dismissable

3. **README updates**
   - Plugin becomes primary installation method
   - `curl | bash` moved to "Legacy Installation" section

### Phase 4: v1.0.0 — Pure Plugin

1. **Remove shell wrapper scripts**
   - Delete: `scripts/claude-docs-helper.sh`
   - Delete: `scripts/claude-docs-helper.sh.template`

2. **Remove legacy installation**
   - Delete: `install.sh`
   - Delete: `uninstall.sh`

3. **Remove local-use Python packages**
   - Delete: `scripts/lookup/` (Claude does search natively)
   - Keep: `scripts/fetcher/` (CI/CD only)
   - Keep: `scripts/build_search_index.py` (CI/CD only, if search index still useful)

4. **Update tests**
   - Remove tests for deleted shell/Python scripts
   - Add tests for plugin components (if applicable)

5. **Clean up documentation**
   - `CLAUDE.md` reflects plugin-only architecture
   - `CONTRIBUTING.md` updated for new structure

## Manifest Strategy

### Current State (Buggy)

| Manifest | Updated By CI/CD | Committed | Status |
|----------|-----------------|-----------|--------|
| `docs/docs_manifest.json` | Yes (every 3h) | Yes | Working |
| `paths_manifest.json` | Yes (regenerated) | **No (bug!)** | Stale since Dec 2025 |
| `docs/.search_index.json` | **No** | N/A | Never auto-generated |

### After Phase 1

| Manifest | Updated By CI/CD | Committed | Status |
|----------|-----------------|-----------|--------|
| `docs/docs_manifest.json` | Yes (every 3h) | Yes | Working |
| `paths_manifest.json` | Yes (regenerated) | **Yes (fixed)** | Current |
| `docs/.search_index.json` | **Yes (new)** | **Yes (new)** | Generated |

### After Phase 4 (Plugin-Only)

The Skill uses Claude's native tools for search. Manifests continue being generated by CI/CD for:
- `docs/docs_manifest.json` — change detection in fetcher pipeline
- `paths_manifest.json` — category reference (optional, Skill can infer from filenames)
- `docs/.search_index.json` — optional enhancement (Claude can Grep directly)

## Safety Considerations

### Existing User Protection

- Phase 1 changes are backward-compatible CI/CD fixes only
- Phase 2 is additive (new `plugin/` directory, nothing removed)
- Phase 3 adds migration nudges, doesn't force migration
- Phase 4 removes legacy code only after sufficient migration period
- `~/.claude-code-docs/` location stays the same throughout all phases

### CI/CD Safeguards (Unchanged)

- `MIN_DISCOVERY_THRESHOLD`: 200 paths minimum from sitemaps
- `MAX_DELETION_PERCENT`: 10% max files deleted per sync
- `MIN_EXPECTED_FILES`: 250 files minimum after sync
- Workflow-level validation with auto-revert

## Success Criteria

### Phase 1
- [ ] `paths_manifest.json` updates on every CI/CD run
- [ ] `.search_index.json` generated on every CI/CD run
- [ ] Issue #15 resolved
- [ ] All 294 existing tests pass
- [ ] No disruption to existing users

### Phase 2
- [ ] Plugin installable via `/plugin marketplace add costiash/claude-code-docs`
- [ ] `/docs` command works via plugin
- [ ] Skill auto-discovers when user asks about Claude features
- [ ] SessionStart hook clones/updates docs
- [ ] Legacy `curl | bash` still works alongside plugin

### Phase 3
- [ ] `install.sh` suggests plugin to users with Claude Code plugin support
- [ ] Migration path clearly documented

### Phase 4
- [ ] All shell wrapper scripts removed
- [ ] Plugin is only installation method
- [ ] Zero Python dependency for end users
- [ ] CI/CD continues functioning with fetcher pipeline

## Open Questions

1. **Search index in Phase 4**: When Claude does content search natively via Grep, is the pre-built `.search_index.json` still useful? Could be removed to simplify CI/CD.
2. **Plugin update frequency**: How often do users need to run `/plugin marketplace update`? Should the SessionStart hook handle this?
3. **Offline support**: Current `curl | bash` works fully offline after install. Plugin + git clone also works offline. Confirm this is acceptable.
4. **`paths_manifest.json` long-term**: In Phase 4, should the Skill rely on the manifest for categories or infer from filename patterns? Manifest is more accurate but requires maintenance; patterns are zero-maintenance but could drift.
