# Prototype in Console

Create and test agents visually in Console without writing API calls.

---

[Console](https://platform.claude.com/workspaces/default/agent-quickstart/)  provides a visual interface for creating and configuring agents. It produces the same `/v1/agents` and `/v1/sessions` resources as the API but lets you iterate on configuration interactively before writing code.

<Note>
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
</Note>

## How to build an agent

The [visual interface](https://platform.claude.com/workspaces/default/agent-quickstart/) walks you through each field of an agent definition:

- **Model and system prompt:** Pick a model and write the system prompt in a full-width editor.
- **MCP servers:** Add remote MCP servers by URL and authenticate your agent to take action on your behalf.
- **Tools:** Extend your agent's capabilities using a pre-built agent toolset and MCP tools.
- **Skills:** Attach Anthropic or custom skills from your organization's library.

As you configure, Console shows the equivalent API request so you can copy it into your code once you're satisfied.

## Testing an agent

Console includes an inline session runner. After configuring your agent, you can start a test session directly, send messages, and watch the event stream without leaving the page. This is the fastest way to check that your system prompt and tool selection produce the behavior you expect.

## From prototype to code

Once your agent works as expected:

1. Copy the agent ID from Console output.
2. Reference it in your code when [creating sessions](/docs/en/managed-agents/sessions):

<CodeGroup>

```bash curl
session=$(curl -fsSL https://api.anthropic.com/v1/sessions \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d '{
    "agent": "agent_01XXXXXXXXXXXXXXXXXXXXXX",
    "environment_id": "env_01XXXXXXXXXXXXXXXXXXXXXX",
    "title": "My first session"
  }')
```

```bash CLI
ant beta:sessions create \
  --agent agent_01XXXXXXXXXXXXXXXXXXXXXX \
  --environment-id env_01XXXXXXXXXXXXXXXXXXXXXX \
  --title "My first session"
```

```python Python
session = client.beta.sessions.create(
    agent="agent_01XXXXXXXXXXXXXXXXXXXXXX",
    environment_id="env_01XXXXXXXXXXXXXXXXXXXXXX",
    title="My first session",
)
```

```typescript TypeScript
const session = await client.beta.sessions.create({
  agent: "agent_01XXXXXXXXXXXXXXXXXXXXXX",
  environment_id: "env_01XXXXXXXXXXXXXXXXXXXXXX",
  title: "My first session"
});
```

```csharp C#
var session = await client.Beta.Sessions.Create(new()
{
    Agent = "agent_01XXXXXXXXXXXXXXXXXXXXXX",
    EnvironmentID = "env_01XXXXXXXXXXXXXXXXXXXXXX",
    Title = "My first session",
});
```

```go Go
session, err := client.Beta.Sessions.New(ctx, anthropic.BetaSessionNewParams{
	Agent: anthropic.BetaSessionNewParamsAgentUnion{
		OfBetaManagedAgentsAgents: &anthropic.BetaManagedAgentsAgentParams{
			Type:    anthropic.BetaManagedAgentsAgentParamsTypeAgent,
			ID:      "agent_01XXXXXXXXXXXXXXXXXXXXXX",
			Version: anthropic.Int(1),
		},
	},
	EnvironmentID: "env_01XXXXXXXXXXXXXXXXXXXXXX",
	Title:         anthropic.String("My first session"),
})
if err != nil {
	panic(err)
}
_ = session
```

```java Java
var session = client.beta().sessions().create(
    SessionCreateParams.builder()
        .agent("agent_01XXXXXXXXXXXXXXXXXXXXXX")
        .environmentId("env_01XXXXXXXXXXXXXXXXXXXXXX")
        .title("My first session")
        .build()
);
```

```php PHP
$session = $client->beta->sessions->create(
    agent: 'agent_01XXXXXXXXXXXXXXXXXXXXXX',
    environmentID: 'env_01XXXXXXXXXXXXXXXXXXXXXX',
    title: 'My first session',
);
```

```ruby Ruby
session = client.beta.sessions.create(
  agent: "agent_01XXXXXXXXXXXXXXXXXXXXXX",
  environment_id: "env_01XXXXXXXXXXXXXXXXXXXXXX",
  title: "My first session"
)
```
</CodeGroup>