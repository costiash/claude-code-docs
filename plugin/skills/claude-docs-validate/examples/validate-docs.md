# Example: Documentation Validation

## User Query
> /docs -t

or

> Are my docs up to date?

## Skill Reasoning
- User asks about documentation freshness/health
- Strategy: Run validation workflow

## Actions
1. Check `~/.claude-code-docs/docs/` exists
2. Run: `cd ~/.claude-code-docs && git log -1 --format="%ci %s"`
   - Result: "2026-03-28 12:20:11 +0000 Update Claude Code docs - 2026-03-28"
3. (Optional) Run: `validate-paths.sh --quick`
   - Result: "18/20 reachable, 2 broken"

## Output Format
"Your documentation was last updated on March 28, 2026 (today).

Quick health check: 18/20 sampled docs are reachable. 2 returned errors:
- `docs__en__resources__prompt-library__code-clarifier.md` → 404
- `docs__en__resources__prompt-library__meeting-scribe.md` → 404

These prompt library pages may have been removed upstream. Run `cd ~/.claude-code-docs && git pull` to sync latest, or report persistent issues at https://github.com/costiash/claude-code-docs/issues."
