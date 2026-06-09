# Deployment Runs

## List Deployment Runs

`DeploymentRunListPageResponse Beta.DeploymentRuns.List(DeploymentRunListParams?parameters, CancellationTokencancellationToken = default)`

**get** `/v1/deployment_runs`

List Deployment Runs

### Parameters

- `DeploymentRunListParams parameters`

  - `DateTimeOffset createdAtGt`

    Query param: Return runs created strictly after this time (exclusive).

  - `DateTimeOffset createdAtGte`

    Query param: Return runs created at or after this time (inclusive).

  - `DateTimeOffset createdAtLt`

    Query param: Return runs created strictly before this time (exclusive).

  - `DateTimeOffset createdAtLte`

    Query param: Return runs created at or before this time (inclusive).

  - `string deploymentID`

    Query param: Filter to a specific deployment. Omit to list across all deployments in the workspace. Filtering by a non-existent deployment_id returns 200 with empty data.

  - `Boolean hasError`

    Query param: Filter: true for runs with non-null error, false for runs with non-null session_id. Omit for all.

  - `Int limit`

    Query param: Maximum results per page. Default 20, maximum 1000.

  - `string page`

    Query param: Opaque pagination cursor. Pass next_page from the previous response. Invalid or expired cursors return 400.

  - `BetaManagedAgentsTriggerType triggerType`

    Query param: Filter runs by what triggered them. Omit to return all runs.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

### Returns

- `class DeploymentRunListPageResponse:`

  Paginated list of deployment runs. Sorted by created_at descending (most recent first).

  - `required IReadOnlyList<BetaManagedAgentsDeploymentRun> Data`

    List of deployment runs.

    - `required string ID`

      Unique identifier for this run (`drun_...`).

    - `required BetaManagedAgentsAgentReference Agent`

      A resolved agent reference with a concrete version.

      - `required string ID`

      - `required Type Type`

        - `"agent"Agent`

      - `required Int Version`

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required string DeploymentID`

      ID of the deployment that produced this run.

    - `required Error? Error`

      Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

      - `class BetaManagedAgentsEnvironmentArchivedRunError:`

        The deployment's environment was archived.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"environment_archived_error"EnvironmentArchivedError`

      - `class BetaManagedAgentsAgentArchivedRunError:`

        The deployment's agent was archived.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"agent_archived_error"AgentArchivedError`

      - `class BetaManagedAgentsEnvironmentNotFoundRunError:`

        The deployment's environment no longer exists.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"environment_not_found_error"EnvironmentNotFoundError`

      - `class BetaManagedAgentsVaultNotFoundRunError:`

        A vault referenced by the deployment no longer exists.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"vault_not_found_error"VaultNotFoundError`

      - `class BetaManagedAgentsVaultArchivedRunError:`

        A vault referenced by the deployment is archived.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"vault_archived_error"VaultArchivedError`

      - `class BetaManagedAgentsFileNotFoundRunError:`

        A file resource referenced by the deployment no longer exists.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"file_not_found_error"FileNotFoundError`

      - `class BetaManagedAgentsMemoryStoreArchivedRunError:`

        A memory store referenced by the deployment is archived.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"memory_store_archived_error"MemoryStoreArchivedError`

      - `class BetaManagedAgentsSkillNotFoundRunError:`

        A skill referenced by the deployment's agent no longer exists.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"skill_not_found_error"SkillNotFoundError`

      - `class BetaManagedAgentsSessionResourceNotFoundRunError:`

        A referenced resource no longer exists and its kind was not reported.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"session_resource_not_found_error"SessionResourceNotFoundError`

      - `class BetaManagedAgentsWorkspaceArchivedRunError:`

        The deployment's workspace was archived.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"workspace_archived_error"WorkspaceArchivedError`

      - `class BetaManagedAgentsOrganizationDisabledRunError:`

        The deployment's organization is disabled.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"organization_disabled_error"OrganizationDisabledError`

      - `class BetaManagedAgentsSessionRateLimitedRunError:`

        Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"session_rate_limited_error"SessionRateLimitedError`

      - `class BetaManagedAgentsSessionCreationRejectedRunError:`

        The session create request was rejected with a non-retryable validation error.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"session_creation_rejected_error"SessionCreationRejectedError`

      - `class BetaManagedAgentsUnknownRunError:`

        An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"unknown_error"UnknownError`

      - `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError:`

        The deployment configures resources, but its environment is self-hosted and cannot mount them.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

      - `class BetaManagedAgentsMcpEgressBlockedRunError:`

        An MCP server host used by the deployment's agent is blocked by the environment's network policy.

        - `required string Message`

          Human-readable error description.

        - `required Type Type`

          - `"mcp_egress_blocked_error"McpEgressBlockedError`

    - `required string? SessionID`

      Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

    - `required BetaManagedAgentsTriggerContext TriggerContext`

      Describes what triggered a deployment run, with trigger-specific metadata.

      - `class BetaManagedAgentsScheduleTriggerContext:`

        The run was fired by the deployment's cron schedule.

        - `required DateTimeOffset ScheduledAt`

          A timestamp in RFC 3339 format

        - `required Type Type`

          - `"schedule"Schedule`

      - `class BetaManagedAgentsManualTriggerContext:`

        The run was started manually by creating a session directly against the deployment.

        - `required Type Type`

          - `"manual"Manual`

    - `required Type Type`

      - `"deployment_run"DeploymentRun`

  - `string? NextPage`

    Opaque cursor for the next page. Null when no more results.

### Example

```csharp
DeploymentRunListParams parameters = new();

var page = await client.Beta.DeploymentRuns.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
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

`BetaManagedAgentsDeploymentRun Beta.DeploymentRuns.Retrieve(DeploymentRunRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/deployment_runs/{deployment_run_id}`

Get Deployment Run

### Parameters

- `DeploymentRunRetrieveParams parameters`

  - `required string deploymentRunID`

    Path parameter deployment_run_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

### Returns

- `class BetaManagedAgentsDeploymentRun:`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `required string ID`

    Unique identifier for this run (`drun_...`).

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

      - `"agent"Agent`

    - `required Int Version`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string DeploymentID`

    ID of the deployment that produced this run.

  - `required Error? Error`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `class BetaManagedAgentsEnvironmentArchivedRunError:`

      The deployment's environment was archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"environment_archived_error"EnvironmentArchivedError`

    - `class BetaManagedAgentsAgentArchivedRunError:`

      The deployment's agent was archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"agent_archived_error"AgentArchivedError`

    - `class BetaManagedAgentsEnvironmentNotFoundRunError:`

      The deployment's environment no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"environment_not_found_error"EnvironmentNotFoundError`

    - `class BetaManagedAgentsVaultNotFoundRunError:`

      A vault referenced by the deployment no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"vault_not_found_error"VaultNotFoundError`

    - `class BetaManagedAgentsVaultArchivedRunError:`

      A vault referenced by the deployment is archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"vault_archived_error"VaultArchivedError`

    - `class BetaManagedAgentsFileNotFoundRunError:`

      A file resource referenced by the deployment no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"file_not_found_error"FileNotFoundError`

    - `class BetaManagedAgentsMemoryStoreArchivedRunError:`

      A memory store referenced by the deployment is archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"memory_store_archived_error"MemoryStoreArchivedError`

    - `class BetaManagedAgentsSkillNotFoundRunError:`

      A skill referenced by the deployment's agent no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"skill_not_found_error"SkillNotFoundError`

    - `class BetaManagedAgentsSessionResourceNotFoundRunError:`

      A referenced resource no longer exists and its kind was not reported.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"session_resource_not_found_error"SessionResourceNotFoundError`

    - `class BetaManagedAgentsWorkspaceArchivedRunError:`

      The deployment's workspace was archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"workspace_archived_error"WorkspaceArchivedError`

    - `class BetaManagedAgentsOrganizationDisabledRunError:`

      The deployment's organization is disabled.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"organization_disabled_error"OrganizationDisabledError`

    - `class BetaManagedAgentsSessionRateLimitedRunError:`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"session_rate_limited_error"SessionRateLimitedError`

    - `class BetaManagedAgentsSessionCreationRejectedRunError:`

      The session create request was rejected with a non-retryable validation error.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"session_creation_rejected_error"SessionCreationRejectedError`

    - `class BetaManagedAgentsUnknownRunError:`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"unknown_error"UnknownError`

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError:`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

    - `class BetaManagedAgentsMcpEgressBlockedRunError:`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"mcp_egress_blocked_error"McpEgressBlockedError`

  - `required string? SessionID`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `required BetaManagedAgentsTriggerContext TriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `class BetaManagedAgentsScheduleTriggerContext:`

      The run was fired by the deployment's cron schedule.

      - `required DateTimeOffset ScheduledAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"schedule"Schedule`

    - `class BetaManagedAgentsManualTriggerContext:`

      The run was started manually by creating a session directly against the deployment.

      - `required Type Type`

        - `"manual"Manual`

  - `required Type Type`

    - `"deployment_run"DeploymentRun`

### Example

```csharp
DeploymentRunRetrieveParams parameters = new()
{
    DeploymentRunID = "deployment_run_id"
};

var betaManagedAgentsDeploymentRun = await client.Beta.DeploymentRuns.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsDeploymentRun);
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

- `class BetaManagedAgentsAgentArchivedRunError:`

  The deployment's agent was archived.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"agent_archived_error"AgentArchivedError`

### Beta Managed Agents Deployment Run

- `class BetaManagedAgentsDeploymentRun:`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `required string ID`

    Unique identifier for this run (`drun_...`).

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

      - `"agent"Agent`

    - `required Int Version`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string DeploymentID`

    ID of the deployment that produced this run.

  - `required Error? Error`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `class BetaManagedAgentsEnvironmentArchivedRunError:`

      The deployment's environment was archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"environment_archived_error"EnvironmentArchivedError`

    - `class BetaManagedAgentsAgentArchivedRunError:`

      The deployment's agent was archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"agent_archived_error"AgentArchivedError`

    - `class BetaManagedAgentsEnvironmentNotFoundRunError:`

      The deployment's environment no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"environment_not_found_error"EnvironmentNotFoundError`

    - `class BetaManagedAgentsVaultNotFoundRunError:`

      A vault referenced by the deployment no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"vault_not_found_error"VaultNotFoundError`

    - `class BetaManagedAgentsVaultArchivedRunError:`

      A vault referenced by the deployment is archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"vault_archived_error"VaultArchivedError`

    - `class BetaManagedAgentsFileNotFoundRunError:`

      A file resource referenced by the deployment no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"file_not_found_error"FileNotFoundError`

    - `class BetaManagedAgentsMemoryStoreArchivedRunError:`

      A memory store referenced by the deployment is archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"memory_store_archived_error"MemoryStoreArchivedError`

    - `class BetaManagedAgentsSkillNotFoundRunError:`

      A skill referenced by the deployment's agent no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"skill_not_found_error"SkillNotFoundError`

    - `class BetaManagedAgentsSessionResourceNotFoundRunError:`

      A referenced resource no longer exists and its kind was not reported.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"session_resource_not_found_error"SessionResourceNotFoundError`

    - `class BetaManagedAgentsWorkspaceArchivedRunError:`

      The deployment's workspace was archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"workspace_archived_error"WorkspaceArchivedError`

    - `class BetaManagedAgentsOrganizationDisabledRunError:`

      The deployment's organization is disabled.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"organization_disabled_error"OrganizationDisabledError`

    - `class BetaManagedAgentsSessionRateLimitedRunError:`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"session_rate_limited_error"SessionRateLimitedError`

    - `class BetaManagedAgentsSessionCreationRejectedRunError:`

      The session create request was rejected with a non-retryable validation error.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"session_creation_rejected_error"SessionCreationRejectedError`

    - `class BetaManagedAgentsUnknownRunError:`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"unknown_error"UnknownError`

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError:`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

    - `class BetaManagedAgentsMcpEgressBlockedRunError:`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

        - `"mcp_egress_blocked_error"McpEgressBlockedError`

  - `required string? SessionID`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `required BetaManagedAgentsTriggerContext TriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `class BetaManagedAgentsScheduleTriggerContext:`

      The run was fired by the deployment's cron schedule.

      - `required DateTimeOffset ScheduledAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"schedule"Schedule`

    - `class BetaManagedAgentsManualTriggerContext:`

      The run was started manually by creating a session directly against the deployment.

      - `required Type Type`

        - `"manual"Manual`

  - `required Type Type`

    - `"deployment_run"DeploymentRun`

### Beta Managed Agents Environment Archived Run Error

- `class BetaManagedAgentsEnvironmentArchivedRunError:`

  The deployment's environment was archived.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"environment_archived_error"EnvironmentArchivedError`

### Beta Managed Agents Environment Not Found Run Error

- `class BetaManagedAgentsEnvironmentNotFoundRunError:`

  The deployment's environment no longer exists.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"environment_not_found_error"EnvironmentNotFoundError`

### Beta Managed Agents File Not Found Run Error

- `class BetaManagedAgentsFileNotFoundRunError:`

  A file resource referenced by the deployment no longer exists.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"file_not_found_error"FileNotFoundError`

### Beta Managed Agents Manual Trigger Context

- `class BetaManagedAgentsManualTriggerContext:`

  The run was started manually by creating a session directly against the deployment.

  - `required Type Type`

    - `"manual"Manual`

### Beta Managed Agents MCP Egress Blocked Run Error

- `class BetaManagedAgentsMcpEgressBlockedRunError:`

  An MCP server host used by the deployment's agent is blocked by the environment's network policy.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"mcp_egress_blocked_error"McpEgressBlockedError`

### Beta Managed Agents Memory Store Archived Run Error

- `class BetaManagedAgentsMemoryStoreArchivedRunError:`

  A memory store referenced by the deployment is archived.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"memory_store_archived_error"MemoryStoreArchivedError`

### Beta Managed Agents Organization Disabled Run Error

- `class BetaManagedAgentsOrganizationDisabledRunError:`

  The deployment's organization is disabled.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"organization_disabled_error"OrganizationDisabledError`

### Beta Managed Agents Schedule Trigger Context

- `class BetaManagedAgentsScheduleTriggerContext:`

  The run was fired by the deployment's cron schedule.

  - `required DateTimeOffset ScheduledAt`

    A timestamp in RFC 3339 format

  - `required Type Type`

    - `"schedule"Schedule`

### Beta Managed Agents Self Hosted Resources Unsupported Run Error

- `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError:`

  The deployment configures resources, but its environment is self-hosted and cannot mount them.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

### Beta Managed Agents Session Creation Rejected Run Error

- `class BetaManagedAgentsSessionCreationRejectedRunError:`

  The session create request was rejected with a non-retryable validation error.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"session_creation_rejected_error"SessionCreationRejectedError`

### Beta Managed Agents Session Rate Limited Run Error

- `class BetaManagedAgentsSessionRateLimitedRunError:`

  Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"session_rate_limited_error"SessionRateLimitedError`

### Beta Managed Agents Session Resource Not Found Run Error

- `class BetaManagedAgentsSessionResourceNotFoundRunError:`

  A referenced resource no longer exists and its kind was not reported.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"session_resource_not_found_error"SessionResourceNotFoundError`

### Beta Managed Agents Skill Not Found Run Error

- `class BetaManagedAgentsSkillNotFoundRunError:`

  A skill referenced by the deployment's agent no longer exists.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"skill_not_found_error"SkillNotFoundError`

### Beta Managed Agents Trigger Context

- `class BetaManagedAgentsTriggerContext: A class that can be one of several variants.union`

  Describes what triggered a deployment run, with trigger-specific metadata.

  - `class BetaManagedAgentsScheduleTriggerContext:`

    The run was fired by the deployment's cron schedule.

    - `required DateTimeOffset ScheduledAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"schedule"Schedule`

  - `class BetaManagedAgentsManualTriggerContext:`

    The run was started manually by creating a session directly against the deployment.

    - `required Type Type`

      - `"manual"Manual`

### Beta Managed Agents Trigger Type

- `enum BetaManagedAgentsTriggerType:`

  What triggered a deployment run.

  - `"schedule"Schedule`

  - `"manual"Manual`

### Beta Managed Agents Unknown Run Error

- `class BetaManagedAgentsUnknownRunError:`

  An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"unknown_error"UnknownError`

### Beta Managed Agents Vault Archived Run Error

- `class BetaManagedAgentsVaultArchivedRunError:`

  A vault referenced by the deployment is archived.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"vault_archived_error"VaultArchivedError`

### Beta Managed Agents Vault Not Found Run Error

- `class BetaManagedAgentsVaultNotFoundRunError:`

  A vault referenced by the deployment no longer exists.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"vault_not_found_error"VaultNotFoundError`

### Beta Managed Agents Workspace Archived Run Error

- `class BetaManagedAgentsWorkspaceArchivedRunError:`

  The deployment's workspace was archived.

  - `required string Message`

    Human-readable error description.

  - `required Type Type`

    - `"workspace_archived_error"WorkspaceArchivedError`
