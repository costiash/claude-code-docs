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

**Freshness check** (`-t`, `--check`, or user asks about freshness/health/validation):
→ Use the `claude-docs-validate` skill to check doc health and freshness.

**What's new** (`what's new`, `recent changes`):
→ Run: `cd ~/.claude-code-docs && git log --oneline -5 -- docs/`
→ Present the recent commits naturally.

**Uninstall** (`uninstall`):
→ Tell the user: `/plugin uninstall claude-docs@claude-code-docs`
→ Optionally clean up: `rm -rf ~/.claude-code-docs`

**Everything else** (topic lookups, questions, searches):
→ Use the `claude-docs-search` skill to find and present documentation.

## User's Request

The user requested: `$ARGUMENTS`
