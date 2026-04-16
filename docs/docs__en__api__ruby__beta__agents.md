# Agents

## Create

`beta.agents.create(**kwargs) -> BetaManagedAgentsAgent`

**post** `/v1/agents`

Create Agent

### Parameters

- `model: BetaManagedAgentsModel | BetaManagedAgentsModelConfigParams`

  Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-4-6`, or a `model_config` object for additional configuration control

  - `BetaManagedAgentsModel = :"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more | String`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `:"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `:"claude-opus-4-7"`

        Frontier intelligence for long-running agents and coding

      - `:"claude-opus-4-6"`

        Most intelligent model for building agents and coding

      - `:"claude-sonnet-4-6"`

        Best combination of speed and intelligence

      - `:"claude-haiku-4-5"`

        Fastest model with near-frontier intelligence

      - `:"claude-haiku-4-5-20251001"`

        Fastest model with near-frontier intelligence

      - `:"claude-opus-4-5"`

        Premium model combining maximum intelligence with practical performance

      - `:"claude-opus-4-5-20251101"`

        Premium model combining maximum intelligence with practical performance

      - `:"claude-sonnet-4-5"`

        High-performance model for agents and coding

      - `:"claude-sonnet-4-5-20250929"`

        High-performance model for agents and coding

    - `String`

  - `class BetaManagedAgentsModelConfigParams`

    An object that defines additional configuration control over model use

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `:"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-opus-4-7"`

          Frontier intelligence for long-running agents and coding

        - `:"claude-opus-4-6"`

          Most intelligent model for building agents and coding

        - `:"claude-sonnet-4-6"`

          Best combination of speed and intelligence

        - `:"claude-haiku-4-5"`

          Fastest model with near-frontier intelligence

        - `:"claude-haiku-4-5-20251001"`

          Fastest model with near-frontier intelligence

        - `:"claude-opus-4-5"`

          Premium model combining maximum intelligence with practical performance

        - `:"claude-opus-4-5-20251101"`

          Premium model combining maximum intelligence with practical performance

        - `:"claude-sonnet-4-5"`

          High-performance model for agents and coding

        - `:"claude-sonnet-4-5-20250929"`

          High-performance model for agents and coding

      - `String`

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

- `name: String`

  Human-readable name for the agent. 1-256 characters.

- `description: String`

  Description of what the agent does. Up to 2048 characters.

- `mcp_servers: Array[BetaManagedAgentsURLMCPServerParams]`

  MCP servers this agent connects to. Maximum 20. Names must be unique within the array.

  - `name: String`

    Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

  - `type: :url`

    - `:url`

  - `url: String`

    Endpoint URL for the MCP server.

- `metadata: Hash[Symbol, String]`

  Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `skills: Array[BetaManagedAgentsSkillParams]`

  Skills available to the agent. Maximum 20.

  - `class BetaManagedAgentsAnthropicSkillParams`

    An Anthropic-managed skill.

    - `skill_id: String`

      Identifier of the Anthropic skill (e.g., "xlsx").

    - `type: :anthropic`

      - `:anthropic`

    - `version: String`

      Version to pin. Defaults to latest if omitted.

  - `class BetaManagedAgentsCustomSkillParams`

    A user-created custom skill.

    - `skill_id: String`

      Tagged ID of the custom skill (e.g., "skill_01XJ5...").

    - `type: :custom`

      - `:custom`

    - `version: String`

      Version to pin. Defaults to latest if omitted.

- `system_: String`

  System prompt for the agent. Up to 100,000 characters.

- `tools: Array[BetaManagedAgentsAgentToolset20260401Params | BetaManagedAgentsMCPToolsetParams | BetaManagedAgentsCustomToolParams]`

  Tool configurations available to the agent. Maximum of 128 tools across all toolsets allowed.

  - `class BetaManagedAgentsAgentToolset20260401Params`

    Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

    - `type: :agent_toolset_20260401`

      - `:agent_toolset_20260401`

    - `configs: Array[BetaManagedAgentsAgentToolConfigParams]`

      Per-tool configuration overrides.

      - `name: :bash | :edit | :read | 5 more`

        Built-in agent tool identifier.

        - `:bash`

        - `:edit`

        - `:read`

        - `:write`

        - `:glob`

        - `:grep`

        - `:web_fetch`

        - `:web_search`

      - `enabled: bool`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

          - `type: :always_allow`

            - `:always_allow`

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

          - `type: :always_ask`

            - `:always_ask`

    - `default_config: BetaManagedAgentsAgentToolsetDefaultConfigParams`

      Default configuration for all tools in a toolset.

      - `enabled: bool`

        Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

          - `type: :always_allow`

            - `:always_allow`

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

          - `type: :always_ask`

            - `:always_ask`

  - `class BetaManagedAgentsMCPToolsetParams`

    Configuration for tools from an MCP server defined in `mcp_servers`.

    - `mcp_server_name: String`

      Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

    - `type: :mcp_toolset`

      - `:mcp_toolset`

    - `configs: Array[BetaManagedAgentsMCPToolConfigParams]`

      Per-tool configuration overrides.

      - `name: String`

        Name of the MCP tool to configure. 1-128 characters.

      - `enabled: bool`

        Whether this tool is enabled. Overrides the `default_config` setting.

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

          - `type: :always_allow`

            - `:always_allow`

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

          - `type: :always_ask`

            - `:always_ask`

    - `default_config: BetaManagedAgentsMCPToolsetDefaultConfigParams`

      Default configuration for all tools from an MCP server.

      - `enabled: bool`

        Whether tools are enabled by default. Defaults to true if not specified.

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

          - `type: :always_allow`

            - `:always_allow`

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

          - `type: :always_ask`

            - `:always_ask`

  - `class BetaManagedAgentsCustomToolParams`

    A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

    - `description: String`

      Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

    - `input_schema: BetaManagedAgentsCustomToolInputSchema`

      JSON Schema for custom tool input parameters.

      - `properties: Hash[Symbol, untyped]`

        JSON Schema properties defining the tool's input parameters.

      - `required: Array[String]`

        List of required property names.

      - `type: :object`

        Must be 'object' for tool input schemas.

        - `:object`

    - `name: String`

      Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

    - `type: :custom`

      - `:custom`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 20 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"advisor-tool-2026-03-01"`

    - `:"user-profiles-2026-03-24"`

### Returns

- `class BetaManagedAgentsAgent`

  A Managed Agents `agent`.

  - `id: String`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `description: String`

  - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

    - `name: String`

    - `type: :url`

      - `:url`

    - `url: String`

  - `metadata: Hash[Symbol, String]`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `:"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-opus-4-7"`

          Frontier intelligence for long-running agents and coding

        - `:"claude-opus-4-6"`

          Most intelligent model for building agents and coding

        - `:"claude-sonnet-4-6"`

          Best combination of speed and intelligence

        - `:"claude-haiku-4-5"`

          Fastest model with near-frontier intelligence

        - `:"claude-haiku-4-5-20251001"`

          Fastest model with near-frontier intelligence

        - `:"claude-opus-4-5"`

          Premium model combining maximum intelligence with practical performance

        - `:"claude-opus-4-5-20251101"`

          Premium model combining maximum intelligence with practical performance

        - `:"claude-sonnet-4-5"`

          High-performance model for agents and coding

        - `:"claude-sonnet-4-5-20250929"`

          High-performance model for agents and coding

      - `String`

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `name: String`

  - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

    - `class BetaManagedAgentsAnthropicSkill`

      A resolved Anthropic-managed skill.

      - `skill_id: String`

      - `type: :anthropic`

        - `:anthropic`

      - `version: String`

    - `class BetaManagedAgentsCustomSkill`

      A resolved user-created custom skill.

      - `skill_id: String`

      - `type: :custom`

        - `:custom`

      - `version: String`

  - `system_: String`

  - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

    - `class BetaManagedAgentsAgentToolset20260401`

      - `configs: Array[BetaManagedAgentsAgentToolConfig]`

        - `enabled: bool`

        - `name: :bash | :edit | :read | 5 more`

          Built-in agent tool identifier.

          - `:bash`

          - `:edit`

          - `:read`

          - `:write`

          - `:glob`

          - `:grep`

          - `:web_fetch`

          - `:web_search`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `type: :agent_toolset_20260401`

        - `:agent_toolset_20260401`

    - `class BetaManagedAgentsMCPToolset`

      - `configs: Array[BetaManagedAgentsMCPToolConfig]`

        - `enabled: bool`

        - `name: String`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `mcp_server_name: String`

      - `type: :mcp_toolset`

        - `:mcp_toolset`

    - `class BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: String`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `properties: Hash[Symbol, untyped]`

          JSON Schema properties defining the tool's input parameters.

        - `required: Array[String]`

          List of required property names.

        - `type: :object`

          Must be 'object' for tool input schemas.

          - `:object`

      - `name: String`

      - `type: :custom`

        - `:custom`

  - `type: :agent`

    - `:agent`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `version: Integer`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_agent = anthropic.beta.agents.create(model: :"claude-sonnet-4-6", name: "My First Agent")

puts(beta_managed_agents_agent)
```

## List

`beta.agents.list(**kwargs) -> PageCursor<BetaManagedAgentsAgent>`

**get** `/v1/agents`

List Agents

### Parameters

- `created_at_gte: Time`

  Return agents created at or after this time (inclusive).

- `created_at_lte: Time`

  Return agents created at or before this time (inclusive).

- `include_archived: bool`

  Include archived agents in results. Defaults to false.

- `limit: Integer`

  Maximum results per page. Default 20, maximum 100.

- `page: String`

  Opaque pagination cursor from a previous response.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 20 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"advisor-tool-2026-03-01"`

    - `:"user-profiles-2026-03-24"`

### Returns

- `class BetaManagedAgentsAgent`

  A Managed Agents `agent`.

  - `id: String`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `description: String`

  - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

    - `name: String`

    - `type: :url`

      - `:url`

    - `url: String`

  - `metadata: Hash[Symbol, String]`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `:"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-opus-4-7"`

          Frontier intelligence for long-running agents and coding

        - `:"claude-opus-4-6"`

          Most intelligent model for building agents and coding

        - `:"claude-sonnet-4-6"`

          Best combination of speed and intelligence

        - `:"claude-haiku-4-5"`

          Fastest model with near-frontier intelligence

        - `:"claude-haiku-4-5-20251001"`

          Fastest model with near-frontier intelligence

        - `:"claude-opus-4-5"`

          Premium model combining maximum intelligence with practical performance

        - `:"claude-opus-4-5-20251101"`

          Premium model combining maximum intelligence with practical performance

        - `:"claude-sonnet-4-5"`

          High-performance model for agents and coding

        - `:"claude-sonnet-4-5-20250929"`

          High-performance model for agents and coding

      - `String`

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `name: String`

  - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

    - `class BetaManagedAgentsAnthropicSkill`

      A resolved Anthropic-managed skill.

      - `skill_id: String`

      - `type: :anthropic`

        - `:anthropic`

      - `version: String`

    - `class BetaManagedAgentsCustomSkill`

      A resolved user-created custom skill.

      - `skill_id: String`

      - `type: :custom`

        - `:custom`

      - `version: String`

  - `system_: String`

  - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

    - `class BetaManagedAgentsAgentToolset20260401`

      - `configs: Array[BetaManagedAgentsAgentToolConfig]`

        - `enabled: bool`

        - `name: :bash | :edit | :read | 5 more`

          Built-in agent tool identifier.

          - `:bash`

          - `:edit`

          - `:read`

          - `:write`

          - `:glob`

          - `:grep`

          - `:web_fetch`

          - `:web_search`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `type: :agent_toolset_20260401`

        - `:agent_toolset_20260401`

    - `class BetaManagedAgentsMCPToolset`

      - `configs: Array[BetaManagedAgentsMCPToolConfig]`

        - `enabled: bool`

        - `name: String`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `mcp_server_name: String`

      - `type: :mcp_toolset`

        - `:mcp_toolset`

    - `class BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: String`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `properties: Hash[Symbol, untyped]`

          JSON Schema properties defining the tool's input parameters.

        - `required: Array[String]`

          List of required property names.

        - `type: :object`

          Must be 'object' for tool input schemas.

          - `:object`

      - `name: String`

      - `type: :custom`

        - `:custom`

  - `type: :agent`

    - `:agent`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `version: Integer`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.agents.list

puts(page)
```

## Retrieve

`beta.agents.retrieve(agent_id, **kwargs) -> BetaManagedAgentsAgent`

**get** `/v1/agents/{agent_id}`

Get Agent

### Parameters

- `agent_id: String`

- `version: Integer`

  Agent version. Omit for the most recent version. Must be at least 1 if specified.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 20 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"advisor-tool-2026-03-01"`

    - `:"user-profiles-2026-03-24"`

### Returns

- `class BetaManagedAgentsAgent`

  A Managed Agents `agent`.

  - `id: String`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `description: String`

  - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

    - `name: String`

    - `type: :url`

      - `:url`

    - `url: String`

  - `metadata: Hash[Symbol, String]`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `:"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-opus-4-7"`

          Frontier intelligence for long-running agents and coding

        - `:"claude-opus-4-6"`

          Most intelligent model for building agents and coding

        - `:"claude-sonnet-4-6"`

          Best combination of speed and intelligence

        - `:"claude-haiku-4-5"`

          Fastest model with near-frontier intelligence

        - `:"claude-haiku-4-5-20251001"`

          Fastest model with near-frontier intelligence

        - `:"claude-opus-4-5"`

          Premium model combining maximum intelligence with practical performance

        - `:"claude-opus-4-5-20251101"`

          Premium model combining maximum intelligence with practical performance

        - `:"claude-sonnet-4-5"`

          High-performance model for agents and coding

        - `:"claude-sonnet-4-5-20250929"`

          High-performance model for agents and coding

      - `String`

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `name: String`

  - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

    - `class BetaManagedAgentsAnthropicSkill`

      A resolved Anthropic-managed skill.

      - `skill_id: String`

      - `type: :anthropic`

        - `:anthropic`

      - `version: String`

    - `class BetaManagedAgentsCustomSkill`

      A resolved user-created custom skill.

      - `skill_id: String`

      - `type: :custom`

        - `:custom`

      - `version: String`

  - `system_: String`

  - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

    - `class BetaManagedAgentsAgentToolset20260401`

      - `configs: Array[BetaManagedAgentsAgentToolConfig]`

        - `enabled: bool`

        - `name: :bash | :edit | :read | 5 more`

          Built-in agent tool identifier.

          - `:bash`

          - `:edit`

          - `:read`

          - `:write`

          - `:glob`

          - `:grep`

          - `:web_fetch`

          - `:web_search`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `type: :agent_toolset_20260401`

        - `:agent_toolset_20260401`

    - `class BetaManagedAgentsMCPToolset`

      - `configs: Array[BetaManagedAgentsMCPToolConfig]`

        - `enabled: bool`

        - `name: String`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `mcp_server_name: String`

      - `type: :mcp_toolset`

        - `:mcp_toolset`

    - `class BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: String`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `properties: Hash[Symbol, untyped]`

          JSON Schema properties defining the tool's input parameters.

        - `required: Array[String]`

          List of required property names.

        - `type: :object`

          Must be 'object' for tool input schemas.

          - `:object`

      - `name: String`

      - `type: :custom`

        - `:custom`

  - `type: :agent`

    - `:agent`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `version: Integer`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_agent = anthropic.beta.agents.retrieve("agent_011CZkYpogX7uDKUyvBTophP")

puts(beta_managed_agents_agent)
```

## Update

`beta.agents.update(agent_id, **kwargs) -> BetaManagedAgentsAgent`

**post** `/v1/agents/{agent_id}`

Update Agent

### Parameters

- `agent_id: String`

- `version: Integer`

  The agent's current version, used to prevent concurrent overwrites. Obtain this value from a create or retrieve response. The request fails if this does not match the server's current version.

- `description: String`

  Description. Up to 2048 characters. Omit to preserve; send empty string or null to clear.

- `mcp_servers: Array[BetaManagedAgentsURLMCPServerParams]`

  MCP servers. Full replacement. Omit to preserve; send empty array or null to clear. Names must be unique. Maximum 20.

  - `name: String`

    Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

  - `type: :url`

    - `:url`

  - `url: String`

    Endpoint URL for the MCP server.

- `metadata: Hash[Symbol, String]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `model: BetaManagedAgentsModel | BetaManagedAgentsModelConfigParams`

  Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-4-6`, or a `model_config` object for additional configuration control. Omit to preserve. Cannot be cleared.

  - `BetaManagedAgentsModel = :"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more | String`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `:"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `:"claude-opus-4-7"`

        Frontier intelligence for long-running agents and coding

      - `:"claude-opus-4-6"`

        Most intelligent model for building agents and coding

      - `:"claude-sonnet-4-6"`

        Best combination of speed and intelligence

      - `:"claude-haiku-4-5"`

        Fastest model with near-frontier intelligence

      - `:"claude-haiku-4-5-20251001"`

        Fastest model with near-frontier intelligence

      - `:"claude-opus-4-5"`

        Premium model combining maximum intelligence with practical performance

      - `:"claude-opus-4-5-20251101"`

        Premium model combining maximum intelligence with practical performance

      - `:"claude-sonnet-4-5"`

        High-performance model for agents and coding

      - `:"claude-sonnet-4-5-20250929"`

        High-performance model for agents and coding

    - `String`

  - `class BetaManagedAgentsModelConfigParams`

    An object that defines additional configuration control over model use

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `:"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-opus-4-7"`

          Frontier intelligence for long-running agents and coding

        - `:"claude-opus-4-6"`

          Most intelligent model for building agents and coding

        - `:"claude-sonnet-4-6"`

          Best combination of speed and intelligence

        - `:"claude-haiku-4-5"`

          Fastest model with near-frontier intelligence

        - `:"claude-haiku-4-5-20251001"`

          Fastest model with near-frontier intelligence

        - `:"claude-opus-4-5"`

          Premium model combining maximum intelligence with practical performance

        - `:"claude-opus-4-5-20251101"`

          Premium model combining maximum intelligence with practical performance

        - `:"claude-sonnet-4-5"`

          High-performance model for agents and coding

        - `:"claude-sonnet-4-5-20250929"`

          High-performance model for agents and coding

      - `String`

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

- `name: String`

  Human-readable name. 1-256 characters. Omit to preserve. Cannot be cleared.

- `skills: Array[BetaManagedAgentsSkillParams]`

  Skills. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 20.

  - `class BetaManagedAgentsAnthropicSkillParams`

    An Anthropic-managed skill.

    - `skill_id: String`

      Identifier of the Anthropic skill (e.g., "xlsx").

    - `type: :anthropic`

      - `:anthropic`

    - `version: String`

      Version to pin. Defaults to latest if omitted.

  - `class BetaManagedAgentsCustomSkillParams`

    A user-created custom skill.

    - `skill_id: String`

      Tagged ID of the custom skill (e.g., "skill_01XJ5...").

    - `type: :custom`

      - `:custom`

    - `version: String`

      Version to pin. Defaults to latest if omitted.

- `system_: String`

  System prompt. Up to 100,000 characters. Omit to preserve; send empty string or null to clear.

- `tools: Array[BetaManagedAgentsAgentToolset20260401Params | BetaManagedAgentsMCPToolsetParams | BetaManagedAgentsCustomToolParams]`

  Tool configurations available to the agent. Full replacement. Omit to preserve; send empty array or null to clear. Maximum of 128 tools across all toolsets allowed.

  - `class BetaManagedAgentsAgentToolset20260401Params`

    Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

    - `type: :agent_toolset_20260401`

      - `:agent_toolset_20260401`

    - `configs: Array[BetaManagedAgentsAgentToolConfigParams]`

      Per-tool configuration overrides.

      - `name: :bash | :edit | :read | 5 more`

        Built-in agent tool identifier.

        - `:bash`

        - `:edit`

        - `:read`

        - `:write`

        - `:glob`

        - `:grep`

        - `:web_fetch`

        - `:web_search`

      - `enabled: bool`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

          - `type: :always_allow`

            - `:always_allow`

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

          - `type: :always_ask`

            - `:always_ask`

    - `default_config: BetaManagedAgentsAgentToolsetDefaultConfigParams`

      Default configuration for all tools in a toolset.

      - `enabled: bool`

        Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

          - `type: :always_allow`

            - `:always_allow`

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

          - `type: :always_ask`

            - `:always_ask`

  - `class BetaManagedAgentsMCPToolsetParams`

    Configuration for tools from an MCP server defined in `mcp_servers`.

    - `mcp_server_name: String`

      Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

    - `type: :mcp_toolset`

      - `:mcp_toolset`

    - `configs: Array[BetaManagedAgentsMCPToolConfigParams]`

      Per-tool configuration overrides.

      - `name: String`

        Name of the MCP tool to configure. 1-128 characters.

      - `enabled: bool`

        Whether this tool is enabled. Overrides the `default_config` setting.

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

          - `type: :always_allow`

            - `:always_allow`

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

          - `type: :always_ask`

            - `:always_ask`

    - `default_config: BetaManagedAgentsMCPToolsetDefaultConfigParams`

      Default configuration for all tools from an MCP server.

      - `enabled: bool`

        Whether tools are enabled by default. Defaults to true if not specified.

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

          - `type: :always_allow`

            - `:always_allow`

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

          - `type: :always_ask`

            - `:always_ask`

  - `class BetaManagedAgentsCustomToolParams`

    A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

    - `description: String`

      Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

    - `input_schema: BetaManagedAgentsCustomToolInputSchema`

      JSON Schema for custom tool input parameters.

      - `properties: Hash[Symbol, untyped]`

        JSON Schema properties defining the tool's input parameters.

      - `required: Array[String]`

        List of required property names.

      - `type: :object`

        Must be 'object' for tool input schemas.

        - `:object`

    - `name: String`

      Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

    - `type: :custom`

      - `:custom`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 20 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"advisor-tool-2026-03-01"`

    - `:"user-profiles-2026-03-24"`

### Returns

- `class BetaManagedAgentsAgent`

  A Managed Agents `agent`.

  - `id: String`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `description: String`

  - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

    - `name: String`

    - `type: :url`

      - `:url`

    - `url: String`

  - `metadata: Hash[Symbol, String]`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `:"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-opus-4-7"`

          Frontier intelligence for long-running agents and coding

        - `:"claude-opus-4-6"`

          Most intelligent model for building agents and coding

        - `:"claude-sonnet-4-6"`

          Best combination of speed and intelligence

        - `:"claude-haiku-4-5"`

          Fastest model with near-frontier intelligence

        - `:"claude-haiku-4-5-20251001"`

          Fastest model with near-frontier intelligence

        - `:"claude-opus-4-5"`

          Premium model combining maximum intelligence with practical performance

        - `:"claude-opus-4-5-20251101"`

          Premium model combining maximum intelligence with practical performance

        - `:"claude-sonnet-4-5"`

          High-performance model for agents and coding

        - `:"claude-sonnet-4-5-20250929"`

          High-performance model for agents and coding

      - `String`

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `name: String`

  - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

    - `class BetaManagedAgentsAnthropicSkill`

      A resolved Anthropic-managed skill.

      - `skill_id: String`

      - `type: :anthropic`

        - `:anthropic`

      - `version: String`

    - `class BetaManagedAgentsCustomSkill`

      A resolved user-created custom skill.

      - `skill_id: String`

      - `type: :custom`

        - `:custom`

      - `version: String`

  - `system_: String`

  - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

    - `class BetaManagedAgentsAgentToolset20260401`

      - `configs: Array[BetaManagedAgentsAgentToolConfig]`

        - `enabled: bool`

        - `name: :bash | :edit | :read | 5 more`

          Built-in agent tool identifier.

          - `:bash`

          - `:edit`

          - `:read`

          - `:write`

          - `:glob`

          - `:grep`

          - `:web_fetch`

          - `:web_search`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `type: :agent_toolset_20260401`

        - `:agent_toolset_20260401`

    - `class BetaManagedAgentsMCPToolset`

      - `configs: Array[BetaManagedAgentsMCPToolConfig]`

        - `enabled: bool`

        - `name: String`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `mcp_server_name: String`

      - `type: :mcp_toolset`

        - `:mcp_toolset`

    - `class BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: String`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `properties: Hash[Symbol, untyped]`

          JSON Schema properties defining the tool's input parameters.

        - `required: Array[String]`

          List of required property names.

        - `type: :object`

          Must be 'object' for tool input schemas.

          - `:object`

      - `name: String`

      - `type: :custom`

        - `:custom`

  - `type: :agent`

    - `:agent`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `version: Integer`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_agent = anthropic.beta.agents.update("agent_011CZkYpogX7uDKUyvBTophP", version: 1)

puts(beta_managed_agents_agent)
```

## Archive

`beta.agents.archive(agent_id, **kwargs) -> BetaManagedAgentsAgent`

**post** `/v1/agents/{agent_id}/archive`

Archive Agent

### Parameters

- `agent_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 20 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"advisor-tool-2026-03-01"`

    - `:"user-profiles-2026-03-24"`

### Returns

- `class BetaManagedAgentsAgent`

  A Managed Agents `agent`.

  - `id: String`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `description: String`

  - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

    - `name: String`

    - `type: :url`

      - `:url`

    - `url: String`

  - `metadata: Hash[Symbol, String]`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `:"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-opus-4-7"`

          Frontier intelligence for long-running agents and coding

        - `:"claude-opus-4-6"`

          Most intelligent model for building agents and coding

        - `:"claude-sonnet-4-6"`

          Best combination of speed and intelligence

        - `:"claude-haiku-4-5"`

          Fastest model with near-frontier intelligence

        - `:"claude-haiku-4-5-20251001"`

          Fastest model with near-frontier intelligence

        - `:"claude-opus-4-5"`

          Premium model combining maximum intelligence with practical performance

        - `:"claude-opus-4-5-20251101"`

          Premium model combining maximum intelligence with practical performance

        - `:"claude-sonnet-4-5"`

          High-performance model for agents and coding

        - `:"claude-sonnet-4-5-20250929"`

          High-performance model for agents and coding

      - `String`

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `name: String`

  - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

    - `class BetaManagedAgentsAnthropicSkill`

      A resolved Anthropic-managed skill.

      - `skill_id: String`

      - `type: :anthropic`

        - `:anthropic`

      - `version: String`

    - `class BetaManagedAgentsCustomSkill`

      A resolved user-created custom skill.

      - `skill_id: String`

      - `type: :custom`

        - `:custom`

      - `version: String`

  - `system_: String`

  - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

    - `class BetaManagedAgentsAgentToolset20260401`

      - `configs: Array[BetaManagedAgentsAgentToolConfig]`

        - `enabled: bool`

        - `name: :bash | :edit | :read | 5 more`

          Built-in agent tool identifier.

          - `:bash`

          - `:edit`

          - `:read`

          - `:write`

          - `:glob`

          - `:grep`

          - `:web_fetch`

          - `:web_search`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `type: :agent_toolset_20260401`

        - `:agent_toolset_20260401`

    - `class BetaManagedAgentsMCPToolset`

      - `configs: Array[BetaManagedAgentsMCPToolConfig]`

        - `enabled: bool`

        - `name: String`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `mcp_server_name: String`

      - `type: :mcp_toolset`

        - `:mcp_toolset`

    - `class BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: String`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `properties: Hash[Symbol, untyped]`

          JSON Schema properties defining the tool's input parameters.

        - `required: Array[String]`

          List of required property names.

        - `type: :object`

          Must be 'object' for tool input schemas.

          - `:object`

      - `name: String`

      - `type: :custom`

        - `:custom`

  - `type: :agent`

    - `:agent`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `version: Integer`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_agent = anthropic.beta.agents.archive("agent_011CZkYpogX7uDKUyvBTophP")

puts(beta_managed_agents_agent)
```

## Domain Types

### Beta Managed Agents Agent

- `class BetaManagedAgentsAgent`

  A Managed Agents `agent`.

  - `id: String`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `description: String`

  - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

    - `name: String`

    - `type: :url`

      - `:url`

    - `url: String`

  - `metadata: Hash[Symbol, String]`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `:"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-opus-4-7"`

          Frontier intelligence for long-running agents and coding

        - `:"claude-opus-4-6"`

          Most intelligent model for building agents and coding

        - `:"claude-sonnet-4-6"`

          Best combination of speed and intelligence

        - `:"claude-haiku-4-5"`

          Fastest model with near-frontier intelligence

        - `:"claude-haiku-4-5-20251001"`

          Fastest model with near-frontier intelligence

        - `:"claude-opus-4-5"`

          Premium model combining maximum intelligence with practical performance

        - `:"claude-opus-4-5-20251101"`

          Premium model combining maximum intelligence with practical performance

        - `:"claude-sonnet-4-5"`

          High-performance model for agents and coding

        - `:"claude-sonnet-4-5-20250929"`

          High-performance model for agents and coding

      - `String`

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `name: String`

  - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

    - `class BetaManagedAgentsAnthropicSkill`

      A resolved Anthropic-managed skill.

      - `skill_id: String`

      - `type: :anthropic`

        - `:anthropic`

      - `version: String`

    - `class BetaManagedAgentsCustomSkill`

      A resolved user-created custom skill.

      - `skill_id: String`

      - `type: :custom`

        - `:custom`

      - `version: String`

  - `system_: String`

  - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

    - `class BetaManagedAgentsAgentToolset20260401`

      - `configs: Array[BetaManagedAgentsAgentToolConfig]`

        - `enabled: bool`

        - `name: :bash | :edit | :read | 5 more`

          Built-in agent tool identifier.

          - `:bash`

          - `:edit`

          - `:read`

          - `:write`

          - `:glob`

          - `:grep`

          - `:web_fetch`

          - `:web_search`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `type: :agent_toolset_20260401`

        - `:agent_toolset_20260401`

    - `class BetaManagedAgentsMCPToolset`

      - `configs: Array[BetaManagedAgentsMCPToolConfig]`

        - `enabled: bool`

        - `name: String`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `mcp_server_name: String`

      - `type: :mcp_toolset`

        - `:mcp_toolset`

    - `class BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: String`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `properties: Hash[Symbol, untyped]`

          JSON Schema properties defining the tool's input parameters.

        - `required: Array[String]`

          List of required property names.

        - `type: :object`

          Must be 'object' for tool input schemas.

          - `:object`

      - `name: String`

      - `type: :custom`

        - `:custom`

  - `type: :agent`

    - `:agent`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `version: Integer`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Beta Managed Agents Agent Tool Config

- `class BetaManagedAgentsAgentToolConfig`

  Configuration for a specific agent tool.

  - `enabled: bool`

  - `name: :bash | :edit | :read | 5 more`

    Built-in agent tool identifier.

    - `:bash`

    - `:edit`

    - `:read`

    - `:write`

    - `:glob`

    - `:grep`

    - `:web_fetch`

    - `:web_search`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

        - `:always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

        - `:always_ask`

### Beta Managed Agents Agent Tool Config Params

- `class BetaManagedAgentsAgentToolConfigParams`

  Configuration override for a specific tool within a toolset.

  - `name: :bash | :edit | :read | 5 more`

    Built-in agent tool identifier.

    - `:bash`

    - `:edit`

    - `:read`

    - `:write`

    - `:glob`

    - `:grep`

    - `:web_fetch`

    - `:web_search`

  - `enabled: bool`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

        - `:always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

        - `:always_ask`

### Beta Managed Agents Agent Toolset Default Config

- `class BetaManagedAgentsAgentToolsetDefaultConfig`

  Resolved default configuration for agent tools.

  - `enabled: bool`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

        - `:always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

        - `:always_ask`

### Beta Managed Agents Agent Toolset Default Config Params

- `class BetaManagedAgentsAgentToolsetDefaultConfigParams`

  Default configuration for all tools in a toolset.

  - `enabled: bool`

    Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

        - `:always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

        - `:always_ask`

### Beta Managed Agents Agent Toolset20260401

- `class BetaManagedAgentsAgentToolset20260401`

  - `configs: Array[BetaManagedAgentsAgentToolConfig]`

    - `enabled: bool`

    - `name: :bash | :edit | :read | 5 more`

      Built-in agent tool identifier.

      - `:bash`

      - `:edit`

      - `:read`

      - `:write`

      - `:glob`

      - `:grep`

      - `:web_fetch`

      - `:web_search`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

        - `type: :always_allow`

          - `:always_allow`

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

        - `type: :always_ask`

          - `:always_ask`

  - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

    Resolved default configuration for agent tools.

    - `enabled: bool`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

        - `type: :always_allow`

          - `:always_allow`

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

        - `type: :always_ask`

          - `:always_ask`

  - `type: :agent_toolset_20260401`

    - `:agent_toolset_20260401`

### Beta Managed Agents Agent Toolset20260401 Params

- `class BetaManagedAgentsAgentToolset20260401Params`

  Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

  - `type: :agent_toolset_20260401`

    - `:agent_toolset_20260401`

  - `configs: Array[BetaManagedAgentsAgentToolConfigParams]`

    Per-tool configuration overrides.

    - `name: :bash | :edit | :read | 5 more`

      Built-in agent tool identifier.

      - `:bash`

      - `:edit`

      - `:read`

      - `:write`

      - `:glob`

      - `:grep`

      - `:web_fetch`

      - `:web_search`

    - `enabled: bool`

      Whether this tool is enabled and available to Claude. Overrides the default_config setting.

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

        - `type: :always_allow`

          - `:always_allow`

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

        - `type: :always_ask`

          - `:always_ask`

  - `default_config: BetaManagedAgentsAgentToolsetDefaultConfigParams`

    Default configuration for all tools in a toolset.

    - `enabled: bool`

      Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

        - `type: :always_allow`

          - `:always_allow`

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

        - `type: :always_ask`

          - `:always_ask`

### Beta Managed Agents Always Allow Policy

- `class BetaManagedAgentsAlwaysAllowPolicy`

  Tool calls are automatically approved without user confirmation.

  - `type: :always_allow`

    - `:always_allow`

### Beta Managed Agents Always Ask Policy

- `class BetaManagedAgentsAlwaysAskPolicy`

  Tool calls require user confirmation before execution.

  - `type: :always_ask`

    - `:always_ask`

### Beta Managed Agents Anthropic Skill

- `class BetaManagedAgentsAnthropicSkill`

  A resolved Anthropic-managed skill.

  - `skill_id: String`

  - `type: :anthropic`

    - `:anthropic`

  - `version: String`

### Beta Managed Agents Anthropic Skill Params

- `class BetaManagedAgentsAnthropicSkillParams`

  An Anthropic-managed skill.

  - `skill_id: String`

    Identifier of the Anthropic skill (e.g., "xlsx").

  - `type: :anthropic`

    - `:anthropic`

  - `version: String`

    Version to pin. Defaults to latest if omitted.

### Beta Managed Agents Custom Skill

- `class BetaManagedAgentsCustomSkill`

  A resolved user-created custom skill.

  - `skill_id: String`

  - `type: :custom`

    - `:custom`

  - `version: String`

### Beta Managed Agents Custom Skill Params

- `class BetaManagedAgentsCustomSkillParams`

  A user-created custom skill.

  - `skill_id: String`

    Tagged ID of the custom skill (e.g., "skill_01XJ5...").

  - `type: :custom`

    - `:custom`

  - `version: String`

    Version to pin. Defaults to latest if omitted.

### Beta Managed Agents Custom Tool

- `class BetaManagedAgentsCustomTool`

  A custom tool as returned in API responses.

  - `description: String`

  - `input_schema: BetaManagedAgentsCustomToolInputSchema`

    JSON Schema for custom tool input parameters.

    - `properties: Hash[Symbol, untyped]`

      JSON Schema properties defining the tool's input parameters.

    - `required: Array[String]`

      List of required property names.

    - `type: :object`

      Must be 'object' for tool input schemas.

      - `:object`

  - `name: String`

  - `type: :custom`

    - `:custom`

### Beta Managed Agents Custom Tool Input Schema

- `class BetaManagedAgentsCustomToolInputSchema`

  JSON Schema for custom tool input parameters.

  - `properties: Hash[Symbol, untyped]`

    JSON Schema properties defining the tool's input parameters.

  - `required: Array[String]`

    List of required property names.

  - `type: :object`

    Must be 'object' for tool input schemas.

    - `:object`

### Beta Managed Agents Custom Tool Params

- `class BetaManagedAgentsCustomToolParams`

  A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

  - `description: String`

    Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

  - `input_schema: BetaManagedAgentsCustomToolInputSchema`

    JSON Schema for custom tool input parameters.

    - `properties: Hash[Symbol, untyped]`

      JSON Schema properties defining the tool's input parameters.

    - `required: Array[String]`

      List of required property names.

    - `type: :object`

      Must be 'object' for tool input schemas.

      - `:object`

  - `name: String`

    Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

  - `type: :custom`

    - `:custom`

### Beta Managed Agents MCP Server URL Definition

- `class BetaManagedAgentsMCPServerURLDefinition`

  URL-based MCP server connection as returned in API responses.

  - `name: String`

  - `type: :url`

    - `:url`

  - `url: String`

### Beta Managed Agents MCP Tool Config

- `class BetaManagedAgentsMCPToolConfig`

  Resolved configuration for a specific MCP tool.

  - `enabled: bool`

  - `name: String`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

        - `:always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

        - `:always_ask`

### Beta Managed Agents MCP Tool Config Params

- `class BetaManagedAgentsMCPToolConfigParams`

  Configuration override for a specific MCP tool.

  - `name: String`

    Name of the MCP tool to configure. 1-128 characters.

  - `enabled: bool`

    Whether this tool is enabled. Overrides the `default_config` setting.

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

        - `:always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

        - `:always_ask`

### Beta Managed Agents MCP Toolset

- `class BetaManagedAgentsMCPToolset`

  - `configs: Array[BetaManagedAgentsMCPToolConfig]`

    - `enabled: bool`

    - `name: String`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

        - `type: :always_allow`

          - `:always_allow`

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

        - `type: :always_ask`

          - `:always_ask`

  - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

    Resolved default configuration for all tools from an MCP server.

    - `enabled: bool`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

        - `type: :always_allow`

          - `:always_allow`

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

        - `type: :always_ask`

          - `:always_ask`

  - `mcp_server_name: String`

  - `type: :mcp_toolset`

    - `:mcp_toolset`

### Beta Managed Agents MCP Toolset Default Config

- `class BetaManagedAgentsMCPToolsetDefaultConfig`

  Resolved default configuration for all tools from an MCP server.

  - `enabled: bool`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

        - `:always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

        - `:always_ask`

### Beta Managed Agents MCP Toolset Default Config Params

- `class BetaManagedAgentsMCPToolsetDefaultConfigParams`

  Default configuration for all tools from an MCP server.

  - `enabled: bool`

    Whether tools are enabled by default. Defaults to true if not specified.

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

        - `:always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

        - `:always_ask`

### Beta Managed Agents MCP Toolset Params

- `class BetaManagedAgentsMCPToolsetParams`

  Configuration for tools from an MCP server defined in `mcp_servers`.

  - `mcp_server_name: String`

    Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

  - `type: :mcp_toolset`

    - `:mcp_toolset`

  - `configs: Array[BetaManagedAgentsMCPToolConfigParams]`

    Per-tool configuration overrides.

    - `name: String`

      Name of the MCP tool to configure. 1-128 characters.

    - `enabled: bool`

      Whether this tool is enabled. Overrides the `default_config` setting.

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

        - `type: :always_allow`

          - `:always_allow`

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

        - `type: :always_ask`

          - `:always_ask`

  - `default_config: BetaManagedAgentsMCPToolsetDefaultConfigParams`

    Default configuration for all tools from an MCP server.

    - `enabled: bool`

      Whether tools are enabled by default. Defaults to true if not specified.

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

        - `type: :always_allow`

          - `:always_allow`

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

        - `type: :always_ask`

          - `:always_ask`

### Beta Managed Agents Model

- `BetaManagedAgentsModel = :"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more | String`

  The model that will power your agent.

  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `:"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `:"claude-opus-4-7"`

      Frontier intelligence for long-running agents and coding

    - `:"claude-opus-4-6"`

      Most intelligent model for building agents and coding

    - `:"claude-sonnet-4-6"`

      Best combination of speed and intelligence

    - `:"claude-haiku-4-5"`

      Fastest model with near-frontier intelligence

    - `:"claude-haiku-4-5-20251001"`

      Fastest model with near-frontier intelligence

    - `:"claude-opus-4-5"`

      Premium model combining maximum intelligence with practical performance

    - `:"claude-opus-4-5-20251101"`

      Premium model combining maximum intelligence with practical performance

    - `:"claude-sonnet-4-5"`

      High-performance model for agents and coding

    - `:"claude-sonnet-4-5-20250929"`

      High-performance model for agents and coding

  - `String`

### Beta Managed Agents Model Config

- `class BetaManagedAgentsModelConfig`

  Model identifier and configuration.

  - `id: BetaManagedAgentsModel`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `:"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `:"claude-opus-4-7"`

        Frontier intelligence for long-running agents and coding

      - `:"claude-opus-4-6"`

        Most intelligent model for building agents and coding

      - `:"claude-sonnet-4-6"`

        Best combination of speed and intelligence

      - `:"claude-haiku-4-5"`

        Fastest model with near-frontier intelligence

      - `:"claude-haiku-4-5-20251001"`

        Fastest model with near-frontier intelligence

      - `:"claude-opus-4-5"`

        Premium model combining maximum intelligence with practical performance

      - `:"claude-opus-4-5-20251101"`

        Premium model combining maximum intelligence with practical performance

      - `:"claude-sonnet-4-5"`

        High-performance model for agents and coding

      - `:"claude-sonnet-4-5-20250929"`

        High-performance model for agents and coding

    - `String`

  - `speed: :standard | :fast`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `:standard`

    - `:fast`

### Beta Managed Agents Model Config Params

- `class BetaManagedAgentsModelConfigParams`

  An object that defines additional configuration control over model use

  - `id: BetaManagedAgentsModel`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `:"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `:"claude-opus-4-7"`

        Frontier intelligence for long-running agents and coding

      - `:"claude-opus-4-6"`

        Most intelligent model for building agents and coding

      - `:"claude-sonnet-4-6"`

        Best combination of speed and intelligence

      - `:"claude-haiku-4-5"`

        Fastest model with near-frontier intelligence

      - `:"claude-haiku-4-5-20251001"`

        Fastest model with near-frontier intelligence

      - `:"claude-opus-4-5"`

        Premium model combining maximum intelligence with practical performance

      - `:"claude-opus-4-5-20251101"`

        Premium model combining maximum intelligence with practical performance

      - `:"claude-sonnet-4-5"`

        High-performance model for agents and coding

      - `:"claude-sonnet-4-5-20250929"`

        High-performance model for agents and coding

    - `String`

  - `speed: :standard | :fast`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `:standard`

    - `:fast`

### Beta Managed Agents Skill Params

- `BetaManagedAgentsSkillParams = BetaManagedAgentsAnthropicSkillParams | BetaManagedAgentsCustomSkillParams`

  Skill to load in the session container.

  - `class BetaManagedAgentsAnthropicSkillParams`

    An Anthropic-managed skill.

    - `skill_id: String`

      Identifier of the Anthropic skill (e.g., "xlsx").

    - `type: :anthropic`

      - `:anthropic`

    - `version: String`

      Version to pin. Defaults to latest if omitted.

  - `class BetaManagedAgentsCustomSkillParams`

    A user-created custom skill.

    - `skill_id: String`

      Tagged ID of the custom skill (e.g., "skill_01XJ5...").

    - `type: :custom`

      - `:custom`

    - `version: String`

      Version to pin. Defaults to latest if omitted.

### Beta Managed Agents URL MCP Server Params

- `class BetaManagedAgentsURLMCPServerParams`

  URL-based MCP server connection.

  - `name: String`

    Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

  - `type: :url`

    - `:url`

  - `url: String`

    Endpoint URL for the MCP server.

# Versions

## List

`beta.agents.versions.list(agent_id, **kwargs) -> PageCursor<BetaManagedAgentsAgent>`

**get** `/v1/agents/{agent_id}/versions`

List Agent Versions

### Parameters

- `agent_id: String`

- `limit: Integer`

  Maximum results per page. Default 20, maximum 100.

- `page: String`

  Opaque pagination cursor.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 20 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"advisor-tool-2026-03-01"`

    - `:"user-profiles-2026-03-24"`

### Returns

- `class BetaManagedAgentsAgent`

  A Managed Agents `agent`.

  - `id: String`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `description: String`

  - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

    - `name: String`

    - `type: :url`

      - `:url`

    - `url: String`

  - `metadata: Hash[Symbol, String]`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `:"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-opus-4-7"`

          Frontier intelligence for long-running agents and coding

        - `:"claude-opus-4-6"`

          Most intelligent model for building agents and coding

        - `:"claude-sonnet-4-6"`

          Best combination of speed and intelligence

        - `:"claude-haiku-4-5"`

          Fastest model with near-frontier intelligence

        - `:"claude-haiku-4-5-20251001"`

          Fastest model with near-frontier intelligence

        - `:"claude-opus-4-5"`

          Premium model combining maximum intelligence with practical performance

        - `:"claude-opus-4-5-20251101"`

          Premium model combining maximum intelligence with practical performance

        - `:"claude-sonnet-4-5"`

          High-performance model for agents and coding

        - `:"claude-sonnet-4-5-20250929"`

          High-performance model for agents and coding

      - `String`

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `name: String`

  - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

    - `class BetaManagedAgentsAnthropicSkill`

      A resolved Anthropic-managed skill.

      - `skill_id: String`

      - `type: :anthropic`

        - `:anthropic`

      - `version: String`

    - `class BetaManagedAgentsCustomSkill`

      A resolved user-created custom skill.

      - `skill_id: String`

      - `type: :custom`

        - `:custom`

      - `version: String`

  - `system_: String`

  - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

    - `class BetaManagedAgentsAgentToolset20260401`

      - `configs: Array[BetaManagedAgentsAgentToolConfig]`

        - `enabled: bool`

        - `name: :bash | :edit | :read | 5 more`

          Built-in agent tool identifier.

          - `:bash`

          - `:edit`

          - `:read`

          - `:write`

          - `:glob`

          - `:grep`

          - `:web_fetch`

          - `:web_search`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `type: :agent_toolset_20260401`

        - `:agent_toolset_20260401`

    - `class BetaManagedAgentsMCPToolset`

      - `configs: Array[BetaManagedAgentsMCPToolConfig]`

        - `enabled: bool`

        - `name: String`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `mcp_server_name: String`

      - `type: :mcp_toolset`

        - `:mcp_toolset`

    - `class BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: String`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `properties: Hash[Symbol, untyped]`

          JSON Schema properties defining the tool's input parameters.

        - `required: Array[String]`

          List of required property names.

        - `type: :object`

          Must be 'object' for tool input schemas.

          - `:object`

      - `name: String`

      - `type: :custom`

        - `:custom`

  - `type: :agent`

    - `:agent`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `version: Integer`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.agents.versions.list("agent_011CZkYpogX7uDKUyvBTophP")

puts(page)
```
