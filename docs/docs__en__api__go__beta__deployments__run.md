## Run Deployment Now

`client.Beta.Deployments.Run(ctx, deploymentID, body) (*BetaManagedAgentsDeploymentRun, error)`

**post** `/v1/deployments/{deployment_id}/run`

Run Deployment Now

### Parameters

- `deploymentID string`

- `body BetaDeploymentRunParams`

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

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsDeploymentRun struct{…}`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `ID string`

    Unique identifier for this run (`drun_...`).

  - `Agent BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `ID string`

    - `Type BetaManagedAgentsAgentReferenceType`

      - `const BetaManagedAgentsAgentReferenceTypeAgent BetaManagedAgentsAgentReferenceType = "agent"`

    - `Version int64`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `DeploymentID string`

    ID of the deployment that produced this run.

  - `Error BetaManagedAgentsDeploymentRunErrorUnion`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `type BetaManagedAgentsEnvironmentArchivedRunError struct{…}`

      The deployment's environment was archived.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsEnvironmentArchivedRunErrorType`

        - `const BetaManagedAgentsEnvironmentArchivedRunErrorTypeEnvironmentArchivedError BetaManagedAgentsEnvironmentArchivedRunErrorType = "environment_archived_error"`

    - `type BetaManagedAgentsAgentArchivedRunError struct{…}`

      The deployment's agent was archived.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsAgentArchivedRunErrorType`

        - `const BetaManagedAgentsAgentArchivedRunErrorTypeAgentArchivedError BetaManagedAgentsAgentArchivedRunErrorType = "agent_archived_error"`

    - `type BetaManagedAgentsEnvironmentNotFoundRunError struct{…}`

      The deployment's environment no longer exists.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsEnvironmentNotFoundRunErrorType`

        - `const BetaManagedAgentsEnvironmentNotFoundRunErrorTypeEnvironmentNotFoundError BetaManagedAgentsEnvironmentNotFoundRunErrorType = "environment_not_found_error"`

    - `type BetaManagedAgentsVaultNotFoundRunError struct{…}`

      A vault referenced by the deployment no longer exists.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsVaultNotFoundRunErrorType`

        - `const BetaManagedAgentsVaultNotFoundRunErrorTypeVaultNotFoundError BetaManagedAgentsVaultNotFoundRunErrorType = "vault_not_found_error"`

    - `type BetaManagedAgentsVaultArchivedRunError struct{…}`

      A vault referenced by the deployment is archived.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsVaultArchivedRunErrorType`

        - `const BetaManagedAgentsVaultArchivedRunErrorTypeVaultArchivedError BetaManagedAgentsVaultArchivedRunErrorType = "vault_archived_error"`

    - `type BetaManagedAgentsFileNotFoundRunError struct{…}`

      A file resource referenced by the deployment no longer exists.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsFileNotFoundRunErrorType`

        - `const BetaManagedAgentsFileNotFoundRunErrorTypeFileNotFoundError BetaManagedAgentsFileNotFoundRunErrorType = "file_not_found_error"`

    - `type BetaManagedAgentsMemoryStoreArchivedRunError struct{…}`

      A memory store referenced by the deployment is archived.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsMemoryStoreArchivedRunErrorType`

        - `const BetaManagedAgentsMemoryStoreArchivedRunErrorTypeMemoryStoreArchivedError BetaManagedAgentsMemoryStoreArchivedRunErrorType = "memory_store_archived_error"`

    - `type BetaManagedAgentsSkillNotFoundRunError struct{…}`

      A skill referenced by the deployment's agent no longer exists.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsSkillNotFoundRunErrorType`

        - `const BetaManagedAgentsSkillNotFoundRunErrorTypeSkillNotFoundError BetaManagedAgentsSkillNotFoundRunErrorType = "skill_not_found_error"`

    - `type BetaManagedAgentsSessionResourceNotFoundRunError struct{…}`

      A referenced resource no longer exists and its kind was not reported.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsSessionResourceNotFoundRunErrorType`

        - `const BetaManagedAgentsSessionResourceNotFoundRunErrorTypeSessionResourceNotFoundError BetaManagedAgentsSessionResourceNotFoundRunErrorType = "session_resource_not_found_error"`

    - `type BetaManagedAgentsWorkspaceArchivedRunError struct{…}`

      The deployment's workspace was archived.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsWorkspaceArchivedRunErrorType`

        - `const BetaManagedAgentsWorkspaceArchivedRunErrorTypeWorkspaceArchivedError BetaManagedAgentsWorkspaceArchivedRunErrorType = "workspace_archived_error"`

    - `type BetaManagedAgentsOrganizationDisabledRunError struct{…}`

      The deployment's organization is disabled.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsOrganizationDisabledRunErrorType`

        - `const BetaManagedAgentsOrganizationDisabledRunErrorTypeOrganizationDisabledError BetaManagedAgentsOrganizationDisabledRunErrorType = "organization_disabled_error"`

    - `type BetaManagedAgentsSessionRateLimitedRunError struct{…}`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsSessionRateLimitedRunErrorType`

        - `const BetaManagedAgentsSessionRateLimitedRunErrorTypeSessionRateLimitedError BetaManagedAgentsSessionRateLimitedRunErrorType = "session_rate_limited_error"`

    - `type BetaManagedAgentsSessionCreationRejectedRunError struct{…}`

      The session create request was rejected with a non-retryable validation error.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsSessionCreationRejectedRunErrorType`

        - `const BetaManagedAgentsSessionCreationRejectedRunErrorTypeSessionCreationRejectedError BetaManagedAgentsSessionCreationRejectedRunErrorType = "session_creation_rejected_error"`

    - `type BetaManagedAgentsUnknownRunError struct{…}`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsUnknownRunErrorType`

        - `const BetaManagedAgentsUnknownRunErrorTypeUnknownError BetaManagedAgentsUnknownRunErrorType = "unknown_error"`

    - `type BetaManagedAgentsSelfHostedResourcesUnsupportedRunError struct{…}`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsSelfHostedResourcesUnsupportedRunErrorType`

        - `const BetaManagedAgentsSelfHostedResourcesUnsupportedRunErrorTypeSelfHostedResourcesUnsupportedError BetaManagedAgentsSelfHostedResourcesUnsupportedRunErrorType = "self_hosted_resources_unsupported_error"`

    - `type BetaManagedAgentsMCPEgressBlockedRunError struct{…}`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsMCPEgressBlockedRunErrorType`

        - `const BetaManagedAgentsMCPEgressBlockedRunErrorTypeMCPEgressBlockedError BetaManagedAgentsMCPEgressBlockedRunErrorType = "mcp_egress_blocked_error"`

  - `SessionID string`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `TriggerContext BetaManagedAgentsTriggerContextUnion`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `type BetaManagedAgentsScheduleTriggerContext struct{…}`

      The run was fired by the deployment's cron schedule.

      - `ScheduledAt Time`

        A timestamp in RFC 3339 format

      - `Type BetaManagedAgentsScheduleTriggerContextType`

        - `const BetaManagedAgentsScheduleTriggerContextTypeSchedule BetaManagedAgentsScheduleTriggerContextType = "schedule"`

    - `type BetaManagedAgentsManualTriggerContext struct{…}`

      The run was started manually by creating a session directly against the deployment.

      - `Type BetaManagedAgentsManualTriggerContextType`

        - `const BetaManagedAgentsManualTriggerContextTypeManual BetaManagedAgentsManualTriggerContextType = "manual"`

  - `Type BetaManagedAgentsDeploymentRunType`

    - `const BetaManagedAgentsDeploymentRunTypeDeploymentRun BetaManagedAgentsDeploymentRunType = "deployment_run"`

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
  betaManagedAgentsDeploymentRun, err := client.Beta.Deployments.Run(
    context.TODO(),
    "depl_011CZkZcDH3vPqd7xnEfwTai",
    anthropic.BetaDeploymentRunParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsDeploymentRun.ID)
}
```

#### Response

```json
{
  "id": "id",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "type": "agent",
    "version": 1
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "deployment_id": "deployment_id",
  "error": {
    "message": "message",
    "type": "environment_archived_error"
  },
  "session_id": "session_id",
  "trigger_context": {
    "scheduled_at": "2019-12-27T18:11:19.117Z",
    "type": "schedule"
  },
  "type": "deployment_run"
}
```
