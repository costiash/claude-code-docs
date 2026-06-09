# Agents

## Create Agent

**post** `/v1/agents`

Create Agent

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

### Body Parameters

- `model: BetaManagedAgentsModel or BetaManagedAgentsModelConfigParams`

  Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-4-6`, or a `model_config` object for additional configuration control

  - `BetaManagedAgentsModel = "claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more or string`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `"claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

    - `string`

  - `BetaManagedAgentsModelConfigParams object { id, speed }`

    An object that defines additional configuration control over model use

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

- `name: string`

  Human-readable name for the agent.

- `description: optional string`

  Description of what the agent does.

- `mcp_servers: optional array of BetaManagedAgentsURLMCPServerParams`

  MCP servers this agent connects to. Maximum 20. Names must be unique within the array.

  - `name: string`

    Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

  - `type: "url"`

    - `"url"`

  - `url: string`

    Endpoint URL for the MCP server.

- `metadata: optional map[string]`

  Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `multiagent: optional BetaManagedAgentsMultiagentParams`

  A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

  - `agents: array of BetaManagedAgentsMultiagentRosterEntryParams`

    Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

    - `string`

    - `BetaManagedAgentsAgentParams object { id, type, version }`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `id: string`

        The `agent` ID.

      - `type: "agent"`

        - `"agent"`

      - `version: optional number`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

    - `BetaManagedAgentsMultiagentSelfParams object { type }`

      Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

      - `type: "self"`

        - `"self"`

  - `type: "coordinator"`

    - `"coordinator"`

- `skills: optional array of BetaManagedAgentsSkillParams`

  Skills available to the agent.

  - `BetaManagedAgentsAnthropicSkillParams object { skill_id, type, version }`

    An Anthropic-managed skill.

    - `skill_id: string`

      Identifier of the Anthropic skill (e.g., "xlsx").

    - `type: "anthropic"`

      - `"anthropic"`

    - `version: optional string`

      Version to pin. Defaults to latest if omitted.

  - `BetaManagedAgentsCustomSkillParams object { skill_id, type, version }`

    A user-created custom skill.

    - `skill_id: string`

      Tagged ID of the custom skill (e.g., "skill_01XJ5...").

    - `type: "custom"`

      - `"custom"`

    - `version: optional string`

      Version to pin. Defaults to latest if omitted.

- `system: optional string`

  System prompt for the agent.

- `tools: optional array of BetaManagedAgentsAgentToolset20260401Params or BetaManagedAgentsMCPToolsetParams or BetaManagedAgentsCustomToolParams`

  Tool configurations available to the agent. Maximum of 128 tools across all toolsets allowed.

  - `BetaManagedAgentsAgentToolset20260401Params object { type, configs, default_config }`

    Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

    - `type: "agent_toolset_20260401"`

      - `"agent_toolset_20260401"`

    - `configs: optional array of BetaManagedAgentsAgentToolConfigParams`

      Per-tool configuration overrides.

      - `name: "bash" or "edit" or "read" or 5 more`

        Built-in agent tool identifier.

        - `"bash"`

        - `"edit"`

        - `"read"`

        - `"write"`

        - `"glob"`

        - `"grep"`

        - `"web_fetch"`

        - `"web_search"`

      - `enabled: optional boolean`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

          Tool calls are automatically approved without user confirmation.

          - `type: "always_allow"`

            - `"always_allow"`

        - `BetaManagedAgentsAlwaysAskPolicy object { type }`

          Tool calls require user confirmation before execution.

          - `type: "always_ask"`

            - `"always_ask"`

    - `default_config: optional BetaManagedAgentsAgentToolsetDefaultConfigParams`

      Default configuration for all tools in a toolset.

      - `enabled: optional boolean`

        Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

      - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

          Tool calls are automatically approved without user confirmation.

        - `BetaManagedAgentsAlwaysAskPolicy object { type }`

          Tool calls require user confirmation before execution.

  - `BetaManagedAgentsMCPToolsetParams object { mcp_server_name, type, configs, default_config }`

    Configuration for tools from an MCP server defined in `mcp_servers`.

    - `mcp_server_name: string`

      Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

    - `type: "mcp_toolset"`

      - `"mcp_toolset"`

    - `configs: optional array of BetaManagedAgentsMCPToolConfigParams`

      Per-tool configuration overrides.

      - `name: string`

        Name of the MCP tool to configure. 1-128 characters.

      - `enabled: optional boolean`

        Whether this tool is enabled. Overrides the `default_config` setting.

      - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

          Tool calls are automatically approved without user confirmation.

        - `BetaManagedAgentsAlwaysAskPolicy object { type }`

          Tool calls require user confirmation before execution.

    - `default_config: optional BetaManagedAgentsMCPToolsetDefaultConfigParams`

      Default configuration for all tools from an MCP server.

      - `enabled: optional boolean`

        Whether tools are enabled by default. Defaults to true if not specified.

      - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

          Tool calls are automatically approved without user confirmation.

        - `BetaManagedAgentsAlwaysAskPolicy object { type }`

          Tool calls require user confirmation before execution.

  - `BetaManagedAgentsCustomToolParams object { description, input_schema, name, type }`

    A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

    - `description: string`

      Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

    - `input_schema: BetaManagedAgentsCustomToolInputSchema`

      JSON Schema for custom tool input parameters.

      - `type: "object"`

        - `"object"`

      - `properties: optional map[unknown]`

      - `required: optional array of string`

    - `name: string`

      Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

    - `type: "custom"`

      - `"custom"`

### Returns

- `BetaManagedAgentsAgent object { id, archived_at, created_at, 12 more }`

  A Managed Agents `agent`.

  - `id: string`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

  - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

    - `name: string`

    - `type: "url"`

      - `"url"`

    - `url: string`

  - `metadata: map[string]`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

      - `string`

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `multiagent: BetaManagedAgentsMultiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: array of BetaManagedAgentsAgentReference`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `id: string`

      - `type: "agent"`

        - `"agent"`

      - `version: number`

    - `type: "coordinator"`

      - `"coordinator"`

  - `name: string`

  - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

    - `BetaManagedAgentsAnthropicSkill object { skill_id, type, version }`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

        - `"anthropic"`

      - `version: string`

    - `BetaManagedAgentsCustomSkill object { skill_id, type, version }`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

        - `"custom"`

      - `version: string`

  - `system: string`

  - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

    - `BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type }`

      - `configs: array of BetaManagedAgentsAgentToolConfig`

        - `enabled: boolean`

        - `name: "bash" or "edit" or "read" or 5 more`

          Built-in agent tool identifier.

          - `"bash"`

          - `"edit"`

          - `"read"`

          - `"write"`

          - `"glob"`

          - `"grep"`

          - `"web_fetch"`

          - `"web_search"`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

    - `BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type }`

      - `configs: array of BetaManagedAgentsMCPToolConfig`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

    - `BetaManagedAgentsCustomTool object { description, input_schema, name, type }`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: "object"`

          - `"object"`

        - `properties: optional map[unknown]`

        - `required: optional array of string`

      - `name: string`

      - `type: "custom"`

        - `"custom"`

  - `type: "agent"`

    - `"agent"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `version: number`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```http
curl https://api.anthropic.com/v1/agents \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d "{
          \"model\": \"claude-sonnet-4-6\",
          \"name\": \"My First Agent\",
          \"description\": \"A general-purpose starter agent.\",
          \"metadata\": {
            \"foo\": \"bar\"
          },
          \"system\": \"You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.\",
          \"tools\": [
            {
              \"type\": \"agent_toolset_20260401\"
            }
          ]
        }"
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

**get** `/v1/agents`

List Agents

### Query Parameters

- `"created_at[gte]": optional string`

  Return agents created at or after this time (inclusive).

- `"created_at[lte]": optional string`

  Return agents created at or before this time (inclusive).

- `include_archived: optional boolean`

  Include archived agents in results. Defaults to false.

- `limit: optional number`

  Maximum results per page. Default 20, maximum 100.

- `page: optional string`

  Opaque pagination cursor from a previous response.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

### Returns

- `data: array of BetaManagedAgentsAgent`

  List of agents.

  - `id: string`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

  - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

    - `name: string`

    - `type: "url"`

      - `"url"`

    - `url: string`

  - `metadata: map[string]`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

      - `string`

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `multiagent: BetaManagedAgentsMultiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: array of BetaManagedAgentsAgentReference`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `id: string`

      - `type: "agent"`

        - `"agent"`

      - `version: number`

    - `type: "coordinator"`

      - `"coordinator"`

  - `name: string`

  - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

    - `BetaManagedAgentsAnthropicSkill object { skill_id, type, version }`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

        - `"anthropic"`

      - `version: string`

    - `BetaManagedAgentsCustomSkill object { skill_id, type, version }`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

        - `"custom"`

      - `version: string`

  - `system: string`

  - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

    - `BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type }`

      - `configs: array of BetaManagedAgentsAgentToolConfig`

        - `enabled: boolean`

        - `name: "bash" or "edit" or "read" or 5 more`

          Built-in agent tool identifier.

          - `"bash"`

          - `"edit"`

          - `"read"`

          - `"write"`

          - `"glob"`

          - `"grep"`

          - `"web_fetch"`

          - `"web_search"`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

    - `BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type }`

      - `configs: array of BetaManagedAgentsMCPToolConfig`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

    - `BetaManagedAgentsCustomTool object { description, input_schema, name, type }`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: "object"`

          - `"object"`

        - `properties: optional map[unknown]`

        - `required: optional array of string`

      - `name: string`

      - `type: "custom"`

        - `"custom"`

  - `type: "agent"`

    - `"agent"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `version: number`

    The agent's current version. Starts at 1 and increments when the agent is modified.

- `next_page: optional string`

  Opaque cursor for the next page. Null when no more results.

### Example

```http
curl https://api.anthropic.com/v1/agents \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**get** `/v1/agents/{agent_id}`

Get Agent

### Path Parameters

- `agent_id: string`

### Query Parameters

- `version: optional number`

  Agent version. Omit for the most recent version. Must be at least 1 if specified.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

### Returns

- `BetaManagedAgentsAgent object { id, archived_at, created_at, 12 more }`

  A Managed Agents `agent`.

  - `id: string`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

  - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

    - `name: string`

    - `type: "url"`

      - `"url"`

    - `url: string`

  - `metadata: map[string]`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

      - `string`

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `multiagent: BetaManagedAgentsMultiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: array of BetaManagedAgentsAgentReference`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `id: string`

      - `type: "agent"`

        - `"agent"`

      - `version: number`

    - `type: "coordinator"`

      - `"coordinator"`

  - `name: string`

  - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

    - `BetaManagedAgentsAnthropicSkill object { skill_id, type, version }`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

        - `"anthropic"`

      - `version: string`

    - `BetaManagedAgentsCustomSkill object { skill_id, type, version }`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

        - `"custom"`

      - `version: string`

  - `system: string`

  - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

    - `BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type }`

      - `configs: array of BetaManagedAgentsAgentToolConfig`

        - `enabled: boolean`

        - `name: "bash" or "edit" or "read" or 5 more`

          Built-in agent tool identifier.

          - `"bash"`

          - `"edit"`

          - `"read"`

          - `"write"`

          - `"glob"`

          - `"grep"`

          - `"web_fetch"`

          - `"web_search"`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

    - `BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type }`

      - `configs: array of BetaManagedAgentsMCPToolConfig`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

    - `BetaManagedAgentsCustomTool object { description, input_schema, name, type }`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: "object"`

          - `"object"`

        - `properties: optional map[unknown]`

        - `required: optional array of string`

      - `name: string`

      - `type: "custom"`

        - `"custom"`

  - `type: "agent"`

    - `"agent"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `version: number`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```http
curl https://api.anthropic.com/v1/agents/$AGENT_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**post** `/v1/agents/{agent_id}`

Update Agent

### Path Parameters

- `agent_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

### Body Parameters

- `version: number`

  The agent's current version, used to prevent concurrent overwrites. Obtain this value from a create or retrieve response. The request fails if this does not match the server's current version.

- `description: optional string`

  Description. Omit to preserve; send empty string or null to clear.

- `mcp_servers: optional array of BetaManagedAgentsURLMCPServerParams`

  MCP servers. Full replacement. Omit to preserve; send empty array or null to clear. Names must be unique. Maximum 20.

  - `name: string`

    Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

  - `type: "url"`

    - `"url"`

  - `url: string`

    Endpoint URL for the MCP server.

- `metadata: optional map[string]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `model: optional BetaManagedAgentsModel or BetaManagedAgentsModelConfigParams`

  Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-4-6`, or a `model_config` object for additional configuration control. Omit to preserve. Cannot be cleared.

  - `BetaManagedAgentsModel = "claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more or string`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `"claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

    - `string`

  - `BetaManagedAgentsModelConfigParams object { id, speed }`

    An object that defines additional configuration control over model use

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

- `multiagent: optional BetaManagedAgentsMultiagentParams`

  A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

  - `agents: array of BetaManagedAgentsMultiagentRosterEntryParams`

    Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

    - `string`

    - `BetaManagedAgentsAgentParams object { id, type, version }`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `id: string`

        The `agent` ID.

      - `type: "agent"`

        - `"agent"`

      - `version: optional number`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

    - `BetaManagedAgentsMultiagentSelfParams object { type }`

      Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

      - `type: "self"`

        - `"self"`

  - `type: "coordinator"`

    - `"coordinator"`

- `name: optional string`

  Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

- `skills: optional array of BetaManagedAgentsSkillParams`

  Skills. Full replacement. Omit to preserve; send empty array or null to clear.

  - `BetaManagedAgentsAnthropicSkillParams object { skill_id, type, version }`

    An Anthropic-managed skill.

    - `skill_id: string`

      Identifier of the Anthropic skill (e.g., "xlsx").

    - `type: "anthropic"`

      - `"anthropic"`

    - `version: optional string`

      Version to pin. Defaults to latest if omitted.

  - `BetaManagedAgentsCustomSkillParams object { skill_id, type, version }`

    A user-created custom skill.

    - `skill_id: string`

      Tagged ID of the custom skill (e.g., "skill_01XJ5...").

    - `type: "custom"`

      - `"custom"`

    - `version: optional string`

      Version to pin. Defaults to latest if omitted.

- `system: optional string`

  System prompt. Omit to preserve; send empty string or null to clear.

- `tools: optional array of BetaManagedAgentsAgentToolset20260401Params or BetaManagedAgentsMCPToolsetParams or BetaManagedAgentsCustomToolParams`

  Tool configurations available to the agent. Full replacement. Omit to preserve; send empty array or null to clear. Maximum of 128 tools across all toolsets allowed.

  - `BetaManagedAgentsAgentToolset20260401Params object { type, configs, default_config }`

    Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

    - `type: "agent_toolset_20260401"`

      - `"agent_toolset_20260401"`

    - `configs: optional array of BetaManagedAgentsAgentToolConfigParams`

      Per-tool configuration overrides.

      - `name: "bash" or "edit" or "read" or 5 more`

        Built-in agent tool identifier.

        - `"bash"`

        - `"edit"`

        - `"read"`

        - `"write"`

        - `"glob"`

        - `"grep"`

        - `"web_fetch"`

        - `"web_search"`

      - `enabled: optional boolean`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

          Tool calls are automatically approved without user confirmation.

          - `type: "always_allow"`

            - `"always_allow"`

        - `BetaManagedAgentsAlwaysAskPolicy object { type }`

          Tool calls require user confirmation before execution.

          - `type: "always_ask"`

            - `"always_ask"`

    - `default_config: optional BetaManagedAgentsAgentToolsetDefaultConfigParams`

      Default configuration for all tools in a toolset.

      - `enabled: optional boolean`

        Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

      - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

          Tool calls are automatically approved without user confirmation.

        - `BetaManagedAgentsAlwaysAskPolicy object { type }`

          Tool calls require user confirmation before execution.

  - `BetaManagedAgentsMCPToolsetParams object { mcp_server_name, type, configs, default_config }`

    Configuration for tools from an MCP server defined in `mcp_servers`.

    - `mcp_server_name: string`

      Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

    - `type: "mcp_toolset"`

      - `"mcp_toolset"`

    - `configs: optional array of BetaManagedAgentsMCPToolConfigParams`

      Per-tool configuration overrides.

      - `name: string`

        Name of the MCP tool to configure. 1-128 characters.

      - `enabled: optional boolean`

        Whether this tool is enabled. Overrides the `default_config` setting.

      - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

          Tool calls are automatically approved without user confirmation.

        - `BetaManagedAgentsAlwaysAskPolicy object { type }`

          Tool calls require user confirmation before execution.

    - `default_config: optional BetaManagedAgentsMCPToolsetDefaultConfigParams`

      Default configuration for all tools from an MCP server.

      - `enabled: optional boolean`

        Whether tools are enabled by default. Defaults to true if not specified.

      - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

          Tool calls are automatically approved without user confirmation.

        - `BetaManagedAgentsAlwaysAskPolicy object { type }`

          Tool calls require user confirmation before execution.

  - `BetaManagedAgentsCustomToolParams object { description, input_schema, name, type }`

    A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

    - `description: string`

      Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

    - `input_schema: BetaManagedAgentsCustomToolInputSchema`

      JSON Schema for custom tool input parameters.

      - `type: "object"`

        - `"object"`

      - `properties: optional map[unknown]`

      - `required: optional array of string`

    - `name: string`

      Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

    - `type: "custom"`

      - `"custom"`

### Returns

- `BetaManagedAgentsAgent object { id, archived_at, created_at, 12 more }`

  A Managed Agents `agent`.

  - `id: string`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

  - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

    - `name: string`

    - `type: "url"`

      - `"url"`

    - `url: string`

  - `metadata: map[string]`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

      - `string`

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `multiagent: BetaManagedAgentsMultiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: array of BetaManagedAgentsAgentReference`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `id: string`

      - `type: "agent"`

        - `"agent"`

      - `version: number`

    - `type: "coordinator"`

      - `"coordinator"`

  - `name: string`

  - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

    - `BetaManagedAgentsAnthropicSkill object { skill_id, type, version }`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

        - `"anthropic"`

      - `version: string`

    - `BetaManagedAgentsCustomSkill object { skill_id, type, version }`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

        - `"custom"`

      - `version: string`

  - `system: string`

  - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

    - `BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type }`

      - `configs: array of BetaManagedAgentsAgentToolConfig`

        - `enabled: boolean`

        - `name: "bash" or "edit" or "read" or 5 more`

          Built-in agent tool identifier.

          - `"bash"`

          - `"edit"`

          - `"read"`

          - `"write"`

          - `"glob"`

          - `"grep"`

          - `"web_fetch"`

          - `"web_search"`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

    - `BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type }`

      - `configs: array of BetaManagedAgentsMCPToolConfig`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

    - `BetaManagedAgentsCustomTool object { description, input_schema, name, type }`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: "object"`

          - `"object"`

        - `properties: optional map[unknown]`

        - `required: optional array of string`

      - `name: string`

      - `type: "custom"`

        - `"custom"`

  - `type: "agent"`

    - `"agent"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `version: number`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```http
curl https://api.anthropic.com/v1/agents/$AGENT_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d "{
          \"version\": 1,
          \"system\": \"You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.\"
        }"
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

**post** `/v1/agents/{agent_id}/archive`

Archive Agent

### Path Parameters

- `agent_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

### Returns

- `BetaManagedAgentsAgent object { id, archived_at, created_at, 12 more }`

  A Managed Agents `agent`.

  - `id: string`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

  - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

    - `name: string`

    - `type: "url"`

      - `"url"`

    - `url: string`

  - `metadata: map[string]`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

      - `string`

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `multiagent: BetaManagedAgentsMultiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: array of BetaManagedAgentsAgentReference`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `id: string`

      - `type: "agent"`

        - `"agent"`

      - `version: number`

    - `type: "coordinator"`

      - `"coordinator"`

  - `name: string`

  - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

    - `BetaManagedAgentsAnthropicSkill object { skill_id, type, version }`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

        - `"anthropic"`

      - `version: string`

    - `BetaManagedAgentsCustomSkill object { skill_id, type, version }`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

        - `"custom"`

      - `version: string`

  - `system: string`

  - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

    - `BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type }`

      - `configs: array of BetaManagedAgentsAgentToolConfig`

        - `enabled: boolean`

        - `name: "bash" or "edit" or "read" or 5 more`

          Built-in agent tool identifier.

          - `"bash"`

          - `"edit"`

          - `"read"`

          - `"write"`

          - `"glob"`

          - `"grep"`

          - `"web_fetch"`

          - `"web_search"`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

    - `BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type }`

      - `configs: array of BetaManagedAgentsMCPToolConfig`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

    - `BetaManagedAgentsCustomTool object { description, input_schema, name, type }`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: "object"`

          - `"object"`

        - `properties: optional map[unknown]`

        - `required: optional array of string`

      - `name: string`

      - `type: "custom"`

        - `"custom"`

  - `type: "agent"`

    - `"agent"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `version: number`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```http
curl https://api.anthropic.com/v1/agents/$AGENT_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

- `BetaManagedAgentsAgent object { id, archived_at, created_at, 12 more }`

  A Managed Agents `agent`.

  - `id: string`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

  - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

    - `name: string`

    - `type: "url"`

      - `"url"`

    - `url: string`

  - `metadata: map[string]`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

      - `string`

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `multiagent: BetaManagedAgentsMultiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: array of BetaManagedAgentsAgentReference`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `id: string`

      - `type: "agent"`

        - `"agent"`

      - `version: number`

    - `type: "coordinator"`

      - `"coordinator"`

  - `name: string`

  - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

    - `BetaManagedAgentsAnthropicSkill object { skill_id, type, version }`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

        - `"anthropic"`

      - `version: string`

    - `BetaManagedAgentsCustomSkill object { skill_id, type, version }`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

        - `"custom"`

      - `version: string`

  - `system: string`

  - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

    - `BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type }`

      - `configs: array of BetaManagedAgentsAgentToolConfig`

        - `enabled: boolean`

        - `name: "bash" or "edit" or "read" or 5 more`

          Built-in agent tool identifier.

          - `"bash"`

          - `"edit"`

          - `"read"`

          - `"write"`

          - `"glob"`

          - `"grep"`

          - `"web_fetch"`

          - `"web_search"`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

    - `BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type }`

      - `configs: array of BetaManagedAgentsMCPToolConfig`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

    - `BetaManagedAgentsCustomTool object { description, input_schema, name, type }`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: "object"`

          - `"object"`

        - `properties: optional map[unknown]`

        - `required: optional array of string`

      - `name: string`

      - `type: "custom"`

        - `"custom"`

  - `type: "agent"`

    - `"agent"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `version: number`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Beta Managed Agents Agent Reference

- `BetaManagedAgentsAgentReference object { id, type, version }`

  A resolved agent reference with a concrete version.

  - `id: string`

  - `type: "agent"`

    - `"agent"`

  - `version: number`

### Beta Managed Agents Agent Tool Config

- `BetaManagedAgentsAgentToolConfig object { enabled, name, permission_policy }`

  Configuration for a specific agent tool.

  - `enabled: boolean`

  - `name: "bash" or "edit" or "read" or 5 more`

    Built-in agent tool identifier.

    - `"bash"`

    - `"edit"`

    - `"read"`

    - `"write"`

    - `"glob"`

    - `"grep"`

    - `"web_fetch"`

    - `"web_search"`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `BetaManagedAgentsAlwaysAskPolicy object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents Agent Tool Config Params

- `BetaManagedAgentsAgentToolConfigParams object { name, enabled, permission_policy }`

  Configuration override for a specific tool within a toolset.

  - `name: "bash" or "edit" or "read" or 5 more`

    Built-in agent tool identifier.

    - `"bash"`

    - `"edit"`

    - `"read"`

    - `"write"`

    - `"glob"`

    - `"grep"`

    - `"web_fetch"`

    - `"web_search"`

  - `enabled: optional boolean`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `BetaManagedAgentsAlwaysAskPolicy object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents Agent Toolset Default Config

- `BetaManagedAgentsAgentToolsetDefaultConfig object { enabled, permission_policy }`

  Resolved default configuration for agent tools.

  - `enabled: boolean`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `BetaManagedAgentsAlwaysAskPolicy object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents Agent Toolset Default Config Params

- `BetaManagedAgentsAgentToolsetDefaultConfigParams object { enabled, permission_policy }`

  Default configuration for all tools in a toolset.

  - `enabled: optional boolean`

    Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

  - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `BetaManagedAgentsAlwaysAskPolicy object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents Agent Toolset20260401

- `BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type }`

  - `configs: array of BetaManagedAgentsAgentToolConfig`

    - `enabled: boolean`

    - `name: "bash" or "edit" or "read" or 5 more`

      Built-in agent tool identifier.

      - `"bash"`

      - `"edit"`

      - `"read"`

      - `"write"`

      - `"glob"`

      - `"grep"`

      - `"web_fetch"`

      - `"web_search"`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

        Tool calls are automatically approved without user confirmation.

        - `type: "always_allow"`

          - `"always_allow"`

      - `BetaManagedAgentsAlwaysAskPolicy object { type }`

        Tool calls require user confirmation before execution.

        - `type: "always_ask"`

          - `"always_ask"`

  - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

    Resolved default configuration for agent tools.

    - `enabled: boolean`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

        Tool calls are automatically approved without user confirmation.

      - `BetaManagedAgentsAlwaysAskPolicy object { type }`

        Tool calls require user confirmation before execution.

  - `type: "agent_toolset_20260401"`

    - `"agent_toolset_20260401"`

### Beta Managed Agents Agent Toolset20260401 Bash Input

- `BetaManagedAgentsAgentToolset20260401BashInput object { command, restart, timeout_ms }`

  Input payload for the `bash` tool of the
  `agent_toolset_20260401` toolset. All fields are optional;
  a normal invocation supplies `command`, while `restart=true`
  (with no `command`) reboots the runner-side bash session.

  - `command: optional string`

    Shell command to execute. Omit only when `restart` is true.

  - `restart: optional boolean`

    When true, restart the persistent bash session instead of
    running a command. Subsequent calls without `restart` will
    run against the fresh session.

  - `timeout_ms: optional number`

    Per-call timeout in milliseconds. Defaults to the
    runner-wide tool timeout when omitted or zero.

### Beta Managed Agents Agent Toolset20260401 Edit Input

- `BetaManagedAgentsAgentToolset20260401EditInput object { file_path, new_string, old_string, replace_all }`

  Input payload for the `edit` tool. Performs a string
  replacement in the named file; by default `old_string` must
  occur exactly once.

  - `file_path: string`

    Path of the file to edit.

  - `new_string: string`

    Replacement text.

  - `old_string: string`

    Substring to find and replace.

  - `replace_all: optional boolean`

    When true, replace every occurrence of `old_string`
    instead of requiring a unique match.

### Beta Managed Agents Agent Toolset20260401 Glob Input

- `BetaManagedAgentsAgentToolset20260401GlobInput object { pattern, path }`

  Input payload for the `glob` tool. Returns paths matching a
  doublestar glob pattern, newest first.

  - `pattern: string`

    Doublestar glob pattern (e.g. `**/*.go`). Absolute patterns
    are only permitted when the runner is configured to allow
    them.

  - `path: optional string`

    Optional directory root to search under. Defaults to the
    runner's working directory.

### Beta Managed Agents Agent Toolset20260401 Grep Input

- `BetaManagedAgentsAgentToolset20260401GrepInput object { pattern, path }`

  Input payload for the `grep` tool. Searches file contents for
  a regular expression, returning matching lines.

  - `pattern: string`

    Regular expression to search for.

  - `path: optional string`

    Optional directory root to search under. Defaults to the
    runner's working directory.

### Beta Managed Agents Agent Toolset20260401 Params

- `BetaManagedAgentsAgentToolset20260401Params object { type, configs, default_config }`

  Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

  - `type: "agent_toolset_20260401"`

    - `"agent_toolset_20260401"`

  - `configs: optional array of BetaManagedAgentsAgentToolConfigParams`

    Per-tool configuration overrides.

    - `name: "bash" or "edit" or "read" or 5 more`

      Built-in agent tool identifier.

      - `"bash"`

      - `"edit"`

      - `"read"`

      - `"write"`

      - `"glob"`

      - `"grep"`

      - `"web_fetch"`

      - `"web_search"`

    - `enabled: optional boolean`

      Whether this tool is enabled and available to Claude. Overrides the default_config setting.

    - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

        Tool calls are automatically approved without user confirmation.

        - `type: "always_allow"`

          - `"always_allow"`

      - `BetaManagedAgentsAlwaysAskPolicy object { type }`

        Tool calls require user confirmation before execution.

        - `type: "always_ask"`

          - `"always_ask"`

  - `default_config: optional BetaManagedAgentsAgentToolsetDefaultConfigParams`

    Default configuration for all tools in a toolset.

    - `enabled: optional boolean`

      Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

    - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

        Tool calls are automatically approved without user confirmation.

      - `BetaManagedAgentsAlwaysAskPolicy object { type }`

        Tool calls require user confirmation before execution.

### Beta Managed Agents Agent Toolset20260401 Read Input

- `BetaManagedAgentsAgentToolset20260401ReadInput object { file_path, view_range }`

  Input payload for the `read` tool. Reads file contents
  relative to the runner's working directory (or absolute when
  the runner permits).

  - `file_path: string`

    Path of the file to read.

  - `view_range: optional array of number`

    Optional `[start_line, end_line]` 1-indexed inclusive
    range. When omitted the entire file is returned.
    `end_line` of 0 or negative means "to end of file".

### Beta Managed Agents Agent Toolset20260401 Write Input

- `BetaManagedAgentsAgentToolset20260401WriteInput object { content, file_path }`

  Input payload for the `write` tool. Writes (overwriting) the
  entire file contents.

  - `content: string`

    Full file contents to write.

  - `file_path: string`

    Path of the file to write.

### Beta Managed Agents Always Allow Policy

- `BetaManagedAgentsAlwaysAllowPolicy object { type }`

  Tool calls are automatically approved without user confirmation.

  - `type: "always_allow"`

    - `"always_allow"`

### Beta Managed Agents Always Ask Policy

- `BetaManagedAgentsAlwaysAskPolicy object { type }`

  Tool calls require user confirmation before execution.

  - `type: "always_ask"`

    - `"always_ask"`

### Beta Managed Agents Anthropic Skill

- `BetaManagedAgentsAnthropicSkill object { skill_id, type, version }`

  A resolved Anthropic-managed skill.

  - `skill_id: string`

  - `type: "anthropic"`

    - `"anthropic"`

  - `version: string`

### Beta Managed Agents Anthropic Skill Params

- `BetaManagedAgentsAnthropicSkillParams object { skill_id, type, version }`

  An Anthropic-managed skill.

  - `skill_id: string`

    Identifier of the Anthropic skill (e.g., "xlsx").

  - `type: "anthropic"`

    - `"anthropic"`

  - `version: optional string`

    Version to pin. Defaults to latest if omitted.

### Beta Managed Agents Custom Skill

- `BetaManagedAgentsCustomSkill object { skill_id, type, version }`

  A resolved user-created custom skill.

  - `skill_id: string`

  - `type: "custom"`

    - `"custom"`

  - `version: string`

### Beta Managed Agents Custom Skill Params

- `BetaManagedAgentsCustomSkillParams object { skill_id, type, version }`

  A user-created custom skill.

  - `skill_id: string`

    Tagged ID of the custom skill (e.g., "skill_01XJ5...").

  - `type: "custom"`

    - `"custom"`

  - `version: optional string`

    Version to pin. Defaults to latest if omitted.

### Beta Managed Agents Custom Tool

- `BetaManagedAgentsCustomTool object { description, input_schema, name, type }`

  A custom tool as returned in API responses.

  - `description: string`

  - `input_schema: BetaManagedAgentsCustomToolInputSchema`

    JSON Schema for custom tool input parameters.

    - `type: "object"`

      - `"object"`

    - `properties: optional map[unknown]`

    - `required: optional array of string`

  - `name: string`

  - `type: "custom"`

    - `"custom"`

### Beta Managed Agents Custom Tool Input Schema

- `BetaManagedAgentsCustomToolInputSchema object { type, properties, required }`

  JSON Schema for custom tool input parameters.

  - `type: "object"`

    - `"object"`

  - `properties: optional map[unknown]`

  - `required: optional array of string`

### Beta Managed Agents Custom Tool Params

- `BetaManagedAgentsCustomToolParams object { description, input_schema, name, type }`

  A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

  - `description: string`

    Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

  - `input_schema: BetaManagedAgentsCustomToolInputSchema`

    JSON Schema for custom tool input parameters.

    - `type: "object"`

      - `"object"`

    - `properties: optional map[unknown]`

    - `required: optional array of string`

  - `name: string`

    Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

  - `type: "custom"`

    - `"custom"`

### Beta Managed Agents MCP Server URL Definition

- `BetaManagedAgentsMCPServerURLDefinition object { name, type, url }`

  URL-based MCP server connection as returned in API responses.

  - `name: string`

  - `type: "url"`

    - `"url"`

  - `url: string`

### Beta Managed Agents MCP Tool Config

- `BetaManagedAgentsMCPToolConfig object { enabled, name, permission_policy }`

  Resolved configuration for a specific MCP tool.

  - `enabled: boolean`

  - `name: string`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `BetaManagedAgentsAlwaysAskPolicy object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents MCP Tool Config Params

- `BetaManagedAgentsMCPToolConfigParams object { name, enabled, permission_policy }`

  Configuration override for a specific MCP tool.

  - `name: string`

    Name of the MCP tool to configure. 1-128 characters.

  - `enabled: optional boolean`

    Whether this tool is enabled. Overrides the `default_config` setting.

  - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `BetaManagedAgentsAlwaysAskPolicy object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents MCP Toolset

- `BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type }`

  - `configs: array of BetaManagedAgentsMCPToolConfig`

    - `enabled: boolean`

    - `name: string`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

        Tool calls are automatically approved without user confirmation.

        - `type: "always_allow"`

          - `"always_allow"`

      - `BetaManagedAgentsAlwaysAskPolicy object { type }`

        Tool calls require user confirmation before execution.

        - `type: "always_ask"`

          - `"always_ask"`

  - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

    Resolved default configuration for all tools from an MCP server.

    - `enabled: boolean`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

        Tool calls are automatically approved without user confirmation.

      - `BetaManagedAgentsAlwaysAskPolicy object { type }`

        Tool calls require user confirmation before execution.

  - `mcp_server_name: string`

  - `type: "mcp_toolset"`

    - `"mcp_toolset"`

### Beta Managed Agents MCP Toolset Default Config

- `BetaManagedAgentsMCPToolsetDefaultConfig object { enabled, permission_policy }`

  Resolved default configuration for all tools from an MCP server.

  - `enabled: boolean`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `BetaManagedAgentsAlwaysAskPolicy object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents MCP Toolset Default Config Params

- `BetaManagedAgentsMCPToolsetDefaultConfigParams object { enabled, permission_policy }`

  Default configuration for all tools from an MCP server.

  - `enabled: optional boolean`

    Whether tools are enabled by default. Defaults to true if not specified.

  - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `BetaManagedAgentsAlwaysAskPolicy object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents MCP Toolset Params

- `BetaManagedAgentsMCPToolsetParams object { mcp_server_name, type, configs, default_config }`

  Configuration for tools from an MCP server defined in `mcp_servers`.

  - `mcp_server_name: string`

    Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

  - `type: "mcp_toolset"`

    - `"mcp_toolset"`

  - `configs: optional array of BetaManagedAgentsMCPToolConfigParams`

    Per-tool configuration overrides.

    - `name: string`

      Name of the MCP tool to configure. 1-128 characters.

    - `enabled: optional boolean`

      Whether this tool is enabled. Overrides the `default_config` setting.

    - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

        Tool calls are automatically approved without user confirmation.

        - `type: "always_allow"`

          - `"always_allow"`

      - `BetaManagedAgentsAlwaysAskPolicy object { type }`

        Tool calls require user confirmation before execution.

        - `type: "always_ask"`

          - `"always_ask"`

  - `default_config: optional BetaManagedAgentsMCPToolsetDefaultConfigParams`

    Default configuration for all tools from an MCP server.

    - `enabled: optional boolean`

      Whether tools are enabled by default. Defaults to true if not specified.

    - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

        Tool calls are automatically approved without user confirmation.

      - `BetaManagedAgentsAlwaysAskPolicy object { type }`

        Tool calls require user confirmation before execution.

### Beta Managed Agents Model

- `BetaManagedAgentsModel = "claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more or string`

  The model that will power your agent.

  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `"claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

  - `string`

### Beta Managed Agents Model Config

- `BetaManagedAgentsModelConfig object { id, speed }`

  Model identifier and configuration.

  - `id: BetaManagedAgentsModel`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `"claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

    - `string`

  - `speed: optional "standard" or "fast"`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"`

    - `"fast"`

### Beta Managed Agents Model Config Params

- `BetaManagedAgentsModelConfigParams object { id, speed }`

  An object that defines additional configuration control over model use

  - `id: BetaManagedAgentsModel`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `"claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

    - `string`

  - `speed: optional "standard" or "fast"`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"`

    - `"fast"`

### Beta Managed Agents Multiagent Coordinator

- `BetaManagedAgentsMultiagentCoordinator object { agents, type }`

  Resolved coordinator topology with a concrete agent roster.

  - `agents: array of BetaManagedAgentsAgentReference`

    Agents the coordinator may spawn as session threads, each resolved to a specific version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `type: "coordinator"`

    - `"coordinator"`

### Beta Managed Agents Multiagent Coordinator Params

- `BetaManagedAgentsMultiagentCoordinatorParams object { agents, type }`

  A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

  - `agents: array of BetaManagedAgentsMultiagentRosterEntryParams`

    Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

    - `string`

    - `BetaManagedAgentsAgentParams object { id, type, version }`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `id: string`

        The `agent` ID.

      - `type: "agent"`

        - `"agent"`

      - `version: optional number`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

    - `BetaManagedAgentsMultiagentSelfParams object { type }`

      Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

      - `type: "self"`

        - `"self"`

  - `type: "coordinator"`

    - `"coordinator"`

### Beta Managed Agents Multiagent Self Params

- `BetaManagedAgentsMultiagentSelfParams object { type }`

  Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

  - `type: "self"`

    - `"self"`

### Beta Managed Agents Session Thread Agent

- `BetaManagedAgentsSessionThreadAgent object { id, description, mcp_servers, 7 more }`

  Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

  - `id: string`

  - `description: string`

  - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

    - `name: string`

    - `type: "url"`

      - `"url"`

    - `url: string`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

      - `string`

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `name: string`

  - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

    - `BetaManagedAgentsAnthropicSkill object { skill_id, type, version }`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

        - `"anthropic"`

      - `version: string`

    - `BetaManagedAgentsCustomSkill object { skill_id, type, version }`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

        - `"custom"`

      - `version: string`

  - `system: string`

  - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

    - `BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type }`

      - `configs: array of BetaManagedAgentsAgentToolConfig`

        - `enabled: boolean`

        - `name: "bash" or "edit" or "read" or 5 more`

          Built-in agent tool identifier.

          - `"bash"`

          - `"edit"`

          - `"read"`

          - `"write"`

          - `"glob"`

          - `"grep"`

          - `"web_fetch"`

          - `"web_search"`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

    - `BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type }`

      - `configs: array of BetaManagedAgentsMCPToolConfig`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

    - `BetaManagedAgentsCustomTool object { description, input_schema, name, type }`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: "object"`

          - `"object"`

        - `properties: optional map[unknown]`

        - `required: optional array of string`

      - `name: string`

      - `type: "custom"`

        - `"custom"`

  - `type: "agent"`

    - `"agent"`

  - `version: number`

### Beta Managed Agents Skill Params

- `BetaManagedAgentsSkillParams = BetaManagedAgentsAnthropicSkillParams or BetaManagedAgentsCustomSkillParams`

  Skill to load in the session container.

  - `BetaManagedAgentsAnthropicSkillParams object { skill_id, type, version }`

    An Anthropic-managed skill.

    - `skill_id: string`

      Identifier of the Anthropic skill (e.g., "xlsx").

    - `type: "anthropic"`

      - `"anthropic"`

    - `version: optional string`

      Version to pin. Defaults to latest if omitted.

  - `BetaManagedAgentsCustomSkillParams object { skill_id, type, version }`

    A user-created custom skill.

    - `skill_id: string`

      Tagged ID of the custom skill (e.g., "skill_01XJ5...").

    - `type: "custom"`

      - `"custom"`

    - `version: optional string`

      Version to pin. Defaults to latest if omitted.

### Beta Managed Agents URL MCP Server Params

- `BetaManagedAgentsURLMCPServerParams object { name, type, url }`

  URL-based MCP server connection.

  - `name: string`

    Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

  - `type: "url"`

    - `"url"`

  - `url: string`

    Endpoint URL for the MCP server.

# Versions

## List Agent Versions

**get** `/v1/agents/{agent_id}/versions`

List Agent Versions

### Path Parameters

- `agent_id: string`

### Query Parameters

- `limit: optional number`

  Maximum results per page. Default 20, maximum 100.

- `page: optional string`

  Opaque pagination cursor.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

### Returns

- `data: array of BetaManagedAgentsAgent`

  Agent versions.

  - `id: string`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

  - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

    - `name: string`

    - `type: "url"`

      - `"url"`

    - `url: string`

  - `metadata: map[string]`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

      - `string`

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `multiagent: BetaManagedAgentsMultiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: array of BetaManagedAgentsAgentReference`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `id: string`

      - `type: "agent"`

        - `"agent"`

      - `version: number`

    - `type: "coordinator"`

      - `"coordinator"`

  - `name: string`

  - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

    - `BetaManagedAgentsAnthropicSkill object { skill_id, type, version }`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

        - `"anthropic"`

      - `version: string`

    - `BetaManagedAgentsCustomSkill object { skill_id, type, version }`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

        - `"custom"`

      - `version: string`

  - `system: string`

  - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

    - `BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type }`

      - `configs: array of BetaManagedAgentsAgentToolConfig`

        - `enabled: boolean`

        - `name: "bash" or "edit" or "read" or 5 more`

          Built-in agent tool identifier.

          - `"bash"`

          - `"edit"`

          - `"read"`

          - `"write"`

          - `"glob"`

          - `"grep"`

          - `"web_fetch"`

          - `"web_search"`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

    - `BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type }`

      - `configs: array of BetaManagedAgentsMCPToolConfig`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy object { type }`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy object { type }`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

    - `BetaManagedAgentsCustomTool object { description, input_schema, name, type }`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: "object"`

          - `"object"`

        - `properties: optional map[unknown]`

        - `required: optional array of string`

      - `name: string`

      - `type: "custom"`

        - `"custom"`

  - `type: "agent"`

    - `"agent"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `version: number`

    The agent's current version. Starts at 1 and increments when the agent is modified.

- `next_page: optional string`

  Opaque cursor for the next page. Null when no more results.

### Example

```http
curl https://api.anthropic.com/v1/agents/$AGENT_ID/versions \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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
