# Example: Semantic Search

## User Query
> /docs best practices for extended thinking

## Skill Reasoning
- User asks a question — no exact filename match for "best practices for extended thinking"
- Strategy: Semantic/Content search (Priority 3)
- Extract keywords: "extended thinking", "best practices"

## Actions
1. Glob: `~/.claude-code-docs/docs/*extended*thinking*.md` → no matches
2. Run: `content-search.sh "extended" "thinking" "best practices"`
3. Results (sorted by relevance):
   - `docs__en__build-with-claude__adaptive-thinking.md` (3 matches)
   - `docs__en__build-with-claude__extended-thinking-tips.md` (2 matches)
   - `docs__en__api__messages__create.md` (1 match — mentions thinking parameter)
4. All are platform docs (same context) → read top 2-3, synthesize

## Output Format
"Extended thinking (also called adaptive thinking) lets Claude work through complex problems step by step before responding...

[Synthesized best practices from the matched docs]

Sources:
- [Adaptive Thinking](https://platform.claude.com/en/docs/build-with-claude/adaptive-thinking)
- [Extended Thinking Tips](https://platform.claude.com/en/docs/build-with-claude/extended-thinking-tips)"
