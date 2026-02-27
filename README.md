# Claude Code Documentation Tool

[![Last Update](https://img.shields.io/github/last-commit/costiash/claude-code-docs/main.svg?label=docs%20updated)](https://github.com/costiash/claude-code-docs/commits/main)
[![Tests](https://github.com/costiash/claude-code-docs/actions/workflows/test.yml/badge.svg)](https://github.com/costiash/claude-code-docs/actions)
[![Python](https://img.shields.io/badge/python-3.9+-blue)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey)](https://github.com/costiash/claude-code-docs)
[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge.svg)](https://github.com/hesreallyhim/awesome-claude-code)

> **Enhanced fork of [ericbuess/claude-code-docs](https://github.com/ericbuess/claude-code-docs)** — adds Python-powered search, validation, and auto-regeneration while maintaining graceful degradation.

**Fast, searchable access to Claude documentation — locally, always up-to-date.**

## Key Features

- **AI-Powered Search** — Ask questions naturally via `/docs`, Claude routes intelligently
- **Complete Coverage** — 6 categories of documentation paths tracked and downloaded as markdown
- **Always Fresh** — Auto-updated every 3 hours via GitHub Actions; run `/docs -t` to pull latest
- **Graceful Degradation** — Works with or without Python 3.9+
- **Multi-Language SDK Docs** — Python, TypeScript, Go, Java, Kotlin, Ruby

## Installation

### Method 1: Plugin Install (Recommended)

If you have Claude Code with plugin support:

```bash
/plugin marketplace add costiash/claude-code-docs
/plugin install claude-docs
```

**What it does:**
1. Installs the claude-docs plugin (provides `/docs` command + auto-discovery Skill)
2. On first session, automatically clones documentation to `~/.claude-code-docs/`
3. On each subsequent session, auto-updates docs via git pull

**Requirements:** Claude Code with plugin support

### Method 2: Script Install (Legacy)

For environments without plugin support:

```bash
curl -fsSL https://raw.githubusercontent.com/costiash/claude-code-docs/main/install.sh | bash
```

This clones the repository to `~/.claude-code-docs`, installs documentation files, and sets up the `/docs` command. Python features activate automatically if Python 3.9+ is available.

**CI/CD or non-interactive environments:**
```bash
CLAUDE_DOCS_AUTO_INSTALL=yes curl -fsSL https://raw.githubusercontent.com/costiash/claude-code-docs/main/install.sh | bash
```

**Requirements:** macOS 12+ or Linux, git, jq, curl. Python 3.9+ optional.

## Usage

```bash
/docs hooks              # Read hooks documentation
/docs mcp                # Read MCP documentation
/docs -t                 # Check sync status and pull updates
/docs what's new         # Recent documentation changes
/docs changelog          # Official Claude Code release notes
```

### Natural Language Queries

The `/docs` command leverages Claude's semantic understanding — ask questions in plain English:

```bash
/docs what are the best practices for Agent SDK in Python?
/docs explain the differences between hooks and MCP
/docs show me everything about memory features
/docs how do I use extended thinking?
```

Claude analyzes your intent, searches relevant documentation, synthesizes answers from multiple sources, and presents results with links.

### Advanced Commands (Python 3.9+)

```bash
~/.claude-code-docs/claude-docs-helper.sh --search "keyword"          # Fuzzy path search
~/.claude-code-docs/claude-docs-helper.sh --search-content "term"     # Full-text content search
~/.claude-code-docs/claude-docs-helper.sh --validate                  # Check all paths for 404s
~/.claude-code-docs/claude-docs-helper.sh --status                    # Installation status
```

## How Updates Work

1. **Automatic** — GitHub Actions fetches from Anthropic sitemaps every 3 hours
2. **On-Demand** — `/docs -t` checks for and pulls updates
3. **Manual** — `cd ~/.claude-code-docs && git pull`
4. **Safe** — Sync safeguards prevent mass deletion (min discovery threshold, max 10% deletion per sync, min file count)

## Documentation Categories

Documentation is organized across 6 categories (counts update automatically with each sync):

- **API Reference** — Complete API docs, Admin API, Agent SDK, multi-language SDK docs
- **Core Documentation** — Guides, tutorials, prompt engineering, best practices
- **Claude Code** — CLI-specific docs: hooks, skills, MCP, settings, plugins
- **Prompt Library** — Ready-to-use prompt templates
- **Release Notes** — Version history
- **Resources** — Additional resources

Run `~/.claude-code-docs/claude-docs-helper.sh --status` to see current counts.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `/docs` not found | Check `ls ~/.claude/commands/docs.md`, restart Claude Code |
| "Installation cancelled" with `curl \| bash` | Use `CLAUDE_DOCS_AUTO_INSTALL=yes` or download first |
| Docs seem outdated | `/docs -t` to force update, or `cd ~/.claude-code-docs && git pull` |
| Check version | `~/.claude-code-docs/claude-docs-helper.sh --version` |

## Uninstalling

```bash
~/.claude-code-docs/uninstall.sh
```

## Security

- Input sanitization and path traversal protection
- Sync safeguards prevent catastrophic documentation loss (min thresholds, max deletion limits, auto-revert)
- All operations limited to documentation directory, HTTPS-only
- Full test suite with security test coverage

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for architecture overview, development setup, testing requirements, and PR guidelines.

## Acknowledgments

- **[Eric Buess](https://github.com/ericbuess)** — Creator of the [original claude-code-docs](https://github.com/ericbuess/claude-code-docs)
- **[Anthropic](https://www.anthropic.com/)** — For Claude Code and the documentation

## License

MIT License. Documentation content belongs to Anthropic. Tool code is open source — see [LICENSE](LICENSE).
