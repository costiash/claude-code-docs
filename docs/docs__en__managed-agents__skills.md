# Skills

Attach reusable, filesystem-based expertise to your agent for domain-specific workflows.

---

Skills are reusable, filesystem-based resources that give your agent domain-specific expertise: workflows, context, and best practices that turn a general-purpose agent into a specialist. Unlike prompts (conversation-level instructions for one-off tasks), skills load on demand, only impacting the context window when needed.

Two types of skill are supported. Both work the same way: your agent invokes them automatically when they are relevant to the task.

- **Pre-built Anthropic skills:** Common document tasks such as PowerPoint, Excel, Word, and PDF handling.
- **Custom skills:** Skills you author and upload to your organization.

To learn how to author custom skills, see the [Agent Skills overview](/docs/en/agents-and-tools/agent-skills/overview) and [best practices](/docs/en/agents-and-tools/agent-skills/best-practices). This page assumes you already have skills available in your organization or are using Anthropic pre-built skills.

<Note>
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
</Note>

## Enable skills on a session

Attach skills when creating an agent. A maximum of 20 skills per session is supported - this includes skills across all agents for the session, if you are working with [multiple agents](/docs/en/managed-agents/multi-agent).

<CodeGroup>
```bash curl
agent=$(curl -sS https://api.anthropic.com/v1/agents \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  --json @- <<'EOF'
{
  "name": "Financial Analyst",
  "model": "claude-opus-4-7",
  "system": "You are a financial analysis agent.",
  "skills": [
    {"type": "anthropic", "skill_id": "xlsx"},
    {"type": "custom", "skill_id": "skill_abc123", "version": "latest"}
  ]
}
EOF
)
```

```bash CLI nocheck
ant beta:agents create <<'YAML'
name: Financial Analyst
model: claude-opus-4-7
system: You are a financial analysis agent.
skills:
  - type: anthropic
    skill_id: xlsx
  - type: custom
    skill_id: skill_abc123
    version: latest
YAML
```

```python Python
agent = client.beta.agents.create(
    name="Financial Analyst",
    model="claude-opus-4-7",
    system="You are a financial analysis agent.",
    skills=[
        {
            "type": "anthropic",
            "skill_id": "xlsx",
        },
        {
            "type": "custom",
            "skill_id": "skill_abc123",
            "version": "latest",
        },
    ],
)
```

```typescript TypeScript
const agent = await client.beta.agents.create({
  name: "Financial Analyst",
  model: "claude-opus-4-7",
  system: "You are a financial analysis agent.",
  skills: [
    {
      type: "anthropic",
      skill_id: "xlsx"
    },
    {
      type: "custom",
      skill_id: "skill_abc123",
      version: "latest"
    }
  ]
});
```

```csharp C#
var agent = await client.Beta.Agents.Create(new()
{
    Name = "Financial Analyst",
    Model = BetaManagedAgentsModel.ClaudeOpus4_7,
    System = "You are a financial analysis agent.",
    Skills =
    [
        new BetaManagedAgentsAnthropicSkillParams { Type = BetaManagedAgentsAnthropicSkillParamsType.Anthropic, SkillID = "xlsx" },
        new BetaManagedAgentsCustomSkillParams { Type = BetaManagedAgentsCustomSkillParamsType.Custom, SkillID = "skill_abc123", Version = "latest" },
    ],
});
```

```go Go
agent, err := client.Beta.Agents.New(ctx, anthropic.BetaAgentNewParams{
	Name: "Financial Analyst",
	Model: anthropic.BetaManagedAgentsModelConfigParams{
		ID:   "claude-opus-4-7",
		Type: anthropic.BetaManagedAgentsModelConfigParamsTypeModelConfig,
	},
	System: anthropic.String("You are a financial analysis agent."),
	Skills: []anthropic.ManagedAgentsSkillParamUnion{
		{OfAnthropic: &anthropic.BetaManagedAgentsAnthropicSkillParams{
			SkillID: "xlsx",
			Type:    anthropic.BetaManagedAgentsAnthropicSkillParamsTypeAnthropic,
		}},
		{OfCustom: &anthropic.BetaManagedAgentsCustomSkillParams{
			SkillID: "skill_abc123",
			Type:    anthropic.BetaManagedAgentsCustomSkillParamsTypeCustom,
			Version: anthropic.String("latest"),
		}},
	},
})
if err != nil {
	panic(err)
}
```

```java Java
var agent = client.beta().agents().create(
    AgentCreateParams.builder()
        .name("Financial Analyst")
        .model(BetaManagedAgentsModel.CLAUDE_OPUS_4_7)
        .system("You are a financial analysis agent.")
        .addSkill(
            BetaManagedAgentsAnthropicSkillParams.builder()
                .type(BetaManagedAgentsAnthropicSkillParams.Type.ANTHROPIC)
                .skillId("xlsx")
                .build()
        )
        .addSkill(
            BetaManagedAgentsCustomSkillParams.builder()
                .type(BetaManagedAgentsCustomSkillParams.Type.CUSTOM)
                .skillId("skill_abc123")
                .version("latest")
                .build()
        )
        .build()
);
```

```php PHP
$agent = $client->beta->agents->create(
    name: 'Financial Analyst',
    model: 'claude-opus-4-7',
    system: 'You are a financial analysis agent.',
    skills: [
        ['type' => 'anthropic', 'skill_id' => 'xlsx'],
        ['type' => 'custom', 'skill_id' => 'skill_abc123', 'version' => 'latest'],
    ],
);
```

```ruby Ruby
agent = client.beta.agents.create(
  name: "Financial Analyst",
  model: "claude-opus-4-7",
  system_: "You are a financial analysis agent.",
  skills: [
    {type: "anthropic", skill_id: "xlsx"},
    {type: "custom", skill_id: "skill_abc123", version: "latest"}
  ]
)
```
</CodeGroup>

## Skill types

| Field | Description |
| --- | --- |
| `type` | Either `anthropic` for pre-built skills or `custom` for organization-authored skills. |
| `skill_id` | The skill identifier. For Anthropic skills, use the short name (for example, `xlsx`). For custom skills, use the `skill_*` ID returned at creation. |
| `version` | Custom skills only. Pin to a specific version or use `latest`. |