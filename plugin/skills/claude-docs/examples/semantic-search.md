# Example: Semantic Search

## User Query
> /docs best practices for extended thinking

## Skill Reasoning
- User asks a question — no exact filename match for "best practices for extended thinking"
- Strategy: Semantic/Content search (Priority 3)
- **Keyword extraction:** Strip filler words → `"extended"` `"thinking"`
- Check synonym table: "thinking" → also try "extended thinking", "adaptive thinking"

## Actions
1. Glob: `~/.claude-code-docs/docs/*extended*thinking*.md` → matches found
   - `docs__en__build-with-claude__extended-thinking.md`
2. Run: `content-search.sh "extended" "thinking"` for additional results
3. Results (sorted by relevance):
   - `docs__en__build-with-claude__adaptive-thinking.md` (2 matches — keywords + preview)
   - `docs__en__build-with-claude__extended-thinking.md` (2 matches — keywords + filename)
   - `docs__en__api__messages__create.md` (1 match — mentions thinking parameter)
4. All are platform docs (same context) → read top 2-3, synthesize

## Output Format
"Extended thinking (also called adaptive thinking) lets Claude work through complex problems step by step before responding...

[Synthesized best practices from the matched docs]

Sources:
- [Extended Thinking](https://platform.claude.com/en/docs/build-with-claude/extended-thinking)
- [Adaptive Thinking](https://platform.claude.com/en/docs/build-with-claude/adaptive-thinking)"
