# Start a session

Create a session to run your agent and begin executing tasks.

---

A session is an agent instance within an environment. Each session references an [agent](/docs/en/managed-agents/agent-setup) and an [environment](/docs/en/managed-agents/environments) (both created separately), and maintains conversation history across multiple interactions. Sessions follow a two-step lifecycle: first [create the session](#creating-a-session) to provision its container, then [send a user event](#starting-the-session) to start work.

<Note>
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
</Note>

## Creating a session

A session requires an `agent` ID and an `environment` ID. Agents are versioned resources; passing in the `agent` ID as a string starts the session with the latest agent version.

<CodeGroup defaultLanguage="CLI">
  
````bash
session=$(curl -fsSL https://api.anthropic.com/v1/sessions \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d @- <<EOF
{
  "agent": "$AGENT_ID",
  "environment_id": "$ENVIRONMENT_ID"
}
EOF
)
SESSION_ID=$(jq -r '.id' <<< "$session")
````

  
````bash
ant beta:sessions create \
  --agent "$AGENT_ID" \
  --environment-id "$ENVIRONMENT_ID"
````

  
````python
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
)
````

  
````typescript
const session = await client.beta.sessions.create({
  agent: agent.id,
  environment_id: environment.id
});
````

  
````csharp
var session = await client.Beta.Sessions.Create(new()
{
    Agent = agent.ID,
    EnvironmentID = environment.ID,
});
````

  
````go
session, err := client.Beta.Sessions.New(ctx, anthropic.BetaSessionNewParams{
	Agent: anthropic.BetaSessionNewParamsAgentUnion{
		OfString: anthropic.String(agent.ID),
	},
	EnvironmentID: environment.ID,
})
if err != nil {
	panic(err)
}
````

  
````java
var session = client.beta().sessions().create(SessionCreateParams.builder()
    .agent(agent.id())
    .environmentId(environment.id())
    .build());
````

  
````php
$session = $client->beta->sessions->create(
    agent: $agent->id,
    environmentID: $environment->id,
);
````

  
````ruby
session = client.beta.sessions.create(
  agent: agent.id,
  environment_id: environment.id
)
````

</CodeGroup>

To pin a session to a specific agent version, pass an object. This lets you control exactly which version runs and stage rollouts of new versions independently.

<CodeGroup defaultLanguage="CLI">
  
````bash
pinned_session=$(curl -fsSL https://api.anthropic.com/v1/sessions \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d @- <<EOF
{
  "agent": {"type": "agent", "id": "$AGENT_ID", "version": 1},
  "environment_id": "$ENVIRONMENT_ID"
}
EOF
)
PINNED_SESSION_ID=$(jq -r '.id' <<< "$pinned_session")
````

  
````bash
ant beta:sessions create <<YAML
agent:
  type: agent
  id: $AGENT_ID
  version: 1
environment_id: $ENVIRONMENT_ID
YAML
````

  
````python
pinned_session = client.beta.sessions.create(
    agent={"type": "agent", "id": agent.id, "version": 1},
    environment_id=environment.id,
)
````

  
````typescript
const pinnedSession = await client.beta.sessions.create({
  agent: { type: "agent", id: agent.id, version: 1 },
  environment_id: environment.id
});
````

  
````csharp
var pinnedSession = await client.Beta.Sessions.Create(new()
{
    Agent = new BetaManagedAgentsAgentParams
    {
        Type = Anthropic.Models.Beta.Sessions.Type.Agent,
        ID = agent.ID,
        Version = 1,
    },
    EnvironmentID = environment.ID,
});
````

  
````go
pinnedSession, err := client.Beta.Sessions.New(ctx, anthropic.BetaSessionNewParams{
	Agent: anthropic.BetaSessionNewParamsAgentUnion{
		OfBetaManagedAgentsAgents: &anthropic.BetaManagedAgentsAgentParams{
			Type:    anthropic.BetaManagedAgentsAgentParamsTypeAgent,
			ID:      agent.ID,
			Version: anthropic.Int(1),
		},
	},
	EnvironmentID: environment.ID,
})
if err != nil {
	panic(err)
}
````

  
````java
var pinnedSession = client.beta().sessions().create(SessionCreateParams.builder()
    .agent(BetaManagedAgentsAgentParams.builder()
        .type(BetaManagedAgentsAgentParams.Type.AGENT)
        .id(agent.id())
        .version(1)
        .build())
    .environmentId(environment.id())
    .build());
````

  
````php
$pinnedSession = $client->beta->sessions->create(
    agent: ['type' => 'agent', 'id' => $agent->id, 'version' => 1],
    environmentID: $environment->id,
);
````

  
````ruby
pinned_session = client.beta.sessions.create(
  agent: {type: :agent, id: agent.id, version: 1},
  environment_id: environment.id
)
````

</CodeGroup>

<Tip>
The agent defines how Claude behaves within the session, including the model, system prompt, tools, and MCP servers. See [Define your agent](/docs/en/managed-agents/agent-setup) for details.
</Tip>

## MCP authentication through vaults

If your agent uses MCP tools that require authentication, pass `vault_ids` at session creation to reference a vault containing stored OAuth credentials. Anthropic manages token refresh on your behalf. See [Authenticate with vaults](/docs/en/managed-agents/vaults) for how to create vaults and register credentials.

<CodeGroup defaultLanguage="CLI">
  
````bash
vault_session=$(curl -fsSL https://api.anthropic.com/v1/sessions \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d @- <<EOF
{
  "agent": "$AGENT_ID",
  "environment_id": "$ENVIRONMENT_ID",
  "vault_ids": ["$VAULT_ID"]
}
EOF
)
VAULT_SESSION_ID=$(jq -r '.id' <<< "$vault_session")
````

  
````bash
ant beta:sessions create <<YAML
agent: $AGENT_ID
environment_id: $ENVIRONMENT_ID
vault_ids:
  - $VAULT_ID
YAML
````

  
````python
vault_session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    vault_ids=[vault.id],
)
````

  
````typescript
const vaultSession = await client.beta.sessions.create({
  agent: agent.id,
  environment_id: environment.id,
  vault_ids: [vault.id]
});
````

  
````csharp
var vaultSession = await client.Beta.Sessions.Create(new()
{
    Agent = agent.ID,
    EnvironmentID = environment.ID,
    VaultIds = [vault.ID],
});
````

  
````go
vaultSession, err := client.Beta.Sessions.New(ctx, anthropic.BetaSessionNewParams{
	Agent: anthropic.BetaSessionNewParamsAgentUnion{
		OfString: anthropic.String(agent.ID),
	},
	EnvironmentID: environment.ID,
	VaultIDs:      []string{vault.ID},
})
if err != nil {
	panic(err)
}
````

  
````java
var vaultSession = client.beta().sessions().create(SessionCreateParams.builder()
    .agent(agent.id())
    .environmentId(environment.id())
    .addVaultId(vault.id())
    .build());
````

  
````php
$vaultSession = $client->beta->sessions->create(
    agent: $agent->id,
    environmentID: $environment->id,
    vaultIDs: [$vault->id],
);
````

  
````ruby
vault_session = client.beta.sessions.create(
  agent: agent.id,
  environment_id: environment.id,
  vault_ids: [vault.id]
)
````

</CodeGroup>

## Starting the session

Creating a session provisions the environment's container but does not start any work. To delegate a task, send events to the session using a [user event](/docs/en/managed-agents/events-and-streaming#event-types). The session acts as a state machine that tracks progress while events drive the actual execution.

<CodeGroup defaultLanguage="CLI">
  
````bash
curl -fsSL "https://api.anthropic.com/v1/sessions/$SESSION_ID/events" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d @- <<'EOF'
{
  "events": [
    {
      "type": "user.message",
      "content": [{"type": "text", "text": "List the files in the working directory."}]
    }
  ]
}
EOF
````

  
````bash
ant beta:sessions:events send \
  --session-id "$SESSION_ID" <<'YAML'
events:
  - type: user.message
    content:
      - type: text
        text: List the files in the working directory.
YAML
````

  
````python
client.beta.sessions.events.send(
    session.id,
    events=[
        {
            "type": "user.message",
            "content": [
                {"type": "text", "text": "List the files in the working directory."}
            ],
        },
    ],
)
````

  
````typescript
await client.beta.sessions.events.send(session.id, {
  events: [
    {
      type: "user.message",
      content: [{ type: "text", text: "List the files in the working directory." }]
    }
  ]
});
````

  
````csharp
await client.Beta.Sessions.Events.Send(session.ID, new()
{
    Events =
    [
        new BetaManagedAgentsUserMessageEventParams
        {
            Type = BetaManagedAgentsUserMessageEventParamsType.UserMessage,
            Content =
            [
                new BetaManagedAgentsTextBlock
                {
                    Type = BetaManagedAgentsTextBlockType.Text,
                    Text = "List the files in the working directory.",
                },
            ],
        },
    ],
});
````

  
````go
if _, err := client.Beta.Sessions.Events.Send(ctx, session.ID, anthropic.BetaSessionEventSendParams{
	Events: []anthropic.BetaManagedAgentsEventParamsUnion{{
		OfUserMessage: &anthropic.BetaManagedAgentsUserMessageEventParams{
			Type: anthropic.BetaManagedAgentsUserMessageEventParamsTypeUserMessage,
			Content: []anthropic.BetaManagedAgentsUserMessageEventParamsContentUnion{{
				OfText: &anthropic.BetaManagedAgentsTextBlockParam{
					Type: anthropic.BetaManagedAgentsTextBlockTypeText,
					Text: "List the files in the working directory.",
				},
			}},
		},
	}},
}); err != nil {
	panic(err)
}
````

  
````java
client.beta().sessions().events().send(
    session.id(),
    EventSendParams.builder()
        .addEvent(BetaManagedAgentsUserMessageEventParams.builder()
            .type(BetaManagedAgentsUserMessageEventParams.Type.USER_MESSAGE)
            .addTextContent("List the files in the working directory.")
            .build())
        .build());
````

  
````php
$client->beta->sessions->events->send(
    $session->id,
    events: [
        [
            'type' => 'user.message',
            'content' => [['type' => 'text', 'text' => 'List the files in the working directory.']],
        ],
    ],
);
````

  
````ruby
client.beta.sessions.events.send_(
  session.id,
  events: [
    {
      type: :"user.message",
      content: [{type: :text, text: "List the files in the working directory."}]
    }
  ]
)
````

</CodeGroup>

See [Session event stream](/docs/en/managed-agents/events-and-streaming) for how to stream the agent's responses and handle tool confirmations.

## Session statuses

Sessions progress through these statuses:

| Status | Description |
|--------|-------------|
| `idle` | Agent is waiting for input, including user messages or tool confirmations. Sessions start in `idle`. |
| `running` | Agent is actively executing. |
| `rescheduling` | Transient error occurred, retrying automatically. |
| `terminated` | Session has ended due to an unrecoverable error. |

## Other session operations

### Updating the agent configuration

You can update a session's `agent.tools` and `agent.mcp_servers`, including permission policies, mid-session without creating a new agent version. Updates are session-local and do not propagate back to the underlying agent.

The semantics of an update are full replacement: the provided array is the new value. To preserve existing entries, `GET` the session, modify the array, and `POST` it back.

The session must be `idle` to update the agent. [Interrupt](/docs/en/managed-agents/events-and-streaming#integrating-events) the session if you need to update the agent while it's running.

<CodeGroup defaultLanguage="CLI">
  
````bash
curl -sS --fail-with-body "https://api.anthropic.com/v1/sessions/$SESSION_ID" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d @- <<EOF
{
  "agent": {
    "tools": [
      {"type": "agent_toolset_20260401"},
      {"type": "mcp_toolset", "mcp_server_name": "linear"}
    ],
    "mcp_servers": [
      {"type": "url", "name": "linear", "url": "https://mcp.linear.app/sse"}
    ]
  }
}
EOF
````

  
````bash
ant beta:sessions update --session-id "$SESSION_ID" <<'YAML'
agent:
  tools:
    - type: agent_toolset_20260401
    - type: mcp_toolset
      mcp_server_name: linear
  mcp_servers:
    - type: url
      name: linear
      url: https://mcp.linear.app/sse
YAML
````

  
````python
client.beta.sessions.update(
    session.id,
    agent={
        "tools": [
            {"type": "agent_toolset_20260401"},
            {"type": "mcp_toolset", "mcp_server_name": "linear"},
        ],
        "mcp_servers": [
            {"type": "url", "name": "linear", "url": "https://mcp.linear.app/sse"}
        ],
    },
)
````

  
````typescript
await client.beta.sessions.update(session.id, {
  agent: {
    tools: [
      { type: "agent_toolset_20260401" },
      { type: "mcp_toolset", mcp_server_name: "linear" }
    ],
    mcp_servers: [{ type: "url", name: "linear", url: "https://mcp.linear.app/sse" }]
  }
});
````

  
````csharp
using Anthropic.Models.Beta.Agents;

await client.Beta.Sessions.Update(session.ID, new()
{
    Agent = new()
    {
        Tools =
        [
            new BetaManagedAgentsAgentToolset20260401Params
            {
                Type = BetaManagedAgentsAgentToolset20260401ParamsType.AgentToolset20260401,
            },
            new BetaManagedAgentsMcpToolsetParams
            {
                Type = BetaManagedAgentsMcpToolsetParamsType.McpToolset,
                McpServerName = "linear",
            },
        ],
        McpServers =
        [
            new()
            {
                Type = BetaManagedAgentsUrlMcpServerParamsType.Url,
                Name = "linear",
                Url = "https://mcp.linear.app/sse",
            },
        ],
    },
});
````

  
````go
_, err = client.Beta.Sessions.Update(ctx, session.ID, anthropic.BetaSessionUpdateParams{
	Agent: anthropic.BetaManagedAgentsSessionAgentUpdateParam{
		Tools: []anthropic.BetaManagedAgentsSessionAgentUpdateToolUnionParam{
			{
				OfAgentToolset20260401: &anthropic.BetaManagedAgentsAgentToolset20260401Params{
					Type: anthropic.BetaManagedAgentsAgentToolset20260401ParamsTypeAgentToolset20260401,
				},
			},
			{
				OfMCPToolset: &anthropic.BetaManagedAgentsMCPToolsetParams{
					Type:          anthropic.BetaManagedAgentsMCPToolsetParamsTypeMCPToolset,
					MCPServerName: "linear",
				},
			},
		},
		MCPServers: []anthropic.BetaManagedAgentsURLMCPServerParams{
			{
				Type: anthropic.BetaManagedAgentsURLMCPServerParamsTypeURL,
				Name: "linear",
				URL:  "https://mcp.linear.app/sse",
			},
		},
	},
})
if err != nil {
	panic(err)
}
````

  
````java
client.beta().sessions().update(
    session.id(),
    SessionUpdateParams.builder()
        .agent(BetaManagedAgentsSessionAgentUpdate.builder()
            .addTool(BetaManagedAgentsAgentToolset20260401Params.builder()
                .type(BetaManagedAgentsAgentToolset20260401Params.Type.AGENT_TOOLSET_20260401)
                .build())
            .addTool(BetaManagedAgentsMcpToolsetParams.builder()
                .type(BetaManagedAgentsMcpToolsetParams.Type.MCP_TOOLSET)
                .mcpServerName("linear")
                .build())
            .addMcpServer(BetaManagedAgentsUrlMcpServerParams.builder()
                .type(BetaManagedAgentsUrlMcpServerParams.Type.URL)
                .name("linear")
                .url("https://mcp.linear.app/sse")
                .build())
            .build())
        .build()
);
````

  
````php
$client->beta->sessions->update(
    $session->id,
    agent: BetaManagedAgentsSessionAgentUpdate::with(
        tools: [
            BetaManagedAgentsAgentToolset20260401Params::with(type: 'agent_toolset_20260401'),
            BetaManagedAgentsMCPToolsetParams::with(mcpServerName: 'linear', type: 'mcp_toolset'),
        ],
        mcpServers: [
            BetaManagedAgentsURLMCPServerParams::with(
                name: 'linear',
                type: 'url',
                url: 'https://mcp.linear.app/sse',
            ),
        ],
    ),
);
````

  
````ruby
client.beta.sessions.update(
  session.id,
  agent: {
    tools: [
      {type: :agent_toolset_20260401},
      {type: :mcp_toolset, mcp_server_name: "linear"}
    ],
    mcp_servers: [
      {type: :url, name: "linear", url: "https://mcp.linear.app/sse"}
    ]
  }
)
````

</CodeGroup>

### Retrieving a session

<CodeGroup defaultLanguage="CLI">
  
````bash
retrieved=$(curl -fsSL "https://api.anthropic.com/v1/sessions/$SESSION_ID" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01")
echo "Status: $(jq -r '.status' <<< "$retrieved")"
````

  
````bash
ant beta:sessions retrieve --session-id "$SESSION_ID"
````

  
````python
retrieved = client.beta.sessions.retrieve(session.id)
print(f"Status: {retrieved.status}")
````

  
````typescript
const retrieved = await client.beta.sessions.retrieve(session.id);
console.log(`Status: ${retrieved.status}`);
````

  
````csharp
var retrieved = await client.Beta.Sessions.Retrieve(session.ID);
Console.WriteLine($"Status: {retrieved.Status.Raw()}");
````

  
````go
retrieved, err := client.Beta.Sessions.Get(ctx, session.ID, anthropic.BetaSessionGetParams{})
if err != nil {
	panic(err)
}
fmt.Printf("Status: %s\n", retrieved.Status)
````

  
````java
var retrieved = client.beta().sessions().retrieve(session.id());
IO.println("Status: " + retrieved.status());
````

  
````php
$retrieved = $client->beta->sessions->retrieve($session->id);
echo "Status: {$retrieved->status}\n";
````

  
````ruby
retrieved = client.beta.sessions.retrieve(session.id)
puts "Status: #{retrieved.status}"
````

</CodeGroup>

### Listing sessions

<CodeGroup defaultLanguage="CLI">
  
````bash
curl -fsSL "https://api.anthropic.com/v1/sessions?agent_id=$AGENT_ID" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  | jq -r '.data[] | "\(.id): \(.status)"'
````

  
````bash
ant beta:sessions list --agent-id "$AGENT_ID"
````

  
````python
for listed_session in client.beta.sessions.list(agent_id=agent.id):
    print(f"{listed_session.id}: {listed_session.status}")
````

  
````typescript
for await (const session of client.beta.sessions.list({ agent_id: agent.id })) {
  console.log(`${session.id}: ${session.status}`);
}
````

  
````csharp
var sessions = await client.Beta.Sessions.List(new SessionListParams { AgentID = agent.ID });
await foreach (var listedSession in sessions.Paginate())
{
    Console.WriteLine($"{listedSession.ID}: {listedSession.Status.Raw()}");
}
````

  
````go
page := client.Beta.Sessions.ListAutoPaging(ctx, anthropic.BetaSessionListParams{
	AgentID: anthropic.String(agent.ID),
})
for page.Next() {
	session := page.Current()
	fmt.Printf("%s: %s\n", session.ID, session.Status)
}
if err := page.Err(); err != nil {
	panic(err)
}
````

  
````java
var params = SessionListParams.builder().agentId(agent.id()).build();
for (var listed : client.beta().sessions().list(params).autoPager()) {
    IO.println(listed.id() + ": " + listed.status());
}
````

  
````php
foreach ($client->beta->sessions->list(agentID: $agent->id)->pagingEachItem() as $listedSession) {
    echo "{$listedSession->id}: {$listedSession->status}\n";
}
````

  
````ruby
client.beta.sessions.list(agent_id: agent.id).auto_paging_each do |session|
  puts "#{session.id}: #{session.status}"
end
````

</CodeGroup>

### Archiving a session

Archive a session to prevent new events from being sent while preserving its history:

<CodeGroup defaultLanguage="CLI">
  
````bash
curl -fsSL -X POST "https://api.anthropic.com/v1/sessions/$SESSION_ID/archive" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01"
````

  
````bash
ant beta:sessions archive \
  --session-id "$SESSION_ID"
````

  
````python
client.beta.sessions.archive(session.id)
````

  
````typescript
await client.beta.sessions.archive(session.id);
````

  
````csharp
await client.Beta.Sessions.Archive(session.ID);
````

  
````go
_, err = client.Beta.Sessions.Archive(ctx, session.ID, anthropic.BetaSessionArchiveParams{})
if err != nil {
	panic(err)
}
````

  
````java
client.beta().sessions().archive(session.id());
````

  
````php
$client->beta->sessions->archive($session->id);
````

  
````ruby
client.beta.sessions.archive(session.id)
````

</CodeGroup>

### Deleting a session

Delete a session to permanently remove its record, events, and associated container. A `running` session cannot be deleted; send an [interrupt event](/docs/en/managed-agents/events-and-streaming#event-types) if you need to delete it immediately.

Files, memory stores, vaults, skills, environments, and agents are independent resources and are not affected by session deletion.

<CodeGroup defaultLanguage="CLI">
  
````bash
curl -fsSL -X DELETE "https://api.anthropic.com/v1/sessions/$SESSION_ID" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01"
````

  
````bash
ant beta:sessions delete \
  --session-id "$SESSION_ID"
````

  
````python
client.beta.sessions.delete(session.id)
````

  
````typescript
await client.beta.sessions.delete(session.id);
````

  
````csharp
await client.Beta.Sessions.Delete(session.ID);
````

  
````go
_, err = client.Beta.Sessions.Delete(ctx, session.ID, anthropic.BetaSessionDeleteParams{})
if err != nil {
	panic(err)
}
````

  
````java
client.beta().sessions().delete(session.id());
````

  
````php
$client->beta->sessions->delete($session->id);
````

  
````ruby
client.beta.sessions.delete(session.id)
````

</CodeGroup>