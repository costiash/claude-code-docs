# Deployments

## Create Deployment

`client.beta.deployments.create(DeploymentCreateParamsparams, RequestOptionsoptions?): BetaManagedAgentsDeployment`

**post** `/v1/deployments`

Create Deployment

### Parameters

- `params: DeploymentCreateParams`

  - `agent: string | BetaManagedAgentsAgentParams`

    Body param: Agent to deploy. Accepts the `agent` ID string, which pins the latest version, or an `agent` object with both id and version specified. The agent must exist and not be archived.

    - `string`

    - `BetaManagedAgentsAgentParams`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `id: string`

        The `agent` ID.

      - `type: "agent"`

        - `"agent"`

      - `version?: number`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

  - `environment_id: string`

    Body param: ID of the `environment` defining the container configuration for sessions created from this deployment.

  - `initial_events: Array<BetaManagedAgentsDeploymentInitialEventParams>`

    Body param: Events to send to each session immediately after creation. At least 1, maximum 50.

    - `BetaManagedAgentsUserMessageEventParams`

      Parameters for sending a user message to the session.

      - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock>`

        Array of content blocks for the user message.

        - `BetaManagedAgentsTextBlock`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context?: string | null`

            Additional context about the document for the model.

          - `title?: string | null`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

    - `BetaManagedAgentsUserDefineOutcomeEventParams`

      Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubricParams | BetaManagedAgentsTextRubricParams`

        Rubric for grading the quality of an outcome.

        - `BetaManagedAgentsFileRubricParams`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

            - `"file"`

        - `BetaManagedAgentsTextRubricParams`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

          - `type: "text"`

            - `"text"`

      - `type: "user.define_outcome"`

        - `"user.define_outcome"`

      - `max_iterations?: number | null`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `BetaManagedAgentsSystemMessageEventParams`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

      - `content: Array<BetaManagedAgentsSystemContentBlock>`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `type: "system.message"`

        - `"system.message"`

  - `name: string`

    Body param: Human-readable name for the deployment.

  - `description?: string | null`

    Body param: Description of what the deployment does.

  - `metadata?: Record<string, string>`

    Body param: Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `resources?: Array<BetaManagedAgentsGitHubRepositoryResourceParams | BetaManagedAgentsFileResourceParams | BetaManagedAgentsMemoryStoreResourceParam>`

    Body param: Resources (e.g. repositories, files) to mount into each session's container. Maximum 500.

    - `BetaManagedAgentsGitHubRepositoryResourceParams`

      Mount a GitHub repository into the session's container.

      - `authorization_token: string`

        GitHub authorization token used to clone the repository.

      - `type: "github_repository"`

        - `"github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout?: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout | null`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `BetaManagedAgentsBranchCheckout`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `BetaManagedAgentsCommitCheckout`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

      - `mount_path?: string | null`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `BetaManagedAgentsFileResourceParams`

      Mount a file uploaded via the Files API into the session.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

      - `mount_path?: string | null`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `BetaManagedAgentsMemoryStoreResourceParam`

      Parameters for attaching a memory store to an agent session.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access?: "read_write" | "read_only" | null`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions?: string | null`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule?: BetaManagedAgentsScheduleParams | null`

    Body param: 5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: string`

      Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

    - `type: "cron"`

      - `"cron"`

  - `vault_ids?: Array<string>`

    Body param: Vault IDs for stored credentials the agent can use during sessions created from this deployment. Maximum 50.

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

- `BetaManagedAgentsDeployment`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string | null`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: Array<BetaManagedAgentsDeploymentInitialEvent>`

    Events sent to each session immediately after creation.

    - `BetaManagedAgentsDeploymentUserMessageEvent`

      A user message sent to the session.

      - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock>`

        Array of content blocks for the user message.

        - `BetaManagedAgentsTextBlock`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context?: string | null`

            Additional context about the document for the model.

          - `title?: string | null`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

    - `BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `BetaManagedAgentsFileRubric`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

            - `"file"`

        - `BetaManagedAgentsTextRubric`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

            - `"text"`

      - `type: "user.define_outcome"`

        - `"user.define_outcome"`

      - `max_iterations?: number | null`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `BetaManagedAgentsDeploymentSystemMessageEvent`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: Array<BetaManagedAgentsSystemContentBlock>`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `type: "system.message"`

        - `"system.message"`

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsDeploymentPausedReason | null`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `BetaManagedAgentsManualDeploymentPausedReason`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

        - `"manual"`

    - `BetaManagedAgentsErrorDeploymentPausedReason`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

            - `"environment_archived_error"`

        - `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

            - `"agent_archived_error"`

        - `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

            - `"environment_not_found_error"`

        - `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

            - `"vault_not_found_error"`

        - `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

            - `"file_not_found_error"`

        - `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

            - `"session_resource_not_found_error"`

        - `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

            - `"workspace_archived_error"`

        - `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

            - `"organization_disabled_error"`

        - `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

            - `"memory_store_archived_error"`

        - `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

            - `"skill_not_found_error"`

        - `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

            - `"vault_archived_error"`

        - `BetaManagedAgentsUnknownDeploymentPausedReasonError`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

            - `"unknown_error"`

        - `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

            - `"self_hosted_resources_unsupported_error"`

        - `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

            - `"mcp_egress_blocked_error"`

      - `type: "error"`

        - `"error"`

  - `resources: Array<BetaManagedAgentsSessionResourceConfig>`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `BetaManagedAgentsGitHubRepositoryResourceConfig`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

        - `"github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout?: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout | null`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `BetaManagedAgentsBranchCheckout`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `BetaManagedAgentsCommitCheckout`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

      - `mount_path?: string | null`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `BetaManagedAgentsFileResourceConfig`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

      - `mount_path?: string | null`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `BetaManagedAgentsMemoryStoreResourceConfig`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access?: "read_write" | "read_only" | null`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions?: string | null`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: BetaManagedAgentsSchedule | null`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: "cron"`

      - `"cron"`

    - `last_run_at?: string | null`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at?: Array<string>`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

    - `"deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_ids: Array<string>`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsDeployment = await client.beta.deployments.create({
  agent: 'string',
  environment_id: 'x',
  initial_events: [
    { content: [{ text: 'Where is my order #1234?', type: 'text' }], type: 'user.message' },
  ],
  name: 'x',
});

console.log(betaManagedAgentsDeployment.id);
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
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "environment_id": "environment_id",
  "initial_events": [
    {
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {
    "foo": "string"
  },
  "name": "name",
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
    "expression": "x",
    "timezone": "x",
    "type": "cron",
    "last_run_at": "2019-12-27T18:11:19.117Z",
    "upcoming_runs_at": [
      "2019-12-27T18:11:19.117Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "vault_ids": [
    "string"
  ]
}
```

## List Deployments

`client.beta.deployments.list(DeploymentListParamsparams?, RequestOptionsoptions?): PageCursor<BetaManagedAgentsDeployment>`

**get** `/v1/deployments`

List Deployments

### Parameters

- `params: DeploymentListParams`

  - `agent_id?: string`

    Query param: Filter by agent ID.

  - `"created_at[gte]"?: string`

    Query param: Return deployments created at or after this time (inclusive).

  - `"created_at[lte]"?: string`

    Query param: Return deployments created at or before this time (inclusive).

  - `include_archived?: boolean`

    Query param: When true, includes archived deployments. Default: false (exclude archived).

  - `limit?: number`

    Query param: Maximum results per page. Default 20, maximum 100.

  - `page?: string`

    Query param: Opaque pagination cursor.

  - `status?: BetaManagedAgentsDeploymentStatus`

    Query param: Filter by status: active or paused. Omit for both. To include archived deployments, use include_archived instead; the two cannot be combined.

    - `"active"`

    - `"paused"`

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

- `BetaManagedAgentsDeployment`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string | null`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: Array<BetaManagedAgentsDeploymentInitialEvent>`

    Events sent to each session immediately after creation.

    - `BetaManagedAgentsDeploymentUserMessageEvent`

      A user message sent to the session.

      - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock>`

        Array of content blocks for the user message.

        - `BetaManagedAgentsTextBlock`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context?: string | null`

            Additional context about the document for the model.

          - `title?: string | null`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

    - `BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `BetaManagedAgentsFileRubric`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

            - `"file"`

        - `BetaManagedAgentsTextRubric`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

            - `"text"`

      - `type: "user.define_outcome"`

        - `"user.define_outcome"`

      - `max_iterations?: number | null`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `BetaManagedAgentsDeploymentSystemMessageEvent`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: Array<BetaManagedAgentsSystemContentBlock>`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `type: "system.message"`

        - `"system.message"`

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsDeploymentPausedReason | null`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `BetaManagedAgentsManualDeploymentPausedReason`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

        - `"manual"`

    - `BetaManagedAgentsErrorDeploymentPausedReason`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

            - `"environment_archived_error"`

        - `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

            - `"agent_archived_error"`

        - `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

            - `"environment_not_found_error"`

        - `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

            - `"vault_not_found_error"`

        - `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

            - `"file_not_found_error"`

        - `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

            - `"session_resource_not_found_error"`

        - `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

            - `"workspace_archived_error"`

        - `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

            - `"organization_disabled_error"`

        - `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

            - `"memory_store_archived_error"`

        - `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

            - `"skill_not_found_error"`

        - `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

            - `"vault_archived_error"`

        - `BetaManagedAgentsUnknownDeploymentPausedReasonError`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

            - `"unknown_error"`

        - `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

            - `"self_hosted_resources_unsupported_error"`

        - `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

            - `"mcp_egress_blocked_error"`

      - `type: "error"`

        - `"error"`

  - `resources: Array<BetaManagedAgentsSessionResourceConfig>`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `BetaManagedAgentsGitHubRepositoryResourceConfig`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

        - `"github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout?: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout | null`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `BetaManagedAgentsBranchCheckout`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `BetaManagedAgentsCommitCheckout`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

      - `mount_path?: string | null`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `BetaManagedAgentsFileResourceConfig`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

      - `mount_path?: string | null`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `BetaManagedAgentsMemoryStoreResourceConfig`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access?: "read_write" | "read_only" | null`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions?: string | null`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: BetaManagedAgentsSchedule | null`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: "cron"`

      - `"cron"`

    - `last_run_at?: string | null`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at?: Array<string>`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

    - `"deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_ids: Array<string>`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsDeployment of client.beta.deployments.list()) {
  console.log(betaManagedAgentsDeployment.id);
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
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "description": "description",
      "environment_id": "environment_id",
      "initial_events": [
        {
          "content": [
            {
              "text": "Where is my order #1234?",
              "type": "text"
            }
          ],
          "type": "user.message"
        }
      ],
      "metadata": {
        "foo": "string"
      },
      "name": "name",
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
        "expression": "x",
        "timezone": "x",
        "type": "cron",
        "last_run_at": "2019-12-27T18:11:19.117Z",
        "upcoming_runs_at": [
          "2019-12-27T18:11:19.117Z"
        ]
      },
      "status": "active",
      "type": "deployment",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "vault_ids": [
        "string"
      ]
    }
  ],
  "next_page": "next_page"
}
```

## Get Deployment

`client.beta.deployments.retrieve(stringdeploymentID, DeploymentRetrieveParamsparams?, RequestOptionsoptions?): BetaManagedAgentsDeployment`

**get** `/v1/deployments/{deployment_id}`

Get Deployment

### Parameters

- `deploymentID: string`

- `params: DeploymentRetrieveParams`

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

- `BetaManagedAgentsDeployment`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string | null`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: Array<BetaManagedAgentsDeploymentInitialEvent>`

    Events sent to each session immediately after creation.

    - `BetaManagedAgentsDeploymentUserMessageEvent`

      A user message sent to the session.

      - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock>`

        Array of content blocks for the user message.

        - `BetaManagedAgentsTextBlock`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context?: string | null`

            Additional context about the document for the model.

          - `title?: string | null`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

    - `BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `BetaManagedAgentsFileRubric`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

            - `"file"`

        - `BetaManagedAgentsTextRubric`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

            - `"text"`

      - `type: "user.define_outcome"`

        - `"user.define_outcome"`

      - `max_iterations?: number | null`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `BetaManagedAgentsDeploymentSystemMessageEvent`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: Array<BetaManagedAgentsSystemContentBlock>`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `type: "system.message"`

        - `"system.message"`

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsDeploymentPausedReason | null`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `BetaManagedAgentsManualDeploymentPausedReason`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

        - `"manual"`

    - `BetaManagedAgentsErrorDeploymentPausedReason`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

            - `"environment_archived_error"`

        - `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

            - `"agent_archived_error"`

        - `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

            - `"environment_not_found_error"`

        - `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

            - `"vault_not_found_error"`

        - `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

            - `"file_not_found_error"`

        - `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

            - `"session_resource_not_found_error"`

        - `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

            - `"workspace_archived_error"`

        - `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

            - `"organization_disabled_error"`

        - `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

            - `"memory_store_archived_error"`

        - `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

            - `"skill_not_found_error"`

        - `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

            - `"vault_archived_error"`

        - `BetaManagedAgentsUnknownDeploymentPausedReasonError`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

            - `"unknown_error"`

        - `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

            - `"self_hosted_resources_unsupported_error"`

        - `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

            - `"mcp_egress_blocked_error"`

      - `type: "error"`

        - `"error"`

  - `resources: Array<BetaManagedAgentsSessionResourceConfig>`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `BetaManagedAgentsGitHubRepositoryResourceConfig`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

        - `"github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout?: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout | null`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `BetaManagedAgentsBranchCheckout`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `BetaManagedAgentsCommitCheckout`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

      - `mount_path?: string | null`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `BetaManagedAgentsFileResourceConfig`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

      - `mount_path?: string | null`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `BetaManagedAgentsMemoryStoreResourceConfig`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access?: "read_write" | "read_only" | null`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions?: string | null`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: BetaManagedAgentsSchedule | null`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: "cron"`

      - `"cron"`

    - `last_run_at?: string | null`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at?: Array<string>`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

    - `"deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_ids: Array<string>`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsDeployment = await client.beta.deployments.retrieve('deployment_id');

console.log(betaManagedAgentsDeployment.id);
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
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "environment_id": "environment_id",
  "initial_events": [
    {
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {
    "foo": "string"
  },
  "name": "name",
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
    "expression": "x",
    "timezone": "x",
    "type": "cron",
    "last_run_at": "2019-12-27T18:11:19.117Z",
    "upcoming_runs_at": [
      "2019-12-27T18:11:19.117Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "vault_ids": [
    "string"
  ]
}
```

## Update Deployment

`client.beta.deployments.update(stringdeploymentID, DeploymentUpdateParamsparams, RequestOptionsoptions?): BetaManagedAgentsDeployment`

**post** `/v1/deployments/{deployment_id}`

Update Deployment

### Parameters

- `deploymentID: string`

- `params: DeploymentUpdateParams`

  - `agent?: string | BetaManagedAgentsAgentParams`

    Body param: Agent to deploy. Accepts the `agent` ID string, which re-pins to the latest version, or an `agent` object with both id and version specified. Omit to preserve. Cannot be cleared.

    - `string`

    - `BetaManagedAgentsAgentParams`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `id: string`

        The `agent` ID.

      - `type: "agent"`

        - `"agent"`

      - `version?: number`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

  - `description?: string | null`

    Body param: Description. Omit to preserve; send empty string or null to clear.

  - `environment_id?: string`

    Body param: ID of the `environment` where sessions run. Omit to preserve. Cannot be cleared.

  - `initial_events?: Array<BetaManagedAgentsDeploymentInitialEventParams>`

    Body param: Initial events. Full replacement. Omit to preserve. Cannot be cleared. At least 1, maximum 50.

    - `BetaManagedAgentsUserMessageEventParams`

      Parameters for sending a user message to the session.

      - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock>`

        Array of content blocks for the user message.

        - `BetaManagedAgentsTextBlock`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context?: string | null`

            Additional context about the document for the model.

          - `title?: string | null`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

    - `BetaManagedAgentsUserDefineOutcomeEventParams`

      Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubricParams | BetaManagedAgentsTextRubricParams`

        Rubric for grading the quality of an outcome.

        - `BetaManagedAgentsFileRubricParams`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

            - `"file"`

        - `BetaManagedAgentsTextRubricParams`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

          - `type: "text"`

            - `"text"`

      - `type: "user.define_outcome"`

        - `"user.define_outcome"`

      - `max_iterations?: number | null`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `BetaManagedAgentsSystemMessageEventParams`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

      - `content: Array<BetaManagedAgentsSystemContentBlock>`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `type: "system.message"`

        - `"system.message"`

  - `metadata?: Record<string, string | null> | null`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `name?: string`

    Body param: Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

  - `resources?: Array<BetaManagedAgentsGitHubRepositoryResourceParams | BetaManagedAgentsFileResourceParams | BetaManagedAgentsMemoryStoreResourceParam> | null`

    Body param: Session resources. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 500.

    - `BetaManagedAgentsGitHubRepositoryResourceParams`

      Mount a GitHub repository into the session's container.

      - `authorization_token: string`

        GitHub authorization token used to clone the repository.

      - `type: "github_repository"`

        - `"github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout?: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout | null`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `BetaManagedAgentsBranchCheckout`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `BetaManagedAgentsCommitCheckout`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

      - `mount_path?: string | null`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `BetaManagedAgentsFileResourceParams`

      Mount a file uploaded via the Files API into the session.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

      - `mount_path?: string | null`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `BetaManagedAgentsMemoryStoreResourceParam`

      Parameters for attaching a memory store to an agent session.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access?: "read_write" | "read_only" | null`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions?: string | null`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule?: BetaManagedAgentsScheduleParams | null`

    Body param: 5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: string`

      Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

    - `type: "cron"`

      - `"cron"`

  - `vault_ids?: Array<string> | null`

    Body param: Vault IDs. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 50.

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

- `BetaManagedAgentsDeployment`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string | null`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: Array<BetaManagedAgentsDeploymentInitialEvent>`

    Events sent to each session immediately after creation.

    - `BetaManagedAgentsDeploymentUserMessageEvent`

      A user message sent to the session.

      - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock>`

        Array of content blocks for the user message.

        - `BetaManagedAgentsTextBlock`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context?: string | null`

            Additional context about the document for the model.

          - `title?: string | null`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

    - `BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `BetaManagedAgentsFileRubric`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

            - `"file"`

        - `BetaManagedAgentsTextRubric`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

            - `"text"`

      - `type: "user.define_outcome"`

        - `"user.define_outcome"`

      - `max_iterations?: number | null`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `BetaManagedAgentsDeploymentSystemMessageEvent`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: Array<BetaManagedAgentsSystemContentBlock>`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `type: "system.message"`

        - `"system.message"`

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsDeploymentPausedReason | null`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `BetaManagedAgentsManualDeploymentPausedReason`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

        - `"manual"`

    - `BetaManagedAgentsErrorDeploymentPausedReason`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

            - `"environment_archived_error"`

        - `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

            - `"agent_archived_error"`

        - `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

            - `"environment_not_found_error"`

        - `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

            - `"vault_not_found_error"`

        - `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

            - `"file_not_found_error"`

        - `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

            - `"session_resource_not_found_error"`

        - `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

            - `"workspace_archived_error"`

        - `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

            - `"organization_disabled_error"`

        - `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

            - `"memory_store_archived_error"`

        - `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

            - `"skill_not_found_error"`

        - `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

            - `"vault_archived_error"`

        - `BetaManagedAgentsUnknownDeploymentPausedReasonError`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

            - `"unknown_error"`

        - `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

            - `"self_hosted_resources_unsupported_error"`

        - `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

            - `"mcp_egress_blocked_error"`

      - `type: "error"`

        - `"error"`

  - `resources: Array<BetaManagedAgentsSessionResourceConfig>`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `BetaManagedAgentsGitHubRepositoryResourceConfig`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

        - `"github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout?: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout | null`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `BetaManagedAgentsBranchCheckout`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `BetaManagedAgentsCommitCheckout`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

      - `mount_path?: string | null`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `BetaManagedAgentsFileResourceConfig`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

      - `mount_path?: string | null`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `BetaManagedAgentsMemoryStoreResourceConfig`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access?: "read_write" | "read_only" | null`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions?: string | null`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: BetaManagedAgentsSchedule | null`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: "cron"`

      - `"cron"`

    - `last_run_at?: string | null`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at?: Array<string>`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

    - `"deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_ids: Array<string>`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsDeployment = await client.beta.deployments.update('deployment_id');

console.log(betaManagedAgentsDeployment.id);
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
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "environment_id": "environment_id",
  "initial_events": [
    {
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {
    "foo": "string"
  },
  "name": "name",
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
    "expression": "x",
    "timezone": "x",
    "type": "cron",
    "last_run_at": "2019-12-27T18:11:19.117Z",
    "upcoming_runs_at": [
      "2019-12-27T18:11:19.117Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "vault_ids": [
    "string"
  ]
}
```

## Archive Deployment

`client.beta.deployments.archive(stringdeploymentID, DeploymentArchiveParamsparams?, RequestOptionsoptions?): BetaManagedAgentsDeployment`

**post** `/v1/deployments/{deployment_id}/archive`

Archive Deployment

### Parameters

- `deploymentID: string`

- `params: DeploymentArchiveParams`

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

- `BetaManagedAgentsDeployment`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string | null`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: Array<BetaManagedAgentsDeploymentInitialEvent>`

    Events sent to each session immediately after creation.

    - `BetaManagedAgentsDeploymentUserMessageEvent`

      A user message sent to the session.

      - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock>`

        Array of content blocks for the user message.

        - `BetaManagedAgentsTextBlock`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context?: string | null`

            Additional context about the document for the model.

          - `title?: string | null`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

    - `BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `BetaManagedAgentsFileRubric`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

            - `"file"`

        - `BetaManagedAgentsTextRubric`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

            - `"text"`

      - `type: "user.define_outcome"`

        - `"user.define_outcome"`

      - `max_iterations?: number | null`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `BetaManagedAgentsDeploymentSystemMessageEvent`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: Array<BetaManagedAgentsSystemContentBlock>`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `type: "system.message"`

        - `"system.message"`

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsDeploymentPausedReason | null`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `BetaManagedAgentsManualDeploymentPausedReason`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

        - `"manual"`

    - `BetaManagedAgentsErrorDeploymentPausedReason`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

            - `"environment_archived_error"`

        - `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

            - `"agent_archived_error"`

        - `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

            - `"environment_not_found_error"`

        - `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

            - `"vault_not_found_error"`

        - `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

            - `"file_not_found_error"`

        - `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

            - `"session_resource_not_found_error"`

        - `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

            - `"workspace_archived_error"`

        - `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

            - `"organization_disabled_error"`

        - `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

            - `"memory_store_archived_error"`

        - `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

            - `"skill_not_found_error"`

        - `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

            - `"vault_archived_error"`

        - `BetaManagedAgentsUnknownDeploymentPausedReasonError`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

            - `"unknown_error"`

        - `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

            - `"self_hosted_resources_unsupported_error"`

        - `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

            - `"mcp_egress_blocked_error"`

      - `type: "error"`

        - `"error"`

  - `resources: Array<BetaManagedAgentsSessionResourceConfig>`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `BetaManagedAgentsGitHubRepositoryResourceConfig`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

        - `"github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout?: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout | null`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `BetaManagedAgentsBranchCheckout`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `BetaManagedAgentsCommitCheckout`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

      - `mount_path?: string | null`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `BetaManagedAgentsFileResourceConfig`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

      - `mount_path?: string | null`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `BetaManagedAgentsMemoryStoreResourceConfig`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access?: "read_write" | "read_only" | null`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions?: string | null`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: BetaManagedAgentsSchedule | null`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: "cron"`

      - `"cron"`

    - `last_run_at?: string | null`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at?: Array<string>`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

    - `"deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_ids: Array<string>`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsDeployment = await client.beta.deployments.archive('deployment_id');

console.log(betaManagedAgentsDeployment.id);
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
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "environment_id": "environment_id",
  "initial_events": [
    {
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {
    "foo": "string"
  },
  "name": "name",
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
    "expression": "x",
    "timezone": "x",
    "type": "cron",
    "last_run_at": "2019-12-27T18:11:19.117Z",
    "upcoming_runs_at": [
      "2019-12-27T18:11:19.117Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "vault_ids": [
    "string"
  ]
}
```

## Run Deployment Now

`client.beta.deployments.run(stringdeploymentID, DeploymentRunParamsparams?, RequestOptionsoptions?): BetaManagedAgentsDeploymentRun`

**post** `/v1/deployments/{deployment_id}/run`

Run Deployment Now

### Parameters

- `deploymentID: string`

- `params: DeploymentRunParams`

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

const betaManagedAgentsDeploymentRun = await client.beta.deployments.run('deployment_id');

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

## Pause Deployment

`client.beta.deployments.pause(stringdeploymentID, DeploymentPauseParamsparams?, RequestOptionsoptions?): BetaManagedAgentsDeployment`

**post** `/v1/deployments/{deployment_id}/pause`

Pause Deployment

### Parameters

- `deploymentID: string`

- `params: DeploymentPauseParams`

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

- `BetaManagedAgentsDeployment`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string | null`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: Array<BetaManagedAgentsDeploymentInitialEvent>`

    Events sent to each session immediately after creation.

    - `BetaManagedAgentsDeploymentUserMessageEvent`

      A user message sent to the session.

      - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock>`

        Array of content blocks for the user message.

        - `BetaManagedAgentsTextBlock`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context?: string | null`

            Additional context about the document for the model.

          - `title?: string | null`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

    - `BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `BetaManagedAgentsFileRubric`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

            - `"file"`

        - `BetaManagedAgentsTextRubric`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

            - `"text"`

      - `type: "user.define_outcome"`

        - `"user.define_outcome"`

      - `max_iterations?: number | null`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `BetaManagedAgentsDeploymentSystemMessageEvent`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: Array<BetaManagedAgentsSystemContentBlock>`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `type: "system.message"`

        - `"system.message"`

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsDeploymentPausedReason | null`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `BetaManagedAgentsManualDeploymentPausedReason`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

        - `"manual"`

    - `BetaManagedAgentsErrorDeploymentPausedReason`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

            - `"environment_archived_error"`

        - `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

            - `"agent_archived_error"`

        - `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

            - `"environment_not_found_error"`

        - `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

            - `"vault_not_found_error"`

        - `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

            - `"file_not_found_error"`

        - `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

            - `"session_resource_not_found_error"`

        - `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

            - `"workspace_archived_error"`

        - `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

            - `"organization_disabled_error"`

        - `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

            - `"memory_store_archived_error"`

        - `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

            - `"skill_not_found_error"`

        - `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

            - `"vault_archived_error"`

        - `BetaManagedAgentsUnknownDeploymentPausedReasonError`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

            - `"unknown_error"`

        - `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

            - `"self_hosted_resources_unsupported_error"`

        - `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

            - `"mcp_egress_blocked_error"`

      - `type: "error"`

        - `"error"`

  - `resources: Array<BetaManagedAgentsSessionResourceConfig>`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `BetaManagedAgentsGitHubRepositoryResourceConfig`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

        - `"github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout?: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout | null`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `BetaManagedAgentsBranchCheckout`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `BetaManagedAgentsCommitCheckout`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

      - `mount_path?: string | null`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `BetaManagedAgentsFileResourceConfig`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

      - `mount_path?: string | null`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `BetaManagedAgentsMemoryStoreResourceConfig`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access?: "read_write" | "read_only" | null`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions?: string | null`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: BetaManagedAgentsSchedule | null`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: "cron"`

      - `"cron"`

    - `last_run_at?: string | null`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at?: Array<string>`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

    - `"deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_ids: Array<string>`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsDeployment = await client.beta.deployments.pause('deployment_id');

console.log(betaManagedAgentsDeployment.id);
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
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "environment_id": "environment_id",
  "initial_events": [
    {
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {
    "foo": "string"
  },
  "name": "name",
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
    "expression": "x",
    "timezone": "x",
    "type": "cron",
    "last_run_at": "2019-12-27T18:11:19.117Z",
    "upcoming_runs_at": [
      "2019-12-27T18:11:19.117Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "vault_ids": [
    "string"
  ]
}
```

## Unpause Deployment

`client.beta.deployments.unpause(stringdeploymentID, DeploymentUnpauseParamsparams?, RequestOptionsoptions?): BetaManagedAgentsDeployment`

**post** `/v1/deployments/{deployment_id}/unpause`

Unpause Deployment

### Parameters

- `deploymentID: string`

- `params: DeploymentUnpauseParams`

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

- `BetaManagedAgentsDeployment`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string | null`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: Array<BetaManagedAgentsDeploymentInitialEvent>`

    Events sent to each session immediately after creation.

    - `BetaManagedAgentsDeploymentUserMessageEvent`

      A user message sent to the session.

      - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock>`

        Array of content blocks for the user message.

        - `BetaManagedAgentsTextBlock`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context?: string | null`

            Additional context about the document for the model.

          - `title?: string | null`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

    - `BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `BetaManagedAgentsFileRubric`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

            - `"file"`

        - `BetaManagedAgentsTextRubric`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

            - `"text"`

      - `type: "user.define_outcome"`

        - `"user.define_outcome"`

      - `max_iterations?: number | null`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `BetaManagedAgentsDeploymentSystemMessageEvent`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: Array<BetaManagedAgentsSystemContentBlock>`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `type: "system.message"`

        - `"system.message"`

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsDeploymentPausedReason | null`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `BetaManagedAgentsManualDeploymentPausedReason`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

        - `"manual"`

    - `BetaManagedAgentsErrorDeploymentPausedReason`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

            - `"environment_archived_error"`

        - `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

            - `"agent_archived_error"`

        - `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

            - `"environment_not_found_error"`

        - `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

            - `"vault_not_found_error"`

        - `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

            - `"file_not_found_error"`

        - `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

            - `"session_resource_not_found_error"`

        - `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

            - `"workspace_archived_error"`

        - `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

            - `"organization_disabled_error"`

        - `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

            - `"memory_store_archived_error"`

        - `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

            - `"skill_not_found_error"`

        - `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

            - `"vault_archived_error"`

        - `BetaManagedAgentsUnknownDeploymentPausedReasonError`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

            - `"unknown_error"`

        - `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

            - `"self_hosted_resources_unsupported_error"`

        - `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

            - `"mcp_egress_blocked_error"`

      - `type: "error"`

        - `"error"`

  - `resources: Array<BetaManagedAgentsSessionResourceConfig>`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `BetaManagedAgentsGitHubRepositoryResourceConfig`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

        - `"github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout?: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout | null`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `BetaManagedAgentsBranchCheckout`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `BetaManagedAgentsCommitCheckout`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

      - `mount_path?: string | null`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `BetaManagedAgentsFileResourceConfig`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

      - `mount_path?: string | null`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `BetaManagedAgentsMemoryStoreResourceConfig`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access?: "read_write" | "read_only" | null`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions?: string | null`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: BetaManagedAgentsSchedule | null`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: "cron"`

      - `"cron"`

    - `last_run_at?: string | null`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at?: Array<string>`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

    - `"deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_ids: Array<string>`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsDeployment = await client.beta.deployments.unpause('deployment_id');

console.log(betaManagedAgentsDeployment.id);
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
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "environment_id": "environment_id",
  "initial_events": [
    {
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {
    "foo": "string"
  },
  "name": "name",
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
    "expression": "x",
    "timezone": "x",
    "type": "cron",
    "last_run_at": "2019-12-27T18:11:19.117Z",
    "upcoming_runs_at": [
      "2019-12-27T18:11:19.117Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "vault_ids": [
    "string"
  ]
}
```

## Domain Types

### Beta Managed Agents Agent Archived Deployment Paused Reason Error

- `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

  The deployment's agent was archived.

  - `type: "agent_archived_error"`

    - `"agent_archived_error"`

### Beta Managed Agents Cron Schedule

- `BetaManagedAgentsCronSchedule`

  5-field POSIX cron schedule with computed runtime timestamps.

  - `expression: string`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `timezone: string`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

  - `type: "cron"`

    - `"cron"`

  - `last_run_at?: string | null`

    A timestamp in RFC 3339 format

  - `upcoming_runs_at?: Array<string>`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Cron Schedule Params

- `BetaManagedAgentsCronScheduleParams`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `expression: string`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `timezone: string`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `type: "cron"`

    - `"cron"`

### Beta Managed Agents Deployment

- `BetaManagedAgentsDeployment`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string | null`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: Array<BetaManagedAgentsDeploymentInitialEvent>`

    Events sent to each session immediately after creation.

    - `BetaManagedAgentsDeploymentUserMessageEvent`

      A user message sent to the session.

      - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock>`

        Array of content blocks for the user message.

        - `BetaManagedAgentsTextBlock`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context?: string | null`

            Additional context about the document for the model.

          - `title?: string | null`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

    - `BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `BetaManagedAgentsFileRubric`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

            - `"file"`

        - `BetaManagedAgentsTextRubric`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

            - `"text"`

      - `type: "user.define_outcome"`

        - `"user.define_outcome"`

      - `max_iterations?: number | null`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `BetaManagedAgentsDeploymentSystemMessageEvent`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: Array<BetaManagedAgentsSystemContentBlock>`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `type: "system.message"`

        - `"system.message"`

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsDeploymentPausedReason | null`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `BetaManagedAgentsManualDeploymentPausedReason`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

        - `"manual"`

    - `BetaManagedAgentsErrorDeploymentPausedReason`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

            - `"environment_archived_error"`

        - `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

            - `"agent_archived_error"`

        - `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

            - `"environment_not_found_error"`

        - `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

            - `"vault_not_found_error"`

        - `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

            - `"file_not_found_error"`

        - `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

            - `"session_resource_not_found_error"`

        - `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

            - `"workspace_archived_error"`

        - `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

            - `"organization_disabled_error"`

        - `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

            - `"memory_store_archived_error"`

        - `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

            - `"skill_not_found_error"`

        - `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

            - `"vault_archived_error"`

        - `BetaManagedAgentsUnknownDeploymentPausedReasonError`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

            - `"unknown_error"`

        - `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

            - `"self_hosted_resources_unsupported_error"`

        - `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

            - `"mcp_egress_blocked_error"`

      - `type: "error"`

        - `"error"`

  - `resources: Array<BetaManagedAgentsSessionResourceConfig>`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `BetaManagedAgentsGitHubRepositoryResourceConfig`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

        - `"github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout?: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout | null`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `BetaManagedAgentsBranchCheckout`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `BetaManagedAgentsCommitCheckout`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

      - `mount_path?: string | null`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `BetaManagedAgentsFileResourceConfig`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

      - `mount_path?: string | null`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `BetaManagedAgentsMemoryStoreResourceConfig`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access?: "read_write" | "read_only" | null`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions?: string | null`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: BetaManagedAgentsSchedule | null`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: "cron"`

      - `"cron"`

    - `last_run_at?: string | null`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at?: Array<string>`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

    - `"deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_ids: Array<string>`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Beta Managed Agents Deployment Initial Event

- `BetaManagedAgentsDeploymentInitialEvent = BetaManagedAgentsDeploymentUserMessageEvent | BetaManagedAgentsDeploymentUserDefineOutcomeEvent | BetaManagedAgentsDeploymentSystemMessageEvent`

  An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

  - `BetaManagedAgentsDeploymentUserMessageEvent`

    A user message sent to the session.

    - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock>`

      Array of content blocks for the user message.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context?: string | null`

          Additional context about the document for the model.

        - `title?: string | null`

          The title of the document.

    - `type: "user.message"`

      - `"user.message"`

  - `BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

    An outcome the agent should work toward. The agent begins work on receipt.

    - `description: string`

      What the agent should produce. This is the task specification.

    - `rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric`

      Rubric for grading the quality of an outcome.

      - `BetaManagedAgentsFileRubric`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: string`

          ID of the rubric file.

        - `type: "file"`

          - `"file"`

      - `BetaManagedAgentsTextRubric`

        Rubric content provided inline as text.

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: "text"`

          - `"text"`

    - `type: "user.define_outcome"`

      - `"user.define_outcome"`

    - `max_iterations?: number | null`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `BetaManagedAgentsDeploymentSystemMessageEvent`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

    - `content: Array<BetaManagedAgentsSystemContentBlock>`

      System content blocks to append. Text-only.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `type: "system.message"`

      - `"system.message"`

### Beta Managed Agents Deployment Initial Event Params

- `BetaManagedAgentsDeploymentInitialEventParams = BetaManagedAgentsUserMessageEventParams | BetaManagedAgentsUserDefineOutcomeEventParams | BetaManagedAgentsSystemMessageEventParams`

  An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

  - `BetaManagedAgentsUserMessageEventParams`

    Parameters for sending a user message to the session.

    - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock>`

      Array of content blocks for the user message.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context?: string | null`

          Additional context about the document for the model.

        - `title?: string | null`

          The title of the document.

    - `type: "user.message"`

      - `"user.message"`

  - `BetaManagedAgentsUserDefineOutcomeEventParams`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `description: string`

      What the agent should produce. This is the task specification.

    - `rubric: BetaManagedAgentsFileRubricParams | BetaManagedAgentsTextRubricParams`

      Rubric for grading the quality of an outcome.

      - `BetaManagedAgentsFileRubricParams`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: string`

          ID of the rubric file.

        - `type: "file"`

          - `"file"`

      - `BetaManagedAgentsTextRubricParams`

        Rubric content provided inline as text.

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

        - `type: "text"`

          - `"text"`

    - `type: "user.define_outcome"`

      - `"user.define_outcome"`

    - `max_iterations?: number | null`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `BetaManagedAgentsSystemMessageEventParams`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `content: Array<BetaManagedAgentsSystemContentBlock>`

      System content blocks to append. Text-only.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `type: "system.message"`

      - `"system.message"`

### Beta Managed Agents Deployment Paused Reason

- `BetaManagedAgentsDeploymentPausedReason = BetaManagedAgentsManualDeploymentPausedReason | BetaManagedAgentsErrorDeploymentPausedReason`

  Why a deployment is paused. Non-null exactly when `status` is `paused`.

  - `BetaManagedAgentsManualDeploymentPausedReason`

    The caller invoked the pause endpoint on the deployment.

    - `type: "manual"`

      - `"manual"`

  - `BetaManagedAgentsErrorDeploymentPausedReason`

    A scheduled fire recorded a failed run whose error auto-pauses the deployment.

    - `error: BetaManagedAgentsDeploymentPausedReasonError`

      The error that triggered an auto-pause. Matches the failed run's `error.type`.

      - `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

        The deployment's environment was archived.

        - `type: "environment_archived_error"`

          - `"environment_archived_error"`

      - `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

        The deployment's agent was archived.

        - `type: "agent_archived_error"`

          - `"agent_archived_error"`

      - `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

        The deployment's environment no longer exists.

        - `type: "environment_not_found_error"`

          - `"environment_not_found_error"`

      - `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

        A vault referenced by the deployment no longer exists.

        - `type: "vault_not_found_error"`

          - `"vault_not_found_error"`

      - `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

        A file resource referenced by the deployment no longer exists.

        - `type: "file_not_found_error"`

          - `"file_not_found_error"`

      - `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

        A referenced resource no longer exists and its kind was not reported.

        - `type: "session_resource_not_found_error"`

          - `"session_resource_not_found_error"`

      - `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

        The deployment's workspace was archived.

        - `type: "workspace_archived_error"`

          - `"workspace_archived_error"`

      - `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

        The deployment's organization is disabled.

        - `type: "organization_disabled_error"`

          - `"organization_disabled_error"`

      - `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

        A memory store referenced by the deployment is archived.

        - `type: "memory_store_archived_error"`

          - `"memory_store_archived_error"`

      - `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

        A skill referenced by the deployment's agent no longer exists.

        - `type: "skill_not_found_error"`

          - `"skill_not_found_error"`

      - `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

        A vault referenced by the deployment is archived.

        - `type: "vault_archived_error"`

          - `"vault_archived_error"`

      - `BetaManagedAgentsUnknownDeploymentPausedReasonError`

        An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

        - `type: "unknown_error"`

          - `"unknown_error"`

      - `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

        The deployment configures resources, but its environment is self-hosted and cannot mount them.

        - `type: "self_hosted_resources_unsupported_error"`

          - `"self_hosted_resources_unsupported_error"`

      - `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

        An MCP server host used by the deployment's agent is blocked by the environment's network policy.

        - `type: "mcp_egress_blocked_error"`

          - `"mcp_egress_blocked_error"`

    - `type: "error"`

      - `"error"`

### Beta Managed Agents Deployment Paused Reason Error

- `BetaManagedAgentsDeploymentPausedReasonError = BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError | BetaManagedAgentsAgentArchivedDeploymentPausedReasonError | BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError | 11 more`

  The error that triggered an auto-pause. Matches the failed run's `error.type`.

  - `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

    The deployment's environment was archived.

    - `type: "environment_archived_error"`

      - `"environment_archived_error"`

  - `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

    The deployment's agent was archived.

    - `type: "agent_archived_error"`

      - `"agent_archived_error"`

  - `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

    The deployment's environment no longer exists.

    - `type: "environment_not_found_error"`

      - `"environment_not_found_error"`

  - `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

    A vault referenced by the deployment no longer exists.

    - `type: "vault_not_found_error"`

      - `"vault_not_found_error"`

  - `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

    A file resource referenced by the deployment no longer exists.

    - `type: "file_not_found_error"`

      - `"file_not_found_error"`

  - `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

    A referenced resource no longer exists and its kind was not reported.

    - `type: "session_resource_not_found_error"`

      - `"session_resource_not_found_error"`

  - `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

    The deployment's workspace was archived.

    - `type: "workspace_archived_error"`

      - `"workspace_archived_error"`

  - `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

    The deployment's organization is disabled.

    - `type: "organization_disabled_error"`

      - `"organization_disabled_error"`

  - `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

    A memory store referenced by the deployment is archived.

    - `type: "memory_store_archived_error"`

      - `"memory_store_archived_error"`

  - `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

    A skill referenced by the deployment's agent no longer exists.

    - `type: "skill_not_found_error"`

      - `"skill_not_found_error"`

  - `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

    A vault referenced by the deployment is archived.

    - `type: "vault_archived_error"`

      - `"vault_archived_error"`

  - `BetaManagedAgentsUnknownDeploymentPausedReasonError`

    An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

    - `type: "unknown_error"`

      - `"unknown_error"`

  - `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

    The deployment configures resources, but its environment is self-hosted and cannot mount them.

    - `type: "self_hosted_resources_unsupported_error"`

      - `"self_hosted_resources_unsupported_error"`

  - `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

    An MCP server host used by the deployment's agent is blocked by the environment's network policy.

    - `type: "mcp_egress_blocked_error"`

      - `"mcp_egress_blocked_error"`

### Beta Managed Agents Deployment Status

- `BetaManagedAgentsDeploymentStatus = "active" | "paused"`

  Lifecycle status of a deployment.

  - `"active"`

  - `"paused"`

### Beta Managed Agents Deployment System Message Event

- `BetaManagedAgentsDeploymentSystemMessageEvent`

  Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

  - `content: Array<BetaManagedAgentsSystemContentBlock>`

    System content blocks to append. Text-only.

    - `text: string`

      The text content.

    - `type: "text"`

      - `"text"`

  - `type: "system.message"`

    - `"system.message"`

### Beta Managed Agents Deployment User Define Outcome Event

- `BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

  An outcome the agent should work toward. The agent begins work on receipt.

  - `description: string`

    What the agent should produce. This is the task specification.

  - `rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric`

    Rubric for grading the quality of an outcome.

    - `BetaManagedAgentsFileRubric`

      Rubric referenced by a file uploaded via the Files API.

      - `file_id: string`

        ID of the rubric file.

      - `type: "file"`

        - `"file"`

    - `BetaManagedAgentsTextRubric`

      Rubric content provided inline as text.

      - `content: string`

        Rubric content. Plain text or markdown — the grader treats it as freeform text.

      - `type: "text"`

        - `"text"`

  - `type: "user.define_outcome"`

    - `"user.define_outcome"`

  - `max_iterations?: number | null`

    Eval→revision cycles before giving up. Default 3, max 20.

### Beta Managed Agents Deployment User Message Event

- `BetaManagedAgentsDeploymentUserMessageEvent`

  A user message sent to the session.

  - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock>`

    Array of content blocks for the user message.

    - `BetaManagedAgentsTextBlock`

      Regular text content.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `BetaManagedAgentsImageBlock`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `BetaManagedAgentsBase64ImageSource`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: "base64"`

            - `"base64"`

        - `BetaManagedAgentsURLImageSource`

          Image referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the image to fetch.

        - `BetaManagedAgentsFileImageSource`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "image"`

        - `"image"`

    - `BetaManagedAgentsDocumentBlock`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `BetaManagedAgentsBase64DocumentSource`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

          - `type: "base64"`

            - `"base64"`

        - `BetaManagedAgentsPlainTextDocumentSource`

          Plain text document content.

          - `data: string`

            The plain text content.

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsURLDocumentSource`

          Document referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the document to fetch.

        - `BetaManagedAgentsFileDocumentSource`

          Document referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "document"`

        - `"document"`

      - `context?: string | null`

        Additional context about the document for the model.

      - `title?: string | null`

        The title of the document.

  - `type: "user.message"`

    - `"user.message"`

### Beta Managed Agents Environment Archived Deployment Paused Reason Error

- `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

  The deployment's environment was archived.

  - `type: "environment_archived_error"`

    - `"environment_archived_error"`

### Beta Managed Agents Environment Not Found Deployment Paused Reason Error

- `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

  The deployment's environment no longer exists.

  - `type: "environment_not_found_error"`

    - `"environment_not_found_error"`

### Beta Managed Agents Error Deployment Paused Reason

- `BetaManagedAgentsErrorDeploymentPausedReason`

  A scheduled fire recorded a failed run whose error auto-pauses the deployment.

  - `error: BetaManagedAgentsDeploymentPausedReasonError`

    The error that triggered an auto-pause. Matches the failed run's `error.type`.

    - `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

      The deployment's environment was archived.

      - `type: "environment_archived_error"`

        - `"environment_archived_error"`

    - `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

      The deployment's agent was archived.

      - `type: "agent_archived_error"`

        - `"agent_archived_error"`

    - `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

      The deployment's environment no longer exists.

      - `type: "environment_not_found_error"`

        - `"environment_not_found_error"`

    - `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

      A vault referenced by the deployment no longer exists.

      - `type: "vault_not_found_error"`

        - `"vault_not_found_error"`

    - `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

      A file resource referenced by the deployment no longer exists.

      - `type: "file_not_found_error"`

        - `"file_not_found_error"`

    - `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

      A referenced resource no longer exists and its kind was not reported.

      - `type: "session_resource_not_found_error"`

        - `"session_resource_not_found_error"`

    - `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

      The deployment's workspace was archived.

      - `type: "workspace_archived_error"`

        - `"workspace_archived_error"`

    - `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

      The deployment's organization is disabled.

      - `type: "organization_disabled_error"`

        - `"organization_disabled_error"`

    - `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

      A memory store referenced by the deployment is archived.

      - `type: "memory_store_archived_error"`

        - `"memory_store_archived_error"`

    - `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

      A skill referenced by the deployment's agent no longer exists.

      - `type: "skill_not_found_error"`

        - `"skill_not_found_error"`

    - `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

      A vault referenced by the deployment is archived.

      - `type: "vault_archived_error"`

        - `"vault_archived_error"`

    - `BetaManagedAgentsUnknownDeploymentPausedReasonError`

      An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

      - `type: "unknown_error"`

        - `"unknown_error"`

    - `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `type: "self_hosted_resources_unsupported_error"`

        - `"self_hosted_resources_unsupported_error"`

    - `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `type: "mcp_egress_blocked_error"`

        - `"mcp_egress_blocked_error"`

  - `type: "error"`

    - `"error"`

### Beta Managed Agents File Not Found Deployment Paused Reason Error

- `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

  A file resource referenced by the deployment no longer exists.

  - `type: "file_not_found_error"`

    - `"file_not_found_error"`

### Beta Managed Agents File Resource Config

- `BetaManagedAgentsFileResourceConfig`

  A file mounted into each session's container.

  - `file_id: string`

    ID of a previously uploaded file.

  - `type: "file"`

    - `"file"`

  - `mount_path?: string | null`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

### Beta Managed Agents GitHub Repository Resource Config

- `BetaManagedAgentsGitHubRepositoryResourceConfig`

  A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

  - `type: "github_repository"`

    - `"github_repository"`

  - `url: string`

    Github URL of the repository

  - `checkout?: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout | null`

    Branch or commit to check out. Defaults to the repository's default branch.

    - `BetaManagedAgentsBranchCheckout`

      - `name: string`

        Branch name to check out.

      - `type: "branch"`

        - `"branch"`

    - `BetaManagedAgentsCommitCheckout`

      - `sha: string`

        Full commit SHA to check out.

      - `type: "commit"`

        - `"commit"`

  - `mount_path?: string | null`

    Mount path in the container. Defaults to `/workspace/<repo-name>`.

### Beta Managed Agents Manual Deployment Paused Reason

- `BetaManagedAgentsManualDeploymentPausedReason`

  The caller invoked the pause endpoint on the deployment.

  - `type: "manual"`

    - `"manual"`

### Beta Managed Agents MCP Egress Blocked Deployment Paused Reason Error

- `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

  An MCP server host used by the deployment's agent is blocked by the environment's network policy.

  - `type: "mcp_egress_blocked_error"`

    - `"mcp_egress_blocked_error"`

### Beta Managed Agents Memory Store Archived Deployment Paused Reason Error

- `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

  A memory store referenced by the deployment is archived.

  - `type: "memory_store_archived_error"`

    - `"memory_store_archived_error"`

### Beta Managed Agents Memory Store Resource Config

- `BetaManagedAgentsMemoryStoreResourceConfig`

  A memory store attached to each session created from this deployment.

  - `memory_store_id: string`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `type: "memory_store"`

    - `"memory_store"`

  - `access?: "read_write" | "read_only" | null`

    Access mode for an attached memory store.

    - `"read_write"`

    - `"read_only"`

  - `instructions?: string | null`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Organization Disabled Deployment Paused Reason Error

- `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

  The deployment's organization is disabled.

  - `type: "organization_disabled_error"`

    - `"organization_disabled_error"`

### Beta Managed Agents Schedule

- `BetaManagedAgentsSchedule`

  5-field POSIX cron schedule with computed runtime timestamps.

  - `expression: string`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `timezone: string`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

  - `type: "cron"`

    - `"cron"`

  - `last_run_at?: string | null`

    A timestamp in RFC 3339 format

  - `upcoming_runs_at?: Array<string>`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Schedule Params

- `BetaManagedAgentsScheduleParams`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `expression: string`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `timezone: string`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `type: "cron"`

    - `"cron"`

### Beta Managed Agents Self Hosted Resources Unsupported Deployment Paused Reason Error

- `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

  The deployment configures resources, but its environment is self-hosted and cannot mount them.

  - `type: "self_hosted_resources_unsupported_error"`

    - `"self_hosted_resources_unsupported_error"`

### Beta Managed Agents Session Resource Config

- `BetaManagedAgentsSessionResourceConfig = BetaManagedAgentsGitHubRepositoryResourceConfig | BetaManagedAgentsFileResourceConfig | BetaManagedAgentsMemoryStoreResourceConfig`

  A configured session resource. Echoes the input minus write-only credentials.

  - `BetaManagedAgentsGitHubRepositoryResourceConfig`

    A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

    - `type: "github_repository"`

      - `"github_repository"`

    - `url: string`

      Github URL of the repository

    - `checkout?: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout | null`

      Branch or commit to check out. Defaults to the repository's default branch.

      - `BetaManagedAgentsBranchCheckout`

        - `name: string`

          Branch name to check out.

        - `type: "branch"`

          - `"branch"`

      - `BetaManagedAgentsCommitCheckout`

        - `sha: string`

          Full commit SHA to check out.

        - `type: "commit"`

          - `"commit"`

    - `mount_path?: string | null`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

  - `BetaManagedAgentsFileResourceConfig`

    A file mounted into each session's container.

    - `file_id: string`

      ID of a previously uploaded file.

    - `type: "file"`

      - `"file"`

    - `mount_path?: string | null`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  - `BetaManagedAgentsMemoryStoreResourceConfig`

    A memory store attached to each session created from this deployment.

    - `memory_store_id: string`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: "memory_store"`

      - `"memory_store"`

    - `access?: "read_write" | "read_only" | null`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `instructions?: string | null`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Session Resource Not Found Deployment Paused Reason Error

- `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

  A referenced resource no longer exists and its kind was not reported.

  - `type: "session_resource_not_found_error"`

    - `"session_resource_not_found_error"`

### Beta Managed Agents Skill Not Found Deployment Paused Reason Error

- `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

  A skill referenced by the deployment's agent no longer exists.

  - `type: "skill_not_found_error"`

    - `"skill_not_found_error"`

### Beta Managed Agents Unknown Deployment Paused Reason Error

- `BetaManagedAgentsUnknownDeploymentPausedReasonError`

  An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

  - `type: "unknown_error"`

    - `"unknown_error"`

### Beta Managed Agents Vault Archived Deployment Paused Reason Error

- `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

  A vault referenced by the deployment is archived.

  - `type: "vault_archived_error"`

    - `"vault_archived_error"`

### Beta Managed Agents Vault Not Found Deployment Paused Reason Error

- `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

  A vault referenced by the deployment no longer exists.

  - `type: "vault_not_found_error"`

    - `"vault_not_found_error"`

### Beta Managed Agents Workspace Archived Deployment Paused Reason Error

- `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

  The deployment's workspace was archived.

  - `type: "workspace_archived_error"`

    - `"workspace_archived_error"`
