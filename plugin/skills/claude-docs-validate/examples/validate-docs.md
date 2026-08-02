# Example: Documentation Validation

## User Query
> /docs -t

or

> Are my docs up to date?

## Skill Reasoning
- User asks about documentation freshness/health
- Strategy: Run the v2 validation workflow (metadata freshness + cache status + URL spot-check)

## Actions
1. Check the metadata is installed: `~/.claude-code-docs/paths_manifest.json` exists
2. Check freshness — manifest build time and clone last update:
   ```bash
   jq -r '.generated_at' ~/.claude-code-docs/paths_manifest.json
   cd ~/.claude-code-docs && git log -1 --format="%ci %s"
   ```
   - Result: `2026-08-02T09:47:04.778349Z` / "2026-08-02 10:02:11 +0000 Update docs metadata"
3. Check the page cache:
   ```bash
   ~/.claude-code-docs/plugin/scripts/fetch-docs.sh status
   ```
   - Result:
     ```
     manifest pages : 725
     syncable       : 725
     cached         : 698
     pending        : 27
     stale          : 0
     ```
4. (Optional, if the user wants URL checks) Run:
   ```bash
   bash ~/.claude-code-docs/plugin/skills/claude-docs-validate/scripts/validate-paths.sh --quick
   ```
   - Result: "Total checked: 20 / Reachable: 18 / Broken: 2"

## Output Format
"Your documentation metadata was generated today (2026-08-02) and the local clone is current.

Cache status: 698 of 725 pages cached, 27 pending (they'll be fetched on demand, or run `/docs sync`).

Quick URL health check: 18/20 sampled docs are reachable. 2 returned errors — the upstream
pages may have moved. The SessionStart hook refreshes the metadata automatically; a manual
refresh is `cd ~/.claude-code-docs && git fetch origin main && git reset --hard origin/main`.
Report persistent issues at https://github.com/costiash/claude-code-docs/issues."
