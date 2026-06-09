## Run Deployment Now

`BetaManagedAgentsDeploymentRun beta().deployments().run(DeploymentRunParamsparams = DeploymentRunParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/deployments/{deployment_id}/run`

Run Deployment Now

### Parameters

- `DeploymentRunParams params`

  - `Optional<String> deploymentId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

### Returns

- `class BetaManagedAgentsDeploymentRun:`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `String id`

    Unique identifier for this run (`drun_...`).

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

    - `String id`

    - `Type type`

      - `AGENT("agent")`

    - `long version`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String deploymentId`

    ID of the deployment that produced this run.

  - `Optional<Error> error`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `class BetaManagedAgentsEnvironmentArchivedRunError:`

      The deployment's environment was archived.

      - `String message`

        Human-readable error description.

      - `Type type`

        - `ENVIRONMENT_ARCHIVED_ERROR("environment_archived_error")`

    - `class BetaManagedAgentsAgentArchivedRunError:`

      The deployment's agent was archived.

      - `String message`

        Human-readable error description.

      - `Type type`

        - `AGENT_ARCHIVED_ERROR("agent_archived_error")`

    - `class BetaManagedAgentsEnvironmentNotFoundRunError:`

      The deployment's environment no longer exists.

      - `String message`

        Human-readable error description.

      - `Type type`

        - `ENVIRONMENT_NOT_FOUND_ERROR("environment_not_found_error")`

    - `class BetaManagedAgentsVaultNotFoundRunError:`

      A vault referenced by the deployment no longer exists.

      - `String message`

        Human-readable error description.

      - `Type type`

        - `VAULT_NOT_FOUND_ERROR("vault_not_found_error")`

    - `class BetaManagedAgentsVaultArchivedRunError:`

      A vault referenced by the deployment is archived.

      - `String message`

        Human-readable error description.

      - `Type type`

        - `VAULT_ARCHIVED_ERROR("vault_archived_error")`

    - `class BetaManagedAgentsFileNotFoundRunError:`

      A file resource referenced by the deployment no longer exists.

      - `String message`

        Human-readable error description.

      - `Type type`

        - `FILE_NOT_FOUND_ERROR("file_not_found_error")`

    - `class BetaManagedAgentsMemoryStoreArchivedRunError:`

      A memory store referenced by the deployment is archived.

      - `String message`

        Human-readable error description.

      - `Type type`

        - `MEMORY_STORE_ARCHIVED_ERROR("memory_store_archived_error")`

    - `class BetaManagedAgentsSkillNotFoundRunError:`

      A skill referenced by the deployment's agent no longer exists.

      - `String message`

        Human-readable error description.

      - `Type type`

        - `SKILL_NOT_FOUND_ERROR("skill_not_found_error")`

    - `class BetaManagedAgentsSessionResourceNotFoundRunError:`

      A referenced resource no longer exists and its kind was not reported.

      - `String message`

        Human-readable error description.

      - `Type type`

        - `SESSION_RESOURCE_NOT_FOUND_ERROR("session_resource_not_found_error")`

    - `class BetaManagedAgentsWorkspaceArchivedRunError:`

      The deployment's workspace was archived.

      - `String message`

        Human-readable error description.

      - `Type type`

        - `WORKSPACE_ARCHIVED_ERROR("workspace_archived_error")`

    - `class BetaManagedAgentsOrganizationDisabledRunError:`

      The deployment's organization is disabled.

      - `String message`

        Human-readable error description.

      - `Type type`

        - `ORGANIZATION_DISABLED_ERROR("organization_disabled_error")`

    - `class BetaManagedAgentsSessionRateLimitedRunError:`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `String message`

        Human-readable error description.

      - `Type type`

        - `SESSION_RATE_LIMITED_ERROR("session_rate_limited_error")`

    - `class BetaManagedAgentsSessionCreationRejectedRunError:`

      The session create request was rejected with a non-retryable validation error.

      - `String message`

        Human-readable error description.

      - `Type type`

        - `SESSION_CREATION_REJECTED_ERROR("session_creation_rejected_error")`

    - `class BetaManagedAgentsUnknownRunError:`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `String message`

        Human-readable error description.

      - `Type type`

        - `UNKNOWN_ERROR("unknown_error")`

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError:`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `String message`

        Human-readable error description.

      - `Type type`

        - `SELF_HOSTED_RESOURCES_UNSUPPORTED_ERROR("self_hosted_resources_unsupported_error")`

    - `class BetaManagedAgentsMcpEgressBlockedRunError:`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `String message`

        Human-readable error description.

      - `Type type`

        - `MCP_EGRESS_BLOCKED_ERROR("mcp_egress_blocked_error")`

  - `Optional<String> sessionId`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `BetaManagedAgentsTriggerContext triggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `class BetaManagedAgentsScheduleTriggerContext:`

      The run was fired by the deployment's cron schedule.

      - `LocalDateTime scheduledAt`

        A timestamp in RFC 3339 format

      - `Type type`

        - `SCHEDULE("schedule")`

    - `class BetaManagedAgentsManualTriggerContext:`

      The run was started manually by creating a session directly against the deployment.

      - `Type type`

        - `MANUAL("manual")`

  - `Type type`

    - `DEPLOYMENT_RUN("deployment_run")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.deploymentruns.BetaManagedAgentsDeploymentRun;
import com.anthropic.models.beta.deployments.DeploymentRunParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsDeploymentRun betaManagedAgentsDeploymentRun = client.beta().deployments().run("deployment_id");
    }
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
