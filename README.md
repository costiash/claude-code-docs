# Claude Code Documentation Tool

[![Last Update](https://img.shields.io/github/last-commit/costiash/claude-code-docs/main.svg?label=docs%20updated)](https://github.com/costiash/claude-code-docs/commits/main)
[![Tests](https://github.com/costiash/claude-code-docs/actions/workflows/test.yml/badge.svg)](https://github.com/costiash/claude-code-docs/actions)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey)](https://github.com/costiash/claude-code-docs)
[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge.svg)](https://github.com/hesreallyhim/awesome-claude-code)

> **Enhanced fork of [ericbuess/claude-code-docs](https://github.com/ericbuess/claude-code-docs)** with native plugin support, auto-discovery Skill, and AI-powered semantic search.

**Official Claude docs, always up-to-date, always at your fingertips.** Stop searching the web — ask Claude directly and get accurate answers grounded in official documentation.

## Why Use This?

Claude knows a lot — but documentation changes fast. API parameters shift, new features land, SDK methods get renamed. This tool gives Claude a local mirror of every official doc page, so answers come from the source, not stale training data.

| Without claude-code-docs | With claude-code-docs |
|---|---|
| Claude guesses from training data | Claude reads the latest official docs |
| Broken or outdated URLs in answers | Correct `platform.claude.com` / `code.claude.com` links |
| "I think the API works like..." | "According to the documentation..." |
| You verify answers manually | Answers cite specific doc pages |

## Quick Start — Plugin Install (Recommended)

Two commands, no dependencies:

```bash
/plugin marketplace add costiash/claude-code-docs
/plugin install claude-docs@claude-code-docs
```

That's it. On your next session Claude will automatically:
1. Clone all documentation files to `~/.claude-code-docs/`
2. Keep them updated every session via `git pull`
3. Make the `/docs` command available for manual lookups
4. Activate the **auto-discovery Skill** — Claude reads docs automatically when you ask Claude-related questions

### What the Plugin Gets You

- **`/docs` command** — Look up any topic: `/docs hooks`, `/docs extended thinking`, `/docs Agent SDK sessions`
- **Auto-discovery Skill** — Claude proactively searches docs when you ask about Claude Code, the API, SDKs, or prompt engineering. No `/docs` prefix needed.
- **Session-start auto-updates** — Docs stay fresh automatically. No cron jobs, no manual pulls.
- **Zero dependencies** — No Python, no jq, no curl. Just Claude Code with plugin support.

## Alternative: Script Install

For environments without plugin support, or if you prefer manual control:

```bash
curl -fsSL https://raw.githubusercontent.com/costiash/claude-code-docs/main/install.sh | bash
```

This provides the `/docs` command only (no auto-discovery Skill). Python 3.9+ enables advanced features like full-text content search and path validation.

**CI/CD or non-interactive environments:**
```bash
CLAUDE_DOCS_AUTO_INSTALL=yes curl -fsSL https://raw.githubusercontent.com/costiash/claude-code-docs/main/install.sh | bash
```

**Requirements:** macOS 12+ or Linux, git, jq, curl. Python 3.9+ optional.

## Usage

### Direct Lookups

```bash
/docs hooks              # Claude Code hooks
/docs mcp                # MCP server configuration
/docs agent sdk python   # Agent SDK Python guide
/docs -t                 # Check freshness and pull updates
/docs what's new         # Recent documentation changes
```

### Natural Language Queries

The `/docs` command understands intent — ask questions in plain English:

```bash
/docs what are the best practices for Agent SDK in Python?
/docs explain the differences between hooks and MCP
/docs how do I configure extended thinking for the API?
/docs show me all prompt library templates
```

Claude finds the right docs, reads them, and synthesizes a clear answer with source links.

### With the Auto-Discovery Skill (Plugin Only)

When installed as a plugin, you don't even need `/docs`. Just ask naturally:

> "How do I set up MCP servers in Claude Code?"

Claude recognizes this is a documentation question and automatically reads the relevant docs before answering.

## Documentation Coverage

Documentation files across 11 categories, updated every 3 hours:

- **API Reference** — Messages API, Admin API, multi-language SDKs (Python, TypeScript, Go, Java, Kotlin, Ruby)
- **Agent SDK** — Python and TypeScript SDK guides, sessions, hooks, custom tools
- **Claude Code** — CLI docs: hooks, skills, MCP, plugins, settings, sub-agents
- **Agents & Tools** — MCP connectors, tool use patterns, agent capabilities
- **Core Documentation** — Guides, tutorials, prompt engineering, extended thinking
- **About Claude** — Model capabilities, context windows, pricing
- **Getting Started** — Quickstart guides
- **Testing & Evaluation** — Eval frameworks, testing guides
- **Prompt Library** — Ready-to-use prompt templates
- **Release Notes** — Version history and changelogs
- **Resources** — Additional resources

## How Updates Work

1. **Automatic (Plugin)** — Docs update via `git pull` at the start of each Claude Code session
2. **Automatic (CI/CD)** — GitHub Actions fetches from Anthropic sitemaps every 3 hours
3. **On-Demand** — `/docs -t` checks for and pulls updates
4. **Safe** — Sync safeguards prevent mass deletion (min 200 paths discovered, max 10% deletion per sync, min 250 files)

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `/docs` not found | Restart Claude Code; for script install check `ls ~/.claude/commands/docs.md` |
| Docs seem outdated | `/docs -t` to force update, or `cd ~/.claude-code-docs && git pull` |
| Plugin not working | Run `/plugin list` to verify installation |
| "Installation cancelled" | Use `CLAUDE_DOCS_AUTO_INSTALL=yes` with the curl install |

## Uninstalling

**Plugin:**
```bash
/plugin uninstall claude-docs@claude-code-docs
```

**Script install:**
```bash
~/.claude-code-docs/uninstall.sh
```

## Security

- Input sanitization and path traversal protection
- Sync safeguards prevent catastrophic documentation loss
- All operations limited to documentation directory, HTTPS-only
- Full test suite with security coverage

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for architecture overview, development setup, testing requirements, and PR guidelines.

## Acknowledgments

- **[Eric Buess](https://github.com/ericbuess)** — Creator of the [original claude-code-docs](https://github.com/ericbuess/claude-code-docs)
- **[Anthropic](https://www.anthropic.com/)** — For Claude Code and the documentation

## License

MIT License. Documentation content belongs to Anthropic. Tool code is open source — see [LICENSE](LICENSE).
