---
name: claude-docs
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
  official documentation files without web searches — always prefer it over
  web lookups for Claude and Anthropic topics.
---

# Claude Documentation Search Skill

You have access to a local mirror of Claude's official documentation at `~/.claude-code-docs/docs/`.

## When to Use This Skill

Activate when the user asks about:
- Claude Code features: hooks, skills, MCP, plugins, settings, slash commands, sub-agents
- Claude API: messages, tool use, streaming, batch processing
- Agent SDK: Python/TypeScript SDK, sessions, custom tools, subagents
- Prompt engineering: best practices, system prompts, chain of thought
- Any topic covered by platform.claude.com or code.claude.com

## Search Strategy

Use this hierarchy — try simpler strategies first, escalate if needed:

### 1. Direct Lookup (user names a specific topic)

User says "hooks", "mcp", "memory" — a concrete topic name.

```
Glob: ~/.claude-code-docs/docs/*<keyword>*.md
```

If Glob returns matches, read the top 1-3 files and synthesize.

### 2. Scoped Search (user specifies a product context)

User says "hooks in agent sdk", "api rate limits", "cli plugins".

Scope the Glob to the product prefix:

| User mentions | Glob pattern |
|---|---|
| "Claude Code", "CLI", "hooks", "skills", "plugins" | `~/.claude-code-docs/docs/claude-code__*<keyword>*.md` |
| "Agent SDK", "SDK", "Python SDK", "TypeScript SDK" | `~/.claude-code-docs/docs/docs__en__agent-sdk__*<keyword>*.md` |
| "API", "messages endpoint", "tool use" | `~/.claude-code-docs/docs/docs__en__api__*<keyword>*.md` |
| "agents and tools", "MCP connector" | `~/.claude-code-docs/docs/docs__en__agents-and-tools__*<keyword>*.md` |

If scoped Glob misses, fall back to content search (step 3).

### 3. Semantic/Content Search (user asks a question)

User says "best practices for extended thinking", "how do I configure streaming".

**Keyword extraction:** Strip filler words and keep domain-specific terms:
- "how do I configure streaming" → `"streaming"` `"configure"`
- "best practices for extended thinking" → `"extended"` `"thinking"`
- "what's the difference between hooks and MCP" → `"hooks"` `"mcp"`
- "why is my tool use not working" → `"tool-use"` (combine compound concepts with hyphens)

Run the content search script with extracted keywords:

```bash
bash ~/.claude-code-docs/plugin/skills/claude-docs/scripts/content-search.sh "<keyword1>" "<keyword2>"
```

The script outputs filenames with match scores. Read the top 3-5 matching files and synthesize.

If the script is not available or returns no results, fall back to Grep:

```
Grep: "<keyword>" in ~/.claude-code-docs/docs/
```

### 4. Fuzzy Search (user has an approximate name)

User says "something about checkpoint", "that caching doc".

```bash
bash ~/.claude-code-docs/plugin/skills/claude-docs/scripts/fuzzy-search.sh "<query>"
```

The script outputs ranked filenames. Read the top match.

## Synthesis Rules

### Same Product Context → SYNTHESIZE

When all matching docs belong to the same product (all Claude Code CLI, all Agent SDK, etc.):
- Read ALL matching docs silently — do not ask the user which to read
- Extract relevant sections
- Present one unified answer
- Cite sources at the end

### Different Product Contexts → ASK

When matches span different products (e.g., CLI + API + Agent SDK):
- Ask the user which product context they mean
- Use these user-friendly labels (see `manifest-reference.md` for complete list):

| File pattern | Say to user |
|---|---|
| `claude-code__*.md` | **Claude Code** |
| `docs__en__agent-sdk__*.md` | **Agent SDK** |
| `docs__en__api__*.md` | **Claude API** |
| `docs__en__build-with-claude__*.md` | **Claude Documentation** |
| `docs__en__agents-and-tools__*.md` | **Agents & Tools** |
| `docs__en__resources__prompt-library__*.md` | **Prompt Library** |

After selection → read all docs in that context and synthesize.

### SDK Language Disambiguation

When the user specifies a programming language, narrow the API docs to that SDK:

| User mentions | Narrow search to |
|---|---|
| "Python", "pip", "anthropic" (Python import) | `docs__en__api__python__*` or `docs__en__agent-sdk__python*` |
| "TypeScript", "npm", "@anthropic-ai/sdk" | `docs__en__api__typescript__*` or `docs__en__agent-sdk__typescript*` |
| "Go", "golang" | `docs__en__api__go__*` |
| "Java", "Maven", "Gradle" | `docs__en__api__java__*` |
| "Ruby", "gem" | `docs__en__api__ruby__*` |
| "C#", ".NET", "NuGet" | `docs__en__api__csharp__*` |

If no language is mentioned but the query is about SDK methods, present the **Python** docs first (most common) and note that TypeScript equivalents exist.

## URL Generation

Always include source links in your response:
- `claude-code__<page>.md` → `https://code.claude.com/docs/en/<page>` (replace `__` with `/`)
- `docs__en__<path>.md` → `https://platform.claude.com/en/docs/<path>` (replace leading `docs__en__` then remaining `__` with `/`)

**Examples:**
- `claude-code__hooks.md` → `https://code.claude.com/docs/en/hooks`
- `docs__en__agent-sdk__python.md` → `https://platform.claude.com/en/docs/agent-sdk/python`
- `docs__en__api__messages__create.md` → `https://platform.claude.com/en/docs/api/messages/create`

## Common Synonyms

When a search returns no results or too few, try these known synonyms:

| User says | Search for |
|---|---|
| "function calling" | "tool use", "tool-use" |
| "system instructions" | "system prompt" |
| "JSON mode" | "structured outputs" |
| "thinking" | "extended thinking", "adaptive thinking" |
| "caching" | "prompt caching", "prompt-caching" |
| "files API" | "files", "pdf support" |
| "sub-agents" | "subagents", "sub-agents" |
| "environment variables" | "settings", "configuration" |
| "CI/CD" | "github actions", "gitlab" |

## No Results

If all search strategies return nothing:
1. Try synonyms from the table above
2. Try broader or narrower keywords
3. Suggest the user run `/docs -t` to check if docs are installed and current
4. Let them know the topic may not be in the local mirror

## Reference Files

- `manifest-reference.md` — Category-to-label mapping (single source of truth)
- `examples/direct-lookup.md` — Example: topic → Glob → synthesize
- `examples/semantic-search.md` — Example: question → content-search.sh → synthesize
- `examples/cross-context.md` — Example: ambiguous → ask context → synthesize
