# Deployment Runs

## List Deployment Runs

`client.beta.deploymentRuns.list(DeploymentRunListParamsparams?, RequestOptionsoptions?): PageCursor<BetaManagedAgentsDeploymentRun>`

**get** `/v1/deployment_runs`

List Deployment Runs

### Parameters

- `params: DeploymentRunListParams`

  - `"created_at[gt]"?: string`

    Query param: Return runs created strictly after this time (exclusive).

  - `"created_at[gte]"?: string`

    Query param: Return runs created at or after this time (inclusive).

  - `"created_at[lt]"?: string`

    Query param: Return runs created strictly before this time (exclusive).

  - `"created_at[lte]"?: string`

    Query param: Return runs created at or before this time (inclusive).

  - `deployment_id?: string`

    Query param: Filter to a specific deployment. Omit to list across all deployments in the workspace. Filtering by a non-existent deployment_id returns 200 with empty data.

  - `has_error?: boolean`

    Query param: Filter: true for runs with non-null error, false for runs with non-null session_id. Omit for all.

  - `limit?: number`

    Query param: Maximum results per page. Default 20, maximum 1000.

  - `page?: string`

    Query param: Opaque pagination cursor. Pass next_page from the previous response. Invalid or expired cursors return 400.

  - `trigger_type?: BetaManagedAgentsTriggerType`

    Query param: Filter runs by what triggered them. Omit to return all runs.

    - `"schedule"`

    - `"manual"`

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 25 more`

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

      - `"user-profiles-2026-03-24"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"fallback-credit-2026-06-01"`

### Returns

- `BetaManagedAgentsDeploymentRun`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `id: string`

    Unique identifier for this run (`drun_...`).

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `deployment_id: string`

    ID of the deployment that produced this run.

  - `error: BetaManagedAgentsEnvironmentArchivedRunError | BetaManagedAgentsAgentArchivedRunError | BetaManagedAgentsEnvironmentNotFoundRunError | 13 more | null`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `BetaManagedAgentsEnvironmentArchivedRunError`

      The deployment's environment was archived.

      - `message: string`

        Human-readable error description.

      - `type: "environment_archived_error"`

        - `"environment_archived_error"`

    - `BetaManagedAgentsAgentArchivedRunError`

      The deployment's agent was archived.

      - `message: string`

        Human-readable error description.

      - `type: "agent_archived_error"`

        - `"agent_archived_error"`

    - `BetaManagedAgentsEnvironmentNotFoundRunError`

      The deployment's environment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "environment_not_found_error"`

        - `"environment_not_found_error"`

    - `BetaManagedAgentsVaultNotFoundRunError`

      A vault referenced by the deployment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "vault_not_found_error"`

        - `"vault_not_found_error"`

    - `BetaManagedAgentsVaultArchivedRunError`

      A vault referenced by the deployment is archived.

      - `message: string`

        Human-readable error description.

      - `type: "vault_archived_error"`

        - `"vault_archived_error"`

    - `BetaManagedAgentsFileNotFoundRunError`

      A file resource referenced by the deployment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "file_not_found_error"`

        - `"file_not_found_error"`

    - `BetaManagedAgentsMemoryStoreArchivedRunError`

      A memory store referenced by the deployment is archived.

      - `message: string`

        Human-readable error description.

      - `type: "memory_store_archived_error"`

        - `"memory_store_archived_error"`

    - `BetaManagedAgentsSkillNotFoundRunError`

      A skill referenced by the deployment's agent no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "skill_not_found_error"`

        - `"skill_not_found_error"`

    - `BetaManagedAgentsSessionResourceNotFoundRunError`

      A referenced resource no longer exists and its kind was not reported.

      - `message: string`

        Human-readable error description.

      - `type: "session_resource_not_found_error"`

        - `"session_resource_not_found_error"`

    - `BetaManagedAgentsWorkspaceArchivedRunError`

      The deployment's workspace was archived.

      - `message: string`

        Human-readable error description.

      - `type: "workspace_archived_error"`

        - `"workspace_archived_error"`

    - `BetaManagedAgentsOrganizationDisabledRunError`

      The deployment's organization is disabled.

      - `message: string`

        Human-readable error description.

      - `type: "organization_disabled_error"`

        - `"organization_disabled_error"`

    - `BetaManagedAgentsSessionRateLimitedRunError`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `message: string`

        Human-readable error description.

      - `type: "session_rate_limited_error"`

        - `"session_rate_limited_error"`

    - `BetaManagedAgentsSessionCreationRejectedRunError`

      The session create request was rejected with a non-retryable validation error.

      - `message: string`

        Human-readable error description.

      - `type: "session_creation_rejected_error"`

        - `"session_creation_rejected_error"`

    - `BetaManagedAgentsUnknownRunError`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `message: string`

        Human-readable error description.

      - `type: "unknown_error"`

        - `"unknown_error"`

    - `BetaManagedAgentsSelfHostedResourcesUnsupportedRunError`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `message: string`

        Human-readable error description.

      - `type: "self_hosted_resources_unsupported_error"`

        - `"self_hosted_resources_unsupported_error"`

    - `BetaManagedAgentsMCPEgressBlockedRunError`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `message: string`

        Human-readable error description.

      - `type: "mcp_egress_blocked_error"`

        - `"mcp_egress_blocked_error"`

  - `session_id: string | null`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `trigger_context: BetaManagedAgentsTriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `BetaManagedAgentsScheduleTriggerContext`

      The run was fired by the deployment's cron schedule.

      - `scheduled_at: string`

        A timestamp in RFC 3339 format

      - `type: "schedule"`

        - `"schedule"`

    - `BetaManagedAgentsManualTriggerContext`

      The run was started manually by creating a session directly against the deployment.

      - `type: "manual"`

        - `"manual"`

  - `type: "deployment_run"`

    - `"deployment_run"`

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsDeploymentRun of client.beta.deploymentRuns.list()) {
  console.log(betaManagedAgentsDeploymentRun.id);
}
```

#### Response

```json
{
  "data": [
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
  ],
  "next_page": "next_page"
}
```

## Get Deployment Run

`client.beta.deploymentRuns.retrieve(stringdeploymentRunID, DeploymentRunRetrieveParamsparams?, RequestOptionsoptions?): BetaManagedAgentsDeploymentRun`

**get** `/v1/deployment_runs/{deployment_run_id}`

Get Deployment Run

### Parameters

- `deploymentRunID: string`

- `params: DeploymentRunRetrieveParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 25 more`

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

      - `"user-profiles-2026-03-24"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"fallback-credit-2026-06-01"`

### Returns

- `BetaManagedAgentsDeploymentRun`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `id: string`

    Unique identifier for this run (`drun_...`).

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `deployment_id: string`

    ID of the deployment that produced this run.

  - `error: BetaManagedAgentsEnvironmentArchivedRunError | BetaManagedAgentsAgentArchivedRunError | BetaManagedAgentsEnvironmentNotFoundRunError | 13 more | null`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `BetaManagedAgentsEnvironmentArchivedRunError`

      The deployment's environment was archived.

      - `message: string`

        Human-readable error description.

      - `type: "environment_archived_error"`

        - `"environment_archived_error"`

    - `BetaManagedAgentsAgentArchivedRunError`

      The deployment's agent was archived.

      - `message: string`

        Human-readable error description.

      - `type: "agent_archived_error"`

        - `"agent_archived_error"`

    - `BetaManagedAgentsEnvironmentNotFoundRunError`

      The deployment's environment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "environment_not_found_error"`

        - `"environment_not_found_error"`

    - `BetaManagedAgentsVaultNotFoundRunError`

      A vault referenced by the deployment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "vault_not_found_error"`

        - `"vault_not_found_error"`

    - `BetaManagedAgentsVaultArchivedRunError`

      A vault referenced by the deployment is archived.

      - `message: string`

        Human-readable error description.

      - `type: "vault_archived_error"`

        - `"vault_archived_error"`

    - `BetaManagedAgentsFileNotFoundRunError`

      A file resource referenced by the deployment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "file_not_found_error"`

        - `"file_not_found_error"`

    - `BetaManagedAgentsMemoryStoreArchivedRunError`

      A memory store referenced by the deployment is archived.

      - `message: string`

        Human-readable error description.

      - `type: "memory_store_archived_error"`

        - `"memory_store_archived_error"`

    - `BetaManagedAgentsSkillNotFoundRunError`

      A skill referenced by the deployment's agent no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "skill_not_found_error"`

        - `"skill_not_found_error"`

    - `BetaManagedAgentsSessionResourceNotFoundRunError`

      A referenced resource no longer exists and its kind was not reported.

      - `message: string`

        Human-readable error description.

      - `type: "session_resource_not_found_error"`

        - `"session_resource_not_found_error"`

    - `BetaManagedAgentsWorkspaceArchivedRunError`

      The deployment's workspace was archived.

      - `message: string`

        Human-readable error description.

      - `type: "workspace_archived_error"`

        - `"workspace_archived_error"`

    - `BetaManagedAgentsOrganizationDisabledRunError`

      The deployment's organization is disabled.

      - `message: string`

        Human-readable error description.

      - `type: "organization_disabled_error"`

        - `"organization_disabled_error"`

    - `BetaManagedAgentsSessionRateLimitedRunError`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `message: string`

        Human-readable error description.

      - `type: "session_rate_limited_error"`

        - `"session_rate_limited_error"`

    - `BetaManagedAgentsSessionCreationRejectedRunError`

      The session create request was rejected with a non-retryable validation error.

      - `message: string`

        Human-readable error description.

      - `type: "session_creation_rejected_error"`

        - `"session_creation_rejected_error"`

    - `BetaManagedAgentsUnknownRunError`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `message: string`

        Human-readable error description.

      - `type: "unknown_error"`

        - `"unknown_error"`

    - `BetaManagedAgentsSelfHostedResourcesUnsupportedRunError`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `message: string`

        Human-readable error description.

      - `type: "self_hosted_resources_unsupported_error"`

        - `"self_hosted_resources_unsupported_error"`

    - `BetaManagedAgentsMCPEgressBlockedRunError`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `message: string`

        Human-readable error description.

      - `type: "mcp_egress_blocked_error"`

        - `"mcp_egress_blocked_error"`

  - `session_id: string | null`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `trigger_context: BetaManagedAgentsTriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `BetaManagedAgentsScheduleTriggerContext`

      The run was fired by the deployment's cron schedule.

      - `scheduled_at: string`

        A timestamp in RFC 3339 format

      - `type: "schedule"`

        - `"schedule"`

    - `BetaManagedAgentsManualTriggerContext`

      The run was started manually by creating a session directly against the deployment.

      - `type: "manual"`

        - `"manual"`

  - `type: "deployment_run"`

    - `"deployment_run"`

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsDeploymentRun = await client.beta.deploymentRuns.retrieve(
  'deployment_run_id',
);

console.log(betaManagedAgentsDeploymentRun.id);
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

## Domain Types

### Beta Managed Agents Agent Archived Run Error

- `BetaManagedAgentsAgentArchivedRunError`

  The deployment's agent was archived.

  - `message: string`

    Human-readable error description.

  - `type: "agent_archived_error"`

    - `"agent_archived_error"`

### Beta Managed Agents Deployment Run

- `BetaManagedAgentsDeploymentRun`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `id: string`

    Unique identifier for this run (`drun_...`).

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `deployment_id: string`

    ID of the deployment that produced this run.

  - `error: BetaManagedAgentsEnvironmentArchivedRunError | BetaManagedAgentsAgentArchivedRunError | BetaManagedAgentsEnvironmentNotFoundRunError | 13 more | null`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `BetaManagedAgentsEnvironmentArchivedRunError`

      The deployment's environment was archived.

      - `message: string`

        Human-readable error description.

      - `type: "environment_archived_error"`

        - `"environment_archived_error"`

    - `BetaManagedAgentsAgentArchivedRunError`

      The deployment's agent was archived.

      - `message: string`

        Human-readable error description.

      - `type: "agent_archived_error"`

        - `"agent_archived_error"`

    - `BetaManagedAgentsEnvironmentNotFoundRunError`

      The deployment's environment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "environment_not_found_error"`

        - `"environment_not_found_error"`

    - `BetaManagedAgentsVaultNotFoundRunError`

      A vault referenced by the deployment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "vault_not_found_error"`

        - `"vault_not_found_error"`

    - `BetaManagedAgentsVaultArchivedRunError`

      A vault referenced by the deployment is archived.

      - `message: string`

        Human-readable error description.

      - `type: "vault_archived_error"`

        - `"vault_archived_error"`

    - `BetaManagedAgentsFileNotFoundRunError`

      A file resource referenced by the deployment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "file_not_found_error"`

        - `"file_not_found_error"`

    - `BetaManagedAgentsMemoryStoreArchivedRunError`

      A memory store referenced by the deployment is archived.

      - `message: string`

        Human-readable error description.

      - `type: "memory_store_archived_error"`

        - `"memory_store_archived_error"`

    - `BetaManagedAgentsSkillNotFoundRunError`

      A skill referenced by the deployment's agent no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "skill_not_found_error"`

        - `"skill_not_found_error"`

    - `BetaManagedAgentsSessionResourceNotFoundRunError`

      A referenced resource no longer exists and its kind was not reported.

      - `message: string`

        Human-readable error description.

      - `type: "session_resource_not_found_error"`

        - `"session_resource_not_found_error"`

    - `BetaManagedAgentsWorkspaceArchivedRunError`

      The deployment's workspace was archived.

      - `message: string`

        Human-readable error description.

      - `type: "workspace_archived_error"`

        - `"workspace_archived_error"`

    - `BetaManagedAgentsOrganizationDisabledRunError`

      The deployment's organization is disabled.

      - `message: string`

        Human-readable error description.

      - `type: "organization_disabled_error"`

        - `"organization_disabled_error"`

    - `BetaManagedAgentsSessionRateLimitedRunError`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `message: string`

        Human-readable error description.

      - `type: "session_rate_limited_error"`

        - `"session_rate_limited_error"`

    - `BetaManagedAgentsSessionCreationRejectedRunError`

      The session create request was rejected with a non-retryable validation error.

      - `message: string`

        Human-readable error description.

      - `type: "session_creation_rejected_error"`

        - `"session_creation_rejected_error"`

    - `BetaManagedAgentsUnknownRunError`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `message: string`

        Human-readable error description.

      - `type: "unknown_error"`

        - `"unknown_error"`

    - `BetaManagedAgentsSelfHostedResourcesUnsupportedRunError`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `message: string`

        Human-readable error description.

      - `type: "self_hosted_resources_unsupported_error"`

        - `"self_hosted_resources_unsupported_error"`

    - `BetaManagedAgentsMCPEgressBlockedRunError`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `message: string`

        Human-readable error description.

      - `type: "mcp_egress_blocked_error"`

        - `"mcp_egress_blocked_error"`

  - `session_id: string | null`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `trigger_context: BetaManagedAgentsTriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `BetaManagedAgentsScheduleTriggerContext`

      The run was fired by the deployment's cron schedule.

      - `scheduled_at: string`

        A timestamp in RFC 3339 format

      - `type: "schedule"`

        - `"schedule"`

    - `BetaManagedAgentsManualTriggerContext`

      The run was started manually by creating a session directly against the deployment.

      - `type: "manual"`

        - `"manual"`

  - `type: "deployment_run"`

    - `"deployment_run"`

### Beta Managed Agents Environment Archived Run Error

- `BetaManagedAgentsEnvironmentArchivedRunError`

  The deployment's environment was archived.

  - `message: string`

    Human-readable error description.

  - `type: "environment_archived_error"`

    - `"environment_archived_error"`

### Beta Managed Agents Environment Not Found Run Error

- `BetaManagedAgentsEnvironmentNotFoundRunError`

  The deployment's environment no longer exists.

  - `message: string`

    Human-readable error description.

  - `type: "environment_not_found_error"`

    - `"environment_not_found_error"`

### Beta Managed Agents File Not Found Run Error

- `BetaManagedAgentsFileNotFoundRunError`

  A file resource referenced by the deployment no longer exists.

  - `message: string`

    Human-readable error description.

  - `type: "file_not_found_error"`

    - `"file_not_found_error"`

### Beta Managed Agents Manual Trigger Context

- `BetaManagedAgentsManualTriggerContext`

  The run was started manually by creating a session directly against the deployment.

  - `type: "manual"`

    - `"manual"`

### Beta Managed Agents MCP Egress Blocked Run Error

- `BetaManagedAgentsMCPEgressBlockedRunError`

  An MCP server host used by the deployment's agent is blocked by the environment's network policy.

  - `message: string`

    Human-readable error description.

  - `type: "mcp_egress_blocked_error"`

    - `"mcp_egress_blocked_error"`

### Beta Managed Agents Memory Store Archived Run Error

- `BetaManagedAgentsMemoryStoreArchivedRunError`

  A memory store referenced by the deployment is archived.

  - `message: string`

    Human-readable error description.

  - `type: "memory_store_archived_error"`

    - `"memory_store_archived_error"`

### Beta Managed Agents Organization Disabled Run Error

- `BetaManagedAgentsOrganizationDisabledRunError`

  The deployment's organization is disabled.

  - `message: string`

    Human-readable error description.

  - `type: "organization_disabled_error"`

    - `"organization_disabled_error"`

### Beta Managed Agents Schedule Trigger Context

- `BetaManagedAgentsScheduleTriggerContext`

  The run was fired by the deployment's cron schedule.

  - `scheduled_at: string`

    A timestamp in RFC 3339 format

  - `type: "schedule"`

    - `"schedule"`

### Beta Managed Agents Self Hosted Resources Unsupported Run Error

- `BetaManagedAgentsSelfHostedResourcesUnsupportedRunError`

  The deployment configures resources, but its environment is self-hosted and cannot mount them.

  - `message: string`

    Human-readable error description.

  - `type: "self_hosted_resources_unsupported_error"`

    - `"self_hosted_resources_unsupported_error"`

### Beta Managed Agents Session Creation Rejected Run Error

- `BetaManagedAgentsSessionCreationRejectedRunError`

  The session create request was rejected with a non-retryable validation error.

  - `message: string`

    Human-readable error description.

  - `type: "session_creation_rejected_error"`

    - `"session_creation_rejected_error"`

### Beta Managed Agents Session Rate Limited Run Error

- `BetaManagedAgentsSessionRateLimitedRunError`

  Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

  - `message: string`

    Human-readable error description.

  - `type: "session_rate_limited_error"`

    - `"session_rate_limited_error"`

### Beta Managed Agents Session Resource Not Found Run Error

- `BetaManagedAgentsSessionResourceNotFoundRunError`

  A referenced resource no longer exists and its kind was not reported.

  - `message: string`

    Human-readable error description.

  - `type: "session_resource_not_found_error"`

    - `"session_resource_not_found_error"`

### Beta Managed Agents Skill Not Found Run Error

- `BetaManagedAgentsSkillNotFoundRunError`

  A skill referenced by the deployment's agent no longer exists.

  - `message: string`

    Human-readable error description.

  - `type: "skill_not_found_error"`

    - `"skill_not_found_error"`

### Beta Managed Agents Trigger Context

- `BetaManagedAgentsTriggerContext = BetaManagedAgentsScheduleTriggerContext | BetaManagedAgentsManualTriggerContext`

  Describes what triggered a deployment run, with trigger-specific metadata.

  - `BetaManagedAgentsScheduleTriggerContext`

    The run was fired by the deployment's cron schedule.

    - `scheduled_at: string`

      A timestamp in RFC 3339 format

    - `type: "schedule"`

      - `"schedule"`

  - `BetaManagedAgentsManualTriggerContext`

    The run was started manually by creating a session directly against the deployment.

    - `type: "manual"`

      - `"manual"`

### Beta Managed Agents Trigger Type

- `BetaManagedAgentsTriggerType = "schedule" | "manual"`

  What triggered a deployment run.

  - `"schedule"`

  - `"manual"`

### Beta Managed Agents Unknown Run Error

- `BetaManagedAgentsUnknownRunError`

  An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

  - `message: string`

    Human-readable error description.

  - `type: "unknown_error"`

    - `"unknown_error"`

### Beta Managed Agents Vault Archived Run Error

- `BetaManagedAgentsVaultArchivedRunError`

  A vault referenced by the deployment is archived.

  - `message: string`

    Human-readable error description.

  - `type: "vault_archived_error"`

    - `"vault_archived_error"`

### Beta Managed Agents Vault Not Found Run Error

- `BetaManagedAgentsVaultNotFoundRunError`

  A vault referenced by the deployment no longer exists.

  - `message: string`

    Human-readable error description.

  - `type: "vault_not_found_error"`

    - `"vault_not_found_error"`

### Beta Managed Agents Workspace Archived Run Error

- `BetaManagedAgentsWorkspaceArchivedRunError`

  The deployment's workspace was archived.

  - `message: string`

    Human-readable error description.

  - `type: "workspace_archived_error"`

    - `"workspace_archived_error"`
