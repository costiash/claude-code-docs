# Example: Documentation Changelog Report

## User Query
> /docs --report

## Skill Reasoning
- User requests a docs changelog report
- Default timeframe: last 7 days
- Strategy: manifest-diff → categorize → analyze → generate HTML

## Actions

### Phase 1: Discover Changes
1. Run: `~/.claude-code-docs/plugin/scripts/manifest-diff.sh --since 7d --json`
2. Parse the JSON — three arrays of full page entries: `added`, `changed` (sha256 delta
   between manifest revisions), `removed`. Found 12 changes:
   - `added` (1): `claude-code__agent-sdk__tool-search.md` — "Scale to many tools with tool search" (SDK, new)
   - `changed` (11):
     - 5 CLI pages: `claude-code__desktop.md`, `claude-code__sandboxing.md`,
       `claude-code__plugin-marketplaces.md`, `claude-code__common-workflows.md`, `claude-code__settings.md`
     - 6 SDK pages: `claude-code__agent-sdk__custom-tools.md`, `claude-code__agent-sdk__mcp.md`,
       `claude-code__agent-sdk__python.md`, `claude-code__agent-sdk__typescript.md`,
       `claude-code__agent-sdk__user-input.md`, `claude-code__agent-sdk__sessions.md`
   - `removed` (0): empty
3. Each entry already carries `.category`, `.title`, `.url`, `.filename` — map `category`
   to a section label via `manifest-reference.md` (`claude_code` → CLI, `agent_sdk` → SDK)

### Phase 2: Analyze Changes
1. For each `added`/`changed` entry, read the current page at `~/.claude-code-docs/cache/<filename>`
   (if missing: `~/.claude-code-docs/plugin/scripts/fetch-docs.sh get "<filename>"` first).
   v2 keeps no prose history, so there is no line-level diff — summarize the page's current content
2. Group related changes (e.g., 6 SDK pages updated together → 1 card)
3. Extract highlights:
   - New: Tool Search feature in Agent SDK
   - Updated: Desktop app, Sandboxing, Plugin Marketplaces, Common Workflows
   - Updated: Custom Tools, MCP, Python/TypeScript SDKs, User Input

### Phase 3: Generate HTML
1. Create `~/.claude-code-docs/courses/changelog-2026-08-02.html`
2. Structure: header → stats bar → highlights → CLI section (5 cards) → SDK section (grouped cards)
3. Each card's source link is the entry's `.url` verbatim (e.g.
   `https://code.claude.com/docs/en/agent-sdk/tool-search`) — never reconstructed from the filename
4. Each card gets a "Create Course" button with `data-topic` extracted from filename;
   the button copies `/docs --course <topic>` to clipboard on click

### Phase 4: Open and Present
- Open in browser
- "Found 12 changes across 2 categories in the last 7 days. Saved to `~/.claude-code-docs/courses/changelog-2026-08-02.html`"

## Output
Self-contained HTML file with:
- Obsidian & Amber dark theme (matching course design system)
- Stats bar: 5 CLI, 7 SDK (1 new)
- Key highlights box with top 6 changes
- Grouped cards with summaries, bullet lists, source links
- Tags from diff semantics: `added` → New, `changed` → Updated, `removed` → Removed
- Each card has a "Create Course" button → copies clipboard command
- Toast notification on button click
