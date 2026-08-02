# Example: Semantic Search

## User Query
> /docs best practices for extended thinking

## Skill Reasoning
- User asks a question — no exact filename match for "best practices for extended thinking"
- Strategy: Content search (default for questions and topics)
- **Keyword extraction:** Strip filler words → `"extended"` `"thinking"`
- Check synonym table: "thinking" → also try "extended thinking", "adaptive thinking"

## Actions
1. Run:
   ```bash
   bash ~/.claude-code-docs/plugin/skills/claude-docs/scripts/content-search.sh "extended" "thinking"
   ```
2. Output is `filename<TAB>title<TAB>score`, best first:
   ```
   docs__en__build-with-claude__extended-thinking.md	Extended thinking (legacy)	81.97
   docs__en__build-with-claude__thinking.md	Overview	51
   docs__en__build-with-claude__thinking-troubleshooting.md	Troubleshooting	44.91
   docs__en__build-with-claude__thinking-steering-and-cost.md	Steering and cost control	37.97
   docs__en__build-with-claude__thinking-tool-workflows.md	Tool and multi-turn workflows	34.28
   ```
3. All are platform docs (same context) → read the top 2-3 from
   `~/.claude-code-docs/cache/<filename>`; on a cache miss, fetch first:
   `~/.claude-code-docs/plugin/scripts/fetch-docs.sh get "docs__en__build-with-claude__thinking.md"`
4. Note the top hit is titled "(legacy)" — lead with the current overview page, cite both
5. Get exact URLs from the manifest:
   ```bash
   jq -r '.pages[] | select(.filename=="docs__en__build-with-claude__thinking.md") | .url' ~/.claude-code-docs/paths_manifest.json
   ```

## Output Format
"Extended thinking lets Claude work through complex problems step by step before responding...

[Synthesized best practices from the matched docs]

Sources:
- [Thinking overview](https://platform.claude.com/docs/en/build-with-claude/thinking)
- [Extended thinking (legacy)](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)
- [Steering and cost control](https://platform.claude.com/docs/en/build-with-claude/thinking-steering-and-cost)"
