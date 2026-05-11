# Define your agent

Create a reusable, versioned agent configuration.

---

An agent is a reusable, versioned configuration that defines persona and capabilities. It bundles the model, system prompt, tools, MCP servers, and skills that shape how Claude behaves during a session.

Create the agent once as a reusable resource and reference it by ID each time you [start a session](/docs/en/managed-agents/sessions). Agents are versioned and easier to manage across many sessions.

<Note>
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
</Note>

## Agent configuration fields

| Field | Description |
| --- | --- |
| `name` | Required. A human-readable name for the agent. |
| `model` | Required. The Claude [model](/docs/en/about-claude/models/overview) that powers the agent. All Claude 4.5 and later models are supported. |
| `system` | A [system prompt](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role) that defines the agent's behavior and persona. The system prompt is distinct from [user messages](/docs/en/managed-agents/events-and-streaming#user-events), which should describe the work to be done. |
| `tools` | The tools available to the agent. Combines [pre-built agent tools](/docs/en/managed-agents/tools), [MCP tools](/docs/en/managed-agents/mcp-connector), and [custom tools](/docs/en/managed-agents/tools#custom-tools). |
| `mcp_servers` | MCP servers that provide standardized third-party capabilities. |
| `skills` | [Skills](/docs/en/managed-agents/skills) that supply domain-specific context with progressive disclosure. |
| `multiagent` | A coordinator declaration listing the agents this agent can delegate to. See [Multiagent sessions](/docs/en/managed-agents/multi-agent). |
| `description` | A description of what the agent does. |
| `metadata` | Arbitrary key-value pairs for your own tracking. |

## Create an agent

The following example defines a coding agent that uses Claude Opus 4.7 with access to the pre-built agent toolset. The toolset lets the agent write code, read files, search the web, and more. See the [agent tools reference](/docs/en/managed-agents/tools) for the full list of supported tools.

<CodeGroup defaultLanguage="CLI">
  
````bash
agent=$(curl -fsSL https://api.anthropic.com/v1/agents \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d '{
    "name": "Coding Assistant",
    "model": "claude-opus-4-7",
    "system": "You are a helpful coding agent.",
    "tools": [{"type": "agent_toolset_20260401"}]
  }')

AGENT_ID=$(jq -r '.id' <<< "$agent")
AGENT_VERSION=$(jq -r '.version' <<< "$agent")
````

  
````bash
ant beta:agents create \
  --name "Coding Assistant" \
  --model '{id: claude-opus-4-7}' \
  --system "You are a helpful coding agent." \
  --tool '{type: agent_toolset_20260401}'
````

  
````python
agent = client.beta.agents.create(
    name="Coding Assistant",
    model="claude-opus-4-7",
    system="You are a helpful coding agent.",
    tools=[
        {"type": "agent_toolset_20260401"},
    ],
)
````

  
````typescript
const agent = await client.beta.agents.create({
  name: "Coding Assistant",
  model: "claude-opus-4-7",
  system: "You are a helpful coding agent.",
  tools: [{ type: "agent_toolset_20260401" }],
});
````

  
````csharp
var agent = await client.Beta.Agents.Create(new()
{
    Name = "Coding Assistant",
    Model = new("claude-opus-4-7"),
    System = "You are a helpful coding agent.",
    Tools =
    [
        new BetaManagedAgentsAgentToolset20260401Params
        {
            Type = "agent_toolset_20260401",
        },
    ],
});
````

  
````go
agent, err := client.Beta.Agents.New(ctx, anthropic.BetaAgentNewParams{
	Name: "Coding Assistant",
	Model: anthropic.BetaManagedAgentsModelConfigParams{
		ID:   "claude-opus-4-7",
		Type: anthropic.BetaManagedAgentsModelConfigParamsTypeModelConfig,
	},
	System: anthropic.String("You are a helpful coding agent."),
	Tools: []anthropic.BetaAgentNewParamsToolUnion{{
		OfAgentToolset20260401: &anthropic.BetaManagedAgentsAgentToolset20260401Params{
			Type: anthropic.BetaManagedAgentsAgentToolset20260401ParamsTypeAgentToolset20260401,
			},
	}},
})
if err != nil {
	panic(err)
}
````

  
````java
var agent = client.beta().agents().create(
    AgentCreateParams.builder()
        .name("Coding Assistant")
        .model(BetaManagedAgentsModel.CLAUDE_OPUS_4_7)
        .system("You are a helpful coding agent.")
        .addTool(
            BetaManagedAgentsAgentToolset20260401Params.builder()
                .type(BetaManagedAgentsAgentToolset20260401Params.Type.AGENT_TOOLSET_20260401)
                .build()
        )
        .build()
);
````

  
````php
$agent = $client->beta->agents->create(
    name: 'Coding Assistant',
    model: 'claude-opus-4-7',
    system: 'You are a helpful coding agent.',
    tools: [
        BetaManagedAgentsAgentToolset20260401Params::with(
            type: 'agent_toolset_20260401',
        ),
    ],
);
````

  
````ruby
agent = client.beta.agents.create(
  name: "Coding Assistant",
  model: "claude-opus-4-7",
  system_: "You are a helpful coding agent.",
  tools: [{type: "agent_toolset_20260401"}]
)
````

</CodeGroup>

<Tip>
To use Claude Opus 4.6 with [fast mode](/docs/en/build-with-claude/fast-mode), pass `model` as an object: `{"id": "claude-opus-4-6", "speed": "fast"}`.
</Tip>

The response echoes your configuration and adds `id`, `type`, `version`, `created_at`, `updated_at`, and `archived_at` fields. The `version` starts at 1 and increments each time an update changes the agent.

```json
{
  "id": "agent_01HqR2k7vXbZ9mNpL3wYcT8f",
  "type": "agent",
  "name": "Coding Assistant",
  "model": {
    "id": "claude-opus-4-7",
    "speed": "standard"
  },
  "system": "You are a helpful coding agent.",
  "description": null,
  "tools": [
    {
      "type": "agent_toolset_20260401",
      "default_config": {
        "permission_policy": { "type": "always_allow" }
      }
    }
  ],
  "skills": [],
  "mcp_servers": [],
  "metadata": {},
  "version": 1,
  "created_at": "2026-04-03T18:24:10.412Z",
  "updated_at": "2026-04-03T18:24:10.412Z",
  "archived_at": null
}
```

## Update an agent

Updating an agent generates a new version when the configuration changes. Pass the current `version` to ensure you're updating from a known state.

<CodeGroup defaultLanguage="CLI">
  
````bash
updated_agent=$(curl -fsSL "https://api.anthropic.com/v1/agents/$AGENT_ID" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d @- <<EOF
{
  "version": $AGENT_VERSION,
  "system": "You are a helpful coding agent. Always write tests."
}
EOF
)

echo "New version: $(jq -r '.version' <<< "$updated_agent")"
````

  
````bash
ant beta:agents update \
  --agent-id "$AGENT_ID" \
  --version "$AGENT_VERSION" \
  --system "You are a helpful coding agent. Always write tests."
````

  
````python
updated_agent = client.beta.agents.update(
    agent.id,
    version=agent.version,
    system="You are a helpful coding agent. Always write tests.",
)

print(f"New version: {updated_agent.version}")
````

  
````typescript
const updatedAgent = await client.beta.agents.update(agent.id, {
  version: agent.version,
  system: "You are a helpful coding agent. Always write tests.",
});

console.log(`New version: ${updatedAgent.version}`);
````

  
````csharp
var updatedAgent = await client.Beta.Agents.Update(agent.ID, new()
{
    Version = agent.Version,
    System = "You are a helpful coding agent. Always write tests.",
});

Console.WriteLine($"New version: {updatedAgent.Version}");
````

  
````go
updatedAgent, err := client.Beta.Agents.Update(ctx, agent.ID, anthropic.BetaAgentUpdateParams{
	Version: agent.Version,
	System:  anthropic.String("You are a helpful coding agent. Always write tests."),
})
if err != nil {
	panic(err)
}

fmt.Printf("New version: %d\n", updatedAgent.Version)
````

  
````java
var updatedAgent = client.beta().agents().update(
    agent.id(),
    AgentUpdateParams.builder()
        .version(agent.version())
        .system("You are a helpful coding agent. Always write tests.")
        .build()
);

IO.println("New version: " + updatedAgent.version());
````

  
````php
$updatedAgent = $client->beta->agents->update(
    $agent->id,
    version: $agent->version,
    system: 'You are a helpful coding agent. Always write tests.',
);

echo "New version: {$updatedAgent->version}\n";
````

  
````ruby
updated_agent = client.beta.agents.update(
  agent.id,
  version: agent.version,
  system_: "You are a helpful coding agent. Always write tests."
)

puts "New version: #{updated_agent.version}"
````

</CodeGroup>

### Update semantics

- **Omitted fields are preserved.** You only need to include the fields you want to change.

- **Scalar fields** (`model`, `system`, `name`, `description`) are replaced with the new value. `system` and `description` can be cleared by passing `null`. `model` and `name` are mandatory and cannot be cleared.

- **Array fields** (`tools`, `mcp_servers`, `skills`) are fully replaced by the new array. To clear an array field entirely, pass `null` or an empty array.

- **`multiagent`** is replaced as a whole, including its `agents` roster. Pass `null` to clear it.

- **Metadata** is merged at the key level. Keys you provide are added or updated. Keys you omit are preserved. To delete a specific key, set its value to an empty string.

- **No-op detection.** If the update produces no change relative to the current version, no new version is created and the existing version is returned.

## Agent lifecycle

| Operation | Behavior |
| --- | --- |
| **Update** | Generates a new agent version when the configuration changes. |
| **List versions** | Returns the full version history so you can track changes over time. |
| **Archive** | Makes the agent read-only. New sessions cannot reference it, but existing sessions continue to run. |

### List versions

Fetch the full version history to track how an agent has changed over time.

<CodeGroup defaultLanguage="CLI">
  
````bash
curl -fsSL "https://api.anthropic.com/v1/agents/$AGENT_ID/versions" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  | jq -r '.data[] | "Version \(.version): \(.updated_at)"'
````

  
````bash
ant beta:agents:versions list --agent-id "$AGENT_ID"
````

  
````python
for version in client.beta.agents.versions.list(agent.id):
    print(f"Version {version.version}: {version.updated_at.isoformat()}")
````

  
````typescript
for await (const version of client.beta.agents.versions.list(agent.id)) {
  console.log(`Version ${version.version}: ${version.updated_at}`);
}
````

  
````csharp
var versions = await client.Beta.Agents.Versions.List(agent.ID);
await foreach (var version in versions.Paginate())
{
    Console.WriteLine($"Version {version.Version}: {version.UpdatedAt:O}");
}
````

  
````go
iter := client.Beta.Agents.Versions.ListAutoPaging(ctx, agent.ID, anthropic.BetaAgentVersionListParams{})
for iter.Next() {
	version := iter.Current()
	fmt.Printf("Version %d: %s\n", version.Version, version.UpdatedAt.Format(time.RFC3339))
}
if err := iter.Err(); err != nil {
	panic(err)
}
````

  
````java
for (var version : client.beta().agents().versions().list(agent.id()).autoPager()) {
    IO.println("Version " + version.version() + ": " + version.updatedAt());
}
````

  
````php
foreach ($client->beta->agents->versions->list($agent->id)->pagingEachItem() as $version) {
    echo "Version {$version->version}: {$version->updatedAt->format(DateTimeInterface::ATOM)}\n";
}
````

  
````ruby
client.beta.agents.versions.list(agent.id).auto_paging_each do
  puts "Version #{it.version}: #{it.updated_at.iso8601}"
end
````

</CodeGroup>

### Archive an agent

Archiving makes the agent read-only. Existing sessions continue to run, but new sessions cannot reference the agent. The response sets `archived_at` to the archive timestamp.

<CodeGroup defaultLanguage="CLI">
  
````bash
archived=$(curl -fsSL -X POST "https://api.anthropic.com/v1/agents/$AGENT_ID/archive" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01")

echo "Archived at: $(jq -r '.archived_at' <<< "$archived")"
````

  
````bash
ant beta:agents archive --agent-id "$AGENT_ID"
````

  
````python
archived = client.beta.agents.archive(agent.id)

print(f"Archived at: {archived.archived_at.isoformat()}")
````

  
````typescript
const archived = await client.beta.agents.archive(agent.id);
console.log(`Archived at: ${archived.archived_at}`);
````

  
````csharp
var archived = await client.Beta.Agents.Archive(agent.ID);
Console.WriteLine($"Archived at: {archived.ArchivedAt:O}");
````

  
````go
archived, err := client.Beta.Agents.Archive(ctx, agent.ID, anthropic.BetaAgentArchiveParams{})
if err != nil {
	panic(err)
}
fmt.Printf("Archived at: %s\n", archived.ArchivedAt.Format(time.RFC3339))
````

  
````java
var archived = client.beta().agents().archive(agent.id());
IO.println("Archived at: " + archived.archivedAt().orElseThrow());
````

  
````php
$archived = $client->beta->agents->archive($agent->id);

echo "Archived at: {$archived->archivedAt->format(DateTimeInterface::ATOM)}\n";
````

  
````ruby
archived = client.beta.agents.archive(agent.id)
puts "Archived at: #{archived.archived_at.iso8601}"
````

</CodeGroup>

## Next steps

- [Configure tools](/docs/en/managed-agents/tools) to customize which capabilities the agent can use.
- [Attach skills](/docs/en/managed-agents/skills) for domain-specific expertise.
- [Start a session](/docs/en/managed-agents/sessions) that references your agent.