# Agents

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

  MCP servers this agent connects to. Maximum 20. Names must be unique within the array. Every server must be referenced by an `mcp_toolset` in `tools`; unreferenced servers are rejected. See the [MCP connector guide](https://platform.claude.com/docs/en/managed-agents/mcp-connector).

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

## List Agents

`$client->beta->agents->list(?\Datetime createdAtGte, ?\Datetime createdAtLte, ?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<BetaManagedAgentsAgent>`

**get** `/v1/agents`

List Agents

### Parameters

- `createdAtGte?:optional \Datetime`

  Return agents created at or after this time (inclusive).

- `createdAtLte?:optional \Datetime`

  Return agents created at or before this time (inclusive).

- `includeArchived?:optional bool`

  Include archived agents in results. Defaults to false.

- `limit?:optional int`

  Maximum results per page. Default 20, maximum 100.

- `page?:optional string`

  Opaque pagination cursor from a previous response.

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

$page = $client->beta->agents->list(
  createdAtGte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  includeArchived: true,
  limit: 0,
  page: 'page',
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

#### Response

```json
{
  "data": [
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
  ],
  "next_page": "next_page"
}
```

## Get Agent

`$client->beta->agents->retrieve(string agentID, ?int version, ?list<AnthropicBeta> betas): BetaManagedAgentsAgent`

**get** `/v1/agents/{agent_id}`

Get Agent

### Parameters

- `agentID: string`

- `version?:optional int`

  Agent version. Omit for the most recent version. Must be at least 1 if specified.

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

$betaManagedAgentsAgent = $client->beta->agents->retrieve(
  'agent_011CZkYpogX7uDKUyvBTophP',
  version: 0,
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

## Update Agent

`$client->beta->agents->update(string agentID, int version, ?string description, ?list<BetaManagedAgentsURLMCPServerParams> mcpServers, ?array<string,string> metadata, ?Model model, ?BetaManagedAgentsMultiagentParams multiagent, ?string name, ?list<BetaManagedAgentsSkillParams> skills, ?string system, ?list<Tool> tools, ?list<AnthropicBeta> betas): BetaManagedAgentsAgent`

**post** `/v1/agents/{agent_id}`

Update Agent

### Parameters

- `agentID: string`

- `version: int`

  The agent's current version, used to prevent concurrent overwrites. Obtain this value from a create or retrieve response. The request fails if this does not match the server's current version.

- `description?:optional string`

  Description. Omit to preserve; send empty string or null to clear.

- `mcpServers?:optional list<BetaManagedAgentsURLMCPServerParams>`

  MCP servers. Full replacement. Omit to preserve; send empty array or `null` to clear. Names must be unique. Maximum 20. Every server must be referenced by an `mcp_toolset` in the agent's resulting `tools`; unreferenced servers are rejected. See the [MCP connector guide](https://platform.claude.com/docs/en/managed-agents/mcp-connector).

- `metadata?:optional array<string,string>`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `model?:optional Model`

  Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-4-6`, or a `model_config` object for additional configuration control. Omit to preserve. Cannot be cleared.

- `multiagent?:optional BetaManagedAgentsMultiagentParams`

  A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

- `name?:optional string`

  Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

- `skills?:optional list<BetaManagedAgentsSkillParams>`

  Skills. Full replacement. Omit to preserve; send empty array or null to clear.

- `system?:optional string`

  System prompt. Omit to preserve; send empty string or null to clear.

- `tools?:optional list<Tool>`

  Tool configurations available to the agent. Full replacement. Omit to preserve; send empty array or null to clear. Maximum of 128 tools across all toolsets allowed.

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

$betaManagedAgentsAgent = $client->beta->agents->update(
  'agent_011CZkYpogX7uDKUyvBTophP',
  version: 1,
  description: 'description',
  mcpServers: [
    [
      'name' => 'example-mcp',
      'type' => 'url',
      'url' => 'https://example-server.modelcontextprotocol.io/sse',
    ],
  ],
  metadata: ['foo' => 'string'],
  model: ['id' => 'claude-opus-4-6', 'speed' => 'standard'],
  multiagent: [
    'agents' => ['agent_011CZkYqphY8vELVzwCUpqiQ', ['type' => 'self']],
    'type' => 'coordinator',
  ],
  name: 'name',
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

## Archive Agent

`$client->beta->agents->archive(string agentID, ?list<AnthropicBeta> betas): BetaManagedAgentsAgent`

**post** `/v1/agents/{agent_id}/archive`

Archive Agent

### Parameters

- `agentID: string`

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

$betaManagedAgentsAgent = $client->beta->agents->archive(
  'agent_011CZkYpogX7uDKUyvBTophP', betas: ['message-batches-2024-09-24']
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

## Domain Types

### Beta Managed Agents Agent

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

### Beta Managed Agents Agent Reference

- `BetaManagedAgentsAgentReference`

  - `string id`

  - `Type type`

  - `int version`

### Beta Managed Agents Agent Tool Config

- `BetaManagedAgentsAgentToolConfig`

  - `bool enabled`

  - `Name name`

    Built-in agent tool identifier.

  - `PermissionPolicy permissionPolicy`

    Permission policy for tool execution.

### Beta Managed Agents Agent Tool Config Params

- `BetaManagedAgentsAgentToolConfigParams`

  - `Name name`

    Built-in agent tool identifier.

  - `?bool enabled`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `?PermissionPolicy permissionPolicy`

    Permission policy for tool execution.

### Beta Managed Agents Agent Toolset Default Config

- `BetaManagedAgentsAgentToolsetDefaultConfig`

  - `bool enabled`

  - `PermissionPolicy permissionPolicy`

    Permission policy for tool execution.

### Beta Managed Agents Agent Toolset Default Config Params

- `BetaManagedAgentsAgentToolsetDefaultConfigParams`

  - `?bool enabled`

    Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

  - `?PermissionPolicy permissionPolicy`

    Permission policy for tool execution.

### Beta Managed Agents Agent Toolset20260401

- `BetaManagedAgentsAgentToolset20260401`

  - `list<BetaManagedAgentsAgentToolConfig> configs`

  - `BetaManagedAgentsAgentToolsetDefaultConfig defaultConfig`

    Resolved default configuration for agent tools.

  - `Type type`

### Beta Managed Agents Agent Toolset20260401 Bash Input

- `BetaManagedAgentsAgentToolset20260401BashInput`

  - `?string command`

    Shell command to execute. Omit only when `restart` is true.

  - `?bool restart`

    When true, restart the persistent bash session instead of
    running a command. Subsequent calls without `restart` will
    run against the fresh session.

  - `?int timeoutMs`

    Per-call timeout in milliseconds. Defaults to the
    runner-wide tool timeout when omitted or zero.

### Beta Managed Agents Agent Toolset20260401 Edit Input

- `BetaManagedAgentsAgentToolset20260401EditInput`

  - `string filePath`

    Path of the file to edit.

  - `string newString`

    Replacement text.

  - `string oldString`

    Substring to find and replace.

  - `?bool replaceAll`

    When true, replace every occurrence of `old_string`
    instead of requiring a unique match.

### Beta Managed Agents Agent Toolset20260401 Glob Input

- `BetaManagedAgentsAgentToolset20260401GlobInput`

  - `string pattern`

    Doublestar glob pattern (e.g. `**/*.go`). Absolute patterns
    are only permitted when the runner is configured to allow
    them.

  - `?string path`

    Optional directory root to search under. Defaults to the
    runner's working directory.

### Beta Managed Agents Agent Toolset20260401 Grep Input

- `BetaManagedAgentsAgentToolset20260401GrepInput`

  - `string pattern`

    Regular expression to search for.

  - `?string path`

    Optional directory root to search under. Defaults to the
    runner's working directory.

### Beta Managed Agents Agent Toolset20260401 Params

- `BetaManagedAgentsAgentToolset20260401Params`

  - `Type type`

  - `?list<BetaManagedAgentsAgentToolConfigParams> configs`

    Per-tool configuration overrides.

  - `?BetaManagedAgentsAgentToolsetDefaultConfigParams defaultConfig`

    Default configuration for all tools in a toolset.

### Beta Managed Agents Agent Toolset20260401 Read Input

- `BetaManagedAgentsAgentToolset20260401ReadInput`

  - `string filePath`

    Path of the file to read.

  - `?list<int> viewRange`

    Optional `[start_line, end_line]` 1-indexed inclusive
    range. When omitted the entire file is returned.
    `end_line` of 0 or negative means "to end of file".

### Beta Managed Agents Agent Toolset20260401 Write Input

- `BetaManagedAgentsAgentToolset20260401WriteInput`

  - `string content`

    Full file contents to write.

  - `string filePath`

    Path of the file to write.

### Beta Managed Agents Always Allow Policy

- `BetaManagedAgentsAlwaysAllowPolicy`

  - `Type type`

### Beta Managed Agents Always Ask Policy

- `BetaManagedAgentsAlwaysAskPolicy`

  - `Type type`

### Beta Managed Agents Anthropic Skill

- `BetaManagedAgentsAnthropicSkill`

  - `string skillID`

  - `Type type`

  - `string version`

### Beta Managed Agents Anthropic Skill Params

- `BetaManagedAgentsAnthropicSkillParams`

  - `string skillID`

    Identifier of the Anthropic skill (e.g., "xlsx").

  - `Type type`

  - `?string version`

    Version to pin. Defaults to latest if omitted.

### Beta Managed Agents Custom Skill

- `BetaManagedAgentsCustomSkill`

  - `string skillID`

  - `Type type`

  - `string version`

### Beta Managed Agents Custom Skill Params

- `BetaManagedAgentsCustomSkillParams`

  - `string skillID`

    Tagged ID of the custom skill (e.g., "skill_01XJ5...").

  - `Type type`

  - `?string version`

    Version to pin. Defaults to latest if omitted.

### Beta Managed Agents Custom Tool

- `BetaManagedAgentsCustomTool`

  - `string description`

  - `BetaManagedAgentsCustomToolInputSchema inputSchema`

    JSON Schema for custom tool input parameters.

  - `string name`

  - `Type type`

### Beta Managed Agents Custom Tool Input Schema

- `BetaManagedAgentsCustomToolInputSchema`

  - `"object" type`

  - `?array<string,mixed> properties`

  - `?list<string> required`

### Beta Managed Agents Custom Tool Params

- `BetaManagedAgentsCustomToolParams`

  - `string description`

    Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

  - `BetaManagedAgentsCustomToolInputSchema inputSchema`

    JSON Schema for custom tool input parameters.

  - `string name`

    Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

  - `Type type`

### Beta Managed Agents MCP Server URL Definition

- `BetaManagedAgentsMCPServerURLDefinition`

  - `string name`

  - `Type type`

  - `string url`

### Beta Managed Agents MCP Tool Config

- `BetaManagedAgentsMCPToolConfig`

  - `bool enabled`

  - `string name`

  - `PermissionPolicy permissionPolicy`

    Permission policy for tool execution.

### Beta Managed Agents MCP Tool Config Params

- `BetaManagedAgentsMCPToolConfigParams`

  - `string name`

    Name of the MCP tool to configure. 1-128 characters.

  - `?bool enabled`

    Whether this tool is enabled. Overrides the `default_config` setting.

  - `?PermissionPolicy permissionPolicy`

    Permission policy for tool execution.

### Beta Managed Agents MCP Toolset

- `BetaManagedAgentsMCPToolset`

  - `list<BetaManagedAgentsMCPToolConfig> configs`

  - `BetaManagedAgentsMCPToolsetDefaultConfig defaultConfig`

    Resolved default configuration for all tools from an MCP server.

  - `string mcpServerName`

  - `Type type`

### Beta Managed Agents MCP Toolset Default Config

- `BetaManagedAgentsMCPToolsetDefaultConfig`

  - `bool enabled`

  - `PermissionPolicy permissionPolicy`

    Permission policy for tool execution.

### Beta Managed Agents MCP Toolset Default Config Params

- `BetaManagedAgentsMCPToolsetDefaultConfigParams`

  - `?bool enabled`

    Whether tools are enabled by default. Defaults to true if not specified.

  - `?PermissionPolicy permissionPolicy`

    Permission policy for tool execution.

### Beta Managed Agents MCP Toolset Params

- `BetaManagedAgentsMCPToolsetParams`

  - `string mcpServerName`

    Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

  - `Type type`

  - `?list<BetaManagedAgentsMCPToolConfigParams> configs`

    Per-tool configuration overrides.

  - `?BetaManagedAgentsMCPToolsetDefaultConfigParams defaultConfig`

    Default configuration for all tools from an MCP server.

### Beta Managed Agents Model

- `BetaManagedAgentsModel`

  - `"claude-sonnet-5"`

    High-performance model for coding and agents

  - `"claude-fable-5"`

    Next generation of intelligence for the hardest knowledge work and coding problems

  - `"claude-opus-4-8"`

    Frontier intelligence for long-running agents and coding

  - `"claude-opus-4-7"`

    Frontier intelligence for long-running agents and coding

  - `"claude-opus-4-6"`

    Most intelligent model for building agents and coding

  - `"claude-sonnet-4-6"`

    Best combination of speed and intelligence

  - `"claude-haiku-4-5"`

    Fastest model with near-frontier intelligence

  - `"claude-haiku-4-5-20251001"`

    Fastest model with near-frontier intelligence

  - `"claude-opus-4-5"`

    Premium model combining maximum intelligence with practical performance

  - `"claude-opus-4-5-20251101"`

    Premium model combining maximum intelligence with practical performance

  - `"claude-sonnet-4-5"`

    High-performance model for agents and coding

  - `"claude-sonnet-4-5-20250929"`

    High-performance model for agents and coding

### Beta Managed Agents Model Config

- `BetaManagedAgentsModelConfig`

  - `BetaManagedAgentsModel id`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `?Speed speed`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

### Beta Managed Agents Model Config Params

- `BetaManagedAgentsModelConfigParams`

  - `BetaManagedAgentsModel id`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `?Speed speed`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

### Beta Managed Agents Multiagent Coordinator

- `BetaManagedAgentsMultiagentCoordinator`

  - `list<BetaManagedAgentsAgentReference> agents`

    Agents the coordinator may spawn as session threads, each resolved to a specific version.

  - `Type type`

### Beta Managed Agents Multiagent Coordinator Params

- `BetaManagedAgentsMultiagentCoordinatorParams`

  - `list<BetaManagedAgentsMultiagentRosterEntryParams> agents`

    Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

  - `Type type`

### Beta Managed Agents Multiagent Self Params

- `BetaManagedAgentsMultiagentSelfParams`

  - `Type type`

### Beta Managed Agents Session Thread Agent

- `BetaManagedAgentsSessionThreadAgent`

  - `string id`

  - `?string description`

  - `list<BetaManagedAgentsMCPServerURLDefinition> mcpServers`

  - `BetaManagedAgentsModelConfig model`

    Model identifier and configuration.

  - `string name`

  - `list<Skill> skills`

  - `?string system`

  - `list<Tool> tools`

  - `Type type`

  - `int version`

### Beta Managed Agents Skill Params

- `BetaManagedAgentsSkillParams`

  - `BetaManagedAgentsAnthropicSkillParams`

    - `string skillID`

      Identifier of the Anthropic skill (e.g., "xlsx").

    - `Type type`

    - `?string version`

      Version to pin. Defaults to latest if omitted.

  - `BetaManagedAgentsCustomSkillParams`

    - `string skillID`

      Tagged ID of the custom skill (e.g., "skill_01XJ5...").

    - `Type type`

    - `?string version`

      Version to pin. Defaults to latest if omitted.

### Beta Managed Agents URL MCP Server Params

- `BetaManagedAgentsURLMCPServerParams`

  - `string name`

    Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

  - `Type type`

  - `string url`

    Endpoint URL for the MCP server.

# Versions

## List Agent Versions

`$client->beta->agents->versions->list(string agentID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<BetaManagedAgentsAgent>`

**get** `/v1/agents/{agent_id}/versions`

List Agent Versions

### Parameters

- `agentID: string`

- `limit?:optional int`

  Maximum results per page. Default 20, maximum 100.

- `page?:optional string`

  Opaque pagination cursor.

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

$page = $client->beta->agents->versions->list(
  'agent_011CZkYpogX7uDKUyvBTophP',
  limit: 0,
  page: 'page',
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

#### Response

```json
{
  "data": [
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
  ],
  "next_page": "next_page"
}
```
