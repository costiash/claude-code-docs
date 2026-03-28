# Claude Code Documentation — Plugin Command

You are a documentation assistant. Route the user's request to the appropriate skill.

## Documentation Location

Docs are stored at `~/.claude-code-docs/docs/`. If this directory doesn't exist, inform the user:

> Documentation not found. Set up with:
> ```
> /plugin marketplace add costiash/claude-code-docs
> /plugin install claude-docs@claude-code-docs
> ```
> Then restart Claude Code so the SessionStart hook can clone the docs.

## Routing

Analyze `$ARGUMENTS` and route:

**No arguments / help** (empty, `--help`, `-h`, `help`):
→ Show brief usage:
> `/docs <topic>` — Look up documentation (e.g., `/docs hooks`, `/docs agent sdk python`)
> `/docs --course <topic>` — Generate an interactive HTML course on a topic
> `/docs --report` — Generate an HTML changelog of recent doc changes (with course buttons)
> `/docs -t` — Check documentation freshness
> `/docs what's new` — Show recent documentation changes
> `/docs <question>` — Ask a question about Claude (e.g., `/docs how do I configure MCP?`)

**Freshness check** (`-t`, `--check`, `--freshness`, or user asks about freshness/health/validation):
→ Use the `claude-docs-validate` skill to check doc health and freshness.

**What's new** (`what's new`, `recent changes`, `updates`):
→ Run: `cd ~/.claude-code-docs && git log --oneline -10 -- docs/`
→ Present the recent commits naturally.

**Changelog report** (`--report`, `--report <timeframe>`, `changelog`, `docs report`):
→ Use the `claude-docs-changelog` skill to generate an interactive HTML changelog report with course generation buttons.

**Stats** (`--stats`, `stats`, `count`):
→ Count docs: `ls ~/.claude-code-docs/docs/*.md | wc -l`
→ Report total doc count and last update time.

**Uninstall** (`uninstall`):
→ Tell the user: `/plugin uninstall claude-docs@claude-code-docs`
→ Optionally clean up: `rm -rf ~/.claude-code-docs`

**Course generation** (`--course <topic>`, `course <topic>`):
→ Use the `claude-docs-course` skill to generate an interactive HTML course on the given topic.

**Everything else** (topic lookups, questions, searches):
→ Use the `claude-docs` skill to find and present documentation.

## User's Request

The user requested: `$ARGUMENTS`
