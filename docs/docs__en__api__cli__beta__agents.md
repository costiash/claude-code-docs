# Agents

## Create

`$ ant beta:agents create`

**post** `/v1/agents`

Create Agent

### Parameters

- `--model: BetaManagedAgentsModelConfigParams`

  Body param: Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-4-6`, or a `model_config` object for additional configuration control

- `--name: string`

  Body param: Human-readable name for the agent. 1-256 characters.

- `--description: optional string`

  Body param: Description of what the agent does. Up to 2048 characters.

- `--mcp-server: optional array of BetaManagedAgentsURLMCPServerParams`

  Body param: MCP servers this agent connects to. Maximum 20. Names must be unique within the array.

- `--metadata: optional map[string]`

  Body param: Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `--skill: optional array of BetaManagedAgentsSkillParams`

  Body param: Skills available to the agent. Maximum 20.

- `--system: optional string`

  Body param: System prompt for the agent. Up to 100,000 characters.

- `--tool: optional array of BetaManagedAgentsAgentToolset20260401Params or BetaManagedAgentsMCPToolsetParams or BetaManagedAgentsCustomToolParams`

  Body param: Tool configurations available to the agent. Maximum of 128 tools across all toolsets allowed.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_agent: object { id, archived_at, created_at, 11 more }`

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

  - `model: object { id, speed }`

    Model identifier and configuration.

    - `id: "claude-opus-4-6" or "claude-sonnet-4-6" or "claude-haiku-4-5" or 5 more or string`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `name: string`

  - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

    - `beta_managed_agents_anthropic_skill: object { skill_id, type, version }`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

        - `"anthropic"`

      - `version: string`

    - `beta_managed_agents_custom_skill: object { skill_id, type, version }`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

        - `"custom"`

      - `version: string`

  - `system: string`

  - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

    - `beta_managed_agents_agent_toolset20260401: object { configs, default_config, type }`

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

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: object { enabled, permission_policy }`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

    - `beta_managed_agents_mcp_toolset: object { configs, default_config, mcp_server_name, type }`

      - `configs: array of BetaManagedAgentsMCPToolConfig`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: object { enabled, permission_policy }`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

    - `beta_managed_agents_custom_tool: object { description, input_schema, name, type }`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: object { properties, required, type }`

        JSON Schema for custom tool input parameters.

        - `properties: optional map[unknown]`

          JSON Schema properties defining the tool's input parameters.

        - `required: optional array of string`

          List of required property names.

        - `type: optional "object"`

          Must be 'object' for tool input schemas.

          - `"object"`

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

```cli
ant beta:agents create \
  --api-key my-anthropic-api-key \
  --model '{id: claude-opus-4-6}' \
  --name 'My First Agent'
```

## List

`$ ant beta:agents list`

**get** `/v1/agents`

List Agents

### Parameters

- `--created-at-gte: optional string`

  Query param: Return agents created at or after this time (inclusive).

- `--created-at-lte: optional string`

  Query param: Return agents created at or before this time (inclusive).

- `--include-archived: optional boolean`

  Query param: Include archived agents in results. Defaults to false.

- `--limit: optional number`

  Query param: Maximum results per page. Default 20, maximum 100.

- `--page: optional string`

  Query param: Opaque pagination cursor from a previous response.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsListAgents: object { data, next_page }`

  Paginated list of agents.

  - `data: optional array of BetaManagedAgentsAgent`

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

    - `model: object { id, speed }`

      Model identifier and configuration.

      - `id: "claude-opus-4-6" or "claude-sonnet-4-6" or "claude-haiku-4-5" or 5 more or string`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `name: string`

    - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

      - `beta_managed_agents_anthropic_skill: object { skill_id, type, version }`

        A resolved Anthropic-managed skill.

        - `skill_id: string`

        - `type: "anthropic"`

          - `"anthropic"`

        - `version: string`

      - `beta_managed_agents_custom_skill: object { skill_id, type, version }`

        A resolved user-created custom skill.

        - `skill_id: string`

        - `type: "custom"`

          - `"custom"`

        - `version: string`

    - `system: string`

    - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

      - `beta_managed_agents_agent_toolset20260401: object { configs, default_config, type }`

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

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `default_config: object { enabled, permission_policy }`

          Resolved default configuration for agent tools.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `type: "agent_toolset_20260401"`

          - `"agent_toolset_20260401"`

      - `beta_managed_agents_mcp_toolset: object { configs, default_config, mcp_server_name, type }`

        - `configs: array of BetaManagedAgentsMCPToolConfig`

          - `enabled: boolean`

          - `name: string`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `default_config: object { enabled, permission_policy }`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `mcp_server_name: string`

        - `type: "mcp_toolset"`

          - `"mcp_toolset"`

      - `beta_managed_agents_custom_tool: object { description, input_schema, name, type }`

        A custom tool as returned in API responses.

        - `description: string`

        - `input_schema: object { properties, required, type }`

          JSON Schema for custom tool input parameters.

          - `properties: optional map[unknown]`

            JSON Schema properties defining the tool's input parameters.

          - `required: optional array of string`

            List of required property names.

          - `type: optional "object"`

            Must be 'object' for tool input schemas.

            - `"object"`

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

```cli
ant beta:agents list \
  --api-key my-anthropic-api-key
```

## Retrieve

`$ ant beta:agents retrieve`

**get** `/v1/agents/{agent_id}`

Get Agent

### Parameters

- `--agent-id: string`

  Path param: Path parameter agent_id

- `--version: optional number`

  Query param: Agent version. Omit for the most recent version. Must be at least 1 if specified.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_agent: object { id, archived_at, created_at, 11 more }`

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

  - `model: object { id, speed }`

    Model identifier and configuration.

    - `id: "claude-opus-4-6" or "claude-sonnet-4-6" or "claude-haiku-4-5" or 5 more or string`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `name: string`

  - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

    - `beta_managed_agents_anthropic_skill: object { skill_id, type, version }`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

        - `"anthropic"`

      - `version: string`

    - `beta_managed_agents_custom_skill: object { skill_id, type, version }`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

        - `"custom"`

      - `version: string`

  - `system: string`

  - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

    - `beta_managed_agents_agent_toolset20260401: object { configs, default_config, type }`

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

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: object { enabled, permission_policy }`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

    - `beta_managed_agents_mcp_toolset: object { configs, default_config, mcp_server_name, type }`

      - `configs: array of BetaManagedAgentsMCPToolConfig`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: object { enabled, permission_policy }`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

    - `beta_managed_agents_custom_tool: object { description, input_schema, name, type }`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: object { properties, required, type }`

        JSON Schema for custom tool input parameters.

        - `properties: optional map[unknown]`

          JSON Schema properties defining the tool's input parameters.

        - `required: optional array of string`

          List of required property names.

        - `type: optional "object"`

          Must be 'object' for tool input schemas.

          - `"object"`

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

```cli
ant beta:agents retrieve \
  --api-key my-anthropic-api-key \
  --agent-id agent_011CZkYpogX7uDKUyvBTophP
```

## Update

`$ ant beta:agents update`

**post** `/v1/agents/{agent_id}`

Update Agent

### Parameters

- `--agent-id: string`

  Path param: Path parameter agent_id

- `--version: number`

  Body param: The agent's current version, used to prevent concurrent overwrites. Obtain this value from a create or retrieve response. The request fails if this does not match the server's current version.

- `--description: optional string`

  Body param: Description. Up to 2048 characters. Omit to preserve; send empty string or null to clear.

- `--mcp-server: optional array of BetaManagedAgentsURLMCPServerParams`

  Body param: MCP servers. Full replacement. Omit to preserve; send empty array or null to clear. Names must be unique. Maximum 20.

- `--metadata: optional map[string]`

  Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `--model: optional BetaManagedAgentsModelConfigParams`

  Body param: Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-4-6`, or a `model_config` object for additional configuration control. Omit to preserve. Cannot be cleared.

- `--name: optional string`

  Body param: Human-readable name. 1-256 characters. Omit to preserve. Cannot be cleared.

- `--skill: optional array of BetaManagedAgentsSkillParams`

  Body param: Skills. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 20.

- `--system: optional string`

  Body param: System prompt. Up to 100,000 characters. Omit to preserve; send empty string or null to clear.

- `--tool: optional array of BetaManagedAgentsAgentToolset20260401Params or BetaManagedAgentsMCPToolsetParams or BetaManagedAgentsCustomToolParams`

  Body param: Tool configurations available to the agent. Full replacement. Omit to preserve; send empty array or null to clear. Maximum of 128 tools across all toolsets allowed.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_agent: object { id, archived_at, created_at, 11 more }`

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

  - `model: object { id, speed }`

    Model identifier and configuration.

    - `id: "claude-opus-4-6" or "claude-sonnet-4-6" or "claude-haiku-4-5" or 5 more or string`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `name: string`

  - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

    - `beta_managed_agents_anthropic_skill: object { skill_id, type, version }`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

        - `"anthropic"`

      - `version: string`

    - `beta_managed_agents_custom_skill: object { skill_id, type, version }`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

        - `"custom"`

      - `version: string`

  - `system: string`

  - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

    - `beta_managed_agents_agent_toolset20260401: object { configs, default_config, type }`

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

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: object { enabled, permission_policy }`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

    - `beta_managed_agents_mcp_toolset: object { configs, default_config, mcp_server_name, type }`

      - `configs: array of BetaManagedAgentsMCPToolConfig`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: object { enabled, permission_policy }`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

    - `beta_managed_agents_custom_tool: object { description, input_schema, name, type }`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: object { properties, required, type }`

        JSON Schema for custom tool input parameters.

        - `properties: optional map[unknown]`

          JSON Schema properties defining the tool's input parameters.

        - `required: optional array of string`

          List of required property names.

        - `type: optional "object"`

          Must be 'object' for tool input schemas.

          - `"object"`

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

```cli
ant beta:agents update \
  --api-key my-anthropic-api-key \
  --agent-id agent_011CZkYpogX7uDKUyvBTophP \
  --version 1
```

## Archive

`$ ant beta:agents archive`

**post** `/v1/agents/{agent_id}/archive`

Archive Agent

### Parameters

- `--agent-id: string`

  Path parameter agent_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_agent: object { id, archived_at, created_at, 11 more }`

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

  - `model: object { id, speed }`

    Model identifier and configuration.

    - `id: "claude-opus-4-6" or "claude-sonnet-4-6" or "claude-haiku-4-5" or 5 more or string`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `name: string`

  - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

    - `beta_managed_agents_anthropic_skill: object { skill_id, type, version }`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

        - `"anthropic"`

      - `version: string`

    - `beta_managed_agents_custom_skill: object { skill_id, type, version }`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

        - `"custom"`

      - `version: string`

  - `system: string`

  - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

    - `beta_managed_agents_agent_toolset20260401: object { configs, default_config, type }`

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

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: object { enabled, permission_policy }`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

    - `beta_managed_agents_mcp_toolset: object { configs, default_config, mcp_server_name, type }`

      - `configs: array of BetaManagedAgentsMCPToolConfig`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: object { enabled, permission_policy }`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

    - `beta_managed_agents_custom_tool: object { description, input_schema, name, type }`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: object { properties, required, type }`

        JSON Schema for custom tool input parameters.

        - `properties: optional map[unknown]`

          JSON Schema properties defining the tool's input parameters.

        - `required: optional array of string`

          List of required property names.

        - `type: optional "object"`

          Must be 'object' for tool input schemas.

          - `"object"`

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

```cli
ant beta:agents archive \
  --api-key my-anthropic-api-key \
  --agent-id agent_011CZkYpogX7uDKUyvBTophP
```

## Domain Types

### Beta Managed Agents Agent

- `beta_managed_agents_agent: object { id, archived_at, created_at, 11 more }`

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

  - `model: object { id, speed }`

    Model identifier and configuration.

    - `id: "claude-opus-4-6" or "claude-sonnet-4-6" or "claude-haiku-4-5" or 5 more or string`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `name: string`

  - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

    - `beta_managed_agents_anthropic_skill: object { skill_id, type, version }`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

        - `"anthropic"`

      - `version: string`

    - `beta_managed_agents_custom_skill: object { skill_id, type, version }`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

        - `"custom"`

      - `version: string`

  - `system: string`

  - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

    - `beta_managed_agents_agent_toolset20260401: object { configs, default_config, type }`

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

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: object { enabled, permission_policy }`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

    - `beta_managed_agents_mcp_toolset: object { configs, default_config, mcp_server_name, type }`

      - `configs: array of BetaManagedAgentsMCPToolConfig`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: object { enabled, permission_policy }`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

    - `beta_managed_agents_custom_tool: object { description, input_schema, name, type }`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: object { properties, required, type }`

        JSON Schema for custom tool input parameters.

        - `properties: optional map[unknown]`

          JSON Schema properties defining the tool's input parameters.

        - `required: optional array of string`

          List of required property names.

        - `type: optional "object"`

          Must be 'object' for tool input schemas.

          - `"object"`

      - `name: string`

      - `type: "custom"`

        - `"custom"`

  - `type: "agent"`

    - `"agent"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `version: number`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Beta Managed Agents Agent Tool Config

- `beta_managed_agents_agent_tool_config: object { enabled, name, permission_policy }`

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

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents Agent Tool Config Params

- `beta_managed_agents_agent_tool_config_params: object { name, enabled, permission_policy }`

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

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents Agent Toolset Default Config

- `beta_managed_agents_agent_toolset_default_config: object { enabled, permission_policy }`

  Resolved default configuration for agent tools.

  - `enabled: boolean`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents Agent Toolset Default Config Params

- `beta_managed_agents_agent_toolset_default_config_params: object { enabled, permission_policy }`

  Default configuration for all tools in a toolset.

  - `enabled: optional boolean`

    Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

  - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents Agent Toolset20260401

- `beta_managed_agents_agent_toolset20260401: object { configs, default_config, type }`

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

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

        - `type: "always_allow"`

          - `"always_allow"`

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

        - `type: "always_ask"`

          - `"always_ask"`

  - `default_config: object { enabled, permission_policy }`

    Resolved default configuration for agent tools.

    - `enabled: boolean`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

        - `type: "always_allow"`

          - `"always_allow"`

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

        - `type: "always_ask"`

          - `"always_ask"`

  - `type: "agent_toolset_20260401"`

    - `"agent_toolset_20260401"`

### Beta Managed Agents Agent Toolset20260401 Params

- `beta_managed_agents_agent_toolset20260401_params: object { type, configs, default_config }`

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

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

        - `type: "always_allow"`

          - `"always_allow"`

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

        - `type: "always_ask"`

          - `"always_ask"`

  - `default_config: optional object { enabled, permission_policy }`

    Default configuration for all tools in a toolset.

    - `enabled: optional boolean`

      Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

    - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

        - `type: "always_allow"`

          - `"always_allow"`

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

        - `type: "always_ask"`

          - `"always_ask"`

### Beta Managed Agents Always Allow Policy

- `beta_managed_agents_always_allow_policy: object { type }`

  Tool calls are automatically approved without user confirmation.

  - `type: "always_allow"`

    - `"always_allow"`

### Beta Managed Agents Always Ask Policy

- `beta_managed_agents_always_ask_policy: object { type }`

  Tool calls require user confirmation before execution.

  - `type: "always_ask"`

    - `"always_ask"`

### Beta Managed Agents Anthropic Skill

- `beta_managed_agents_anthropic_skill: object { skill_id, type, version }`

  A resolved Anthropic-managed skill.

  - `skill_id: string`

  - `type: "anthropic"`

    - `"anthropic"`

  - `version: string`

### Beta Managed Agents Anthropic Skill Params

- `beta_managed_agents_anthropic_skill_params: object { skill_id, type, version }`

  An Anthropic-managed skill.

  - `skill_id: string`

    Identifier of the Anthropic skill (e.g., "xlsx").

  - `type: "anthropic"`

    - `"anthropic"`

  - `version: optional string`

    Version to pin. Defaults to latest if omitted.

### Beta Managed Agents Custom Skill

- `beta_managed_agents_custom_skill: object { skill_id, type, version }`

  A resolved user-created custom skill.

  - `skill_id: string`

  - `type: "custom"`

    - `"custom"`

  - `version: string`

### Beta Managed Agents Custom Skill Params

- `beta_managed_agents_custom_skill_params: object { skill_id, type, version }`

  A user-created custom skill.

  - `skill_id: string`

    Tagged ID of the custom skill (e.g., "skill_01XJ5...").

  - `type: "custom"`

    - `"custom"`

  - `version: optional string`

    Version to pin. Defaults to latest if omitted.

### Beta Managed Agents Custom Tool

- `beta_managed_agents_custom_tool: object { description, input_schema, name, type }`

  A custom tool as returned in API responses.

  - `description: string`

  - `input_schema: object { properties, required, type }`

    JSON Schema for custom tool input parameters.

    - `properties: optional map[unknown]`

      JSON Schema properties defining the tool's input parameters.

    - `required: optional array of string`

      List of required property names.

    - `type: optional "object"`

      Must be 'object' for tool input schemas.

      - `"object"`

  - `name: string`

  - `type: "custom"`

    - `"custom"`

### Beta Managed Agents Custom Tool Input Schema

- `beta_managed_agents_custom_tool_input_schema: object { properties, required, type }`

  JSON Schema for custom tool input parameters.

  - `properties: optional map[unknown]`

    JSON Schema properties defining the tool's input parameters.

  - `required: optional array of string`

    List of required property names.

  - `type: optional "object"`

    Must be 'object' for tool input schemas.

    - `"object"`

### Beta Managed Agents Custom Tool Params

- `beta_managed_agents_custom_tool_params: object { description, input_schema, name, type }`

  A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

  - `description: string`

    Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

  - `input_schema: object { properties, required, type }`

    JSON Schema for custom tool input parameters.

    - `properties: optional map[unknown]`

      JSON Schema properties defining the tool's input parameters.

    - `required: optional array of string`

      List of required property names.

    - `type: optional "object"`

      Must be 'object' for tool input schemas.

      - `"object"`

  - `name: string`

    Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

  - `type: "custom"`

    - `"custom"`

### Beta Managed Agents MCP Server URL Definition

- `beta_managed_agents_mcp_server_url_definition: object { name, type, url }`

  URL-based MCP server connection as returned in API responses.

  - `name: string`

  - `type: "url"`

    - `"url"`

  - `url: string`

### Beta Managed Agents MCP Tool Config

- `beta_managed_agents_mcp_tool_config: object { enabled, name, permission_policy }`

  Resolved configuration for a specific MCP tool.

  - `enabled: boolean`

  - `name: string`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents MCP Tool Config Params

- `beta_managed_agents_mcp_tool_config_params: object { name, enabled, permission_policy }`

  Configuration override for a specific MCP tool.

  - `name: string`

    Name of the MCP tool to configure. 1-128 characters.

  - `enabled: optional boolean`

    Whether this tool is enabled. Overrides the `default_config` setting.

  - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents MCP Toolset

- `beta_managed_agents_mcp_toolset: object { configs, default_config, mcp_server_name, type }`

  - `configs: array of BetaManagedAgentsMCPToolConfig`

    - `enabled: boolean`

    - `name: string`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

        - `type: "always_allow"`

          - `"always_allow"`

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

        - `type: "always_ask"`

          - `"always_ask"`

  - `default_config: object { enabled, permission_policy }`

    Resolved default configuration for all tools from an MCP server.

    - `enabled: boolean`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

        - `type: "always_allow"`

          - `"always_allow"`

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

        - `type: "always_ask"`

          - `"always_ask"`

  - `mcp_server_name: string`

  - `type: "mcp_toolset"`

    - `"mcp_toolset"`

### Beta Managed Agents MCP Toolset Default Config

- `beta_managed_agents_mcp_toolset_default_config: object { enabled, permission_policy }`

  Resolved default configuration for all tools from an MCP server.

  - `enabled: boolean`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents MCP Toolset Default Config Params

- `beta_managed_agents_mcp_toolset_default_config_params: object { enabled, permission_policy }`

  Default configuration for all tools from an MCP server.

  - `enabled: optional boolean`

    Whether tools are enabled by default. Defaults to true if not specified.

  - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents MCP Toolset Params

- `beta_managed_agents_mcp_toolset_params: object { mcp_server_name, type, configs, default_config }`

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

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

        - `type: "always_allow"`

          - `"always_allow"`

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

        - `type: "always_ask"`

          - `"always_ask"`

  - `default_config: optional object { enabled, permission_policy }`

    Default configuration for all tools from an MCP server.

    - `enabled: optional boolean`

      Whether tools are enabled by default. Defaults to true if not specified.

    - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

        - `type: "always_allow"`

          - `"always_allow"`

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

        - `type: "always_ask"`

          - `"always_ask"`

### Beta Managed Agents Model Config

- `beta_managed_agents_model_config: object { id, speed }`

  Model identifier and configuration.

  - `id: "claude-opus-4-6" or "claude-sonnet-4-6" or "claude-haiku-4-5" or 5 more or string`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

  - `speed: optional "standard" or "fast"`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"`

    - `"fast"`

### Beta Managed Agents Model Config Params

- `beta_managed_agents_model_config_params: object { id, speed }`

  An object that defines additional configuration control over model use

  - `id: "claude-opus-4-6" or "claude-sonnet-4-6" or "claude-haiku-4-5" or 5 more or string`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

  - `speed: optional "standard" or "fast"`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"`

    - `"fast"`

### Beta Managed Agents Skill Params

- `beta_managed_agents_skill_params: BetaManagedAgentsAnthropicSkillParams or BetaManagedAgentsCustomSkillParams`

  Skill to load in the session container.

  - `beta_managed_agents_anthropic_skill_params: object { skill_id, type, version }`

    An Anthropic-managed skill.

    - `skill_id: string`

      Identifier of the Anthropic skill (e.g., "xlsx").

    - `type: "anthropic"`

      - `"anthropic"`

    - `version: optional string`

      Version to pin. Defaults to latest if omitted.

  - `beta_managed_agents_custom_skill_params: object { skill_id, type, version }`

    A user-created custom skill.

    - `skill_id: string`

      Tagged ID of the custom skill (e.g., "skill_01XJ5...").

    - `type: "custom"`

      - `"custom"`

    - `version: optional string`

      Version to pin. Defaults to latest if omitted.

### Beta Managed Agents URL MCP Server Params

- `beta_managed_agents_url_mcp_server_params: object { name, type, url }`

  URL-based MCP server connection.

  - `name: string`

    Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

  - `type: "url"`

    - `"url"`

  - `url: string`

    Endpoint URL for the MCP server.

# Versions

## List

`$ ant beta:agents:versions list`

**get** `/v1/agents/{agent_id}/versions`

List Agent Versions

### Parameters

- `--agent-id: string`

  Path param: Path parameter agent_id

- `--limit: optional number`

  Query param: Maximum results per page. Default 20, maximum 100.

- `--page: optional string`

  Query param: Opaque pagination cursor.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsListAgentVersions: object { data, next_page }`

  Paginated list of agent versions.

  - `data: optional array of BetaManagedAgentsAgent`

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

    - `model: object { id, speed }`

      Model identifier and configuration.

      - `id: "claude-opus-4-6" or "claude-sonnet-4-6" or "claude-haiku-4-5" or 5 more or string`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `name: string`

    - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

      - `beta_managed_agents_anthropic_skill: object { skill_id, type, version }`

        A resolved Anthropic-managed skill.

        - `skill_id: string`

        - `type: "anthropic"`

          - `"anthropic"`

        - `version: string`

      - `beta_managed_agents_custom_skill: object { skill_id, type, version }`

        A resolved user-created custom skill.

        - `skill_id: string`

        - `type: "custom"`

          - `"custom"`

        - `version: string`

    - `system: string`

    - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

      - `beta_managed_agents_agent_toolset20260401: object { configs, default_config, type }`

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

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `default_config: object { enabled, permission_policy }`

          Resolved default configuration for agent tools.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `type: "agent_toolset_20260401"`

          - `"agent_toolset_20260401"`

      - `beta_managed_agents_mcp_toolset: object { configs, default_config, mcp_server_name, type }`

        - `configs: array of BetaManagedAgentsMCPToolConfig`

          - `enabled: boolean`

          - `name: string`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `default_config: object { enabled, permission_policy }`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `mcp_server_name: string`

        - `type: "mcp_toolset"`

          - `"mcp_toolset"`

      - `beta_managed_agents_custom_tool: object { description, input_schema, name, type }`

        A custom tool as returned in API responses.

        - `description: string`

        - `input_schema: object { properties, required, type }`

          JSON Schema for custom tool input parameters.

          - `properties: optional map[unknown]`

            JSON Schema properties defining the tool's input parameters.

          - `required: optional array of string`

            List of required property names.

          - `type: optional "object"`

            Must be 'object' for tool input schemas.

            - `"object"`

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

```cli
ant beta:agents:versions list \
  --api-key my-anthropic-api-key \
  --agent-id agent_011CZkYpogX7uDKUyvBTophP
```
