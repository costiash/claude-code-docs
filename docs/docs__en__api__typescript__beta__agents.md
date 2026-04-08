# Agents

## Create

`client.beta.agents.create(AgentCreateParamsparams, RequestOptionsoptions?): BetaManagedAgentsAgent`

**post** `/v1/agents`

Create Agent

### Parameters

- `params: AgentCreateParams`

  - `model: BetaManagedAgentsModel | BetaManagedAgentsModelConfigParams`

    Body param: Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-4-6`, or a `model_config` object for additional configuration control

    - `BetaManagedAgentsModel = "claude-opus-4-6" | "claude-sonnet-4-6" | "claude-haiku-4-5" | 5 more | (string & {})`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-haiku-4-5" | 5 more`

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

      - `(string & {})`

    - `BetaManagedAgentsModelConfigParams`

      An object that defines additional configuration control over model use

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-haiku-4-5" | 5 more`

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

        - `(string & {})`

      - `speed?: "standard" | "fast" | null`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `name: string`

    Body param: Human-readable name for the agent. 1-256 characters.

  - `description?: string | null`

    Body param: Description of what the agent does. Up to 2048 characters.

  - `mcp_servers?: Array<BetaManagedAgentsURLMCPServerParams>`

    Body param: MCP servers this agent connects to. Maximum 20. Names must be unique within the array.

    - `name: string`

      Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

    - `type: "url"`

      - `"url"`

    - `url: string`

      Endpoint URL for the MCP server.

  - `metadata?: Record<string, string>`

    Body param: Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `skills?: Array<BetaManagedAgentsSkillParams>`

    Body param: Skills available to the agent. Maximum 20.

    - `BetaManagedAgentsAnthropicSkillParams`

      An Anthropic-managed skill.

      - `skill_id: string`

        Identifier of the Anthropic skill (e.g., "xlsx").

      - `type: "anthropic"`

        - `"anthropic"`

      - `version?: string | null`

        Version to pin. Defaults to latest if omitted.

    - `BetaManagedAgentsCustomSkillParams`

      A user-created custom skill.

      - `skill_id: string`

        Tagged ID of the custom skill (e.g., "skill_01XJ5...").

      - `type: "custom"`

        - `"custom"`

      - `version?: string | null`

        Version to pin. Defaults to latest if omitted.

  - `system?: string | null`

    Body param: System prompt for the agent. Up to 100,000 characters.

  - `tools?: Array<BetaManagedAgentsAgentToolset20260401Params | BetaManagedAgentsMCPToolsetParams | BetaManagedAgentsCustomToolParams>`

    Body param: Tool configurations available to the agent. Maximum of 128 tools across all toolsets allowed.

    - `BetaManagedAgentsAgentToolset20260401Params`

      Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

      - `configs?: Array<BetaManagedAgentsAgentToolConfigParams>`

        Per-tool configuration overrides.

        - `name: "bash" | "edit" | "read" | 5 more`

          Built-in agent tool identifier.

          - `"bash"`

          - `"edit"`

          - `"read"`

          - `"write"`

          - `"glob"`

          - `"grep"`

          - `"web_fetch"`

          - `"web_search"`

        - `enabled?: boolean | null`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | null`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config?: BetaManagedAgentsAgentToolsetDefaultConfigParams | null`

        Default configuration for all tools in a toolset.

        - `enabled?: boolean | null`

          Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

        - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | null`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

    - `BetaManagedAgentsMCPToolsetParams`

      Configuration for tools from an MCP server defined in `mcp_servers`.

      - `mcp_server_name: string`

        Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

      - `configs?: Array<BetaManagedAgentsMCPToolConfigParams>`

        Per-tool configuration overrides.

        - `name: string`

          Name of the MCP tool to configure. 1-128 characters.

        - `enabled?: boolean | null`

          Whether this tool is enabled. Overrides the `default_config` setting.

        - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | null`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config?: BetaManagedAgentsMCPToolsetDefaultConfigParams | null`

        Default configuration for all tools from an MCP server.

        - `enabled?: boolean | null`

          Whether tools are enabled by default. Defaults to true if not specified.

        - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | null`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

    - `BetaManagedAgentsCustomToolParams`

      A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

      - `description: string`

        Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `properties?: Record<string, unknown> | null`

          JSON Schema properties defining the tool's input parameters.

        - `required?: Array<string>`

          List of required property names.

        - `type?: "object"`

          Must be 'object' for tool input schemas.

          - `"object"`

      - `name: string`

        Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

      - `type: "custom"`

        - `"custom"`

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 18 more`

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

### Returns

- `BetaManagedAgentsAgent`

  A Managed Agents `agent`.

  - `id: string`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string | null`

  - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

    - `name: string`

    - `type: "url"`

      - `"url"`

    - `url: string`

  - `metadata: Record<string, string>`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-haiku-4-5" | 5 more`

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

      - `(string & {})`

    - `speed?: "standard" | "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `name: string`

  - `skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>`

    - `BetaManagedAgentsAnthropicSkill`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

        - `"anthropic"`

      - `version: string`

    - `BetaManagedAgentsCustomSkill`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

        - `"custom"`

      - `version: string`

  - `system: string | null`

  - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

    - `BetaManagedAgentsAgentToolset20260401`

      - `configs: Array<BetaManagedAgentsAgentToolConfig>`

        - `enabled: boolean`

        - `name: "bash" | "edit" | "read" | 5 more`

          Built-in agent tool identifier.

          - `"bash"`

          - `"edit"`

          - `"read"`

          - `"write"`

          - `"glob"`

          - `"grep"`

          - `"web_fetch"`

          - `"web_search"`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

    - `BetaManagedAgentsMCPToolset`

      - `configs: Array<BetaManagedAgentsMCPToolConfig>`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

    - `BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `properties?: Record<string, unknown> | null`

          JSON Schema properties defining the tool's input parameters.

        - `required?: Array<string>`

          List of required property names.

        - `type?: "object"`

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

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsAgent = await client.beta.agents.create({
  model: 'claude-sonnet-4-6',
  name: 'My First Agent',
});

console.log(betaManagedAgentsAgent.id);
```

## List

`client.beta.agents.list(AgentListParamsparams?, RequestOptionsoptions?): PageCursor<BetaManagedAgentsAgent>`

**get** `/v1/agents`

List Agents

### Parameters

- `params: AgentListParams`

  - `createdAtGte?: string`

    Query param: Return agents created at or after this time (inclusive).

  - `createdAtLte?: string`

    Query param: Return agents created at or before this time (inclusive).

  - `include_archived?: boolean`

    Query param: Include archived agents in results. Defaults to false.

  - `limit?: number`

    Query param: Maximum results per page. Default 20, maximum 100.

  - `page?: string`

    Query param: Opaque pagination cursor from a previous response.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 18 more`

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

### Returns

- `BetaManagedAgentsAgent`

  A Managed Agents `agent`.

  - `id: string`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string | null`

  - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

    - `name: string`

    - `type: "url"`

      - `"url"`

    - `url: string`

  - `metadata: Record<string, string>`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-haiku-4-5" | 5 more`

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

      - `(string & {})`

    - `speed?: "standard" | "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `name: string`

  - `skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>`

    - `BetaManagedAgentsAnthropicSkill`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

        - `"anthropic"`

      - `version: string`

    - `BetaManagedAgentsCustomSkill`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

        - `"custom"`

      - `version: string`

  - `system: string | null`

  - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

    - `BetaManagedAgentsAgentToolset20260401`

      - `configs: Array<BetaManagedAgentsAgentToolConfig>`

        - `enabled: boolean`

        - `name: "bash" | "edit" | "read" | 5 more`

          Built-in agent tool identifier.

          - `"bash"`

          - `"edit"`

          - `"read"`

          - `"write"`

          - `"glob"`

          - `"grep"`

          - `"web_fetch"`

          - `"web_search"`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

    - `BetaManagedAgentsMCPToolset`

      - `configs: Array<BetaManagedAgentsMCPToolConfig>`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

    - `BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `properties?: Record<string, unknown> | null`

          JSON Schema properties defining the tool's input parameters.

        - `required?: Array<string>`

          List of required property names.

        - `type?: "object"`

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

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsAgent of client.beta.agents.list()) {
  console.log(betaManagedAgentsAgent.id);
}
```

## Retrieve

`client.beta.agents.retrieve(stringagentID, AgentRetrieveParamsparams?, RequestOptionsoptions?): BetaManagedAgentsAgent`

**get** `/v1/agents/{agent_id}`

Get Agent

### Parameters

- `agentID: string`

- `params: AgentRetrieveParams`

  - `version?: number`

    Query param: Agent version. Omit for the most recent version. Must be at least 1 if specified.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 18 more`

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

### Returns

- `BetaManagedAgentsAgent`

  A Managed Agents `agent`.

  - `id: string`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string | null`

  - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

    - `name: string`

    - `type: "url"`

      - `"url"`

    - `url: string`

  - `metadata: Record<string, string>`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-haiku-4-5" | 5 more`

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

      - `(string & {})`

    - `speed?: "standard" | "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `name: string`

  - `skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>`

    - `BetaManagedAgentsAnthropicSkill`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

        - `"anthropic"`

      - `version: string`

    - `BetaManagedAgentsCustomSkill`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

        - `"custom"`

      - `version: string`

  - `system: string | null`

  - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

    - `BetaManagedAgentsAgentToolset20260401`

      - `configs: Array<BetaManagedAgentsAgentToolConfig>`

        - `enabled: boolean`

        - `name: "bash" | "edit" | "read" | 5 more`

          Built-in agent tool identifier.

          - `"bash"`

          - `"edit"`

          - `"read"`

          - `"write"`

          - `"glob"`

          - `"grep"`

          - `"web_fetch"`

          - `"web_search"`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

    - `BetaManagedAgentsMCPToolset`

      - `configs: Array<BetaManagedAgentsMCPToolConfig>`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

    - `BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `properties?: Record<string, unknown> | null`

          JSON Schema properties defining the tool's input parameters.

        - `required?: Array<string>`

          List of required property names.

        - `type?: "object"`

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

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsAgent = await client.beta.agents.retrieve('agent_011CZkYpogX7uDKUyvBTophP');

console.log(betaManagedAgentsAgent.id);
```

## Update

`client.beta.agents.update(stringagentID, AgentUpdateParamsparams, RequestOptionsoptions?): BetaManagedAgentsAgent`

**post** `/v1/agents/{agent_id}`

Update Agent

### Parameters

- `agentID: string`

- `params: AgentUpdateParams`

  - `version: number`

    Body param: The agent's current version, used to prevent concurrent overwrites. Obtain this value from a create or retrieve response. The request fails if this does not match the server's current version.

  - `description?: string | null`

    Body param: Description. Up to 2048 characters. Omit to preserve; send empty string or null to clear.

  - `mcp_servers?: Array<BetaManagedAgentsURLMCPServerParams> | null`

    Body param: MCP servers. Full replacement. Omit to preserve; send empty array or null to clear. Names must be unique. Maximum 20.

    - `name: string`

      Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

    - `type: "url"`

      - `"url"`

    - `url: string`

      Endpoint URL for the MCP server.

  - `metadata?: Record<string, string | null> | null`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `model?: BetaManagedAgentsModel | BetaManagedAgentsModelConfigParams`

    Body param: Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-4-6`, or a `model_config` object for additional configuration control. Omit to preserve. Cannot be cleared.

    - `BetaManagedAgentsModel = "claude-opus-4-6" | "claude-sonnet-4-6" | "claude-haiku-4-5" | 5 more | (string & {})`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-haiku-4-5" | 5 more`

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

      - `(string & {})`

    - `BetaManagedAgentsModelConfigParams`

      An object that defines additional configuration control over model use

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-haiku-4-5" | 5 more`

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

        - `(string & {})`

      - `speed?: "standard" | "fast" | null`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `name?: string`

    Body param: Human-readable name. 1-256 characters. Omit to preserve. Cannot be cleared.

  - `skills?: Array<BetaManagedAgentsSkillParams> | null`

    Body param: Skills. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 20.

    - `BetaManagedAgentsAnthropicSkillParams`

      An Anthropic-managed skill.

      - `skill_id: string`

        Identifier of the Anthropic skill (e.g., "xlsx").

      - `type: "anthropic"`

        - `"anthropic"`

      - `version?: string | null`

        Version to pin. Defaults to latest if omitted.

    - `BetaManagedAgentsCustomSkillParams`

      A user-created custom skill.

      - `skill_id: string`

        Tagged ID of the custom skill (e.g., "skill_01XJ5...").

      - `type: "custom"`

        - `"custom"`

      - `version?: string | null`

        Version to pin. Defaults to latest if omitted.

  - `system?: string | null`

    Body param: System prompt. Up to 100,000 characters. Omit to preserve; send empty string or null to clear.

  - `tools?: Array<BetaManagedAgentsAgentToolset20260401Params | BetaManagedAgentsMCPToolsetParams | BetaManagedAgentsCustomToolParams> | null`

    Body param: Tool configurations available to the agent. Full replacement. Omit to preserve; send empty array or null to clear. Maximum of 128 tools across all toolsets allowed.

    - `BetaManagedAgentsAgentToolset20260401Params`

      Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

      - `configs?: Array<BetaManagedAgentsAgentToolConfigParams>`

        Per-tool configuration overrides.

        - `name: "bash" | "edit" | "read" | 5 more`

          Built-in agent tool identifier.

          - `"bash"`

          - `"edit"`

          - `"read"`

          - `"write"`

          - `"glob"`

          - `"grep"`

          - `"web_fetch"`

          - `"web_search"`

        - `enabled?: boolean | null`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | null`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config?: BetaManagedAgentsAgentToolsetDefaultConfigParams | null`

        Default configuration for all tools in a toolset.

        - `enabled?: boolean | null`

          Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

        - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | null`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

    - `BetaManagedAgentsMCPToolsetParams`

      Configuration for tools from an MCP server defined in `mcp_servers`.

      - `mcp_server_name: string`

        Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

      - `configs?: Array<BetaManagedAgentsMCPToolConfigParams>`

        Per-tool configuration overrides.

        - `name: string`

          Name of the MCP tool to configure. 1-128 characters.

        - `enabled?: boolean | null`

          Whether this tool is enabled. Overrides the `default_config` setting.

        - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | null`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config?: BetaManagedAgentsMCPToolsetDefaultConfigParams | null`

        Default configuration for all tools from an MCP server.

        - `enabled?: boolean | null`

          Whether tools are enabled by default. Defaults to true if not specified.

        - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | null`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

    - `BetaManagedAgentsCustomToolParams`

      A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

      - `description: string`

        Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `properties?: Record<string, unknown> | null`

          JSON Schema properties defining the tool's input parameters.

        - `required?: Array<string>`

          List of required property names.

        - `type?: "object"`

          Must be 'object' for tool input schemas.

          - `"object"`

      - `name: string`

        Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

      - `type: "custom"`

        - `"custom"`

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 18 more`

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

### Returns

- `BetaManagedAgentsAgent`

  A Managed Agents `agent`.

  - `id: string`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string | null`

  - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

    - `name: string`

    - `type: "url"`

      - `"url"`

    - `url: string`

  - `metadata: Record<string, string>`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-haiku-4-5" | 5 more`

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

      - `(string & {})`

    - `speed?: "standard" | "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `name: string`

  - `skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>`

    - `BetaManagedAgentsAnthropicSkill`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

        - `"anthropic"`

      - `version: string`

    - `BetaManagedAgentsCustomSkill`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

        - `"custom"`

      - `version: string`

  - `system: string | null`

  - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

    - `BetaManagedAgentsAgentToolset20260401`

      - `configs: Array<BetaManagedAgentsAgentToolConfig>`

        - `enabled: boolean`

        - `name: "bash" | "edit" | "read" | 5 more`

          Built-in agent tool identifier.

          - `"bash"`

          - `"edit"`

          - `"read"`

          - `"write"`

          - `"glob"`

          - `"grep"`

          - `"web_fetch"`

          - `"web_search"`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

    - `BetaManagedAgentsMCPToolset`

      - `configs: Array<BetaManagedAgentsMCPToolConfig>`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

    - `BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `properties?: Record<string, unknown> | null`

          JSON Schema properties defining the tool's input parameters.

        - `required?: Array<string>`

          List of required property names.

        - `type?: "object"`

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

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsAgent = await client.beta.agents.update('agent_011CZkYpogX7uDKUyvBTophP', {
  version: 1,
});

console.log(betaManagedAgentsAgent.id);
```

## Archive

`client.beta.agents.archive(stringagentID, AgentArchiveParamsparams?, RequestOptionsoptions?): BetaManagedAgentsAgent`

**post** `/v1/agents/{agent_id}/archive`

Archive Agent

### Parameters

- `agentID: string`

- `params: AgentArchiveParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 18 more`

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

### Returns

- `BetaManagedAgentsAgent`

  A Managed Agents `agent`.

  - `id: string`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string | null`

  - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

    - `name: string`

    - `type: "url"`

      - `"url"`

    - `url: string`

  - `metadata: Record<string, string>`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-haiku-4-5" | 5 more`

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

      - `(string & {})`

    - `speed?: "standard" | "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `name: string`

  - `skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>`

    - `BetaManagedAgentsAnthropicSkill`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

        - `"anthropic"`

      - `version: string`

    - `BetaManagedAgentsCustomSkill`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

        - `"custom"`

      - `version: string`

  - `system: string | null`

  - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

    - `BetaManagedAgentsAgentToolset20260401`

      - `configs: Array<BetaManagedAgentsAgentToolConfig>`

        - `enabled: boolean`

        - `name: "bash" | "edit" | "read" | 5 more`

          Built-in agent tool identifier.

          - `"bash"`

          - `"edit"`

          - `"read"`

          - `"write"`

          - `"glob"`

          - `"grep"`

          - `"web_fetch"`

          - `"web_search"`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

    - `BetaManagedAgentsMCPToolset`

      - `configs: Array<BetaManagedAgentsMCPToolConfig>`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

    - `BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `properties?: Record<string, unknown> | null`

          JSON Schema properties defining the tool's input parameters.

        - `required?: Array<string>`

          List of required property names.

        - `type?: "object"`

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

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsAgent = await client.beta.agents.archive('agent_011CZkYpogX7uDKUyvBTophP');

console.log(betaManagedAgentsAgent.id);
```

## Domain Types

### Beta Managed Agents Agent

- `BetaManagedAgentsAgent`

  A Managed Agents `agent`.

  - `id: string`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string | null`

  - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

    - `name: string`

    - `type: "url"`

      - `"url"`

    - `url: string`

  - `metadata: Record<string, string>`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-haiku-4-5" | 5 more`

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

      - `(string & {})`

    - `speed?: "standard" | "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `name: string`

  - `skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>`

    - `BetaManagedAgentsAnthropicSkill`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

        - `"anthropic"`

      - `version: string`

    - `BetaManagedAgentsCustomSkill`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

        - `"custom"`

      - `version: string`

  - `system: string | null`

  - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

    - `BetaManagedAgentsAgentToolset20260401`

      - `configs: Array<BetaManagedAgentsAgentToolConfig>`

        - `enabled: boolean`

        - `name: "bash" | "edit" | "read" | 5 more`

          Built-in agent tool identifier.

          - `"bash"`

          - `"edit"`

          - `"read"`

          - `"write"`

          - `"glob"`

          - `"grep"`

          - `"web_fetch"`

          - `"web_search"`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

    - `BetaManagedAgentsMCPToolset`

      - `configs: Array<BetaManagedAgentsMCPToolConfig>`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

    - `BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `properties?: Record<string, unknown> | null`

          JSON Schema properties defining the tool's input parameters.

        - `required?: Array<string>`

          List of required property names.

        - `type?: "object"`

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

- `BetaManagedAgentsAgentToolConfig`

  Configuration for a specific agent tool.

  - `enabled: boolean`

  - `name: "bash" | "edit" | "read" | 5 more`

    Built-in agent tool identifier.

    - `"bash"`

    - `"edit"`

    - `"read"`

    - `"write"`

    - `"glob"`

    - `"grep"`

    - `"web_fetch"`

    - `"web_search"`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents Agent Tool Config Params

- `BetaManagedAgentsAgentToolConfigParams`

  Configuration override for a specific tool within a toolset.

  - `name: "bash" | "edit" | "read" | 5 more`

    Built-in agent tool identifier.

    - `"bash"`

    - `"edit"`

    - `"read"`

    - `"write"`

    - `"glob"`

    - `"grep"`

    - `"web_fetch"`

    - `"web_search"`

  - `enabled?: boolean | null`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | null`

    Permission policy for tool execution.

    - `BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents Agent Toolset Default Config

- `BetaManagedAgentsAgentToolsetDefaultConfig`

  Resolved default configuration for agent tools.

  - `enabled: boolean`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents Agent Toolset Default Config Params

- `BetaManagedAgentsAgentToolsetDefaultConfigParams`

  Default configuration for all tools in a toolset.

  - `enabled?: boolean | null`

    Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

  - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | null`

    Permission policy for tool execution.

    - `BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents Agent Toolset20260401

- `BetaManagedAgentsAgentToolset20260401`

  - `configs: Array<BetaManagedAgentsAgentToolConfig>`

    - `enabled: boolean`

    - `name: "bash" | "edit" | "read" | 5 more`

      Built-in agent tool identifier.

      - `"bash"`

      - `"edit"`

      - `"read"`

      - `"write"`

      - `"glob"`

      - `"grep"`

      - `"web_fetch"`

      - `"web_search"`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

        - `type: "always_allow"`

          - `"always_allow"`

      - `BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

        - `type: "always_ask"`

          - `"always_ask"`

  - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

    Resolved default configuration for agent tools.

    - `enabled: boolean`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

        - `type: "always_allow"`

          - `"always_allow"`

      - `BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

        - `type: "always_ask"`

          - `"always_ask"`

  - `type: "agent_toolset_20260401"`

    - `"agent_toolset_20260401"`

### Beta Managed Agents Agent Toolset20260401 Params

- `BetaManagedAgentsAgentToolset20260401Params`

  Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

  - `type: "agent_toolset_20260401"`

    - `"agent_toolset_20260401"`

  - `configs?: Array<BetaManagedAgentsAgentToolConfigParams>`

    Per-tool configuration overrides.

    - `name: "bash" | "edit" | "read" | 5 more`

      Built-in agent tool identifier.

      - `"bash"`

      - `"edit"`

      - `"read"`

      - `"write"`

      - `"glob"`

      - `"grep"`

      - `"web_fetch"`

      - `"web_search"`

    - `enabled?: boolean | null`

      Whether this tool is enabled and available to Claude. Overrides the default_config setting.

    - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | null`

      Permission policy for tool execution.

      - `BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

        - `type: "always_allow"`

          - `"always_allow"`

      - `BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

        - `type: "always_ask"`

          - `"always_ask"`

  - `default_config?: BetaManagedAgentsAgentToolsetDefaultConfigParams | null`

    Default configuration for all tools in a toolset.

    - `enabled?: boolean | null`

      Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

    - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | null`

      Permission policy for tool execution.

      - `BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

        - `type: "always_allow"`

          - `"always_allow"`

      - `BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

        - `type: "always_ask"`

          - `"always_ask"`

### Beta Managed Agents Always Allow Policy

- `BetaManagedAgentsAlwaysAllowPolicy`

  Tool calls are automatically approved without user confirmation.

  - `type: "always_allow"`

    - `"always_allow"`

### Beta Managed Agents Always Ask Policy

- `BetaManagedAgentsAlwaysAskPolicy`

  Tool calls require user confirmation before execution.

  - `type: "always_ask"`

    - `"always_ask"`

### Beta Managed Agents Anthropic Skill

- `BetaManagedAgentsAnthropicSkill`

  A resolved Anthropic-managed skill.

  - `skill_id: string`

  - `type: "anthropic"`

    - `"anthropic"`

  - `version: string`

### Beta Managed Agents Anthropic Skill Params

- `BetaManagedAgentsAnthropicSkillParams`

  An Anthropic-managed skill.

  - `skill_id: string`

    Identifier of the Anthropic skill (e.g., "xlsx").

  - `type: "anthropic"`

    - `"anthropic"`

  - `version?: string | null`

    Version to pin. Defaults to latest if omitted.

### Beta Managed Agents Custom Skill

- `BetaManagedAgentsCustomSkill`

  A resolved user-created custom skill.

  - `skill_id: string`

  - `type: "custom"`

    - `"custom"`

  - `version: string`

### Beta Managed Agents Custom Skill Params

- `BetaManagedAgentsCustomSkillParams`

  A user-created custom skill.

  - `skill_id: string`

    Tagged ID of the custom skill (e.g., "skill_01XJ5...").

  - `type: "custom"`

    - `"custom"`

  - `version?: string | null`

    Version to pin. Defaults to latest if omitted.

### Beta Managed Agents Custom Tool

- `BetaManagedAgentsCustomTool`

  A custom tool as returned in API responses.

  - `description: string`

  - `input_schema: BetaManagedAgentsCustomToolInputSchema`

    JSON Schema for custom tool input parameters.

    - `properties?: Record<string, unknown> | null`

      JSON Schema properties defining the tool's input parameters.

    - `required?: Array<string>`

      List of required property names.

    - `type?: "object"`

      Must be 'object' for tool input schemas.

      - `"object"`

  - `name: string`

  - `type: "custom"`

    - `"custom"`

### Beta Managed Agents Custom Tool Input Schema

- `BetaManagedAgentsCustomToolInputSchema`

  JSON Schema for custom tool input parameters.

  - `properties?: Record<string, unknown> | null`

    JSON Schema properties defining the tool's input parameters.

  - `required?: Array<string>`

    List of required property names.

  - `type?: "object"`

    Must be 'object' for tool input schemas.

    - `"object"`

### Beta Managed Agents Custom Tool Params

- `BetaManagedAgentsCustomToolParams`

  A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

  - `description: string`

    Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

  - `input_schema: BetaManagedAgentsCustomToolInputSchema`

    JSON Schema for custom tool input parameters.

    - `properties?: Record<string, unknown> | null`

      JSON Schema properties defining the tool's input parameters.

    - `required?: Array<string>`

      List of required property names.

    - `type?: "object"`

      Must be 'object' for tool input schemas.

      - `"object"`

  - `name: string`

    Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

  - `type: "custom"`

    - `"custom"`

### Beta Managed Agents MCP Server URL Definition

- `BetaManagedAgentsMCPServerURLDefinition`

  URL-based MCP server connection as returned in API responses.

  - `name: string`

  - `type: "url"`

    - `"url"`

  - `url: string`

### Beta Managed Agents MCP Tool Config

- `BetaManagedAgentsMCPToolConfig`

  Resolved configuration for a specific MCP tool.

  - `enabled: boolean`

  - `name: string`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents MCP Tool Config Params

- `BetaManagedAgentsMCPToolConfigParams`

  Configuration override for a specific MCP tool.

  - `name: string`

    Name of the MCP tool to configure. 1-128 characters.

  - `enabled?: boolean | null`

    Whether this tool is enabled. Overrides the `default_config` setting.

  - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | null`

    Permission policy for tool execution.

    - `BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents MCP Toolset

- `BetaManagedAgentsMCPToolset`

  - `configs: Array<BetaManagedAgentsMCPToolConfig>`

    - `enabled: boolean`

    - `name: string`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

        - `type: "always_allow"`

          - `"always_allow"`

      - `BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

        - `type: "always_ask"`

          - `"always_ask"`

  - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

    Resolved default configuration for all tools from an MCP server.

    - `enabled: boolean`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

        - `type: "always_allow"`

          - `"always_allow"`

      - `BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

        - `type: "always_ask"`

          - `"always_ask"`

  - `mcp_server_name: string`

  - `type: "mcp_toolset"`

    - `"mcp_toolset"`

### Beta Managed Agents MCP Toolset Default Config

- `BetaManagedAgentsMCPToolsetDefaultConfig`

  Resolved default configuration for all tools from an MCP server.

  - `enabled: boolean`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents MCP Toolset Default Config Params

- `BetaManagedAgentsMCPToolsetDefaultConfigParams`

  Default configuration for all tools from an MCP server.

  - `enabled?: boolean | null`

    Whether tools are enabled by default. Defaults to true if not specified.

  - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | null`

    Permission policy for tool execution.

    - `BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents MCP Toolset Params

- `BetaManagedAgentsMCPToolsetParams`

  Configuration for tools from an MCP server defined in `mcp_servers`.

  - `mcp_server_name: string`

    Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

  - `type: "mcp_toolset"`

    - `"mcp_toolset"`

  - `configs?: Array<BetaManagedAgentsMCPToolConfigParams>`

    Per-tool configuration overrides.

    - `name: string`

      Name of the MCP tool to configure. 1-128 characters.

    - `enabled?: boolean | null`

      Whether this tool is enabled. Overrides the `default_config` setting.

    - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | null`

      Permission policy for tool execution.

      - `BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

        - `type: "always_allow"`

          - `"always_allow"`

      - `BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

        - `type: "always_ask"`

          - `"always_ask"`

  - `default_config?: BetaManagedAgentsMCPToolsetDefaultConfigParams | null`

    Default configuration for all tools from an MCP server.

    - `enabled?: boolean | null`

      Whether tools are enabled by default. Defaults to true if not specified.

    - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | null`

      Permission policy for tool execution.

      - `BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

        - `type: "always_allow"`

          - `"always_allow"`

      - `BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

        - `type: "always_ask"`

          - `"always_ask"`

### Beta Managed Agents Model

- `BetaManagedAgentsModel = "claude-opus-4-6" | "claude-sonnet-4-6" | "claude-haiku-4-5" | 5 more | (string & {})`

  The model that will power your agent.

  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-haiku-4-5" | 5 more`

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

  - `(string & {})`

### Beta Managed Agents Model Config

- `BetaManagedAgentsModelConfig`

  Model identifier and configuration.

  - `id: BetaManagedAgentsModel`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-haiku-4-5" | 5 more`

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

    - `(string & {})`

  - `speed?: "standard" | "fast"`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"`

    - `"fast"`

### Beta Managed Agents Model Config Params

- `BetaManagedAgentsModelConfigParams`

  An object that defines additional configuration control over model use

  - `id: BetaManagedAgentsModel`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-haiku-4-5" | 5 more`

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

    - `(string & {})`

  - `speed?: "standard" | "fast" | null`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"`

    - `"fast"`

### Beta Managed Agents Skill Params

- `BetaManagedAgentsSkillParams = BetaManagedAgentsAnthropicSkillParams | BetaManagedAgentsCustomSkillParams`

  Skill to load in the session container.

  - `BetaManagedAgentsAnthropicSkillParams`

    An Anthropic-managed skill.

    - `skill_id: string`

      Identifier of the Anthropic skill (e.g., "xlsx").

    - `type: "anthropic"`

      - `"anthropic"`

    - `version?: string | null`

      Version to pin. Defaults to latest if omitted.

  - `BetaManagedAgentsCustomSkillParams`

    A user-created custom skill.

    - `skill_id: string`

      Tagged ID of the custom skill (e.g., "skill_01XJ5...").

    - `type: "custom"`

      - `"custom"`

    - `version?: string | null`

      Version to pin. Defaults to latest if omitted.

### Beta Managed Agents URL MCP Server Params

- `BetaManagedAgentsURLMCPServerParams`

  URL-based MCP server connection.

  - `name: string`

    Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

  - `type: "url"`

    - `"url"`

  - `url: string`

    Endpoint URL for the MCP server.

# Versions

## List

`client.beta.agents.versions.list(stringagentID, VersionListParamsparams?, RequestOptionsoptions?): PageCursor<BetaManagedAgentsAgent>`

**get** `/v1/agents/{agent_id}/versions`

List Agent Versions

### Parameters

- `agentID: string`

- `params: VersionListParams`

  - `limit?: number`

    Query param: Maximum results per page. Default 20, maximum 100.

  - `page?: string`

    Query param: Opaque pagination cursor.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 18 more`

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

### Returns

- `BetaManagedAgentsAgent`

  A Managed Agents `agent`.

  - `id: string`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string | null`

  - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

    - `name: string`

    - `type: "url"`

      - `"url"`

    - `url: string`

  - `metadata: Record<string, string>`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-haiku-4-5" | 5 more`

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

      - `(string & {})`

    - `speed?: "standard" | "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `name: string`

  - `skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>`

    - `BetaManagedAgentsAnthropicSkill`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

        - `"anthropic"`

      - `version: string`

    - `BetaManagedAgentsCustomSkill`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

        - `"custom"`

      - `version: string`

  - `system: string | null`

  - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

    - `BetaManagedAgentsAgentToolset20260401`

      - `configs: Array<BetaManagedAgentsAgentToolConfig>`

        - `enabled: boolean`

        - `name: "bash" | "edit" | "read" | 5 more`

          Built-in agent tool identifier.

          - `"bash"`

          - `"edit"`

          - `"read"`

          - `"write"`

          - `"glob"`

          - `"grep"`

          - `"web_fetch"`

          - `"web_search"`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

    - `BetaManagedAgentsMCPToolset`

      - `configs: Array<BetaManagedAgentsMCPToolConfig>`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

    - `BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `properties?: Record<string, unknown> | null`

          JSON Schema properties defining the tool's input parameters.

        - `required?: Array<string>`

          List of required property names.

        - `type?: "object"`

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

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsAgent of client.beta.agents.versions.list(
  'agent_011CZkYpogX7uDKUyvBTophP',
)) {
  console.log(betaManagedAgentsAgent.id);
}
```
