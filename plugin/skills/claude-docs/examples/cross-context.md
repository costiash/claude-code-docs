# Example: Cross-Context Disambiguation

## User Query
> /docs skills

## Skill Reasoning
- User names a specific topic: "skills"
- Strategy: Direct lookup (Priority 1)
- Multiple product contexts expected

## Actions
1. Glob: `~/.claude-code-docs/docs/*skills*.md`
2. Results span 3 product contexts:
   - `claude-code__skills.md` → **Claude Code**
   - `docs__en__agent-sdk__skills.md` → **Agent SDK**
   - `docs__en__api__beta__skills.md` and related → **Claude API**
   - `docs__en__agents-and-tools__agent-skills__*.md` → **Agents & Tools**
3. Different contexts → ASK the user

## Output Format
"Skills exist across several Claude products with different purposes:

1. **Claude Code** — Install and run pre-built skills in the CLI
2. **Agent SDK** — Build custom agent capabilities in Python/TypeScript
3. **Claude API** — Programmatic skill management endpoints
4. **Agents & Tools** — Agent skill patterns and best practices

Which are you working with?"

[After user selects, e.g., "1. Claude Code"]

→ Read `claude-code__skills.md`, synthesize, present with source link.
