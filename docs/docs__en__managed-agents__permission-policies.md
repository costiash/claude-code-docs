# Permission policies

Control when agent and MCP tools execute.

---

Permission policies control whether server-executed tools (the pre-built agent toolset and MCP toolset) run automatically or wait for your approval. Custom tools are executed by your application and controlled by you, so they are not governed by permission policies.

<Note>
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
</Note>

## Permission policy types

| Policy | Behavior |
| --- | --- |
| `always_allow` | The tool executes automatically with no confirmation. |
| `always_ask` | The session pauses and waits for your approval before executing. See [Respond to confirmation requests](#respond-to-confirmation-requests) for the event flow. |

## Set a policy for a toolset

### Agent toolset permissions
When creating an agent, you may optionally apply a policy to every tool in `agent_toolset_20260401` using `default_config.permission_policy`:

<CodeGroup defaultLanguage="CLI">
```bash curl
agent=$(curl -fsSL https://api.anthropic.com/v1/agents \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d '{
    "name": "Coding Assistant",
    "model": "claude-opus-4-7",
    "tools": [
      {
        "type": "agent_toolset_20260401",
        "default_config": {
          "permission_policy": {"type": "always_ask"}
        }
      }
    ]
  }')
```

```bash CLI
ant beta:agents create <<'YAML'
name: Coding Assistant
model: claude-opus-4-7
tools:
  - type: agent_toolset_20260401
    default_config:
      permission_policy:
        type: always_ask
YAML
```

```python Python
agent = client.beta.agents.create(
    name="Coding Assistant",
    model="claude-opus-4-7",
    tools=[
        {
            "type": "agent_toolset_20260401",
            "default_config": {
                "permission_policy": {"type": "always_ask"},
            },
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
      default_config: {
        permission_policy: { type: "always_ask" }
      }
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
            DefaultConfig = new()
            {
                PermissionPolicy = new BetaManagedAgentsAlwaysAskPolicy { Type = "always_ask" },
            },
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
			DefaultConfig: anthropic.BetaManagedAgentsAgentToolsetDefaultConfigParams{
				PermissionPolicy: anthropic.BetaManagedAgentsAgentToolsetDefaultConfigParamsPermissionPolicyUnion{
					OfAlwaysAsk: &anthropic.BetaManagedAgentsAlwaysAskPolicyParam{
						Type: anthropic.BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk,
					},
				},
			},
		},
	}},
})
if err != nil {
	panic(err)
}
```

```java Java
var agent = client.beta().agents().create(
    AgentCreateParams.builder()
        .name("Coding Assistant")
        .model(BetaManagedAgentsModel.CLAUDE_OPUS_4_7)
        .addTool(
            BetaManagedAgentsAgentToolset20260401Params.builder()
                .type(BetaManagedAgentsAgentToolset20260401Params.Type.AGENT_TOOLSET_20260401)
                .defaultConfig(
                    BetaManagedAgentsAgentToolsetDefaultConfigParams.builder()
                        .permissionPolicy(
                            BetaManagedAgentsAlwaysAskPolicy.builder()
                                .type(BetaManagedAgentsAlwaysAskPolicy.Type.ALWAYS_ASK)
                                .build()
                        )
                        .build()
                )
                .build()
        )
        .build()
);
```

```php PHP
$agent = $client->beta->agents->create(
    name: 'Coding Assistant',
    model: 'claude-opus-4-7',
    tools: [
        BetaManagedAgentsAgentToolset20260401Params::with(
            type: 'agent_toolset_20260401',
            defaultConfig: BetaManagedAgentsAgentToolsetDefaultConfigParams::with(
                permissionPolicy: BetaManagedAgentsAlwaysAskPolicy::with(type: 'always_ask'),
            ),
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
      type: "agent_toolset_20260401",
      default_config: {
        permission_policy: {type: "always_ask"}
      }
    }
  ]
)
```
</CodeGroup>

`default_config` is an optional setting. If you omit it, the agent toolset will be enabled with the default permission policy, `always_allow`.

### MCP toolset permissions

MCP toolsets default to `always_ask`. This ensures that new tools that are added to an MCP server do not execute in your application without approval. To auto-approve tools from a trusted MCP server, set `default_config.permission_policy` on the `mcp_toolset` entry.

The `mcp_server_name` must match the `name` referenced in the `mcp_servers` array.

This example connects a GitHub MCP server and allows its tools to run without confirmation:

<CodeGroup defaultLanguage="CLI">
```bash curl
agent=$(curl -fsSL https://api.anthropic.com/v1/agents \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d '{
    "name": "Dev Assistant",
    "model": "claude-opus-4-7",
    "mcp_servers": [
      {"type": "url", "name": "github", "url": "https://mcp.example.com/github"}
    ],
    "tools": [
      {"type": "agent_toolset_20260401"},
      {
        "type": "mcp_toolset",
        "mcp_server_name": "github",
        "default_config": {
          "permission_policy": {"type": "always_allow"}
        }
      }
    ]
  }')
```

```bash CLI
ant beta:agents create <<'YAML'
name: Dev Assistant
model: claude-opus-4-7
mcp_servers:
  - type: url
    name: github
    url: https://mcp.example.com/github
tools:
  - type: agent_toolset_20260401
  - type: mcp_toolset
    mcp_server_name: github
    default_config:
      permission_policy:
        type: always_allow
YAML
```

```python Python
agent = client.beta.agents.create(
    name="Dev Assistant",
    model="claude-opus-4-7",
    mcp_servers=[
        {"type": "url", "name": "github", "url": "https://mcp.example.com/github"},
    ],
    tools=[
        {"type": "agent_toolset_20260401"},
        {
            "type": "mcp_toolset",
            "mcp_server_name": "github",
            "default_config": {
                "permission_policy": {"type": "always_allow"},
            },
        },
    ],
)
```

```typescript TypeScript
const agent = await client.beta.agents.create({
  name: "Dev Assistant",
  model: "claude-opus-4-7",
  mcp_servers: [{ type: "url", name: "github", url: "https://mcp.example.com/github" }],
  tools: [
    { type: "agent_toolset_20260401" },
    {
      type: "mcp_toolset",
      mcp_server_name: "github",
      default_config: {
        permission_policy: { type: "always_allow" }
      }
    }
  ]
});
```

```csharp C#
var agent = await client.Beta.Agents.Create(new()
{
    Name = "Dev Assistant",
    Model = new("claude-opus-4-7"),
    McpServers =
    [
        new() { Type = "url", Name = "github", Url = "https://mcp.example.com/github" },
    ],
    Tools =
    [
        new BetaManagedAgentsAgentToolset20260401Params
        {
            Type = "agent_toolset_20260401",
        },
        new BetaManagedAgentsMcpToolsetParams
        {
            Type = "mcp_toolset",
            McpServerName = "github",
            DefaultConfig = new()
            {
                PermissionPolicy = new BetaManagedAgentsAlwaysAllowPolicy { Type = "always_allow" },
            },
        },
    ],
});
```

```go Go
agent, err := client.Beta.Agents.New(ctx, anthropic.BetaAgentNewParams{
	Name: "Dev Assistant",
	Model: anthropic.BetaManagedAgentsModelConfigParams{
		ID:   "claude-opus-4-7",
		Type: anthropic.BetaManagedAgentsModelConfigParamsTypeModelConfig,
	},
	MCPServers: []anthropic.BetaManagedAgentsUrlmcpServerParams{{
		Type: anthropic.BetaManagedAgentsUrlmcpServerParamsTypeURL,
		Name: "github",
		URL:  "https://mcp.example.com/github",
	}},
	Tools: []anthropic.BetaAgentNewParamsToolUnion{
		{
			OfAgentToolset20260401: &anthropic.BetaManagedAgentsAgentToolset20260401Params{
				Type: anthropic.BetaManagedAgentsAgentToolset20260401ParamsTypeAgentToolset20260401,
			},
		},
		{
			OfMCPToolset: &anthropic.BetaManagedAgentsMCPToolsetParams{
				Type:          anthropic.BetaManagedAgentsMCPToolsetParamsTypeMCPToolset,
				MCPServerName: "github",
				DefaultConfig: anthropic.BetaManagedAgentsMCPToolsetDefaultConfigParams{
					PermissionPolicy: anthropic.BetaManagedAgentsMCPToolsetDefaultConfigParamsPermissionPolicyUnion{
						OfAlwaysAllow: &anthropic.BetaManagedAgentsAlwaysAllowPolicyParam{
							Type: anthropic.BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow,
						},
					},
				},
			},
		},
	},
})
if err != nil {
	panic(err)
}
```

```java Java
var agent = client.beta().agents().create(
    AgentCreateParams.builder()
        .name("Dev Assistant")
        .model(BetaManagedAgentsModel.CLAUDE_OPUS_4_7)
        .addMcpServer(
            BetaManagedAgentsUrlmcpServerParams.builder()
                .type(BetaManagedAgentsUrlmcpServerParams.Type.URL)
                .name("github")
                .url("https://mcp.example.com/github")
                .build()
        )
        .addTool(
            BetaManagedAgentsAgentToolset20260401Params.builder()
                .type(BetaManagedAgentsAgentToolset20260401Params.Type.AGENT_TOOLSET_20260401)
                .build()
        )
        .addTool(
            BetaManagedAgentsMcpToolsetParams.builder()
                .type(BetaManagedAgentsMcpToolsetParams.Type.MCP_TOOLSET)
                .mcpServerName("github")
                .defaultConfig(
                    BetaManagedAgentsMcpToolsetDefaultConfigParams.builder()
                        .permissionPolicy(
                            BetaManagedAgentsAlwaysAllowPolicy.builder()
                                .type(BetaManagedAgentsAlwaysAllowPolicy.Type.ALWAYS_ALLOW)
                                .build()
                        )
                        .build()
                )
                .build()
        )
        .build()
);
```

```php PHP
use Anthropic\Beta\Agents\BetaManagedAgentsMCPToolsetDefaultConfigParams;
use Anthropic\Beta\Agents\BetaManagedAgentsMCPToolsetParams;
use Anthropic\Beta\Agents\BetaManagedAgentsUrlmcpServerParams;

$agent = $client->beta->agents->create(
    name: 'Dev Assistant',
    model: 'claude-opus-4-7',
    mcpServers: [
        BetaManagedAgentsUrlmcpServerParams::with(
            type: 'url',
            name: 'github',
            url: 'https://mcp.example.com/github',
        ),
    ],
    tools: [
        BetaManagedAgentsAgentToolset20260401Params::with(
            type: 'agent_toolset_20260401',
        ),
        BetaManagedAgentsMCPToolsetParams::with(
            type: 'mcp_toolset',
            mcpServerName: 'github',
            defaultConfig: BetaManagedAgentsMCPToolsetDefaultConfigParams::with(
                permissionPolicy: BetaManagedAgentsAlwaysAllowPolicy::with(type: 'always_allow'),
            ),
        ),
    ],
);
```

```ruby Ruby
agent = client.beta.agents.create(
  name: "Dev Assistant",
  model: "claude-opus-4-7",
  mcp_servers: [
    {type: "url", name: "github", url: "https://mcp.example.com/github"}
  ],
  tools: [
    {type: "agent_toolset_20260401"},
    {
      type: "mcp_toolset",
      mcp_server_name: "github",
      default_config: {
        permission_policy: {type: "always_allow"}
      }
    }
  ]
)
```
</CodeGroup>

## Override an individual tool policy

Use the `configs` array to override the default for individual tools. This example allows the full agent toolset by default but requires confirmation before any bash command runs:

<CodeGroup defaultLanguage="CLI">
```bash curl
tools='[
  {
    "type": "agent_toolset_20260401",
    "default_config": {
      "permission_policy": {"type": "always_allow"}
    },
    "configs": [
      {
        "name": "bash",
        "permission_policy": {"type": "always_ask"}
      }
    ]
  }
]'
```

```bash CLI
tools=$(cat <<'YAML'
- type: agent_toolset_20260401
  default_config:
    permission_policy:
      type: always_allow
  configs:
    - name: bash
      permission_policy:
        type: always_ask
YAML
)
```

```python Python
tools = [
    {
        "type": "agent_toolset_20260401",
        "default_config": {
            "permission_policy": {"type": "always_allow"},
        },
        "configs": [
            {
                "name": "bash",
                "permission_policy": {"type": "always_ask"},
            },
        ],
    },
]
```

```typescript TypeScript
const tools = [
  {
    type: "agent_toolset_20260401",
    default_config: {
      permission_policy: { type: "always_allow" }
    },
    configs: [
      {
        name: "bash",
        permission_policy: { type: "always_ask" }
      }
    ]
  }
] satisfies Anthropic.Beta.AgentCreateParams["tools"];
```

```csharp C#
Tool[] tools =
[
    new BetaManagedAgentsAgentToolset20260401Params
    {
        Type = "agent_toolset_20260401",
        DefaultConfig = new()
        {
            PermissionPolicy = new BetaManagedAgentsAlwaysAllowPolicy { Type = "always_allow" },
        },
        Configs =
        [
            new()
            {
                Name = "bash",
                PermissionPolicy = new BetaManagedAgentsAlwaysAskPolicy { Type = "always_ask" },
            },
        ],
    },
];
```

```go Go
tools := []anthropic.BetaAgentNewParamsToolUnion{{
	OfAgentToolset20260401: &anthropic.BetaManagedAgentsAgentToolset20260401Params{
		Type: anthropic.BetaManagedAgentsAgentToolset20260401ParamsTypeAgentToolset20260401,
		DefaultConfig: anthropic.BetaManagedAgentsAgentToolsetDefaultConfigParams{
			PermissionPolicy: anthropic.BetaManagedAgentsAgentToolsetDefaultConfigParamsPermissionPolicyUnion{
				OfAlwaysAllow: &anthropic.BetaManagedAgentsAlwaysAllowPolicyParam{
					Type: anthropic.BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow,
				},
			},
		},
		Configs: []anthropic.BetaManagedAgentsAgentToolConfigParams{{
			Name: anthropic.BetaManagedAgentsAgentToolConfigParamsNameBash,
			PermissionPolicy: anthropic.BetaManagedAgentsAgentToolConfigParamsPermissionPolicyUnion{
				OfAlwaysAsk: &anthropic.BetaManagedAgentsAlwaysAskPolicyParam{
					Type: anthropic.BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk,
				},
			},
		}},
	},
}}
```

```java Java
var tools = List.of(
    AgentCreateParams.Tool.ofAgentToolset20260401(
        BetaManagedAgentsAgentToolset20260401Params.builder()
            .type(BetaManagedAgentsAgentToolset20260401Params.Type.AGENT_TOOLSET_20260401)
            .defaultConfig(
                BetaManagedAgentsAgentToolsetDefaultConfigParams.builder()
                    .permissionPolicy(
                        BetaManagedAgentsAlwaysAllowPolicy.builder()
                            .type(BetaManagedAgentsAlwaysAllowPolicy.Type.ALWAYS_ALLOW)
                            .build()
                    )
                    .build()
            )
            .addConfig(
                BetaManagedAgentsAgentToolConfigParams.builder()
                    .name(BetaManagedAgentsAgentToolConfigParams.Name.BASH)
                    .permissionPolicy(
                        BetaManagedAgentsAlwaysAskPolicy.builder()
                            .type(BetaManagedAgentsAlwaysAskPolicy.Type.ALWAYS_ASK)
                            .build()
                    )
                    .build()
            )
            .build()
    )
);
```

```php PHP
use Anthropic\Beta\Agents\BetaManagedAgentsAlwaysAskPolicy;

$tools = [
    BetaManagedAgentsAgentToolset20260401Params::with(
        type: 'agent_toolset_20260401',
        defaultConfig: BetaManagedAgentsAgentToolsetDefaultConfigParams::with(
            permissionPolicy: BetaManagedAgentsAlwaysAllowPolicy::with(type: 'always_allow'),
        ),
        configs: [
            BetaManagedAgentsAgentToolConfigParams::with(
                name: 'bash',
                permissionPolicy: BetaManagedAgentsAlwaysAskPolicy::with(type: 'always_ask'),
            ),
        ],
    ),
];
```

```ruby Ruby
tools = [
  {
    type: "agent_toolset_20260401",
    default_config: {
      permission_policy: {type: "always_allow"}
    },
    configs: [
      {
        name: "bash",
        permission_policy: {type: "always_ask"}
      }
    ]
  }
]
```
</CodeGroup>

## Respond to confirmation requests

When the agent invokes a tool with an `always_ask` policy:

1. The session emits an `agent.tool_use` or `agent.mcp_tool_use` event.
2. The session pauses with a `session.status_idle` event containing `stop_reason: requires_action`. The blocking event IDs are in the `stop_reason.event_ids` array.
3. Send a `user.tool_confirmation` event for each, passing the event ID in the `tool_use_id` parameter. Set `result` to `"allow"` or `"deny"`. Use `deny_message` to explain a denial.
4. Once all blocking events are resolved, the session transitions back to `running`.

Learn more about event handling in the [Session event stream](/docs/en/managed-agents/events-and-streaming) guide.

<CodeGroup defaultLanguage="CLI">
```bash curl
# Allow the tool to execute
curl -fsSL "https://api.anthropic.com/v1/sessions/$SESSION_ID/events" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d '{
    "events": [
      {
        "type": "user.tool_confirmation",
        "tool_use_id": "'$AGENT_TOOL_USE_EVENT_ID'",
        "result": "allow"
      }
    ]
  }'

# Or deny it with an explanation
curl -fsSL "https://api.anthropic.com/v1/sessions/$SESSION_ID/events" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d '{
    "events": [
      {
        "type": "user.tool_confirmation",
        "tool_use_id": "'$MCP_TOOL_USE_EVENT_ID'",
        "result": "deny",
        "deny_message": "Don'\''t create issues in the production project. Use the staging project."
      }
    ]
  }'
```

```bash CLI nocheck
# Allow the tool to execute
ant beta:sessions:events send \
  --session-id "$SESSION_ID" \
  --event "{type: user.tool_confirmation, tool_use_id: $AGENT_TOOL_USE_EVENT_ID, result: allow}"

# Or deny it with an explanation
ant beta:sessions:events send \
  --session-id "$SESSION_ID" \
  --event "{type: user.tool_confirmation, tool_use_id: $MCP_TOOL_USE_EVENT_ID, result: deny,
    deny_message: Don't create issues in the production project. Use the staging project.}"
```

```python Python
# Allow the tool to execute
client.beta.sessions.events.send(
    session.id,
    events=[
        {
            "type": "user.tool_confirmation",
            "tool_use_id": agent_tool_use_event.id,
            "result": "allow",
        },
    ],
)

# Or deny it with an explanation
client.beta.sessions.events.send(
    session.id,
    events=[
        {
            "type": "user.tool_confirmation",
            "tool_use_id": mcp_tool_use_event.id,
            "result": "deny",
            "deny_message": "Don't create issues in the production project. Use the staging project.",
        },
    ],
)
```

```typescript TypeScript
// Allow the tool to execute
await client.beta.sessions.events.send(session.id, {
  events: [
    {
      type: "user.tool_confirmation",
      tool_use_id: agent_tool_use_event.id,
      result: "allow"
    }
  ]
});

// Or deny it with an explanation
await client.beta.sessions.events.send(session.id, {
  events: [
    {
      type: "user.tool_confirmation",
      tool_use_id: mcp_tool_use_event.id,
      result: "deny",
      deny_message: "Don't create issues in the production project. Use the staging project."
    }
  ]
});
```

```csharp C#
// Allow the tool to execute
await client.Beta.Sessions.Events.Send(session.ID, new()
{
    Events =
    [
        new BetaManagedAgentsUserToolConfirmationEventParams
        {
            Type = "user.tool_confirmation",
            ToolUseID = agentToolUseEvent.ID,
            Result = "allow",
        },
    ],
});

// Or deny it with an explanation
await client.Beta.Sessions.Events.Send(session.ID, new()
{
    Events =
    [
        new BetaManagedAgentsUserToolConfirmationEventParams
        {
            Type = "user.tool_confirmation",
            ToolUseID = mcpToolUseEvent.ID,
            Result = "deny",
            DenyMessage = "Don't create issues in the production project. Use the staging project.",
        },
    ],
});
```

```go Go
// Allow the tool to execute
_, err = client.Beta.Sessions.Events.Send(ctx, session.ID, anthropic.BetaSessionEventSendParams{
	Events: []anthropic.SendEventsParamsUnion{{
		OfUserToolConfirmation: &anthropic.BetaManagedAgentsUserToolConfirmationEventParams{
			Type:      anthropic.BetaManagedAgentsUserToolConfirmationEventParamsTypeUserToolConfirmation,
			ToolUseID: agentToolUseEvent.ID,
			Result:    anthropic.BetaManagedAgentsUserToolConfirmationEventParamsResultAllow,
		},
	}},
})
if err != nil {
	panic(err)
}

// Or deny it with an explanation
_, err = client.Beta.Sessions.Events.Send(ctx, session.ID, anthropic.BetaSessionEventSendParams{
	Events: []anthropic.SendEventsParamsUnion{{
		OfUserToolConfirmation: &anthropic.BetaManagedAgentsUserToolConfirmationEventParams{
			Type:        anthropic.BetaManagedAgentsUserToolConfirmationEventParamsTypeUserToolConfirmation,
			ToolUseID:   mcpToolUseEvent.ID,
			Result:      anthropic.BetaManagedAgentsUserToolConfirmationEventParamsResultDeny,
			DenyMessage: anthropic.String("Don't create issues in the production project. Use the staging project."),
		},
	}},
})
if err != nil {
	panic(err)
}
```

```java Java
// Allow the tool to execute
client.beta().sessions().events().send(
    session.id(),
    EventSendParams.builder()
        .addEvent(
            BetaManagedAgentsUserToolConfirmationEventParams.builder()
                .type(BetaManagedAgentsUserToolConfirmationEventParams.Type.USER_TOOL_CONFIRMATION)
                .toolUseId(agentToolUseEvent.id())
                .result(BetaManagedAgentsUserToolConfirmationEventParams.Result.ALLOW)
                .build()
        )
        .build()
);

// Or deny it with an explanation
client.beta().sessions().events().send(
    session.id(),
    EventSendParams.builder()
        .addEvent(
            BetaManagedAgentsUserToolConfirmationEventParams.builder()
                .type(BetaManagedAgentsUserToolConfirmationEventParams.Type.USER_TOOL_CONFIRMATION)
                .toolUseId(mcpToolUseEvent.id())
                .result(BetaManagedAgentsUserToolConfirmationEventParams.Result.DENY)
                .denyMessage("Don't create issues in the production project. Use the staging project.")
                .build()
        )
        .build()
);
```

```php PHP
use Anthropic\Beta\Sessions\Events\ManagedAgentsUserToolConfirmationEventParams;

// Allow the tool to execute
$client->beta->sessions->events->send(
    $session->id,
    events: [
        ManagedAgentsUserToolConfirmationEventParams::with(
            type: 'user.tool_confirmation',
            toolUseID: $agentToolUseEvent->id,
            result: 'allow',
        ),
    ],
);

// Or deny it with an explanation
$client->beta->sessions->events->send(
    $session->id,
    events: [
        ManagedAgentsUserToolConfirmationEventParams::with(
            type: 'user.tool_confirmation',
            toolUseID: $mcpToolUseEvent->id,
            result: 'deny',
            denyMessage: "Don't create issues in the production project. Use the staging project.",
        ),
    ],
);
```

```ruby Ruby
# Allow the tool to execute
client.beta.sessions.events.send_(
  session.id,
  events: [
    {
      type: "user.tool_confirmation",
      tool_use_id: agent_tool_use_event.id,
      result: "allow"
    }
  ]
)

# Or deny it with an explanation
client.beta.sessions.events.send_(
  session.id,
  events: [
    {
      type: "user.tool_confirmation",
      tool_use_id: mcp_tool_use_event.id,
      result: "deny",
      deny_message: "Don't create issues in the production project. Use the staging project."
    }
  ]
)
```
</CodeGroup>

## Custom tools

Permission policies do not apply to custom tools. When the agent invokes a custom tool, your application receives an `agent.custom_tool_use` event and is responsible for deciding whether to execute it before sending back a `user.custom_tool_result`. See [Session event stream](/docs/en/managed-agents/events-and-streaming#handling-custom-tool-calls) for the full flow.