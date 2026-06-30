# Deployments

## Create Deployment

`BetaManagedAgentsDeployment Beta.Deployments.Create(DeploymentCreateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/deployments`

Create Deployment

### Parameters

- `DeploymentCreateParams parameters`

  - `required Agent agent`

    Body param: Agent to deploy. Accepts the `agent` ID string, which pins the latest version, or an `agent` object with both id and version specified. The agent must exist and not be archived.

    - `string`

    - `class BetaManagedAgentsAgentParams:`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `required string ID`

        The `agent` ID.

      - `required Type Type`

        - `"agent"Agent`

      - `Int Version`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

  - `required string environmentID`

    Body param: ID of the `environment` defining the container configuration for sessions created from this deployment.

  - `required IReadOnlyList<BetaManagedAgentsDeploymentInitialEventParams> initialEvents`

    Body param: Events to send to each session immediately after creation. At least 1, maximum 50.

    - `class BetaManagedAgentsUserMessageEventParams:`

      Parameters for sending a user message to the session.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

      - `required Type Type`

        - `"user.message"UserMessage`

    - `class BetaManagedAgentsUserDefineOutcomeEventParams:`

      Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

      - `required string Description`

        What the agent should produce. This is the task specification.

      - `required Rubric Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubricParams:`

          Rubric referenced by a file uploaded via the Files API.

          - `required string FileID`

            ID of the rubric file.

          - `required Type Type`

            - `"file"File`

        - `class BetaManagedAgentsTextRubricParams:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

          - `required Type Type`

            - `"text"Text`

      - `required Type Type`

        - `"user.define_outcome"UserDefineOutcome`

      - `Int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsSystemMessageEventParams:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `required Type Type`

        - `"system.message"SystemMessage`

  - `required string name`

    Body param: Human-readable name for the deployment.

  - `string? description`

    Body param: Description of what the deployment does.

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `IReadOnlyList<Resource> resources`

    Body param: Resources (e.g. repositories, files) to mount into each session's container. Maximum 500.

    - `class BetaManagedAgentsGitHubRepositoryResourceParams:`

      Mount a GitHub repository into the session's container.

      - `required string AuthorizationToken`

        GitHub authorization token used to clone the repository.

      - `required Type Type`

        - `"github_repository"GitHubRepository`

      - `required string Url`

        Github URL of the repository

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

          - `required Type Type`

            - `"branch"Branch`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

          - `required Type Type`

            - `"commit"Commit`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceParams:`

      Mount a file uploaded via the Files API into the session.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

        - `"file"File`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceParam:`

      Parameters for attaching a memory store to an agent session.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

        - `"memory_store"MemoryStore`

      - `Access? Access`

        Access mode for an attached memory store.

        - `"read_write"ReadWrite`

        - `"read_only"ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `BetaManagedAgentsScheduleParams? schedule`

    Body param: 5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `IReadOnlyList<string> vaultIds`

    Body param: Vault IDs for stored credentials the agent can use during sessions created from this deployment. Maximum 50.

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

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `required string ID`

    Unique identifier for this deployment.

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

      - `"agent"Agent`

    - `required Int Version`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? Description`

    Description of what the deployment does.

  - `required string EnvironmentID`

    ID of the `environment` where sessions run.

  - `required IReadOnlyList<BetaManagedAgentsDeploymentInitialEvent> InitialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

      - `required Type Type`

        - `"user.message"UserMessage`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `required string Description`

        What the agent should produce. This is the task specification.

      - `required Rubric Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `required string FileID`

            ID of the rubric file.

          - `required Type Type`

            - `"file"File`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `required Type Type`

            - `"text"Text`

      - `required Type Type`

        - `"user.define_outcome"UserDefineOutcome`

      - `Int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `required Type Type`

        - `"system.message"SystemMessage`

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `required string Name`

    Human-readable name.

  - `required BetaManagedAgentsDeploymentPausedReason? PausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `required Type Type`

        - `"manual"Manual`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `required BetaManagedAgentsDeploymentPausedReasonError Error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `required Type Type`

            - `"environment_archived_error"EnvironmentArchivedError`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `required Type Type`

            - `"agent_archived_error"AgentArchivedError`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `required Type Type`

            - `"environment_not_found_error"EnvironmentNotFoundError`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `required Type Type`

            - `"vault_not_found_error"VaultNotFoundError`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `required Type Type`

            - `"file_not_found_error"FileNotFoundError`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `required Type Type`

            - `"session_resource_not_found_error"SessionResourceNotFoundError`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `required Type Type`

            - `"workspace_archived_error"WorkspaceArchivedError`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `required Type Type`

            - `"organization_disabled_error"OrganizationDisabledError`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `required Type Type`

            - `"memory_store_archived_error"MemoryStoreArchivedError`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `required Type Type`

            - `"skill_not_found_error"SkillNotFoundError`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `required Type Type`

            - `"vault_archived_error"VaultArchivedError`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `required Type Type`

            - `"unknown_error"UnknownError`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `required Type Type`

            - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `required Type Type`

            - `"mcp_egress_blocked_error"McpEgressBlockedError`

      - `required Type Type`

        - `"error"Error`

  - `required IReadOnlyList<BetaManagedAgentsSessionResourceConfig> Resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `required Type Type`

        - `"github_repository"GitHubRepository`

      - `required string Url`

        Github URL of the repository

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

          - `required Type Type`

            - `"branch"Branch`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

          - `required Type Type`

            - `"commit"Commit`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

        - `"file"File`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

        - `"memory_store"MemoryStore`

      - `Access? Access`

        Access mode for an attached memory store.

        - `"read_write"ReadWrite`

        - `"read_only"ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `required BetaManagedAgentsSchedule? Schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `required string Expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `required string Timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `required Type Type`

      - `"cron"Cron`

    - `DateTimeOffset? LastRunAt`

      A timestamp in RFC 3339 format

    - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `required BetaManagedAgentsDeploymentStatus Status`

    Lifecycle status of a deployment.

    - `"active"Active`

    - `"paused"Paused`

  - `required Type Type`

    - `"deployment"Deployment`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyList<string> VaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```csharp
DeploymentCreateParams parameters = new()
{
    Agent = "string",
    EnvironmentID = "x",
    InitialEvents =
    [
        new BetaManagedAgentsUserMessageEventParams()
        {
            Content =
            [
                new BetaManagedAgentsTextBlock()
                {
                    Text = "Where is my order #1234?",
                    Type = Type.Text,
                },
            ],
            Type = Type.UserMessage,
        },
    ],
    Name = "x",
};

var betaManagedAgentsDeployment = await client.Beta.Deployments.Create(parameters);

Console.WriteLine(betaManagedAgentsDeployment);
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

`DeploymentListPageResponse Beta.Deployments.List(DeploymentListParams?parameters, CancellationTokencancellationToken = default)`

**get** `/v1/deployments`

List Deployments

### Parameters

- `DeploymentListParams parameters`

  - `string agentID`

    Query param: Filter by agent ID.

  - `DateTimeOffset createdAtGte`

    Query param: Return deployments created at or after this time (inclusive).

  - `DateTimeOffset createdAtLte`

    Query param: Return deployments created at or before this time (inclusive).

  - `Boolean includeArchived`

    Query param: When true, includes archived deployments. Default: false (exclude archived).

  - `Int limit`

    Query param: Maximum results per page. Default 20, maximum 100.

  - `string page`

    Query param: Opaque pagination cursor.

  - `BetaManagedAgentsDeploymentStatus status`

    Query param: Filter by status: active or paused. Omit for both. To include archived deployments, use include_archived instead; the two cannot be combined.

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

- `class DeploymentListPageResponse:`

  Paginated list of deployments.

  - `required IReadOnlyList<BetaManagedAgentsDeployment> Data`

    List of deployments.

    - `required string ID`

      Unique identifier for this deployment.

    - `required BetaManagedAgentsAgentReference Agent`

      A resolved agent reference with a concrete version.

      - `required string ID`

      - `required Type Type`

        - `"agent"Agent`

      - `required Int Version`

    - `required DateTimeOffset? ArchivedAt`

      A timestamp in RFC 3339 format

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required string? Description`

      Description of what the deployment does.

    - `required string EnvironmentID`

      ID of the `environment` where sessions run.

    - `required IReadOnlyList<BetaManagedAgentsDeploymentInitialEvent> InitialEvents`

      Events sent to each session immediately after creation.

      - `class BetaManagedAgentsDeploymentUserMessageEvent:`

        A user message sent to the session.

        - `required IReadOnlyList<Content> Content`

          Array of content blocks for the user message.

          - `class BetaManagedAgentsTextBlock:`

            Regular text content.

            - `required string Text`

              The text content.

            - `required Type Type`

              - `"text"Text`

          - `class BetaManagedAgentsImageBlock:`

            Image content specified directly as base64 data or as a reference via a URL.

            - `required Source Source`

              Union type for image source variants.

              - `class BetaManagedAgentsBase64ImageSource:`

                Base64-encoded image data.

                - `required string Data`

                  Base64-encoded image data.

                - `required string MediaType`

                  MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                - `required Type Type`

                  - `"base64"Base64`

              - `class BetaManagedAgentsUrlImageSource:`

                Image referenced by URL.

                - `required Type Type`

                  - `"url"Url`

                - `required string Url`

                  URL of the image to fetch.

              - `class BetaManagedAgentsFileImageSource:`

                Image referenced by file ID.

                - `required string FileID`

                  ID of a previously uploaded file.

                - `required Type Type`

                  - `"file"File`

            - `required Type Type`

              - `"image"Image`

          - `class BetaManagedAgentsDocumentBlock:`

            Document content, either specified directly as base64 data, as text, or as a reference via a URL.

            - `required Source Source`

              Union type for document source variants.

              - `class BetaManagedAgentsBase64DocumentSource:`

                Base64-encoded document data.

                - `required string Data`

                  Base64-encoded document data.

                - `required string MediaType`

                  MIME type of the document (e.g., "application/pdf").

                - `required Type Type`

                  - `"base64"Base64`

              - `class BetaManagedAgentsPlainTextDocumentSource:`

                Plain text document content.

                - `required string Data`

                  The plain text content.

                - `required MediaType MediaType`

                  MIME type of the text content. Must be "text/plain".

                  - `"text/plain"TextPlain`

                - `required Type Type`

                  - `"text"Text`

              - `class BetaManagedAgentsUrlDocumentSource:`

                Document referenced by URL.

                - `required Type Type`

                  - `"url"Url`

                - `required string Url`

                  URL of the document to fetch.

              - `class BetaManagedAgentsFileDocumentSource:`

                Document referenced by file ID.

                - `required string FileID`

                  ID of a previously uploaded file.

                - `required Type Type`

                  - `"file"File`

            - `required Type Type`

              - `"document"Document`

            - `string? Context`

              Additional context about the document for the model.

            - `string? Title`

              The title of the document.

        - `required Type Type`

          - `"user.message"UserMessage`

      - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

        An outcome the agent should work toward. The agent begins work on receipt.

        - `required string Description`

          What the agent should produce. This is the task specification.

        - `required Rubric Rubric`

          Rubric for grading the quality of an outcome.

          - `class BetaManagedAgentsFileRubric:`

            Rubric referenced by a file uploaded via the Files API.

            - `required string FileID`

              ID of the rubric file.

            - `required Type Type`

              - `"file"File`

          - `class BetaManagedAgentsTextRubric:`

            Rubric content provided inline as text.

            - `required string Content`

              Rubric content. Plain text or markdown — the grader treats it as freeform text.

            - `required Type Type`

              - `"text"Text`

        - `required Type Type`

          - `"user.define_outcome"UserDefineOutcome`

        - `Int? MaxIterations`

          Eval→revision cycles before giving up. Default 3, max 20.

      - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

        Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

        - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

          System content blocks to append. Text-only.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `required Type Type`

          - `"system.message"SystemMessage`

    - `required IReadOnlyDictionary<string, string> Metadata`

      Arbitrary key-value metadata. Maximum 16 pairs.

    - `required string Name`

      Human-readable name.

    - `required BetaManagedAgentsDeploymentPausedReason? PausedReason`

      Why a deployment is paused. Non-null exactly when `status` is `paused`.

      - `class BetaManagedAgentsManualDeploymentPausedReason:`

        The caller invoked the pause endpoint on the deployment.

        - `required Type Type`

          - `"manual"Manual`

      - `class BetaManagedAgentsErrorDeploymentPausedReason:`

        A scheduled fire recorded a failed run whose error auto-pauses the deployment.

        - `required BetaManagedAgentsDeploymentPausedReasonError Error`

          The error that triggered an auto-pause. Matches the failed run's `error.type`.

          - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

            The deployment's environment was archived.

            - `required Type Type`

              - `"environment_archived_error"EnvironmentArchivedError`

          - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

            The deployment's agent was archived.

            - `required Type Type`

              - `"agent_archived_error"AgentArchivedError`

          - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

            The deployment's environment no longer exists.

            - `required Type Type`

              - `"environment_not_found_error"EnvironmentNotFoundError`

          - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

            A vault referenced by the deployment no longer exists.

            - `required Type Type`

              - `"vault_not_found_error"VaultNotFoundError`

          - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

            A file resource referenced by the deployment no longer exists.

            - `required Type Type`

              - `"file_not_found_error"FileNotFoundError`

          - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

            A referenced resource no longer exists and its kind was not reported.

            - `required Type Type`

              - `"session_resource_not_found_error"SessionResourceNotFoundError`

          - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

            The deployment's workspace was archived.

            - `required Type Type`

              - `"workspace_archived_error"WorkspaceArchivedError`

          - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

            The deployment's organization is disabled.

            - `required Type Type`

              - `"organization_disabled_error"OrganizationDisabledError`

          - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

            A memory store referenced by the deployment is archived.

            - `required Type Type`

              - `"memory_store_archived_error"MemoryStoreArchivedError`

          - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

            A skill referenced by the deployment's agent no longer exists.

            - `required Type Type`

              - `"skill_not_found_error"SkillNotFoundError`

          - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

            A vault referenced by the deployment is archived.

            - `required Type Type`

              - `"vault_archived_error"VaultArchivedError`

          - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

            An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

            - `required Type Type`

              - `"unknown_error"UnknownError`

          - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

            The deployment configures resources, but its environment is self-hosted and cannot mount them.

            - `required Type Type`

              - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

          - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

            An MCP server host used by the deployment's agent is blocked by the environment's network policy.

            - `required Type Type`

              - `"mcp_egress_blocked_error"McpEgressBlockedError`

        - `required Type Type`

          - `"error"Error`

    - `required IReadOnlyList<BetaManagedAgentsSessionResourceConfig> Resources`

      Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

      - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

        A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

        - `required Type Type`

          - `"github_repository"GitHubRepository`

        - `required string Url`

          Github URL of the repository

        - `Checkout? Checkout`

          Branch or commit to check out. Defaults to the repository's default branch.

          - `class BetaManagedAgentsBranchCheckout:`

            - `required string Name`

              Branch name to check out.

            - `required Type Type`

              - `"branch"Branch`

          - `class BetaManagedAgentsCommitCheckout:`

            - `required string Sha`

              Full commit SHA to check out.

            - `required Type Type`

              - `"commit"Commit`

        - `string? MountPath`

          Mount path in the container. Defaults to `/workspace/<repo-name>`.

      - `class BetaManagedAgentsFileResourceConfig:`

        A file mounted into each session's container.

        - `required string FileID`

          ID of a previously uploaded file.

        - `required Type Type`

          - `"file"File`

        - `string? MountPath`

          Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

      - `class BetaManagedAgentsMemoryStoreResourceConfig:`

        A memory store attached to each session created from this deployment.

        - `required string MemoryStoreID`

          The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

        - `required Type Type`

          - `"memory_store"MemoryStore`

        - `Access? Access`

          Access mode for an attached memory store.

          - `"read_write"ReadWrite`

          - `"read_only"ReadOnly`

        - `string? Instructions`

          Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `required BetaManagedAgentsSchedule? Schedule`

      5-field POSIX cron schedule with computed runtime timestamps.

      - `required string Expression`

        5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      - `required string Timezone`

        IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      - `required Type Type`

        - `"cron"Cron`

      - `DateTimeOffset? LastRunAt`

        A timestamp in RFC 3339 format

      - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

        Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

    - `required BetaManagedAgentsDeploymentStatus Status`

      Lifecycle status of a deployment.

      - `"active"Active`

      - `"paused"Paused`

    - `required Type Type`

      - `"deployment"Deployment`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

    - `required IReadOnlyList<string> VaultIds`

      Vault IDs supplying stored credentials for sessions created from this deployment.

  - `string? NextPage`

    Opaque cursor for the next page. Null when no more results.

### Example

```csharp
DeploymentListParams parameters = new();

var page = await client.Beta.Deployments.List(parameters);
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

`BetaManagedAgentsDeployment Beta.Deployments.Retrieve(DeploymentRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/deployments/{deployment_id}`

Get Deployment

### Parameters

- `DeploymentRetrieveParams parameters`

  - `required string deploymentID`

    Path parameter deployment_id

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

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `required string ID`

    Unique identifier for this deployment.

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

      - `"agent"Agent`

    - `required Int Version`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? Description`

    Description of what the deployment does.

  - `required string EnvironmentID`

    ID of the `environment` where sessions run.

  - `required IReadOnlyList<BetaManagedAgentsDeploymentInitialEvent> InitialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

      - `required Type Type`

        - `"user.message"UserMessage`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `required string Description`

        What the agent should produce. This is the task specification.

      - `required Rubric Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `required string FileID`

            ID of the rubric file.

          - `required Type Type`

            - `"file"File`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `required Type Type`

            - `"text"Text`

      - `required Type Type`

        - `"user.define_outcome"UserDefineOutcome`

      - `Int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `required Type Type`

        - `"system.message"SystemMessage`

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `required string Name`

    Human-readable name.

  - `required BetaManagedAgentsDeploymentPausedReason? PausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `required Type Type`

        - `"manual"Manual`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `required BetaManagedAgentsDeploymentPausedReasonError Error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `required Type Type`

            - `"environment_archived_error"EnvironmentArchivedError`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `required Type Type`

            - `"agent_archived_error"AgentArchivedError`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `required Type Type`

            - `"environment_not_found_error"EnvironmentNotFoundError`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `required Type Type`

            - `"vault_not_found_error"VaultNotFoundError`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `required Type Type`

            - `"file_not_found_error"FileNotFoundError`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `required Type Type`

            - `"session_resource_not_found_error"SessionResourceNotFoundError`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `required Type Type`

            - `"workspace_archived_error"WorkspaceArchivedError`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `required Type Type`

            - `"organization_disabled_error"OrganizationDisabledError`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `required Type Type`

            - `"memory_store_archived_error"MemoryStoreArchivedError`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `required Type Type`

            - `"skill_not_found_error"SkillNotFoundError`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `required Type Type`

            - `"vault_archived_error"VaultArchivedError`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `required Type Type`

            - `"unknown_error"UnknownError`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `required Type Type`

            - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `required Type Type`

            - `"mcp_egress_blocked_error"McpEgressBlockedError`

      - `required Type Type`

        - `"error"Error`

  - `required IReadOnlyList<BetaManagedAgentsSessionResourceConfig> Resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `required Type Type`

        - `"github_repository"GitHubRepository`

      - `required string Url`

        Github URL of the repository

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

          - `required Type Type`

            - `"branch"Branch`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

          - `required Type Type`

            - `"commit"Commit`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

        - `"file"File`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

        - `"memory_store"MemoryStore`

      - `Access? Access`

        Access mode for an attached memory store.

        - `"read_write"ReadWrite`

        - `"read_only"ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `required BetaManagedAgentsSchedule? Schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `required string Expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `required string Timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `required Type Type`

      - `"cron"Cron`

    - `DateTimeOffset? LastRunAt`

      A timestamp in RFC 3339 format

    - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `required BetaManagedAgentsDeploymentStatus Status`

    Lifecycle status of a deployment.

    - `"active"Active`

    - `"paused"Paused`

  - `required Type Type`

    - `"deployment"Deployment`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyList<string> VaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```csharp
DeploymentRetrieveParams parameters = new()
{
    DeploymentID = "depl_011CZkZcDH3vPqd7xnEfwTai"
};

var betaManagedAgentsDeployment = await client.Beta.Deployments.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsDeployment);
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

`BetaManagedAgentsDeployment Beta.Deployments.Update(DeploymentUpdateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/deployments/{deployment_id}`

Update Deployment

### Parameters

- `DeploymentUpdateParams parameters`

  - `required string deploymentID`

    Path param: Path parameter deployment_id

  - `Agent agent`

    Body param: Agent to deploy. Accepts the `agent` ID string, which re-pins to the latest version, or an `agent` object with both id and version specified. Omit to preserve. Cannot be cleared.

    - `string`

    - `class BetaManagedAgentsAgentParams:`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `required string ID`

        The `agent` ID.

      - `required Type Type`

        - `"agent"Agent`

      - `Int Version`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

  - `string? description`

    Body param: Description. Omit to preserve; send empty string or null to clear.

  - `string environmentID`

    Body param: ID of the `environment` where sessions run. Omit to preserve. Cannot be cleared.

  - `IReadOnlyList<BetaManagedAgentsDeploymentInitialEventParams> initialEvents`

    Body param: Initial events. Full replacement. Omit to preserve. Cannot be cleared. At least 1, maximum 50.

    - `class BetaManagedAgentsUserMessageEventParams:`

      Parameters for sending a user message to the session.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

      - `required Type Type`

        - `"user.message"UserMessage`

    - `class BetaManagedAgentsUserDefineOutcomeEventParams:`

      Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

      - `required string Description`

        What the agent should produce. This is the task specification.

      - `required Rubric Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubricParams:`

          Rubric referenced by a file uploaded via the Files API.

          - `required string FileID`

            ID of the rubric file.

          - `required Type Type`

            - `"file"File`

        - `class BetaManagedAgentsTextRubricParams:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

          - `required Type Type`

            - `"text"Text`

      - `required Type Type`

        - `"user.define_outcome"UserDefineOutcome`

      - `Int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsSystemMessageEventParams:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `required Type Type`

        - `"system.message"SystemMessage`

  - `IReadOnlyDictionary<string, string>? metadata`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `string name`

    Body param: Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

  - `IReadOnlyList<Resource>? resources`

    Body param: Session resources. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 500.

    - `class BetaManagedAgentsGitHubRepositoryResourceParams:`

      Mount a GitHub repository into the session's container.

      - `required string AuthorizationToken`

        GitHub authorization token used to clone the repository.

      - `required Type Type`

        - `"github_repository"GitHubRepository`

      - `required string Url`

        Github URL of the repository

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

          - `required Type Type`

            - `"branch"Branch`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

          - `required Type Type`

            - `"commit"Commit`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceParams:`

      Mount a file uploaded via the Files API into the session.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

        - `"file"File`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceParam:`

      Parameters for attaching a memory store to an agent session.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

        - `"memory_store"MemoryStore`

      - `Access? Access`

        Access mode for an attached memory store.

        - `"read_write"ReadWrite`

        - `"read_only"ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `BetaManagedAgentsScheduleParams? schedule`

    Body param: 5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `IReadOnlyList<string>? vaultIds`

    Body param: Vault IDs. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 50.

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

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `required string ID`

    Unique identifier for this deployment.

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

      - `"agent"Agent`

    - `required Int Version`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? Description`

    Description of what the deployment does.

  - `required string EnvironmentID`

    ID of the `environment` where sessions run.

  - `required IReadOnlyList<BetaManagedAgentsDeploymentInitialEvent> InitialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

      - `required Type Type`

        - `"user.message"UserMessage`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `required string Description`

        What the agent should produce. This is the task specification.

      - `required Rubric Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `required string FileID`

            ID of the rubric file.

          - `required Type Type`

            - `"file"File`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `required Type Type`

            - `"text"Text`

      - `required Type Type`

        - `"user.define_outcome"UserDefineOutcome`

      - `Int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `required Type Type`

        - `"system.message"SystemMessage`

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `required string Name`

    Human-readable name.

  - `required BetaManagedAgentsDeploymentPausedReason? PausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `required Type Type`

        - `"manual"Manual`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `required BetaManagedAgentsDeploymentPausedReasonError Error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `required Type Type`

            - `"environment_archived_error"EnvironmentArchivedError`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `required Type Type`

            - `"agent_archived_error"AgentArchivedError`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `required Type Type`

            - `"environment_not_found_error"EnvironmentNotFoundError`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `required Type Type`

            - `"vault_not_found_error"VaultNotFoundError`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `required Type Type`

            - `"file_not_found_error"FileNotFoundError`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `required Type Type`

            - `"session_resource_not_found_error"SessionResourceNotFoundError`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `required Type Type`

            - `"workspace_archived_error"WorkspaceArchivedError`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `required Type Type`

            - `"organization_disabled_error"OrganizationDisabledError`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `required Type Type`

            - `"memory_store_archived_error"MemoryStoreArchivedError`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `required Type Type`

            - `"skill_not_found_error"SkillNotFoundError`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `required Type Type`

            - `"vault_archived_error"VaultArchivedError`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `required Type Type`

            - `"unknown_error"UnknownError`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `required Type Type`

            - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `required Type Type`

            - `"mcp_egress_blocked_error"McpEgressBlockedError`

      - `required Type Type`

        - `"error"Error`

  - `required IReadOnlyList<BetaManagedAgentsSessionResourceConfig> Resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `required Type Type`

        - `"github_repository"GitHubRepository`

      - `required string Url`

        Github URL of the repository

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

          - `required Type Type`

            - `"branch"Branch`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

          - `required Type Type`

            - `"commit"Commit`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

        - `"file"File`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

        - `"memory_store"MemoryStore`

      - `Access? Access`

        Access mode for an attached memory store.

        - `"read_write"ReadWrite`

        - `"read_only"ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `required BetaManagedAgentsSchedule? Schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `required string Expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `required string Timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `required Type Type`

      - `"cron"Cron`

    - `DateTimeOffset? LastRunAt`

      A timestamp in RFC 3339 format

    - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `required BetaManagedAgentsDeploymentStatus Status`

    Lifecycle status of a deployment.

    - `"active"Active`

    - `"paused"Paused`

  - `required Type Type`

    - `"deployment"Deployment`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyList<string> VaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```csharp
DeploymentUpdateParams parameters = new()
{
    DeploymentID = "depl_011CZkZcDH3vPqd7xnEfwTai"
};

var betaManagedAgentsDeployment = await client.Beta.Deployments.Update(parameters);

Console.WriteLine(betaManagedAgentsDeployment);
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

`BetaManagedAgentsDeployment Beta.Deployments.Archive(DeploymentArchiveParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/deployments/{deployment_id}/archive`

Archive Deployment

### Parameters

- `DeploymentArchiveParams parameters`

  - `required string deploymentID`

    Path parameter deployment_id

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

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `required string ID`

    Unique identifier for this deployment.

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

      - `"agent"Agent`

    - `required Int Version`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? Description`

    Description of what the deployment does.

  - `required string EnvironmentID`

    ID of the `environment` where sessions run.

  - `required IReadOnlyList<BetaManagedAgentsDeploymentInitialEvent> InitialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

      - `required Type Type`

        - `"user.message"UserMessage`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `required string Description`

        What the agent should produce. This is the task specification.

      - `required Rubric Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `required string FileID`

            ID of the rubric file.

          - `required Type Type`

            - `"file"File`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `required Type Type`

            - `"text"Text`

      - `required Type Type`

        - `"user.define_outcome"UserDefineOutcome`

      - `Int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `required Type Type`

        - `"system.message"SystemMessage`

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `required string Name`

    Human-readable name.

  - `required BetaManagedAgentsDeploymentPausedReason? PausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `required Type Type`

        - `"manual"Manual`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `required BetaManagedAgentsDeploymentPausedReasonError Error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `required Type Type`

            - `"environment_archived_error"EnvironmentArchivedError`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `required Type Type`

            - `"agent_archived_error"AgentArchivedError`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `required Type Type`

            - `"environment_not_found_error"EnvironmentNotFoundError`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `required Type Type`

            - `"vault_not_found_error"VaultNotFoundError`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `required Type Type`

            - `"file_not_found_error"FileNotFoundError`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `required Type Type`

            - `"session_resource_not_found_error"SessionResourceNotFoundError`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `required Type Type`

            - `"workspace_archived_error"WorkspaceArchivedError`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `required Type Type`

            - `"organization_disabled_error"OrganizationDisabledError`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `required Type Type`

            - `"memory_store_archived_error"MemoryStoreArchivedError`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `required Type Type`

            - `"skill_not_found_error"SkillNotFoundError`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `required Type Type`

            - `"vault_archived_error"VaultArchivedError`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `required Type Type`

            - `"unknown_error"UnknownError`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `required Type Type`

            - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `required Type Type`

            - `"mcp_egress_blocked_error"McpEgressBlockedError`

      - `required Type Type`

        - `"error"Error`

  - `required IReadOnlyList<BetaManagedAgentsSessionResourceConfig> Resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `required Type Type`

        - `"github_repository"GitHubRepository`

      - `required string Url`

        Github URL of the repository

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

          - `required Type Type`

            - `"branch"Branch`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

          - `required Type Type`

            - `"commit"Commit`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

        - `"file"File`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

        - `"memory_store"MemoryStore`

      - `Access? Access`

        Access mode for an attached memory store.

        - `"read_write"ReadWrite`

        - `"read_only"ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `required BetaManagedAgentsSchedule? Schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `required string Expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `required string Timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `required Type Type`

      - `"cron"Cron`

    - `DateTimeOffset? LastRunAt`

      A timestamp in RFC 3339 format

    - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `required BetaManagedAgentsDeploymentStatus Status`

    Lifecycle status of a deployment.

    - `"active"Active`

    - `"paused"Paused`

  - `required Type Type`

    - `"deployment"Deployment`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyList<string> VaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```csharp
DeploymentArchiveParams parameters = new()
{
    DeploymentID = "depl_011CZkZcDH3vPqd7xnEfwTai"
};

var betaManagedAgentsDeployment = await client.Beta.Deployments.Archive(parameters);

Console.WriteLine(betaManagedAgentsDeployment);
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

`BetaManagedAgentsDeploymentRun Beta.Deployments.Run(DeploymentRunParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/deployments/{deployment_id}/run`

Run Deployment Now

### Parameters

- `DeploymentRunParams parameters`

  - `required string deploymentID`

    Path parameter deployment_id

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
DeploymentRunParams parameters = new()
{
    DeploymentID = "depl_011CZkZcDH3vPqd7xnEfwTai"
};

var betaManagedAgentsDeploymentRun = await client.Beta.Deployments.Run(parameters);

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

## Pause Deployment

`BetaManagedAgentsDeployment Beta.Deployments.Pause(DeploymentPauseParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/deployments/{deployment_id}/pause`

Pause Deployment

### Parameters

- `DeploymentPauseParams parameters`

  - `required string deploymentID`

    Path parameter deployment_id

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

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `required string ID`

    Unique identifier for this deployment.

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

      - `"agent"Agent`

    - `required Int Version`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? Description`

    Description of what the deployment does.

  - `required string EnvironmentID`

    ID of the `environment` where sessions run.

  - `required IReadOnlyList<BetaManagedAgentsDeploymentInitialEvent> InitialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

      - `required Type Type`

        - `"user.message"UserMessage`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `required string Description`

        What the agent should produce. This is the task specification.

      - `required Rubric Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `required string FileID`

            ID of the rubric file.

          - `required Type Type`

            - `"file"File`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `required Type Type`

            - `"text"Text`

      - `required Type Type`

        - `"user.define_outcome"UserDefineOutcome`

      - `Int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `required Type Type`

        - `"system.message"SystemMessage`

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `required string Name`

    Human-readable name.

  - `required BetaManagedAgentsDeploymentPausedReason? PausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `required Type Type`

        - `"manual"Manual`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `required BetaManagedAgentsDeploymentPausedReasonError Error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `required Type Type`

            - `"environment_archived_error"EnvironmentArchivedError`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `required Type Type`

            - `"agent_archived_error"AgentArchivedError`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `required Type Type`

            - `"environment_not_found_error"EnvironmentNotFoundError`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `required Type Type`

            - `"vault_not_found_error"VaultNotFoundError`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `required Type Type`

            - `"file_not_found_error"FileNotFoundError`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `required Type Type`

            - `"session_resource_not_found_error"SessionResourceNotFoundError`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `required Type Type`

            - `"workspace_archived_error"WorkspaceArchivedError`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `required Type Type`

            - `"organization_disabled_error"OrganizationDisabledError`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `required Type Type`

            - `"memory_store_archived_error"MemoryStoreArchivedError`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `required Type Type`

            - `"skill_not_found_error"SkillNotFoundError`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `required Type Type`

            - `"vault_archived_error"VaultArchivedError`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `required Type Type`

            - `"unknown_error"UnknownError`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `required Type Type`

            - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `required Type Type`

            - `"mcp_egress_blocked_error"McpEgressBlockedError`

      - `required Type Type`

        - `"error"Error`

  - `required IReadOnlyList<BetaManagedAgentsSessionResourceConfig> Resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `required Type Type`

        - `"github_repository"GitHubRepository`

      - `required string Url`

        Github URL of the repository

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

          - `required Type Type`

            - `"branch"Branch`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

          - `required Type Type`

            - `"commit"Commit`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

        - `"file"File`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

        - `"memory_store"MemoryStore`

      - `Access? Access`

        Access mode for an attached memory store.

        - `"read_write"ReadWrite`

        - `"read_only"ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `required BetaManagedAgentsSchedule? Schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `required string Expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `required string Timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `required Type Type`

      - `"cron"Cron`

    - `DateTimeOffset? LastRunAt`

      A timestamp in RFC 3339 format

    - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `required BetaManagedAgentsDeploymentStatus Status`

    Lifecycle status of a deployment.

    - `"active"Active`

    - `"paused"Paused`

  - `required Type Type`

    - `"deployment"Deployment`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyList<string> VaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```csharp
DeploymentPauseParams parameters = new()
{
    DeploymentID = "depl_011CZkZcDH3vPqd7xnEfwTai"
};

var betaManagedAgentsDeployment = await client.Beta.Deployments.Pause(parameters);

Console.WriteLine(betaManagedAgentsDeployment);
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

`BetaManagedAgentsDeployment Beta.Deployments.Unpause(DeploymentUnpauseParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/deployments/{deployment_id}/unpause`

Unpause Deployment

### Parameters

- `DeploymentUnpauseParams parameters`

  - `required string deploymentID`

    Path parameter deployment_id

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

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `required string ID`

    Unique identifier for this deployment.

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

      - `"agent"Agent`

    - `required Int Version`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? Description`

    Description of what the deployment does.

  - `required string EnvironmentID`

    ID of the `environment` where sessions run.

  - `required IReadOnlyList<BetaManagedAgentsDeploymentInitialEvent> InitialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

      - `required Type Type`

        - `"user.message"UserMessage`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `required string Description`

        What the agent should produce. This is the task specification.

      - `required Rubric Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `required string FileID`

            ID of the rubric file.

          - `required Type Type`

            - `"file"File`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `required Type Type`

            - `"text"Text`

      - `required Type Type`

        - `"user.define_outcome"UserDefineOutcome`

      - `Int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `required Type Type`

        - `"system.message"SystemMessage`

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `required string Name`

    Human-readable name.

  - `required BetaManagedAgentsDeploymentPausedReason? PausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `required Type Type`

        - `"manual"Manual`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `required BetaManagedAgentsDeploymentPausedReasonError Error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `required Type Type`

            - `"environment_archived_error"EnvironmentArchivedError`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `required Type Type`

            - `"agent_archived_error"AgentArchivedError`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `required Type Type`

            - `"environment_not_found_error"EnvironmentNotFoundError`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `required Type Type`

            - `"vault_not_found_error"VaultNotFoundError`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `required Type Type`

            - `"file_not_found_error"FileNotFoundError`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `required Type Type`

            - `"session_resource_not_found_error"SessionResourceNotFoundError`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `required Type Type`

            - `"workspace_archived_error"WorkspaceArchivedError`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `required Type Type`

            - `"organization_disabled_error"OrganizationDisabledError`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `required Type Type`

            - `"memory_store_archived_error"MemoryStoreArchivedError`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `required Type Type`

            - `"skill_not_found_error"SkillNotFoundError`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `required Type Type`

            - `"vault_archived_error"VaultArchivedError`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `required Type Type`

            - `"unknown_error"UnknownError`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `required Type Type`

            - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `required Type Type`

            - `"mcp_egress_blocked_error"McpEgressBlockedError`

      - `required Type Type`

        - `"error"Error`

  - `required IReadOnlyList<BetaManagedAgentsSessionResourceConfig> Resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `required Type Type`

        - `"github_repository"GitHubRepository`

      - `required string Url`

        Github URL of the repository

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

          - `required Type Type`

            - `"branch"Branch`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

          - `required Type Type`

            - `"commit"Commit`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

        - `"file"File`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

        - `"memory_store"MemoryStore`

      - `Access? Access`

        Access mode for an attached memory store.

        - `"read_write"ReadWrite`

        - `"read_only"ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `required BetaManagedAgentsSchedule? Schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `required string Expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `required string Timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `required Type Type`

      - `"cron"Cron`

    - `DateTimeOffset? LastRunAt`

      A timestamp in RFC 3339 format

    - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `required BetaManagedAgentsDeploymentStatus Status`

    Lifecycle status of a deployment.

    - `"active"Active`

    - `"paused"Paused`

  - `required Type Type`

    - `"deployment"Deployment`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyList<string> VaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```csharp
DeploymentUnpauseParams parameters = new()
{
    DeploymentID = "depl_011CZkZcDH3vPqd7xnEfwTai"
};

var betaManagedAgentsDeployment = await client.Beta.Deployments.Unpause(parameters);

Console.WriteLine(betaManagedAgentsDeployment);
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

  - `required Type Type`

    - `"agent_archived_error"AgentArchivedError`

### Beta Managed Agents Cron Schedule

- `class BetaManagedAgentsCronSchedule:`

  5-field POSIX cron schedule with computed runtime timestamps.

  - `required string Expression`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `required string Timezone`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

  - `required Type Type`

    - `"cron"Cron`

  - `DateTimeOffset? LastRunAt`

    A timestamp in RFC 3339 format

  - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Cron Schedule Params

- `class BetaManagedAgentsCronScheduleParams:`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `required string Expression`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `required string Timezone`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `required Type Type`

    - `"cron"Cron`

### Beta Managed Agents Deployment

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `required string ID`

    Unique identifier for this deployment.

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

      - `"agent"Agent`

    - `required Int Version`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? Description`

    Description of what the deployment does.

  - `required string EnvironmentID`

    ID of the `environment` where sessions run.

  - `required IReadOnlyList<BetaManagedAgentsDeploymentInitialEvent> InitialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

      - `required Type Type`

        - `"user.message"UserMessage`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `required string Description`

        What the agent should produce. This is the task specification.

      - `required Rubric Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `required string FileID`

            ID of the rubric file.

          - `required Type Type`

            - `"file"File`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `required Type Type`

            - `"text"Text`

      - `required Type Type`

        - `"user.define_outcome"UserDefineOutcome`

      - `Int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `required Type Type`

        - `"system.message"SystemMessage`

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `required string Name`

    Human-readable name.

  - `required BetaManagedAgentsDeploymentPausedReason? PausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `required Type Type`

        - `"manual"Manual`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `required BetaManagedAgentsDeploymentPausedReasonError Error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `required Type Type`

            - `"environment_archived_error"EnvironmentArchivedError`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `required Type Type`

            - `"agent_archived_error"AgentArchivedError`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `required Type Type`

            - `"environment_not_found_error"EnvironmentNotFoundError`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `required Type Type`

            - `"vault_not_found_error"VaultNotFoundError`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `required Type Type`

            - `"file_not_found_error"FileNotFoundError`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `required Type Type`

            - `"session_resource_not_found_error"SessionResourceNotFoundError`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `required Type Type`

            - `"workspace_archived_error"WorkspaceArchivedError`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `required Type Type`

            - `"organization_disabled_error"OrganizationDisabledError`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `required Type Type`

            - `"memory_store_archived_error"MemoryStoreArchivedError`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `required Type Type`

            - `"skill_not_found_error"SkillNotFoundError`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `required Type Type`

            - `"vault_archived_error"VaultArchivedError`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `required Type Type`

            - `"unknown_error"UnknownError`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `required Type Type`

            - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `required Type Type`

            - `"mcp_egress_blocked_error"McpEgressBlockedError`

      - `required Type Type`

        - `"error"Error`

  - `required IReadOnlyList<BetaManagedAgentsSessionResourceConfig> Resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `required Type Type`

        - `"github_repository"GitHubRepository`

      - `required string Url`

        Github URL of the repository

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

          - `required Type Type`

            - `"branch"Branch`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

          - `required Type Type`

            - `"commit"Commit`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

        - `"file"File`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

        - `"memory_store"MemoryStore`

      - `Access? Access`

        Access mode for an attached memory store.

        - `"read_write"ReadWrite`

        - `"read_only"ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `required BetaManagedAgentsSchedule? Schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `required string Expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `required string Timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `required Type Type`

      - `"cron"Cron`

    - `DateTimeOffset? LastRunAt`

      A timestamp in RFC 3339 format

    - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `required BetaManagedAgentsDeploymentStatus Status`

    Lifecycle status of a deployment.

    - `"active"Active`

    - `"paused"Paused`

  - `required Type Type`

    - `"deployment"Deployment`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyList<string> VaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Beta Managed Agents Deployment Initial Event

- `class BetaManagedAgentsDeploymentInitialEvent: A class that can be one of several variants.union`

  An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

  - `class BetaManagedAgentsDeploymentUserMessageEvent:`

    A user message sent to the session.

    - `required IReadOnlyList<Content> Content`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"image"Image`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"TextPlain`

            - `required Type Type`

              - `"text"Text`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"document"Document`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

    - `required Type Type`

      - `"user.message"UserMessage`

  - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

    An outcome the agent should work toward. The agent begins work on receipt.

    - `required string Description`

      What the agent should produce. This is the task specification.

    - `required Rubric Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric:`

        Rubric referenced by a file uploaded via the Files API.

        - `required string FileID`

          ID of the rubric file.

        - `required Type Type`

          - `"file"File`

      - `class BetaManagedAgentsTextRubric:`

        Rubric content provided inline as text.

        - `required string Content`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `required Type Type`

          - `"text"Text`

    - `required Type Type`

      - `"user.define_outcome"UserDefineOutcome`

    - `Int? MaxIterations`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

    - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

      System content blocks to append. Text-only.

      - `required string Text`

        The text content.

      - `required Type Type`

        - `"text"Text`

    - `required Type Type`

      - `"system.message"SystemMessage`

### Beta Managed Agents Deployment Initial Event Params

- `class BetaManagedAgentsDeploymentInitialEventParams: A class that can be one of several variants.union`

  An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

  - `class BetaManagedAgentsUserMessageEventParams:`

    Parameters for sending a user message to the session.

    - `required IReadOnlyList<Content> Content`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"image"Image`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"TextPlain`

            - `required Type Type`

              - `"text"Text`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"document"Document`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

    - `required Type Type`

      - `"user.message"UserMessage`

  - `class BetaManagedAgentsUserDefineOutcomeEventParams:`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `required string Description`

      What the agent should produce. This is the task specification.

    - `required Rubric Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubricParams:`

        Rubric referenced by a file uploaded via the Files API.

        - `required string FileID`

          ID of the rubric file.

        - `required Type Type`

          - `"file"File`

      - `class BetaManagedAgentsTextRubricParams:`

        Rubric content provided inline as text.

        - `required string Content`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

        - `required Type Type`

          - `"text"Text`

    - `required Type Type`

      - `"user.define_outcome"UserDefineOutcome`

    - `Int? MaxIterations`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `class BetaManagedAgentsSystemMessageEventParams:`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

      System content blocks to append. Text-only.

      - `required string Text`

        The text content.

      - `required Type Type`

        - `"text"Text`

    - `required Type Type`

      - `"system.message"SystemMessage`

### Beta Managed Agents Deployment Paused Reason

- `class BetaManagedAgentsDeploymentPausedReason: A class that can be one of several variants.union`

  Why a deployment is paused. Non-null exactly when `status` is `paused`.

  - `class BetaManagedAgentsManualDeploymentPausedReason:`

    The caller invoked the pause endpoint on the deployment.

    - `required Type Type`

      - `"manual"Manual`

  - `class BetaManagedAgentsErrorDeploymentPausedReason:`

    A scheduled fire recorded a failed run whose error auto-pauses the deployment.

    - `required BetaManagedAgentsDeploymentPausedReasonError Error`

      The error that triggered an auto-pause. Matches the failed run's `error.type`.

      - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

        The deployment's environment was archived.

        - `required Type Type`

          - `"environment_archived_error"EnvironmentArchivedError`

      - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

        The deployment's agent was archived.

        - `required Type Type`

          - `"agent_archived_error"AgentArchivedError`

      - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

        The deployment's environment no longer exists.

        - `required Type Type`

          - `"environment_not_found_error"EnvironmentNotFoundError`

      - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

        A vault referenced by the deployment no longer exists.

        - `required Type Type`

          - `"vault_not_found_error"VaultNotFoundError`

      - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

        A file resource referenced by the deployment no longer exists.

        - `required Type Type`

          - `"file_not_found_error"FileNotFoundError`

      - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

        A referenced resource no longer exists and its kind was not reported.

        - `required Type Type`

          - `"session_resource_not_found_error"SessionResourceNotFoundError`

      - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

        The deployment's workspace was archived.

        - `required Type Type`

          - `"workspace_archived_error"WorkspaceArchivedError`

      - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

        The deployment's organization is disabled.

        - `required Type Type`

          - `"organization_disabled_error"OrganizationDisabledError`

      - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

        A memory store referenced by the deployment is archived.

        - `required Type Type`

          - `"memory_store_archived_error"MemoryStoreArchivedError`

      - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

        A skill referenced by the deployment's agent no longer exists.

        - `required Type Type`

          - `"skill_not_found_error"SkillNotFoundError`

      - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

        A vault referenced by the deployment is archived.

        - `required Type Type`

          - `"vault_archived_error"VaultArchivedError`

      - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

        An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

        - `required Type Type`

          - `"unknown_error"UnknownError`

      - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

        The deployment configures resources, but its environment is self-hosted and cannot mount them.

        - `required Type Type`

          - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

      - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

        An MCP server host used by the deployment's agent is blocked by the environment's network policy.

        - `required Type Type`

          - `"mcp_egress_blocked_error"McpEgressBlockedError`

    - `required Type Type`

      - `"error"Error`

### Beta Managed Agents Deployment Paused Reason Error

- `class BetaManagedAgentsDeploymentPausedReasonError: A class that can be one of several variants.union`

  The error that triggered an auto-pause. Matches the failed run's `error.type`.

  - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

    The deployment's environment was archived.

    - `required Type Type`

      - `"environment_archived_error"EnvironmentArchivedError`

  - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

    The deployment's agent was archived.

    - `required Type Type`

      - `"agent_archived_error"AgentArchivedError`

  - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

    The deployment's environment no longer exists.

    - `required Type Type`

      - `"environment_not_found_error"EnvironmentNotFoundError`

  - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

    A vault referenced by the deployment no longer exists.

    - `required Type Type`

      - `"vault_not_found_error"VaultNotFoundError`

  - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

    A file resource referenced by the deployment no longer exists.

    - `required Type Type`

      - `"file_not_found_error"FileNotFoundError`

  - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

    A referenced resource no longer exists and its kind was not reported.

    - `required Type Type`

      - `"session_resource_not_found_error"SessionResourceNotFoundError`

  - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

    The deployment's workspace was archived.

    - `required Type Type`

      - `"workspace_archived_error"WorkspaceArchivedError`

  - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

    The deployment's organization is disabled.

    - `required Type Type`

      - `"organization_disabled_error"OrganizationDisabledError`

  - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

    A memory store referenced by the deployment is archived.

    - `required Type Type`

      - `"memory_store_archived_error"MemoryStoreArchivedError`

  - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

    A skill referenced by the deployment's agent no longer exists.

    - `required Type Type`

      - `"skill_not_found_error"SkillNotFoundError`

  - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

    A vault referenced by the deployment is archived.

    - `required Type Type`

      - `"vault_archived_error"VaultArchivedError`

  - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

    An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

    - `required Type Type`

      - `"unknown_error"UnknownError`

  - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

    The deployment configures resources, but its environment is self-hosted and cannot mount them.

    - `required Type Type`

      - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

  - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

    An MCP server host used by the deployment's agent is blocked by the environment's network policy.

    - `required Type Type`

      - `"mcp_egress_blocked_error"McpEgressBlockedError`

### Beta Managed Agents Deployment Status

- `enum BetaManagedAgentsDeploymentStatus:`

  Lifecycle status of a deployment.

  - `"active"Active`

  - `"paused"Paused`

### Beta Managed Agents Deployment System Message Event

- `class BetaManagedAgentsDeploymentSystemMessageEvent:`

  Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

  - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

    System content blocks to append. Text-only.

    - `required string Text`

      The text content.

    - `required Type Type`

      - `"text"Text`

  - `required Type Type`

    - `"system.message"SystemMessage`

### Beta Managed Agents Deployment User Define Outcome Event

- `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

  An outcome the agent should work toward. The agent begins work on receipt.

  - `required string Description`

    What the agent should produce. This is the task specification.

  - `required Rubric Rubric`

    Rubric for grading the quality of an outcome.

    - `class BetaManagedAgentsFileRubric:`

      Rubric referenced by a file uploaded via the Files API.

      - `required string FileID`

        ID of the rubric file.

      - `required Type Type`

        - `"file"File`

    - `class BetaManagedAgentsTextRubric:`

      Rubric content provided inline as text.

      - `required string Content`

        Rubric content. Plain text or markdown — the grader treats it as freeform text.

      - `required Type Type`

        - `"text"Text`

  - `required Type Type`

    - `"user.define_outcome"UserDefineOutcome`

  - `Int? MaxIterations`

    Eval→revision cycles before giving up. Default 3, max 20.

### Beta Managed Agents Deployment User Message Event

- `class BetaManagedAgentsDeploymentUserMessageEvent:`

  A user message sent to the session.

  - `required IReadOnlyList<Content> Content`

    Array of content blocks for the user message.

    - `class BetaManagedAgentsTextBlock:`

      Regular text content.

      - `required string Text`

        The text content.

      - `required Type Type`

        - `"text"Text`

    - `class BetaManagedAgentsImageBlock:`

      Image content specified directly as base64 data or as a reference via a URL.

      - `required Source Source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource:`

          Base64-encoded image data.

          - `required string Data`

            Base64-encoded image data.

          - `required string MediaType`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `required Type Type`

            - `"base64"Base64`

        - `class BetaManagedAgentsUrlImageSource:`

          Image referenced by URL.

          - `required Type Type`

            - `"url"Url`

          - `required string Url`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource:`

          Image referenced by file ID.

          - `required string FileID`

            ID of a previously uploaded file.

          - `required Type Type`

            - `"file"File`

      - `required Type Type`

        - `"image"Image`

    - `class BetaManagedAgentsDocumentBlock:`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `required Source Source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource:`

          Base64-encoded document data.

          - `required string Data`

            Base64-encoded document data.

          - `required string MediaType`

            MIME type of the document (e.g., "application/pdf").

          - `required Type Type`

            - `"base64"Base64`

        - `class BetaManagedAgentsPlainTextDocumentSource:`

          Plain text document content.

          - `required string Data`

            The plain text content.

          - `required MediaType MediaType`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"TextPlain`

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsUrlDocumentSource:`

          Document referenced by URL.

          - `required Type Type`

            - `"url"Url`

          - `required string Url`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource:`

          Document referenced by file ID.

          - `required string FileID`

            ID of a previously uploaded file.

          - `required Type Type`

            - `"file"File`

      - `required Type Type`

        - `"document"Document`

      - `string? Context`

        Additional context about the document for the model.

      - `string? Title`

        The title of the document.

  - `required Type Type`

    - `"user.message"UserMessage`

### Beta Managed Agents Environment Archived Deployment Paused Reason Error

- `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

  The deployment's environment was archived.

  - `required Type Type`

    - `"environment_archived_error"EnvironmentArchivedError`

### Beta Managed Agents Environment Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

  The deployment's environment no longer exists.

  - `required Type Type`

    - `"environment_not_found_error"EnvironmentNotFoundError`

### Beta Managed Agents Error Deployment Paused Reason

- `class BetaManagedAgentsErrorDeploymentPausedReason:`

  A scheduled fire recorded a failed run whose error auto-pauses the deployment.

  - `required BetaManagedAgentsDeploymentPausedReasonError Error`

    The error that triggered an auto-pause. Matches the failed run's `error.type`.

    - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

      The deployment's environment was archived.

      - `required Type Type`

        - `"environment_archived_error"EnvironmentArchivedError`

    - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

      The deployment's agent was archived.

      - `required Type Type`

        - `"agent_archived_error"AgentArchivedError`

    - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

      The deployment's environment no longer exists.

      - `required Type Type`

        - `"environment_not_found_error"EnvironmentNotFoundError`

    - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

      A vault referenced by the deployment no longer exists.

      - `required Type Type`

        - `"vault_not_found_error"VaultNotFoundError`

    - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

      A file resource referenced by the deployment no longer exists.

      - `required Type Type`

        - `"file_not_found_error"FileNotFoundError`

    - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

      A referenced resource no longer exists and its kind was not reported.

      - `required Type Type`

        - `"session_resource_not_found_error"SessionResourceNotFoundError`

    - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

      The deployment's workspace was archived.

      - `required Type Type`

        - `"workspace_archived_error"WorkspaceArchivedError`

    - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

      The deployment's organization is disabled.

      - `required Type Type`

        - `"organization_disabled_error"OrganizationDisabledError`

    - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

      A memory store referenced by the deployment is archived.

      - `required Type Type`

        - `"memory_store_archived_error"MemoryStoreArchivedError`

    - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

      A skill referenced by the deployment's agent no longer exists.

      - `required Type Type`

        - `"skill_not_found_error"SkillNotFoundError`

    - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

      A vault referenced by the deployment is archived.

      - `required Type Type`

        - `"vault_archived_error"VaultArchivedError`

    - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

      An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

      - `required Type Type`

        - `"unknown_error"UnknownError`

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `required Type Type`

        - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

    - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `required Type Type`

        - `"mcp_egress_blocked_error"McpEgressBlockedError`

  - `required Type Type`

    - `"error"Error`

### Beta Managed Agents File Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

  A file resource referenced by the deployment no longer exists.

  - `required Type Type`

    - `"file_not_found_error"FileNotFoundError`

### Beta Managed Agents File Resource Config

- `class BetaManagedAgentsFileResourceConfig:`

  A file mounted into each session's container.

  - `required string FileID`

    ID of a previously uploaded file.

  - `required Type Type`

    - `"file"File`

  - `string? MountPath`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

### Beta Managed Agents GitHub Repository Resource Config

- `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

  A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

  - `required Type Type`

    - `"github_repository"GitHubRepository`

  - `required string Url`

    Github URL of the repository

  - `Checkout? Checkout`

    Branch or commit to check out. Defaults to the repository's default branch.

    - `class BetaManagedAgentsBranchCheckout:`

      - `required string Name`

        Branch name to check out.

      - `required Type Type`

        - `"branch"Branch`

    - `class BetaManagedAgentsCommitCheckout:`

      - `required string Sha`

        Full commit SHA to check out.

      - `required Type Type`

        - `"commit"Commit`

  - `string? MountPath`

    Mount path in the container. Defaults to `/workspace/<repo-name>`.

### Beta Managed Agents Manual Deployment Paused Reason

- `class BetaManagedAgentsManualDeploymentPausedReason:`

  The caller invoked the pause endpoint on the deployment.

  - `required Type Type`

    - `"manual"Manual`

### Beta Managed Agents MCP Egress Blocked Deployment Paused Reason Error

- `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

  An MCP server host used by the deployment's agent is blocked by the environment's network policy.

  - `required Type Type`

    - `"mcp_egress_blocked_error"McpEgressBlockedError`

### Beta Managed Agents Memory Store Archived Deployment Paused Reason Error

- `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

  A memory store referenced by the deployment is archived.

  - `required Type Type`

    - `"memory_store_archived_error"MemoryStoreArchivedError`

### Beta Managed Agents Memory Store Resource Config

- `class BetaManagedAgentsMemoryStoreResourceConfig:`

  A memory store attached to each session created from this deployment.

  - `required string MemoryStoreID`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `required Type Type`

    - `"memory_store"MemoryStore`

  - `Access? Access`

    Access mode for an attached memory store.

    - `"read_write"ReadWrite`

    - `"read_only"ReadOnly`

  - `string? Instructions`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Organization Disabled Deployment Paused Reason Error

- `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

  The deployment's organization is disabled.

  - `required Type Type`

    - `"organization_disabled_error"OrganizationDisabledError`

### Beta Managed Agents Schedule

- `class BetaManagedAgentsSchedule:`

  5-field POSIX cron schedule with computed runtime timestamps.

  - `required string Expression`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `required string Timezone`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

  - `required Type Type`

    - `"cron"Cron`

  - `DateTimeOffset? LastRunAt`

    A timestamp in RFC 3339 format

  - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Schedule Params

- `class BetaManagedAgentsScheduleParams:`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `required string Expression`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `required string Timezone`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `required Type Type`

    - `"cron"Cron`

### Beta Managed Agents Self Hosted Resources Unsupported Deployment Paused Reason Error

- `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

  The deployment configures resources, but its environment is self-hosted and cannot mount them.

  - `required Type Type`

    - `"self_hosted_resources_unsupported_error"SelfHostedResourcesUnsupportedError`

### Beta Managed Agents Session Resource Config

- `class BetaManagedAgentsSessionResourceConfig: A class that can be one of several variants.union`

  A configured session resource. Echoes the input minus write-only credentials.

  - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

    A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

    - `required Type Type`

      - `"github_repository"GitHubRepository`

    - `required string Url`

      Github URL of the repository

    - `Checkout? Checkout`

      Branch or commit to check out. Defaults to the repository's default branch.

      - `class BetaManagedAgentsBranchCheckout:`

        - `required string Name`

          Branch name to check out.

        - `required Type Type`

          - `"branch"Branch`

      - `class BetaManagedAgentsCommitCheckout:`

        - `required string Sha`

          Full commit SHA to check out.

        - `required Type Type`

          - `"commit"Commit`

    - `string? MountPath`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

  - `class BetaManagedAgentsFileResourceConfig:`

    A file mounted into each session's container.

    - `required string FileID`

      ID of a previously uploaded file.

    - `required Type Type`

      - `"file"File`

    - `string? MountPath`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  - `class BetaManagedAgentsMemoryStoreResourceConfig:`

    A memory store attached to each session created from this deployment.

    - `required string MemoryStoreID`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `required Type Type`

      - `"memory_store"MemoryStore`

    - `Access? Access`

      Access mode for an attached memory store.

      - `"read_write"ReadWrite`

      - `"read_only"ReadOnly`

    - `string? Instructions`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Session Resource Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

  A referenced resource no longer exists and its kind was not reported.

  - `required Type Type`

    - `"session_resource_not_found_error"SessionResourceNotFoundError`

### Beta Managed Agents Skill Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

  A skill referenced by the deployment's agent no longer exists.

  - `required Type Type`

    - `"skill_not_found_error"SkillNotFoundError`

### Beta Managed Agents Unknown Deployment Paused Reason Error

- `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

  An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

  - `required Type Type`

    - `"unknown_error"UnknownError`

### Beta Managed Agents Vault Archived Deployment Paused Reason Error

- `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

  A vault referenced by the deployment is archived.

  - `required Type Type`

    - `"vault_archived_error"VaultArchivedError`

### Beta Managed Agents Vault Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

  A vault referenced by the deployment no longer exists.

  - `required Type Type`

    - `"vault_not_found_error"VaultNotFoundError`

### Beta Managed Agents Workspace Archived Deployment Paused Reason Error

- `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

  The deployment's workspace was archived.

  - `required Type Type`

    - `"workspace_archived_error"WorkspaceArchivedError`
