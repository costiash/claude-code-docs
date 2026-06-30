# Deployments

## Create Deployment

`BetaManagedAgentsDeployment beta().deployments().create(DeploymentCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/deployments`

Create Deployment

### Parameters

- `DeploymentCreateParams params`

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

  - `Agent agent`

    Agent to deploy. Accepts the `agent` ID string, which pins the latest version, or an `agent` object with both id and version specified. The agent must exist and not be archived.

    - `String`

    - `class BetaManagedAgentsAgentParams:`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `String id`

        The `agent` ID.

      - `Type type`

        - `AGENT("agent")`

      - `Optional<Long> version`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

  - `String environmentId`

    ID of the `environment` defining the container configuration for sessions created from this deployment.

  - `List<BetaManagedAgentsDeploymentInitialEventParams> initialEvents`

    Events to send to each session immediately after creation. At least 1, maximum 50.

    - `class BetaManagedAgentsUserMessageEventParams:`

      Parameters for sending a user message to the session.

      - `List<Content> content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

          - `Type type`

            - `TEXT("text")`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `IMAGE("image")`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

                - `TEXT_PLAIN("text/plain")`

              - `Type type`

                - `TEXT("text")`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `DOCUMENT("document")`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

      - `Type type`

        - `USER_MESSAGE("user.message")`

    - `class BetaManagedAgentsUserDefineOutcomeEventParams:`

      Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

      - `String description`

        What the agent should produce. This is the task specification.

      - `Rubric rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubricParams:`

          Rubric referenced by a file uploaded via the Files API.

          - `String fileId`

            ID of the rubric file.

          - `Type type`

            - `FILE("file")`

        - `class BetaManagedAgentsTextRubricParams:`

          Rubric content provided inline as text.

          - `String content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

          - `Type type`

            - `TEXT("text")`

      - `Type type`

        - `USER_DEFINE_OUTCOME("user.define_outcome")`

      - `Optional<Long> maxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsSystemMessageEventParams:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

      - `List<BetaManagedAgentsSystemContentBlock> content`

        System content blocks to append. Text-only.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `Type type`

        - `SYSTEM_MESSAGE("system.message")`

  - `String name`

    Human-readable name for the deployment.

  - `Optional<String> description`

    Description of what the deployment does.

  - `Optional<Metadata> metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `Optional<List<Resource>> resources`

    Resources (e.g. repositories, files) to mount into each session's container. Maximum 500.

    - `class BetaManagedAgentsGitHubRepositoryResourceParams:`

      Mount a GitHub repository into the session's container.

      - `String authorizationToken`

        GitHub authorization token used to clone the repository.

      - `Type type`

        - `GITHUB_REPOSITORY("github_repository")`

      - `String url`

        Github URL of the repository

      - `Optional<Checkout> checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `String name`

            Branch name to check out.

          - `Type type`

            - `BRANCH("branch")`

        - `class BetaManagedAgentsCommitCheckout:`

          - `String sha`

            Full commit SHA to check out.

          - `Type type`

            - `COMMIT("commit")`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceParams:`

      Mount a file uploaded via the Files API into the session.

      - `String fileId`

        ID of a previously uploaded file.

      - `Type type`

        - `FILE("file")`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceParam:`

      Parameters for attaching a memory store to an agent session.

      - `String memoryStoreId`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type type`

        - `MEMORY_STORE("memory_store")`

      - `Optional<Access> access`

        Access mode for an attached memory store.

        - `READ_WRITE("read_write")`

        - `READ_ONLY("read_only")`

      - `Optional<String> instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `Optional<BetaManagedAgentsScheduleParams> schedule`

    5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `Optional<List<String>> vaultIds`

    Vault IDs for stored credentials the agent can use during sessions created from this deployment. Maximum 50.

### Returns

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `String id`

    Unique identifier for this deployment.

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

    - `String id`

    - `Type type`

      - `AGENT("agent")`

    - `long version`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> description`

    Description of what the deployment does.

  - `String environmentId`

    ID of the `environment` where sessions run.

  - `List<BetaManagedAgentsDeploymentInitialEvent> initialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `List<Content> content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

          - `Type type`

            - `TEXT("text")`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `IMAGE("image")`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

                - `TEXT_PLAIN("text/plain")`

              - `Type type`

                - `TEXT("text")`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `DOCUMENT("document")`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

      - `Type type`

        - `USER_MESSAGE("user.message")`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `String description`

        What the agent should produce. This is the task specification.

      - `Rubric rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `String fileId`

            ID of the rubric file.

          - `Type type`

            - `FILE("file")`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `String content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `Type type`

            - `TEXT("text")`

      - `Type type`

        - `USER_DEFINE_OUTCOME("user.define_outcome")`

      - `Optional<Long> maxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `List<BetaManagedAgentsSystemContentBlock> content`

        System content blocks to append. Text-only.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `Type type`

        - `SYSTEM_MESSAGE("system.message")`

  - `Metadata metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `String name`

    Human-readable name.

  - `Optional<BetaManagedAgentsDeploymentPausedReason> pausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `Type type`

        - `MANUAL("manual")`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `BetaManagedAgentsDeploymentPausedReasonError error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `Type type`

            - `ENVIRONMENT_ARCHIVED_ERROR("environment_archived_error")`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `Type type`

            - `AGENT_ARCHIVED_ERROR("agent_archived_error")`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `Type type`

            - `ENVIRONMENT_NOT_FOUND_ERROR("environment_not_found_error")`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `Type type`

            - `VAULT_NOT_FOUND_ERROR("vault_not_found_error")`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `Type type`

            - `FILE_NOT_FOUND_ERROR("file_not_found_error")`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `Type type`

            - `SESSION_RESOURCE_NOT_FOUND_ERROR("session_resource_not_found_error")`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `Type type`

            - `WORKSPACE_ARCHIVED_ERROR("workspace_archived_error")`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `Type type`

            - `ORGANIZATION_DISABLED_ERROR("organization_disabled_error")`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `Type type`

            - `MEMORY_STORE_ARCHIVED_ERROR("memory_store_archived_error")`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `Type type`

            - `SKILL_NOT_FOUND_ERROR("skill_not_found_error")`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `Type type`

            - `VAULT_ARCHIVED_ERROR("vault_archived_error")`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `Type type`

            - `UNKNOWN_ERROR("unknown_error")`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `Type type`

            - `SELF_HOSTED_RESOURCES_UNSUPPORTED_ERROR("self_hosted_resources_unsupported_error")`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `Type type`

            - `MCP_EGRESS_BLOCKED_ERROR("mcp_egress_blocked_error")`

      - `Type type`

        - `ERROR("error")`

  - `List<BetaManagedAgentsSessionResourceConfig> resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `Type type`

        - `GITHUB_REPOSITORY("github_repository")`

      - `String url`

        Github URL of the repository

      - `Optional<Checkout> checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `String name`

            Branch name to check out.

          - `Type type`

            - `BRANCH("branch")`

        - `class BetaManagedAgentsCommitCheckout:`

          - `String sha`

            Full commit SHA to check out.

          - `Type type`

            - `COMMIT("commit")`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `String fileId`

        ID of a previously uploaded file.

      - `Type type`

        - `FILE("file")`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `String memoryStoreId`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type type`

        - `MEMORY_STORE("memory_store")`

      - `Optional<Access> access`

        Access mode for an attached memory store.

        - `READ_WRITE("read_write")`

        - `READ_ONLY("read_only")`

      - `Optional<String> instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `Optional<BetaManagedAgentsSchedule> schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `String expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `String timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `Type type`

      - `CRON("cron")`

    - `Optional<LocalDateTime> lastRunAt`

      A timestamp in RFC 3339 format

    - `Optional<List<LocalDateTime>> upcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `BetaManagedAgentsDeploymentStatus status`

    Lifecycle status of a deployment.

    - `ACTIVE("active")`

    - `PAUSED("paused")`

  - `Type type`

    - `DEPLOYMENT("deployment")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `List<String> vaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.deployments.BetaManagedAgentsDeployment;
import com.anthropic.models.beta.deployments.DeploymentCreateParams;
import com.anthropic.models.beta.sessions.events.BetaManagedAgentsTextBlock;
import com.anthropic.models.beta.sessions.events.BetaManagedAgentsUserMessageEventParams;
import java.util.List;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        DeploymentCreateParams params = DeploymentCreateParams.builder()
            .agent("string")
            .environmentId("x")
            .addUserMessageInitialEvent(List.of(BetaManagedAgentsUserMessageEventParams.Content.ofText(BetaManagedAgentsTextBlock.builder()
                .text("Where is my order #1234?")
                .type(BetaManagedAgentsTextBlock.Type.TEXT)
                .build())))
            .name("x")
            .build();
        BetaManagedAgentsDeployment betaManagedAgentsDeployment = client.beta().deployments().create(params);
    }
}
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

## List Deployments

`DeploymentListPage beta().deployments().list(DeploymentListParamsparams = DeploymentListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/deployments`

List Deployments

### Parameters

- `DeploymentListParams params`

  - `Optional<String> agentId`

    Filter by agent ID.

  - `Optional<LocalDateTime> createdAtGte`

    Return deployments created at or after this time (inclusive).

  - `Optional<LocalDateTime> createdAtLte`

    Return deployments created at or before this time (inclusive).

  - `Optional<Boolean> includeArchived`

    When true, includes archived deployments. Default: false (exclude archived).

  - `Optional<Long> limit`

    Maximum results per page. Default 20, maximum 100.

  - `Optional<String> page`

    Opaque pagination cursor.

  - `Optional<BetaManagedAgentsDeploymentStatus> status`

    Filter by status: active or paused. Omit for both. To include archived deployments, use include_archived instead; the two cannot be combined.

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

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `String id`

    Unique identifier for this deployment.

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

    - `String id`

    - `Type type`

      - `AGENT("agent")`

    - `long version`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> description`

    Description of what the deployment does.

  - `String environmentId`

    ID of the `environment` where sessions run.

  - `List<BetaManagedAgentsDeploymentInitialEvent> initialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `List<Content> content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

          - `Type type`

            - `TEXT("text")`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `IMAGE("image")`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

                - `TEXT_PLAIN("text/plain")`

              - `Type type`

                - `TEXT("text")`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `DOCUMENT("document")`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

      - `Type type`

        - `USER_MESSAGE("user.message")`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `String description`

        What the agent should produce. This is the task specification.

      - `Rubric rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `String fileId`

            ID of the rubric file.

          - `Type type`

            - `FILE("file")`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `String content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `Type type`

            - `TEXT("text")`

      - `Type type`

        - `USER_DEFINE_OUTCOME("user.define_outcome")`

      - `Optional<Long> maxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `List<BetaManagedAgentsSystemContentBlock> content`

        System content blocks to append. Text-only.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `Type type`

        - `SYSTEM_MESSAGE("system.message")`

  - `Metadata metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `String name`

    Human-readable name.

  - `Optional<BetaManagedAgentsDeploymentPausedReason> pausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `Type type`

        - `MANUAL("manual")`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `BetaManagedAgentsDeploymentPausedReasonError error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `Type type`

            - `ENVIRONMENT_ARCHIVED_ERROR("environment_archived_error")`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `Type type`

            - `AGENT_ARCHIVED_ERROR("agent_archived_error")`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `Type type`

            - `ENVIRONMENT_NOT_FOUND_ERROR("environment_not_found_error")`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `Type type`

            - `VAULT_NOT_FOUND_ERROR("vault_not_found_error")`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `Type type`

            - `FILE_NOT_FOUND_ERROR("file_not_found_error")`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `Type type`

            - `SESSION_RESOURCE_NOT_FOUND_ERROR("session_resource_not_found_error")`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `Type type`

            - `WORKSPACE_ARCHIVED_ERROR("workspace_archived_error")`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `Type type`

            - `ORGANIZATION_DISABLED_ERROR("organization_disabled_error")`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `Type type`

            - `MEMORY_STORE_ARCHIVED_ERROR("memory_store_archived_error")`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `Type type`

            - `SKILL_NOT_FOUND_ERROR("skill_not_found_error")`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `Type type`

            - `VAULT_ARCHIVED_ERROR("vault_archived_error")`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `Type type`

            - `UNKNOWN_ERROR("unknown_error")`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `Type type`

            - `SELF_HOSTED_RESOURCES_UNSUPPORTED_ERROR("self_hosted_resources_unsupported_error")`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `Type type`

            - `MCP_EGRESS_BLOCKED_ERROR("mcp_egress_blocked_error")`

      - `Type type`

        - `ERROR("error")`

  - `List<BetaManagedAgentsSessionResourceConfig> resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `Type type`

        - `GITHUB_REPOSITORY("github_repository")`

      - `String url`

        Github URL of the repository

      - `Optional<Checkout> checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `String name`

            Branch name to check out.

          - `Type type`

            - `BRANCH("branch")`

        - `class BetaManagedAgentsCommitCheckout:`

          - `String sha`

            Full commit SHA to check out.

          - `Type type`

            - `COMMIT("commit")`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `String fileId`

        ID of a previously uploaded file.

      - `Type type`

        - `FILE("file")`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `String memoryStoreId`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type type`

        - `MEMORY_STORE("memory_store")`

      - `Optional<Access> access`

        Access mode for an attached memory store.

        - `READ_WRITE("read_write")`

        - `READ_ONLY("read_only")`

      - `Optional<String> instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `Optional<BetaManagedAgentsSchedule> schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `String expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `String timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `Type type`

      - `CRON("cron")`

    - `Optional<LocalDateTime> lastRunAt`

      A timestamp in RFC 3339 format

    - `Optional<List<LocalDateTime>> upcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `BetaManagedAgentsDeploymentStatus status`

    Lifecycle status of a deployment.

    - `ACTIVE("active")`

    - `PAUSED("paused")`

  - `Type type`

    - `DEPLOYMENT("deployment")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `List<String> vaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.deployments.DeploymentListPage;
import com.anthropic.models.beta.deployments.DeploymentListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        DeploymentListPage page = client.beta().deployments().list();
    }
}
```

#### Response

```json
{
  "data": [
    {
      "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
      "agent": {
        "id": "agent_011CZkYpogX7uDKUyvBTophP",
        "type": "agent",
        "version": 1
      },
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "description": "Compiles yesterday's orders into a report every weekday morning.",
      "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
      "initial_events": [
        {
          "content": [
            {
              "text": "Compile yesterday's orders into report.md.",
              "type": "text"
            }
          ],
          "type": "user.message"
        }
      ],
      "metadata": {},
      "name": "Daily order report",
      "paused_reason": {
        "type": "manual"
      },
      "resources": [
        {
          "type": "github_repository",
          "url": "url",
          "checkout": {
            "name": "main",
            "type": "branch"
          },
          "mount_path": "mount_path"
        }
      ],
      "schedule": {
        "expression": "0 9 * * 1-5",
        "timezone": "America/Los_Angeles",
        "type": "cron",
        "last_run_at": "2026-03-16T16:00:09Z",
        "upcoming_runs_at": [
          "2026-03-17T16:00:00Z",
          "2026-03-18T16:00:00Z"
        ]
      },
      "status": "active",
      "type": "deployment",
      "updated_at": "2026-03-15T10:00:00Z",
      "vault_ids": [
        "vlt_011CZkZDLs7fYzm1hXNPeRjv"
      ]
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Deployment

`BetaManagedAgentsDeployment beta().deployments().retrieve(DeploymentRetrieveParamsparams = DeploymentRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/deployments/{deployment_id}`

Get Deployment

### Parameters

- `DeploymentRetrieveParams params`

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

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `String id`

    Unique identifier for this deployment.

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

    - `String id`

    - `Type type`

      - `AGENT("agent")`

    - `long version`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> description`

    Description of what the deployment does.

  - `String environmentId`

    ID of the `environment` where sessions run.

  - `List<BetaManagedAgentsDeploymentInitialEvent> initialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `List<Content> content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

          - `Type type`

            - `TEXT("text")`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `IMAGE("image")`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

                - `TEXT_PLAIN("text/plain")`

              - `Type type`

                - `TEXT("text")`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `DOCUMENT("document")`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

      - `Type type`

        - `USER_MESSAGE("user.message")`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `String description`

        What the agent should produce. This is the task specification.

      - `Rubric rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `String fileId`

            ID of the rubric file.

          - `Type type`

            - `FILE("file")`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `String content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `Type type`

            - `TEXT("text")`

      - `Type type`

        - `USER_DEFINE_OUTCOME("user.define_outcome")`

      - `Optional<Long> maxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `List<BetaManagedAgentsSystemContentBlock> content`

        System content blocks to append. Text-only.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `Type type`

        - `SYSTEM_MESSAGE("system.message")`

  - `Metadata metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `String name`

    Human-readable name.

  - `Optional<BetaManagedAgentsDeploymentPausedReason> pausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `Type type`

        - `MANUAL("manual")`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `BetaManagedAgentsDeploymentPausedReasonError error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `Type type`

            - `ENVIRONMENT_ARCHIVED_ERROR("environment_archived_error")`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `Type type`

            - `AGENT_ARCHIVED_ERROR("agent_archived_error")`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `Type type`

            - `ENVIRONMENT_NOT_FOUND_ERROR("environment_not_found_error")`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `Type type`

            - `VAULT_NOT_FOUND_ERROR("vault_not_found_error")`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `Type type`

            - `FILE_NOT_FOUND_ERROR("file_not_found_error")`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `Type type`

            - `SESSION_RESOURCE_NOT_FOUND_ERROR("session_resource_not_found_error")`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `Type type`

            - `WORKSPACE_ARCHIVED_ERROR("workspace_archived_error")`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `Type type`

            - `ORGANIZATION_DISABLED_ERROR("organization_disabled_error")`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `Type type`

            - `MEMORY_STORE_ARCHIVED_ERROR("memory_store_archived_error")`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `Type type`

            - `SKILL_NOT_FOUND_ERROR("skill_not_found_error")`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `Type type`

            - `VAULT_ARCHIVED_ERROR("vault_archived_error")`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `Type type`

            - `UNKNOWN_ERROR("unknown_error")`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `Type type`

            - `SELF_HOSTED_RESOURCES_UNSUPPORTED_ERROR("self_hosted_resources_unsupported_error")`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `Type type`

            - `MCP_EGRESS_BLOCKED_ERROR("mcp_egress_blocked_error")`

      - `Type type`

        - `ERROR("error")`

  - `List<BetaManagedAgentsSessionResourceConfig> resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `Type type`

        - `GITHUB_REPOSITORY("github_repository")`

      - `String url`

        Github URL of the repository

      - `Optional<Checkout> checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `String name`

            Branch name to check out.

          - `Type type`

            - `BRANCH("branch")`

        - `class BetaManagedAgentsCommitCheckout:`

          - `String sha`

            Full commit SHA to check out.

          - `Type type`

            - `COMMIT("commit")`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `String fileId`

        ID of a previously uploaded file.

      - `Type type`

        - `FILE("file")`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `String memoryStoreId`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type type`

        - `MEMORY_STORE("memory_store")`

      - `Optional<Access> access`

        Access mode for an attached memory store.

        - `READ_WRITE("read_write")`

        - `READ_ONLY("read_only")`

      - `Optional<String> instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `Optional<BetaManagedAgentsSchedule> schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `String expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `String timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `Type type`

      - `CRON("cron")`

    - `Optional<LocalDateTime> lastRunAt`

      A timestamp in RFC 3339 format

    - `Optional<List<LocalDateTime>> upcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `BetaManagedAgentsDeploymentStatus status`

    Lifecycle status of a deployment.

    - `ACTIVE("active")`

    - `PAUSED("paused")`

  - `Type type`

    - `DEPLOYMENT("deployment")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `List<String> vaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.deployments.BetaManagedAgentsDeployment;
import com.anthropic.models.beta.deployments.DeploymentRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsDeployment betaManagedAgentsDeployment = client.beta().deployments().retrieve("depl_011CZkZcDH3vPqd7xnEfwTai");
    }
}
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

## Update Deployment

`BetaManagedAgentsDeployment beta().deployments().update(DeploymentUpdateParamsparams = DeploymentUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/deployments/{deployment_id}`

Update Deployment

### Parameters

- `DeploymentUpdateParams params`

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

  - `Optional<Agent> agent`

    Agent to deploy. Accepts the `agent` ID string, which re-pins to the latest version, or an `agent` object with both id and version specified. Omit to preserve. Cannot be cleared.

    - `String`

    - `class BetaManagedAgentsAgentParams:`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `String id`

        The `agent` ID.

      - `Type type`

        - `AGENT("agent")`

      - `Optional<Long> version`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

  - `Optional<String> description`

    Description. Omit to preserve; send empty string or null to clear.

  - `Optional<String> environmentId`

    ID of the `environment` where sessions run. Omit to preserve. Cannot be cleared.

  - `Optional<List<BetaManagedAgentsDeploymentInitialEventParams>> initialEvents`

    Initial events. Full replacement. Omit to preserve. Cannot be cleared. At least 1, maximum 50.

    - `class BetaManagedAgentsUserMessageEventParams:`

      Parameters for sending a user message to the session.

      - `List<Content> content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

          - `Type type`

            - `TEXT("text")`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `IMAGE("image")`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

                - `TEXT_PLAIN("text/plain")`

              - `Type type`

                - `TEXT("text")`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `DOCUMENT("document")`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

      - `Type type`

        - `USER_MESSAGE("user.message")`

    - `class BetaManagedAgentsUserDefineOutcomeEventParams:`

      Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

      - `String description`

        What the agent should produce. This is the task specification.

      - `Rubric rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubricParams:`

          Rubric referenced by a file uploaded via the Files API.

          - `String fileId`

            ID of the rubric file.

          - `Type type`

            - `FILE("file")`

        - `class BetaManagedAgentsTextRubricParams:`

          Rubric content provided inline as text.

          - `String content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

          - `Type type`

            - `TEXT("text")`

      - `Type type`

        - `USER_DEFINE_OUTCOME("user.define_outcome")`

      - `Optional<Long> maxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsSystemMessageEventParams:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

      - `List<BetaManagedAgentsSystemContentBlock> content`

        System content blocks to append. Text-only.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `Type type`

        - `SYSTEM_MESSAGE("system.message")`

  - `Optional<Metadata> metadata`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `Optional<String> name`

    Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

  - `Optional<List<Resource>> resources`

    Session resources. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 500.

    - `class BetaManagedAgentsGitHubRepositoryResourceParams:`

      Mount a GitHub repository into the session's container.

      - `String authorizationToken`

        GitHub authorization token used to clone the repository.

      - `Type type`

        - `GITHUB_REPOSITORY("github_repository")`

      - `String url`

        Github URL of the repository

      - `Optional<Checkout> checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `String name`

            Branch name to check out.

          - `Type type`

            - `BRANCH("branch")`

        - `class BetaManagedAgentsCommitCheckout:`

          - `String sha`

            Full commit SHA to check out.

          - `Type type`

            - `COMMIT("commit")`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceParams:`

      Mount a file uploaded via the Files API into the session.

      - `String fileId`

        ID of a previously uploaded file.

      - `Type type`

        - `FILE("file")`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceParam:`

      Parameters for attaching a memory store to an agent session.

      - `String memoryStoreId`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type type`

        - `MEMORY_STORE("memory_store")`

      - `Optional<Access> access`

        Access mode for an attached memory store.

        - `READ_WRITE("read_write")`

        - `READ_ONLY("read_only")`

      - `Optional<String> instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `Optional<BetaManagedAgentsScheduleParams> schedule`

    5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `Optional<List<String>> vaultIds`

    Vault IDs. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 50.

### Returns

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `String id`

    Unique identifier for this deployment.

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

    - `String id`

    - `Type type`

      - `AGENT("agent")`

    - `long version`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> description`

    Description of what the deployment does.

  - `String environmentId`

    ID of the `environment` where sessions run.

  - `List<BetaManagedAgentsDeploymentInitialEvent> initialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `List<Content> content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

          - `Type type`

            - `TEXT("text")`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `IMAGE("image")`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

                - `TEXT_PLAIN("text/plain")`

              - `Type type`

                - `TEXT("text")`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `DOCUMENT("document")`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

      - `Type type`

        - `USER_MESSAGE("user.message")`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `String description`

        What the agent should produce. This is the task specification.

      - `Rubric rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `String fileId`

            ID of the rubric file.

          - `Type type`

            - `FILE("file")`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `String content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `Type type`

            - `TEXT("text")`

      - `Type type`

        - `USER_DEFINE_OUTCOME("user.define_outcome")`

      - `Optional<Long> maxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `List<BetaManagedAgentsSystemContentBlock> content`

        System content blocks to append. Text-only.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `Type type`

        - `SYSTEM_MESSAGE("system.message")`

  - `Metadata metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `String name`

    Human-readable name.

  - `Optional<BetaManagedAgentsDeploymentPausedReason> pausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `Type type`

        - `MANUAL("manual")`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `BetaManagedAgentsDeploymentPausedReasonError error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `Type type`

            - `ENVIRONMENT_ARCHIVED_ERROR("environment_archived_error")`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `Type type`

            - `AGENT_ARCHIVED_ERROR("agent_archived_error")`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `Type type`

            - `ENVIRONMENT_NOT_FOUND_ERROR("environment_not_found_error")`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `Type type`

            - `VAULT_NOT_FOUND_ERROR("vault_not_found_error")`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `Type type`

            - `FILE_NOT_FOUND_ERROR("file_not_found_error")`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `Type type`

            - `SESSION_RESOURCE_NOT_FOUND_ERROR("session_resource_not_found_error")`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `Type type`

            - `WORKSPACE_ARCHIVED_ERROR("workspace_archived_error")`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `Type type`

            - `ORGANIZATION_DISABLED_ERROR("organization_disabled_error")`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `Type type`

            - `MEMORY_STORE_ARCHIVED_ERROR("memory_store_archived_error")`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `Type type`

            - `SKILL_NOT_FOUND_ERROR("skill_not_found_error")`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `Type type`

            - `VAULT_ARCHIVED_ERROR("vault_archived_error")`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `Type type`

            - `UNKNOWN_ERROR("unknown_error")`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `Type type`

            - `SELF_HOSTED_RESOURCES_UNSUPPORTED_ERROR("self_hosted_resources_unsupported_error")`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `Type type`

            - `MCP_EGRESS_BLOCKED_ERROR("mcp_egress_blocked_error")`

      - `Type type`

        - `ERROR("error")`

  - `List<BetaManagedAgentsSessionResourceConfig> resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `Type type`

        - `GITHUB_REPOSITORY("github_repository")`

      - `String url`

        Github URL of the repository

      - `Optional<Checkout> checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `String name`

            Branch name to check out.

          - `Type type`

            - `BRANCH("branch")`

        - `class BetaManagedAgentsCommitCheckout:`

          - `String sha`

            Full commit SHA to check out.

          - `Type type`

            - `COMMIT("commit")`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `String fileId`

        ID of a previously uploaded file.

      - `Type type`

        - `FILE("file")`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `String memoryStoreId`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type type`

        - `MEMORY_STORE("memory_store")`

      - `Optional<Access> access`

        Access mode for an attached memory store.

        - `READ_WRITE("read_write")`

        - `READ_ONLY("read_only")`

      - `Optional<String> instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `Optional<BetaManagedAgentsSchedule> schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `String expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `String timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `Type type`

      - `CRON("cron")`

    - `Optional<LocalDateTime> lastRunAt`

      A timestamp in RFC 3339 format

    - `Optional<List<LocalDateTime>> upcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `BetaManagedAgentsDeploymentStatus status`

    Lifecycle status of a deployment.

    - `ACTIVE("active")`

    - `PAUSED("paused")`

  - `Type type`

    - `DEPLOYMENT("deployment")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `List<String> vaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.deployments.BetaManagedAgentsDeployment;
import com.anthropic.models.beta.deployments.DeploymentUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsDeployment betaManagedAgentsDeployment = client.beta().deployments().update("depl_011CZkZcDH3vPqd7xnEfwTai");
    }
}
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

## Archive Deployment

`BetaManagedAgentsDeployment beta().deployments().archive(DeploymentArchiveParamsparams = DeploymentArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/deployments/{deployment_id}/archive`

Archive Deployment

### Parameters

- `DeploymentArchiveParams params`

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

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `String id`

    Unique identifier for this deployment.

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

    - `String id`

    - `Type type`

      - `AGENT("agent")`

    - `long version`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> description`

    Description of what the deployment does.

  - `String environmentId`

    ID of the `environment` where sessions run.

  - `List<BetaManagedAgentsDeploymentInitialEvent> initialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `List<Content> content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

          - `Type type`

            - `TEXT("text")`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `IMAGE("image")`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

                - `TEXT_PLAIN("text/plain")`

              - `Type type`

                - `TEXT("text")`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `DOCUMENT("document")`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

      - `Type type`

        - `USER_MESSAGE("user.message")`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `String description`

        What the agent should produce. This is the task specification.

      - `Rubric rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `String fileId`

            ID of the rubric file.

          - `Type type`

            - `FILE("file")`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `String content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `Type type`

            - `TEXT("text")`

      - `Type type`

        - `USER_DEFINE_OUTCOME("user.define_outcome")`

      - `Optional<Long> maxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `List<BetaManagedAgentsSystemContentBlock> content`

        System content blocks to append. Text-only.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `Type type`

        - `SYSTEM_MESSAGE("system.message")`

  - `Metadata metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `String name`

    Human-readable name.

  - `Optional<BetaManagedAgentsDeploymentPausedReason> pausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `Type type`

        - `MANUAL("manual")`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `BetaManagedAgentsDeploymentPausedReasonError error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `Type type`

            - `ENVIRONMENT_ARCHIVED_ERROR("environment_archived_error")`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `Type type`

            - `AGENT_ARCHIVED_ERROR("agent_archived_error")`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `Type type`

            - `ENVIRONMENT_NOT_FOUND_ERROR("environment_not_found_error")`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `Type type`

            - `VAULT_NOT_FOUND_ERROR("vault_not_found_error")`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `Type type`

            - `FILE_NOT_FOUND_ERROR("file_not_found_error")`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `Type type`

            - `SESSION_RESOURCE_NOT_FOUND_ERROR("session_resource_not_found_error")`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `Type type`

            - `WORKSPACE_ARCHIVED_ERROR("workspace_archived_error")`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `Type type`

            - `ORGANIZATION_DISABLED_ERROR("organization_disabled_error")`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `Type type`

            - `MEMORY_STORE_ARCHIVED_ERROR("memory_store_archived_error")`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `Type type`

            - `SKILL_NOT_FOUND_ERROR("skill_not_found_error")`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `Type type`

            - `VAULT_ARCHIVED_ERROR("vault_archived_error")`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `Type type`

            - `UNKNOWN_ERROR("unknown_error")`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `Type type`

            - `SELF_HOSTED_RESOURCES_UNSUPPORTED_ERROR("self_hosted_resources_unsupported_error")`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `Type type`

            - `MCP_EGRESS_BLOCKED_ERROR("mcp_egress_blocked_error")`

      - `Type type`

        - `ERROR("error")`

  - `List<BetaManagedAgentsSessionResourceConfig> resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `Type type`

        - `GITHUB_REPOSITORY("github_repository")`

      - `String url`

        Github URL of the repository

      - `Optional<Checkout> checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `String name`

            Branch name to check out.

          - `Type type`

            - `BRANCH("branch")`

        - `class BetaManagedAgentsCommitCheckout:`

          - `String sha`

            Full commit SHA to check out.

          - `Type type`

            - `COMMIT("commit")`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `String fileId`

        ID of a previously uploaded file.

      - `Type type`

        - `FILE("file")`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `String memoryStoreId`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type type`

        - `MEMORY_STORE("memory_store")`

      - `Optional<Access> access`

        Access mode for an attached memory store.

        - `READ_WRITE("read_write")`

        - `READ_ONLY("read_only")`

      - `Optional<String> instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `Optional<BetaManagedAgentsSchedule> schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `String expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `String timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `Type type`

      - `CRON("cron")`

    - `Optional<LocalDateTime> lastRunAt`

      A timestamp in RFC 3339 format

    - `Optional<List<LocalDateTime>> upcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `BetaManagedAgentsDeploymentStatus status`

    Lifecycle status of a deployment.

    - `ACTIVE("active")`

    - `PAUSED("paused")`

  - `Type type`

    - `DEPLOYMENT("deployment")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `List<String> vaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.deployments.BetaManagedAgentsDeployment;
import com.anthropic.models.beta.deployments.DeploymentArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsDeployment betaManagedAgentsDeployment = client.beta().deployments().archive("depl_011CZkZcDH3vPqd7xnEfwTai");
    }
}
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

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

        BetaManagedAgentsDeploymentRun betaManagedAgentsDeploymentRun = client.beta().deployments().run("depl_011CZkZcDH3vPqd7xnEfwTai");
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

## Pause Deployment

`BetaManagedAgentsDeployment beta().deployments().pause(DeploymentPauseParamsparams = DeploymentPauseParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/deployments/{deployment_id}/pause`

Pause Deployment

### Parameters

- `DeploymentPauseParams params`

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

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `String id`

    Unique identifier for this deployment.

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

    - `String id`

    - `Type type`

      - `AGENT("agent")`

    - `long version`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> description`

    Description of what the deployment does.

  - `String environmentId`

    ID of the `environment` where sessions run.

  - `List<BetaManagedAgentsDeploymentInitialEvent> initialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `List<Content> content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

          - `Type type`

            - `TEXT("text")`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `IMAGE("image")`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

                - `TEXT_PLAIN("text/plain")`

              - `Type type`

                - `TEXT("text")`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `DOCUMENT("document")`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

      - `Type type`

        - `USER_MESSAGE("user.message")`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `String description`

        What the agent should produce. This is the task specification.

      - `Rubric rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `String fileId`

            ID of the rubric file.

          - `Type type`

            - `FILE("file")`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `String content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `Type type`

            - `TEXT("text")`

      - `Type type`

        - `USER_DEFINE_OUTCOME("user.define_outcome")`

      - `Optional<Long> maxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `List<BetaManagedAgentsSystemContentBlock> content`

        System content blocks to append. Text-only.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `Type type`

        - `SYSTEM_MESSAGE("system.message")`

  - `Metadata metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `String name`

    Human-readable name.

  - `Optional<BetaManagedAgentsDeploymentPausedReason> pausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `Type type`

        - `MANUAL("manual")`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `BetaManagedAgentsDeploymentPausedReasonError error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `Type type`

            - `ENVIRONMENT_ARCHIVED_ERROR("environment_archived_error")`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `Type type`

            - `AGENT_ARCHIVED_ERROR("agent_archived_error")`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `Type type`

            - `ENVIRONMENT_NOT_FOUND_ERROR("environment_not_found_error")`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `Type type`

            - `VAULT_NOT_FOUND_ERROR("vault_not_found_error")`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `Type type`

            - `FILE_NOT_FOUND_ERROR("file_not_found_error")`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `Type type`

            - `SESSION_RESOURCE_NOT_FOUND_ERROR("session_resource_not_found_error")`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `Type type`

            - `WORKSPACE_ARCHIVED_ERROR("workspace_archived_error")`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `Type type`

            - `ORGANIZATION_DISABLED_ERROR("organization_disabled_error")`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `Type type`

            - `MEMORY_STORE_ARCHIVED_ERROR("memory_store_archived_error")`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `Type type`

            - `SKILL_NOT_FOUND_ERROR("skill_not_found_error")`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `Type type`

            - `VAULT_ARCHIVED_ERROR("vault_archived_error")`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `Type type`

            - `UNKNOWN_ERROR("unknown_error")`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `Type type`

            - `SELF_HOSTED_RESOURCES_UNSUPPORTED_ERROR("self_hosted_resources_unsupported_error")`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `Type type`

            - `MCP_EGRESS_BLOCKED_ERROR("mcp_egress_blocked_error")`

      - `Type type`

        - `ERROR("error")`

  - `List<BetaManagedAgentsSessionResourceConfig> resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `Type type`

        - `GITHUB_REPOSITORY("github_repository")`

      - `String url`

        Github URL of the repository

      - `Optional<Checkout> checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `String name`

            Branch name to check out.

          - `Type type`

            - `BRANCH("branch")`

        - `class BetaManagedAgentsCommitCheckout:`

          - `String sha`

            Full commit SHA to check out.

          - `Type type`

            - `COMMIT("commit")`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `String fileId`

        ID of a previously uploaded file.

      - `Type type`

        - `FILE("file")`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `String memoryStoreId`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type type`

        - `MEMORY_STORE("memory_store")`

      - `Optional<Access> access`

        Access mode for an attached memory store.

        - `READ_WRITE("read_write")`

        - `READ_ONLY("read_only")`

      - `Optional<String> instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `Optional<BetaManagedAgentsSchedule> schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `String expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `String timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `Type type`

      - `CRON("cron")`

    - `Optional<LocalDateTime> lastRunAt`

      A timestamp in RFC 3339 format

    - `Optional<List<LocalDateTime>> upcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `BetaManagedAgentsDeploymentStatus status`

    Lifecycle status of a deployment.

    - `ACTIVE("active")`

    - `PAUSED("paused")`

  - `Type type`

    - `DEPLOYMENT("deployment")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `List<String> vaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.deployments.BetaManagedAgentsDeployment;
import com.anthropic.models.beta.deployments.DeploymentPauseParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsDeployment betaManagedAgentsDeployment = client.beta().deployments().pause("depl_011CZkZcDH3vPqd7xnEfwTai");
    }
}
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

## Unpause Deployment

`BetaManagedAgentsDeployment beta().deployments().unpause(DeploymentUnpauseParamsparams = DeploymentUnpauseParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/deployments/{deployment_id}/unpause`

Unpause Deployment

### Parameters

- `DeploymentUnpauseParams params`

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

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `String id`

    Unique identifier for this deployment.

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

    - `String id`

    - `Type type`

      - `AGENT("agent")`

    - `long version`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> description`

    Description of what the deployment does.

  - `String environmentId`

    ID of the `environment` where sessions run.

  - `List<BetaManagedAgentsDeploymentInitialEvent> initialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `List<Content> content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

          - `Type type`

            - `TEXT("text")`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `IMAGE("image")`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

                - `TEXT_PLAIN("text/plain")`

              - `Type type`

                - `TEXT("text")`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `DOCUMENT("document")`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

      - `Type type`

        - `USER_MESSAGE("user.message")`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `String description`

        What the agent should produce. This is the task specification.

      - `Rubric rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `String fileId`

            ID of the rubric file.

          - `Type type`

            - `FILE("file")`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `String content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `Type type`

            - `TEXT("text")`

      - `Type type`

        - `USER_DEFINE_OUTCOME("user.define_outcome")`

      - `Optional<Long> maxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `List<BetaManagedAgentsSystemContentBlock> content`

        System content blocks to append. Text-only.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `Type type`

        - `SYSTEM_MESSAGE("system.message")`

  - `Metadata metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `String name`

    Human-readable name.

  - `Optional<BetaManagedAgentsDeploymentPausedReason> pausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `Type type`

        - `MANUAL("manual")`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `BetaManagedAgentsDeploymentPausedReasonError error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `Type type`

            - `ENVIRONMENT_ARCHIVED_ERROR("environment_archived_error")`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `Type type`

            - `AGENT_ARCHIVED_ERROR("agent_archived_error")`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `Type type`

            - `ENVIRONMENT_NOT_FOUND_ERROR("environment_not_found_error")`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `Type type`

            - `VAULT_NOT_FOUND_ERROR("vault_not_found_error")`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `Type type`

            - `FILE_NOT_FOUND_ERROR("file_not_found_error")`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `Type type`

            - `SESSION_RESOURCE_NOT_FOUND_ERROR("session_resource_not_found_error")`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `Type type`

            - `WORKSPACE_ARCHIVED_ERROR("workspace_archived_error")`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `Type type`

            - `ORGANIZATION_DISABLED_ERROR("organization_disabled_error")`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `Type type`

            - `MEMORY_STORE_ARCHIVED_ERROR("memory_store_archived_error")`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `Type type`

            - `SKILL_NOT_FOUND_ERROR("skill_not_found_error")`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `Type type`

            - `VAULT_ARCHIVED_ERROR("vault_archived_error")`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `Type type`

            - `UNKNOWN_ERROR("unknown_error")`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `Type type`

            - `SELF_HOSTED_RESOURCES_UNSUPPORTED_ERROR("self_hosted_resources_unsupported_error")`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `Type type`

            - `MCP_EGRESS_BLOCKED_ERROR("mcp_egress_blocked_error")`

      - `Type type`

        - `ERROR("error")`

  - `List<BetaManagedAgentsSessionResourceConfig> resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `Type type`

        - `GITHUB_REPOSITORY("github_repository")`

      - `String url`

        Github URL of the repository

      - `Optional<Checkout> checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `String name`

            Branch name to check out.

          - `Type type`

            - `BRANCH("branch")`

        - `class BetaManagedAgentsCommitCheckout:`

          - `String sha`

            Full commit SHA to check out.

          - `Type type`

            - `COMMIT("commit")`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `String fileId`

        ID of a previously uploaded file.

      - `Type type`

        - `FILE("file")`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `String memoryStoreId`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type type`

        - `MEMORY_STORE("memory_store")`

      - `Optional<Access> access`

        Access mode for an attached memory store.

        - `READ_WRITE("read_write")`

        - `READ_ONLY("read_only")`

      - `Optional<String> instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `Optional<BetaManagedAgentsSchedule> schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `String expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `String timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `Type type`

      - `CRON("cron")`

    - `Optional<LocalDateTime> lastRunAt`

      A timestamp in RFC 3339 format

    - `Optional<List<LocalDateTime>> upcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `BetaManagedAgentsDeploymentStatus status`

    Lifecycle status of a deployment.

    - `ACTIVE("active")`

    - `PAUSED("paused")`

  - `Type type`

    - `DEPLOYMENT("deployment")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `List<String> vaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.deployments.BetaManagedAgentsDeployment;
import com.anthropic.models.beta.deployments.DeploymentUnpauseParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsDeployment betaManagedAgentsDeployment = client.beta().deployments().unpause("depl_011CZkZcDH3vPqd7xnEfwTai");
    }
}
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

## Domain Types

### Beta Managed Agents Agent Archived Deployment Paused Reason Error

- `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

  The deployment's agent was archived.

  - `Type type`

    - `AGENT_ARCHIVED_ERROR("agent_archived_error")`

### Beta Managed Agents Cron Schedule

- `class BetaManagedAgentsCronSchedule:`

  5-field POSIX cron schedule with computed runtime timestamps.

  - `String expression`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `String timezone`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

  - `Type type`

    - `CRON("cron")`

  - `Optional<LocalDateTime> lastRunAt`

    A timestamp in RFC 3339 format

  - `Optional<List<LocalDateTime>> upcomingRunsAt`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Cron Schedule Params

- `class BetaManagedAgentsCronScheduleParams:`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `String expression`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `String timezone`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `Type type`

    - `CRON("cron")`

### Beta Managed Agents Deployment

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `String id`

    Unique identifier for this deployment.

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

    - `String id`

    - `Type type`

      - `AGENT("agent")`

    - `long version`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> description`

    Description of what the deployment does.

  - `String environmentId`

    ID of the `environment` where sessions run.

  - `List<BetaManagedAgentsDeploymentInitialEvent> initialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `List<Content> content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

          - `Type type`

            - `TEXT("text")`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `IMAGE("image")`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

                - `TEXT_PLAIN("text/plain")`

              - `Type type`

                - `TEXT("text")`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `DOCUMENT("document")`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

      - `Type type`

        - `USER_MESSAGE("user.message")`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `String description`

        What the agent should produce. This is the task specification.

      - `Rubric rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `String fileId`

            ID of the rubric file.

          - `Type type`

            - `FILE("file")`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `String content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `Type type`

            - `TEXT("text")`

      - `Type type`

        - `USER_DEFINE_OUTCOME("user.define_outcome")`

      - `Optional<Long> maxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `List<BetaManagedAgentsSystemContentBlock> content`

        System content blocks to append. Text-only.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `Type type`

        - `SYSTEM_MESSAGE("system.message")`

  - `Metadata metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `String name`

    Human-readable name.

  - `Optional<BetaManagedAgentsDeploymentPausedReason> pausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `Type type`

        - `MANUAL("manual")`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `BetaManagedAgentsDeploymentPausedReasonError error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `Type type`

            - `ENVIRONMENT_ARCHIVED_ERROR("environment_archived_error")`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `Type type`

            - `AGENT_ARCHIVED_ERROR("agent_archived_error")`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `Type type`

            - `ENVIRONMENT_NOT_FOUND_ERROR("environment_not_found_error")`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `Type type`

            - `VAULT_NOT_FOUND_ERROR("vault_not_found_error")`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `Type type`

            - `FILE_NOT_FOUND_ERROR("file_not_found_error")`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `Type type`

            - `SESSION_RESOURCE_NOT_FOUND_ERROR("session_resource_not_found_error")`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `Type type`

            - `WORKSPACE_ARCHIVED_ERROR("workspace_archived_error")`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `Type type`

            - `ORGANIZATION_DISABLED_ERROR("organization_disabled_error")`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `Type type`

            - `MEMORY_STORE_ARCHIVED_ERROR("memory_store_archived_error")`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `Type type`

            - `SKILL_NOT_FOUND_ERROR("skill_not_found_error")`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `Type type`

            - `VAULT_ARCHIVED_ERROR("vault_archived_error")`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `Type type`

            - `UNKNOWN_ERROR("unknown_error")`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `Type type`

            - `SELF_HOSTED_RESOURCES_UNSUPPORTED_ERROR("self_hosted_resources_unsupported_error")`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `Type type`

            - `MCP_EGRESS_BLOCKED_ERROR("mcp_egress_blocked_error")`

      - `Type type`

        - `ERROR("error")`

  - `List<BetaManagedAgentsSessionResourceConfig> resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `Type type`

        - `GITHUB_REPOSITORY("github_repository")`

      - `String url`

        Github URL of the repository

      - `Optional<Checkout> checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `String name`

            Branch name to check out.

          - `Type type`

            - `BRANCH("branch")`

        - `class BetaManagedAgentsCommitCheckout:`

          - `String sha`

            Full commit SHA to check out.

          - `Type type`

            - `COMMIT("commit")`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `String fileId`

        ID of a previously uploaded file.

      - `Type type`

        - `FILE("file")`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `String memoryStoreId`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type type`

        - `MEMORY_STORE("memory_store")`

      - `Optional<Access> access`

        Access mode for an attached memory store.

        - `READ_WRITE("read_write")`

        - `READ_ONLY("read_only")`

      - `Optional<String> instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `Optional<BetaManagedAgentsSchedule> schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `String expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `String timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `Type type`

      - `CRON("cron")`

    - `Optional<LocalDateTime> lastRunAt`

      A timestamp in RFC 3339 format

    - `Optional<List<LocalDateTime>> upcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `BetaManagedAgentsDeploymentStatus status`

    Lifecycle status of a deployment.

    - `ACTIVE("active")`

    - `PAUSED("paused")`

  - `Type type`

    - `DEPLOYMENT("deployment")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `List<String> vaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Beta Managed Agents Deployment Initial Event

- `class BetaManagedAgentsDeploymentInitialEvent: A class that can be one of several variants.union`

  An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

  - `class BetaManagedAgentsDeploymentUserMessageEvent:`

    A user message sent to the session.

    - `List<Content> content`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Type type`

      - `USER_MESSAGE("user.message")`

  - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

    An outcome the agent should work toward. The agent begins work on receipt.

    - `String description`

      What the agent should produce. This is the task specification.

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric:`

        Rubric referenced by a file uploaded via the Files API.

        - `String fileId`

          ID of the rubric file.

        - `Type type`

          - `FILE("file")`

      - `class BetaManagedAgentsTextRubric:`

        Rubric content provided inline as text.

        - `String content`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `Type type`

          - `TEXT("text")`

    - `Type type`

      - `USER_DEFINE_OUTCOME("user.define_outcome")`

    - `Optional<Long> maxIterations`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

    - `List<BetaManagedAgentsSystemContentBlock> content`

      System content blocks to append. Text-only.

      - `String text`

        The text content.

      - `Type type`

        - `TEXT("text")`

    - `Type type`

      - `SYSTEM_MESSAGE("system.message")`

### Beta Managed Agents Deployment Initial Event Params

- `class BetaManagedAgentsDeploymentInitialEventParams: A class that can be one of several variants.union`

  An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

  - `class BetaManagedAgentsUserMessageEventParams:`

    Parameters for sending a user message to the session.

    - `List<Content> content`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Type type`

      - `USER_MESSAGE("user.message")`

  - `class BetaManagedAgentsUserDefineOutcomeEventParams:`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `String description`

      What the agent should produce. This is the task specification.

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubricParams:`

        Rubric referenced by a file uploaded via the Files API.

        - `String fileId`

          ID of the rubric file.

        - `Type type`

          - `FILE("file")`

      - `class BetaManagedAgentsTextRubricParams:`

        Rubric content provided inline as text.

        - `String content`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

        - `Type type`

          - `TEXT("text")`

    - `Type type`

      - `USER_DEFINE_OUTCOME("user.define_outcome")`

    - `Optional<Long> maxIterations`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `class BetaManagedAgentsSystemMessageEventParams:`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `List<BetaManagedAgentsSystemContentBlock> content`

      System content blocks to append. Text-only.

      - `String text`

        The text content.

      - `Type type`

        - `TEXT("text")`

    - `Type type`

      - `SYSTEM_MESSAGE("system.message")`

### Beta Managed Agents Deployment Paused Reason

- `class BetaManagedAgentsDeploymentPausedReason: A class that can be one of several variants.union`

  Why a deployment is paused. Non-null exactly when `status` is `paused`.

  - `class BetaManagedAgentsManualDeploymentPausedReason:`

    The caller invoked the pause endpoint on the deployment.

    - `Type type`

      - `MANUAL("manual")`

  - `class BetaManagedAgentsErrorDeploymentPausedReason:`

    A scheduled fire recorded a failed run whose error auto-pauses the deployment.

    - `BetaManagedAgentsDeploymentPausedReasonError error`

      The error that triggered an auto-pause. Matches the failed run's `error.type`.

      - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

        The deployment's environment was archived.

        - `Type type`

          - `ENVIRONMENT_ARCHIVED_ERROR("environment_archived_error")`

      - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

        The deployment's agent was archived.

        - `Type type`

          - `AGENT_ARCHIVED_ERROR("agent_archived_error")`

      - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

        The deployment's environment no longer exists.

        - `Type type`

          - `ENVIRONMENT_NOT_FOUND_ERROR("environment_not_found_error")`

      - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

        A vault referenced by the deployment no longer exists.

        - `Type type`

          - `VAULT_NOT_FOUND_ERROR("vault_not_found_error")`

      - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

        A file resource referenced by the deployment no longer exists.

        - `Type type`

          - `FILE_NOT_FOUND_ERROR("file_not_found_error")`

      - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

        A referenced resource no longer exists and its kind was not reported.

        - `Type type`

          - `SESSION_RESOURCE_NOT_FOUND_ERROR("session_resource_not_found_error")`

      - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

        The deployment's workspace was archived.

        - `Type type`

          - `WORKSPACE_ARCHIVED_ERROR("workspace_archived_error")`

      - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

        The deployment's organization is disabled.

        - `Type type`

          - `ORGANIZATION_DISABLED_ERROR("organization_disabled_error")`

      - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

        A memory store referenced by the deployment is archived.

        - `Type type`

          - `MEMORY_STORE_ARCHIVED_ERROR("memory_store_archived_error")`

      - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

        A skill referenced by the deployment's agent no longer exists.

        - `Type type`

          - `SKILL_NOT_FOUND_ERROR("skill_not_found_error")`

      - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

        A vault referenced by the deployment is archived.

        - `Type type`

          - `VAULT_ARCHIVED_ERROR("vault_archived_error")`

      - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

        An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

        - `Type type`

          - `UNKNOWN_ERROR("unknown_error")`

      - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

        The deployment configures resources, but its environment is self-hosted and cannot mount them.

        - `Type type`

          - `SELF_HOSTED_RESOURCES_UNSUPPORTED_ERROR("self_hosted_resources_unsupported_error")`

      - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

        An MCP server host used by the deployment's agent is blocked by the environment's network policy.

        - `Type type`

          - `MCP_EGRESS_BLOCKED_ERROR("mcp_egress_blocked_error")`

    - `Type type`

      - `ERROR("error")`

### Beta Managed Agents Deployment Paused Reason Error

- `class BetaManagedAgentsDeploymentPausedReasonError: A class that can be one of several variants.union`

  The error that triggered an auto-pause. Matches the failed run's `error.type`.

  - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

    The deployment's environment was archived.

    - `Type type`

      - `ENVIRONMENT_ARCHIVED_ERROR("environment_archived_error")`

  - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

    The deployment's agent was archived.

    - `Type type`

      - `AGENT_ARCHIVED_ERROR("agent_archived_error")`

  - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

    The deployment's environment no longer exists.

    - `Type type`

      - `ENVIRONMENT_NOT_FOUND_ERROR("environment_not_found_error")`

  - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

    A vault referenced by the deployment no longer exists.

    - `Type type`

      - `VAULT_NOT_FOUND_ERROR("vault_not_found_error")`

  - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

    A file resource referenced by the deployment no longer exists.

    - `Type type`

      - `FILE_NOT_FOUND_ERROR("file_not_found_error")`

  - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

    A referenced resource no longer exists and its kind was not reported.

    - `Type type`

      - `SESSION_RESOURCE_NOT_FOUND_ERROR("session_resource_not_found_error")`

  - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

    The deployment's workspace was archived.

    - `Type type`

      - `WORKSPACE_ARCHIVED_ERROR("workspace_archived_error")`

  - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

    The deployment's organization is disabled.

    - `Type type`

      - `ORGANIZATION_DISABLED_ERROR("organization_disabled_error")`

  - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

    A memory store referenced by the deployment is archived.

    - `Type type`

      - `MEMORY_STORE_ARCHIVED_ERROR("memory_store_archived_error")`

  - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

    A skill referenced by the deployment's agent no longer exists.

    - `Type type`

      - `SKILL_NOT_FOUND_ERROR("skill_not_found_error")`

  - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

    A vault referenced by the deployment is archived.

    - `Type type`

      - `VAULT_ARCHIVED_ERROR("vault_archived_error")`

  - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

    An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

    - `Type type`

      - `UNKNOWN_ERROR("unknown_error")`

  - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

    The deployment configures resources, but its environment is self-hosted and cannot mount them.

    - `Type type`

      - `SELF_HOSTED_RESOURCES_UNSUPPORTED_ERROR("self_hosted_resources_unsupported_error")`

  - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

    An MCP server host used by the deployment's agent is blocked by the environment's network policy.

    - `Type type`

      - `MCP_EGRESS_BLOCKED_ERROR("mcp_egress_blocked_error")`

### Beta Managed Agents Deployment Status

- `enum BetaManagedAgentsDeploymentStatus:`

  Lifecycle status of a deployment.

  - `ACTIVE("active")`

  - `PAUSED("paused")`

### Beta Managed Agents Deployment System Message Event

- `class BetaManagedAgentsDeploymentSystemMessageEvent:`

  Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

  - `List<BetaManagedAgentsSystemContentBlock> content`

    System content blocks to append. Text-only.

    - `String text`

      The text content.

    - `Type type`

      - `TEXT("text")`

  - `Type type`

    - `SYSTEM_MESSAGE("system.message")`

### Beta Managed Agents Deployment User Define Outcome Event

- `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

  An outcome the agent should work toward. The agent begins work on receipt.

  - `String description`

    What the agent should produce. This is the task specification.

  - `Rubric rubric`

    Rubric for grading the quality of an outcome.

    - `class BetaManagedAgentsFileRubric:`

      Rubric referenced by a file uploaded via the Files API.

      - `String fileId`

        ID of the rubric file.

      - `Type type`

        - `FILE("file")`

    - `class BetaManagedAgentsTextRubric:`

      Rubric content provided inline as text.

      - `String content`

        Rubric content. Plain text or markdown — the grader treats it as freeform text.

      - `Type type`

        - `TEXT("text")`

  - `Type type`

    - `USER_DEFINE_OUTCOME("user.define_outcome")`

  - `Optional<Long> maxIterations`

    Eval→revision cycles before giving up. Default 3, max 20.

### Beta Managed Agents Deployment User Message Event

- `class BetaManagedAgentsDeploymentUserMessageEvent:`

  A user message sent to the session.

  - `List<Content> content`

    Array of content blocks for the user message.

    - `class BetaManagedAgentsTextBlock:`

      Regular text content.

      - `String text`

        The text content.

      - `Type type`

        - `TEXT("text")`

    - `class BetaManagedAgentsImageBlock:`

      Image content specified directly as base64 data or as a reference via a URL.

      - `Source source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource:`

          Base64-encoded image data.

          - `String data`

            Base64-encoded image data.

          - `String mediaType`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `Type type`

            - `BASE64("base64")`

        - `class BetaManagedAgentsUrlImageSource:`

          Image referenced by URL.

          - `Type type`

            - `URL("url")`

          - `String url`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource:`

          Image referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

          - `Type type`

            - `FILE("file")`

      - `Type type`

        - `IMAGE("image")`

    - `class BetaManagedAgentsDocumentBlock:`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `Source source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource:`

          Base64-encoded document data.

          - `String data`

            Base64-encoded document data.

          - `String mediaType`

            MIME type of the document (e.g., "application/pdf").

          - `Type type`

            - `BASE64("base64")`

        - `class BetaManagedAgentsPlainTextDocumentSource:`

          Plain text document content.

          - `String data`

            The plain text content.

          - `MediaType mediaType`

            MIME type of the text content. Must be "text/plain".

            - `TEXT_PLAIN("text/plain")`

          - `Type type`

            - `TEXT("text")`

        - `class BetaManagedAgentsUrlDocumentSource:`

          Document referenced by URL.

          - `Type type`

            - `URL("url")`

          - `String url`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource:`

          Document referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

          - `Type type`

            - `FILE("file")`

      - `Type type`

        - `DOCUMENT("document")`

      - `Optional<String> context`

        Additional context about the document for the model.

      - `Optional<String> title`

        The title of the document.

  - `Type type`

    - `USER_MESSAGE("user.message")`

### Beta Managed Agents Environment Archived Deployment Paused Reason Error

- `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

  The deployment's environment was archived.

  - `Type type`

    - `ENVIRONMENT_ARCHIVED_ERROR("environment_archived_error")`

### Beta Managed Agents Environment Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

  The deployment's environment no longer exists.

  - `Type type`

    - `ENVIRONMENT_NOT_FOUND_ERROR("environment_not_found_error")`

### Beta Managed Agents Error Deployment Paused Reason

- `class BetaManagedAgentsErrorDeploymentPausedReason:`

  A scheduled fire recorded a failed run whose error auto-pauses the deployment.

  - `BetaManagedAgentsDeploymentPausedReasonError error`

    The error that triggered an auto-pause. Matches the failed run's `error.type`.

    - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

      The deployment's environment was archived.

      - `Type type`

        - `ENVIRONMENT_ARCHIVED_ERROR("environment_archived_error")`

    - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

      The deployment's agent was archived.

      - `Type type`

        - `AGENT_ARCHIVED_ERROR("agent_archived_error")`

    - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

      The deployment's environment no longer exists.

      - `Type type`

        - `ENVIRONMENT_NOT_FOUND_ERROR("environment_not_found_error")`

    - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

      A vault referenced by the deployment no longer exists.

      - `Type type`

        - `VAULT_NOT_FOUND_ERROR("vault_not_found_error")`

    - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

      A file resource referenced by the deployment no longer exists.

      - `Type type`

        - `FILE_NOT_FOUND_ERROR("file_not_found_error")`

    - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

      A referenced resource no longer exists and its kind was not reported.

      - `Type type`

        - `SESSION_RESOURCE_NOT_FOUND_ERROR("session_resource_not_found_error")`

    - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

      The deployment's workspace was archived.

      - `Type type`

        - `WORKSPACE_ARCHIVED_ERROR("workspace_archived_error")`

    - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

      The deployment's organization is disabled.

      - `Type type`

        - `ORGANIZATION_DISABLED_ERROR("organization_disabled_error")`

    - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

      A memory store referenced by the deployment is archived.

      - `Type type`

        - `MEMORY_STORE_ARCHIVED_ERROR("memory_store_archived_error")`

    - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

      A skill referenced by the deployment's agent no longer exists.

      - `Type type`

        - `SKILL_NOT_FOUND_ERROR("skill_not_found_error")`

    - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

      A vault referenced by the deployment is archived.

      - `Type type`

        - `VAULT_ARCHIVED_ERROR("vault_archived_error")`

    - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

      An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

      - `Type type`

        - `UNKNOWN_ERROR("unknown_error")`

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `Type type`

        - `SELF_HOSTED_RESOURCES_UNSUPPORTED_ERROR("self_hosted_resources_unsupported_error")`

    - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `Type type`

        - `MCP_EGRESS_BLOCKED_ERROR("mcp_egress_blocked_error")`

  - `Type type`

    - `ERROR("error")`

### Beta Managed Agents File Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

  A file resource referenced by the deployment no longer exists.

  - `Type type`

    - `FILE_NOT_FOUND_ERROR("file_not_found_error")`

### Beta Managed Agents File Resource Config

- `class BetaManagedAgentsFileResourceConfig:`

  A file mounted into each session's container.

  - `String fileId`

    ID of a previously uploaded file.

  - `Type type`

    - `FILE("file")`

  - `Optional<String> mountPath`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

### Beta Managed Agents GitHub Repository Resource Config

- `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

  A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

  - `Type type`

    - `GITHUB_REPOSITORY("github_repository")`

  - `String url`

    Github URL of the repository

  - `Optional<Checkout> checkout`

    Branch or commit to check out. Defaults to the repository's default branch.

    - `class BetaManagedAgentsBranchCheckout:`

      - `String name`

        Branch name to check out.

      - `Type type`

        - `BRANCH("branch")`

    - `class BetaManagedAgentsCommitCheckout:`

      - `String sha`

        Full commit SHA to check out.

      - `Type type`

        - `COMMIT("commit")`

  - `Optional<String> mountPath`

    Mount path in the container. Defaults to `/workspace/<repo-name>`.

### Beta Managed Agents Manual Deployment Paused Reason

- `class BetaManagedAgentsManualDeploymentPausedReason:`

  The caller invoked the pause endpoint on the deployment.

  - `Type type`

    - `MANUAL("manual")`

### Beta Managed Agents MCP Egress Blocked Deployment Paused Reason Error

- `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

  An MCP server host used by the deployment's agent is blocked by the environment's network policy.

  - `Type type`

    - `MCP_EGRESS_BLOCKED_ERROR("mcp_egress_blocked_error")`

### Beta Managed Agents Memory Store Archived Deployment Paused Reason Error

- `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

  A memory store referenced by the deployment is archived.

  - `Type type`

    - `MEMORY_STORE_ARCHIVED_ERROR("memory_store_archived_error")`

### Beta Managed Agents Memory Store Resource Config

- `class BetaManagedAgentsMemoryStoreResourceConfig:`

  A memory store attached to each session created from this deployment.

  - `String memoryStoreId`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `Type type`

    - `MEMORY_STORE("memory_store")`

  - `Optional<Access> access`

    Access mode for an attached memory store.

    - `READ_WRITE("read_write")`

    - `READ_ONLY("read_only")`

  - `Optional<String> instructions`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Organization Disabled Deployment Paused Reason Error

- `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

  The deployment's organization is disabled.

  - `Type type`

    - `ORGANIZATION_DISABLED_ERROR("organization_disabled_error")`

### Beta Managed Agents Schedule

- `class BetaManagedAgentsSchedule:`

  5-field POSIX cron schedule with computed runtime timestamps.

  - `String expression`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `String timezone`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

  - `Type type`

    - `CRON("cron")`

  - `Optional<LocalDateTime> lastRunAt`

    A timestamp in RFC 3339 format

  - `Optional<List<LocalDateTime>> upcomingRunsAt`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Schedule Params

- `class BetaManagedAgentsScheduleParams:`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `String expression`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `String timezone`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `Type type`

    - `CRON("cron")`

### Beta Managed Agents Self Hosted Resources Unsupported Deployment Paused Reason Error

- `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

  The deployment configures resources, but its environment is self-hosted and cannot mount them.

  - `Type type`

    - `SELF_HOSTED_RESOURCES_UNSUPPORTED_ERROR("self_hosted_resources_unsupported_error")`

### Beta Managed Agents Session Resource Config

- `class BetaManagedAgentsSessionResourceConfig: A class that can be one of several variants.union`

  A configured session resource. Echoes the input minus write-only credentials.

  - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

    A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

    - `Type type`

      - `GITHUB_REPOSITORY("github_repository")`

    - `String url`

      Github URL of the repository

    - `Optional<Checkout> checkout`

      Branch or commit to check out. Defaults to the repository's default branch.

      - `class BetaManagedAgentsBranchCheckout:`

        - `String name`

          Branch name to check out.

        - `Type type`

          - `BRANCH("branch")`

      - `class BetaManagedAgentsCommitCheckout:`

        - `String sha`

          Full commit SHA to check out.

        - `Type type`

          - `COMMIT("commit")`

    - `Optional<String> mountPath`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

  - `class BetaManagedAgentsFileResourceConfig:`

    A file mounted into each session's container.

    - `String fileId`

      ID of a previously uploaded file.

    - `Type type`

      - `FILE("file")`

    - `Optional<String> mountPath`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  - `class BetaManagedAgentsMemoryStoreResourceConfig:`

    A memory store attached to each session created from this deployment.

    - `String memoryStoreId`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `Type type`

      - `MEMORY_STORE("memory_store")`

    - `Optional<Access> access`

      Access mode for an attached memory store.

      - `READ_WRITE("read_write")`

      - `READ_ONLY("read_only")`

    - `Optional<String> instructions`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Session Resource Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

  A referenced resource no longer exists and its kind was not reported.

  - `Type type`

    - `SESSION_RESOURCE_NOT_FOUND_ERROR("session_resource_not_found_error")`

### Beta Managed Agents Skill Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

  A skill referenced by the deployment's agent no longer exists.

  - `Type type`

    - `SKILL_NOT_FOUND_ERROR("skill_not_found_error")`

### Beta Managed Agents Unknown Deployment Paused Reason Error

- `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

  An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

  - `Type type`

    - `UNKNOWN_ERROR("unknown_error")`

### Beta Managed Agents Vault Archived Deployment Paused Reason Error

- `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

  A vault referenced by the deployment is archived.

  - `Type type`

    - `VAULT_ARCHIVED_ERROR("vault_archived_error")`

### Beta Managed Agents Vault Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

  A vault referenced by the deployment no longer exists.

  - `Type type`

    - `VAULT_NOT_FOUND_ERROR("vault_not_found_error")`

### Beta Managed Agents Workspace Archived Deployment Paused Reason Error

- `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

  The deployment's workspace was archived.

  - `Type type`

    - `WORKSPACE_ARCHIVED_ERROR("workspace_archived_error")`
