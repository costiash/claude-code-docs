# Example: Cross-Context Disambiguation

## User Query
> /docs skills

## Skill Reasoning
- User names a specific topic: "skills"
- Strategy: Direct manifest lookup
- Multiple product contexts expected

## Actions
1. Query the manifest:
   ```bash
   jq -r '.pages[] | select(.filename | test("skills")) | [.filename, .category] | @tsv' ~/.claude-code-docs/paths_manifest.json
   ```
2. Results span several product contexts (and both doc hosts):
   - `claude-code__skills.md` → **Claude Code** (code.claude.com)
   - `claude-code__agent-sdk__skills.md` → **Agent SDK** (code.claude.com)
   - `docs__en__api__beta__skills.md` and related → **Claude API** (platform.claude.com)
   - `docs__en__agents-and-tools__agent-skills__overview.md` and related → **Agents & Tools** (platform.claude.com)
3. Different contexts → ASK the user

## Output Format
"Skills exist across several Claude products with different purposes:

1. **Claude Code** — Install and run pre-built skills in the CLI
2. **Agent SDK** — Build custom agent capabilities in Python/TypeScript
3. **Claude API** — Programmatic skill management endpoints
4. **Agents & Tools** — Agent skill patterns and best practices

Which are you working with?"

[After user selects, e.g., "1. Claude Code"]

→ Read `~/.claude-code-docs/cache/claude-code__skills.md` (on a cache miss:
`~/.claude-code-docs/plugin/scripts/fetch-docs.sh get "claude-code__skills.md"` first),
synthesize, present with the manifest's source link
([Extend Claude with skills](https://code.claude.com/docs/en/skills)).

---

## User Query (with SDK context)
> /docs how do I create messages in Python?

## Skill Reasoning
- User mentions "Python" → SDK language disambiguation applies
- Topic: "messages" + "create" + Python client SDK

## Actions
1. Run: `bash ~/.claude-code-docs/plugin/skills/claude-docs/scripts/content-search.sh "python" "sdk"`
   → top hits include `docs__en__cli-sdks-libraries__sdks__python.md` (Python client SDK)
2. Fetch and read it, plus the API reference page `docs__en__api__messages__create.md`
   for the endpoint parameters
3. Present the Python SDK example
4. Note: "TypeScript equivalent: [TypeScript SDK](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/typescript)"

Sources:
- [Python SDK](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python)
- [Create a Message](https://platform.claude.com/docs/en/api/messages/create)
