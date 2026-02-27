---
name: claude-docs-search
description: >
  Search and read locally-stored Claude documentation covering Claude Code CLI,
  Claude API (Messages, tool use, vision, streaming, batch), Agent SDK (Python and
  TypeScript), prompt engineering, and all Anthropic platform docs. Use this skill
  whenever the user asks about Claude Code features (hooks, MCP servers, skills,
  plugins, settings, permissions, keybindings, sub-agents), the Anthropic API or
  any of its SDKs (Python, TypeScript, Go, Java), the Agent SDK (sessions, hooks,
  custom tools, MCP), model capabilities (context windows, extended thinking,
  pricing, rate limits, vision), prompt engineering best practices, or
  troubleshooting any Claude-related error. This skill provides instant access to
  574+ official documentation files without web searches — always prefer it over
  web lookups for Claude and Anthropic topics.
---

# Claude Documentation Search Skill

You have access to a local mirror of Claude's official documentation at `~/.claude-code-docs/docs/`.

## When to Use This Skill

Activate when the user asks about:
- Claude Code features: hooks, skills, MCP, plugins, settings, slash commands, sub-agents
- Claude API: messages, tool use, streaming, batch processing, embeddings
- Agent SDK: Python/TypeScript SDK, sessions, custom tools, subagents
- Prompt engineering: best practices, system prompts, chain of thought
- Any topic covered by platform.claude.com or code.claude.com

## How to Search

### Filename-Based Category Inference

Documentation files follow naming conventions:
- `claude-code__<page>.md` → Claude Code CLI docs (hooks, mcp, skills, etc.)
- `docs__en__agent-sdk__<page>.md` → Agent SDK docs
- `docs__en__api__<lang>__<endpoint>.md` → API reference (Python, TypeScript, Go, Java, Kotlin, Ruby)
- `docs__en__build-with-claude__<page>.md` → Guides and tutorials
- `docs__en__resources__prompt-library__<name>.md` → Prompt templates

### Search Strategy

**Step 1 — Scope by context if the user names a product:**

| User mentions | Try first |
|---|---|
| "Claude Code", "CLI", "hooks", "skills", "plugins" | `~/.claude-code-docs/docs/claude-code__*<keyword>*.md` |
| "Agent SDK", "SDK", "Python SDK", "TypeScript SDK" | `~/.claude-code-docs/docs/docs__en__agent-sdk__*<keyword>*.md` |
| "API", "messages endpoint", "tool use" | `~/.claude-code-docs/docs/docs__en__api__*.md` + Grep |
| "agents and tools", "MCP connector" | `~/.claude-code-docs/docs/docs__en__agents-and-tools__*.md` |

If the user doesn't name a product, search broadly.

**Step 2 — Glob for candidate files:**
```
Glob: ~/.claude-code-docs/docs/*<keyword>*.md
```

**Step 3 — If Glob finds matches**, Read the most relevant files (up to 3-4)

**Step 4 — If Glob finds nothing**, use Grep for content search:
```
Grep: "<keyword>" in ~/.claude-code-docs/docs/
```

**Step 5 — If both Glob and Grep return nothing:**
- Try alternative keywords (synonyms, related terms)
- Check if the topic exists under a different name (e.g., "function calling" → "tool use")
- Suggest the user run `/docs -t` to check if docs are installed and up to date
- Let the user know the topic may not be covered in the local mirror

### Synthesis Instructions

- Read ALL matching docs within the same product context
- Synthesize a unified answer — don't dump raw file contents
- Include code examples from the docs when relevant
- Cite sources with official URLs (see below)
- If results span different products, ask user which context they mean

### Determining Source URLs

- Files starting with `claude-code__` → `https://code.claude.com/docs/en/<page>` (strip `.md` extension, replace `claude-code__` prefix and `__` with `/`)
- Files starting with `docs__en__` → `https://platform.claude.com/en/docs/<path>` (strip `.md` extension, replace `docs__en__` prefix with `en/docs/` and remaining `__` with `/`)

## Reference Files

- `manifest-reference.md` — Documentation about the manifest structure and categories
