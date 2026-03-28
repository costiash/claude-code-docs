# Example: Documentation Changelog Report

## User Query
> /docs --report

## Skill Reasoning
- User requests a docs changelog report
- Default timeframe: last 7 days
- Strategy: git log → categorize → analyze → generate HTML

## Actions

### Phase 1: Discover Changes
1. Run: `cd ~/.claude-code-docs && git log --since="7 days ago" --name-status --pretty=format:"%H %ai %s" -- docs/`
2. Parse output — found 12 changed files:
   - 5 Modified in `claude-code__*.md` (CLI category)
   - 6 Modified in `docs__en__agent-sdk__*.md` (SDK category)
   - 1 Added: `docs__en__agent-sdk__tool-search.md` (SDK, new)

### Phase 2: Analyze Changes
1. Read each changed file + `git diff` for modified files
2. Group related changes (e.g., 5 SDK language docs with same update → 1 card)
3. Extract highlights:
   - New: Tool Search feature in Agent SDK
   - Updated: Desktop app, Sandboxing, Plugin Marketplaces, Common Workflows
   - Updated: Custom Tools, MCP, Python/TypeScript SDKs, User Input

### Phase 3: Generate HTML
1. Create `~/.claude-code-docs/courses/changelog-2026-03-28.html`
2. Structure: header → stats bar → highlights → CLI section (5 cards) → SDK section (6 cards) → Platform section (1 card)
3. Each card gets a "Create Course" button with `data-topic` extracted from filename
4. Course button copies `/docs --course <topic>` to clipboard on click

### Phase 4: Open and Present
- Open in browser
- "Found 12 changes across 3 categories in the last 7 days. Saved to `~/.claude-code-docs/courses/changelog-2026-03-28.html`"

## Output
Self-contained HTML file with:
- Obsidian & Amber dark theme (matching course design system)
- Stats bar: 5 CLI, 6 SDK (1 new), 1 Platform
- Key highlights box with top 6 changes
- 8 cards (grouped) with summaries, bullet lists, source links
- Each card has a "Create Course" button → copies clipboard command
- Toast notification on button click
