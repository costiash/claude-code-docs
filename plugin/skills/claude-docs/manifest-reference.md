# Documentation Manifest Reference

## Overview

The documentation mirror at `~/.claude-code-docs/` contains:
- `docs/` — Markdown files fetched from Anthropic's documentation sites
- `docs/docs_manifest.json` — File tracking manifest (updated by CI/CD)
- `paths_manifest.json` — Path categorization manifest (updated by CI/CD)

## Categories

Documentation is organized into these categories:

| Category | Description | File Pattern |
|----------|------------|-------------|
| `claude_code` | Claude Code CLI docs | `docs__en__*.md` |
| `api_reference` | API endpoints, SDK docs | `en__api__*.md` |
| `core_documentation` | Guides, tutorials | `en__docs__build-with-claude__*.md` |
| `prompt_library` | Prompt templates | `en__resources__prompt-library__*.md` |
| `release_notes` | Changelog | `en__release-notes__*.md` |
| `resources` | Additional resources | `en__resources__overview.md` |

## User-Friendly Labels

When presenting results to users:
- `claude_code` → "Claude Code CLI"
- `api_reference` → "Claude API"
- Agent SDK paths → "Claude Agent SDK"
- `core_documentation` → "Claude Documentation"
- `prompt_library` → "Prompt Library"

## Dynamic Discovery

To count available docs:
```
Glob: ~/.claude-code-docs/docs/*.md
```

To check categories in manifest:
```
Read: ~/.claude-code-docs/paths_manifest.json
```
