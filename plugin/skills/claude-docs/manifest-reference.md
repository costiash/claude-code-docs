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
| `claude_code` | Claude Code CLI docs | `claude-code__*.md` |
| `agent_sdk` | Agent SDK (Python, TypeScript) | `docs__en__agent-sdk__*.md` |
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

Convert filenames to source URLs:

| Filename | URL |
|---|---|
| `claude-code__hooks.md` | `https://code.claude.com/docs/en/hooks` |
| `claude-code__hooks-guide.md` | `https://code.claude.com/docs/en/hooks-guide` |
| `docs__en__api__messages__create.md` | `https://platform.claude.com/en/docs/api/messages/create` |
| `docs__en__agent-sdk__python.md` | `https://platform.claude.com/en/docs/agent-sdk/python` |
| `docs__en__build-with-claude__vision.md` | `https://platform.claude.com/en/docs/build-with-claude/vision` |
| `docs__en__resources__prompt-library__code-clarifier.md` | `https://platform.claude.com/en/docs/resources/prompt-library/code-clarifier` |

**Rules:**
- `claude-code__<page>.md` → `https://code.claude.com/docs/en/<page>`
- `docs__en__<path>.md` → `https://platform.claude.com/en/docs/<path>` (replace `__` with `/`)

## Dynamic Discovery

To count available docs:
```
Glob: ~/.claude-code-docs/docs/*.md
```

To check categories in manifest:
```
Read: ~/.claude-code-docs/paths_manifest.json
```
