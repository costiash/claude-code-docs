## Get Session

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

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

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

          - `const BetaManagedAgentsModelClaudeSonnet5 BetaManagedAgentsModel = "claude-sonnet-5"`

            High-performance model for coding and agents

          - `const BetaManagedAgentsModelClaudeFable5 BetaManagedAgentsModel = "claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `const BetaManagedAgentsModelClaudeOpus4_8 BetaManagedAgentsModel = "claude-opus-4-8"`

            Frontier intelligence for long-running agents and coding

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

    - `Multiagent BetaManagedAgentsSessionMultiagentCoordinator`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `Agents []BetaManagedAgentsSessionThreadAgent`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `ID string`

        - `Description string`

        - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

          - `Name string`

          - `Type BetaManagedAgentsMCPServerURLDefinitionType`

          - `URL string`

        - `Model BetaManagedAgentsModelConfig`

          Model identifier and configuration.

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

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

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

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

            - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfig`

              Resolved default configuration for all tools from an MCP server.

              - `Enabled bool`

              - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

            - `MCPServerName string`

            - `Type BetaManagedAgentsMCPToolsetType`

              - `const BetaManagedAgentsMCPToolsetTypeMCPToolset BetaManagedAgentsMCPToolsetType = "mcp_toolset"`

          - `type BetaManagedAgentsCustomTool struct{…}`

            A custom tool as returned in API responses.

            - `Description string`

            - `InputSchema BetaManagedAgentsCustomToolInputSchema`

              JSON Schema for custom tool input parameters.

              - `Type Object`

                - `const ObjectObject Object = "object"`

              - `Properties map[string, any]`

              - `Required []string`

            - `Name string`

            - `Type BetaManagedAgentsCustomToolType`

              - `const BetaManagedAgentsCustomToolTypeCustom BetaManagedAgentsCustomToolType = "custom"`

        - `Type BetaManagedAgentsSessionThreadAgentType`

          - `const BetaManagedAgentsSessionThreadAgentTypeAgent BetaManagedAgentsSessionThreadAgentType = "agent"`

        - `Version int64`

      - `Type BetaManagedAgentsSessionMultiagentCoordinatorType`

        - `const BetaManagedAgentsSessionMultiagentCoordinatorTypeCoordinator BetaManagedAgentsSessionMultiagentCoordinatorType = "coordinator"`

    - `Name string`

    - `Skills []BetaManagedAgentsSessionAgentSkillUnion`

      - `type BetaManagedAgentsAnthropicSkill struct{…}`

        A resolved Anthropic-managed skill.

      - `type BetaManagedAgentsCustomSkill struct{…}`

        A resolved user-created custom skill.

    - `System string`

    - `Tools []BetaManagedAgentsSessionAgentToolUnion`

      - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

      - `type BetaManagedAgentsMCPToolset struct{…}`

      - `type BetaManagedAgentsCustomTool struct{…}`

        A custom tool as returned in API responses.

    - `Type BetaManagedAgentsSessionAgentType`

      - `const BetaManagedAgentsSessionAgentTypeAgent BetaManagedAgentsSessionAgentType = "agent"`

    - `Version int64`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `EnvironmentID string`

  - `Metadata map[string, string]`

  - `OutcomeEvaluations []BetaManagedAgentsOutcomeEvaluationResource`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

    - `CompletedAt Time`

      A timestamp in RFC 3339 format

    - `Description string`

      What the agent should produce.

    - `Explanation string`

      Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

    - `Iteration int64`

      0-indexed revision cycle the outcome is currently on.

    - `OutcomeID string`

      Server-generated outc_ ID for this outcome.

    - `Result string`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `Type BetaManagedAgentsOutcomeEvaluationResourceType`

      - `const BetaManagedAgentsOutcomeEvaluationResourceTypeOutcomeEvaluation BetaManagedAgentsOutcomeEvaluationResourceType = "outcome_evaluation"`

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

    - `type BetaManagedAgentsMemoryStoreResource struct{…}`

      A memory store attached to an agent session.

      - `MemoryStoreID string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type BetaManagedAgentsMemoryStoreResourceType`

        - `const BetaManagedAgentsMemoryStoreResourceTypeMemoryStore BetaManagedAgentsMemoryStoreResourceType = "memory_store"`

      - `Access BetaManagedAgentsMemoryStoreResourceAccess`

        Access mode for an attached memory store.

        - `const BetaManagedAgentsMemoryStoreResourceAccessReadWrite BetaManagedAgentsMemoryStoreResourceAccess = "read_write"`

        - `const BetaManagedAgentsMemoryStoreResourceAccessReadOnly BetaManagedAgentsMemoryStoreResourceAccess = "read_only"`

      - `Description string`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `Instructions string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      - `MountPath string`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `Name string`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

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

  - `DeploymentID string`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

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

#### Response

```json
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "description": "A general-purpose starter agent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-sonnet-4-6",
      "speed": "standard"
    },
    "multiagent": {
      "agents": [
        {
          "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
          "description": "A focused research subagent.",
          "mcp_servers": [
            {
              "name": "example-mcp",
              "type": "url",
              "url": "https://example-server.modelcontextprotocol.io/sse"
            }
          ],
          "model": {
            "id": "claude-sonnet-4-6",
            "speed": "standard"
          },
          "name": "Researcher",
          "skills": [
            {
              "skill_id": "xlsx",
              "type": "anthropic",
              "version": "1"
            }
          ],
          "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
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
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "metadata": {},
  "outcome_evaluations": [
    {
      "completed_at": "2026-03-15T10:02:31Z",
      "description": "Produce a 2-page summary as summary.md",
      "explanation": "All five sections present with inline citations.",
      "iteration": 0,
      "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
      "result": "satisfied",
      "type": "outcome_evaluation"
    }
  ],
  "resources": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0
  },
  "status": "idle",
  "title": "Order #1234 inquiry",
  "type": "session",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  },
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "deployment_id": "deployment_id"
}
```
