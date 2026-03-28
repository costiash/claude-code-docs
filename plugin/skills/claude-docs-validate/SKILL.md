---
name: claude-docs-validate
description: >
  Check the health and freshness of locally-stored Claude documentation.
  Use this skill when the user asks about documentation health, broken links,
  stale docs, freshness checks, or wants to validate that their local mirror
  is up-to-date and all URLs are reachable. Triggers on: "are my docs current",
  "check doc health", "validate documentation", "broken links", "stale docs".
---

# Claude Documentation Validation Skill

Check whether the local documentation mirror at `~/.claude-code-docs/` is healthy and up-to-date.

## When to Use This Skill

Activate when the user asks about:
- Documentation freshness or staleness
- Broken links or unreachable docs
- Health checks on their local mirror
- Whether docs need updating

## Validation Workflow

### Step 1: Check if docs exist

Verify `~/.claude-code-docs/docs/` exists and contains `.md` files. If not:
> Documentation not found. Run this in Claude Code to install:
> ```
> /plugin marketplace add costiash/claude-code-docs
> /plugin install claude-docs@claude-code-docs
> ```

### Step 2: Check freshness via git

```bash
cd ~/.claude-code-docs && git log -1 --format="%ci %s"
```

Report when docs were last updated. If older than 24 hours, suggest:
```bash
cd ~/.claude-code-docs && git pull
```

### Step 3: Run URL validation (if user asks for it)

For a quick spot-check (recommended first):
```bash
bash ~/.claude-code-docs/plugin/skills/claude-docs-validate/scripts/validate-paths.sh --quick
```

For a full scan (all docs — takes 1-2 minutes):
```bash
bash ~/.claude-code-docs/plugin/skills/claude-docs-validate/scripts/validate-paths.sh
```

### Step 4: Present results

- Report summary: total checked, reachable, broken, timed out
- For broken paths, suggest:
  - Run `cd ~/.claude-code-docs && git pull` to get latest
  - If still broken after pull, the upstream page may have moved
  - Report persistent issues at https://github.com/costiash/claude-code-docs/issues

### Step 5: Doc statistics (if user asks for stats/count)

Report documentation coverage:
```bash
# Total docs
ls ~/.claude-code-docs/docs/*.md | wc -l

# By category
echo "Claude Code:  $(ls ~/.claude-code-docs/docs/claude-code__*.md 2>/dev/null | wc -l)"
echo "Agent SDK:    $(ls ~/.claude-code-docs/docs/docs__en__agent-sdk__*.md 2>/dev/null | wc -l)"
echo "API Reference:$(ls ~/.claude-code-docs/docs/docs__en__api__*.md 2>/dev/null | wc -l)"
echo "Build Guides: $(ls ~/.claude-code-docs/docs/docs__en__build-with-claude__*.md 2>/dev/null | wc -l)"
echo "Tools:        $(ls ~/.claude-code-docs/docs/docs__en__agents-and-tools__*.md 2>/dev/null | wc -l)"
```

## Troubleshooting

| Issue | Solution |
|---|---|
| "Documentation not found" | Plugin not installed or docs not cloned. Re-run `/plugin install claude-docs@claude-code-docs` |
| Many broken URLs | Likely a sitemap change. Run `git pull` first, then re-validate |
| Timeout errors | Network issue or Anthropic site is slow. Try again later |
| "Permission denied" | Check that `~/.claude-code-docs/` is readable |

## Reference Files

- `examples/validate-docs.md` — Example validation workflow
