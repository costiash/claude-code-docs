# Agents

## Create Agent

`beta.agents.create(**kwargs) -> BetaManagedAgentsAgent`

**post** `/v1/agents`

Create Agent

### Parameters

- `model: BetaManagedAgentsModel | BetaManagedAgentsModelConfigParams`

  Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-4-6`, or a `model_config` object for additional configuration control

  - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-4-8" | 9 more | String`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-4-8" | 9 more`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `:"claude-sonnet-5"`

        High-performance model for coding and agents

      - `:"claude-fable-5"`

        Next generation of intelligence for the hardest knowledge work and coding problems

      - `:"claude-opus-4-8"`

        Frontier intelligence for long-running agents and coding

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

    - `String = String`

  - `class BetaManagedAgentsModelConfigParams`

    An object that defines additional configuration control over model use

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

- `name: String`

  Human-readable name for the agent.

- `description: String`

  Description of what the agent does.

- `mcp_servers: Array[BetaManagedAgentsURLMCPServerParams]`

  MCP servers this agent connects to. Maximum 20. Names must be unique within the array. Every server must be referenced by an `mcp_toolset` in `tools`; unreferenced servers are rejected. See the [MCP connector guide](https://platform.claude.com/docs/en/managed-agents/mcp-connector).

  - `name: String`

    Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

  - `type: :url`

    - `:url`

  - `url: String`

    Endpoint URL for the MCP server.

- `metadata: Hash[Symbol, String]`

  Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `multiagent: BetaManagedAgentsMultiagentParams`

  A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

  - `agents: Array[BetaManagedAgentsMultiagentRosterEntryParams]`

    Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

    - `String = String`

    - `class BetaManagedAgentsAgentParams`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `id: String`

        The `agent` ID.

      - `type: :agent`

        - `:agent`

      - `version: Integer`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

    - `class BetaManagedAgentsMultiagentSelfParams`

      Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

      - `type: :self`

        - `:self`

  - `type: :coordinator`

    - `:coordinator`

- `skills: Array[BetaManagedAgentsSkillParams]`

  Skills available to the agent.

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

  System prompt for the agent.

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

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

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

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

    - `default_config: BetaManagedAgentsMCPToolsetDefaultConfigParams`

      Default configuration for all tools from an MCP server.

      - `enabled: bool`

        Whether tools are enabled by default. Defaults to true if not specified.

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

  - `class BetaManagedAgentsCustomToolParams`

    A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

    - `description: String`

      Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-4096 characters.

    - `input_schema: BetaManagedAgentsCustomToolInputSchema`

      JSON Schema for custom tool input parameters.

      - `type: :object`

        - `:object`

      - `properties: Hash[Symbol, untyped]`

      - `required: Array[String]`

    - `name: String`

      Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

    - `type: :custom`

      - `:custom`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 26 more`

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

    - `:"user-profiles-2026-03-24"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"agent-memory-2026-07-22"`

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

      - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-4-8" | 9 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-sonnet-5"`

          High-performance model for coding and agents

        - `:"claude-fable-5"`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `:"claude-opus-4-8"`

          Frontier intelligence for long-running agents and coding

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

      - `String = String`

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `multiagent: BetaManagedAgentsMultiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: Array[BetaManagedAgentsAgentReference]`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `id: String`

      - `type: :agent`

        - `:agent`

      - `version: Integer`

    - `type: :coordinator`

      - `:coordinator`

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

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

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

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: String`

      - `type: :mcp_toolset`

        - `:mcp_toolset`

    - `class BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: String`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: :object`

          - `:object`

        - `properties: Hash[Symbol, untyped]`

        - `required: Array[String]`

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

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 26 more`

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

    - `:"user-profiles-2026-03-24"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"agent-memory-2026-07-22"`

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

      - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-4-8" | 9 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-sonnet-5"`

          High-performance model for coding and agents

        - `:"claude-fable-5"`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `:"claude-opus-4-8"`

          Frontier intelligence for long-running agents and coding

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

      - `String = String`

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `multiagent: BetaManagedAgentsMultiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: Array[BetaManagedAgentsAgentReference]`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `id: String`

      - `type: :agent`

        - `:agent`

      - `version: Integer`

    - `type: :coordinator`

      - `:coordinator`

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

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

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

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: String`

      - `type: :mcp_toolset`

        - `:mcp_toolset`

    - `class BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: String`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: :object`

          - `:object`

        - `properties: Hash[Symbol, untyped]`

        - `required: Array[String]`

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

`beta.agents.retrieve(agent_id, **kwargs) -> BetaManagedAgentsAgent`

**get** `/v1/agents/{agent_id}`

Get Agent

### Parameters

- `agent_id: String`

- `version: Integer`

  Agent version. Omit for the most recent version. Must be at least 1 if specified.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 26 more`

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

    - `:"user-profiles-2026-03-24"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"agent-memory-2026-07-22"`

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

      - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-4-8" | 9 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-sonnet-5"`

          High-performance model for coding and agents

        - `:"claude-fable-5"`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `:"claude-opus-4-8"`

          Frontier intelligence for long-running agents and coding

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

      - `String = String`

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `multiagent: BetaManagedAgentsMultiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: Array[BetaManagedAgentsAgentReference]`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `id: String`

      - `type: :agent`

        - `:agent`

      - `version: Integer`

    - `type: :coordinator`

      - `:coordinator`

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

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

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

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: String`

      - `type: :mcp_toolset`

        - `:mcp_toolset`

    - `class BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: String`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: :object`

          - `:object`

        - `properties: Hash[Symbol, untyped]`

        - `required: Array[String]`

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

`beta.agents.update(agent_id, **kwargs) -> BetaManagedAgentsAgent`

**post** `/v1/agents/{agent_id}`

Update Agent

### Parameters

- `agent_id: String`

- `version: Integer`

  The agent's current version, used to prevent concurrent overwrites. Obtain this value from a create or retrieve response. The request fails if this does not match the server's current version.

- `description: String`

  Description. Omit to preserve; send empty string or null to clear.

- `mcp_servers: Array[BetaManagedAgentsURLMCPServerParams]`

  MCP servers. Full replacement. Omit to preserve; send empty array or `null` to clear. Names must be unique. Maximum 20. Every server must be referenced by an `mcp_toolset` in the agent's resulting `tools`; unreferenced servers are rejected. See the [MCP connector guide](https://platform.claude.com/docs/en/managed-agents/mcp-connector).

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

  - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-4-8" | 9 more | String`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-4-8" | 9 more`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `:"claude-sonnet-5"`

        High-performance model for coding and agents

      - `:"claude-fable-5"`

        Next generation of intelligence for the hardest knowledge work and coding problems

      - `:"claude-opus-4-8"`

        Frontier intelligence for long-running agents and coding

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

    - `String = String`

  - `class BetaManagedAgentsModelConfigParams`

    An object that defines additional configuration control over model use

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

- `multiagent: BetaManagedAgentsMultiagentParams`

  A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

  - `agents: Array[BetaManagedAgentsMultiagentRosterEntryParams]`

    Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

    - `String = String`

    - `class BetaManagedAgentsAgentParams`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `id: String`

        The `agent` ID.

      - `type: :agent`

        - `:agent`

      - `version: Integer`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

    - `class BetaManagedAgentsMultiagentSelfParams`

      Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

      - `type: :self`

        - `:self`

  - `type: :coordinator`

    - `:coordinator`

- `name: String`

  Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

- `skills: Array[BetaManagedAgentsSkillParams]`

  Skills. Full replacement. Omit to preserve; send empty array or null to clear.

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

  System prompt. Omit to preserve; send empty string or null to clear.

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

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

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

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

    - `default_config: BetaManagedAgentsMCPToolsetDefaultConfigParams`

      Default configuration for all tools from an MCP server.

      - `enabled: bool`

        Whether tools are enabled by default. Defaults to true if not specified.

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

  - `class BetaManagedAgentsCustomToolParams`

    A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

    - `description: String`

      Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-4096 characters.

    - `input_schema: BetaManagedAgentsCustomToolInputSchema`

      JSON Schema for custom tool input parameters.

      - `type: :object`

        - `:object`

      - `properties: Hash[Symbol, untyped]`

      - `required: Array[String]`

    - `name: String`

      Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

    - `type: :custom`

      - `:custom`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 26 more`

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

    - `:"user-profiles-2026-03-24"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"agent-memory-2026-07-22"`

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

      - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-4-8" | 9 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-sonnet-5"`

          High-performance model for coding and agents

        - `:"claude-fable-5"`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `:"claude-opus-4-8"`

          Frontier intelligence for long-running agents and coding

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

      - `String = String`

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `multiagent: BetaManagedAgentsMultiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: Array[BetaManagedAgentsAgentReference]`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `id: String`

      - `type: :agent`

        - `:agent`

      - `version: Integer`

    - `type: :coordinator`

      - `:coordinator`

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

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

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

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: String`

      - `type: :mcp_toolset`

        - `:mcp_toolset`

    - `class BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: String`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: :object`

          - `:object`

        - `properties: Hash[Symbol, untyped]`

        - `required: Array[String]`

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

`beta.agents.archive(agent_id, **kwargs) -> BetaManagedAgentsAgent`

**post** `/v1/agents/{agent_id}/archive`

Archive Agent

### Parameters

- `agent_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 26 more`

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

    - `:"user-profiles-2026-03-24"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"agent-memory-2026-07-22"`

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

      - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-4-8" | 9 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-sonnet-5"`

          High-performance model for coding and agents

        - `:"claude-fable-5"`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `:"claude-opus-4-8"`

          Frontier intelligence for long-running agents and coding

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

      - `String = String`

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `multiagent: BetaManagedAgentsMultiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: Array[BetaManagedAgentsAgentReference]`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `id: String`

      - `type: :agent`

        - `:agent`

      - `version: Integer`

    - `type: :coordinator`

      - `:coordinator`

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

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

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

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: String`

      - `type: :mcp_toolset`

        - `:mcp_toolset`

    - `class BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: String`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: :object`

          - `:object`

        - `properties: Hash[Symbol, untyped]`

        - `required: Array[String]`

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

      - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-4-8" | 9 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-sonnet-5"`

          High-performance model for coding and agents

        - `:"claude-fable-5"`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `:"claude-opus-4-8"`

          Frontier intelligence for long-running agents and coding

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

      - `String = String`

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `multiagent: BetaManagedAgentsMultiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: Array[BetaManagedAgentsAgentReference]`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `id: String`

      - `type: :agent`

        - `:agent`

      - `version: Integer`

    - `type: :coordinator`

      - `:coordinator`

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

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

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

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: String`

      - `type: :mcp_toolset`

        - `:mcp_toolset`

    - `class BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: String`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: :object`

          - `:object`

        - `properties: Hash[Symbol, untyped]`

        - `required: Array[String]`

      - `name: String`

      - `type: :custom`

        - `:custom`

  - `type: :agent`

    - `:agent`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `version: Integer`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Beta Managed Agents Agent Reference

- `class BetaManagedAgentsAgentReference`

  A resolved agent reference with a concrete version.

  - `id: String`

  - `type: :agent`

    - `:agent`

  - `version: Integer`

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

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

  - `type: :agent_toolset_20260401`

    - `:agent_toolset_20260401`

### Beta Managed Agents Agent Toolset20260401 Bash Input

- `class BetaManagedAgentsAgentToolset20260401BashInput`

  Input payload for the `bash` tool of the
  `agent_toolset_20260401` toolset. All fields are optional;
  a normal invocation supplies `command`, while `restart=true`
  (with no `command`) reboots the runner-side bash session.

  - `command: String`

    Shell command to execute. Omit only when `restart` is true.

  - `restart: bool`

    When true, restart the persistent bash session instead of
    running a command. Subsequent calls without `restart` will
    run against the fresh session.

  - `timeout_ms: Integer`

    Per-call timeout in milliseconds. Defaults to the
    runner-wide tool timeout when omitted or zero.

### Beta Managed Agents Agent Toolset20260401 Edit Input

- `class BetaManagedAgentsAgentToolset20260401EditInput`

  Input payload for the `edit` tool. Performs a string
  replacement in the named file; by default `old_string` must
  occur exactly once.

  - `file_path: String`

    Path of the file to edit.

  - `new_string: String`

    Replacement text.

  - `old_string: String`

    Substring to find and replace.

  - `replace_all: bool`

    When true, replace every occurrence of `old_string`
    instead of requiring a unique match.

### Beta Managed Agents Agent Toolset20260401 Glob Input

- `class BetaManagedAgentsAgentToolset20260401GlobInput`

  Input payload for the `glob` tool. Returns paths matching a
  doublestar glob pattern, newest first.

  - `pattern: String`

    Doublestar glob pattern (e.g. `**/*.go`). Absolute patterns
    are only permitted when the runner is configured to allow
    them.

  - `path: String`

    Optional directory root to search under. Defaults to the
    runner's working directory.

### Beta Managed Agents Agent Toolset20260401 Grep Input

- `class BetaManagedAgentsAgentToolset20260401GrepInput`

  Input payload for the `grep` tool. Searches file contents for
  a regular expression, returning matching lines.

  - `pattern: String`

    Regular expression to search for.

  - `path: String`

    Optional directory root to search under. Defaults to the
    runner's working directory.

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

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

### Beta Managed Agents Agent Toolset20260401 Read Input

- `class BetaManagedAgentsAgentToolset20260401ReadInput`

  Input payload for the `read` tool. Reads file contents
  relative to the runner's working directory (or absolute when
  the runner permits).

  - `file_path: String`

    Path of the file to read.

  - `view_range: Array[Integer]`

    Optional `[start_line, end_line]` 1-indexed inclusive
    range. When omitted the entire file is returned.
    `end_line` of 0 or negative means "to end of file".

### Beta Managed Agents Agent Toolset20260401 Write Input

- `class BetaManagedAgentsAgentToolset20260401WriteInput`

  Input payload for the `write` tool. Writes (overwriting) the
  entire file contents.

  - `content: String`

    Full file contents to write.

  - `file_path: String`

    Path of the file to write.

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

    - `type: :object`

      - `:object`

    - `properties: Hash[Symbol, untyped]`

    - `required: Array[String]`

  - `name: String`

  - `type: :custom`

    - `:custom`

### Beta Managed Agents Custom Tool Input Schema

- `class BetaManagedAgentsCustomToolInputSchema`

  JSON Schema for custom tool input parameters.

  - `type: :object`

    - `:object`

  - `properties: Hash[Symbol, untyped]`

  - `required: Array[String]`

### Beta Managed Agents Custom Tool Params

- `class BetaManagedAgentsCustomToolParams`

  A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

  - `description: String`

    Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-4096 characters.

  - `input_schema: BetaManagedAgentsCustomToolInputSchema`

    JSON Schema for custom tool input parameters.

    - `type: :object`

      - `:object`

    - `properties: Hash[Symbol, untyped]`

    - `required: Array[String]`

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

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

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

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

### Beta Managed Agents Model

- `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-4-8" | 9 more | String`

  The model that will power your agent.

  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-4-8" | 9 more`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `:"claude-sonnet-5"`

      High-performance model for coding and agents

    - `:"claude-fable-5"`

      Next generation of intelligence for the hardest knowledge work and coding problems

    - `:"claude-opus-4-8"`

      Frontier intelligence for long-running agents and coding

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

  - `String = String`

### Beta Managed Agents Model Config

- `class BetaManagedAgentsModelConfig`

  Model identifier and configuration.

  - `id: BetaManagedAgentsModel`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-4-8" | 9 more`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `:"claude-sonnet-5"`

        High-performance model for coding and agents

      - `:"claude-fable-5"`

        Next generation of intelligence for the hardest knowledge work and coding problems

      - `:"claude-opus-4-8"`

        Frontier intelligence for long-running agents and coding

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

    - `String = String`

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

    - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-4-8" | 9 more`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `:"claude-sonnet-5"`

        High-performance model for coding and agents

      - `:"claude-fable-5"`

        Next generation of intelligence for the hardest knowledge work and coding problems

      - `:"claude-opus-4-8"`

        Frontier intelligence for long-running agents and coding

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

    - `String = String`

  - `speed: :standard | :fast`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `:standard`

    - `:fast`

### Beta Managed Agents Multiagent Coordinator

- `class BetaManagedAgentsMultiagentCoordinator`

  Resolved coordinator topology with a concrete agent roster.

  - `agents: Array[BetaManagedAgentsAgentReference]`

    Agents the coordinator may spawn as session threads, each resolved to a specific version.

    - `id: String`

    - `type: :agent`

      - `:agent`

    - `version: Integer`

  - `type: :coordinator`

    - `:coordinator`

### Beta Managed Agents Multiagent Coordinator Params

- `class BetaManagedAgentsMultiagentCoordinatorParams`

  A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

  - `agents: Array[BetaManagedAgentsMultiagentRosterEntryParams]`

    Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

    - `String = String`

    - `class BetaManagedAgentsAgentParams`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `id: String`

        The `agent` ID.

      - `type: :agent`

        - `:agent`

      - `version: Integer`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

    - `class BetaManagedAgentsMultiagentSelfParams`

      Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

      - `type: :self`

        - `:self`

  - `type: :coordinator`

    - `:coordinator`

### Beta Managed Agents Multiagent Self Params

- `class BetaManagedAgentsMultiagentSelfParams`

  Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

  - `type: :self`

    - `:self`

### Beta Managed Agents Session Thread Agent

- `class BetaManagedAgentsSessionThreadAgent`

  Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

  - `id: String`

  - `description: String`

  - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

    - `name: String`

    - `type: :url`

      - `:url`

    - `url: String`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-4-8" | 9 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-sonnet-5"`

          High-performance model for coding and agents

        - `:"claude-fable-5"`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `:"claude-opus-4-8"`

          Frontier intelligence for long-running agents and coding

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

      - `String = String`

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

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

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

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: String`

      - `type: :mcp_toolset`

        - `:mcp_toolset`

    - `class BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: String`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: :object`

          - `:object`

        - `properties: Hash[Symbol, untyped]`

        - `required: Array[String]`

      - `name: String`

      - `type: :custom`

        - `:custom`

  - `type: :agent`

    - `:agent`

  - `version: Integer`

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

## List Agent Versions

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

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 26 more`

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

    - `:"user-profiles-2026-03-24"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"agent-memory-2026-07-22"`

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

      - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-4-8" | 9 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-sonnet-5"`

          High-performance model for coding and agents

        - `:"claude-fable-5"`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `:"claude-opus-4-8"`

          Frontier intelligence for long-running agents and coding

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

      - `String = String`

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `multiagent: BetaManagedAgentsMultiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: Array[BetaManagedAgentsAgentReference]`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `id: String`

      - `type: :agent`

        - `:agent`

      - `version: Integer`

    - `type: :coordinator`

      - `:coordinator`

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

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

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

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: String`

      - `type: :mcp_toolset`

        - `:mcp_toolset`

    - `class BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: String`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: :object`

          - `:object`

        - `properties: Hash[Symbol, untyped]`

        - `required: Array[String]`

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
