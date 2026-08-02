# Example: Direct Lookup

## User Query
> /docs hooks

## Skill Reasoning
- User names a specific topic: "hooks"
- Strategy: Direct manifest lookup (exact topic named)
- No product context specified — search broadly

## Actions
1. Query the manifest:
   ```bash
   jq -r '.pages[] | select(.filename | test("hooks")) | .filename' ~/.claude-code-docs/paths_manifest.json
   ```
2. Results:
   - `claude-code__hooks.md` (Claude Code CLI — "Hooks reference")
   - `claude-code__hooks-guide.md` (Claude Code CLI — "Automate actions with hooks")
   - `claude-code__agent-sdk__hooks.md` (Agent SDK — "Intercept and control agent behavior with hooks")
   - `docs__en__api__beta__webhooks.md` (matched "hooks" but is webhooks — irrelevant, drop it)
3. Read `~/.claude-code-docs/cache/claude-code__hooks.md` and `~/.claude-code-docs/cache/claude-code__hooks-guide.md`.
   On a cache miss, fetch first: `~/.claude-code-docs/plugin/scripts/fetch-docs.sh get "claude-code__hooks.md"`, then read.
4. Both CLI files are same context → synthesize
5. Agent SDK file is different context → note but include since "hooks" is unambiguous enough
6. Get exact source URLs from the manifest (never reconstruct from filenames):
   ```bash
   jq -r '.pages[] | select(.filename=="claude-code__hooks.md") | .url' ~/.claude-code-docs/paths_manifest.json
   ```

## Output Format
"Claude Code hooks allow you to run shell commands at specific points in Claude's workflow...

[Synthesized explanation from both CLI docs]

For Agent SDK hooks, see also the [Agent SDK hooks guide](https://code.claude.com/docs/en/agent-sdk/hooks).

Sources:
- [Hooks reference](https://code.claude.com/docs/en/hooks)
- [Automate actions with hooks](https://code.claude.com/docs/en/hooks-guide)
- [Intercept and control agent behavior with hooks](https://code.claude.com/docs/en/agent-sdk/hooks)"
