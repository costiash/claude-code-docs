---
name: claude-docs-search
description: >
  Search and read locally-stored Claude documentation. Use when the user asks about
  Claude Code features (hooks, skills, MCP, settings, plugins), Claude API usage,
  Agent SDK, prompt engineering, or any Anthropic documentation topic. Provides
  instant access to official docs without web searches.
---

# Claude Documentation Search Skill

You have access to a local mirror of Claude's official documentation at `~/.claude-code-docs/docs/`.

## When to Use This Skill

Activate when the user asks about:
- Claude Code features: hooks, skills, MCP, plugins, settings, slash commands, sub-agents
- Claude API: messages, tool use, streaming, batch processing, embeddings
- Agent SDK: Python/TypeScript SDK, sessions, custom tools, subagents
- Prompt engineering: best practices, system prompts, chain of thought
- Any topic covered by docs.anthropic.com or code.claude.com

## How to Search

### Filename-Based Category Inference

Documentation files follow naming conventions:
- `docs__en__<page>.md` → Claude Code CLI docs (hooks, mcp, skills, etc.)
- `en__docs__agent-sdk__<page>.md` → Agent SDK docs
- `en__api__<lang>__<endpoint>.md` → API reference (Python, TypeScript, Go, Java, Kotlin, Ruby)
- `en__docs__build-with-claude__<page>.md` → Guides and tutorials
- `en__resources__prompt-library__<name>.md` → Prompt templates

### Search Strategy

1. **Start with Glob** to find candidate files:
   ```
   Glob: ~/.claude-code-docs/docs/*<keyword>*.md
   ```

2. **If Glob finds matches**, Read the most relevant files (up to 3-4)

3. **If Glob finds nothing**, use Grep for content search:
   ```
   Grep: "<keyword>" in ~/.claude-code-docs/docs/
   ```

4. **Read matching files** and extract relevant sections

### Synthesis Instructions

- Read ALL matching docs within the same product context
- Synthesize a unified answer — don't dump raw file contents
- Include code examples from the docs when relevant
- Cite sources with links: `https://docs.anthropic.com/<path>` or `https://code.claude.com/<path>`
- If results span different products, ask user which context they mean

### Determining Source URLs

- Files starting with `docs__en__` → `https://code.claude.com/docs/en/<page>`
- Files starting with `en__` → `https://platform.claude.com/<path>` (replace `__` with `/`)

## Reference Files

- `manifest-reference.md` — Documentation about the manifest structure and categories
