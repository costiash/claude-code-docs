## List Deployment Runs

**get** `/v1/deployment_runs`

List Deployment Runs

### Query Parameters

- `"created_at[gt]": optional string`

  Return runs created strictly after this time (exclusive).

- `"created_at[gte]": optional string`

  Return runs created at or after this time (inclusive).

- `"created_at[lt]": optional string`

  Return runs created strictly before this time (exclusive).

- `"created_at[lte]": optional string`

  Return runs created at or before this time (inclusive).

- `deployment_id: optional string`

  Filter to a specific deployment. Omit to list across all deployments in the workspace. Filtering by a non-existent deployment_id returns 200 with empty data.

- `has_error: optional boolean`

  Filter: true for runs with non-null error, false for runs with non-null session_id. Omit for all.

- `limit: optional number`

  Maximum results per page. Default 20, maximum 1000.

- `page: optional string`

  Opaque pagination cursor. Pass next_page from the previous response. Invalid or expired cursors return 400.

- `trigger_type: optional BetaManagedAgentsTriggerType`

  Filter runs by what triggered them. Omit to return all runs.

  - `"schedule"`

  - `"manual"`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more`

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

- `data: array of BetaManagedAgentsDeploymentRun`

  List of deployment runs.

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

  - `error: BetaManagedAgentsEnvironmentArchivedRunError or BetaManagedAgentsAgentArchivedRunError or BetaManagedAgentsEnvironmentNotFoundRunError or 13 more`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `BetaManagedAgentsEnvironmentArchivedRunError object { message, type }`

      The deployment's environment was archived.

      - `message: string`

        Human-readable error description.

      - `type: "environment_archived_error"`

        - `"environment_archived_error"`

    - `BetaManagedAgentsAgentArchivedRunError object { message, type }`

      The deployment's agent was archived.

      - `message: string`

        Human-readable error description.

      - `type: "agent_archived_error"`

        - `"agent_archived_error"`

    - `BetaManagedAgentsEnvironmentNotFoundRunError object { message, type }`

      The deployment's environment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "environment_not_found_error"`

        - `"environment_not_found_error"`

    - `BetaManagedAgentsVaultNotFoundRunError object { message, type }`

      A vault referenced by the deployment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "vault_not_found_error"`

        - `"vault_not_found_error"`

    - `BetaManagedAgentsVaultArchivedRunError object { message, type }`

      A vault referenced by the deployment is archived.

      - `message: string`

        Human-readable error description.

      - `type: "vault_archived_error"`

        - `"vault_archived_error"`

    - `BetaManagedAgentsFileNotFoundRunError object { message, type }`

      A file resource referenced by the deployment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "file_not_found_error"`

        - `"file_not_found_error"`

    - `BetaManagedAgentsMemoryStoreArchivedRunError object { message, type }`

      A memory store referenced by the deployment is archived.

      - `message: string`

        Human-readable error description.

      - `type: "memory_store_archived_error"`

        - `"memory_store_archived_error"`

    - `BetaManagedAgentsSkillNotFoundRunError object { message, type }`

      A skill referenced by the deployment's agent no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "skill_not_found_error"`

        - `"skill_not_found_error"`

    - `BetaManagedAgentsSessionResourceNotFoundRunError object { message, type }`

      A referenced resource no longer exists and its kind was not reported.

      - `message: string`

        Human-readable error description.

      - `type: "session_resource_not_found_error"`

        - `"session_resource_not_found_error"`

    - `BetaManagedAgentsWorkspaceArchivedRunError object { message, type }`

      The deployment's workspace was archived.

      - `message: string`

        Human-readable error description.

      - `type: "workspace_archived_error"`

        - `"workspace_archived_error"`

    - `BetaManagedAgentsOrganizationDisabledRunError object { message, type }`

      The deployment's organization is disabled.

      - `message: string`

        Human-readable error description.

      - `type: "organization_disabled_error"`

        - `"organization_disabled_error"`

    - `BetaManagedAgentsSessionRateLimitedRunError object { message, type }`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `message: string`

        Human-readable error description.

      - `type: "session_rate_limited_error"`

        - `"session_rate_limited_error"`

    - `BetaManagedAgentsSessionCreationRejectedRunError object { message, type }`

      The session create request was rejected with a non-retryable validation error.

      - `message: string`

        Human-readable error description.

      - `type: "session_creation_rejected_error"`

        - `"session_creation_rejected_error"`

    - `BetaManagedAgentsUnknownRunError object { message, type }`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `message: string`

        Human-readable error description.

      - `type: "unknown_error"`

        - `"unknown_error"`

    - `BetaManagedAgentsSelfHostedResourcesUnsupportedRunError object { message, type }`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `message: string`

        Human-readable error description.

      - `type: "self_hosted_resources_unsupported_error"`

        - `"self_hosted_resources_unsupported_error"`

    - `BetaManagedAgentsMCPEgressBlockedRunError object { message, type }`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `message: string`

        Human-readable error description.

      - `type: "mcp_egress_blocked_error"`

        - `"mcp_egress_blocked_error"`

  - `session_id: string`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `trigger_context: BetaManagedAgentsTriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `BetaManagedAgentsScheduleTriggerContext object { scheduled_at, type }`

      The run was fired by the deployment's cron schedule.

      - `scheduled_at: string`

        A timestamp in RFC 3339 format

      - `type: "schedule"`

        - `"schedule"`

    - `BetaManagedAgentsManualTriggerContext object { type }`

      The run was started manually by creating a session directly against the deployment.

      - `type: "manual"`

        - `"manual"`

  - `type: "deployment_run"`

    - `"deployment_run"`

- `next_page: optional string`

  Opaque cursor for the next page. Null when no more results.

### Example

```http
curl https://api.anthropic.com/v1/deployment_runs \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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
