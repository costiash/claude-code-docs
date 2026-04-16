# Tools

Configure tools available to your agent.

---

Claude Managed Agents provides a set of built-in tools that Claude can use autonomously within a session. You control which tools are available by specifying them in the agent configuration.

Custom, user-defined tools are also supported. Your application executes these tools separately and sends the tool results back to Claude; Claude can use the results to continue the task at hand.

<Note>
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
</Note>

## Available tools

The agent toolset includes the following tools. All are enabled by default when you include the toolset in your agent configuration.

| Tool | Name | Description |
|---|---|---|
| Bash | `bash` | Execute bash commands in a shell session |
| Read | `read` | Read a file from the local filesystem |
| Write | `write` | Write a file to the local filesystem |
| Edit | `edit` | Perform string replacement in a file |
| Glob | `glob` | Fast file pattern matching using glob patterns |
| Grep | `grep` | Text search using regex patterns |
| Web fetch | `web_fetch` | Fetch content from a URL |
| Web search | `web_search` | Search the web for information |

## Configuring the toolset

Enable the full toolset with `agent_toolset_20260401` when creating an agent. Use the `configs` array to disable specific tools or override their settings.

<CodeGroup defaultLanguage="CLI">
```bash curl
agent=$(curl -fsSL https://api.anthropic.com/v1/agents \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d @- <<'EOF'
{
  "name": "Coding Assistant",
  "model": "claude-opus-4-7",
  "tools": [
    {
      "type": "agent_toolset_20260401",
      "configs": [
        {"name": "web_fetch", "enabled": false}
      ]
    }
  ]
}
EOF
)
```

```bash CLI
ant beta:agents create <<'YAML'
name: Coding Assistant
model: claude-opus-4-7
tools:
  - type: agent_toolset_20260401
    configs:
      - name: web_fetch
        enabled: false
YAML
```

```python Python
agent = client.beta.agents.create(
    name="Coding Assistant",
    model="claude-opus-4-7",
    tools=[
        {
            "type": "agent_toolset_20260401",
            "configs": [
                {"name": "web_fetch", "enabled": False},
            ],
        },
    ],
)
```

```typescript TypeScript
const agent = await client.beta.agents.create({
  name: "Coding Assistant",
  model: "claude-opus-4-7",
  tools: [
    {
      type: "agent_toolset_20260401",
      configs: [{ name: "web_fetch", enabled: false }]
    }
  ]
});
```

```csharp C#
var agent = await client.Beta.Agents.Create(new()
{
    Name = "Coding Assistant",
    Model = new("claude-opus-4-7"),
    Tools =
    [
        new BetaManagedAgentsAgentToolset20260401Params
        {
            Type = "agent_toolset_20260401",
            Configs =
            [
                new() { Name = "web_fetch", Enabled = false },
            ],
        },
    ],
});
```

```go Go
agent, err := client.Beta.Agents.New(ctx, anthropic.BetaAgentNewParams{
	Name: "Coding Assistant",
	Model: anthropic.BetaManagedAgentsModelConfigParams{
		ID:   "claude-opus-4-7",
		Type: anthropic.BetaManagedAgentsModelConfigParamsTypeModelConfig,
	},
	Tools: []anthropic.BetaAgentNewParamsToolUnion{{
		OfAgentToolset20260401: &anthropic.BetaManagedAgentsAgentToolset20260401Params{
			Type: anthropic.BetaManagedAgentsAgentToolset20260401ParamsTypeAgentToolset20260401,
			Configs: []anthropic.BetaManagedAgentsAgentToolConfigParams{{
				Name:    anthropic.BetaManagedAgentsAgentToolConfigParamsNameWebFetch,
				Enabled: anthropic.Bool(false),
			}},
		},
	}},
})
if err != nil {
	panic(err)
}
```

```java Java
var agent = client.beta().agents().create(AgentCreateParams.builder()
    .name("Coding Assistant")
    .model(BetaManagedAgentsModel.CLAUDE_OPUS_4_7)
    .addTool(BetaManagedAgentsAgentToolset20260401Params.builder()
        .type(BetaManagedAgentsAgentToolset20260401Params.Type.AGENT_TOOLSET_20260401)
        .addConfig(BetaManagedAgentsAgentToolConfigParams.builder()
            .name(BetaManagedAgentsAgentToolConfigParams.Name.WEB_FETCH)
            .enabled(false)
            .build())
        .build())
    .build());
```

```php PHP

$agent = $client->beta->agents->create(
    name: 'Coding Assistant',
    model: 'claude-opus-4-7',
    tools: [
        BetaManagedAgentsAgentToolset20260401Params::with(
            type: 'agent_toolset_20260401',
            configs: [
                BetaManagedAgentsAgentToolConfigParams::with(name: 'web_fetch', enabled: false),
            ],
        ),
    ],
);
```

```ruby Ruby
agent = client.beta.agents.create(
  name: "Coding Assistant",
  model: "claude-opus-4-7",
  tools: [
    {
      type: :agent_toolset_20260401,
      configs: [
        {name: :web_fetch, enabled: false}
      ]
    }
  ]
)
```
</CodeGroup>

### Disabling specific tools

To disable a tool, set `enabled: false` in its config entry:

```json
{
  "type": "agent_toolset_20260401",
  "configs": [
    { "name": "web_fetch", "enabled": false },
    { "name": "web_search", "enabled": false }
  ]
}
```

### Enabling only specific tools

To start with everything off and enable only what you need, set `default_config.enabled` to `false`:

```json
{
  "type": "agent_toolset_20260401",
  "default_config": { "enabled": false },
  "configs": [
    { "name": "bash", "enabled": true },
    { "name": "read", "enabled": true },
    { "name": "write", "enabled": true }
  ]
}
```

## Custom tools

In addition to built-in tools, you can define custom tools. Custom tools are analogous to [user-defined client tools](/docs/en/agents-and-tools/tool-use/how-tool-use-works#user-defined-tools-client-executed) in the Messages API.

Custom tools allow you to extend Claude's capabilities to perform a wider variety of tasks. Each tool defines a contract: you specify what operations are available and what they return; Claude decides when and how to call them. The model never executes anything on its own. It emits a structured request, your code runs the operation, and the result flows back into the conversation.

<CodeGroup defaultLanguage="CLI">
```bash curl
agent=$(curl -fsSL https://api.anthropic.com/v1/agents \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d @- <<'EOF'
{
  "name": "Weather Agent",
  "model": "claude-opus-4-7",
  "tools": [
    {
      "type": "agent_toolset_20260401"
    },
    {
      "type": "custom",
      "name": "get_weather",
      "description": "Get current weather for a location",
      "input_schema": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "City name"}
        },
        "required": ["location"]
      }
    }
  ]
}
EOF
)
```

```bash CLI
ant beta:agents create <<'YAML'
name: Weather Agent
model: claude-opus-4-7
tools:
  - type: agent_toolset_20260401
  - type: custom
    name: get_weather
    description: Get current weather for a location
    input_schema:
      type: object
      properties:
        location:
          type: string
          description: City name
      required:
        - location
YAML
```

```python Python
agent = client.beta.agents.create(
    name="Weather Agent",
    model="claude-opus-4-7",
    tools=[
        {
            "type": "agent_toolset_20260401",
        },
        {
            "type": "custom",
            "name": "get_weather",
            "description": "Get current weather for a location",
            "input_schema": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "City name"},
                },
                "required": ["location"],
            },
        },
    ],
)
```

```typescript TypeScript
const agent = await client.beta.agents.create({
  name: "Weather Agent",
  model: "claude-opus-4-7",
  tools: [
    { type: "agent_toolset_20260401" },
    {
      type: "custom",
      name: "get_weather",
      description: "Get current weather for a location",
      input_schema: {
        type: "object",
        properties: { location: { type: "string", description: "City name" } },
        required: ["location"]
      }
    }
  ]
});
```

```csharp C#

var agent = await client.Beta.Agents.Create(new()
{
    Name = "Weather Agent",
    Model = new("claude-opus-4-7"),
    Tools =
    [
        new BetaManagedAgentsAgentToolset20260401Params
        {
            Type = "agent_toolset_20260401",
        },
        new BetaManagedAgentsCustomToolParams
        {
            Type = "custom",
            Name = "get_weather",
            Description = "Get current weather for a location",
            InputSchema = new()
            {
                Type = "object",
                Properties = new Dictionary<string, JsonElement>
                {
                    ["location"] = JsonSerializer.SerializeToElement(
                        new { type = "string", description = "City name" }
                    ),
                },
                Required = ["location"],
            },
        },
    ],
});
```

```go Go
agent, err := client.Beta.Agents.New(ctx, anthropic.BetaAgentNewParams{
	Name: "Weather Agent",
	Model: anthropic.BetaManagedAgentsModelConfigParams{
		ID:   "claude-opus-4-7",
		Type: anthropic.BetaManagedAgentsModelConfigParamsTypeModelConfig,
	},
	Tools: []anthropic.BetaAgentNewParamsToolUnion{{
		OfAgentToolset20260401: &anthropic.BetaManagedAgentsAgentToolset20260401Params{
			Type: anthropic.BetaManagedAgentsAgentToolset20260401ParamsTypeAgentToolset20260401,
		},
	}, {
		OfCustom: &anthropic.BetaManagedAgentsCustomToolParams{
			Type:        anthropic.BetaManagedAgentsCustomToolParamsTypeCustom,
			Name:        "get_weather",
			Description: "Get current weather for a location",
			InputSchema: anthropic.BetaManagedAgentsCustomToolInputSchemaParam{
				Type: anthropic.BetaManagedAgentsCustomToolInputSchemaTypeObject,
				Properties: map[string]any{
					"location": map[string]any{
						"type":        "string",
						"description": "City name",
					},
				},
				Required: []string{"location"},
			},
		},
	}},
})
if err != nil {
	panic(err)
}
```

```java Java
var agent = client.beta().agents().create(AgentCreateParams.builder()
    .name("Weather Agent")
    .model(BetaManagedAgentsModel.CLAUDE_OPUS_4_7)
    .addTool(BetaManagedAgentsAgentToolset20260401Params.builder()
        .type(BetaManagedAgentsAgentToolset20260401Params.Type.AGENT_TOOLSET_20260401)
        .build())
    .addTool(BetaManagedAgentsCustomToolParams.builder()
        .type(BetaManagedAgentsCustomToolParams.Type.CUSTOM)
        .name("get_weather")
        .description("Get current weather for a location")
        .inputSchema(BetaManagedAgentsCustomToolInputSchema.builder()
            .type(BetaManagedAgentsCustomToolInputSchema.Type.OBJECT)
            .properties(BetaManagedAgentsCustomToolInputSchema.Properties.builder()
                .putAdditionalProperty("location", JsonValue.from(Map.of(
                    "type", "string",
                    "description", "City name")))
                .build())
            .addRequired("location")
            .build())
        .build())
    .build());
```

```php PHP
use Anthropic\Beta\Agents\BetaManagedAgentsCustomToolInputSchema;
use Anthropic\Beta\Agents\BetaManagedAgentsCustomToolParams;

$agent = $client->beta->agents->create(
    name: 'Weather Agent',
    model: 'claude-opus-4-7',
    tools: [
        BetaManagedAgentsAgentToolset20260401Params::with(
            type: 'agent_toolset_20260401',
        ),
        BetaManagedAgentsCustomToolParams::with(
            type: 'custom',
            name: 'get_weather',
            description: 'Get current weather for a location',
            inputSchema: BetaManagedAgentsCustomToolInputSchema::with(
                type: 'object',
                properties: ['location' => ['type' => 'string', 'description' => 'City name']],
                required: ['location'],
            ),
        ),
    ],
);
```

```ruby Ruby
agent = client.beta.agents.create(
  name: "Weather Agent",
  model: "claude-opus-4-7",
  tools: [
    {type: :agent_toolset_20260401},
    {
      type: :custom,
      name: "get_weather",
      description: "Get current weather for a location",
      input_schema: {
        type: :object,
        properties: {location: {type: "string", description: "City name"}},
        required: ["location"]
      }
    }
  ]
)
```
</CodeGroup>

Once you've defined the tool at the agent level, the agent will invoke the tools through the course of a session. See [Session event stream](/docs/en/managed-agents/events-and-streaming#handling-custom-tool-calls) for the full flow.

### Best practices for custom tool definitions

- **Provide extremely detailed descriptions.** This is by far the most important factor in tool performance. Your descriptions should explain what the tool does, when it should be used (and when it shouldn't), what each parameter means and how it affects the tool's behavior, and any important caveats or limitations. The more context you can give Claude about your tools, the better it will be at deciding when and how to use them. Aim for at least 3-4 sentences per tool description, more if the tool is complex.
- **Consolidate related operations into fewer tools.** Rather than creating a separate tool for every action (`create_pr`, `review_pr`, `merge_pr`), group them into a single tool with an `action` parameter. Fewer, more capable tools reduce selection ambiguity and make your tool surface easier for Claude to navigate.
- **Use meaningful namespacing in tool names.** When your tools span multiple services or resources, prefix names with the resource (e.g., `db_query`, `storage_read`). This makes tool selection unambiguous as your library grows.
- **Design tool responses to return only high-signal information.** Return semantic, stable identifiers (e.g., slugs or UUIDs) rather than opaque internal references, and include only the fields Claude needs to reason about its next step. Bloated responses waste context and make it harder for Claude to extract what matters.