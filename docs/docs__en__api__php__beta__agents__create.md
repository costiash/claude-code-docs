## Create Agent

`$client->beta->agents->create(Model model, string name, ?string description, ?list<BetaManagedAgentsURLMCPServerParams> mcpServers, ?array<string,string> metadata, ?BetaManagedAgentsMultiagentParams multiagent, ?list<BetaManagedAgentsSkillParams> skills, ?string system, ?list<Tool> tools, ?list<AnthropicBeta> betas): BetaManagedAgentsAgent`

**post** `/v1/agents`

Create Agent

### Parameters

- `model: Model`

  Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-4-6`, or a `model_config` object for additional configuration control

- `name: string`

  Human-readable name for the agent.

- `description?:optional string`

  Description of what the agent does.

- `mcpServers?:optional list<BetaManagedAgentsURLMCPServerParams>`

  MCP servers this agent connects to. Maximum 20. Names must be unique within the array.

- `metadata?:optional array<string,string>`

  Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `multiagent?:optional BetaManagedAgentsMultiagentParams`

  A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

- `skills?:optional list<BetaManagedAgentsSkillParams>`

  Skills available to the agent.

- `system?:optional string`

  System prompt for the agent.

- `tools?:optional list<Tool>`

  Tool configurations available to the agent. Maximum of 128 tools across all toolsets allowed.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsAgent`

  - `string id`

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?string description`

  - `list<BetaManagedAgentsMCPServerURLDefinition> mcpServers`

  - `array<string,string> metadata`

  - `BetaManagedAgentsModelConfig model`

    Model identifier and configuration.

  - `?BetaManagedAgentsMultiagent multiagent`

    Resolved coordinator topology with a concrete agent roster.

  - `string name`

  - `list<Skill> skills`

  - `?string system`

  - `list<Tool> tools`

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `int version`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsAgent = $client->beta->agents->create(
  model: 'claude-sonnet-4-6',
  name: 'My First Agent',
  description: 'A general-purpose starter agent.',
  mcpServers: [
    [
      'name' => 'example-mcp',
      'type' => 'url',
      'url' => 'https://example-server.modelcontextprotocol.io/sse',
    ],
  ],
  metadata: ['foo' => 'bar'],
  multiagent: [
    'agents' => ['agent_011CZkYqphY8vELVzwCUpqiQ', ['type' => 'self']],
    'type' => 'coordinator',
  ],
  skills: [['skillID' => 'xlsx', 'type' => 'anthropic', 'version' => '1']],
  system: 'You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user\'s task end to end.',
  tools: [
    [
      'type' => 'agent_toolset_20260401',
      'configs' => [
        [
          'name' => 'bash',
          'enabled' => true,
          'permissionPolicy' => ['type' => 'always_allow'],
        ],
      ],
      'defaultConfig' => [
        'enabled' => true, 'permissionPolicy' => ['type' => 'always_allow']
      ],
    ],
  ],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsAgent);
```

#### Response

```json
{
  "id": "agent_011CZkYpogX7uDKUyvBTophP",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "A general-purpose starter agent.",
  "mcp_servers": [
    {
      "name": "example-mcp",
      "type": "url",
      "url": "https://example-server.modelcontextprotocol.io/sse"
    }
  ],
  "metadata": {
    "foo": "bar"
  },
  "model": {
    "id": "claude-sonnet-4-6",
    "speed": "standard"
  },
  "multiagent": {
    "agents": [
      {
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
        "type": "agent",
        "version": 1
      }
    ],
    "type": "coordinator"
  },
  "name": "My First Agent",
  "skills": [
    {
      "skill_id": "xlsx",
      "type": "anthropic",
      "version": "1"
    },
    {
      "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
      "type": "custom",
      "version": "2"
    }
  ],
  "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
  "tools": [
    {
      "configs": [
        {
          "enabled": true,
          "name": "bash",
          "permission_policy": {
            "type": "always_allow"
          }
        }
      ],
      "default_config": {
        "enabled": true,
        "permission_policy": {
          "type": "always_ask"
        }
      },
      "type": "agent_toolset_20260401"
    }
  ],
  "type": "agent",
  "updated_at": "2026-03-15T10:00:00Z",
  "version": 1
}
```
