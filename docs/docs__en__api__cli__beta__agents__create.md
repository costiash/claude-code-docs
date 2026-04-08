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
