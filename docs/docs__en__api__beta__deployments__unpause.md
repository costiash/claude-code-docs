## Unpause Deployment

**post** `/v1/deployments/{deployment_id}/unpause`

Unpause Deployment

### Path Parameters

- `deployment_id: string`

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

- `BetaManagedAgentsDeployment object { id, agent, archived_at, 13 more }`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: array of BetaManagedAgentsDeploymentInitialEvent`

    Events sent to each session immediately after creation.

    - `BetaManagedAgentsDeploymentUserMessageEvent object { content, type }`

      A user message sent to the session.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        Array of content blocks for the user message.

        - `BetaManagedAgentsTextBlock object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsImageBlock object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `BetaManagedAgentsBase64ImageSource object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsURLImageSource object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `BetaManagedAgentsFileImageSource object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `BetaManagedAgentsDocumentBlock object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `BetaManagedAgentsBase64DocumentSource object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `BetaManagedAgentsURLDocumentSource object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `BetaManagedAgentsFileDocumentSource object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

    - `BetaManagedAgentsDeploymentUserDefineOutcomeEvent object { description, rubric, type, max_iterations }`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `BetaManagedAgentsFileRubric object { file_id, type }`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

            - `"file"`

        - `BetaManagedAgentsTextRubric object { content, type }`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

            - `"text"`

      - `type: "user.define_outcome"`

        - `"user.define_outcome"`

      - `max_iterations: optional number`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `BetaManagedAgentsDeploymentSystemMessageEvent object { content, type }`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `type: "system.message"`

        - `"system.message"`

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `BetaManagedAgentsManualDeploymentPausedReason object { type }`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

        - `"manual"`

    - `BetaManagedAgentsErrorDeploymentPausedReason object { error, type }`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError object { type }`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

            - `"environment_archived_error"`

        - `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError object { type }`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

            - `"agent_archived_error"`

        - `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError object { type }`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

            - `"environment_not_found_error"`

        - `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError object { type }`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

            - `"vault_not_found_error"`

        - `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError object { type }`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

            - `"file_not_found_error"`

        - `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError object { type }`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

            - `"session_resource_not_found_error"`

        - `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError object { type }`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

            - `"workspace_archived_error"`

        - `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError object { type }`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

            - `"organization_disabled_error"`

        - `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError object { type }`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

            - `"memory_store_archived_error"`

        - `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError object { type }`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

            - `"skill_not_found_error"`

        - `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError object { type }`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

            - `"vault_archived_error"`

        - `BetaManagedAgentsUnknownDeploymentPausedReasonError object { type }`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

            - `"unknown_error"`

        - `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError object { type }`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

            - `"self_hosted_resources_unsupported_error"`

        - `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError object { type }`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

            - `"mcp_egress_blocked_error"`

      - `type: "error"`

        - `"error"`

  - `resources: array of BetaManagedAgentsSessionResourceConfig`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `BetaManagedAgentsGitHubRepositoryResourceConfig object { type, url, checkout, mount_path }`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

        - `"github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `BetaManagedAgentsBranchCheckout object { name, type }`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `BetaManagedAgentsCommitCheckout object { sha, type }`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `BetaManagedAgentsFileResourceConfig object { file_id, type, mount_path }`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `BetaManagedAgentsMemoryStoreResourceConfig object { memory_store_id, type, access, instructions }`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: BetaManagedAgentsSchedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: "cron"`

      - `"cron"`

    - `last_run_at: optional string`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: optional array of string`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

    - `"deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_ids: array of string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```http
curl https://api.anthropic.com/v1/deployments/$DEPLOYMENT_ID/unpause \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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
