## Update

`client.Beta.Agents.Update(ctx, agentID, params) (*BetaManagedAgentsAgent, error)`

**post** `/v1/agents/{agent_id}`

Update Agent

### Parameters

- `agentID string`

- `params BetaAgentUpdateParams`

  - `Version param.Field[int64]`

    Body param: The agent's current version, used to prevent concurrent overwrites. Obtain this value from a create or retrieve response. The request fails if this does not match the server's current version.

  - `Description param.Field[string]`

    Body param: Description. Up to 2048 characters. Omit to preserve; send empty string or null to clear.

  - `MCPServers param.Field[[]BetaManagedAgentsURLMCPServerParamsResp]`

    Body param: MCP servers. Full replacement. Omit to preserve; send empty array or null to clear. Names must be unique. Maximum 20.

    - `Name string`

      Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

    - `Type BetaManagedAgentsURLMCPServerParamsType`

      - `const BetaManagedAgentsURLMCPServerParamsTypeURL BetaManagedAgentsURLMCPServerParamsType = "url"`

    - `URL string`

      Endpoint URL for the MCP server.

  - `Metadata param.Field[map[string, string]]`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `Model param.Field[BetaManagedAgentsModelConfigParamsResp]`

    Body param: Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-4-6`, or a `model_config` object for additional configuration control. Omit to preserve. Cannot be cleared.

    - `type BetaManagedAgentsModelConfigParamsResp struct{…}`

      An object that defines additional configuration control over model use

      - `ID BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `type BetaManagedAgentsModel string`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `const BetaManagedAgentsModelClaudeOpus4_7 BetaManagedAgentsModel = "claude-opus-4-7"`

            Frontier intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_6 BetaManagedAgentsModel = "claude-opus-4-6"`

            Most intelligent model for building agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_6 BetaManagedAgentsModel = "claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `const BetaManagedAgentsModelClaudeHaiku4_5 BetaManagedAgentsModel = "claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `const BetaManagedAgentsModelClaudeHaiku4_5_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `const BetaManagedAgentsModelClaudeOpus4_5 BetaManagedAgentsModel = "claude-opus-4-5"`

            Premium model combining maximum intelligence with practical performance

          - `const BetaManagedAgentsModelClaudeOpus4_5_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"`

            Premium model combining maximum intelligence with practical performance

          - `const BetaManagedAgentsModelClaudeSonnet4_5 BetaManagedAgentsModel = "claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_5_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `string`

      - `Speed BetaManagedAgentsModelConfigParamsSpeed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `const BetaManagedAgentsModelConfigParamsSpeedStandard BetaManagedAgentsModelConfigParamsSpeed = "standard"`

        - `const BetaManagedAgentsModelConfigParamsSpeedFast BetaManagedAgentsModelConfigParamsSpeed = "fast"`

  - `Name param.Field[string]`

    Body param: Human-readable name. 1-256 characters. Omit to preserve. Cannot be cleared.

  - `Skills param.Field[[]BetaManagedAgentsSkillParamsUnionResp]`

    Body param: Skills. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 20.

    - `type BetaManagedAgentsAnthropicSkillParamsResp struct{…}`

      An Anthropic-managed skill.

      - `SkillID string`

        Identifier of the Anthropic skill (e.g., "xlsx").

      - `Type BetaManagedAgentsAnthropicSkillParamsType`

        - `const BetaManagedAgentsAnthropicSkillParamsTypeAnthropic BetaManagedAgentsAnthropicSkillParamsType = "anthropic"`

      - `Version string`

        Version to pin. Defaults to latest if omitted.

    - `type BetaManagedAgentsCustomSkillParamsResp struct{…}`

      A user-created custom skill.

      - `SkillID string`

        Tagged ID of the custom skill (e.g., "skill_01XJ5...").

      - `Type BetaManagedAgentsCustomSkillParamsType`

        - `const BetaManagedAgentsCustomSkillParamsTypeCustom BetaManagedAgentsCustomSkillParamsType = "custom"`

      - `Version string`

        Version to pin. Defaults to latest if omitted.

  - `System param.Field[string]`

    Body param: System prompt. Up to 100,000 characters. Omit to preserve; send empty string or null to clear.

  - `Tools param.Field[[]BetaAgentUpdateParamsToolUnion]`

    Body param: Tool configurations available to the agent. Full replacement. Omit to preserve; send empty array or null to clear. Maximum of 128 tools across all toolsets allowed.

    - `type BetaManagedAgentsAgentToolset20260401ParamsResp struct{…}`

      Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

      - `Type BetaManagedAgentsAgentToolset20260401ParamsType`

        - `const BetaManagedAgentsAgentToolset20260401ParamsTypeAgentToolset20260401 BetaManagedAgentsAgentToolset20260401ParamsType = "agent_toolset_20260401"`

      - `Configs []BetaManagedAgentsAgentToolConfigParamsResp`

        Per-tool configuration overrides.

        - `Name BetaManagedAgentsAgentToolConfigParamsName`

          Built-in agent tool identifier.

          - `const BetaManagedAgentsAgentToolConfigParamsNameBash BetaManagedAgentsAgentToolConfigParamsName = "bash"`

          - `const BetaManagedAgentsAgentToolConfigParamsNameEdit BetaManagedAgentsAgentToolConfigParamsName = "edit"`

          - `const BetaManagedAgentsAgentToolConfigParamsNameRead BetaManagedAgentsAgentToolConfigParamsName = "read"`

          - `const BetaManagedAgentsAgentToolConfigParamsNameWrite BetaManagedAgentsAgentToolConfigParamsName = "write"`

          - `const BetaManagedAgentsAgentToolConfigParamsNameGlob BetaManagedAgentsAgentToolConfigParamsName = "glob"`

          - `const BetaManagedAgentsAgentToolConfigParamsNameGrep BetaManagedAgentsAgentToolConfigParamsName = "grep"`

          - `const BetaManagedAgentsAgentToolConfigParamsNameWebFetch BetaManagedAgentsAgentToolConfigParamsName = "web_fetch"`

          - `const BetaManagedAgentsAgentToolConfigParamsNameWebSearch BetaManagedAgentsAgentToolConfigParamsName = "web_search"`

        - `Enabled bool`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `PermissionPolicy BetaManagedAgentsAgentToolConfigParamsPermissionPolicyUnionResp`

          Permission policy for tool execution.

          - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

            Tool calls are automatically approved without user confirmation.

            - `Type BetaManagedAgentsAlwaysAllowPolicyType`

              - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

          - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

            Tool calls require user confirmation before execution.

            - `Type BetaManagedAgentsAlwaysAskPolicyType`

              - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

      - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfigParamsResp`

        Default configuration for all tools in a toolset.

        - `Enabled bool`

          Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

        - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigParamsPermissionPolicyUnionResp`

          Permission policy for tool execution.

          - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

            Tool calls are automatically approved without user confirmation.

            - `Type BetaManagedAgentsAlwaysAllowPolicyType`

              - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

          - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

            Tool calls require user confirmation before execution.

            - `Type BetaManagedAgentsAlwaysAskPolicyType`

              - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

    - `type BetaManagedAgentsMCPToolsetParamsResp struct{…}`

      Configuration for tools from an MCP server defined in `mcp_servers`.

      - `MCPServerName string`

        Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

      - `Type BetaManagedAgentsMCPToolsetParamsType`

        - `const BetaManagedAgentsMCPToolsetParamsTypeMCPToolset BetaManagedAgentsMCPToolsetParamsType = "mcp_toolset"`

      - `Configs []BetaManagedAgentsMCPToolConfigParamsResp`

        Per-tool configuration overrides.

        - `Name string`

          Name of the MCP tool to configure. 1-128 characters.

        - `Enabled bool`

          Whether this tool is enabled. Overrides the `default_config` setting.

        - `PermissionPolicy BetaManagedAgentsMCPToolConfigParamsPermissionPolicyUnionResp`

          Permission policy for tool execution.

          - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

            Tool calls are automatically approved without user confirmation.

            - `Type BetaManagedAgentsAlwaysAllowPolicyType`

              - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

          - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

            Tool calls require user confirmation before execution.

            - `Type BetaManagedAgentsAlwaysAskPolicyType`

              - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

      - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfigParamsResp`

        Default configuration for all tools from an MCP server.

        - `Enabled bool`

          Whether tools are enabled by default. Defaults to true if not specified.

        - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigParamsPermissionPolicyUnionResp`

          Permission policy for tool execution.

          - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

            Tool calls are automatically approved without user confirmation.

            - `Type BetaManagedAgentsAlwaysAllowPolicyType`

              - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

          - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

            Tool calls require user confirmation before execution.

            - `Type BetaManagedAgentsAlwaysAskPolicyType`

              - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

    - `type BetaManagedAgentsCustomToolParamsResp struct{…}`

      A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

      - `Description string`

        Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

      - `InputSchema BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `Properties map[string, any]`

          JSON Schema properties defining the tool's input parameters.

        - `Required []string`

          List of required property names.

        - `Type BetaManagedAgentsCustomToolInputSchemaType`

          Must be 'object' for tool input schemas.

          - `const BetaManagedAgentsCustomToolInputSchemaTypeObject BetaManagedAgentsCustomToolInputSchemaType = "object"`

      - `Name string`

        Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

      - `Type BetaManagedAgentsCustomToolParamsType`

        - `const BetaManagedAgentsCustomToolParamsTypeCustom BetaManagedAgentsCustomToolParamsType = "custom"`

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

### Returns

- `type BetaManagedAgentsAgent struct{…}`

  A Managed Agents `agent`.

  - `ID string`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Description string`

  - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

    - `Name string`

    - `Type BetaManagedAgentsMCPServerURLDefinitionType`

      - `const BetaManagedAgentsMCPServerURLDefinitionTypeURL BetaManagedAgentsMCPServerURLDefinitionType = "url"`

    - `URL string`

  - `Metadata map[string, string]`

  - `Model BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `ID BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `type BetaManagedAgentsModel string`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `const BetaManagedAgentsModelClaudeOpus4_7 BetaManagedAgentsModel = "claude-opus-4-7"`

          Frontier intelligence for long-running agents and coding

        - `const BetaManagedAgentsModelClaudeOpus4_6 BetaManagedAgentsModel = "claude-opus-4-6"`

          Most intelligent model for building agents and coding

        - `const BetaManagedAgentsModelClaudeSonnet4_6 BetaManagedAgentsModel = "claude-sonnet-4-6"`

          Best combination of speed and intelligence

        - `const BetaManagedAgentsModelClaudeHaiku4_5 BetaManagedAgentsModel = "claude-haiku-4-5"`

          Fastest model with near-frontier intelligence

        - `const BetaManagedAgentsModelClaudeHaiku4_5_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"`

          Fastest model with near-frontier intelligence

        - `const BetaManagedAgentsModelClaudeOpus4_5 BetaManagedAgentsModel = "claude-opus-4-5"`

          Premium model combining maximum intelligence with practical performance

        - `const BetaManagedAgentsModelClaudeOpus4_5_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"`

          Premium model combining maximum intelligence with practical performance

        - `const BetaManagedAgentsModelClaudeSonnet4_5 BetaManagedAgentsModel = "claude-sonnet-4-5"`

          High-performance model for agents and coding

        - `const BetaManagedAgentsModelClaudeSonnet4_5_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"`

          High-performance model for agents and coding

      - `string`

    - `Speed BetaManagedAgentsModelConfigSpeed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"`

      - `const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"`

  - `Name string`

  - `Skills []BetaManagedAgentsAgentSkillUnion`

    - `type BetaManagedAgentsAnthropicSkill struct{…}`

      A resolved Anthropic-managed skill.

      - `SkillID string`

      - `Type BetaManagedAgentsAnthropicSkillType`

        - `const BetaManagedAgentsAnthropicSkillTypeAnthropic BetaManagedAgentsAnthropicSkillType = "anthropic"`

      - `Version string`

    - `type BetaManagedAgentsCustomSkill struct{…}`

      A resolved user-created custom skill.

      - `SkillID string`

      - `Type BetaManagedAgentsCustomSkillType`

        - `const BetaManagedAgentsCustomSkillTypeCustom BetaManagedAgentsCustomSkillType = "custom"`

      - `Version string`

  - `System string`

  - `Tools []BetaManagedAgentsAgentToolUnion`

    - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

      - `Configs []BetaManagedAgentsAgentToolConfig`

        - `Enabled bool`

        - `Name BetaManagedAgentsAgentToolConfigName`

          Built-in agent tool identifier.

          - `const BetaManagedAgentsAgentToolConfigNameBash BetaManagedAgentsAgentToolConfigName = "bash"`

          - `const BetaManagedAgentsAgentToolConfigNameEdit BetaManagedAgentsAgentToolConfigName = "edit"`

          - `const BetaManagedAgentsAgentToolConfigNameRead BetaManagedAgentsAgentToolConfigName = "read"`

          - `const BetaManagedAgentsAgentToolConfigNameWrite BetaManagedAgentsAgentToolConfigName = "write"`

          - `const BetaManagedAgentsAgentToolConfigNameGlob BetaManagedAgentsAgentToolConfigName = "glob"`

          - `const BetaManagedAgentsAgentToolConfigNameGrep BetaManagedAgentsAgentToolConfigName = "grep"`

          - `const BetaManagedAgentsAgentToolConfigNameWebFetch BetaManagedAgentsAgentToolConfigName = "web_fetch"`

          - `const BetaManagedAgentsAgentToolConfigNameWebSearch BetaManagedAgentsAgentToolConfigName = "web_search"`

        - `PermissionPolicy BetaManagedAgentsAgentToolConfigPermissionPolicyUnion`

          Permission policy for tool execution.

          - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

            Tool calls are automatically approved without user confirmation.

            - `Type BetaManagedAgentsAlwaysAllowPolicyType`

              - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

          - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

            Tool calls require user confirmation before execution.

            - `Type BetaManagedAgentsAlwaysAskPolicyType`

              - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

      - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `Enabled bool`

        - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion`

          Permission policy for tool execution.

          - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

            Tool calls are automatically approved without user confirmation.

            - `Type BetaManagedAgentsAlwaysAllowPolicyType`

              - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

          - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

            Tool calls require user confirmation before execution.

            - `Type BetaManagedAgentsAlwaysAskPolicyType`

              - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

      - `Type BetaManagedAgentsAgentToolset20260401Type`

        - `const BetaManagedAgentsAgentToolset20260401TypeAgentToolset20260401 BetaManagedAgentsAgentToolset20260401Type = "agent_toolset_20260401"`

    - `type BetaManagedAgentsMCPToolset struct{…}`

      - `Configs []BetaManagedAgentsMCPToolConfig`

        - `Enabled bool`

        - `Name string`

        - `PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion`

          Permission policy for tool execution.

          - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

            Tool calls are automatically approved without user confirmation.

            - `Type BetaManagedAgentsAlwaysAllowPolicyType`

              - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

          - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

            Tool calls require user confirmation before execution.

            - `Type BetaManagedAgentsAlwaysAskPolicyType`

              - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

      - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `Enabled bool`

        - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion`

          Permission policy for tool execution.

          - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

            Tool calls are automatically approved without user confirmation.

            - `Type BetaManagedAgentsAlwaysAllowPolicyType`

              - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

          - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

            Tool calls require user confirmation before execution.

            - `Type BetaManagedAgentsAlwaysAskPolicyType`

              - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

      - `MCPServerName string`

      - `Type BetaManagedAgentsMCPToolsetType`

        - `const BetaManagedAgentsMCPToolsetTypeMCPToolset BetaManagedAgentsMCPToolsetType = "mcp_toolset"`

    - `type BetaManagedAgentsCustomTool struct{…}`

      A custom tool as returned in API responses.

      - `Description string`

      - `InputSchema BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `Properties map[string, any]`

          JSON Schema properties defining the tool's input parameters.

        - `Required []string`

          List of required property names.

        - `Type BetaManagedAgentsCustomToolInputSchemaType`

          Must be 'object' for tool input schemas.

          - `const BetaManagedAgentsCustomToolInputSchemaTypeObject BetaManagedAgentsCustomToolInputSchemaType = "object"`

      - `Name string`

      - `Type BetaManagedAgentsCustomToolType`

        - `const BetaManagedAgentsCustomToolTypeCustom BetaManagedAgentsCustomToolType = "custom"`

  - `Type BetaManagedAgentsAgentType`

    - `const BetaManagedAgentsAgentTypeAgent BetaManagedAgentsAgentType = "agent"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Version int64`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaManagedAgentsAgent, err := client.Beta.Agents.Update(
    context.TODO(),
    "agent_011CZkYpogX7uDKUyvBTophP",
    anthropic.BetaAgentUpdateParams{
      Version: 1,
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsAgent.ID)
}
```
