## Create Deployment

`beta.deployments.create(**kwargs) -> BetaManagedAgentsDeployment`

**post** `/v1/deployments`

Create Deployment

### Parameters

- `agent: String | BetaManagedAgentsAgentParams`

  Agent to deploy. Accepts the `agent` ID string, which pins the latest version, or an `agent` object with both id and version specified. The agent must exist and not be archived.

  - `String = String`

  - `class BetaManagedAgentsAgentParams`

    Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

    - `id: String`

      The `agent` ID.

    - `type: :agent`

      - `:agent`

    - `version: Integer`

      The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

- `environment_id: String`

  ID of the `environment` defining the container configuration for sessions created from this deployment.

- `initial_events: Array[BetaManagedAgentsDeploymentInitialEventParams]`

  Events to send to each session immediately after creation. At least 1, maximum 50.

  - `class BetaManagedAgentsUserMessageEventParams`

    Parameters for sending a user message to the session.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `type: :"user.message"`

      - `:"user.message"`

  - `class BetaManagedAgentsUserDefineOutcomeEventParams`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `description: String`

      What the agent should produce. This is the task specification.

    - `rubric: BetaManagedAgentsFileRubricParams | BetaManagedAgentsTextRubricParams`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubricParams`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: String`

          ID of the rubric file.

        - `type: :file`

          - `:file`

      - `class BetaManagedAgentsTextRubricParams`

        Rubric content provided inline as text.

        - `content: String`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

        - `type: :text`

          - `:text`

    - `type: :"user.define_outcome"`

      - `:"user.define_outcome"`

    - `max_iterations: Integer`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `class BetaManagedAgentsSystemMessageEventParams`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `content: Array[BetaManagedAgentsSystemContentBlock]`

      System content blocks to append. Text-only.

      - `text: String`

        The text content.

      - `type: :text`

        - `:text`

    - `type: :"system.message"`

      - `:"system.message"`

- `name: String`

  Human-readable name for the deployment.

- `description: String`

  Description of what the deployment does.

- `metadata: Hash[Symbol, String]`

  Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `resources: Array[BetaManagedAgentsGitHubRepositoryResourceParams | BetaManagedAgentsFileResourceParams | BetaManagedAgentsMemoryStoreResourceParam]`

  Resources (e.g. repositories, files) to mount into each session's container. Maximum 500.

  - `class BetaManagedAgentsGitHubRepositoryResourceParams`

    Mount a GitHub repository into the session's container.

    - `authorization_token: String`

      GitHub authorization token used to clone the repository.

    - `type: :github_repository`

      - `:github_repository`

    - `url: String`

      Github URL of the repository

    - `checkout: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout`

      Branch or commit to check out. Defaults to the repository's default branch.

      - `class BetaManagedAgentsBranchCheckout`

        - `name: String`

          Branch name to check out.

        - `type: :branch`

          - `:branch`

      - `class BetaManagedAgentsCommitCheckout`

        - `sha: String`

          Full commit SHA to check out.

        - `type: :commit`

          - `:commit`

    - `mount_path: String`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

  - `class BetaManagedAgentsFileResourceParams`

    Mount a file uploaded via the Files API into the session.

    - `file_id: String`

      ID of a previously uploaded file.

    - `type: :file`

      - `:file`

    - `mount_path: String`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  - `class BetaManagedAgentsMemoryStoreResourceParam`

    Parameters for attaching a memory store to an agent session.

    - `memory_store_id: String`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: :memory_store`

      - `:memory_store`

    - `access: :read_write | :read_only`

      Access mode for an attached memory store.

      - `:read_write`

      - `:read_only`

    - `instructions: String`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

- `schedule: BetaManagedAgentsScheduleParams`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `expression: String`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `timezone: String`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `type: :cron`

    - `:cron`

- `vault_ids: Array[String]`

  Vault IDs for stored credentials the agent can use during sessions created from this deployment. Maximum 50.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 25 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"fallback-credit-2026-06-01"`

### Returns

- `class BetaManagedAgentsDeployment`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: String`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: String`

    - `type: :agent`

      - `:agent`

    - `version: Integer`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `description: String`

    Description of what the deployment does.

  - `environment_id: String`

    ID of the `environment` where sessions run.

  - `initial_events: Array[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent`

      A user message sent to the session.

      - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock`

          Regular text content.

          - `text: String`

            The text content.

          - `type: :text`

            - `:text`

        - `class BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `data: String`

                Base64-encoded image data.

              - `media_type: String`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: :base64`

                - `:base64`

            - `class BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: :url`

                - `:url`

              - `url: String`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

              - `type: :file`

                - `:file`

          - `type: :image`

            - `:image`

        - `class BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `data: String`

                Base64-encoded document data.

              - `media_type: String`

                MIME type of the document (e.g., "application/pdf").

              - `type: :base64`

                - `:base64`

            - `class BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `data: String`

                The plain text content.

              - `media_type: :"text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `:"text/plain"`

              - `type: :text`

                - `:text`

            - `class BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: :url`

                - `:url`

              - `url: String`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

              - `type: :file`

                - `:file`

          - `type: :document`

            - `:document`

          - `context: String`

            Additional context about the document for the model.

          - `title: String`

            The title of the document.

      - `type: :"user.message"`

        - `:"user.message"`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: String`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: String`

            ID of the rubric file.

          - `type: :file`

            - `:file`

        - `class BetaManagedAgentsTextRubric`

          Rubric content provided inline as text.

          - `content: String`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: :text`

            - `:text`

      - `type: :"user.define_outcome"`

        - `:"user.define_outcome"`

      - `max_iterations: Integer`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: Array[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `type: :"system.message"`

        - `:"system.message"`

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: String`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason`

      The caller invoked the pause endpoint on the deployment.

      - `type: :manual`

        - `:manual`

    - `class BetaManagedAgentsErrorDeploymentPausedReason`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

          The deployment's environment was archived.

          - `type: :environment_archived_error`

            - `:environment_archived_error`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

          The deployment's agent was archived.

          - `type: :agent_archived_error`

            - `:agent_archived_error`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

          The deployment's environment no longer exists.

          - `type: :environment_not_found_error`

            - `:environment_not_found_error`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

          A vault referenced by the deployment no longer exists.

          - `type: :vault_not_found_error`

            - `:vault_not_found_error`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

          A file resource referenced by the deployment no longer exists.

          - `type: :file_not_found_error`

            - `:file_not_found_error`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

          A referenced resource no longer exists and its kind was not reported.

          - `type: :session_resource_not_found_error`

            - `:session_resource_not_found_error`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

          The deployment's workspace was archived.

          - `type: :workspace_archived_error`

            - `:workspace_archived_error`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

          The deployment's organization is disabled.

          - `type: :organization_disabled_error`

            - `:organization_disabled_error`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

          A memory store referenced by the deployment is archived.

          - `type: :memory_store_archived_error`

            - `:memory_store_archived_error`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

          A skill referenced by the deployment's agent no longer exists.

          - `type: :skill_not_found_error`

            - `:skill_not_found_error`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

          A vault referenced by the deployment is archived.

          - `type: :vault_archived_error`

            - `:vault_archived_error`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: :unknown_error`

            - `:unknown_error`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: :self_hosted_resources_unsupported_error`

            - `:self_hosted_resources_unsupported_error`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: :mcp_egress_blocked_error`

            - `:mcp_egress_blocked_error`

      - `type: :error`

        - `:error`

  - `resources: Array[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: :github_repository`

        - `:github_repository`

      - `url: String`

        Github URL of the repository

      - `checkout: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout`

          - `name: String`

            Branch name to check out.

          - `type: :branch`

            - `:branch`

        - `class BetaManagedAgentsCommitCheckout`

          - `sha: String`

            Full commit SHA to check out.

          - `type: :commit`

            - `:commit`

      - `mount_path: String`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig`

      A file mounted into each session's container.

      - `file_id: String`

        ID of a previously uploaded file.

      - `type: :file`

        - `:file`

      - `mount_path: String`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: String`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: :memory_store`

        - `:memory_store`

      - `access: :read_write | :read_only`

        Access mode for an attached memory store.

        - `:read_write`

        - `:read_only`

      - `instructions: String`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: BetaManagedAgentsSchedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: String`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: String`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: :cron`

      - `:cron`

    - `last_run_at: Time`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: Array[Time]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `:active`

    - `:paused`

  - `type: :deployment`

    - `:deployment`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `vault_ids: Array[String]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_deployment = anthropic.beta.deployments.create(
  agent: "string",
  environment_id: "x",
  initial_events: [{content: [{text: "Where is my order #1234?", type: :text}], type: :"user.message"}],
  name: "x"
)

puts(beta_managed_agents_deployment)
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
