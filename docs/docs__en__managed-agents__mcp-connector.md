# MCP connector

Connect MCP servers to your agents for access to external tools and data sources.

---

Claude Managed Agents supports connecting [Model Context Protocol (MCP)](https://modelcontextprotocol.io) servers to your agents. This gives the agent access to external tools, data sources, and services through a standardized protocol.

MCP configuration is split across two steps:

1. **Agent creation** declares which MCP servers the agent connects to, by name and URL.
2. **Session creation** supplies auth for those servers by referencing a pre-registered [vault](/docs/en/managed-agents/vaults).

This separation keeps secrets out of reusable agent definitions while letting each session authenticate with its own credentials.

<Note>
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
</Note>

## Declare MCP servers on the agent

Specify MCP servers in the `mcp_servers` array when creating an agent. Each server needs a `type`, a unique `name`, and a `url`. No auth tokens are provided at this stage.

The `name` you assign in the MCP server array is used to reference the `mcp_toolset` entries in the tools array.

<CodeGroup defaultLanguage="CLI">
  
````bash
agent_response=$(curl -sS --fail-with-body https://api.anthropic.com/v1/agents \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d @- <<'EOF'
{
  "name": "GitHub Assistant",
  "model": "claude-opus-4-7",
  "mcp_servers": [
    {
      "type": "url",
      "name": "github",
      "url": "https://api.githubcopilot.com/mcp/"
    }
  ],
  "tools": [
    {"type": "agent_toolset_20260401"},
    {"type": "mcp_toolset", "mcp_server_name": "github"}
  ]
}
EOF
)
agent_id=$(jq -r '.id' <<<"$agent_response")
````

  
````bash
AGENT_ID=$(ant beta:agents create \
  --name "GitHub Assistant" \
  --model claude-opus-4-7 \
  --mcp-server '{type: url, name: github, url: "https://api.githubcopilot.com/mcp/"}' \
  --tool '{type: agent_toolset_20260401}' \
  --tool '{type: mcp_toolset, mcp_server_name: github}' \
  --transform id --raw-output)
````

  
````python
agent = client.beta.agents.create(
    name="GitHub Assistant",
    model="claude-opus-4-7",
    mcp_servers=[
        {
            "type": "url",
            "name": "github",
            "url": "https://api.githubcopilot.com/mcp/",
        },
    ],
    tools=[
        {"type": "agent_toolset_20260401"},
        {"type": "mcp_toolset", "mcp_server_name": "github"},
    ],
)
````

  
````typescript
const agent = await client.beta.agents.create({
  name: "GitHub Assistant",
  model: "claude-opus-4-7",
  mcp_servers: [
    {
      type: "url",
      name: "github",
      url: "https://api.githubcopilot.com/mcp/",
    },
  ],
  tools: [
    { type: "agent_toolset_20260401" },
    { type: "mcp_toolset", mcp_server_name: "github" },
  ],
});
````

  
````csharp
var agent = await client.Beta.Agents.Create(new()
{
    Name = "GitHub Assistant",
    Model = BetaManagedAgentsModel.ClaudeOpus4_7,
    McpServers =
    [
        new() { Type = "url", Name = "github", Url = "https://api.githubcopilot.com/mcp/" },
    ],
    Tools =
    [
        new BetaManagedAgentsAgentToolset20260401Params
        {
            Type = "agent_toolset_20260401",
        },
        new BetaManagedAgentsMcpToolsetParams { Type = "mcp_toolset", McpServerName = "github" },
    ],
});
````

  
````go
agent, err := client.Beta.Agents.New(ctx, anthropic.BetaAgentNewParams{
	Name: "GitHub Assistant",
	Model: anthropic.BetaManagedAgentsModelConfigParams{
		ID:   anthropic.BetaManagedAgentsModelClaudeOpus4_7,
		Type: anthropic.BetaManagedAgentsModelConfigParamsTypeModelConfig,
	},
	MCPServers: []anthropic.BetaManagedAgentsUrlmcpServerParams{{
		Type: anthropic.BetaManagedAgentsUrlmcpServerParamsTypeURL,
		Name: "github",
		URL:  "https://api.githubcopilot.com/mcp/",
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
			},
		},
	},
})
if err != nil {
	panic(err)
}
````

  
````java
var agent = client.beta().agents().create(
    AgentCreateParams.builder()
        .name("GitHub Assistant")
        .model(BetaManagedAgentsModel.CLAUDE_OPUS_4_7)
        .addMcpServer(
            BetaManagedAgentsUrlmcpServerParams.builder()
                .type(BetaManagedAgentsUrlmcpServerParams.Type.URL)
                .name("github")
                .url("https://api.githubcopilot.com/mcp/")
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
                .build()
        )
        .build()
);
````

  
````php
$agent = $client->beta->agents->create(
    name: 'GitHub Assistant',
    model: 'claude-opus-4-7',
    mcpServers: [
        BetaManagedAgentsUrlmcpServerParams::with(
            type: 'url',
            name: 'github',
            url: 'https://api.githubcopilot.com/mcp/',
        ),
    ],
    tools: [
        BetaManagedAgentsAgentToolset20260401Params::with(
            type: 'agent_toolset_20260401',
        ),
        BetaManagedAgentsMCPToolsetParams::with(
            type: 'mcp_toolset',
            mcpServerName: 'github',
        ),
    ],
);
````

  
````ruby
agent = client.beta.agents.create(
  name: "GitHub Assistant",
  model: "claude-opus-4-7",
  mcp_servers: [
    {
      type: "url",
      name: "github",
      url: "https://api.githubcopilot.com/mcp/"
    }
  ],
  tools: [
    {type: "agent_toolset_20260401"},
    {type: "mcp_toolset", mcp_server_name: "github"}
  ]
)
````

</CodeGroup>

<Tip>
The MCP toolset defaults to a permission policy of `always_ask`, which requires user approval before each tool call. See [permission policies](/docs/en/managed-agents/permission-policies) to configure this behavior.
</Tip>

## Provide auth at session creation

When starting a session, pass `vault_ids` to provide credentials for your MCP servers. Vaults are collections of credentials that you register once and reference by ID. See [Authenticate with vaults](/docs/en/managed-agents/vaults) for how to create vaults and manage credentials.

<CodeGroup>
  
````bash
session_response=$(curl -sS --fail-with-body https://api.anthropic.com/v1/sessions \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d @- <<EOF
{
  "agent": "$agent_id",
  "environment_id": "$environment_id",
  "vault_ids": ["$vault_id"]
}
EOF
)
session_id=$(jq -r '.id' <<<"$session_response")
````

  
````bash
SESSION_ID=$(ant beta:sessions create \
  --agent "$AGENT_ID" \
  --environment-id "$ENVIRONMENT_ID" \
  --vault-id "$VAULT_ID" \
  --transform id --raw-output)
````

  
````python
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    vault_ids=[vault.id],
)
````

  
````typescript
const session = await client.beta.sessions.create({
  agent: agent.id,
  environment_id: environment.id,
  vault_ids: [vault.id],
});
````

  
````csharp
var session = await client.Beta.Sessions.Create(new()
{
    Agent = agent.ID,
    EnvironmentID = environment.ID,
    VaultIds = [vault.ID],
});
````

  
````go
session, err := client.Beta.Sessions.New(ctx, anthropic.BetaSessionNewParams{
	Agent:         anthropic.BetaSessionNewParamsAgentUnion{OfString: anthropic.String(agent.ID)},
	EnvironmentID: environment.ID,
	VaultIDs:      []string{vault.ID},
})
if err != nil {
	panic(err)
}
````

  
````java
var session = client.beta().sessions().create(
    SessionCreateParams.builder()
        .agent(agent.id())
        .environmentId(environment.id())
        .addVaultId(vault.id())
        .build()
);
````

  
````php
$session = $client->beta->sessions->create(
    agent: $agent->id,
    environmentID: $environment->id,
    vaultIDs: [$vault->id],
);
````

  
````ruby
session = client.beta.sessions.create(
  agent: agent.id,
  environment_id: environment.id,
  vault_ids: [vault.id]
)
````

</CodeGroup>

If the authorization credentials supplied in the vault are invalid, session creation will succeed and interaction is still possible. A `session.error` event is emitted describing the MCP auth failure. You can decide whether to block further interactions on this error, trigger a credential update, or allow the session to continue without the MCP. Authentication retries will happen on the following `session.status_idle` to `session.status_running` transition. See [Session event stream](/docs/en/managed-agents/events-and-streaming) for details on consuming `session.error` and other events.

## Supported MCP server types

Claude Managed Agents connects to [remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers) that expose an HTTP endpoint. The server must support the MCP protocol's streamable HTTP transport.

For more information on MCP and building MCP servers, see the [MCP documentation](https://modelcontextprotocol.io).