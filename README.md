# Claude Code Documentation Tool

[![Last Update](https://img.shields.io/github/last-commit/costiash/claude-code-docs/main.svg?label=docs%20updated)](https://github.com/costiash/claude-code-docs/commits/main)
[![Tests](https://github.com/costiash/claude-code-docs/actions/workflows/test.yml/badge.svg)](https://github.com/costiash/claude-code-docs/actions)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey)](https://github.com/costiash/claude-code-docs)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Listed on ClaudePluginHub](https://www.claudepluginhub.com/badge/costiash-claude-docs-plugin)](https://www.claudepluginhub.com/plugins/costiash-claude-docs-plugin?ref=badge)

**Every official Claude doc page, always live, never redistributed.** 700+ pages across `platform.claude.com` and `code.claude.com`, re-indexed every 3 hours — and your Claude reads the actual current page, not a stale copy or a guess from training data.

```bash
/plugin marketplace add costiash/claude-code-docs
/plugin install claude-docs@claude-code-docs
```

Two commands. No Python, no MCP server, no API keys — the client is pure `bash` + `curl` + `jq`.

## The Architecture Nobody Else Uses

Most documentation tools pick one of two designs: **mirror the docs** into a repo (instantly stale between syncs, redistributes content that isn't theirs, ~100 MB clones) or **serve them through an MCP server** (another process to run, network round-trips per query, answers that flood your context window).

This tool does neither. The repository commits **only metadata** — a page manifest and a prose-free search index, about 3 MB total. Your machine fetches each `.md` page **directly from Anthropic's servers, on demand**, into a local cache. Claude searches the index first and reads only the pages it needs.

| | Web search | Docs mirrors | MCP docs servers | **This tool** |
|---|---|---|---|---|
| Freshness | Search-engine lag | Stale between syncs | Usually current | **Live page, every read** |
| Claude docs coverage | Hit-or-miss | Often partial | Generic libraries | **All 700+ pages, both sites** |
| Runtime dependencies | None | git + disk | MCP server + config | **bash, curl, jq** |
| Context cost per answer | Whole pages of noise | Full file reads | Large tool payloads | **Index hit → one targeted page** |
| Redistributes Anthropic's docs | No | **Yes, wholesale** | Varies | **Never — you fetch from the source** |
| Clone size | — | ~100 MB | — | **~3 MB** |

The compliance point is not a footnote: this repo contains **zero documentation prose — not at the tip, not anywhere in its history**. What you install is a map; the territory always comes fresh from Anthropic.

| Without claude-code-docs | With claude-code-docs |
|---|---|
| Claude guesses from training data | Claude reads the latest official docs |
| Broken or outdated URLs in answers | Correct `platform.claude.com` / `code.claude.com` links |
| "I think the API works like..." | "According to the documentation..." |
| You verify answers manually | Answers cite specific doc pages |

## What You Get

- **Auto-discovery** — ask anything about Claude Code, the API, SDKs, or prompt engineering and Claude reads the relevant docs before answering. No prefix, no command. This is the feature you'll forget is running — your answers are just correct.
- **`/docs` skill** — explicit lookups when you want them: `/docs hooks`, `/docs extended thinking`, `/docs Agent SDK sessions`
- **Interactive Courses** — turn any topic into a self-contained animated HTML course (below — this one's unique)
- **Changelog Reports** — visual HTML reports of what changed in the docs, with one-click course generation per entry
- **Token-efficient by design** — search runs in shell against a prose-free index; Claude's context only ever pays for the specific pages it reads
- **Session-start auto-updates** — metadata syncs and changed pages re-fetch in the background every session. No cron jobs, no manual pulls.

On your first session after install, Claude clones the ~3 MB metadata repo to `~/.claude-code-docs/`, warms the page cache in the background, and activates the skills. That's the whole setup.

## Interactive Courses — Learn Claude by Doing

> **No other docs tool does this.** Ask about any Claude topic and get a beautifully crafted, interactive HTML course — animated protocol diagrams, hands-on quizzes, code-with-English translations, in a dark Obsidian & Amber theme. One self-contained file, zero setup, opens right in your browser.

```bash
/docs --course hooks          # Generate a course on Claude Code hooks
/docs --course tool use       # Deep dive into the Tool Use API
/docs --course prompt caching # Master caching with visual explanations
```

Or just ask naturally after any docs response — Claude will offer to create a course on whatever you just looked up.

https://github.com/user-attachments/assets/e36ae4c1-2ee6-4932-b0a5-3463cd20e012

**What's inside a course:**
- **4-7 scroll-based modules** with a progressive learning arc
- **Protocol Conversations** — animated chat-style visualizations of how Client, API, Claude, and tools actually exchange messages
- **Code translations** — real API examples from the docs with line-by-line plain-English explanations
- **Quizzes that test application** — "What would you use for this scenario?", not "Define this term"
- **Glossary tooltips** on every Claude-specific term
- **Obsidian & Amber theme** — Instrument Serif headings, warm amber accents, grain textures, glass effects. Not your typical tutorial.

Courses are saved to `~/.claude-code-docs/courses/` so you can revisit them or share them with your team.

### Changelog Reports — the Docs→Learning Loop

Anthropic's documentation changes daily. Stay ahead of it:

```bash
/docs --report          # Last 7 days of changes
/docs --report 24h      # Last 24 hours
/docs --report 30d      # Last 30 days
```

You get a visual HTML report of every added, changed, and removed page — grouped by category, with summaries. And each entry carries a **"Create Course"** button: click, paste into Claude Code, and deep-dive into whatever just changed. Docs monitoring and learning in one loop.

## Usage

### Direct Lookups

```bash
/docs hooks              # Claude Code hooks
/docs mcp                # MCP server configuration
/docs agent sdk python   # Agent SDK Python guide
/docs --course hooks     # Generate an interactive course on hooks
/docs --report           # HTML changelog of recent doc changes
/docs -t                 # Check freshness (read-only)
/docs what's new         # Recent documentation changes
```

### Natural Language Queries

The `/docs` skill understands intent — ask questions in plain English:

```bash
/docs what are the best practices for Agent SDK in Python?
/docs explain the differences between hooks and MCP
/docs how do I configure extended thinking for the API?
/docs show me all Agent SDK pages
```

Claude finds the right docs, reads them, and synthesizes a clear answer with source links.

### Or Just Ask (Auto-Discovery)

With the plugin installed you don't need `/docs` at all:

> "How do I set up MCP servers in Claude Code?"

Claude recognizes a documentation question and reads the relevant docs before answering — grounded answers with real URLs, every time.

## Documentation Coverage

The full Claude documentation set — every page on **platform.claude.com** and **code.claude.com**:

- **API Reference** — Messages API, Admin API, multi-language SDKs (Python, TypeScript, Go, Java, Ruby, C#, PHP)
- **Claude Code** — CLI docs: hooks, skills, MCP, plugins, settings, sub-agents
- **Core Documentation** — Guides, tutorials, prompt engineering, extended thinking
- **Agents & Tools** — MCP connectors, tool use patterns, agent capabilities
- **Agent SDK** — Python and TypeScript SDK guides, sessions, hooks, custom tools
- **About Claude** — Model capabilities, context windows, pricing
- **Testing & Evaluation** — Eval frameworks, testing guides
- **Release Notes** — Version history and changelogs

## Team / Organization Adoption

Auto-prompt every team member to install the plugin by adding this to your project's `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "claude-code-docs": {
      "source": {
        "source": "github",
        "repo": "costiash/claude-code-docs"
      }
    }
  },
  "enabledPlugins": {
    "claude-docs@claude-code-docs": true
  }
}
```

Commit this file to your repository. When a team member trusts the project folder, they'll be prompted to install the marketplace and plugin automatically — no manual setup needed.

## How Updates Work

1. **Automatic (Plugin)** — Each session the metadata syncs (`git reset --hard origin/main`) and a background fetch updates only changed pages in the local cache
2. **Automatic (CI/CD)** — GitHub Actions regenerates the manifest + index from Anthropic's `llms.txt` + sitemaps every 3 hours
3. **On-Demand** — `/docs sync` fetches changed pages now; `/docs -t` checks freshness
4. **Safe** — Layered fail-closed safeguards: discovery floors, max-removal thresholds, index carry-forward through partial outages, and an independent floor check in CI before any commit. A bad upstream day can delay an update; it cannot corrupt your docs.

## Legacy: Script Install (Migration)

For environments without plugin support:

```bash
curl -fsSL https://raw.githubusercontent.com/costiash/claude-code-docs/main/install.sh | bash
```

If Claude Code is detected, the script will guide you to install the plugin instead. Without Claude Code, it sets up the same metadata clone + on-demand fetching for basic documentation access.

> **Upgrading from a v1 (mirror) install?** Nothing to do — your next session auto-migrates. The SessionStart hook hard-syncs to the metadata-only v2 layout (removing the old committed `docs/`, preserving your cache and courses), then fetches pages on demand.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `/docs` not found | Restart Claude Code so the plugin loads; for a script install, check `ls ~/.claude-code-docs/` |
| `jq` missing | `brew install jq` (macOS) or `sudo apt install jq` (Debian/Ubuntu) — the only dependency not preinstalled everywhere |
| Docs seem outdated | `/docs sync` (or the SessionStart hook, which hard-syncs each session) forces an update; `/docs -t` only checks freshness |
| Plugin not working | Run `/plugin list` to verify installation |
| Script install fails | Install the plugin instead: `/plugin install claude-docs@claude-code-docs` |

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

- **No documentation prose is committed** — the repo holds only metadata (manifest + lossy, non-reconstructible index), verified by tests on every CI run
- The client fetch layer enforces a **domain allowlist** (`code.claude.com`, `platform.claude.com`, `raw.githubusercontent.com`), HTTPS-only with no redirect following, atomic writes, sha256 integrity checks, and filename path-traversal protection
- The CI pipeline is **fail-closed at every layer**: discovery floors, manifest transition guards, index carry-forward ceilings, and an independent jq floor check before any commit
- Third-party CI actions are SHA-pinned; workflows run with least-privilege tokens; the shell client is tested on both Linux and macOS (BSD userland, bash 3.2) on every push
- 150+ automated tests, including a mocked-curl harness that exercises the client's security guards directly

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for architecture overview, development setup, testing requirements, and PR guidelines.

## Acknowledgments

- **[Eric Buess](https://github.com/ericbuess)** — Creator of the [original claude-code-docs](https://github.com/ericbuess/claude-code-docs), the project that pioneered `/docs` in Claude Code and the foundation this tool grew from
- **[zarazhangrui/codebase-to-course](https://github.com/zarazhangrui/codebase-to-course)** — Inspiration for the interactive course generator skill
- **[Anthropic](https://www.anthropic.com/)** — For Claude Code and the documentation

## License

MIT License. Documentation content belongs to Anthropic. Tool code is open source — see [LICENSE](LICENSE).
