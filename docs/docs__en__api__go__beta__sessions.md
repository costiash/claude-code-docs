# Sessions

## Create

`client.Beta.Sessions.New(ctx, params) (*BetaManagedAgentsSession, error)`

**post** `/v1/sessions`

Create Session

### Parameters

- `params BetaSessionNewParams`

  - `Agent param.Field[BetaSessionNewParamsAgentUnion]`

    Body param: Agent identifier. Accepts the `agent` ID string, which pins the latest version for the session, or an `agent` object with both id and version specified.

    - `string`

    - `type BetaManagedAgentsAgentParamsResp struct{…}`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `ID string`

        The `agent` ID.

      - `Type BetaManagedAgentsAgentParamsType`

        - `const BetaManagedAgentsAgentParamsTypeAgent BetaManagedAgentsAgentParamsType = "agent"`

      - `Version int64`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

  - `EnvironmentID param.Field[string]`

    Body param: ID of the `environment` defining the container configuration for this session.

  - `Metadata param.Field[map[string, string]]`

    Body param: Arbitrary key-value metadata attached to the session.

  - `Resources param.Field[[]BetaSessionNewParamsResourceUnion]`

    Body param: Resources (e.g. repositories, files) to mount into the session's container.

    - `type BetaManagedAgentsGitHubRepositoryResourceParamsResp struct{…}`

      Mount a GitHub repository into the session's container.

      - `AuthorizationToken string`

        GitHub authorization token used to clone the repository.

      - `Type BetaManagedAgentsGitHubRepositoryResourceParamsType`

        - `const BetaManagedAgentsGitHubRepositoryResourceParamsTypeGitHubRepository BetaManagedAgentsGitHubRepositoryResourceParamsType = "github_repository"`

      - `URL string`

        Github URL of the repository

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceParamsCheckoutUnionResp`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

          - `Type BetaManagedAgentsBranchCheckoutType`

            - `const BetaManagedAgentsBranchCheckoutTypeBranch BetaManagedAgentsBranchCheckoutType = "branch"`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

          - `Type BetaManagedAgentsCommitCheckoutType`

            - `const BetaManagedAgentsCommitCheckoutTypeCommit BetaManagedAgentsCommitCheckoutType = "commit"`

      - `MountPath string`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `type BetaManagedAgentsFileResourceParamsResp struct{…}`

      Mount a file uploaded via the Files API into the session.

      - `FileID string`

        ID of a previously uploaded file.

      - `Type BetaManagedAgentsFileResourceParamsType`

        - `const BetaManagedAgentsFileResourceParamsTypeFile BetaManagedAgentsFileResourceParamsType = "file"`

      - `MountPath string`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  - `Title param.Field[string]`

    Body param: Human-readable session title.

  - `VaultIDs param.Field[[]string]`

    Body param: Vault IDs for stored credentials the agent can use during the session.

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

### Returns

- `type BetaManagedAgentsSession struct{…}`

  A Managed Agents `session`.

  - `ID string`

  - `Agent BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

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

    - `Skills []BetaManagedAgentsSessionAgentSkillUnion`

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

    - `Tools []BetaManagedAgentsSessionAgentToolUnion`

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

    - `Type BetaManagedAgentsSessionAgentType`

      - `const BetaManagedAgentsSessionAgentTypeAgent BetaManagedAgentsSessionAgentType = "agent"`

    - `Version int64`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `EnvironmentID string`

  - `Metadata map[string, string]`

  - `Resources []BetaManagedAgentsSessionResourceUnion`

    - `type BetaManagedAgentsGitHubRepositoryResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

      - `MountPath string`

      - `Type BetaManagedAgentsGitHubRepositoryResourceType`

        - `const BetaManagedAgentsGitHubRepositoryResourceTypeGitHubRepository BetaManagedAgentsGitHubRepositoryResourceType = "github_repository"`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

      - `URL string`

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnion`

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

          - `Type BetaManagedAgentsBranchCheckoutType`

            - `const BetaManagedAgentsBranchCheckoutTypeBranch BetaManagedAgentsBranchCheckoutType = "branch"`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

          - `Type BetaManagedAgentsCommitCheckoutType`

            - `const BetaManagedAgentsCommitCheckoutTypeCommit BetaManagedAgentsCommitCheckoutType = "commit"`

    - `type BetaManagedAgentsFileResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

      - `FileID string`

      - `MountPath string`

      - `Type BetaManagedAgentsFileResourceType`

        - `const BetaManagedAgentsFileResourceTypeFile BetaManagedAgentsFileResourceType = "file"`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

  - `Stats BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `ActiveSeconds float64`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

    - `DurationSeconds float64`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

  - `Status BetaManagedAgentsSessionStatus`

    SessionStatus enum

    - `const BetaManagedAgentsSessionStatusRescheduling BetaManagedAgentsSessionStatus = "rescheduling"`

    - `const BetaManagedAgentsSessionStatusRunning BetaManagedAgentsSessionStatus = "running"`

    - `const BetaManagedAgentsSessionStatusIdle BetaManagedAgentsSessionStatus = "idle"`

    - `const BetaManagedAgentsSessionStatusTerminated BetaManagedAgentsSessionStatus = "terminated"`

  - `Title string`

  - `Type BetaManagedAgentsSessionType`

    - `const BetaManagedAgentsSessionTypeSession BetaManagedAgentsSessionType = "session"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Usage BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

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

  - `VaultIDs []string`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

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
  betaManagedAgentsSession, err := client.Beta.Sessions.New(context.TODO(), anthropic.BetaSessionNewParams{
    Agent: anthropic.BetaSessionNewParamsAgentUnion{
      OfString: anthropic.String("agent_011CZkYpogX7uDKUyvBTophP"),
    },
    EnvironmentID: "env_011CZkZ9X2dpNyB7HsEFoRfW",
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsSession.ID)
}
```

## List

`client.Beta.Sessions.List(ctx, params) (*PageCursor[BetaManagedAgentsSession], error)`

**get** `/v1/sessions`

List Sessions

### Parameters

- `params BetaSessionListParams`

  - `AgentID param.Field[string]`

    Query param: Filter sessions created with this agent ID.

  - `AgentVersion param.Field[int64]`

    Query param: Filter by agent version. Only applies when agent_id is also set.

  - `CreatedAtGt param.Field[Time]`

    Query param: Return sessions created after this time (exclusive).

  - `CreatedAtGte param.Field[Time]`

    Query param: Return sessions created at or after this time (inclusive).

  - `CreatedAtLt param.Field[Time]`

    Query param: Return sessions created before this time (exclusive).

  - `CreatedAtLte param.Field[Time]`

    Query param: Return sessions created at or before this time (inclusive).

  - `IncludeArchived param.Field[bool]`

    Query param: When true, includes archived sessions. Default: false (exclude archived).

  - `Limit param.Field[int64]`

    Query param: Maximum number of results to return.

  - `Order param.Field[BetaSessionListParamsOrder]`

    Query param: Sort direction for results, ordered by created_at. Defaults to desc (newest first).

    - `const BetaSessionListParamsOrderAsc BetaSessionListParamsOrder = "asc"`

    - `const BetaSessionListParamsOrderDesc BetaSessionListParamsOrder = "desc"`

  - `Page param.Field[string]`

    Query param: Opaque pagination cursor from a previous response's next_page.

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

### Returns

- `type BetaManagedAgentsSession struct{…}`

  A Managed Agents `session`.

  - `ID string`

  - `Agent BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

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

    - `Skills []BetaManagedAgentsSessionAgentSkillUnion`

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

    - `Tools []BetaManagedAgentsSessionAgentToolUnion`

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

    - `Type BetaManagedAgentsSessionAgentType`

      - `const BetaManagedAgentsSessionAgentTypeAgent BetaManagedAgentsSessionAgentType = "agent"`

    - `Version int64`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `EnvironmentID string`

  - `Metadata map[string, string]`

  - `Resources []BetaManagedAgentsSessionResourceUnion`

    - `type BetaManagedAgentsGitHubRepositoryResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

      - `MountPath string`

      - `Type BetaManagedAgentsGitHubRepositoryResourceType`

        - `const BetaManagedAgentsGitHubRepositoryResourceTypeGitHubRepository BetaManagedAgentsGitHubRepositoryResourceType = "github_repository"`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

      - `URL string`

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnion`

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

          - `Type BetaManagedAgentsBranchCheckoutType`

            - `const BetaManagedAgentsBranchCheckoutTypeBranch BetaManagedAgentsBranchCheckoutType = "branch"`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

          - `Type BetaManagedAgentsCommitCheckoutType`

            - `const BetaManagedAgentsCommitCheckoutTypeCommit BetaManagedAgentsCommitCheckoutType = "commit"`

    - `type BetaManagedAgentsFileResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

      - `FileID string`

      - `MountPath string`

      - `Type BetaManagedAgentsFileResourceType`

        - `const BetaManagedAgentsFileResourceTypeFile BetaManagedAgentsFileResourceType = "file"`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

  - `Stats BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `ActiveSeconds float64`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

    - `DurationSeconds float64`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

  - `Status BetaManagedAgentsSessionStatus`

    SessionStatus enum

    - `const BetaManagedAgentsSessionStatusRescheduling BetaManagedAgentsSessionStatus = "rescheduling"`

    - `const BetaManagedAgentsSessionStatusRunning BetaManagedAgentsSessionStatus = "running"`

    - `const BetaManagedAgentsSessionStatusIdle BetaManagedAgentsSessionStatus = "idle"`

    - `const BetaManagedAgentsSessionStatusTerminated BetaManagedAgentsSessionStatus = "terminated"`

  - `Title string`

  - `Type BetaManagedAgentsSessionType`

    - `const BetaManagedAgentsSessionTypeSession BetaManagedAgentsSessionType = "session"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Usage BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

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

  - `VaultIDs []string`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

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
  page, err := client.Beta.Sessions.List(context.TODO(), anthropic.BetaSessionListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

## Retrieve

`client.Beta.Sessions.Get(ctx, sessionID, query) (*BetaManagedAgentsSession, error)`

**get** `/v1/sessions/{session_id}`

Get Session

### Parameters

- `sessionID string`

- `query BetaSessionGetParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

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

### Returns

- `type BetaManagedAgentsSession struct{…}`

  A Managed Agents `session`.

  - `ID string`

  - `Agent BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

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

    - `Skills []BetaManagedAgentsSessionAgentSkillUnion`

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

    - `Tools []BetaManagedAgentsSessionAgentToolUnion`

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

    - `Type BetaManagedAgentsSessionAgentType`

      - `const BetaManagedAgentsSessionAgentTypeAgent BetaManagedAgentsSessionAgentType = "agent"`

    - `Version int64`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `EnvironmentID string`

  - `Metadata map[string, string]`

  - `Resources []BetaManagedAgentsSessionResourceUnion`

    - `type BetaManagedAgentsGitHubRepositoryResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

      - `MountPath string`

      - `Type BetaManagedAgentsGitHubRepositoryResourceType`

        - `const BetaManagedAgentsGitHubRepositoryResourceTypeGitHubRepository BetaManagedAgentsGitHubRepositoryResourceType = "github_repository"`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

      - `URL string`

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnion`

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

          - `Type BetaManagedAgentsBranchCheckoutType`

            - `const BetaManagedAgentsBranchCheckoutTypeBranch BetaManagedAgentsBranchCheckoutType = "branch"`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

          - `Type BetaManagedAgentsCommitCheckoutType`

            - `const BetaManagedAgentsCommitCheckoutTypeCommit BetaManagedAgentsCommitCheckoutType = "commit"`

    - `type BetaManagedAgentsFileResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

      - `FileID string`

      - `MountPath string`

      - `Type BetaManagedAgentsFileResourceType`

        - `const BetaManagedAgentsFileResourceTypeFile BetaManagedAgentsFileResourceType = "file"`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

  - `Stats BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `ActiveSeconds float64`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

    - `DurationSeconds float64`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

  - `Status BetaManagedAgentsSessionStatus`

    SessionStatus enum

    - `const BetaManagedAgentsSessionStatusRescheduling BetaManagedAgentsSessionStatus = "rescheduling"`

    - `const BetaManagedAgentsSessionStatusRunning BetaManagedAgentsSessionStatus = "running"`

    - `const BetaManagedAgentsSessionStatusIdle BetaManagedAgentsSessionStatus = "idle"`

    - `const BetaManagedAgentsSessionStatusTerminated BetaManagedAgentsSessionStatus = "terminated"`

  - `Title string`

  - `Type BetaManagedAgentsSessionType`

    - `const BetaManagedAgentsSessionTypeSession BetaManagedAgentsSessionType = "session"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Usage BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

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

  - `VaultIDs []string`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

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
  betaManagedAgentsSession, err := client.Beta.Sessions.Get(
    context.TODO(),
    "sesn_011CZkZAtmR3yMPDzynEDxu7",
    anthropic.BetaSessionGetParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsSession.ID)
}
```

## Update

`client.Beta.Sessions.Update(ctx, sessionID, params) (*BetaManagedAgentsSession, error)`

**post** `/v1/sessions/{session_id}`

Update Session

### Parameters

- `sessionID string`

- `params BetaSessionUpdateParams`

  - `Metadata param.Field[map[string, string]]`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve.

  - `Title param.Field[string]`

    Body param: Human-readable session title.

  - `VaultIDs param.Field[[]string]`

    Body param: Vault IDs (`vlt_*`) to attach to the session. Not yet supported; requests setting this field are rejected. Reserved for future use.

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

### Returns

- `type BetaManagedAgentsSession struct{…}`

  A Managed Agents `session`.

  - `ID string`

  - `Agent BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

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

    - `Skills []BetaManagedAgentsSessionAgentSkillUnion`

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

    - `Tools []BetaManagedAgentsSessionAgentToolUnion`

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

    - `Type BetaManagedAgentsSessionAgentType`

      - `const BetaManagedAgentsSessionAgentTypeAgent BetaManagedAgentsSessionAgentType = "agent"`

    - `Version int64`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `EnvironmentID string`

  - `Metadata map[string, string]`

  - `Resources []BetaManagedAgentsSessionResourceUnion`

    - `type BetaManagedAgentsGitHubRepositoryResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

      - `MountPath string`

      - `Type BetaManagedAgentsGitHubRepositoryResourceType`

        - `const BetaManagedAgentsGitHubRepositoryResourceTypeGitHubRepository BetaManagedAgentsGitHubRepositoryResourceType = "github_repository"`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

      - `URL string`

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnion`

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

          - `Type BetaManagedAgentsBranchCheckoutType`

            - `const BetaManagedAgentsBranchCheckoutTypeBranch BetaManagedAgentsBranchCheckoutType = "branch"`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

          - `Type BetaManagedAgentsCommitCheckoutType`

            - `const BetaManagedAgentsCommitCheckoutTypeCommit BetaManagedAgentsCommitCheckoutType = "commit"`

    - `type BetaManagedAgentsFileResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

      - `FileID string`

      - `MountPath string`

      - `Type BetaManagedAgentsFileResourceType`

        - `const BetaManagedAgentsFileResourceTypeFile BetaManagedAgentsFileResourceType = "file"`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

  - `Stats BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `ActiveSeconds float64`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

    - `DurationSeconds float64`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

  - `Status BetaManagedAgentsSessionStatus`

    SessionStatus enum

    - `const BetaManagedAgentsSessionStatusRescheduling BetaManagedAgentsSessionStatus = "rescheduling"`

    - `const BetaManagedAgentsSessionStatusRunning BetaManagedAgentsSessionStatus = "running"`

    - `const BetaManagedAgentsSessionStatusIdle BetaManagedAgentsSessionStatus = "idle"`

    - `const BetaManagedAgentsSessionStatusTerminated BetaManagedAgentsSessionStatus = "terminated"`

  - `Title string`

  - `Type BetaManagedAgentsSessionType`

    - `const BetaManagedAgentsSessionTypeSession BetaManagedAgentsSessionType = "session"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Usage BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

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

  - `VaultIDs []string`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

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
  betaManagedAgentsSession, err := client.Beta.Sessions.Update(
    context.TODO(),
    "sesn_011CZkZAtmR3yMPDzynEDxu7",
    anthropic.BetaSessionUpdateParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsSession.ID)
}
```

## Delete

`client.Beta.Sessions.Delete(ctx, sessionID, body) (*BetaManagedAgentsDeletedSession, error)`

**delete** `/v1/sessions/{session_id}`

Delete Session

### Parameters

- `sessionID string`

- `body BetaSessionDeleteParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

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

### Returns

- `type BetaManagedAgentsDeletedSession struct{…}`

  Confirmation that a `session` has been permanently deleted.

  - `ID string`

  - `Type BetaManagedAgentsDeletedSessionType`

    - `const BetaManagedAgentsDeletedSessionTypeSessionDeleted BetaManagedAgentsDeletedSessionType = "session_deleted"`

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
  betaManagedAgentsDeletedSession, err := client.Beta.Sessions.Delete(
    context.TODO(),
    "sesn_011CZkZAtmR3yMPDzynEDxu7",
    anthropic.BetaSessionDeleteParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsDeletedSession.ID)
}
```

## Archive

`client.Beta.Sessions.Archive(ctx, sessionID, body) (*BetaManagedAgentsSession, error)`

**post** `/v1/sessions/{session_id}/archive`

Archive Session

### Parameters

- `sessionID string`

- `body BetaSessionArchiveParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

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

### Returns

- `type BetaManagedAgentsSession struct{…}`

  A Managed Agents `session`.

  - `ID string`

  - `Agent BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

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

    - `Skills []BetaManagedAgentsSessionAgentSkillUnion`

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

    - `Tools []BetaManagedAgentsSessionAgentToolUnion`

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

    - `Type BetaManagedAgentsSessionAgentType`

      - `const BetaManagedAgentsSessionAgentTypeAgent BetaManagedAgentsSessionAgentType = "agent"`

    - `Version int64`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `EnvironmentID string`

  - `Metadata map[string, string]`

  - `Resources []BetaManagedAgentsSessionResourceUnion`

    - `type BetaManagedAgentsGitHubRepositoryResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

      - `MountPath string`

      - `Type BetaManagedAgentsGitHubRepositoryResourceType`

        - `const BetaManagedAgentsGitHubRepositoryResourceTypeGitHubRepository BetaManagedAgentsGitHubRepositoryResourceType = "github_repository"`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

      - `URL string`

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnion`

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

          - `Type BetaManagedAgentsBranchCheckoutType`

            - `const BetaManagedAgentsBranchCheckoutTypeBranch BetaManagedAgentsBranchCheckoutType = "branch"`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

          - `Type BetaManagedAgentsCommitCheckoutType`

            - `const BetaManagedAgentsCommitCheckoutTypeCommit BetaManagedAgentsCommitCheckoutType = "commit"`

    - `type BetaManagedAgentsFileResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

      - `FileID string`

      - `MountPath string`

      - `Type BetaManagedAgentsFileResourceType`

        - `const BetaManagedAgentsFileResourceTypeFile BetaManagedAgentsFileResourceType = "file"`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

  - `Stats BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `ActiveSeconds float64`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

    - `DurationSeconds float64`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

  - `Status BetaManagedAgentsSessionStatus`

    SessionStatus enum

    - `const BetaManagedAgentsSessionStatusRescheduling BetaManagedAgentsSessionStatus = "rescheduling"`

    - `const BetaManagedAgentsSessionStatusRunning BetaManagedAgentsSessionStatus = "running"`

    - `const BetaManagedAgentsSessionStatusIdle BetaManagedAgentsSessionStatus = "idle"`

    - `const BetaManagedAgentsSessionStatusTerminated BetaManagedAgentsSessionStatus = "terminated"`

  - `Title string`

  - `Type BetaManagedAgentsSessionType`

    - `const BetaManagedAgentsSessionTypeSession BetaManagedAgentsSessionType = "session"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Usage BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

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

  - `VaultIDs []string`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

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
  betaManagedAgentsSession, err := client.Beta.Sessions.Archive(
    context.TODO(),
    "sesn_011CZkZAtmR3yMPDzynEDxu7",
    anthropic.BetaSessionArchiveParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsSession.ID)
}
```

## Domain Types

### Beta Managed Agents Agent Params

- `type BetaManagedAgentsAgentParamsResp struct{…}`

  Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

  - `ID string`

    The `agent` ID.

  - `Type BetaManagedAgentsAgentParamsType`

    - `const BetaManagedAgentsAgentParamsTypeAgent BetaManagedAgentsAgentParamsType = "agent"`

  - `Version int64`

    The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

### Beta Managed Agents Branch Checkout

- `type BetaManagedAgentsBranchCheckout struct{…}`

  - `Name string`

    Branch name to check out.

  - `Type BetaManagedAgentsBranchCheckoutType`

    - `const BetaManagedAgentsBranchCheckoutTypeBranch BetaManagedAgentsBranchCheckoutType = "branch"`

### Beta Managed Agents Cache Creation Usage

- `type BetaManagedAgentsCacheCreationUsage struct{…}`

  Prompt-cache creation token usage broken down by cache lifetime.

  - `Ephemeral1hInputTokens int64`

    Tokens used to create 1-hour ephemeral cache entries.

  - `Ephemeral5mInputTokens int64`

    Tokens used to create 5-minute ephemeral cache entries.

### Beta Managed Agents Commit Checkout

- `type BetaManagedAgentsCommitCheckout struct{…}`

  - `Sha string`

    Full commit SHA to check out.

  - `Type BetaManagedAgentsCommitCheckoutType`

    - `const BetaManagedAgentsCommitCheckoutTypeCommit BetaManagedAgentsCommitCheckoutType = "commit"`

### Beta Managed Agents Deleted Session

- `type BetaManagedAgentsDeletedSession struct{…}`

  Confirmation that a `session` has been permanently deleted.

  - `ID string`

  - `Type BetaManagedAgentsDeletedSessionType`

    - `const BetaManagedAgentsDeletedSessionTypeSessionDeleted BetaManagedAgentsDeletedSessionType = "session_deleted"`

### Beta Managed Agents File Resource Params

- `type BetaManagedAgentsFileResourceParamsResp struct{…}`

  Mount a file uploaded via the Files API into the session.

  - `FileID string`

    ID of a previously uploaded file.

  - `Type BetaManagedAgentsFileResourceParamsType`

    - `const BetaManagedAgentsFileResourceParamsTypeFile BetaManagedAgentsFileResourceParamsType = "file"`

  - `MountPath string`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

### Beta Managed Agents GitHub Repository Resource Params

- `type BetaManagedAgentsGitHubRepositoryResourceParamsResp struct{…}`

  Mount a GitHub repository into the session's container.

  - `AuthorizationToken string`

    GitHub authorization token used to clone the repository.

  - `Type BetaManagedAgentsGitHubRepositoryResourceParamsType`

    - `const BetaManagedAgentsGitHubRepositoryResourceParamsTypeGitHubRepository BetaManagedAgentsGitHubRepositoryResourceParamsType = "github_repository"`

  - `URL string`

    Github URL of the repository

  - `Checkout BetaManagedAgentsGitHubRepositoryResourceParamsCheckoutUnionResp`

    Branch or commit to check out. Defaults to the repository's default branch.

    - `type BetaManagedAgentsBranchCheckout struct{…}`

      - `Name string`

        Branch name to check out.

      - `Type BetaManagedAgentsBranchCheckoutType`

        - `const BetaManagedAgentsBranchCheckoutTypeBranch BetaManagedAgentsBranchCheckoutType = "branch"`

    - `type BetaManagedAgentsCommitCheckout struct{…}`

      - `Sha string`

        Full commit SHA to check out.

      - `Type BetaManagedAgentsCommitCheckoutType`

        - `const BetaManagedAgentsCommitCheckoutTypeCommit BetaManagedAgentsCommitCheckoutType = "commit"`

  - `MountPath string`

    Mount path in the container. Defaults to `/workspace/<repo-name>`.

### Beta Managed Agents Session

- `type BetaManagedAgentsSession struct{…}`

  A Managed Agents `session`.

  - `ID string`

  - `Agent BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

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

    - `Skills []BetaManagedAgentsSessionAgentSkillUnion`

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

    - `Tools []BetaManagedAgentsSessionAgentToolUnion`

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

    - `Type BetaManagedAgentsSessionAgentType`

      - `const BetaManagedAgentsSessionAgentTypeAgent BetaManagedAgentsSessionAgentType = "agent"`

    - `Version int64`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `EnvironmentID string`

  - `Metadata map[string, string]`

  - `Resources []BetaManagedAgentsSessionResourceUnion`

    - `type BetaManagedAgentsGitHubRepositoryResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

      - `MountPath string`

      - `Type BetaManagedAgentsGitHubRepositoryResourceType`

        - `const BetaManagedAgentsGitHubRepositoryResourceTypeGitHubRepository BetaManagedAgentsGitHubRepositoryResourceType = "github_repository"`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

      - `URL string`

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnion`

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

          - `Type BetaManagedAgentsBranchCheckoutType`

            - `const BetaManagedAgentsBranchCheckoutTypeBranch BetaManagedAgentsBranchCheckoutType = "branch"`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

          - `Type BetaManagedAgentsCommitCheckoutType`

            - `const BetaManagedAgentsCommitCheckoutTypeCommit BetaManagedAgentsCommitCheckoutType = "commit"`

    - `type BetaManagedAgentsFileResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

      - `FileID string`

      - `MountPath string`

      - `Type BetaManagedAgentsFileResourceType`

        - `const BetaManagedAgentsFileResourceTypeFile BetaManagedAgentsFileResourceType = "file"`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

  - `Stats BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `ActiveSeconds float64`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

    - `DurationSeconds float64`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

  - `Status BetaManagedAgentsSessionStatus`

    SessionStatus enum

    - `const BetaManagedAgentsSessionStatusRescheduling BetaManagedAgentsSessionStatus = "rescheduling"`

    - `const BetaManagedAgentsSessionStatusRunning BetaManagedAgentsSessionStatus = "running"`

    - `const BetaManagedAgentsSessionStatusIdle BetaManagedAgentsSessionStatus = "idle"`

    - `const BetaManagedAgentsSessionStatusTerminated BetaManagedAgentsSessionStatus = "terminated"`

  - `Title string`

  - `Type BetaManagedAgentsSessionType`

    - `const BetaManagedAgentsSessionTypeSession BetaManagedAgentsSessionType = "session"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Usage BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

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

  - `VaultIDs []string`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

### Beta Managed Agents Session Agent

- `type BetaManagedAgentsSessionAgent struct{…}`

  Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

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

  - `Skills []BetaManagedAgentsSessionAgentSkillUnion`

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

  - `Tools []BetaManagedAgentsSessionAgentToolUnion`

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

  - `Type BetaManagedAgentsSessionAgentType`

    - `const BetaManagedAgentsSessionAgentTypeAgent BetaManagedAgentsSessionAgentType = "agent"`

  - `Version int64`

### Beta Managed Agents Session Stats

- `type BetaManagedAgentsSessionStats struct{…}`

  Timing statistics for a session.

  - `ActiveSeconds float64`

    Cumulative time in seconds the session spent in running status. Excludes idle time.

  - `DurationSeconds float64`

    Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

### Beta Managed Agents Session Usage

- `type BetaManagedAgentsSessionUsage struct{…}`

  Cumulative token usage for a session across all turns.

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

# Events

## List

`client.Beta.Sessions.Events.List(ctx, sessionID, params) (*PageCursor[BetaManagedAgentsSessionEventUnion], error)`

**get** `/v1/sessions/{session_id}/events`

List Events

### Parameters

- `sessionID string`

- `params BetaSessionEventListParams`

  - `Limit param.Field[int64]`

    Query param: Query parameter for limit

  - `Order param.Field[BetaSessionEventListParamsOrder]`

    Query param: Sort direction for results, ordered by created_at. Defaults to asc (chronological).

    - `const BetaSessionEventListParamsOrderAsc BetaSessionEventListParamsOrder = "asc"`

    - `const BetaSessionEventListParamsOrderDesc BetaSessionEventListParamsOrder = "desc"`

  - `Page param.Field[string]`

    Query param: Opaque pagination cursor from a previous response's next_page.

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

  - `type BetaManagedAgentsSessionDeletedEvent struct{…}`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSessionDeletedEventType`

      - `const BetaManagedAgentsSessionDeletedEventTypeSessionDeleted BetaManagedAgentsSessionDeletedEventType = "session.deleted"`

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
  page, err := client.Beta.Sessions.Events.List(
    context.TODO(),
    "sesn_011CZkZAtmR3yMPDzynEDxu7",
    anthropic.BetaSessionEventListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

## Send

`client.Beta.Sessions.Events.Send(ctx, sessionID, params) (*BetaManagedAgentsSendSessionEvents, error)`

**post** `/v1/sessions/{session_id}/events`

Send Events

### Parameters

- `sessionID string`

- `params BetaSessionEventSendParams`

  - `Events param.Field[[]BetaManagedAgentsEventParamsUnionResp]`

    Body param: Events to send to the `session`.

    - `type BetaManagedAgentsUserMessageEventParamsResp struct{…}`

      Parameters for sending a user message to the session.

      - `Content []BetaManagedAgentsUserMessageEventParamsContentUnionResp`

        Array of content blocks for the user message.

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

      - `Type BetaManagedAgentsUserMessageEventParamsType`

        - `const BetaManagedAgentsUserMessageEventParamsTypeUserMessage BetaManagedAgentsUserMessageEventParamsType = "user.message"`

    - `type BetaManagedAgentsUserInterruptEventParamsResp struct{…}`

      Parameters for sending an interrupt to pause the agent.

      - `Type BetaManagedAgentsUserInterruptEventParamsType`

        - `const BetaManagedAgentsUserInterruptEventParamsTypeUserInterrupt BetaManagedAgentsUserInterruptEventParamsType = "user.interrupt"`

    - `type BetaManagedAgentsUserToolConfirmationEventParamsResp struct{…}`

      Parameters for confirming or denying a tool execution request.

      - `Result BetaManagedAgentsUserToolConfirmationEventParamsResult`

        UserToolConfirmationResult enum

        - `const BetaManagedAgentsUserToolConfirmationEventParamsResultAllow BetaManagedAgentsUserToolConfirmationEventParamsResult = "allow"`

        - `const BetaManagedAgentsUserToolConfirmationEventParamsResultDeny BetaManagedAgentsUserToolConfirmationEventParamsResult = "deny"`

      - `ToolUseID string`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `Type BetaManagedAgentsUserToolConfirmationEventParamsType`

        - `const BetaManagedAgentsUserToolConfirmationEventParamsTypeUserToolConfirmation BetaManagedAgentsUserToolConfirmationEventParamsType = "user.tool_confirmation"`

      - `DenyMessage string`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `type BetaManagedAgentsUserCustomToolResultEventParamsResp struct{…}`

      Parameters for providing the result of a custom tool execution.

      - `CustomToolUseID string`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `Type BetaManagedAgentsUserCustomToolResultEventParamsType`

        - `const BetaManagedAgentsUserCustomToolResultEventParamsTypeUserCustomToolResult BetaManagedAgentsUserCustomToolResultEventParamsType = "user.custom_tool_result"`

      - `Content []BetaManagedAgentsUserCustomToolResultEventParamsContentUnionResp`

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

### Returns

- `type BetaManagedAgentsSendSessionEvents struct{…}`

  Events that were successfully sent to the session.

  - `Data []BetaManagedAgentsSendSessionEventsDataUnion`

    Sent events

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
  betaManagedAgentsSendSessionEvents, err := client.Beta.Sessions.Events.Send(
    context.TODO(),
    "sesn_011CZkZAtmR3yMPDzynEDxu7",
    anthropic.BetaSessionEventSendParams{
      Events: []anthropic.BetaManagedAgentsEventParamsUnion{anthropic.BetaManagedAgentsEventParamsUnion{
        OfUserMessage: &anthropic.BetaManagedAgentsUserMessageEventParams{
          Content: []anthropic.BetaManagedAgentsUserMessageEventParamsContentUnion{anthropic.BetaManagedAgentsUserMessageEventParamsContentUnion{
            OfText: &anthropic.BetaManagedAgentsTextBlockParam{
              Text: "Where is my order #1234?",
              Type: anthropic.BetaManagedAgentsTextBlockTypeText,
            },
          }},
          Type: anthropic.BetaManagedAgentsUserMessageEventParamsTypeUserMessage,
        },
      }},
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsSendSessionEvents.Data)
}
```

## Stream

`client.Beta.Sessions.Events.Stream(ctx, sessionID, query) (*BetaManagedAgentsStreamSessionEventsUnion, error)`

**get** `/v1/sessions/{session_id}/events/stream`

Stream Events

### Parameters

- `sessionID string`

- `query BetaSessionEventStreamParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

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

### Returns

- `type BetaManagedAgentsStreamSessionEventsUnion interface{…}`

  Server-sent event in the session stream.

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

  - `type BetaManagedAgentsSessionDeletedEvent struct{…}`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSessionDeletedEventType`

      - `const BetaManagedAgentsSessionDeletedEventTypeSessionDeleted BetaManagedAgentsSessionDeletedEventType = "session.deleted"`

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
  stream := client.Beta.Sessions.Events.StreamEvents(
    context.TODO(),
    "sesn_011CZkZAtmR3yMPDzynEDxu7",
    anthropic.BetaSessionEventStreamParams{

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

## Domain Types

### Beta Managed Agents Agent Custom Tool Use Event

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

### Beta Managed Agents Agent MCP Tool Result Event

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

### Beta Managed Agents Agent MCP Tool Use Event

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

### Beta Managed Agents Agent Message Event

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

### Beta Managed Agents Agent Thinking Event

- `type BetaManagedAgentsAgentThinkingEvent struct{…}`

  Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

  - `ID string`

    Unique identifier for this event.

  - `ProcessedAt Time`

    A timestamp in RFC 3339 format

  - `Type BetaManagedAgentsAgentThinkingEventType`

    - `const BetaManagedAgentsAgentThinkingEventTypeAgentThinking BetaManagedAgentsAgentThinkingEventType = "agent.thinking"`

### Beta Managed Agents Agent Thread Context Compacted Event

- `type BetaManagedAgentsAgentThreadContextCompactedEvent struct{…}`

  Indicates that context compaction (summarization) occurred during the session.

  - `ID string`

    Unique identifier for this event.

  - `ProcessedAt Time`

    A timestamp in RFC 3339 format

  - `Type BetaManagedAgentsAgentThreadContextCompactedEventType`

    - `const BetaManagedAgentsAgentThreadContextCompactedEventTypeAgentThreadContextCompacted BetaManagedAgentsAgentThreadContextCompactedEventType = "agent.thread_context_compacted"`

### Beta Managed Agents Agent Tool Result Event

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

### Beta Managed Agents Agent Tool Use Event

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

### Beta Managed Agents Base64 Document Source

- `type BetaManagedAgentsBase64DocumentSource struct{…}`

  Base64-encoded document data.

  - `Data string`

    Base64-encoded document data.

  - `MediaType string`

    MIME type of the document (e.g., "application/pdf").

  - `Type BetaManagedAgentsBase64DocumentSourceType`

    - `const BetaManagedAgentsBase64DocumentSourceTypeBase64 BetaManagedAgentsBase64DocumentSourceType = "base64"`

### Beta Managed Agents Base64 Image Source

- `type BetaManagedAgentsBase64ImageSource struct{…}`

  Base64-encoded image data.

  - `Data string`

    Base64-encoded image data.

  - `MediaType string`

    MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

  - `Type BetaManagedAgentsBase64ImageSourceType`

    - `const BetaManagedAgentsBase64ImageSourceTypeBase64 BetaManagedAgentsBase64ImageSourceType = "base64"`

### Beta Managed Agents Billing Error

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

### Beta Managed Agents Document Block

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

### Beta Managed Agents Event Params

- `type BetaManagedAgentsEventParamsUnionResp interface{…}`

  Union type for event parameters that can be sent to a session.

  - `type BetaManagedAgentsUserMessageEventParamsResp struct{…}`

    Parameters for sending a user message to the session.

    - `Content []BetaManagedAgentsUserMessageEventParamsContentUnionResp`

      Array of content blocks for the user message.

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

    - `Type BetaManagedAgentsUserMessageEventParamsType`

      - `const BetaManagedAgentsUserMessageEventParamsTypeUserMessage BetaManagedAgentsUserMessageEventParamsType = "user.message"`

  - `type BetaManagedAgentsUserInterruptEventParamsResp struct{…}`

    Parameters for sending an interrupt to pause the agent.

    - `Type BetaManagedAgentsUserInterruptEventParamsType`

      - `const BetaManagedAgentsUserInterruptEventParamsTypeUserInterrupt BetaManagedAgentsUserInterruptEventParamsType = "user.interrupt"`

  - `type BetaManagedAgentsUserToolConfirmationEventParamsResp struct{…}`

    Parameters for confirming or denying a tool execution request.

    - `Result BetaManagedAgentsUserToolConfirmationEventParamsResult`

      UserToolConfirmationResult enum

      - `const BetaManagedAgentsUserToolConfirmationEventParamsResultAllow BetaManagedAgentsUserToolConfirmationEventParamsResult = "allow"`

      - `const BetaManagedAgentsUserToolConfirmationEventParamsResultDeny BetaManagedAgentsUserToolConfirmationEventParamsResult = "deny"`

    - `ToolUseID string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type BetaManagedAgentsUserToolConfirmationEventParamsType`

      - `const BetaManagedAgentsUserToolConfirmationEventParamsTypeUserToolConfirmation BetaManagedAgentsUserToolConfirmationEventParamsType = "user.tool_confirmation"`

    - `DenyMessage string`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

  - `type BetaManagedAgentsUserCustomToolResultEventParamsResp struct{…}`

    Parameters for providing the result of a custom tool execution.

    - `CustomToolUseID string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type BetaManagedAgentsUserCustomToolResultEventParamsType`

      - `const BetaManagedAgentsUserCustomToolResultEventParamsTypeUserCustomToolResult BetaManagedAgentsUserCustomToolResultEventParamsType = "user.custom_tool_result"`

    - `Content []BetaManagedAgentsUserCustomToolResultEventParamsContentUnionResp`

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

### Beta Managed Agents File Document Source

- `type BetaManagedAgentsFileDocumentSource struct{…}`

  Document referenced by file ID.

  - `FileID string`

    ID of a previously uploaded file.

  - `Type BetaManagedAgentsFileDocumentSourceType`

    - `const BetaManagedAgentsFileDocumentSourceTypeFile BetaManagedAgentsFileDocumentSourceType = "file"`

### Beta Managed Agents File Image Source

- `type BetaManagedAgentsFileImageSource struct{…}`

  Image referenced by file ID.

  - `FileID string`

    ID of a previously uploaded file.

  - `Type BetaManagedAgentsFileImageSourceType`

    - `const BetaManagedAgentsFileImageSourceTypeFile BetaManagedAgentsFileImageSourceType = "file"`

### Beta Managed Agents Image Block

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

### Beta Managed Agents MCP Authentication Failed Error

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

### Beta Managed Agents MCP Connection Failed Error

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

### Beta Managed Agents Model Overloaded Error

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

### Beta Managed Agents Model Rate Limited Error

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

### Beta Managed Agents Model Request Failed Error

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

### Beta Managed Agents Plain Text Document Source

- `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

  Plain text document content.

  - `Data string`

    The plain text content.

  - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

    MIME type of the text content. Must be "text/plain".

    - `const BetaManagedAgentsPlainTextDocumentSourceMediaTypeTextPlain BetaManagedAgentsPlainTextDocumentSourceMediaType = "text/plain"`

  - `Type BetaManagedAgentsPlainTextDocumentSourceType`

    - `const BetaManagedAgentsPlainTextDocumentSourceTypeText BetaManagedAgentsPlainTextDocumentSourceType = "text"`

### Beta Managed Agents Retry Status Exhausted

- `type BetaManagedAgentsRetryStatusExhausted struct{…}`

  This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

  - `Type BetaManagedAgentsRetryStatusExhaustedType`

    - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

### Beta Managed Agents Retry Status Retrying

- `type BetaManagedAgentsRetryStatusRetrying struct{…}`

  The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

  - `Type BetaManagedAgentsRetryStatusRetryingType`

    - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

### Beta Managed Agents Retry Status Terminal

- `type BetaManagedAgentsRetryStatusTerminal struct{…}`

  The session encountered a terminal error and will transition to `terminated` state.

  - `Type BetaManagedAgentsRetryStatusTerminalType`

    - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

### Beta Managed Agents Send Session Events

- `type BetaManagedAgentsSendSessionEvents struct{…}`

  Events that were successfully sent to the session.

  - `Data []BetaManagedAgentsSendSessionEventsDataUnion`

    Sent events

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

### Beta Managed Agents Session Deleted Event

- `type BetaManagedAgentsSessionDeletedEvent struct{…}`

  Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

  - `ID string`

    Unique identifier for this event.

  - `ProcessedAt Time`

    A timestamp in RFC 3339 format

  - `Type BetaManagedAgentsSessionDeletedEventType`

    - `const BetaManagedAgentsSessionDeletedEventTypeSessionDeleted BetaManagedAgentsSessionDeletedEventType = "session.deleted"`

### Beta Managed Agents Session End Turn

- `type BetaManagedAgentsSessionEndTurn struct{…}`

  The agent completed its turn naturally and is ready for the next user message.

  - `Type BetaManagedAgentsSessionEndTurnType`

    - `const BetaManagedAgentsSessionEndTurnTypeEndTurn BetaManagedAgentsSessionEndTurnType = "end_turn"`

### Beta Managed Agents Session Error Event

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

### Beta Managed Agents Session Event

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

  - `type BetaManagedAgentsSessionDeletedEvent struct{…}`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSessionDeletedEventType`

      - `const BetaManagedAgentsSessionDeletedEventTypeSessionDeleted BetaManagedAgentsSessionDeletedEventType = "session.deleted"`

### Beta Managed Agents Session Requires Action

- `type BetaManagedAgentsSessionRequiresAction struct{…}`

  The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

  - `EventIDs []string`

    The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

  - `Type BetaManagedAgentsSessionRequiresActionType`

    - `const BetaManagedAgentsSessionRequiresActionTypeRequiresAction BetaManagedAgentsSessionRequiresActionType = "requires_action"`

### Beta Managed Agents Session Retries Exhausted

- `type BetaManagedAgentsSessionRetriesExhausted struct{…}`

  The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

  - `Type BetaManagedAgentsSessionRetriesExhaustedType`

    - `const BetaManagedAgentsSessionRetriesExhaustedTypeRetriesExhausted BetaManagedAgentsSessionRetriesExhaustedType = "retries_exhausted"`

### Beta Managed Agents Session Status Idle Event

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

### Beta Managed Agents Session Status Rescheduled Event

- `type BetaManagedAgentsSessionStatusRescheduledEvent struct{…}`

  Indicates the session is recovering from an error state and is rescheduled for execution.

  - `ID string`

    Unique identifier for this event.

  - `ProcessedAt Time`

    A timestamp in RFC 3339 format

  - `Type BetaManagedAgentsSessionStatusRescheduledEventType`

    - `const BetaManagedAgentsSessionStatusRescheduledEventTypeSessionStatusRescheduled BetaManagedAgentsSessionStatusRescheduledEventType = "session.status_rescheduled"`

### Beta Managed Agents Session Status Running Event

- `type BetaManagedAgentsSessionStatusRunningEvent struct{…}`

  Indicates the session is actively running and the agent is working.

  - `ID string`

    Unique identifier for this event.

  - `ProcessedAt Time`

    A timestamp in RFC 3339 format

  - `Type BetaManagedAgentsSessionStatusRunningEventType`

    - `const BetaManagedAgentsSessionStatusRunningEventTypeSessionStatusRunning BetaManagedAgentsSessionStatusRunningEventType = "session.status_running"`

### Beta Managed Agents Session Status Terminated Event

- `type BetaManagedAgentsSessionStatusTerminatedEvent struct{…}`

  Indicates the session has terminated, either due to an error or completion.

  - `ID string`

    Unique identifier for this event.

  - `ProcessedAt Time`

    A timestamp in RFC 3339 format

  - `Type BetaManagedAgentsSessionStatusTerminatedEventType`

    - `const BetaManagedAgentsSessionStatusTerminatedEventTypeSessionStatusTerminated BetaManagedAgentsSessionStatusTerminatedEventType = "session.status_terminated"`

### Beta Managed Agents Span Model Request End Event

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

### Beta Managed Agents Span Model Request Start Event

- `type BetaManagedAgentsSpanModelRequestStartEvent struct{…}`

  Emitted when a model request is initiated by the agent.

  - `ID string`

    Unique identifier for this event.

  - `ProcessedAt Time`

    A timestamp in RFC 3339 format

  - `Type BetaManagedAgentsSpanModelRequestStartEventType`

    - `const BetaManagedAgentsSpanModelRequestStartEventTypeSpanModelRequestStart BetaManagedAgentsSpanModelRequestStartEventType = "span.model_request_start"`

### Beta Managed Agents Span Model Usage

- `type BetaManagedAgentsSpanModelUsage struct{…}`

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

### Beta Managed Agents Stream Session Events

- `type BetaManagedAgentsStreamSessionEventsUnion interface{…}`

  Server-sent event in the session stream.

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

  - `type BetaManagedAgentsSessionDeletedEvent struct{…}`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSessionDeletedEventType`

      - `const BetaManagedAgentsSessionDeletedEventTypeSessionDeleted BetaManagedAgentsSessionDeletedEventType = "session.deleted"`

### Beta Managed Agents Text Block

- `type BetaManagedAgentsTextBlock struct{…}`

  Regular text content.

  - `Text string`

    The text content.

  - `Type BetaManagedAgentsTextBlockType`

    - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

### Beta Managed Agents Unknown Error

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

### Beta Managed Agents URL Document Source

- `type BetaManagedAgentsURLDocumentSource struct{…}`

  Document referenced by URL.

  - `Type BetaManagedAgentsURLDocumentSourceType`

    - `const BetaManagedAgentsURLDocumentSourceTypeURL BetaManagedAgentsURLDocumentSourceType = "url"`

  - `URL string`

    URL of the document to fetch.

### Beta Managed Agents URL Image Source

- `type BetaManagedAgentsURLImageSource struct{…}`

  Image referenced by URL.

  - `Type BetaManagedAgentsURLImageSourceType`

    - `const BetaManagedAgentsURLImageSourceTypeURL BetaManagedAgentsURLImageSourceType = "url"`

  - `URL string`

    URL of the image to fetch.

### Beta Managed Agents User Custom Tool Result Event

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

### Beta Managed Agents User Custom Tool Result Event Params

- `type BetaManagedAgentsUserCustomToolResultEventParamsResp struct{…}`

  Parameters for providing the result of a custom tool execution.

  - `CustomToolUseID string`

    The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `Type BetaManagedAgentsUserCustomToolResultEventParamsType`

    - `const BetaManagedAgentsUserCustomToolResultEventParamsTypeUserCustomToolResult BetaManagedAgentsUserCustomToolResultEventParamsType = "user.custom_tool_result"`

  - `Content []BetaManagedAgentsUserCustomToolResultEventParamsContentUnionResp`

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

### Beta Managed Agents User Interrupt Event

- `type BetaManagedAgentsUserInterruptEvent struct{…}`

  An interrupt event that pauses agent execution and returns control to the user.

  - `ID string`

    Unique identifier for this event.

  - `Type BetaManagedAgentsUserInterruptEventType`

    - `const BetaManagedAgentsUserInterruptEventTypeUserInterrupt BetaManagedAgentsUserInterruptEventType = "user.interrupt"`

  - `ProcessedAt Time`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Interrupt Event Params

- `type BetaManagedAgentsUserInterruptEventParamsResp struct{…}`

  Parameters for sending an interrupt to pause the agent.

  - `Type BetaManagedAgentsUserInterruptEventParamsType`

    - `const BetaManagedAgentsUserInterruptEventParamsTypeUserInterrupt BetaManagedAgentsUserInterruptEventParamsType = "user.interrupt"`

### Beta Managed Agents User Message Event

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

### Beta Managed Agents User Message Event Params

- `type BetaManagedAgentsUserMessageEventParamsResp struct{…}`

  Parameters for sending a user message to the session.

  - `Content []BetaManagedAgentsUserMessageEventParamsContentUnionResp`

    Array of content blocks for the user message.

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

  - `Type BetaManagedAgentsUserMessageEventParamsType`

    - `const BetaManagedAgentsUserMessageEventParamsTypeUserMessage BetaManagedAgentsUserMessageEventParamsType = "user.message"`

### Beta Managed Agents User Tool Confirmation Event

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

### Beta Managed Agents User Tool Confirmation Event Params

- `type BetaManagedAgentsUserToolConfirmationEventParamsResp struct{…}`

  Parameters for confirming or denying a tool execution request.

  - `Result BetaManagedAgentsUserToolConfirmationEventParamsResult`

    UserToolConfirmationResult enum

    - `const BetaManagedAgentsUserToolConfirmationEventParamsResultAllow BetaManagedAgentsUserToolConfirmationEventParamsResult = "allow"`

    - `const BetaManagedAgentsUserToolConfirmationEventParamsResultDeny BetaManagedAgentsUserToolConfirmationEventParamsResult = "deny"`

  - `ToolUseID string`

    The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `Type BetaManagedAgentsUserToolConfirmationEventParamsType`

    - `const BetaManagedAgentsUserToolConfirmationEventParamsTypeUserToolConfirmation BetaManagedAgentsUserToolConfirmationEventParamsType = "user.tool_confirmation"`

  - `DenyMessage string`

    Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

# Resources

## Add

`client.Beta.Sessions.Resources.Add(ctx, sessionID, params) (*BetaManagedAgentsFileResource, error)`

**post** `/v1/sessions/{session_id}/resources`

Add Session Resource

### Parameters

- `sessionID string`

- `params BetaSessionResourceAddParams`

  - `BetaManagedAgentsFileResourceParams param.Field[BetaManagedAgentsFileResourceParamsResp]`

    Body param: Mount a file uploaded via the Files API into the session.

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

### Returns

- `type BetaManagedAgentsFileResource struct{…}`

  - `ID string`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `FileID string`

  - `MountPath string`

  - `Type BetaManagedAgentsFileResourceType`

    - `const BetaManagedAgentsFileResourceTypeFile BetaManagedAgentsFileResourceType = "file"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

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
  betaManagedAgentsFileResource, err := client.Beta.Sessions.Resources.Add(
    context.TODO(),
    "sesn_011CZkZAtmR3yMPDzynEDxu7",
    anthropic.BetaSessionResourceAddParams{
      BetaManagedAgentsFileResourceParams: anthropic.BetaManagedAgentsFileResourceParams{
        FileID: "file_011CNha8iCJcU1wXNR6q4V8w",
        Type: anthropic.BetaManagedAgentsFileResourceParamsTypeFile,
      },
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsFileResource.ID)
}
```

## List

`client.Beta.Sessions.Resources.List(ctx, sessionID, params) (*PageCursor[BetaManagedAgentsSessionResourceUnion], error)`

**get** `/v1/sessions/{session_id}/resources`

List Session Resources

### Parameters

- `sessionID string`

- `params BetaSessionResourceListParams`

  - `Limit param.Field[int64]`

    Query param: Maximum number of resources to return per page (max 1000). If omitted, returns all resources.

  - `Page param.Field[string]`

    Query param: Opaque cursor from a previous response's next_page field.

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

### Returns

- `type BetaManagedAgentsSessionResourceUnion interface{…}`

  - `type BetaManagedAgentsGitHubRepositoryResource struct{…}`

    - `ID string`

    - `CreatedAt Time`

      A timestamp in RFC 3339 format

    - `MountPath string`

    - `Type BetaManagedAgentsGitHubRepositoryResourceType`

      - `const BetaManagedAgentsGitHubRepositoryResourceTypeGitHubRepository BetaManagedAgentsGitHubRepositoryResourceType = "github_repository"`

    - `UpdatedAt Time`

      A timestamp in RFC 3339 format

    - `URL string`

    - `Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnion`

      - `type BetaManagedAgentsBranchCheckout struct{…}`

        - `Name string`

          Branch name to check out.

        - `Type BetaManagedAgentsBranchCheckoutType`

          - `const BetaManagedAgentsBranchCheckoutTypeBranch BetaManagedAgentsBranchCheckoutType = "branch"`

      - `type BetaManagedAgentsCommitCheckout struct{…}`

        - `Sha string`

          Full commit SHA to check out.

        - `Type BetaManagedAgentsCommitCheckoutType`

          - `const BetaManagedAgentsCommitCheckoutTypeCommit BetaManagedAgentsCommitCheckoutType = "commit"`

  - `type BetaManagedAgentsFileResource struct{…}`

    - `ID string`

    - `CreatedAt Time`

      A timestamp in RFC 3339 format

    - `FileID string`

    - `MountPath string`

    - `Type BetaManagedAgentsFileResourceType`

      - `const BetaManagedAgentsFileResourceTypeFile BetaManagedAgentsFileResourceType = "file"`

    - `UpdatedAt Time`

      A timestamp in RFC 3339 format

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
  page, err := client.Beta.Sessions.Resources.List(
    context.TODO(),
    "sesn_011CZkZAtmR3yMPDzynEDxu7",
    anthropic.BetaSessionResourceListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

## Retrieve

`client.Beta.Sessions.Resources.Get(ctx, resourceID, params) (*BetaSessionResourceGetResponseUnion, error)`

**get** `/v1/sessions/{session_id}/resources/{resource_id}`

Get Session Resource

### Parameters

- `resourceID string`

- `params BetaSessionResourceGetParams`

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

### Returns

- `type BetaSessionResourceGetResponseUnion interface{…}`

  The requested session resource.

  - `type BetaManagedAgentsGitHubRepositoryResource struct{…}`

    - `ID string`

    - `CreatedAt Time`

      A timestamp in RFC 3339 format

    - `MountPath string`

    - `Type BetaManagedAgentsGitHubRepositoryResourceType`

      - `const BetaManagedAgentsGitHubRepositoryResourceTypeGitHubRepository BetaManagedAgentsGitHubRepositoryResourceType = "github_repository"`

    - `UpdatedAt Time`

      A timestamp in RFC 3339 format

    - `URL string`

    - `Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnion`

      - `type BetaManagedAgentsBranchCheckout struct{…}`

        - `Name string`

          Branch name to check out.

        - `Type BetaManagedAgentsBranchCheckoutType`

          - `const BetaManagedAgentsBranchCheckoutTypeBranch BetaManagedAgentsBranchCheckoutType = "branch"`

      - `type BetaManagedAgentsCommitCheckout struct{…}`

        - `Sha string`

          Full commit SHA to check out.

        - `Type BetaManagedAgentsCommitCheckoutType`

          - `const BetaManagedAgentsCommitCheckoutTypeCommit BetaManagedAgentsCommitCheckoutType = "commit"`

  - `type BetaManagedAgentsFileResource struct{…}`

    - `ID string`

    - `CreatedAt Time`

      A timestamp in RFC 3339 format

    - `FileID string`

    - `MountPath string`

    - `Type BetaManagedAgentsFileResourceType`

      - `const BetaManagedAgentsFileResourceTypeFile BetaManagedAgentsFileResourceType = "file"`

    - `UpdatedAt Time`

      A timestamp in RFC 3339 format

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
  resource, err := client.Beta.Sessions.Resources.Get(
    context.TODO(),
    "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
    anthropic.BetaSessionResourceGetParams{
      SessionID: "sesn_011CZkZAtmR3yMPDzynEDxu7",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", resource)
}
```

## Update

`client.Beta.Sessions.Resources.Update(ctx, resourceID, params) (*BetaSessionResourceUpdateResponseUnion, error)`

**post** `/v1/sessions/{session_id}/resources/{resource_id}`

Update Session Resource

### Parameters

- `resourceID string`

- `params BetaSessionResourceUpdateParams`

  - `SessionID param.Field[string]`

    Path param: Path parameter session_id

  - `AuthorizationToken param.Field[string]`

    Body param: New authorization token for the resource. Currently only `github_repository` resources support token rotation.

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

### Returns

- `type BetaSessionResourceUpdateResponseUnion interface{…}`

  The updated session resource.

  - `type BetaManagedAgentsGitHubRepositoryResource struct{…}`

    - `ID string`

    - `CreatedAt Time`

      A timestamp in RFC 3339 format

    - `MountPath string`

    - `Type BetaManagedAgentsGitHubRepositoryResourceType`

      - `const BetaManagedAgentsGitHubRepositoryResourceTypeGitHubRepository BetaManagedAgentsGitHubRepositoryResourceType = "github_repository"`

    - `UpdatedAt Time`

      A timestamp in RFC 3339 format

    - `URL string`

    - `Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnion`

      - `type BetaManagedAgentsBranchCheckout struct{…}`

        - `Name string`

          Branch name to check out.

        - `Type BetaManagedAgentsBranchCheckoutType`

          - `const BetaManagedAgentsBranchCheckoutTypeBranch BetaManagedAgentsBranchCheckoutType = "branch"`

      - `type BetaManagedAgentsCommitCheckout struct{…}`

        - `Sha string`

          Full commit SHA to check out.

        - `Type BetaManagedAgentsCommitCheckoutType`

          - `const BetaManagedAgentsCommitCheckoutTypeCommit BetaManagedAgentsCommitCheckoutType = "commit"`

  - `type BetaManagedAgentsFileResource struct{…}`

    - `ID string`

    - `CreatedAt Time`

      A timestamp in RFC 3339 format

    - `FileID string`

    - `MountPath string`

    - `Type BetaManagedAgentsFileResourceType`

      - `const BetaManagedAgentsFileResourceTypeFile BetaManagedAgentsFileResourceType = "file"`

    - `UpdatedAt Time`

      A timestamp in RFC 3339 format

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
  resource, err := client.Beta.Sessions.Resources.Update(
    context.TODO(),
    "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
    anthropic.BetaSessionResourceUpdateParams{
      SessionID: "sesn_011CZkZAtmR3yMPDzynEDxu7",
      AuthorizationToken: "ghp_exampletoken",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", resource)
}
```

## Delete

`client.Beta.Sessions.Resources.Delete(ctx, resourceID, params) (*BetaManagedAgentsDeleteSessionResource, error)`

**delete** `/v1/sessions/{session_id}/resources/{resource_id}`

Delete Session Resource

### Parameters

- `resourceID string`

- `params BetaSessionResourceDeleteParams`

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

### Returns

- `type BetaManagedAgentsDeleteSessionResource struct{…}`

  Confirmation of resource deletion.

  - `ID string`

  - `Type BetaManagedAgentsDeleteSessionResourceType`

    - `const BetaManagedAgentsDeleteSessionResourceTypeSessionResourceDeleted BetaManagedAgentsDeleteSessionResourceType = "session_resource_deleted"`

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
  betaManagedAgentsDeleteSessionResource, err := client.Beta.Sessions.Resources.Delete(
    context.TODO(),
    "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
    anthropic.BetaSessionResourceDeleteParams{
      SessionID: "sesn_011CZkZAtmR3yMPDzynEDxu7",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsDeleteSessionResource.ID)
}
```

## Domain Types

### Beta Managed Agents Delete Session Resource

- `type BetaManagedAgentsDeleteSessionResource struct{…}`

  Confirmation of resource deletion.

  - `ID string`

  - `Type BetaManagedAgentsDeleteSessionResourceType`

    - `const BetaManagedAgentsDeleteSessionResourceTypeSessionResourceDeleted BetaManagedAgentsDeleteSessionResourceType = "session_resource_deleted"`

### Beta Managed Agents File Resource

- `type BetaManagedAgentsFileResource struct{…}`

  - `ID string`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `FileID string`

  - `MountPath string`

  - `Type BetaManagedAgentsFileResourceType`

    - `const BetaManagedAgentsFileResourceTypeFile BetaManagedAgentsFileResourceType = "file"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

### Beta Managed Agents GitHub Repository Resource

- `type BetaManagedAgentsGitHubRepositoryResource struct{…}`

  - `ID string`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `MountPath string`

  - `Type BetaManagedAgentsGitHubRepositoryResourceType`

    - `const BetaManagedAgentsGitHubRepositoryResourceTypeGitHubRepository BetaManagedAgentsGitHubRepositoryResourceType = "github_repository"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `URL string`

  - `Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnion`

    - `type BetaManagedAgentsBranchCheckout struct{…}`

      - `Name string`

        Branch name to check out.

      - `Type BetaManagedAgentsBranchCheckoutType`

        - `const BetaManagedAgentsBranchCheckoutTypeBranch BetaManagedAgentsBranchCheckoutType = "branch"`

    - `type BetaManagedAgentsCommitCheckout struct{…}`

      - `Sha string`

        Full commit SHA to check out.

      - `Type BetaManagedAgentsCommitCheckoutType`

        - `const BetaManagedAgentsCommitCheckoutTypeCommit BetaManagedAgentsCommitCheckoutType = "commit"`

### Beta Managed Agents Session Resource

- `type BetaManagedAgentsSessionResourceUnion interface{…}`

  - `type BetaManagedAgentsGitHubRepositoryResource struct{…}`

    - `ID string`

    - `CreatedAt Time`

      A timestamp in RFC 3339 format

    - `MountPath string`

    - `Type BetaManagedAgentsGitHubRepositoryResourceType`

      - `const BetaManagedAgentsGitHubRepositoryResourceTypeGitHubRepository BetaManagedAgentsGitHubRepositoryResourceType = "github_repository"`

    - `UpdatedAt Time`

      A timestamp in RFC 3339 format

    - `URL string`

    - `Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnion`

      - `type BetaManagedAgentsBranchCheckout struct{…}`

        - `Name string`

          Branch name to check out.

        - `Type BetaManagedAgentsBranchCheckoutType`

          - `const BetaManagedAgentsBranchCheckoutTypeBranch BetaManagedAgentsBranchCheckoutType = "branch"`

      - `type BetaManagedAgentsCommitCheckout struct{…}`

        - `Sha string`

          Full commit SHA to check out.

        - `Type BetaManagedAgentsCommitCheckoutType`

          - `const BetaManagedAgentsCommitCheckoutTypeCommit BetaManagedAgentsCommitCheckoutType = "commit"`

  - `type BetaManagedAgentsFileResource struct{…}`

    - `ID string`

    - `CreatedAt Time`

      A timestamp in RFC 3339 format

    - `FileID string`

    - `MountPath string`

    - `Type BetaManagedAgentsFileResourceType`

      - `const BetaManagedAgentsFileResourceTypeFile BetaManagedAgentsFileResourceType = "file"`

    - `UpdatedAt Time`

      A timestamp in RFC 3339 format
