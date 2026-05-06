# Threads

## List

`client.Beta.Sessions.Threads.List(ctx, sessionID, params) (*PageCursor[BetaManagedAgentsSessionThread], error)`

**get** `/v1/sessions/{session_id}/threads`

List Session Threads

### Parameters

- `sessionID string`

- `params BetaSessionThreadListParams`

  - `Limit param.Field[int64]`

    Query param: Maximum results per page. Defaults to 1000.

  - `Page param.Field[string]`

    Query param: Opaque pagination cursor from a previous response's next_page. Forward-only.

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

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

### Returns

- `type BetaManagedAgentsSessionThread struct{…}`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `ID string`

    Unique identifier for this thread.

  - `Agent BetaManagedAgentsSessionThreadAgent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

    - `ID string`

    - `Description string`

    - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

      - `Name string`

      - `Type BetaManagedAgentsMCPServerURLDefinitionType`

        - `const BetaManagedAgentsMCPServerURLDefinitionTypeURL BetaManagedAgentsMCPServerURLDefinitionType = "url"`

      - `URL string`

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

    - `Skills []BetaManagedAgentsSessionThreadAgentSkillUnion`

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

    - `Tools []BetaManagedAgentsSessionThreadAgentToolUnion`

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

    - `Type BetaManagedAgentsSessionThreadAgentType`

      - `const BetaManagedAgentsSessionThreadAgentTypeAgent BetaManagedAgentsSessionThreadAgentType = "agent"`

    - `Version int64`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `ParentThreadID string`

    Parent thread that spawned this thread. Null for the primary thread.

  - `SessionID string`

    The session this thread belongs to.

  - `Stats BetaManagedAgentsSessionThreadStats`

    Timing statistics for a session thread.

    - `ActiveSeconds float64`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `DurationSeconds float64`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `StartupSeconds float64`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `Status BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `const BetaManagedAgentsSessionThreadStatusRunning BetaManagedAgentsSessionThreadStatus = "running"`

    - `const BetaManagedAgentsSessionThreadStatusIdle BetaManagedAgentsSessionThreadStatus = "idle"`

    - `const BetaManagedAgentsSessionThreadStatusRescheduling BetaManagedAgentsSessionThreadStatus = "rescheduling"`

    - `const BetaManagedAgentsSessionThreadStatusTerminated BetaManagedAgentsSessionThreadStatus = "terminated"`

  - `Type BetaManagedAgentsSessionThreadType`

    - `const BetaManagedAgentsSessionThreadTypeSessionThread BetaManagedAgentsSessionThreadType = "session_thread"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Usage BetaManagedAgentsSessionThreadUsage`

    Cumulative token usage for a session thread across all turns.

    - `CacheCreation BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Ephemeral1hInputTokens int64`

        Tokens used to create 1-hour ephemeral cache entries.

      - `Ephemeral5mInputTokens int64`

        Tokens used to create 5-minute ephemeral cache entries.

    - `CacheReadInputTokens int64`

      Total tokens read from prompt cache.

    - `InputTokens int64`

      Total input tokens consumed across all turns.

    - `OutputTokens int64`

      Total output tokens generated across all turns.

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
  page, err := client.Beta.Sessions.Threads.List(
    context.TODO(),
    "sesn_011CZkZAtmR3yMPDzynEDxu7",
    anthropic.BetaSessionThreadListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

## Retrieve

`client.Beta.Sessions.Threads.Get(ctx, threadID, params) (*BetaManagedAgentsSessionThread, error)`

**get** `/v1/sessions/{session_id}/threads/{thread_id}`

Get Session Thread

### Parameters

- `threadID string`

- `params BetaSessionThreadGetParams`

  - `SessionID param.Field[string]`

    Path param: Path parameter session_id

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

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

### Returns

- `type BetaManagedAgentsSessionThread struct{…}`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `ID string`

    Unique identifier for this thread.

  - `Agent BetaManagedAgentsSessionThreadAgent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

    - `ID string`

    - `Description string`

    - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

      - `Name string`

      - `Type BetaManagedAgentsMCPServerURLDefinitionType`

        - `const BetaManagedAgentsMCPServerURLDefinitionTypeURL BetaManagedAgentsMCPServerURLDefinitionType = "url"`

      - `URL string`

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

    - `Skills []BetaManagedAgentsSessionThreadAgentSkillUnion`

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

    - `Tools []BetaManagedAgentsSessionThreadAgentToolUnion`

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

    - `Type BetaManagedAgentsSessionThreadAgentType`

      - `const BetaManagedAgentsSessionThreadAgentTypeAgent BetaManagedAgentsSessionThreadAgentType = "agent"`

    - `Version int64`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `ParentThreadID string`

    Parent thread that spawned this thread. Null for the primary thread.

  - `SessionID string`

    The session this thread belongs to.

  - `Stats BetaManagedAgentsSessionThreadStats`

    Timing statistics for a session thread.

    - `ActiveSeconds float64`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `DurationSeconds float64`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `StartupSeconds float64`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `Status BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `const BetaManagedAgentsSessionThreadStatusRunning BetaManagedAgentsSessionThreadStatus = "running"`

    - `const BetaManagedAgentsSessionThreadStatusIdle BetaManagedAgentsSessionThreadStatus = "idle"`

    - `const BetaManagedAgentsSessionThreadStatusRescheduling BetaManagedAgentsSessionThreadStatus = "rescheduling"`

    - `const BetaManagedAgentsSessionThreadStatusTerminated BetaManagedAgentsSessionThreadStatus = "terminated"`

  - `Type BetaManagedAgentsSessionThreadType`

    - `const BetaManagedAgentsSessionThreadTypeSessionThread BetaManagedAgentsSessionThreadType = "session_thread"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Usage BetaManagedAgentsSessionThreadUsage`

    Cumulative token usage for a session thread across all turns.

    - `CacheCreation BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Ephemeral1hInputTokens int64`

        Tokens used to create 1-hour ephemeral cache entries.

      - `Ephemeral5mInputTokens int64`

        Tokens used to create 5-minute ephemeral cache entries.

    - `CacheReadInputTokens int64`

      Total tokens read from prompt cache.

    - `InputTokens int64`

      Total input tokens consumed across all turns.

    - `OutputTokens int64`

      Total output tokens generated across all turns.

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
  betaManagedAgentsSessionThread, err := client.Beta.Sessions.Threads.Get(
    context.TODO(),
    "sthr_011CZkZVWa6oIjw0rgXZpnBt",
    anthropic.BetaSessionThreadGetParams{
      SessionID: "sesn_011CZkZAtmR3yMPDzynEDxu7",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsSessionThread.ID)
}
```

## Archive

`client.Beta.Sessions.Threads.Archive(ctx, threadID, params) (*BetaManagedAgentsSessionThread, error)`

**post** `/v1/sessions/{session_id}/threads/{thread_id}/archive`

Archive Session Thread

### Parameters

- `threadID string`

- `params BetaSessionThreadArchiveParams`

  - `SessionID param.Field[string]`

    Path param: Path parameter session_id

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

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

### Returns

- `type BetaManagedAgentsSessionThread struct{…}`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `ID string`

    Unique identifier for this thread.

  - `Agent BetaManagedAgentsSessionThreadAgent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

    - `ID string`

    - `Description string`

    - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

      - `Name string`

      - `Type BetaManagedAgentsMCPServerURLDefinitionType`

        - `const BetaManagedAgentsMCPServerURLDefinitionTypeURL BetaManagedAgentsMCPServerURLDefinitionType = "url"`

      - `URL string`

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

    - `Skills []BetaManagedAgentsSessionThreadAgentSkillUnion`

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

    - `Tools []BetaManagedAgentsSessionThreadAgentToolUnion`

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

    - `Type BetaManagedAgentsSessionThreadAgentType`

      - `const BetaManagedAgentsSessionThreadAgentTypeAgent BetaManagedAgentsSessionThreadAgentType = "agent"`

    - `Version int64`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `ParentThreadID string`

    Parent thread that spawned this thread. Null for the primary thread.

  - `SessionID string`

    The session this thread belongs to.

  - `Stats BetaManagedAgentsSessionThreadStats`

    Timing statistics for a session thread.

    - `ActiveSeconds float64`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `DurationSeconds float64`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `StartupSeconds float64`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `Status BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `const BetaManagedAgentsSessionThreadStatusRunning BetaManagedAgentsSessionThreadStatus = "running"`

    - `const BetaManagedAgentsSessionThreadStatusIdle BetaManagedAgentsSessionThreadStatus = "idle"`

    - `const BetaManagedAgentsSessionThreadStatusRescheduling BetaManagedAgentsSessionThreadStatus = "rescheduling"`

    - `const BetaManagedAgentsSessionThreadStatusTerminated BetaManagedAgentsSessionThreadStatus = "terminated"`

  - `Type BetaManagedAgentsSessionThreadType`

    - `const BetaManagedAgentsSessionThreadTypeSessionThread BetaManagedAgentsSessionThreadType = "session_thread"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Usage BetaManagedAgentsSessionThreadUsage`

    Cumulative token usage for a session thread across all turns.

    - `CacheCreation BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Ephemeral1hInputTokens int64`

        Tokens used to create 1-hour ephemeral cache entries.

      - `Ephemeral5mInputTokens int64`

        Tokens used to create 5-minute ephemeral cache entries.

    - `CacheReadInputTokens int64`

      Total tokens read from prompt cache.

    - `InputTokens int64`

      Total input tokens consumed across all turns.

    - `OutputTokens int64`

      Total output tokens generated across all turns.

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
  betaManagedAgentsSessionThread, err := client.Beta.Sessions.Threads.Archive(
    context.TODO(),
    "sthr_011CZkZVWa6oIjw0rgXZpnBt",
    anthropic.BetaSessionThreadArchiveParams{
      SessionID: "sesn_011CZkZAtmR3yMPDzynEDxu7",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsSessionThread.ID)
}
```

## Domain Types

### Beta Managed Agents Session Thread

- `type BetaManagedAgentsSessionThread struct{…}`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `ID string`

    Unique identifier for this thread.

  - `Agent BetaManagedAgentsSessionThreadAgent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

    - `ID string`

    - `Description string`

    - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

      - `Name string`

      - `Type BetaManagedAgentsMCPServerURLDefinitionType`

        - `const BetaManagedAgentsMCPServerURLDefinitionTypeURL BetaManagedAgentsMCPServerURLDefinitionType = "url"`

      - `URL string`

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

    - `Skills []BetaManagedAgentsSessionThreadAgentSkillUnion`

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

    - `Tools []BetaManagedAgentsSessionThreadAgentToolUnion`

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

    - `Type BetaManagedAgentsSessionThreadAgentType`

      - `const BetaManagedAgentsSessionThreadAgentTypeAgent BetaManagedAgentsSessionThreadAgentType = "agent"`

    - `Version int64`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `ParentThreadID string`

    Parent thread that spawned this thread. Null for the primary thread.

  - `SessionID string`

    The session this thread belongs to.

  - `Stats BetaManagedAgentsSessionThreadStats`

    Timing statistics for a session thread.

    - `ActiveSeconds float64`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `DurationSeconds float64`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `StartupSeconds float64`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `Status BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `const BetaManagedAgentsSessionThreadStatusRunning BetaManagedAgentsSessionThreadStatus = "running"`

    - `const BetaManagedAgentsSessionThreadStatusIdle BetaManagedAgentsSessionThreadStatus = "idle"`

    - `const BetaManagedAgentsSessionThreadStatusRescheduling BetaManagedAgentsSessionThreadStatus = "rescheduling"`

    - `const BetaManagedAgentsSessionThreadStatusTerminated BetaManagedAgentsSessionThreadStatus = "terminated"`

  - `Type BetaManagedAgentsSessionThreadType`

    - `const BetaManagedAgentsSessionThreadTypeSessionThread BetaManagedAgentsSessionThreadType = "session_thread"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Usage BetaManagedAgentsSessionThreadUsage`

    Cumulative token usage for a session thread across all turns.

    - `CacheCreation BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Ephemeral1hInputTokens int64`

        Tokens used to create 1-hour ephemeral cache entries.

      - `Ephemeral5mInputTokens int64`

        Tokens used to create 5-minute ephemeral cache entries.

    - `CacheReadInputTokens int64`

      Total tokens read from prompt cache.

    - `InputTokens int64`

      Total input tokens consumed across all turns.

    - `OutputTokens int64`

      Total output tokens generated across all turns.

### Beta Managed Agents Session Thread Agent

- `type BetaManagedAgentsSessionThreadAgent struct{…}`

  Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

  - `ID string`

  - `Description string`

  - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

    - `Name string`

    - `Type BetaManagedAgentsMCPServerURLDefinitionType`

      - `const BetaManagedAgentsMCPServerURLDefinitionTypeURL BetaManagedAgentsMCPServerURLDefinitionType = "url"`

    - `URL string`

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

  - `Skills []BetaManagedAgentsSessionThreadAgentSkillUnion`

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

  - `Tools []BetaManagedAgentsSessionThreadAgentToolUnion`

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

  - `Type BetaManagedAgentsSessionThreadAgentType`

    - `const BetaManagedAgentsSessionThreadAgentTypeAgent BetaManagedAgentsSessionThreadAgentType = "agent"`

  - `Version int64`

### Beta Managed Agents Session Thread Stats

- `type BetaManagedAgentsSessionThreadStats struct{…}`

  Timing statistics for a session thread.

  - `ActiveSeconds float64`

    Cumulative time in seconds the thread spent actively running. Excludes idle time.

  - `DurationSeconds float64`

    Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

  - `StartupSeconds float64`

    Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

### Beta Managed Agents Session Thread Status

- `type BetaManagedAgentsSessionThreadStatus string`

  SessionThreadStatus enum

  - `const BetaManagedAgentsSessionThreadStatusRunning BetaManagedAgentsSessionThreadStatus = "running"`

  - `const BetaManagedAgentsSessionThreadStatusIdle BetaManagedAgentsSessionThreadStatus = "idle"`

  - `const BetaManagedAgentsSessionThreadStatusRescheduling BetaManagedAgentsSessionThreadStatus = "rescheduling"`

  - `const BetaManagedAgentsSessionThreadStatusTerminated BetaManagedAgentsSessionThreadStatus = "terminated"`

### Beta Managed Agents Session Thread Usage

- `type BetaManagedAgentsSessionThreadUsage struct{…}`

  Cumulative token usage for a session thread across all turns.

  - `CacheCreation BetaManagedAgentsCacheCreationUsage`

    Prompt-cache creation token usage broken down by cache lifetime.

    - `Ephemeral1hInputTokens int64`

      Tokens used to create 1-hour ephemeral cache entries.

    - `Ephemeral5mInputTokens int64`

      Tokens used to create 5-minute ephemeral cache entries.

  - `CacheReadInputTokens int64`

    Total tokens read from prompt cache.

  - `InputTokens int64`

    Total input tokens consumed across all turns.

  - `OutputTokens int64`

    Total output tokens generated across all turns.

### Beta Managed Agents Stream Session Thread Events

- `type BetaManagedAgentsStreamSessionThreadEventsUnion interface{…}`

  Server-sent event in a single thread's stream.

  - `type BetaManagedAgentsUserMessageEvent struct{…}`

    A user message event in the session conversation.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsUserMessageEventContentUnion`

      Array of content blocks comprising the user message.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

        - `Type BetaManagedAgentsTextBlockType`

          - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type BetaManagedAgentsBase64ImageSourceType`

              - `const BetaManagedAgentsBase64ImageSourceTypeBase64 BetaManagedAgentsBase64ImageSourceType = "base64"`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

              - `const BetaManagedAgentsURLImageSourceTypeURL BetaManagedAgentsURLImageSourceType = "url"`

            - `URL string`

              URL of the image to fetch.

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileImageSourceType`

              - `const BetaManagedAgentsFileImageSourceTypeFile BetaManagedAgentsFileImageSourceType = "file"`

        - `Type BetaManagedAgentsImageBlockType`

          - `const BetaManagedAgentsImageBlockTypeImage BetaManagedAgentsImageBlockType = "image"`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

            - `Type BetaManagedAgentsBase64DocumentSourceType`

              - `const BetaManagedAgentsBase64DocumentSourceTypeBase64 BetaManagedAgentsBase64DocumentSourceType = "base64"`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

              - `const BetaManagedAgentsPlainTextDocumentSourceMediaTypeTextPlain BetaManagedAgentsPlainTextDocumentSourceMediaType = "text/plain"`

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

              - `const BetaManagedAgentsPlainTextDocumentSourceTypeText BetaManagedAgentsPlainTextDocumentSourceType = "text"`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

              - `const BetaManagedAgentsURLDocumentSourceTypeURL BetaManagedAgentsURLDocumentSourceType = "url"`

            - `URL string`

              URL of the document to fetch.

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileDocumentSourceType`

              - `const BetaManagedAgentsFileDocumentSourceTypeFile BetaManagedAgentsFileDocumentSourceType = "file"`

        - `Type BetaManagedAgentsDocumentBlockType`

          - `const BetaManagedAgentsDocumentBlockTypeDocument BetaManagedAgentsDocumentBlockType = "document"`

        - `Context string`

          Additional context about the document for the model.

        - `Title string`

          The title of the document.

    - `Type BetaManagedAgentsUserMessageEventType`

      - `const BetaManagedAgentsUserMessageEventTypeUserMessage BetaManagedAgentsUserMessageEventType = "user.message"`

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

  - `type BetaManagedAgentsUserInterruptEvent struct{…}`

    An interrupt event that pauses agent execution and returns control to the user.

    - `ID string`

      Unique identifier for this event.

    - `Type BetaManagedAgentsUserInterruptEventType`

      - `const BetaManagedAgentsUserInterruptEventTypeUserInterrupt BetaManagedAgentsUserInterruptEventType = "user.interrupt"`

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `SessionThreadID string`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `type BetaManagedAgentsUserToolConfirmationEvent struct{…}`

    A tool confirmation event that approves or denies a pending tool execution.

    - `ID string`

      Unique identifier for this event.

    - `Result BetaManagedAgentsUserToolConfirmationEventResult`

      UserToolConfirmationResult enum

      - `const BetaManagedAgentsUserToolConfirmationEventResultAllow BetaManagedAgentsUserToolConfirmationEventResult = "allow"`

      - `const BetaManagedAgentsUserToolConfirmationEventResultDeny BetaManagedAgentsUserToolConfirmationEventResult = "deny"`

    - `ToolUseID string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type BetaManagedAgentsUserToolConfirmationEventType`

      - `const BetaManagedAgentsUserToolConfirmationEventTypeUserToolConfirmation BetaManagedAgentsUserToolConfirmationEventType = "user.tool_confirmation"`

    - `DenyMessage string`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `SessionThreadID string`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `type BetaManagedAgentsUserCustomToolResultEvent struct{…}`

    Event sent by the client providing the result of a custom tool execution.

    - `ID string`

      Unique identifier for this event.

    - `CustomToolUseID string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type BetaManagedAgentsUserCustomToolResultEventType`

      - `const BetaManagedAgentsUserCustomToolResultEventTypeUserCustomToolResult BetaManagedAgentsUserCustomToolResultEventType = "user.custom_tool_result"`

    - `Content []BetaManagedAgentsUserCustomToolResultEventContentUnion`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

        - `Type BetaManagedAgentsTextBlockType`

          - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type BetaManagedAgentsBase64ImageSourceType`

              - `const BetaManagedAgentsBase64ImageSourceTypeBase64 BetaManagedAgentsBase64ImageSourceType = "base64"`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

              - `const BetaManagedAgentsURLImageSourceTypeURL BetaManagedAgentsURLImageSourceType = "url"`

            - `URL string`

              URL of the image to fetch.

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileImageSourceType`

              - `const BetaManagedAgentsFileImageSourceTypeFile BetaManagedAgentsFileImageSourceType = "file"`

        - `Type BetaManagedAgentsImageBlockType`

          - `const BetaManagedAgentsImageBlockTypeImage BetaManagedAgentsImageBlockType = "image"`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

            - `Type BetaManagedAgentsBase64DocumentSourceType`

              - `const BetaManagedAgentsBase64DocumentSourceTypeBase64 BetaManagedAgentsBase64DocumentSourceType = "base64"`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

              - `const BetaManagedAgentsPlainTextDocumentSourceMediaTypeTextPlain BetaManagedAgentsPlainTextDocumentSourceMediaType = "text/plain"`

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

              - `const BetaManagedAgentsPlainTextDocumentSourceTypeText BetaManagedAgentsPlainTextDocumentSourceType = "text"`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

              - `const BetaManagedAgentsURLDocumentSourceTypeURL BetaManagedAgentsURLDocumentSourceType = "url"`

            - `URL string`

              URL of the document to fetch.

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileDocumentSourceType`

              - `const BetaManagedAgentsFileDocumentSourceTypeFile BetaManagedAgentsFileDocumentSourceType = "file"`

        - `Type BetaManagedAgentsDocumentBlockType`

          - `const BetaManagedAgentsDocumentBlockTypeDocument BetaManagedAgentsDocumentBlockType = "document"`

        - `Context string`

          Additional context about the document for the model.

        - `Title string`

          The title of the document.

    - `IsError bool`

      Whether the tool execution resulted in an error.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `SessionThreadID string`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `type BetaManagedAgentsAgentCustomToolUseEvent struct{…}`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `Name string`

      Name of the custom tool being called.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentCustomToolUseEventType`

      - `const BetaManagedAgentsAgentCustomToolUseEventTypeAgentCustomToolUse BetaManagedAgentsAgentCustomToolUseEventType = "agent.custom_tool_use"`

    - `SessionThreadID string`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `type BetaManagedAgentsAgentMessageEvent struct{…}`

    An agent response event in the session conversation.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsTextBlock`

      Array of text blocks comprising the agent response.

      - `Text string`

        The text content.

      - `Type BetaManagedAgentsTextBlockType`

        - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentMessageEventType`

      - `const BetaManagedAgentsAgentMessageEventTypeAgentMessage BetaManagedAgentsAgentMessageEventType = "agent.message"`

  - `type BetaManagedAgentsAgentThinkingEvent struct{…}`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentThinkingEventType`

      - `const BetaManagedAgentsAgentThinkingEventTypeAgentThinking BetaManagedAgentsAgentThinkingEventType = "agent.thinking"`

  - `type BetaManagedAgentsAgentMCPToolUseEvent struct{…}`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `MCPServerName string`

      Name of the MCP server providing the tool.

    - `Name string`

      Name of the MCP tool being used.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentMCPToolUseEventType`

      - `const BetaManagedAgentsAgentMCPToolUseEventTypeAgentMCPToolUse BetaManagedAgentsAgentMCPToolUseEventType = "agent.mcp_tool_use"`

    - `EvaluatedPermission BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission`

      AgentEvaluatedPermission enum

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "allow"`

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "ask"`

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "deny"`

    - `SessionThreadID string`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `type BetaManagedAgentsAgentMCPToolResultEvent struct{…}`

    Event representing the result of an MCP tool execution.

    - `ID string`

      Unique identifier for this event.

    - `MCPToolUseID string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentMCPToolResultEventType`

      - `const BetaManagedAgentsAgentMCPToolResultEventTypeAgentMCPToolResult BetaManagedAgentsAgentMCPToolResultEventType = "agent.mcp_tool_result"`

    - `Content []BetaManagedAgentsAgentMCPToolResultEventContentUnion`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

        - `Type BetaManagedAgentsTextBlockType`

          - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type BetaManagedAgentsBase64ImageSourceType`

              - `const BetaManagedAgentsBase64ImageSourceTypeBase64 BetaManagedAgentsBase64ImageSourceType = "base64"`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

              - `const BetaManagedAgentsURLImageSourceTypeURL BetaManagedAgentsURLImageSourceType = "url"`

            - `URL string`

              URL of the image to fetch.

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileImageSourceType`

              - `const BetaManagedAgentsFileImageSourceTypeFile BetaManagedAgentsFileImageSourceType = "file"`

        - `Type BetaManagedAgentsImageBlockType`

          - `const BetaManagedAgentsImageBlockTypeImage BetaManagedAgentsImageBlockType = "image"`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

            - `Type BetaManagedAgentsBase64DocumentSourceType`

              - `const BetaManagedAgentsBase64DocumentSourceTypeBase64 BetaManagedAgentsBase64DocumentSourceType = "base64"`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

              - `const BetaManagedAgentsPlainTextDocumentSourceMediaTypeTextPlain BetaManagedAgentsPlainTextDocumentSourceMediaType = "text/plain"`

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

              - `const BetaManagedAgentsPlainTextDocumentSourceTypeText BetaManagedAgentsPlainTextDocumentSourceType = "text"`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

              - `const BetaManagedAgentsURLDocumentSourceTypeURL BetaManagedAgentsURLDocumentSourceType = "url"`

            - `URL string`

              URL of the document to fetch.

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileDocumentSourceType`

              - `const BetaManagedAgentsFileDocumentSourceTypeFile BetaManagedAgentsFileDocumentSourceType = "file"`

        - `Type BetaManagedAgentsDocumentBlockType`

          - `const BetaManagedAgentsDocumentBlockTypeDocument BetaManagedAgentsDocumentBlockType = "document"`

        - `Context string`

          Additional context about the document for the model.

        - `Title string`

          The title of the document.

    - `IsError bool`

      Whether the tool execution resulted in an error.

  - `type BetaManagedAgentsAgentToolUseEvent struct{…}`

    Event emitted when the agent invokes a built-in agent tool.

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `Name string`

      Name of the agent tool being used.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentToolUseEventType`

      - `const BetaManagedAgentsAgentToolUseEventTypeAgentToolUse BetaManagedAgentsAgentToolUseEventType = "agent.tool_use"`

    - `EvaluatedPermission BetaManagedAgentsAgentToolUseEventEvaluatedPermission`

      AgentEvaluatedPermission enum

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "allow"`

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "ask"`

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "deny"`

    - `SessionThreadID string`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `type BetaManagedAgentsAgentToolResultEvent struct{…}`

    Event representing the result of an agent tool execution.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `ToolUseID string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type BetaManagedAgentsAgentToolResultEventType`

      - `const BetaManagedAgentsAgentToolResultEventTypeAgentToolResult BetaManagedAgentsAgentToolResultEventType = "agent.tool_result"`

    - `Content []BetaManagedAgentsAgentToolResultEventContentUnion`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

        - `Type BetaManagedAgentsTextBlockType`

          - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type BetaManagedAgentsBase64ImageSourceType`

              - `const BetaManagedAgentsBase64ImageSourceTypeBase64 BetaManagedAgentsBase64ImageSourceType = "base64"`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

              - `const BetaManagedAgentsURLImageSourceTypeURL BetaManagedAgentsURLImageSourceType = "url"`

            - `URL string`

              URL of the image to fetch.

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileImageSourceType`

              - `const BetaManagedAgentsFileImageSourceTypeFile BetaManagedAgentsFileImageSourceType = "file"`

        - `Type BetaManagedAgentsImageBlockType`

          - `const BetaManagedAgentsImageBlockTypeImage BetaManagedAgentsImageBlockType = "image"`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

            - `Type BetaManagedAgentsBase64DocumentSourceType`

              - `const BetaManagedAgentsBase64DocumentSourceTypeBase64 BetaManagedAgentsBase64DocumentSourceType = "base64"`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

              - `const BetaManagedAgentsPlainTextDocumentSourceMediaTypeTextPlain BetaManagedAgentsPlainTextDocumentSourceMediaType = "text/plain"`

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

              - `const BetaManagedAgentsPlainTextDocumentSourceTypeText BetaManagedAgentsPlainTextDocumentSourceType = "text"`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

              - `const BetaManagedAgentsURLDocumentSourceTypeURL BetaManagedAgentsURLDocumentSourceType = "url"`

            - `URL string`

              URL of the document to fetch.

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileDocumentSourceType`

              - `const BetaManagedAgentsFileDocumentSourceTypeFile BetaManagedAgentsFileDocumentSourceType = "file"`

        - `Type BetaManagedAgentsDocumentBlockType`

          - `const BetaManagedAgentsDocumentBlockTypeDocument BetaManagedAgentsDocumentBlockType = "document"`

        - `Context string`

          Additional context about the document for the model.

        - `Title string`

          The title of the document.

    - `IsError bool`

      Whether the tool execution resulted in an error.

  - `type BetaManagedAgentsAgentThreadMessageReceivedEvent struct{…}`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsAgentThreadMessageReceivedEventContentUnion`

      Message content blocks.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

        - `Type BetaManagedAgentsTextBlockType`

          - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type BetaManagedAgentsBase64ImageSourceType`

              - `const BetaManagedAgentsBase64ImageSourceTypeBase64 BetaManagedAgentsBase64ImageSourceType = "base64"`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

              - `const BetaManagedAgentsURLImageSourceTypeURL BetaManagedAgentsURLImageSourceType = "url"`

            - `URL string`

              URL of the image to fetch.

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileImageSourceType`

              - `const BetaManagedAgentsFileImageSourceTypeFile BetaManagedAgentsFileImageSourceType = "file"`

        - `Type BetaManagedAgentsImageBlockType`

          - `const BetaManagedAgentsImageBlockTypeImage BetaManagedAgentsImageBlockType = "image"`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

            - `Type BetaManagedAgentsBase64DocumentSourceType`

              - `const BetaManagedAgentsBase64DocumentSourceTypeBase64 BetaManagedAgentsBase64DocumentSourceType = "base64"`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

              - `const BetaManagedAgentsPlainTextDocumentSourceMediaTypeTextPlain BetaManagedAgentsPlainTextDocumentSourceMediaType = "text/plain"`

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

              - `const BetaManagedAgentsPlainTextDocumentSourceTypeText BetaManagedAgentsPlainTextDocumentSourceType = "text"`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

              - `const BetaManagedAgentsURLDocumentSourceTypeURL BetaManagedAgentsURLDocumentSourceType = "url"`

            - `URL string`

              URL of the document to fetch.

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileDocumentSourceType`

              - `const BetaManagedAgentsFileDocumentSourceTypeFile BetaManagedAgentsFileDocumentSourceType = "file"`

        - `Type BetaManagedAgentsDocumentBlockType`

          - `const BetaManagedAgentsDocumentBlockTypeDocument BetaManagedAgentsDocumentBlockType = "document"`

        - `Context string`

          Additional context about the document for the model.

        - `Title string`

          The title of the document.

    - `FromSessionThreadID string`

      Public `sthr_` ID of the thread that sent the message.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentThreadMessageReceivedEventType`

      - `const BetaManagedAgentsAgentThreadMessageReceivedEventTypeAgentThreadMessageReceived BetaManagedAgentsAgentThreadMessageReceivedEventType = "agent.thread_message_received"`

    - `FromAgentName string`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `type BetaManagedAgentsAgentThreadMessageSentEvent struct{…}`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsAgentThreadMessageSentEventContentUnion`

      Message content blocks.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

        - `Type BetaManagedAgentsTextBlockType`

          - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type BetaManagedAgentsBase64ImageSourceType`

              - `const BetaManagedAgentsBase64ImageSourceTypeBase64 BetaManagedAgentsBase64ImageSourceType = "base64"`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

              - `const BetaManagedAgentsURLImageSourceTypeURL BetaManagedAgentsURLImageSourceType = "url"`

            - `URL string`

              URL of the image to fetch.

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileImageSourceType`

              - `const BetaManagedAgentsFileImageSourceTypeFile BetaManagedAgentsFileImageSourceType = "file"`

        - `Type BetaManagedAgentsImageBlockType`

          - `const BetaManagedAgentsImageBlockTypeImage BetaManagedAgentsImageBlockType = "image"`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

            - `Type BetaManagedAgentsBase64DocumentSourceType`

              - `const BetaManagedAgentsBase64DocumentSourceTypeBase64 BetaManagedAgentsBase64DocumentSourceType = "base64"`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

              - `const BetaManagedAgentsPlainTextDocumentSourceMediaTypeTextPlain BetaManagedAgentsPlainTextDocumentSourceMediaType = "text/plain"`

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

              - `const BetaManagedAgentsPlainTextDocumentSourceTypeText BetaManagedAgentsPlainTextDocumentSourceType = "text"`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

              - `const BetaManagedAgentsURLDocumentSourceTypeURL BetaManagedAgentsURLDocumentSourceType = "url"`

            - `URL string`

              URL of the document to fetch.

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileDocumentSourceType`

              - `const BetaManagedAgentsFileDocumentSourceTypeFile BetaManagedAgentsFileDocumentSourceType = "file"`

        - `Type BetaManagedAgentsDocumentBlockType`

          - `const BetaManagedAgentsDocumentBlockTypeDocument BetaManagedAgentsDocumentBlockType = "document"`

        - `Context string`

          Additional context about the document for the model.

        - `Title string`

          The title of the document.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `ToSessionThreadID string`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type BetaManagedAgentsAgentThreadMessageSentEventType`

      - `const BetaManagedAgentsAgentThreadMessageSentEventTypeAgentThreadMessageSent BetaManagedAgentsAgentThreadMessageSentEventType = "agent.thread_message_sent"`

    - `ToAgentName string`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `type BetaManagedAgentsAgentThreadContextCompactedEvent struct{…}`

    Indicates that context compaction (summarization) occurred during the session.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentThreadContextCompactedEventType`

      - `const BetaManagedAgentsAgentThreadContextCompactedEventTypeAgentThreadContextCompacted BetaManagedAgentsAgentThreadContextCompactedEventType = "agent.thread_context_compacted"`

  - `type BetaManagedAgentsSessionErrorEvent struct{…}`

    An error event indicating a problem occurred during session execution.

    - `ID string`

      Unique identifier for this event.

    - `Error BetaManagedAgentsSessionErrorEventErrorUnion`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `type BetaManagedAgentsUnknownError struct{…}`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsUnknownErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsUnknownErrorType`

          - `const BetaManagedAgentsUnknownErrorTypeUnknownError BetaManagedAgentsUnknownErrorType = "unknown_error"`

      - `type BetaManagedAgentsModelOverloadedError struct{…}`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsModelOverloadedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsModelOverloadedErrorType`

          - `const BetaManagedAgentsModelOverloadedErrorTypeModelOverloadedError BetaManagedAgentsModelOverloadedErrorType = "model_overloaded_error"`

      - `type BetaManagedAgentsModelRateLimitedError struct{…}`

        The model request was rate-limited.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsModelRateLimitedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsModelRateLimitedErrorType`

          - `const BetaManagedAgentsModelRateLimitedErrorTypeModelRateLimitedError BetaManagedAgentsModelRateLimitedErrorType = "model_rate_limited_error"`

      - `type BetaManagedAgentsModelRequestFailedError struct{…}`

        A model request failed for a reason other than overload or rate-limiting.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsModelRequestFailedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsModelRequestFailedErrorType`

          - `const BetaManagedAgentsModelRequestFailedErrorTypeModelRequestFailedError BetaManagedAgentsModelRequestFailedErrorType = "model_request_failed_error"`

      - `type BetaManagedAgentsMCPConnectionFailedError struct{…}`

        Failed to connect to an MCP server.

        - `MCPServerName string`

          Name of the MCP server that failed to connect.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsMCPConnectionFailedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsMCPConnectionFailedErrorType`

          - `const BetaManagedAgentsMCPConnectionFailedErrorTypeMCPConnectionFailedError BetaManagedAgentsMCPConnectionFailedErrorType = "mcp_connection_failed_error"`

      - `type BetaManagedAgentsMCPAuthenticationFailedError struct{…}`

        Authentication to an MCP server failed.

        - `MCPServerName string`

          Name of the MCP server that failed authentication.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsMCPAuthenticationFailedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsMCPAuthenticationFailedErrorType`

          - `const BetaManagedAgentsMCPAuthenticationFailedErrorTypeMCPAuthenticationFailedError BetaManagedAgentsMCPAuthenticationFailedErrorType = "mcp_authentication_failed_error"`

      - `type BetaManagedAgentsBillingError struct{…}`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsBillingErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsBillingErrorType`

          - `const BetaManagedAgentsBillingErrorTypeBillingError BetaManagedAgentsBillingErrorType = "billing_error"`

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSessionErrorEventType`

      - `const BetaManagedAgentsSessionErrorEventTypeSessionError BetaManagedAgentsSessionErrorEventType = "session.error"`

  - `type BetaManagedAgentsSessionStatusRescheduledEvent struct{…}`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSessionStatusRescheduledEventType`

      - `const BetaManagedAgentsSessionStatusRescheduledEventTypeSessionStatusRescheduled BetaManagedAgentsSessionStatusRescheduledEventType = "session.status_rescheduled"`

  - `type BetaManagedAgentsSessionStatusRunningEvent struct{…}`

    Indicates the session is actively running and the agent is working.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSessionStatusRunningEventType`

      - `const BetaManagedAgentsSessionStatusRunningEventTypeSessionStatusRunning BetaManagedAgentsSessionStatusRunningEventType = "session.status_running"`

  - `type BetaManagedAgentsSessionStatusIdleEvent struct{…}`

    Indicates the agent has paused and is awaiting user input.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `StopReason BetaManagedAgentsSessionStatusIdleEventStopReasonUnion`

      The agent completed its turn naturally and is ready for the next user message.

      - `type BetaManagedAgentsSessionEndTurn struct{…}`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type BetaManagedAgentsSessionEndTurnType`

          - `const BetaManagedAgentsSessionEndTurnTypeEndTurn BetaManagedAgentsSessionEndTurnType = "end_turn"`

      - `type BetaManagedAgentsSessionRequiresAction struct{…}`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `EventIDs []string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type BetaManagedAgentsSessionRequiresActionType`

          - `const BetaManagedAgentsSessionRequiresActionTypeRequiresAction BetaManagedAgentsSessionRequiresActionType = "requires_action"`

      - `type BetaManagedAgentsSessionRetriesExhausted struct{…}`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `Type BetaManagedAgentsSessionRetriesExhaustedType`

          - `const BetaManagedAgentsSessionRetriesExhaustedTypeRetriesExhausted BetaManagedAgentsSessionRetriesExhaustedType = "retries_exhausted"`

    - `Type BetaManagedAgentsSessionStatusIdleEventType`

      - `const BetaManagedAgentsSessionStatusIdleEventTypeSessionStatusIdle BetaManagedAgentsSessionStatusIdleEventType = "session.status_idle"`

  - `type BetaManagedAgentsSessionStatusTerminatedEvent struct{…}`

    Indicates the session has terminated, either due to an error or completion.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSessionStatusTerminatedEventType`

      - `const BetaManagedAgentsSessionStatusTerminatedEventTypeSessionStatusTerminated BetaManagedAgentsSessionStatusTerminatedEventType = "session.status_terminated"`

  - `type BetaManagedAgentsSessionThreadCreatedEvent struct{…}`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the callable agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `SessionThreadID string`

      Public `sthr_` ID of the newly created thread.

    - `Type BetaManagedAgentsSessionThreadCreatedEventType`

      - `const BetaManagedAgentsSessionThreadCreatedEventTypeSessionThreadCreated BetaManagedAgentsSessionThreadCreatedEventType = "session.thread_created"`

  - `type BetaManagedAgentsSpanOutcomeEvaluationStartEvent struct{…}`

    Emitted when an outcome evaluation cycle begins.

    - `ID string`

      Unique identifier for this event.

    - `Iteration int64`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `OutcomeID string`

      The `outc_` ID of the outcome being evaluated.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSpanOutcomeEvaluationStartEventType`

      - `const BetaManagedAgentsSpanOutcomeEvaluationStartEventTypeSpanOutcomeEvaluationStart BetaManagedAgentsSpanOutcomeEvaluationStartEventType = "span.outcome_evaluation_start"`

  - `type BetaManagedAgentsSpanOutcomeEvaluationEndEvent struct{…}`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `ID string`

      Unique identifier for this event.

    - `Explanation string`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `Iteration int64`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `OutcomeEvaluationStartID string`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `OutcomeID string`

      The `outc_` ID of the outcome being evaluated.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Result string`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type BetaManagedAgentsSpanOutcomeEvaluationEndEventType`

      - `const BetaManagedAgentsSpanOutcomeEvaluationEndEventTypeSpanOutcomeEvaluationEnd BetaManagedAgentsSpanOutcomeEvaluationEndEventType = "span.outcome_evaluation_end"`

    - `Usage BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `CacheCreationInputTokens int64`

        Tokens used to create prompt cache in this request.

      - `CacheReadInputTokens int64`

        Tokens read from prompt cache in this request.

      - `InputTokens int64`

        Input tokens consumed by this request.

      - `OutputTokens int64`

        Output tokens generated by this request.

      - `Speed BetaManagedAgentsSpanModelUsageSpeed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `const BetaManagedAgentsSpanModelUsageSpeedStandard BetaManagedAgentsSpanModelUsageSpeed = "standard"`

        - `const BetaManagedAgentsSpanModelUsageSpeedFast BetaManagedAgentsSpanModelUsageSpeed = "fast"`

  - `type BetaManagedAgentsSpanModelRequestStartEvent struct{…}`

    Emitted when a model request is initiated by the agent.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSpanModelRequestStartEventType`

      - `const BetaManagedAgentsSpanModelRequestStartEventTypeSpanModelRequestStart BetaManagedAgentsSpanModelRequestStartEventType = "span.model_request_start"`

  - `type BetaManagedAgentsSpanModelRequestEndEvent struct{…}`

    Emitted when a model request completes.

    - `ID string`

      Unique identifier for this event.

    - `IsError bool`

      Whether the model request resulted in an error.

    - `ModelRequestStartID string`

      The id of the corresponding `span.model_request_start` event.

    - `ModelUsage BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `CacheCreationInputTokens int64`

        Tokens used to create prompt cache in this request.

      - `CacheReadInputTokens int64`

        Tokens read from prompt cache in this request.

      - `InputTokens int64`

        Input tokens consumed by this request.

      - `OutputTokens int64`

        Output tokens generated by this request.

      - `Speed BetaManagedAgentsSpanModelUsageSpeed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `const BetaManagedAgentsSpanModelUsageSpeedStandard BetaManagedAgentsSpanModelUsageSpeed = "standard"`

        - `const BetaManagedAgentsSpanModelUsageSpeedFast BetaManagedAgentsSpanModelUsageSpeed = "fast"`

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSpanModelRequestEndEventType`

      - `const BetaManagedAgentsSpanModelRequestEndEventTypeSpanModelRequestEnd BetaManagedAgentsSpanModelRequestEndEventType = "span.model_request_end"`

  - `type BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent struct{…}`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `ID string`

      Unique identifier for this event.

    - `Iteration int64`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `OutcomeID string`

      The `outc_` ID of the outcome being evaluated.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSpanOutcomeEvaluationOngoingEventType`

      - `const BetaManagedAgentsSpanOutcomeEvaluationOngoingEventTypeSpanOutcomeEvaluationOngoing BetaManagedAgentsSpanOutcomeEvaluationOngoingEventType = "span.outcome_evaluation_ongoing"`

  - `type BetaManagedAgentsUserDefineOutcomeEvent struct{…}`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `ID string`

      Unique identifier for this event.

    - `Description string`

      What the agent should produce. Copied from the input event.

    - `MaxIterations int64`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `OutcomeID string`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Rubric BetaManagedAgentsUserDefineOutcomeEventRubricUnion`

      Rubric for grading the quality of an outcome.

      - `type BetaManagedAgentsFileRubric struct{…}`

        Rubric referenced by a file uploaded via the Files API.

        - `FileID string`

          ID of the rubric file.

        - `Type BetaManagedAgentsFileRubricType`

          - `const BetaManagedAgentsFileRubricTypeFile BetaManagedAgentsFileRubricType = "file"`

      - `type BetaManagedAgentsTextRubric struct{…}`

        Rubric content provided inline as text.

        - `Content string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `Type BetaManagedAgentsTextRubricType`

          - `const BetaManagedAgentsTextRubricTypeText BetaManagedAgentsTextRubricType = "text"`

    - `Type BetaManagedAgentsUserDefineOutcomeEventType`

      - `const BetaManagedAgentsUserDefineOutcomeEventTypeUserDefineOutcome BetaManagedAgentsUserDefineOutcomeEventType = "user.define_outcome"`

  - `type BetaManagedAgentsSessionDeletedEvent struct{…}`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSessionDeletedEventType`

      - `const BetaManagedAgentsSessionDeletedEventTypeSessionDeleted BetaManagedAgentsSessionDeletedEventType = "session.deleted"`

  - `type BetaManagedAgentsSessionThreadStatusRunningEvent struct{…}`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `SessionThreadID string`

      Public sthr_ ID of the thread that started running.

    - `Type BetaManagedAgentsSessionThreadStatusRunningEventType`

      - `const BetaManagedAgentsSessionThreadStatusRunningEventTypeSessionThreadStatusRunning BetaManagedAgentsSessionThreadStatusRunningEventType = "session.thread_status_running"`

  - `type BetaManagedAgentsSessionThreadStatusIdleEvent struct{…}`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `SessionThreadID string`

      Public sthr_ ID of the thread that went idle.

    - `StopReason BetaManagedAgentsSessionThreadStatusIdleEventStopReasonUnion`

      The agent completed its turn naturally and is ready for the next user message.

      - `type BetaManagedAgentsSessionEndTurn struct{…}`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type BetaManagedAgentsSessionEndTurnType`

          - `const BetaManagedAgentsSessionEndTurnTypeEndTurn BetaManagedAgentsSessionEndTurnType = "end_turn"`

      - `type BetaManagedAgentsSessionRequiresAction struct{…}`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `EventIDs []string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type BetaManagedAgentsSessionRequiresActionType`

          - `const BetaManagedAgentsSessionRequiresActionTypeRequiresAction BetaManagedAgentsSessionRequiresActionType = "requires_action"`

      - `type BetaManagedAgentsSessionRetriesExhausted struct{…}`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `Type BetaManagedAgentsSessionRetriesExhaustedType`

          - `const BetaManagedAgentsSessionRetriesExhaustedTypeRetriesExhausted BetaManagedAgentsSessionRetriesExhaustedType = "retries_exhausted"`

    - `Type BetaManagedAgentsSessionThreadStatusIdleEventType`

      - `const BetaManagedAgentsSessionThreadStatusIdleEventTypeSessionThreadStatusIdle BetaManagedAgentsSessionThreadStatusIdleEventType = "session.thread_status_idle"`

  - `type BetaManagedAgentsSessionThreadStatusTerminatedEvent struct{…}`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `SessionThreadID string`

      Public sthr_ ID of the thread that terminated.

    - `Type BetaManagedAgentsSessionThreadStatusTerminatedEventType`

      - `const BetaManagedAgentsSessionThreadStatusTerminatedEventTypeSessionThreadStatusTerminated BetaManagedAgentsSessionThreadStatusTerminatedEventType = "session.thread_status_terminated"`

  - `type BetaManagedAgentsSessionThreadStatusRescheduledEvent struct{…}`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `SessionThreadID string`

      Public sthr_ ID of the thread that is retrying.

    - `Type BetaManagedAgentsSessionThreadStatusRescheduledEventType`

      - `const BetaManagedAgentsSessionThreadStatusRescheduledEventTypeSessionThreadStatusRescheduled BetaManagedAgentsSessionThreadStatusRescheduledEventType = "session.thread_status_rescheduled"`

# Events

## List

`client.Beta.Sessions.Threads.Events.List(ctx, threadID, params) (*PageCursor[BetaManagedAgentsSessionEventUnion], error)`

**get** `/v1/sessions/{session_id}/threads/{thread_id}/events`

List Session Thread Events

### Parameters

- `threadID string`

- `params BetaSessionThreadEventListParams`

  - `SessionID param.Field[string]`

    Path param: Path parameter session_id

  - `Limit param.Field[int64]`

    Query param: Query parameter for limit

  - `Page param.Field[string]`

    Query param: Query parameter for page

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

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

### Returns

- `type BetaManagedAgentsSessionEventUnion interface{…}`

  Union type for all event types in a session.

  - `type BetaManagedAgentsUserMessageEvent struct{…}`

    A user message event in the session conversation.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsUserMessageEventContentUnion`

      Array of content blocks comprising the user message.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

        - `Type BetaManagedAgentsTextBlockType`

          - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type BetaManagedAgentsBase64ImageSourceType`

              - `const BetaManagedAgentsBase64ImageSourceTypeBase64 BetaManagedAgentsBase64ImageSourceType = "base64"`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

              - `const BetaManagedAgentsURLImageSourceTypeURL BetaManagedAgentsURLImageSourceType = "url"`

            - `URL string`

              URL of the image to fetch.

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileImageSourceType`

              - `const BetaManagedAgentsFileImageSourceTypeFile BetaManagedAgentsFileImageSourceType = "file"`

        - `Type BetaManagedAgentsImageBlockType`

          - `const BetaManagedAgentsImageBlockTypeImage BetaManagedAgentsImageBlockType = "image"`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

            - `Type BetaManagedAgentsBase64DocumentSourceType`

              - `const BetaManagedAgentsBase64DocumentSourceTypeBase64 BetaManagedAgentsBase64DocumentSourceType = "base64"`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

              - `const BetaManagedAgentsPlainTextDocumentSourceMediaTypeTextPlain BetaManagedAgentsPlainTextDocumentSourceMediaType = "text/plain"`

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

              - `const BetaManagedAgentsPlainTextDocumentSourceTypeText BetaManagedAgentsPlainTextDocumentSourceType = "text"`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

              - `const BetaManagedAgentsURLDocumentSourceTypeURL BetaManagedAgentsURLDocumentSourceType = "url"`

            - `URL string`

              URL of the document to fetch.

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileDocumentSourceType`

              - `const BetaManagedAgentsFileDocumentSourceTypeFile BetaManagedAgentsFileDocumentSourceType = "file"`

        - `Type BetaManagedAgentsDocumentBlockType`

          - `const BetaManagedAgentsDocumentBlockTypeDocument BetaManagedAgentsDocumentBlockType = "document"`

        - `Context string`

          Additional context about the document for the model.

        - `Title string`

          The title of the document.

    - `Type BetaManagedAgentsUserMessageEventType`

      - `const BetaManagedAgentsUserMessageEventTypeUserMessage BetaManagedAgentsUserMessageEventType = "user.message"`

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

  - `type BetaManagedAgentsUserInterruptEvent struct{…}`

    An interrupt event that pauses agent execution and returns control to the user.

    - `ID string`

      Unique identifier for this event.

    - `Type BetaManagedAgentsUserInterruptEventType`

      - `const BetaManagedAgentsUserInterruptEventTypeUserInterrupt BetaManagedAgentsUserInterruptEventType = "user.interrupt"`

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `SessionThreadID string`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `type BetaManagedAgentsUserToolConfirmationEvent struct{…}`

    A tool confirmation event that approves or denies a pending tool execution.

    - `ID string`

      Unique identifier for this event.

    - `Result BetaManagedAgentsUserToolConfirmationEventResult`

      UserToolConfirmationResult enum

      - `const BetaManagedAgentsUserToolConfirmationEventResultAllow BetaManagedAgentsUserToolConfirmationEventResult = "allow"`

      - `const BetaManagedAgentsUserToolConfirmationEventResultDeny BetaManagedAgentsUserToolConfirmationEventResult = "deny"`

    - `ToolUseID string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type BetaManagedAgentsUserToolConfirmationEventType`

      - `const BetaManagedAgentsUserToolConfirmationEventTypeUserToolConfirmation BetaManagedAgentsUserToolConfirmationEventType = "user.tool_confirmation"`

    - `DenyMessage string`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `SessionThreadID string`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `type BetaManagedAgentsUserCustomToolResultEvent struct{…}`

    Event sent by the client providing the result of a custom tool execution.

    - `ID string`

      Unique identifier for this event.

    - `CustomToolUseID string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type BetaManagedAgentsUserCustomToolResultEventType`

      - `const BetaManagedAgentsUserCustomToolResultEventTypeUserCustomToolResult BetaManagedAgentsUserCustomToolResultEventType = "user.custom_tool_result"`

    - `Content []BetaManagedAgentsUserCustomToolResultEventContentUnion`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

        - `Type BetaManagedAgentsTextBlockType`

          - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type BetaManagedAgentsBase64ImageSourceType`

              - `const BetaManagedAgentsBase64ImageSourceTypeBase64 BetaManagedAgentsBase64ImageSourceType = "base64"`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

              - `const BetaManagedAgentsURLImageSourceTypeURL BetaManagedAgentsURLImageSourceType = "url"`

            - `URL string`

              URL of the image to fetch.

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileImageSourceType`

              - `const BetaManagedAgentsFileImageSourceTypeFile BetaManagedAgentsFileImageSourceType = "file"`

        - `Type BetaManagedAgentsImageBlockType`

          - `const BetaManagedAgentsImageBlockTypeImage BetaManagedAgentsImageBlockType = "image"`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

            - `Type BetaManagedAgentsBase64DocumentSourceType`

              - `const BetaManagedAgentsBase64DocumentSourceTypeBase64 BetaManagedAgentsBase64DocumentSourceType = "base64"`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

              - `const BetaManagedAgentsPlainTextDocumentSourceMediaTypeTextPlain BetaManagedAgentsPlainTextDocumentSourceMediaType = "text/plain"`

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

              - `const BetaManagedAgentsPlainTextDocumentSourceTypeText BetaManagedAgentsPlainTextDocumentSourceType = "text"`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

              - `const BetaManagedAgentsURLDocumentSourceTypeURL BetaManagedAgentsURLDocumentSourceType = "url"`

            - `URL string`

              URL of the document to fetch.

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileDocumentSourceType`

              - `const BetaManagedAgentsFileDocumentSourceTypeFile BetaManagedAgentsFileDocumentSourceType = "file"`

        - `Type BetaManagedAgentsDocumentBlockType`

          - `const BetaManagedAgentsDocumentBlockTypeDocument BetaManagedAgentsDocumentBlockType = "document"`

        - `Context string`

          Additional context about the document for the model.

        - `Title string`

          The title of the document.

    - `IsError bool`

      Whether the tool execution resulted in an error.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `SessionThreadID string`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `type BetaManagedAgentsAgentCustomToolUseEvent struct{…}`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `Name string`

      Name of the custom tool being called.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentCustomToolUseEventType`

      - `const BetaManagedAgentsAgentCustomToolUseEventTypeAgentCustomToolUse BetaManagedAgentsAgentCustomToolUseEventType = "agent.custom_tool_use"`

    - `SessionThreadID string`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `type BetaManagedAgentsAgentMessageEvent struct{…}`

    An agent response event in the session conversation.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsTextBlock`

      Array of text blocks comprising the agent response.

      - `Text string`

        The text content.

      - `Type BetaManagedAgentsTextBlockType`

        - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentMessageEventType`

      - `const BetaManagedAgentsAgentMessageEventTypeAgentMessage BetaManagedAgentsAgentMessageEventType = "agent.message"`

  - `type BetaManagedAgentsAgentThinkingEvent struct{…}`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentThinkingEventType`

      - `const BetaManagedAgentsAgentThinkingEventTypeAgentThinking BetaManagedAgentsAgentThinkingEventType = "agent.thinking"`

  - `type BetaManagedAgentsAgentMCPToolUseEvent struct{…}`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `MCPServerName string`

      Name of the MCP server providing the tool.

    - `Name string`

      Name of the MCP tool being used.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentMCPToolUseEventType`

      - `const BetaManagedAgentsAgentMCPToolUseEventTypeAgentMCPToolUse BetaManagedAgentsAgentMCPToolUseEventType = "agent.mcp_tool_use"`

    - `EvaluatedPermission BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission`

      AgentEvaluatedPermission enum

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "allow"`

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "ask"`

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "deny"`

    - `SessionThreadID string`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `type BetaManagedAgentsAgentMCPToolResultEvent struct{…}`

    Event representing the result of an MCP tool execution.

    - `ID string`

      Unique identifier for this event.

    - `MCPToolUseID string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentMCPToolResultEventType`

      - `const BetaManagedAgentsAgentMCPToolResultEventTypeAgentMCPToolResult BetaManagedAgentsAgentMCPToolResultEventType = "agent.mcp_tool_result"`

    - `Content []BetaManagedAgentsAgentMCPToolResultEventContentUnion`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

        - `Type BetaManagedAgentsTextBlockType`

          - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type BetaManagedAgentsBase64ImageSourceType`

              - `const BetaManagedAgentsBase64ImageSourceTypeBase64 BetaManagedAgentsBase64ImageSourceType = "base64"`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

              - `const BetaManagedAgentsURLImageSourceTypeURL BetaManagedAgentsURLImageSourceType = "url"`

            - `URL string`

              URL of the image to fetch.

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileImageSourceType`

              - `const BetaManagedAgentsFileImageSourceTypeFile BetaManagedAgentsFileImageSourceType = "file"`

        - `Type BetaManagedAgentsImageBlockType`

          - `const BetaManagedAgentsImageBlockTypeImage BetaManagedAgentsImageBlockType = "image"`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

            - `Type BetaManagedAgentsBase64DocumentSourceType`

              - `const BetaManagedAgentsBase64DocumentSourceTypeBase64 BetaManagedAgentsBase64DocumentSourceType = "base64"`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

              - `const BetaManagedAgentsPlainTextDocumentSourceMediaTypeTextPlain BetaManagedAgentsPlainTextDocumentSourceMediaType = "text/plain"`

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

              - `const BetaManagedAgentsPlainTextDocumentSourceTypeText BetaManagedAgentsPlainTextDocumentSourceType = "text"`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

              - `const BetaManagedAgentsURLDocumentSourceTypeURL BetaManagedAgentsURLDocumentSourceType = "url"`

            - `URL string`

              URL of the document to fetch.

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileDocumentSourceType`

              - `const BetaManagedAgentsFileDocumentSourceTypeFile BetaManagedAgentsFileDocumentSourceType = "file"`

        - `Type BetaManagedAgentsDocumentBlockType`

          - `const BetaManagedAgentsDocumentBlockTypeDocument BetaManagedAgentsDocumentBlockType = "document"`

        - `Context string`

          Additional context about the document for the model.

        - `Title string`

          The title of the document.

    - `IsError bool`

      Whether the tool execution resulted in an error.

  - `type BetaManagedAgentsAgentToolUseEvent struct{…}`

    Event emitted when the agent invokes a built-in agent tool.

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `Name string`

      Name of the agent tool being used.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentToolUseEventType`

      - `const BetaManagedAgentsAgentToolUseEventTypeAgentToolUse BetaManagedAgentsAgentToolUseEventType = "agent.tool_use"`

    - `EvaluatedPermission BetaManagedAgentsAgentToolUseEventEvaluatedPermission`

      AgentEvaluatedPermission enum

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "allow"`

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "ask"`

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "deny"`

    - `SessionThreadID string`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `type BetaManagedAgentsAgentToolResultEvent struct{…}`

    Event representing the result of an agent tool execution.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `ToolUseID string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type BetaManagedAgentsAgentToolResultEventType`

      - `const BetaManagedAgentsAgentToolResultEventTypeAgentToolResult BetaManagedAgentsAgentToolResultEventType = "agent.tool_result"`

    - `Content []BetaManagedAgentsAgentToolResultEventContentUnion`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

        - `Type BetaManagedAgentsTextBlockType`

          - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type BetaManagedAgentsBase64ImageSourceType`

              - `const BetaManagedAgentsBase64ImageSourceTypeBase64 BetaManagedAgentsBase64ImageSourceType = "base64"`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

              - `const BetaManagedAgentsURLImageSourceTypeURL BetaManagedAgentsURLImageSourceType = "url"`

            - `URL string`

              URL of the image to fetch.

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileImageSourceType`

              - `const BetaManagedAgentsFileImageSourceTypeFile BetaManagedAgentsFileImageSourceType = "file"`

        - `Type BetaManagedAgentsImageBlockType`

          - `const BetaManagedAgentsImageBlockTypeImage BetaManagedAgentsImageBlockType = "image"`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

            - `Type BetaManagedAgentsBase64DocumentSourceType`

              - `const BetaManagedAgentsBase64DocumentSourceTypeBase64 BetaManagedAgentsBase64DocumentSourceType = "base64"`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

              - `const BetaManagedAgentsPlainTextDocumentSourceMediaTypeTextPlain BetaManagedAgentsPlainTextDocumentSourceMediaType = "text/plain"`

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

              - `const BetaManagedAgentsPlainTextDocumentSourceTypeText BetaManagedAgentsPlainTextDocumentSourceType = "text"`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

              - `const BetaManagedAgentsURLDocumentSourceTypeURL BetaManagedAgentsURLDocumentSourceType = "url"`

            - `URL string`

              URL of the document to fetch.

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileDocumentSourceType`

              - `const BetaManagedAgentsFileDocumentSourceTypeFile BetaManagedAgentsFileDocumentSourceType = "file"`

        - `Type BetaManagedAgentsDocumentBlockType`

          - `const BetaManagedAgentsDocumentBlockTypeDocument BetaManagedAgentsDocumentBlockType = "document"`

        - `Context string`

          Additional context about the document for the model.

        - `Title string`

          The title of the document.

    - `IsError bool`

      Whether the tool execution resulted in an error.

  - `type BetaManagedAgentsAgentThreadMessageReceivedEvent struct{…}`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsAgentThreadMessageReceivedEventContentUnion`

      Message content blocks.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

        - `Type BetaManagedAgentsTextBlockType`

          - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type BetaManagedAgentsBase64ImageSourceType`

              - `const BetaManagedAgentsBase64ImageSourceTypeBase64 BetaManagedAgentsBase64ImageSourceType = "base64"`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

              - `const BetaManagedAgentsURLImageSourceTypeURL BetaManagedAgentsURLImageSourceType = "url"`

            - `URL string`

              URL of the image to fetch.

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileImageSourceType`

              - `const BetaManagedAgentsFileImageSourceTypeFile BetaManagedAgentsFileImageSourceType = "file"`

        - `Type BetaManagedAgentsImageBlockType`

          - `const BetaManagedAgentsImageBlockTypeImage BetaManagedAgentsImageBlockType = "image"`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

            - `Type BetaManagedAgentsBase64DocumentSourceType`

              - `const BetaManagedAgentsBase64DocumentSourceTypeBase64 BetaManagedAgentsBase64DocumentSourceType = "base64"`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

              - `const BetaManagedAgentsPlainTextDocumentSourceMediaTypeTextPlain BetaManagedAgentsPlainTextDocumentSourceMediaType = "text/plain"`

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

              - `const BetaManagedAgentsPlainTextDocumentSourceTypeText BetaManagedAgentsPlainTextDocumentSourceType = "text"`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

              - `const BetaManagedAgentsURLDocumentSourceTypeURL BetaManagedAgentsURLDocumentSourceType = "url"`

            - `URL string`

              URL of the document to fetch.

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileDocumentSourceType`

              - `const BetaManagedAgentsFileDocumentSourceTypeFile BetaManagedAgentsFileDocumentSourceType = "file"`

        - `Type BetaManagedAgentsDocumentBlockType`

          - `const BetaManagedAgentsDocumentBlockTypeDocument BetaManagedAgentsDocumentBlockType = "document"`

        - `Context string`

          Additional context about the document for the model.

        - `Title string`

          The title of the document.

    - `FromSessionThreadID string`

      Public `sthr_` ID of the thread that sent the message.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentThreadMessageReceivedEventType`

      - `const BetaManagedAgentsAgentThreadMessageReceivedEventTypeAgentThreadMessageReceived BetaManagedAgentsAgentThreadMessageReceivedEventType = "agent.thread_message_received"`

    - `FromAgentName string`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `type BetaManagedAgentsAgentThreadMessageSentEvent struct{…}`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsAgentThreadMessageSentEventContentUnion`

      Message content blocks.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

        - `Type BetaManagedAgentsTextBlockType`

          - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type BetaManagedAgentsBase64ImageSourceType`

              - `const BetaManagedAgentsBase64ImageSourceTypeBase64 BetaManagedAgentsBase64ImageSourceType = "base64"`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

              - `const BetaManagedAgentsURLImageSourceTypeURL BetaManagedAgentsURLImageSourceType = "url"`

            - `URL string`

              URL of the image to fetch.

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileImageSourceType`

              - `const BetaManagedAgentsFileImageSourceTypeFile BetaManagedAgentsFileImageSourceType = "file"`

        - `Type BetaManagedAgentsImageBlockType`

          - `const BetaManagedAgentsImageBlockTypeImage BetaManagedAgentsImageBlockType = "image"`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

            - `Type BetaManagedAgentsBase64DocumentSourceType`

              - `const BetaManagedAgentsBase64DocumentSourceTypeBase64 BetaManagedAgentsBase64DocumentSourceType = "base64"`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

              - `const BetaManagedAgentsPlainTextDocumentSourceMediaTypeTextPlain BetaManagedAgentsPlainTextDocumentSourceMediaType = "text/plain"`

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

              - `const BetaManagedAgentsPlainTextDocumentSourceTypeText BetaManagedAgentsPlainTextDocumentSourceType = "text"`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

              - `const BetaManagedAgentsURLDocumentSourceTypeURL BetaManagedAgentsURLDocumentSourceType = "url"`

            - `URL string`

              URL of the document to fetch.

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileDocumentSourceType`

              - `const BetaManagedAgentsFileDocumentSourceTypeFile BetaManagedAgentsFileDocumentSourceType = "file"`

        - `Type BetaManagedAgentsDocumentBlockType`

          - `const BetaManagedAgentsDocumentBlockTypeDocument BetaManagedAgentsDocumentBlockType = "document"`

        - `Context string`

          Additional context about the document for the model.

        - `Title string`

          The title of the document.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `ToSessionThreadID string`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type BetaManagedAgentsAgentThreadMessageSentEventType`

      - `const BetaManagedAgentsAgentThreadMessageSentEventTypeAgentThreadMessageSent BetaManagedAgentsAgentThreadMessageSentEventType = "agent.thread_message_sent"`

    - `ToAgentName string`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `type BetaManagedAgentsAgentThreadContextCompactedEvent struct{…}`

    Indicates that context compaction (summarization) occurred during the session.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentThreadContextCompactedEventType`

      - `const BetaManagedAgentsAgentThreadContextCompactedEventTypeAgentThreadContextCompacted BetaManagedAgentsAgentThreadContextCompactedEventType = "agent.thread_context_compacted"`

  - `type BetaManagedAgentsSessionErrorEvent struct{…}`

    An error event indicating a problem occurred during session execution.

    - `ID string`

      Unique identifier for this event.

    - `Error BetaManagedAgentsSessionErrorEventErrorUnion`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `type BetaManagedAgentsUnknownError struct{…}`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsUnknownErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsUnknownErrorType`

          - `const BetaManagedAgentsUnknownErrorTypeUnknownError BetaManagedAgentsUnknownErrorType = "unknown_error"`

      - `type BetaManagedAgentsModelOverloadedError struct{…}`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsModelOverloadedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsModelOverloadedErrorType`

          - `const BetaManagedAgentsModelOverloadedErrorTypeModelOverloadedError BetaManagedAgentsModelOverloadedErrorType = "model_overloaded_error"`

      - `type BetaManagedAgentsModelRateLimitedError struct{…}`

        The model request was rate-limited.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsModelRateLimitedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsModelRateLimitedErrorType`

          - `const BetaManagedAgentsModelRateLimitedErrorTypeModelRateLimitedError BetaManagedAgentsModelRateLimitedErrorType = "model_rate_limited_error"`

      - `type BetaManagedAgentsModelRequestFailedError struct{…}`

        A model request failed for a reason other than overload or rate-limiting.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsModelRequestFailedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsModelRequestFailedErrorType`

          - `const BetaManagedAgentsModelRequestFailedErrorTypeModelRequestFailedError BetaManagedAgentsModelRequestFailedErrorType = "model_request_failed_error"`

      - `type BetaManagedAgentsMCPConnectionFailedError struct{…}`

        Failed to connect to an MCP server.

        - `MCPServerName string`

          Name of the MCP server that failed to connect.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsMCPConnectionFailedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsMCPConnectionFailedErrorType`

          - `const BetaManagedAgentsMCPConnectionFailedErrorTypeMCPConnectionFailedError BetaManagedAgentsMCPConnectionFailedErrorType = "mcp_connection_failed_error"`

      - `type BetaManagedAgentsMCPAuthenticationFailedError struct{…}`

        Authentication to an MCP server failed.

        - `MCPServerName string`

          Name of the MCP server that failed authentication.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsMCPAuthenticationFailedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsMCPAuthenticationFailedErrorType`

          - `const BetaManagedAgentsMCPAuthenticationFailedErrorTypeMCPAuthenticationFailedError BetaManagedAgentsMCPAuthenticationFailedErrorType = "mcp_authentication_failed_error"`

      - `type BetaManagedAgentsBillingError struct{…}`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsBillingErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsBillingErrorType`

          - `const BetaManagedAgentsBillingErrorTypeBillingError BetaManagedAgentsBillingErrorType = "billing_error"`

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSessionErrorEventType`

      - `const BetaManagedAgentsSessionErrorEventTypeSessionError BetaManagedAgentsSessionErrorEventType = "session.error"`

  - `type BetaManagedAgentsSessionStatusRescheduledEvent struct{…}`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSessionStatusRescheduledEventType`

      - `const BetaManagedAgentsSessionStatusRescheduledEventTypeSessionStatusRescheduled BetaManagedAgentsSessionStatusRescheduledEventType = "session.status_rescheduled"`

  - `type BetaManagedAgentsSessionStatusRunningEvent struct{…}`

    Indicates the session is actively running and the agent is working.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSessionStatusRunningEventType`

      - `const BetaManagedAgentsSessionStatusRunningEventTypeSessionStatusRunning BetaManagedAgentsSessionStatusRunningEventType = "session.status_running"`

  - `type BetaManagedAgentsSessionStatusIdleEvent struct{…}`

    Indicates the agent has paused and is awaiting user input.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `StopReason BetaManagedAgentsSessionStatusIdleEventStopReasonUnion`

      The agent completed its turn naturally and is ready for the next user message.

      - `type BetaManagedAgentsSessionEndTurn struct{…}`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type BetaManagedAgentsSessionEndTurnType`

          - `const BetaManagedAgentsSessionEndTurnTypeEndTurn BetaManagedAgentsSessionEndTurnType = "end_turn"`

      - `type BetaManagedAgentsSessionRequiresAction struct{…}`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `EventIDs []string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type BetaManagedAgentsSessionRequiresActionType`

          - `const BetaManagedAgentsSessionRequiresActionTypeRequiresAction BetaManagedAgentsSessionRequiresActionType = "requires_action"`

      - `type BetaManagedAgentsSessionRetriesExhausted struct{…}`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `Type BetaManagedAgentsSessionRetriesExhaustedType`

          - `const BetaManagedAgentsSessionRetriesExhaustedTypeRetriesExhausted BetaManagedAgentsSessionRetriesExhaustedType = "retries_exhausted"`

    - `Type BetaManagedAgentsSessionStatusIdleEventType`

      - `const BetaManagedAgentsSessionStatusIdleEventTypeSessionStatusIdle BetaManagedAgentsSessionStatusIdleEventType = "session.status_idle"`

  - `type BetaManagedAgentsSessionStatusTerminatedEvent struct{…}`

    Indicates the session has terminated, either due to an error or completion.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSessionStatusTerminatedEventType`

      - `const BetaManagedAgentsSessionStatusTerminatedEventTypeSessionStatusTerminated BetaManagedAgentsSessionStatusTerminatedEventType = "session.status_terminated"`

  - `type BetaManagedAgentsSessionThreadCreatedEvent struct{…}`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the callable agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `SessionThreadID string`

      Public `sthr_` ID of the newly created thread.

    - `Type BetaManagedAgentsSessionThreadCreatedEventType`

      - `const BetaManagedAgentsSessionThreadCreatedEventTypeSessionThreadCreated BetaManagedAgentsSessionThreadCreatedEventType = "session.thread_created"`

  - `type BetaManagedAgentsSpanOutcomeEvaluationStartEvent struct{…}`

    Emitted when an outcome evaluation cycle begins.

    - `ID string`

      Unique identifier for this event.

    - `Iteration int64`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `OutcomeID string`

      The `outc_` ID of the outcome being evaluated.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSpanOutcomeEvaluationStartEventType`

      - `const BetaManagedAgentsSpanOutcomeEvaluationStartEventTypeSpanOutcomeEvaluationStart BetaManagedAgentsSpanOutcomeEvaluationStartEventType = "span.outcome_evaluation_start"`

  - `type BetaManagedAgentsSpanOutcomeEvaluationEndEvent struct{…}`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `ID string`

      Unique identifier for this event.

    - `Explanation string`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `Iteration int64`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `OutcomeEvaluationStartID string`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `OutcomeID string`

      The `outc_` ID of the outcome being evaluated.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Result string`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type BetaManagedAgentsSpanOutcomeEvaluationEndEventType`

      - `const BetaManagedAgentsSpanOutcomeEvaluationEndEventTypeSpanOutcomeEvaluationEnd BetaManagedAgentsSpanOutcomeEvaluationEndEventType = "span.outcome_evaluation_end"`

    - `Usage BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `CacheCreationInputTokens int64`

        Tokens used to create prompt cache in this request.

      - `CacheReadInputTokens int64`

        Tokens read from prompt cache in this request.

      - `InputTokens int64`

        Input tokens consumed by this request.

      - `OutputTokens int64`

        Output tokens generated by this request.

      - `Speed BetaManagedAgentsSpanModelUsageSpeed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `const BetaManagedAgentsSpanModelUsageSpeedStandard BetaManagedAgentsSpanModelUsageSpeed = "standard"`

        - `const BetaManagedAgentsSpanModelUsageSpeedFast BetaManagedAgentsSpanModelUsageSpeed = "fast"`

  - `type BetaManagedAgentsSpanModelRequestStartEvent struct{…}`

    Emitted when a model request is initiated by the agent.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSpanModelRequestStartEventType`

      - `const BetaManagedAgentsSpanModelRequestStartEventTypeSpanModelRequestStart BetaManagedAgentsSpanModelRequestStartEventType = "span.model_request_start"`

  - `type BetaManagedAgentsSpanModelRequestEndEvent struct{…}`

    Emitted when a model request completes.

    - `ID string`

      Unique identifier for this event.

    - `IsError bool`

      Whether the model request resulted in an error.

    - `ModelRequestStartID string`

      The id of the corresponding `span.model_request_start` event.

    - `ModelUsage BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `CacheCreationInputTokens int64`

        Tokens used to create prompt cache in this request.

      - `CacheReadInputTokens int64`

        Tokens read from prompt cache in this request.

      - `InputTokens int64`

        Input tokens consumed by this request.

      - `OutputTokens int64`

        Output tokens generated by this request.

      - `Speed BetaManagedAgentsSpanModelUsageSpeed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `const BetaManagedAgentsSpanModelUsageSpeedStandard BetaManagedAgentsSpanModelUsageSpeed = "standard"`

        - `const BetaManagedAgentsSpanModelUsageSpeedFast BetaManagedAgentsSpanModelUsageSpeed = "fast"`

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSpanModelRequestEndEventType`

      - `const BetaManagedAgentsSpanModelRequestEndEventTypeSpanModelRequestEnd BetaManagedAgentsSpanModelRequestEndEventType = "span.model_request_end"`

  - `type BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent struct{…}`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `ID string`

      Unique identifier for this event.

    - `Iteration int64`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `OutcomeID string`

      The `outc_` ID of the outcome being evaluated.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSpanOutcomeEvaluationOngoingEventType`

      - `const BetaManagedAgentsSpanOutcomeEvaluationOngoingEventTypeSpanOutcomeEvaluationOngoing BetaManagedAgentsSpanOutcomeEvaluationOngoingEventType = "span.outcome_evaluation_ongoing"`

  - `type BetaManagedAgentsUserDefineOutcomeEvent struct{…}`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `ID string`

      Unique identifier for this event.

    - `Description string`

      What the agent should produce. Copied from the input event.

    - `MaxIterations int64`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `OutcomeID string`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Rubric BetaManagedAgentsUserDefineOutcomeEventRubricUnion`

      Rubric for grading the quality of an outcome.

      - `type BetaManagedAgentsFileRubric struct{…}`

        Rubric referenced by a file uploaded via the Files API.

        - `FileID string`

          ID of the rubric file.

        - `Type BetaManagedAgentsFileRubricType`

          - `const BetaManagedAgentsFileRubricTypeFile BetaManagedAgentsFileRubricType = "file"`

      - `type BetaManagedAgentsTextRubric struct{…}`

        Rubric content provided inline as text.

        - `Content string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `Type BetaManagedAgentsTextRubricType`

          - `const BetaManagedAgentsTextRubricTypeText BetaManagedAgentsTextRubricType = "text"`

    - `Type BetaManagedAgentsUserDefineOutcomeEventType`

      - `const BetaManagedAgentsUserDefineOutcomeEventTypeUserDefineOutcome BetaManagedAgentsUserDefineOutcomeEventType = "user.define_outcome"`

  - `type BetaManagedAgentsSessionDeletedEvent struct{…}`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSessionDeletedEventType`

      - `const BetaManagedAgentsSessionDeletedEventTypeSessionDeleted BetaManagedAgentsSessionDeletedEventType = "session.deleted"`

  - `type BetaManagedAgentsSessionThreadStatusRunningEvent struct{…}`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `SessionThreadID string`

      Public sthr_ ID of the thread that started running.

    - `Type BetaManagedAgentsSessionThreadStatusRunningEventType`

      - `const BetaManagedAgentsSessionThreadStatusRunningEventTypeSessionThreadStatusRunning BetaManagedAgentsSessionThreadStatusRunningEventType = "session.thread_status_running"`

  - `type BetaManagedAgentsSessionThreadStatusIdleEvent struct{…}`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `SessionThreadID string`

      Public sthr_ ID of the thread that went idle.

    - `StopReason BetaManagedAgentsSessionThreadStatusIdleEventStopReasonUnion`

      The agent completed its turn naturally and is ready for the next user message.

      - `type BetaManagedAgentsSessionEndTurn struct{…}`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type BetaManagedAgentsSessionEndTurnType`

          - `const BetaManagedAgentsSessionEndTurnTypeEndTurn BetaManagedAgentsSessionEndTurnType = "end_turn"`

      - `type BetaManagedAgentsSessionRequiresAction struct{…}`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `EventIDs []string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type BetaManagedAgentsSessionRequiresActionType`

          - `const BetaManagedAgentsSessionRequiresActionTypeRequiresAction BetaManagedAgentsSessionRequiresActionType = "requires_action"`

      - `type BetaManagedAgentsSessionRetriesExhausted struct{…}`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `Type BetaManagedAgentsSessionRetriesExhaustedType`

          - `const BetaManagedAgentsSessionRetriesExhaustedTypeRetriesExhausted BetaManagedAgentsSessionRetriesExhaustedType = "retries_exhausted"`

    - `Type BetaManagedAgentsSessionThreadStatusIdleEventType`

      - `const BetaManagedAgentsSessionThreadStatusIdleEventTypeSessionThreadStatusIdle BetaManagedAgentsSessionThreadStatusIdleEventType = "session.thread_status_idle"`

  - `type BetaManagedAgentsSessionThreadStatusTerminatedEvent struct{…}`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `SessionThreadID string`

      Public sthr_ ID of the thread that terminated.

    - `Type BetaManagedAgentsSessionThreadStatusTerminatedEventType`

      - `const BetaManagedAgentsSessionThreadStatusTerminatedEventTypeSessionThreadStatusTerminated BetaManagedAgentsSessionThreadStatusTerminatedEventType = "session.thread_status_terminated"`

  - `type BetaManagedAgentsSessionThreadStatusRescheduledEvent struct{…}`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `SessionThreadID string`

      Public sthr_ ID of the thread that is retrying.

    - `Type BetaManagedAgentsSessionThreadStatusRescheduledEventType`

      - `const BetaManagedAgentsSessionThreadStatusRescheduledEventTypeSessionThreadStatusRescheduled BetaManagedAgentsSessionThreadStatusRescheduledEventType = "session.thread_status_rescheduled"`

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
  page, err := client.Beta.Sessions.Threads.Events.List(
    context.TODO(),
    "sthr_011CZkZVWa6oIjw0rgXZpnBt",
    anthropic.BetaSessionThreadEventListParams{
      SessionID: "sesn_011CZkZAtmR3yMPDzynEDxu7",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

## Stream

`client.Beta.Sessions.Threads.Events.Stream(ctx, threadID, params) (*BetaManagedAgentsStreamSessionThreadEventsUnion, error)`

**get** `/v1/sessions/{session_id}/threads/{thread_id}/stream`

Stream Session Thread Events

### Parameters

- `threadID string`

- `params BetaSessionThreadEventStreamParams`

  - `SessionID param.Field[string]`

    Path param: Path parameter session_id

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

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

### Returns

- `type BetaManagedAgentsStreamSessionThreadEventsUnion interface{…}`

  Server-sent event in a single thread's stream.

  - `type BetaManagedAgentsUserMessageEvent struct{…}`

    A user message event in the session conversation.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsUserMessageEventContentUnion`

      Array of content blocks comprising the user message.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

        - `Type BetaManagedAgentsTextBlockType`

          - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type BetaManagedAgentsBase64ImageSourceType`

              - `const BetaManagedAgentsBase64ImageSourceTypeBase64 BetaManagedAgentsBase64ImageSourceType = "base64"`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

              - `const BetaManagedAgentsURLImageSourceTypeURL BetaManagedAgentsURLImageSourceType = "url"`

            - `URL string`

              URL of the image to fetch.

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileImageSourceType`

              - `const BetaManagedAgentsFileImageSourceTypeFile BetaManagedAgentsFileImageSourceType = "file"`

        - `Type BetaManagedAgentsImageBlockType`

          - `const BetaManagedAgentsImageBlockTypeImage BetaManagedAgentsImageBlockType = "image"`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

            - `Type BetaManagedAgentsBase64DocumentSourceType`

              - `const BetaManagedAgentsBase64DocumentSourceTypeBase64 BetaManagedAgentsBase64DocumentSourceType = "base64"`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

              - `const BetaManagedAgentsPlainTextDocumentSourceMediaTypeTextPlain BetaManagedAgentsPlainTextDocumentSourceMediaType = "text/plain"`

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

              - `const BetaManagedAgentsPlainTextDocumentSourceTypeText BetaManagedAgentsPlainTextDocumentSourceType = "text"`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

              - `const BetaManagedAgentsURLDocumentSourceTypeURL BetaManagedAgentsURLDocumentSourceType = "url"`

            - `URL string`

              URL of the document to fetch.

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileDocumentSourceType`

              - `const BetaManagedAgentsFileDocumentSourceTypeFile BetaManagedAgentsFileDocumentSourceType = "file"`

        - `Type BetaManagedAgentsDocumentBlockType`

          - `const BetaManagedAgentsDocumentBlockTypeDocument BetaManagedAgentsDocumentBlockType = "document"`

        - `Context string`

          Additional context about the document for the model.

        - `Title string`

          The title of the document.

    - `Type BetaManagedAgentsUserMessageEventType`

      - `const BetaManagedAgentsUserMessageEventTypeUserMessage BetaManagedAgentsUserMessageEventType = "user.message"`

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

  - `type BetaManagedAgentsUserInterruptEvent struct{…}`

    An interrupt event that pauses agent execution and returns control to the user.

    - `ID string`

      Unique identifier for this event.

    - `Type BetaManagedAgentsUserInterruptEventType`

      - `const BetaManagedAgentsUserInterruptEventTypeUserInterrupt BetaManagedAgentsUserInterruptEventType = "user.interrupt"`

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `SessionThreadID string`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `type BetaManagedAgentsUserToolConfirmationEvent struct{…}`

    A tool confirmation event that approves or denies a pending tool execution.

    - `ID string`

      Unique identifier for this event.

    - `Result BetaManagedAgentsUserToolConfirmationEventResult`

      UserToolConfirmationResult enum

      - `const BetaManagedAgentsUserToolConfirmationEventResultAllow BetaManagedAgentsUserToolConfirmationEventResult = "allow"`

      - `const BetaManagedAgentsUserToolConfirmationEventResultDeny BetaManagedAgentsUserToolConfirmationEventResult = "deny"`

    - `ToolUseID string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type BetaManagedAgentsUserToolConfirmationEventType`

      - `const BetaManagedAgentsUserToolConfirmationEventTypeUserToolConfirmation BetaManagedAgentsUserToolConfirmationEventType = "user.tool_confirmation"`

    - `DenyMessage string`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `SessionThreadID string`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `type BetaManagedAgentsUserCustomToolResultEvent struct{…}`

    Event sent by the client providing the result of a custom tool execution.

    - `ID string`

      Unique identifier for this event.

    - `CustomToolUseID string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type BetaManagedAgentsUserCustomToolResultEventType`

      - `const BetaManagedAgentsUserCustomToolResultEventTypeUserCustomToolResult BetaManagedAgentsUserCustomToolResultEventType = "user.custom_tool_result"`

    - `Content []BetaManagedAgentsUserCustomToolResultEventContentUnion`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

        - `Type BetaManagedAgentsTextBlockType`

          - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type BetaManagedAgentsBase64ImageSourceType`

              - `const BetaManagedAgentsBase64ImageSourceTypeBase64 BetaManagedAgentsBase64ImageSourceType = "base64"`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

              - `const BetaManagedAgentsURLImageSourceTypeURL BetaManagedAgentsURLImageSourceType = "url"`

            - `URL string`

              URL of the image to fetch.

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileImageSourceType`

              - `const BetaManagedAgentsFileImageSourceTypeFile BetaManagedAgentsFileImageSourceType = "file"`

        - `Type BetaManagedAgentsImageBlockType`

          - `const BetaManagedAgentsImageBlockTypeImage BetaManagedAgentsImageBlockType = "image"`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

            - `Type BetaManagedAgentsBase64DocumentSourceType`

              - `const BetaManagedAgentsBase64DocumentSourceTypeBase64 BetaManagedAgentsBase64DocumentSourceType = "base64"`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

              - `const BetaManagedAgentsPlainTextDocumentSourceMediaTypeTextPlain BetaManagedAgentsPlainTextDocumentSourceMediaType = "text/plain"`

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

              - `const BetaManagedAgentsPlainTextDocumentSourceTypeText BetaManagedAgentsPlainTextDocumentSourceType = "text"`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

              - `const BetaManagedAgentsURLDocumentSourceTypeURL BetaManagedAgentsURLDocumentSourceType = "url"`

            - `URL string`

              URL of the document to fetch.

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileDocumentSourceType`

              - `const BetaManagedAgentsFileDocumentSourceTypeFile BetaManagedAgentsFileDocumentSourceType = "file"`

        - `Type BetaManagedAgentsDocumentBlockType`

          - `const BetaManagedAgentsDocumentBlockTypeDocument BetaManagedAgentsDocumentBlockType = "document"`

        - `Context string`

          Additional context about the document for the model.

        - `Title string`

          The title of the document.

    - `IsError bool`

      Whether the tool execution resulted in an error.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `SessionThreadID string`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `type BetaManagedAgentsAgentCustomToolUseEvent struct{…}`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `Name string`

      Name of the custom tool being called.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentCustomToolUseEventType`

      - `const BetaManagedAgentsAgentCustomToolUseEventTypeAgentCustomToolUse BetaManagedAgentsAgentCustomToolUseEventType = "agent.custom_tool_use"`

    - `SessionThreadID string`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `type BetaManagedAgentsAgentMessageEvent struct{…}`

    An agent response event in the session conversation.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsTextBlock`

      Array of text blocks comprising the agent response.

      - `Text string`

        The text content.

      - `Type BetaManagedAgentsTextBlockType`

        - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentMessageEventType`

      - `const BetaManagedAgentsAgentMessageEventTypeAgentMessage BetaManagedAgentsAgentMessageEventType = "agent.message"`

  - `type BetaManagedAgentsAgentThinkingEvent struct{…}`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentThinkingEventType`

      - `const BetaManagedAgentsAgentThinkingEventTypeAgentThinking BetaManagedAgentsAgentThinkingEventType = "agent.thinking"`

  - `type BetaManagedAgentsAgentMCPToolUseEvent struct{…}`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `MCPServerName string`

      Name of the MCP server providing the tool.

    - `Name string`

      Name of the MCP tool being used.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentMCPToolUseEventType`

      - `const BetaManagedAgentsAgentMCPToolUseEventTypeAgentMCPToolUse BetaManagedAgentsAgentMCPToolUseEventType = "agent.mcp_tool_use"`

    - `EvaluatedPermission BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission`

      AgentEvaluatedPermission enum

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "allow"`

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "ask"`

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "deny"`

    - `SessionThreadID string`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `type BetaManagedAgentsAgentMCPToolResultEvent struct{…}`

    Event representing the result of an MCP tool execution.

    - `ID string`

      Unique identifier for this event.

    - `MCPToolUseID string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentMCPToolResultEventType`

      - `const BetaManagedAgentsAgentMCPToolResultEventTypeAgentMCPToolResult BetaManagedAgentsAgentMCPToolResultEventType = "agent.mcp_tool_result"`

    - `Content []BetaManagedAgentsAgentMCPToolResultEventContentUnion`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

        - `Type BetaManagedAgentsTextBlockType`

          - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type BetaManagedAgentsBase64ImageSourceType`

              - `const BetaManagedAgentsBase64ImageSourceTypeBase64 BetaManagedAgentsBase64ImageSourceType = "base64"`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

              - `const BetaManagedAgentsURLImageSourceTypeURL BetaManagedAgentsURLImageSourceType = "url"`

            - `URL string`

              URL of the image to fetch.

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileImageSourceType`

              - `const BetaManagedAgentsFileImageSourceTypeFile BetaManagedAgentsFileImageSourceType = "file"`

        - `Type BetaManagedAgentsImageBlockType`

          - `const BetaManagedAgentsImageBlockTypeImage BetaManagedAgentsImageBlockType = "image"`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

            - `Type BetaManagedAgentsBase64DocumentSourceType`

              - `const BetaManagedAgentsBase64DocumentSourceTypeBase64 BetaManagedAgentsBase64DocumentSourceType = "base64"`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

              - `const BetaManagedAgentsPlainTextDocumentSourceMediaTypeTextPlain BetaManagedAgentsPlainTextDocumentSourceMediaType = "text/plain"`

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

              - `const BetaManagedAgentsPlainTextDocumentSourceTypeText BetaManagedAgentsPlainTextDocumentSourceType = "text"`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

              - `const BetaManagedAgentsURLDocumentSourceTypeURL BetaManagedAgentsURLDocumentSourceType = "url"`

            - `URL string`

              URL of the document to fetch.

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileDocumentSourceType`

              - `const BetaManagedAgentsFileDocumentSourceTypeFile BetaManagedAgentsFileDocumentSourceType = "file"`

        - `Type BetaManagedAgentsDocumentBlockType`

          - `const BetaManagedAgentsDocumentBlockTypeDocument BetaManagedAgentsDocumentBlockType = "document"`

        - `Context string`

          Additional context about the document for the model.

        - `Title string`

          The title of the document.

    - `IsError bool`

      Whether the tool execution resulted in an error.

  - `type BetaManagedAgentsAgentToolUseEvent struct{…}`

    Event emitted when the agent invokes a built-in agent tool.

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `Name string`

      Name of the agent tool being used.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentToolUseEventType`

      - `const BetaManagedAgentsAgentToolUseEventTypeAgentToolUse BetaManagedAgentsAgentToolUseEventType = "agent.tool_use"`

    - `EvaluatedPermission BetaManagedAgentsAgentToolUseEventEvaluatedPermission`

      AgentEvaluatedPermission enum

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "allow"`

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "ask"`

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "deny"`

    - `SessionThreadID string`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `type BetaManagedAgentsAgentToolResultEvent struct{…}`

    Event representing the result of an agent tool execution.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `ToolUseID string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type BetaManagedAgentsAgentToolResultEventType`

      - `const BetaManagedAgentsAgentToolResultEventTypeAgentToolResult BetaManagedAgentsAgentToolResultEventType = "agent.tool_result"`

    - `Content []BetaManagedAgentsAgentToolResultEventContentUnion`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

        - `Type BetaManagedAgentsTextBlockType`

          - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type BetaManagedAgentsBase64ImageSourceType`

              - `const BetaManagedAgentsBase64ImageSourceTypeBase64 BetaManagedAgentsBase64ImageSourceType = "base64"`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

              - `const BetaManagedAgentsURLImageSourceTypeURL BetaManagedAgentsURLImageSourceType = "url"`

            - `URL string`

              URL of the image to fetch.

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileImageSourceType`

              - `const BetaManagedAgentsFileImageSourceTypeFile BetaManagedAgentsFileImageSourceType = "file"`

        - `Type BetaManagedAgentsImageBlockType`

          - `const BetaManagedAgentsImageBlockTypeImage BetaManagedAgentsImageBlockType = "image"`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

            - `Type BetaManagedAgentsBase64DocumentSourceType`

              - `const BetaManagedAgentsBase64DocumentSourceTypeBase64 BetaManagedAgentsBase64DocumentSourceType = "base64"`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

              - `const BetaManagedAgentsPlainTextDocumentSourceMediaTypeTextPlain BetaManagedAgentsPlainTextDocumentSourceMediaType = "text/plain"`

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

              - `const BetaManagedAgentsPlainTextDocumentSourceTypeText BetaManagedAgentsPlainTextDocumentSourceType = "text"`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

              - `const BetaManagedAgentsURLDocumentSourceTypeURL BetaManagedAgentsURLDocumentSourceType = "url"`

            - `URL string`

              URL of the document to fetch.

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileDocumentSourceType`

              - `const BetaManagedAgentsFileDocumentSourceTypeFile BetaManagedAgentsFileDocumentSourceType = "file"`

        - `Type BetaManagedAgentsDocumentBlockType`

          - `const BetaManagedAgentsDocumentBlockTypeDocument BetaManagedAgentsDocumentBlockType = "document"`

        - `Context string`

          Additional context about the document for the model.

        - `Title string`

          The title of the document.

    - `IsError bool`

      Whether the tool execution resulted in an error.

  - `type BetaManagedAgentsAgentThreadMessageReceivedEvent struct{…}`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsAgentThreadMessageReceivedEventContentUnion`

      Message content blocks.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

        - `Type BetaManagedAgentsTextBlockType`

          - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type BetaManagedAgentsBase64ImageSourceType`

              - `const BetaManagedAgentsBase64ImageSourceTypeBase64 BetaManagedAgentsBase64ImageSourceType = "base64"`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

              - `const BetaManagedAgentsURLImageSourceTypeURL BetaManagedAgentsURLImageSourceType = "url"`

            - `URL string`

              URL of the image to fetch.

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileImageSourceType`

              - `const BetaManagedAgentsFileImageSourceTypeFile BetaManagedAgentsFileImageSourceType = "file"`

        - `Type BetaManagedAgentsImageBlockType`

          - `const BetaManagedAgentsImageBlockTypeImage BetaManagedAgentsImageBlockType = "image"`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

            - `Type BetaManagedAgentsBase64DocumentSourceType`

              - `const BetaManagedAgentsBase64DocumentSourceTypeBase64 BetaManagedAgentsBase64DocumentSourceType = "base64"`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

              - `const BetaManagedAgentsPlainTextDocumentSourceMediaTypeTextPlain BetaManagedAgentsPlainTextDocumentSourceMediaType = "text/plain"`

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

              - `const BetaManagedAgentsPlainTextDocumentSourceTypeText BetaManagedAgentsPlainTextDocumentSourceType = "text"`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

              - `const BetaManagedAgentsURLDocumentSourceTypeURL BetaManagedAgentsURLDocumentSourceType = "url"`

            - `URL string`

              URL of the document to fetch.

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileDocumentSourceType`

              - `const BetaManagedAgentsFileDocumentSourceTypeFile BetaManagedAgentsFileDocumentSourceType = "file"`

        - `Type BetaManagedAgentsDocumentBlockType`

          - `const BetaManagedAgentsDocumentBlockTypeDocument BetaManagedAgentsDocumentBlockType = "document"`

        - `Context string`

          Additional context about the document for the model.

        - `Title string`

          The title of the document.

    - `FromSessionThreadID string`

      Public `sthr_` ID of the thread that sent the message.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentThreadMessageReceivedEventType`

      - `const BetaManagedAgentsAgentThreadMessageReceivedEventTypeAgentThreadMessageReceived BetaManagedAgentsAgentThreadMessageReceivedEventType = "agent.thread_message_received"`

    - `FromAgentName string`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `type BetaManagedAgentsAgentThreadMessageSentEvent struct{…}`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsAgentThreadMessageSentEventContentUnion`

      Message content blocks.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

        - `Type BetaManagedAgentsTextBlockType`

          - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type BetaManagedAgentsBase64ImageSourceType`

              - `const BetaManagedAgentsBase64ImageSourceTypeBase64 BetaManagedAgentsBase64ImageSourceType = "base64"`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

              - `const BetaManagedAgentsURLImageSourceTypeURL BetaManagedAgentsURLImageSourceType = "url"`

            - `URL string`

              URL of the image to fetch.

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileImageSourceType`

              - `const BetaManagedAgentsFileImageSourceTypeFile BetaManagedAgentsFileImageSourceType = "file"`

        - `Type BetaManagedAgentsImageBlockType`

          - `const BetaManagedAgentsImageBlockTypeImage BetaManagedAgentsImageBlockType = "image"`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

            - `Type BetaManagedAgentsBase64DocumentSourceType`

              - `const BetaManagedAgentsBase64DocumentSourceTypeBase64 BetaManagedAgentsBase64DocumentSourceType = "base64"`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

              - `const BetaManagedAgentsPlainTextDocumentSourceMediaTypeTextPlain BetaManagedAgentsPlainTextDocumentSourceMediaType = "text/plain"`

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

              - `const BetaManagedAgentsPlainTextDocumentSourceTypeText BetaManagedAgentsPlainTextDocumentSourceType = "text"`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

              - `const BetaManagedAgentsURLDocumentSourceTypeURL BetaManagedAgentsURLDocumentSourceType = "url"`

            - `URL string`

              URL of the document to fetch.

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileDocumentSourceType`

              - `const BetaManagedAgentsFileDocumentSourceTypeFile BetaManagedAgentsFileDocumentSourceType = "file"`

        - `Type BetaManagedAgentsDocumentBlockType`

          - `const BetaManagedAgentsDocumentBlockTypeDocument BetaManagedAgentsDocumentBlockType = "document"`

        - `Context string`

          Additional context about the document for the model.

        - `Title string`

          The title of the document.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `ToSessionThreadID string`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type BetaManagedAgentsAgentThreadMessageSentEventType`

      - `const BetaManagedAgentsAgentThreadMessageSentEventTypeAgentThreadMessageSent BetaManagedAgentsAgentThreadMessageSentEventType = "agent.thread_message_sent"`

    - `ToAgentName string`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `type BetaManagedAgentsAgentThreadContextCompactedEvent struct{…}`

    Indicates that context compaction (summarization) occurred during the session.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentThreadContextCompactedEventType`

      - `const BetaManagedAgentsAgentThreadContextCompactedEventTypeAgentThreadContextCompacted BetaManagedAgentsAgentThreadContextCompactedEventType = "agent.thread_context_compacted"`

  - `type BetaManagedAgentsSessionErrorEvent struct{…}`

    An error event indicating a problem occurred during session execution.

    - `ID string`

      Unique identifier for this event.

    - `Error BetaManagedAgentsSessionErrorEventErrorUnion`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `type BetaManagedAgentsUnknownError struct{…}`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsUnknownErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsUnknownErrorType`

          - `const BetaManagedAgentsUnknownErrorTypeUnknownError BetaManagedAgentsUnknownErrorType = "unknown_error"`

      - `type BetaManagedAgentsModelOverloadedError struct{…}`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsModelOverloadedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsModelOverloadedErrorType`

          - `const BetaManagedAgentsModelOverloadedErrorTypeModelOverloadedError BetaManagedAgentsModelOverloadedErrorType = "model_overloaded_error"`

      - `type BetaManagedAgentsModelRateLimitedError struct{…}`

        The model request was rate-limited.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsModelRateLimitedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsModelRateLimitedErrorType`

          - `const BetaManagedAgentsModelRateLimitedErrorTypeModelRateLimitedError BetaManagedAgentsModelRateLimitedErrorType = "model_rate_limited_error"`

      - `type BetaManagedAgentsModelRequestFailedError struct{…}`

        A model request failed for a reason other than overload or rate-limiting.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsModelRequestFailedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsModelRequestFailedErrorType`

          - `const BetaManagedAgentsModelRequestFailedErrorTypeModelRequestFailedError BetaManagedAgentsModelRequestFailedErrorType = "model_request_failed_error"`

      - `type BetaManagedAgentsMCPConnectionFailedError struct{…}`

        Failed to connect to an MCP server.

        - `MCPServerName string`

          Name of the MCP server that failed to connect.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsMCPConnectionFailedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsMCPConnectionFailedErrorType`

          - `const BetaManagedAgentsMCPConnectionFailedErrorTypeMCPConnectionFailedError BetaManagedAgentsMCPConnectionFailedErrorType = "mcp_connection_failed_error"`

      - `type BetaManagedAgentsMCPAuthenticationFailedError struct{…}`

        Authentication to an MCP server failed.

        - `MCPServerName string`

          Name of the MCP server that failed authentication.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsMCPAuthenticationFailedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsMCPAuthenticationFailedErrorType`

          - `const BetaManagedAgentsMCPAuthenticationFailedErrorTypeMCPAuthenticationFailedError BetaManagedAgentsMCPAuthenticationFailedErrorType = "mcp_authentication_failed_error"`

      - `type BetaManagedAgentsBillingError struct{…}`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsBillingErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsBillingErrorType`

          - `const BetaManagedAgentsBillingErrorTypeBillingError BetaManagedAgentsBillingErrorType = "billing_error"`

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSessionErrorEventType`

      - `const BetaManagedAgentsSessionErrorEventTypeSessionError BetaManagedAgentsSessionErrorEventType = "session.error"`

  - `type BetaManagedAgentsSessionStatusRescheduledEvent struct{…}`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSessionStatusRescheduledEventType`

      - `const BetaManagedAgentsSessionStatusRescheduledEventTypeSessionStatusRescheduled BetaManagedAgentsSessionStatusRescheduledEventType = "session.status_rescheduled"`

  - `type BetaManagedAgentsSessionStatusRunningEvent struct{…}`

    Indicates the session is actively running and the agent is working.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSessionStatusRunningEventType`

      - `const BetaManagedAgentsSessionStatusRunningEventTypeSessionStatusRunning BetaManagedAgentsSessionStatusRunningEventType = "session.status_running"`

  - `type BetaManagedAgentsSessionStatusIdleEvent struct{…}`

    Indicates the agent has paused and is awaiting user input.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `StopReason BetaManagedAgentsSessionStatusIdleEventStopReasonUnion`

      The agent completed its turn naturally and is ready for the next user message.

      - `type BetaManagedAgentsSessionEndTurn struct{…}`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type BetaManagedAgentsSessionEndTurnType`

          - `const BetaManagedAgentsSessionEndTurnTypeEndTurn BetaManagedAgentsSessionEndTurnType = "end_turn"`

      - `type BetaManagedAgentsSessionRequiresAction struct{…}`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `EventIDs []string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type BetaManagedAgentsSessionRequiresActionType`

          - `const BetaManagedAgentsSessionRequiresActionTypeRequiresAction BetaManagedAgentsSessionRequiresActionType = "requires_action"`

      - `type BetaManagedAgentsSessionRetriesExhausted struct{…}`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `Type BetaManagedAgentsSessionRetriesExhaustedType`

          - `const BetaManagedAgentsSessionRetriesExhaustedTypeRetriesExhausted BetaManagedAgentsSessionRetriesExhaustedType = "retries_exhausted"`

    - `Type BetaManagedAgentsSessionStatusIdleEventType`

      - `const BetaManagedAgentsSessionStatusIdleEventTypeSessionStatusIdle BetaManagedAgentsSessionStatusIdleEventType = "session.status_idle"`

  - `type BetaManagedAgentsSessionStatusTerminatedEvent struct{…}`

    Indicates the session has terminated, either due to an error or completion.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSessionStatusTerminatedEventType`

      - `const BetaManagedAgentsSessionStatusTerminatedEventTypeSessionStatusTerminated BetaManagedAgentsSessionStatusTerminatedEventType = "session.status_terminated"`

  - `type BetaManagedAgentsSessionThreadCreatedEvent struct{…}`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the callable agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `SessionThreadID string`

      Public `sthr_` ID of the newly created thread.

    - `Type BetaManagedAgentsSessionThreadCreatedEventType`

      - `const BetaManagedAgentsSessionThreadCreatedEventTypeSessionThreadCreated BetaManagedAgentsSessionThreadCreatedEventType = "session.thread_created"`

  - `type BetaManagedAgentsSpanOutcomeEvaluationStartEvent struct{…}`

    Emitted when an outcome evaluation cycle begins.

    - `ID string`

      Unique identifier for this event.

    - `Iteration int64`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `OutcomeID string`

      The `outc_` ID of the outcome being evaluated.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSpanOutcomeEvaluationStartEventType`

      - `const BetaManagedAgentsSpanOutcomeEvaluationStartEventTypeSpanOutcomeEvaluationStart BetaManagedAgentsSpanOutcomeEvaluationStartEventType = "span.outcome_evaluation_start"`

  - `type BetaManagedAgentsSpanOutcomeEvaluationEndEvent struct{…}`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `ID string`

      Unique identifier for this event.

    - `Explanation string`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `Iteration int64`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `OutcomeEvaluationStartID string`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `OutcomeID string`

      The `outc_` ID of the outcome being evaluated.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Result string`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type BetaManagedAgentsSpanOutcomeEvaluationEndEventType`

      - `const BetaManagedAgentsSpanOutcomeEvaluationEndEventTypeSpanOutcomeEvaluationEnd BetaManagedAgentsSpanOutcomeEvaluationEndEventType = "span.outcome_evaluation_end"`

    - `Usage BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `CacheCreationInputTokens int64`

        Tokens used to create prompt cache in this request.

      - `CacheReadInputTokens int64`

        Tokens read from prompt cache in this request.

      - `InputTokens int64`

        Input tokens consumed by this request.

      - `OutputTokens int64`

        Output tokens generated by this request.

      - `Speed BetaManagedAgentsSpanModelUsageSpeed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `const BetaManagedAgentsSpanModelUsageSpeedStandard BetaManagedAgentsSpanModelUsageSpeed = "standard"`

        - `const BetaManagedAgentsSpanModelUsageSpeedFast BetaManagedAgentsSpanModelUsageSpeed = "fast"`

  - `type BetaManagedAgentsSpanModelRequestStartEvent struct{…}`

    Emitted when a model request is initiated by the agent.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSpanModelRequestStartEventType`

      - `const BetaManagedAgentsSpanModelRequestStartEventTypeSpanModelRequestStart BetaManagedAgentsSpanModelRequestStartEventType = "span.model_request_start"`

  - `type BetaManagedAgentsSpanModelRequestEndEvent struct{…}`

    Emitted when a model request completes.

    - `ID string`

      Unique identifier for this event.

    - `IsError bool`

      Whether the model request resulted in an error.

    - `ModelRequestStartID string`

      The id of the corresponding `span.model_request_start` event.

    - `ModelUsage BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `CacheCreationInputTokens int64`

        Tokens used to create prompt cache in this request.

      - `CacheReadInputTokens int64`

        Tokens read from prompt cache in this request.

      - `InputTokens int64`

        Input tokens consumed by this request.

      - `OutputTokens int64`

        Output tokens generated by this request.

      - `Speed BetaManagedAgentsSpanModelUsageSpeed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `const BetaManagedAgentsSpanModelUsageSpeedStandard BetaManagedAgentsSpanModelUsageSpeed = "standard"`

        - `const BetaManagedAgentsSpanModelUsageSpeedFast BetaManagedAgentsSpanModelUsageSpeed = "fast"`

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSpanModelRequestEndEventType`

      - `const BetaManagedAgentsSpanModelRequestEndEventTypeSpanModelRequestEnd BetaManagedAgentsSpanModelRequestEndEventType = "span.model_request_end"`

  - `type BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent struct{…}`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `ID string`

      Unique identifier for this event.

    - `Iteration int64`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `OutcomeID string`

      The `outc_` ID of the outcome being evaluated.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSpanOutcomeEvaluationOngoingEventType`

      - `const BetaManagedAgentsSpanOutcomeEvaluationOngoingEventTypeSpanOutcomeEvaluationOngoing BetaManagedAgentsSpanOutcomeEvaluationOngoingEventType = "span.outcome_evaluation_ongoing"`

  - `type BetaManagedAgentsUserDefineOutcomeEvent struct{…}`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `ID string`

      Unique identifier for this event.

    - `Description string`

      What the agent should produce. Copied from the input event.

    - `MaxIterations int64`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `OutcomeID string`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Rubric BetaManagedAgentsUserDefineOutcomeEventRubricUnion`

      Rubric for grading the quality of an outcome.

      - `type BetaManagedAgentsFileRubric struct{…}`

        Rubric referenced by a file uploaded via the Files API.

        - `FileID string`

          ID of the rubric file.

        - `Type BetaManagedAgentsFileRubricType`

          - `const BetaManagedAgentsFileRubricTypeFile BetaManagedAgentsFileRubricType = "file"`

      - `type BetaManagedAgentsTextRubric struct{…}`

        Rubric content provided inline as text.

        - `Content string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `Type BetaManagedAgentsTextRubricType`

          - `const BetaManagedAgentsTextRubricTypeText BetaManagedAgentsTextRubricType = "text"`

    - `Type BetaManagedAgentsUserDefineOutcomeEventType`

      - `const BetaManagedAgentsUserDefineOutcomeEventTypeUserDefineOutcome BetaManagedAgentsUserDefineOutcomeEventType = "user.define_outcome"`

  - `type BetaManagedAgentsSessionDeletedEvent struct{…}`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSessionDeletedEventType`

      - `const BetaManagedAgentsSessionDeletedEventTypeSessionDeleted BetaManagedAgentsSessionDeletedEventType = "session.deleted"`

  - `type BetaManagedAgentsSessionThreadStatusRunningEvent struct{…}`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `SessionThreadID string`

      Public sthr_ ID of the thread that started running.

    - `Type BetaManagedAgentsSessionThreadStatusRunningEventType`

      - `const BetaManagedAgentsSessionThreadStatusRunningEventTypeSessionThreadStatusRunning BetaManagedAgentsSessionThreadStatusRunningEventType = "session.thread_status_running"`

  - `type BetaManagedAgentsSessionThreadStatusIdleEvent struct{…}`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `SessionThreadID string`

      Public sthr_ ID of the thread that went idle.

    - `StopReason BetaManagedAgentsSessionThreadStatusIdleEventStopReasonUnion`

      The agent completed its turn naturally and is ready for the next user message.

      - `type BetaManagedAgentsSessionEndTurn struct{…}`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type BetaManagedAgentsSessionEndTurnType`

          - `const BetaManagedAgentsSessionEndTurnTypeEndTurn BetaManagedAgentsSessionEndTurnType = "end_turn"`

      - `type BetaManagedAgentsSessionRequiresAction struct{…}`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `EventIDs []string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type BetaManagedAgentsSessionRequiresActionType`

          - `const BetaManagedAgentsSessionRequiresActionTypeRequiresAction BetaManagedAgentsSessionRequiresActionType = "requires_action"`

      - `type BetaManagedAgentsSessionRetriesExhausted struct{…}`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `Type BetaManagedAgentsSessionRetriesExhaustedType`

          - `const BetaManagedAgentsSessionRetriesExhaustedTypeRetriesExhausted BetaManagedAgentsSessionRetriesExhaustedType = "retries_exhausted"`

    - `Type BetaManagedAgentsSessionThreadStatusIdleEventType`

      - `const BetaManagedAgentsSessionThreadStatusIdleEventTypeSessionThreadStatusIdle BetaManagedAgentsSessionThreadStatusIdleEventType = "session.thread_status_idle"`

  - `type BetaManagedAgentsSessionThreadStatusTerminatedEvent struct{…}`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `SessionThreadID string`

      Public sthr_ ID of the thread that terminated.

    - `Type BetaManagedAgentsSessionThreadStatusTerminatedEventType`

      - `const BetaManagedAgentsSessionThreadStatusTerminatedEventTypeSessionThreadStatusTerminated BetaManagedAgentsSessionThreadStatusTerminatedEventType = "session.thread_status_terminated"`

  - `type BetaManagedAgentsSessionThreadStatusRescheduledEvent struct{…}`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `SessionThreadID string`

      Public sthr_ ID of the thread that is retrying.

    - `Type BetaManagedAgentsSessionThreadStatusRescheduledEventType`

      - `const BetaManagedAgentsSessionThreadStatusRescheduledEventTypeSessionThreadStatusRescheduled BetaManagedAgentsSessionThreadStatusRescheduledEventType = "session.thread_status_rescheduled"`

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
  stream := client.Beta.Sessions.Threads.Events.StreamEvents(
    context.TODO(),
    "sthr_011CZkZVWa6oIjw0rgXZpnBt",
    anthropic.BetaSessionThreadEventStreamParams{
      SessionID: "sesn_011CZkZAtmR3yMPDzynEDxu7",
    },
  )
  for stream.Next() {
  fmt.Printf("%+v\n", stream.Current())
  }
  err := stream.Err()
  if err != nil {
    panic(err.Error())
  }
}
```
