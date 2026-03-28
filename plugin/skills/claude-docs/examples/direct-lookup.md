# Example: Direct Lookup

## User Query
> /docs hooks

## Skill Reasoning
- User names a specific topic: "hooks"
- Strategy: Direct lookup (Priority 1)
- No product context specified — search broadly

## Actions
1. Glob: `~/.claude-code-docs/docs/*hooks*.md`
2. Results:
   - `claude-code__hooks.md` (Claude Code CLI)
   - `claude-code__hooks-guide.md` (Claude Code CLI)
   - `docs__en__agent-sdk__hooks.md` (Agent SDK)
3. All Claude Code files are same context → read both, synthesize
4. Agent SDK file is different context → note but include since "hooks" is unambiguous enough

## Output Format
"Claude Code hooks allow you to run shell commands at specific points in Claude's workflow...

[Synthesized explanation from both CLI docs]

For Agent SDK hooks, see also the [Agent SDK hooks guide](https://platform.claude.com/en/docs/agent-sdk/hooks).

Sources:
- [Hooks](https://code.claude.com/docs/en/hooks)
- [Hooks Guide](https://code.claude.com/docs/en/hooks-guide)
- [Agent SDK Hooks](https://platform.claude.com/en/docs/agent-sdk/hooks)"
