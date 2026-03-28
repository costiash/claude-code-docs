# Example: Interactive Course from Documentation

## User Query
> /docs --course hooks

## Skill Reasoning
- User requests an interactive course on "hooks"
- Strategy: Topic Discovery → find all hooks-related documentation files

## Actions

### Phase 1: Topic Discovery
1. **Glob:** `~/.claude-code-docs/docs/*hooks*.md`
   - Results: `claude-code__hooks.md`, `claude-code__hooks-guide.md`, `docs__en__agent-sdk__hooks.md`
2. **Read all 3 files** — extract concept definitions, JSON config examples, matcher patterns, event types, lifecycle details
3. **Adjacent docs for context:** Skim `claude-code__skills.md`, `claude-code__settings.md` for related features
4. **Extracted material:**
   - Hook event types: PreToolUse, PostToolUse, SessionStart, etc.
   - JSON configuration format with matcher patterns
   - Shell script examples for hook commands
   - Agent SDK hook variants (Python/TypeScript)

### Phase 2: Curriculum Design
Design 6-module curriculum:

| # | Title | Key Visual |
|---|-------|-----------|
| 1 | What Are Hooks & Why They Matter | Feature cards showing automation scenarios |
| 2 | The Hook Lifecycle | Data flow animation: User action → event → matcher → hook → result |
| 3 | See It In Action | Code translations of hook JSON configs |
| 4 | Matchers & Advanced Patterns | Scenario quiz on matcher patterns |
| 5 | Common Recipes | Pattern cards: auto-format, CI gates, security checks |
| 6 | Hooks in the Ecosystem | Protocol conversation: Claude ↔ Hook Handler ↔ Tool |

### Phase 3: Build
1. Foundation: HTML shell, CSS design system, nav, scroll-snap
2. Module 1: Intro + feature cards
3. Module 2: Lifecycle animation + event type badges
4. Module 3: Hook JSON → English translations
5. Module 4: Matcher quiz + advanced config translations
6. Module 5: Recipe pattern cards + drag-and-drop matching
7. Module 6: Protocol conversation + architecture diagram
8. Polish pass

### Phase 4: Review
- Open HTML in browser
- Walk user through: "Here's what we built — 6 modules covering hooks from concept to advanced patterns"
- Ask for feedback

## Output Format
A single self-contained HTML file (~80-120KB) with:
- 6 scroll-snap modules with progress nav
- Protocol conversation showing hook execution flow
- Code ↔ English translations of hook JSON configs
- Data flow animation of the hook lifecycle
- Multiple-choice quizzes testing practical hook configuration
- Glossary tooltips on terms: matchers, IIFE, ARIA, stdin, SSE, MCP
- Obsidian & Amber design aesthetic (Instrument Serif + Outfit + JetBrains Mono)
