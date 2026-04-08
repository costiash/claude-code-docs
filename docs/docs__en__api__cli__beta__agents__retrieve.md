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
