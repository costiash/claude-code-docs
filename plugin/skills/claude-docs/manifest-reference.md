# Documentation Manifest Reference

## Overview

The clone at `~/.claude-code-docs/` contains only metadata (no prose):
- `paths_manifest.json` — the page index: per page `{id, filename, url, md_url, title, category, sha256, lastmod, fetch_status}` (updated by CI/CD every 3h)
- `search_index.json` — per-page titles, headings, and stemmed term counts
- Fetched `.md` pages are cached at `~/.claude-code-docs/cache/` (override `$CLAUDE_DOCS_CACHE_DIR`)

## Categories

Documentation is organized into these categories:

| Category | Description | File Pattern |
|----------|------------|-------------|
| `claude_code` | Claude Code CLI docs | `claude-code__*.md` |
| `agent_sdk` | Agent SDK (Python, TypeScript) | `claude-code__agent-sdk__*.md` (on code.claude.com) |
| `api_reference` | API endpoints, SDK docs | `docs__en__api__*.md` |
| `agents_and_tools` | MCP, tool use, agent skills | `docs__en__agents-and-tools__*.md` |
| `core_documentation` | Guides, tutorials | `docs__en__build-with-claude__*.md` |
| `about_claude` | Model info, capabilities | `docs__en__about-claude__*.md` |
| `get_started` | Quickstart guides | `docs__en__get-started.md` |
| `test_and_evaluate` | Evals, testing guides | `docs__en__test-and-evaluate__*.md` |
| `prompt_library` | Prompt templates | `docs__en__resources__prompt-library__*.md` |
| `release_notes` | Changelog | `docs__en__release-notes__*.md` |
| `resources` | Additional resources | `docs__en__resources__overview.md` |

## User-Friendly Labels

When presenting results to users:
- `claude_code` → "Claude Code CLI"
- `agent_sdk` → "Claude Agent SDK"
- `api_reference` → "Claude API"
- `agents_and_tools` → "Agents & Tools"
- `core_documentation` → "Claude Documentation"
- `about_claude` → "About Claude"
- `get_started` → "Getting Started"
- `test_and_evaluate` → "Testing & Evaluation"
- `prompt_library` → "Prompt Library"
- `release_notes` → "Release Notes"
- `resources` → "Resources"

## URL Construction

**Do not reconstruct URLs from filenames** — filenames are lossy and hosts vary
(agent-sdk lives on code.claude.com, not platform). The manifest stores the exact,
verbatim source URL for every page. Look it up:

```bash
jq -r '.pages[] | select(.filename=="<filename>") | .url' ~/.claude-code-docs/paths_manifest.json
```

Example: `claude-code__hooks.md` → `https://code.claude.com/docs/en/hooks`.

## Dynamic Discovery

Count indexed pages:
```bash
jq '.pages | length' ~/.claude-code-docs/paths_manifest.json
```

Per-category counts:
```bash
jq -r '.pages[].category' ~/.claude-code-docs/paths_manifest.json | sort | uniq -c | sort -rn
```
