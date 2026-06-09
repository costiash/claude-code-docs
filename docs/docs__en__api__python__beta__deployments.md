# Deployments

## Create Deployment

`beta.deployments.create(DeploymentCreateParams**kwargs)  -> BetaManagedAgentsDeployment`

**post** `/v1/deployments`

Create Deployment

### Parameters

- `agent: Agent`

  Agent to deploy. Accepts the `agent` ID string, which pins the latest version, or an `agent` object with both id and version specified. The agent must exist and not be archived.

  - `str`

  - `class BetaManagedAgentsAgentParams: …`

    Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

    - `id: str`

      The `agent` ID.

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: Optional[int]`

      The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

- `environment_id: str`

  ID of the `environment` defining the container configuration for sessions created from this deployment.

- `initial_events: Iterable[BetaManagedAgentsDeploymentInitialEventParams]`

  Events to send to each session immediately after creation. At least 1, maximum 50.

  - `class BetaManagedAgentsUserMessageEventParams: …`

    Parameters for sending a user message to the session.

    - `content: List[Content]`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `data: str`

              Base64-encoded image data.

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["image"]`

          - `"image"`

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `data: str`

              Base64-encoded document data.

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `data: str`

              The plain text content.

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: Literal["text"]`

              - `"text"`

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["document"]`

          - `"document"`

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

    - `type: Literal["user.message"]`

      - `"user.message"`

  - `class BetaManagedAgentsUserDefineOutcomeEventParams: …`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `description: str`

      What the agent should produce. This is the task specification.

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubricParams: …`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: str`

          ID of the rubric file.

        - `type: Literal["file"]`

          - `"file"`

      - `class BetaManagedAgentsTextRubricParams: …`

        Rubric content provided inline as text.

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

        - `type: Literal["text"]`

          - `"text"`

    - `type: Literal["user.define_outcome"]`

      - `"user.define_outcome"`

    - `max_iterations: Optional[int]`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `class BetaManagedAgentsSystemMessageEventParams: …`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks to append. Text-only.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `type: Literal["system.message"]`

      - `"system.message"`

- `name: str`

  Human-readable name for the deployment.

- `description: Optional[str]`

  Description of what the deployment does.

- `metadata: Optional[Dict[str, str]]`

  Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `resources: Optional[Iterable[Resource]]`

  Resources (e.g. repositories, files) to mount into each session's container. Maximum 500.

  - `class BetaManagedAgentsGitHubRepositoryResourceParams: …`

    Mount a GitHub repository into the session's container.

    - `authorization_token: str`

      GitHub authorization token used to clone the repository.

    - `type: Literal["github_repository"]`

      - `"github_repository"`

    - `url: str`

      Github URL of the repository

    - `checkout: Optional[Checkout]`

      Branch or commit to check out. Defaults to the repository's default branch.

      - `class BetaManagedAgentsBranchCheckout: …`

        - `name: str`

          Branch name to check out.

        - `type: Literal["branch"]`

          - `"branch"`

      - `class BetaManagedAgentsCommitCheckout: …`

        - `sha: str`

          Full commit SHA to check out.

        - `type: Literal["commit"]`

          - `"commit"`

    - `mount_path: Optional[str]`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

  - `class BetaManagedAgentsFileResourceParams: …`

    Mount a file uploaded via the Files API into the session.

    - `file_id: str`

      ID of a previously uploaded file.

    - `type: Literal["file"]`

      - `"file"`

    - `mount_path: Optional[str]`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  - `class BetaManagedAgentsMemoryStoreResourceParam: …`

    Parameters for attaching a memory store to an agent session.

    - `memory_store_id: str`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: Literal["memory_store"]`

      - `"memory_store"`

    - `access: Optional[Literal["read_write", "read_only"]]`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `instructions: Optional[str]`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

- `schedule: Optional[BetaManagedAgentsScheduleParams]`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `expression: str`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `timezone: str`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `type: Literal["cron"]`

    - `"cron"`

- `vault_ids: Optional[Sequence[str]]`

  Vault IDs for stored credentials the agent can use during sessions created from this deployment. Maximum 50.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]`

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

- `class BetaManagedAgentsDeployment: …`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: str`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: str`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `description: Optional[str]`

    Description of what the deployment does.

  - `environment_id: str`

    ID of the `environment` where sessions run.

  - `initial_events: List[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent: …`

      A user message sent to the session.

      - `content: List[Content]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock: …`

          Regular text content.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsImageBlock: …`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource: …`

              Base64-encoded image data.

              - `data: str`

                Base64-encoded image data.

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsURLImageSource: …`

              Image referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource: …`

              Image referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["image"]`

            - `"image"`

        - `class BetaManagedAgentsDocumentBlock: …`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource: …`

              Base64-encoded document data.

              - `data: str`

                Base64-encoded document data.

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsPlainTextDocumentSource: …`

              Plain text document content.

              - `data: str`

                The plain text content.

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: Literal["text"]`

                - `"text"`

            - `class BetaManagedAgentsURLDocumentSource: …`

              Document referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource: …`

              Document referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["document"]`

            - `"document"`

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

      - `type: Literal["user.message"]`

        - `"user.message"`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent: …`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: str`

        What the agent should produce. This is the task specification.

      - `rubric: Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric: …`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: str`

            ID of the rubric file.

          - `type: Literal["file"]`

            - `"file"`

        - `class BetaManagedAgentsTextRubric: …`

          Rubric content provided inline as text.

          - `content: str`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: Literal["text"]`

            - `"text"`

      - `type: Literal["user.define_outcome"]`

        - `"user.define_outcome"`

      - `max_iterations: Optional[int]`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent: …`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: List[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `type: Literal["system.message"]`

        - `"system.message"`

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: str`

    Human-readable name.

  - `paused_reason: Optional[BetaManagedAgentsDeploymentPausedReason]`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason: …`

      The caller invoked the pause endpoint on the deployment.

      - `type: Literal["manual"]`

        - `"manual"`

    - `class BetaManagedAgentsErrorDeploymentPausedReason: …`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …`

          The deployment's environment was archived.

          - `type: Literal["environment_archived_error"]`

            - `"environment_archived_error"`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …`

          The deployment's agent was archived.

          - `type: Literal["agent_archived_error"]`

            - `"agent_archived_error"`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …`

          The deployment's environment no longer exists.

          - `type: Literal["environment_not_found_error"]`

            - `"environment_not_found_error"`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …`

          A vault referenced by the deployment no longer exists.

          - `type: Literal["vault_not_found_error"]`

            - `"vault_not_found_error"`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …`

          A file resource referenced by the deployment no longer exists.

          - `type: Literal["file_not_found_error"]`

            - `"file_not_found_error"`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …`

          A referenced resource no longer exists and its kind was not reported.

          - `type: Literal["session_resource_not_found_error"]`

            - `"session_resource_not_found_error"`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …`

          The deployment's workspace was archived.

          - `type: Literal["workspace_archived_error"]`

            - `"workspace_archived_error"`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …`

          The deployment's organization is disabled.

          - `type: Literal["organization_disabled_error"]`

            - `"organization_disabled_error"`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …`

          A memory store referenced by the deployment is archived.

          - `type: Literal["memory_store_archived_error"]`

            - `"memory_store_archived_error"`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …`

          A skill referenced by the deployment's agent no longer exists.

          - `type: Literal["skill_not_found_error"]`

            - `"skill_not_found_error"`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …`

          A vault referenced by the deployment is archived.

          - `type: Literal["vault_archived_error"]`

            - `"vault_archived_error"`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError: …`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: Literal["unknown_error"]`

            - `"unknown_error"`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: Literal["self_hosted_resources_unsupported_error"]`

            - `"self_hosted_resources_unsupported_error"`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: Literal["mcp_egress_blocked_error"]`

            - `"mcp_egress_blocked_error"`

      - `type: Literal["error"]`

        - `"error"`

  - `resources: List[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig: …`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: Literal["github_repository"]`

        - `"github_repository"`

      - `url: str`

        Github URL of the repository

      - `checkout: Optional[Checkout]`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout: …`

          - `name: str`

            Branch name to check out.

          - `type: Literal["branch"]`

            - `"branch"`

        - `class BetaManagedAgentsCommitCheckout: …`

          - `sha: str`

            Full commit SHA to check out.

          - `type: Literal["commit"]`

            - `"commit"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig: …`

      A file mounted into each session's container.

      - `file_id: str`

        ID of a previously uploaded file.

      - `type: Literal["file"]`

        - `"file"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig: …`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: Literal["memory_store"]`

        - `"memory_store"`

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: Optional[BetaManagedAgentsSchedule]`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: str`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: str`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: Literal["cron"]`

      - `"cron"`

    - `last_run_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: Optional[List[datetime]]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: Literal["deployment"]`

    - `"deployment"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `vault_ids: List[str]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_deployment = client.beta.deployments.create(
    agent="string",
    environment_id="x",
    initial_events=[{
        "content": [{
            "text": "Where is my order #1234?",
            "type": "text",
        }],
        "type": "user.message",
    }],
    name="x",
)
print(beta_managed_agents_deployment.id)
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

`beta.deployments.list(DeploymentListParams**kwargs)  -> SyncPageCursor[BetaManagedAgentsDeployment]`

**get** `/v1/deployments`

List Deployments

### Parameters

- `agent_id: Optional[str]`

  Filter by agent ID.

- `created_at_gte: Optional[Union[str, datetime]]`

  Return deployments created at or after this time (inclusive).

- `created_at_lte: Optional[Union[str, datetime]]`

  Return deployments created at or before this time (inclusive).

- `include_archived: Optional[bool]`

  When true, includes archived deployments. Default: false (exclude archived).

- `limit: Optional[int]`

  Maximum results per page. Default 20, maximum 100.

- `page: Optional[str]`

  Opaque pagination cursor.

- `status: Optional[BetaManagedAgentsDeploymentStatus]`

  Filter by status: active or paused. Omit for both. To include archived deployments, use include_archived instead; the two cannot be combined.

  - `"active"`

  - `"paused"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]`

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

- `class BetaManagedAgentsDeployment: …`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: str`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: str`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `description: Optional[str]`

    Description of what the deployment does.

  - `environment_id: str`

    ID of the `environment` where sessions run.

  - `initial_events: List[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent: …`

      A user message sent to the session.

      - `content: List[Content]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock: …`

          Regular text content.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsImageBlock: …`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource: …`

              Base64-encoded image data.

              - `data: str`

                Base64-encoded image data.

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsURLImageSource: …`

              Image referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource: …`

              Image referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["image"]`

            - `"image"`

        - `class BetaManagedAgentsDocumentBlock: …`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource: …`

              Base64-encoded document data.

              - `data: str`

                Base64-encoded document data.

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsPlainTextDocumentSource: …`

              Plain text document content.

              - `data: str`

                The plain text content.

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: Literal["text"]`

                - `"text"`

            - `class BetaManagedAgentsURLDocumentSource: …`

              Document referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource: …`

              Document referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["document"]`

            - `"document"`

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

      - `type: Literal["user.message"]`

        - `"user.message"`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent: …`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: str`

        What the agent should produce. This is the task specification.

      - `rubric: Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric: …`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: str`

            ID of the rubric file.

          - `type: Literal["file"]`

            - `"file"`

        - `class BetaManagedAgentsTextRubric: …`

          Rubric content provided inline as text.

          - `content: str`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: Literal["text"]`

            - `"text"`

      - `type: Literal["user.define_outcome"]`

        - `"user.define_outcome"`

      - `max_iterations: Optional[int]`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent: …`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: List[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `type: Literal["system.message"]`

        - `"system.message"`

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: str`

    Human-readable name.

  - `paused_reason: Optional[BetaManagedAgentsDeploymentPausedReason]`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason: …`

      The caller invoked the pause endpoint on the deployment.

      - `type: Literal["manual"]`

        - `"manual"`

    - `class BetaManagedAgentsErrorDeploymentPausedReason: …`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …`

          The deployment's environment was archived.

          - `type: Literal["environment_archived_error"]`

            - `"environment_archived_error"`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …`

          The deployment's agent was archived.

          - `type: Literal["agent_archived_error"]`

            - `"agent_archived_error"`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …`

          The deployment's environment no longer exists.

          - `type: Literal["environment_not_found_error"]`

            - `"environment_not_found_error"`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …`

          A vault referenced by the deployment no longer exists.

          - `type: Literal["vault_not_found_error"]`

            - `"vault_not_found_error"`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …`

          A file resource referenced by the deployment no longer exists.

          - `type: Literal["file_not_found_error"]`

            - `"file_not_found_error"`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …`

          A referenced resource no longer exists and its kind was not reported.

          - `type: Literal["session_resource_not_found_error"]`

            - `"session_resource_not_found_error"`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …`

          The deployment's workspace was archived.

          - `type: Literal["workspace_archived_error"]`

            - `"workspace_archived_error"`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …`

          The deployment's organization is disabled.

          - `type: Literal["organization_disabled_error"]`

            - `"organization_disabled_error"`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …`

          A memory store referenced by the deployment is archived.

          - `type: Literal["memory_store_archived_error"]`

            - `"memory_store_archived_error"`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …`

          A skill referenced by the deployment's agent no longer exists.

          - `type: Literal["skill_not_found_error"]`

            - `"skill_not_found_error"`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …`

          A vault referenced by the deployment is archived.

          - `type: Literal["vault_archived_error"]`

            - `"vault_archived_error"`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError: …`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: Literal["unknown_error"]`

            - `"unknown_error"`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: Literal["self_hosted_resources_unsupported_error"]`

            - `"self_hosted_resources_unsupported_error"`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: Literal["mcp_egress_blocked_error"]`

            - `"mcp_egress_blocked_error"`

      - `type: Literal["error"]`

        - `"error"`

  - `resources: List[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig: …`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: Literal["github_repository"]`

        - `"github_repository"`

      - `url: str`

        Github URL of the repository

      - `checkout: Optional[Checkout]`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout: …`

          - `name: str`

            Branch name to check out.

          - `type: Literal["branch"]`

            - `"branch"`

        - `class BetaManagedAgentsCommitCheckout: …`

          - `sha: str`

            Full commit SHA to check out.

          - `type: Literal["commit"]`

            - `"commit"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig: …`

      A file mounted into each session's container.

      - `file_id: str`

        ID of a previously uploaded file.

      - `type: Literal["file"]`

        - `"file"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig: …`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: Literal["memory_store"]`

        - `"memory_store"`

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: Optional[BetaManagedAgentsSchedule]`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: str`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: str`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: Literal["cron"]`

      - `"cron"`

    - `last_run_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: Optional[List[datetime]]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: Literal["deployment"]`

    - `"deployment"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `vault_ids: List[str]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.deployments.list()
page = page.data[0]
print(page.id)
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

`beta.deployments.retrieve(strdeployment_id, DeploymentRetrieveParams**kwargs)  -> BetaManagedAgentsDeployment`

**get** `/v1/deployments/{deployment_id}`

Get Deployment

### Parameters

- `deployment_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]`

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

- `class BetaManagedAgentsDeployment: …`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: str`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: str`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `description: Optional[str]`

    Description of what the deployment does.

  - `environment_id: str`

    ID of the `environment` where sessions run.

  - `initial_events: List[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent: …`

      A user message sent to the session.

      - `content: List[Content]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock: …`

          Regular text content.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsImageBlock: …`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource: …`

              Base64-encoded image data.

              - `data: str`

                Base64-encoded image data.

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsURLImageSource: …`

              Image referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource: …`

              Image referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["image"]`

            - `"image"`

        - `class BetaManagedAgentsDocumentBlock: …`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource: …`

              Base64-encoded document data.

              - `data: str`

                Base64-encoded document data.

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsPlainTextDocumentSource: …`

              Plain text document content.

              - `data: str`

                The plain text content.

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: Literal["text"]`

                - `"text"`

            - `class BetaManagedAgentsURLDocumentSource: …`

              Document referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource: …`

              Document referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["document"]`

            - `"document"`

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

      - `type: Literal["user.message"]`

        - `"user.message"`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent: …`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: str`

        What the agent should produce. This is the task specification.

      - `rubric: Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric: …`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: str`

            ID of the rubric file.

          - `type: Literal["file"]`

            - `"file"`

        - `class BetaManagedAgentsTextRubric: …`

          Rubric content provided inline as text.

          - `content: str`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: Literal["text"]`

            - `"text"`

      - `type: Literal["user.define_outcome"]`

        - `"user.define_outcome"`

      - `max_iterations: Optional[int]`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent: …`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: List[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `type: Literal["system.message"]`

        - `"system.message"`

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: str`

    Human-readable name.

  - `paused_reason: Optional[BetaManagedAgentsDeploymentPausedReason]`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason: …`

      The caller invoked the pause endpoint on the deployment.

      - `type: Literal["manual"]`

        - `"manual"`

    - `class BetaManagedAgentsErrorDeploymentPausedReason: …`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …`

          The deployment's environment was archived.

          - `type: Literal["environment_archived_error"]`

            - `"environment_archived_error"`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …`

          The deployment's agent was archived.

          - `type: Literal["agent_archived_error"]`

            - `"agent_archived_error"`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …`

          The deployment's environment no longer exists.

          - `type: Literal["environment_not_found_error"]`

            - `"environment_not_found_error"`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …`

          A vault referenced by the deployment no longer exists.

          - `type: Literal["vault_not_found_error"]`

            - `"vault_not_found_error"`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …`

          A file resource referenced by the deployment no longer exists.

          - `type: Literal["file_not_found_error"]`

            - `"file_not_found_error"`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …`

          A referenced resource no longer exists and its kind was not reported.

          - `type: Literal["session_resource_not_found_error"]`

            - `"session_resource_not_found_error"`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …`

          The deployment's workspace was archived.

          - `type: Literal["workspace_archived_error"]`

            - `"workspace_archived_error"`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …`

          The deployment's organization is disabled.

          - `type: Literal["organization_disabled_error"]`

            - `"organization_disabled_error"`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …`

          A memory store referenced by the deployment is archived.

          - `type: Literal["memory_store_archived_error"]`

            - `"memory_store_archived_error"`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …`

          A skill referenced by the deployment's agent no longer exists.

          - `type: Literal["skill_not_found_error"]`

            - `"skill_not_found_error"`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …`

          A vault referenced by the deployment is archived.

          - `type: Literal["vault_archived_error"]`

            - `"vault_archived_error"`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError: …`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: Literal["unknown_error"]`

            - `"unknown_error"`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: Literal["self_hosted_resources_unsupported_error"]`

            - `"self_hosted_resources_unsupported_error"`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: Literal["mcp_egress_blocked_error"]`

            - `"mcp_egress_blocked_error"`

      - `type: Literal["error"]`

        - `"error"`

  - `resources: List[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig: …`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: Literal["github_repository"]`

        - `"github_repository"`

      - `url: str`

        Github URL of the repository

      - `checkout: Optional[Checkout]`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout: …`

          - `name: str`

            Branch name to check out.

          - `type: Literal["branch"]`

            - `"branch"`

        - `class BetaManagedAgentsCommitCheckout: …`

          - `sha: str`

            Full commit SHA to check out.

          - `type: Literal["commit"]`

            - `"commit"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig: …`

      A file mounted into each session's container.

      - `file_id: str`

        ID of a previously uploaded file.

      - `type: Literal["file"]`

        - `"file"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig: …`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: Literal["memory_store"]`

        - `"memory_store"`

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: Optional[BetaManagedAgentsSchedule]`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: str`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: str`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: Literal["cron"]`

      - `"cron"`

    - `last_run_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: Optional[List[datetime]]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: Literal["deployment"]`

    - `"deployment"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `vault_ids: List[str]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_deployment = client.beta.deployments.retrieve(
    deployment_id="deployment_id",
)
print(beta_managed_agents_deployment.id)
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

`beta.deployments.update(strdeployment_id, DeploymentUpdateParams**kwargs)  -> BetaManagedAgentsDeployment`

**post** `/v1/deployments/{deployment_id}`

Update Deployment

### Parameters

- `deployment_id: str`

- `agent: Optional[Agent]`

  Agent to deploy. Accepts the `agent` ID string, which re-pins to the latest version, or an `agent` object with both id and version specified. Omit to preserve. Cannot be cleared.

  - `str`

  - `class BetaManagedAgentsAgentParams: …`

    Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

    - `id: str`

      The `agent` ID.

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: Optional[int]`

      The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

- `description: Optional[str]`

  Description. Omit to preserve; send empty string or null to clear.

- `environment_id: Optional[str]`

  ID of the `environment` where sessions run. Omit to preserve. Cannot be cleared.

- `initial_events: Optional[Iterable[BetaManagedAgentsDeploymentInitialEventParams]]`

  Initial events. Full replacement. Omit to preserve. Cannot be cleared. At least 1, maximum 50.

  - `class BetaManagedAgentsUserMessageEventParams: …`

    Parameters for sending a user message to the session.

    - `content: List[Content]`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `data: str`

              Base64-encoded image data.

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["image"]`

          - `"image"`

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `data: str`

              Base64-encoded document data.

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `data: str`

              The plain text content.

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: Literal["text"]`

              - `"text"`

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["document"]`

          - `"document"`

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

    - `type: Literal["user.message"]`

      - `"user.message"`

  - `class BetaManagedAgentsUserDefineOutcomeEventParams: …`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `description: str`

      What the agent should produce. This is the task specification.

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubricParams: …`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: str`

          ID of the rubric file.

        - `type: Literal["file"]`

          - `"file"`

      - `class BetaManagedAgentsTextRubricParams: …`

        Rubric content provided inline as text.

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

        - `type: Literal["text"]`

          - `"text"`

    - `type: Literal["user.define_outcome"]`

      - `"user.define_outcome"`

    - `max_iterations: Optional[int]`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `class BetaManagedAgentsSystemMessageEventParams: …`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks to append. Text-only.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `type: Literal["system.message"]`

      - `"system.message"`

- `metadata: Optional[Dict[str, Optional[str]]]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `name: Optional[str]`

  Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

- `resources: Optional[Iterable[Resource]]`

  Session resources. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 500.

  - `class BetaManagedAgentsGitHubRepositoryResourceParams: …`

    Mount a GitHub repository into the session's container.

    - `authorization_token: str`

      GitHub authorization token used to clone the repository.

    - `type: Literal["github_repository"]`

      - `"github_repository"`

    - `url: str`

      Github URL of the repository

    - `checkout: Optional[Checkout]`

      Branch or commit to check out. Defaults to the repository's default branch.

      - `class BetaManagedAgentsBranchCheckout: …`

        - `name: str`

          Branch name to check out.

        - `type: Literal["branch"]`

          - `"branch"`

      - `class BetaManagedAgentsCommitCheckout: …`

        - `sha: str`

          Full commit SHA to check out.

        - `type: Literal["commit"]`

          - `"commit"`

    - `mount_path: Optional[str]`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

  - `class BetaManagedAgentsFileResourceParams: …`

    Mount a file uploaded via the Files API into the session.

    - `file_id: str`

      ID of a previously uploaded file.

    - `type: Literal["file"]`

      - `"file"`

    - `mount_path: Optional[str]`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  - `class BetaManagedAgentsMemoryStoreResourceParam: …`

    Parameters for attaching a memory store to an agent session.

    - `memory_store_id: str`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: Literal["memory_store"]`

      - `"memory_store"`

    - `access: Optional[Literal["read_write", "read_only"]]`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `instructions: Optional[str]`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

- `schedule: Optional[BetaManagedAgentsScheduleParams]`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `expression: str`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `timezone: str`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `type: Literal["cron"]`

    - `"cron"`

- `vault_ids: Optional[Sequence[str]]`

  Vault IDs. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 50.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]`

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

- `class BetaManagedAgentsDeployment: …`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: str`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: str`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `description: Optional[str]`

    Description of what the deployment does.

  - `environment_id: str`

    ID of the `environment` where sessions run.

  - `initial_events: List[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent: …`

      A user message sent to the session.

      - `content: List[Content]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock: …`

          Regular text content.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsImageBlock: …`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource: …`

              Base64-encoded image data.

              - `data: str`

                Base64-encoded image data.

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsURLImageSource: …`

              Image referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource: …`

              Image referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["image"]`

            - `"image"`

        - `class BetaManagedAgentsDocumentBlock: …`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource: …`

              Base64-encoded document data.

              - `data: str`

                Base64-encoded document data.

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsPlainTextDocumentSource: …`

              Plain text document content.

              - `data: str`

                The plain text content.

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: Literal["text"]`

                - `"text"`

            - `class BetaManagedAgentsURLDocumentSource: …`

              Document referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource: …`

              Document referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["document"]`

            - `"document"`

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

      - `type: Literal["user.message"]`

        - `"user.message"`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent: …`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: str`

        What the agent should produce. This is the task specification.

      - `rubric: Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric: …`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: str`

            ID of the rubric file.

          - `type: Literal["file"]`

            - `"file"`

        - `class BetaManagedAgentsTextRubric: …`

          Rubric content provided inline as text.

          - `content: str`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: Literal["text"]`

            - `"text"`

      - `type: Literal["user.define_outcome"]`

        - `"user.define_outcome"`

      - `max_iterations: Optional[int]`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent: …`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: List[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `type: Literal["system.message"]`

        - `"system.message"`

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: str`

    Human-readable name.

  - `paused_reason: Optional[BetaManagedAgentsDeploymentPausedReason]`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason: …`

      The caller invoked the pause endpoint on the deployment.

      - `type: Literal["manual"]`

        - `"manual"`

    - `class BetaManagedAgentsErrorDeploymentPausedReason: …`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …`

          The deployment's environment was archived.

          - `type: Literal["environment_archived_error"]`

            - `"environment_archived_error"`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …`

          The deployment's agent was archived.

          - `type: Literal["agent_archived_error"]`

            - `"agent_archived_error"`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …`

          The deployment's environment no longer exists.

          - `type: Literal["environment_not_found_error"]`

            - `"environment_not_found_error"`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …`

          A vault referenced by the deployment no longer exists.

          - `type: Literal["vault_not_found_error"]`

            - `"vault_not_found_error"`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …`

          A file resource referenced by the deployment no longer exists.

          - `type: Literal["file_not_found_error"]`

            - `"file_not_found_error"`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …`

          A referenced resource no longer exists and its kind was not reported.

          - `type: Literal["session_resource_not_found_error"]`

            - `"session_resource_not_found_error"`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …`

          The deployment's workspace was archived.

          - `type: Literal["workspace_archived_error"]`

            - `"workspace_archived_error"`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …`

          The deployment's organization is disabled.

          - `type: Literal["organization_disabled_error"]`

            - `"organization_disabled_error"`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …`

          A memory store referenced by the deployment is archived.

          - `type: Literal["memory_store_archived_error"]`

            - `"memory_store_archived_error"`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …`

          A skill referenced by the deployment's agent no longer exists.

          - `type: Literal["skill_not_found_error"]`

            - `"skill_not_found_error"`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …`

          A vault referenced by the deployment is archived.

          - `type: Literal["vault_archived_error"]`

            - `"vault_archived_error"`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError: …`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: Literal["unknown_error"]`

            - `"unknown_error"`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: Literal["self_hosted_resources_unsupported_error"]`

            - `"self_hosted_resources_unsupported_error"`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: Literal["mcp_egress_blocked_error"]`

            - `"mcp_egress_blocked_error"`

      - `type: Literal["error"]`

        - `"error"`

  - `resources: List[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig: …`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: Literal["github_repository"]`

        - `"github_repository"`

      - `url: str`

        Github URL of the repository

      - `checkout: Optional[Checkout]`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout: …`

          - `name: str`

            Branch name to check out.

          - `type: Literal["branch"]`

            - `"branch"`

        - `class BetaManagedAgentsCommitCheckout: …`

          - `sha: str`

            Full commit SHA to check out.

          - `type: Literal["commit"]`

            - `"commit"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig: …`

      A file mounted into each session's container.

      - `file_id: str`

        ID of a previously uploaded file.

      - `type: Literal["file"]`

        - `"file"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig: …`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: Literal["memory_store"]`

        - `"memory_store"`

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: Optional[BetaManagedAgentsSchedule]`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: str`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: str`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: Literal["cron"]`

      - `"cron"`

    - `last_run_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: Optional[List[datetime]]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: Literal["deployment"]`

    - `"deployment"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `vault_ids: List[str]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_deployment = client.beta.deployments.update(
    deployment_id="deployment_id",
)
print(beta_managed_agents_deployment.id)
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

`beta.deployments.archive(strdeployment_id, DeploymentArchiveParams**kwargs)  -> BetaManagedAgentsDeployment`

**post** `/v1/deployments/{deployment_id}/archive`

Archive Deployment

### Parameters

- `deployment_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]`

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

- `class BetaManagedAgentsDeployment: …`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: str`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: str`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `description: Optional[str]`

    Description of what the deployment does.

  - `environment_id: str`

    ID of the `environment` where sessions run.

  - `initial_events: List[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent: …`

      A user message sent to the session.

      - `content: List[Content]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock: …`

          Regular text content.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsImageBlock: …`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource: …`

              Base64-encoded image data.

              - `data: str`

                Base64-encoded image data.

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsURLImageSource: …`

              Image referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource: …`

              Image referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["image"]`

            - `"image"`

        - `class BetaManagedAgentsDocumentBlock: …`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource: …`

              Base64-encoded document data.

              - `data: str`

                Base64-encoded document data.

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsPlainTextDocumentSource: …`

              Plain text document content.

              - `data: str`

                The plain text content.

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: Literal["text"]`

                - `"text"`

            - `class BetaManagedAgentsURLDocumentSource: …`

              Document referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource: …`

              Document referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["document"]`

            - `"document"`

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

      - `type: Literal["user.message"]`

        - `"user.message"`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent: …`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: str`

        What the agent should produce. This is the task specification.

      - `rubric: Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric: …`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: str`

            ID of the rubric file.

          - `type: Literal["file"]`

            - `"file"`

        - `class BetaManagedAgentsTextRubric: …`

          Rubric content provided inline as text.

          - `content: str`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: Literal["text"]`

            - `"text"`

      - `type: Literal["user.define_outcome"]`

        - `"user.define_outcome"`

      - `max_iterations: Optional[int]`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent: …`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: List[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `type: Literal["system.message"]`

        - `"system.message"`

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: str`

    Human-readable name.

  - `paused_reason: Optional[BetaManagedAgentsDeploymentPausedReason]`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason: …`

      The caller invoked the pause endpoint on the deployment.

      - `type: Literal["manual"]`

        - `"manual"`

    - `class BetaManagedAgentsErrorDeploymentPausedReason: …`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …`

          The deployment's environment was archived.

          - `type: Literal["environment_archived_error"]`

            - `"environment_archived_error"`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …`

          The deployment's agent was archived.

          - `type: Literal["agent_archived_error"]`

            - `"agent_archived_error"`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …`

          The deployment's environment no longer exists.

          - `type: Literal["environment_not_found_error"]`

            - `"environment_not_found_error"`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …`

          A vault referenced by the deployment no longer exists.

          - `type: Literal["vault_not_found_error"]`

            - `"vault_not_found_error"`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …`

          A file resource referenced by the deployment no longer exists.

          - `type: Literal["file_not_found_error"]`

            - `"file_not_found_error"`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …`

          A referenced resource no longer exists and its kind was not reported.

          - `type: Literal["session_resource_not_found_error"]`

            - `"session_resource_not_found_error"`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …`

          The deployment's workspace was archived.

          - `type: Literal["workspace_archived_error"]`

            - `"workspace_archived_error"`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …`

          The deployment's organization is disabled.

          - `type: Literal["organization_disabled_error"]`

            - `"organization_disabled_error"`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …`

          A memory store referenced by the deployment is archived.

          - `type: Literal["memory_store_archived_error"]`

            - `"memory_store_archived_error"`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …`

          A skill referenced by the deployment's agent no longer exists.

          - `type: Literal["skill_not_found_error"]`

            - `"skill_not_found_error"`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …`

          A vault referenced by the deployment is archived.

          - `type: Literal["vault_archived_error"]`

            - `"vault_archived_error"`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError: …`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: Literal["unknown_error"]`

            - `"unknown_error"`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: Literal["self_hosted_resources_unsupported_error"]`

            - `"self_hosted_resources_unsupported_error"`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: Literal["mcp_egress_blocked_error"]`

            - `"mcp_egress_blocked_error"`

      - `type: Literal["error"]`

        - `"error"`

  - `resources: List[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig: …`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: Literal["github_repository"]`

        - `"github_repository"`

      - `url: str`

        Github URL of the repository

      - `checkout: Optional[Checkout]`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout: …`

          - `name: str`

            Branch name to check out.

          - `type: Literal["branch"]`

            - `"branch"`

        - `class BetaManagedAgentsCommitCheckout: …`

          - `sha: str`

            Full commit SHA to check out.

          - `type: Literal["commit"]`

            - `"commit"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig: …`

      A file mounted into each session's container.

      - `file_id: str`

        ID of a previously uploaded file.

      - `type: Literal["file"]`

        - `"file"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig: …`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: Literal["memory_store"]`

        - `"memory_store"`

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: Optional[BetaManagedAgentsSchedule]`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: str`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: str`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: Literal["cron"]`

      - `"cron"`

    - `last_run_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: Optional[List[datetime]]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: Literal["deployment"]`

    - `"deployment"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `vault_ids: List[str]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_deployment = client.beta.deployments.archive(
    deployment_id="deployment_id",
)
print(beta_managed_agents_deployment.id)
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

`beta.deployments.run(strdeployment_id, DeploymentRunParams**kwargs)  -> BetaManagedAgentsDeploymentRun`

**post** `/v1/deployments/{deployment_id}/run`

Run Deployment Now

### Parameters

- `deployment_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]`

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

- `class BetaManagedAgentsDeploymentRun: …`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `id: str`

    Unique identifier for this run (`drun_...`).

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: str`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `deployment_id: str`

    ID of the deployment that produced this run.

  - `error: Optional[Error]`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `class BetaManagedAgentsEnvironmentArchivedRunError: …`

      The deployment's environment was archived.

      - `message: str`

        Human-readable error description.

      - `type: Literal["environment_archived_error"]`

        - `"environment_archived_error"`

    - `class BetaManagedAgentsAgentArchivedRunError: …`

      The deployment's agent was archived.

      - `message: str`

        Human-readable error description.

      - `type: Literal["agent_archived_error"]`

        - `"agent_archived_error"`

    - `class BetaManagedAgentsEnvironmentNotFoundRunError: …`

      The deployment's environment no longer exists.

      - `message: str`

        Human-readable error description.

      - `type: Literal["environment_not_found_error"]`

        - `"environment_not_found_error"`

    - `class BetaManagedAgentsVaultNotFoundRunError: …`

      A vault referenced by the deployment no longer exists.

      - `message: str`

        Human-readable error description.

      - `type: Literal["vault_not_found_error"]`

        - `"vault_not_found_error"`

    - `class BetaManagedAgentsVaultArchivedRunError: …`

      A vault referenced by the deployment is archived.

      - `message: str`

        Human-readable error description.

      - `type: Literal["vault_archived_error"]`

        - `"vault_archived_error"`

    - `class BetaManagedAgentsFileNotFoundRunError: …`

      A file resource referenced by the deployment no longer exists.

      - `message: str`

        Human-readable error description.

      - `type: Literal["file_not_found_error"]`

        - `"file_not_found_error"`

    - `class BetaManagedAgentsMemoryStoreArchivedRunError: …`

      A memory store referenced by the deployment is archived.

      - `message: str`

        Human-readable error description.

      - `type: Literal["memory_store_archived_error"]`

        - `"memory_store_archived_error"`

    - `class BetaManagedAgentsSkillNotFoundRunError: …`

      A skill referenced by the deployment's agent no longer exists.

      - `message: str`

        Human-readable error description.

      - `type: Literal["skill_not_found_error"]`

        - `"skill_not_found_error"`

    - `class BetaManagedAgentsSessionResourceNotFoundRunError: …`

      A referenced resource no longer exists and its kind was not reported.

      - `message: str`

        Human-readable error description.

      - `type: Literal["session_resource_not_found_error"]`

        - `"session_resource_not_found_error"`

    - `class BetaManagedAgentsWorkspaceArchivedRunError: …`

      The deployment's workspace was archived.

      - `message: str`

        Human-readable error description.

      - `type: Literal["workspace_archived_error"]`

        - `"workspace_archived_error"`

    - `class BetaManagedAgentsOrganizationDisabledRunError: …`

      The deployment's organization is disabled.

      - `message: str`

        Human-readable error description.

      - `type: Literal["organization_disabled_error"]`

        - `"organization_disabled_error"`

    - `class BetaManagedAgentsSessionRateLimitedRunError: …`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `message: str`

        Human-readable error description.

      - `type: Literal["session_rate_limited_error"]`

        - `"session_rate_limited_error"`

    - `class BetaManagedAgentsSessionCreationRejectedRunError: …`

      The session create request was rejected with a non-retryable validation error.

      - `message: str`

        Human-readable error description.

      - `type: Literal["session_creation_rejected_error"]`

        - `"session_creation_rejected_error"`

    - `class BetaManagedAgentsUnknownRunError: …`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `message: str`

        Human-readable error description.

      - `type: Literal["unknown_error"]`

        - `"unknown_error"`

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError: …`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `message: str`

        Human-readable error description.

      - `type: Literal["self_hosted_resources_unsupported_error"]`

        - `"self_hosted_resources_unsupported_error"`

    - `class BetaManagedAgentsMCPEgressBlockedRunError: …`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `message: str`

        Human-readable error description.

      - `type: Literal["mcp_egress_blocked_error"]`

        - `"mcp_egress_blocked_error"`

  - `session_id: Optional[str]`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `trigger_context: BetaManagedAgentsTriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `class BetaManagedAgentsScheduleTriggerContext: …`

      The run was fired by the deployment's cron schedule.

      - `scheduled_at: datetime`

        A timestamp in RFC 3339 format

      - `type: Literal["schedule"]`

        - `"schedule"`

    - `class BetaManagedAgentsManualTriggerContext: …`

      The run was started manually by creating a session directly against the deployment.

      - `type: Literal["manual"]`

        - `"manual"`

  - `type: Literal["deployment_run"]`

    - `"deployment_run"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_deployment_run = client.beta.deployments.run(
    deployment_id="deployment_id",
)
print(beta_managed_agents_deployment_run.id)
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

`beta.deployments.pause(strdeployment_id, DeploymentPauseParams**kwargs)  -> BetaManagedAgentsDeployment`

**post** `/v1/deployments/{deployment_id}/pause`

Pause Deployment

### Parameters

- `deployment_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]`

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

- `class BetaManagedAgentsDeployment: …`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: str`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: str`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `description: Optional[str]`

    Description of what the deployment does.

  - `environment_id: str`

    ID of the `environment` where sessions run.

  - `initial_events: List[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent: …`

      A user message sent to the session.

      - `content: List[Content]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock: …`

          Regular text content.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsImageBlock: …`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource: …`

              Base64-encoded image data.

              - `data: str`

                Base64-encoded image data.

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsURLImageSource: …`

              Image referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource: …`

              Image referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["image"]`

            - `"image"`

        - `class BetaManagedAgentsDocumentBlock: …`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource: …`

              Base64-encoded document data.

              - `data: str`

                Base64-encoded document data.

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsPlainTextDocumentSource: …`

              Plain text document content.

              - `data: str`

                The plain text content.

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: Literal["text"]`

                - `"text"`

            - `class BetaManagedAgentsURLDocumentSource: …`

              Document referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource: …`

              Document referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["document"]`

            - `"document"`

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

      - `type: Literal["user.message"]`

        - `"user.message"`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent: …`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: str`

        What the agent should produce. This is the task specification.

      - `rubric: Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric: …`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: str`

            ID of the rubric file.

          - `type: Literal["file"]`

            - `"file"`

        - `class BetaManagedAgentsTextRubric: …`

          Rubric content provided inline as text.

          - `content: str`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: Literal["text"]`

            - `"text"`

      - `type: Literal["user.define_outcome"]`

        - `"user.define_outcome"`

      - `max_iterations: Optional[int]`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent: …`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: List[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `type: Literal["system.message"]`

        - `"system.message"`

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: str`

    Human-readable name.

  - `paused_reason: Optional[BetaManagedAgentsDeploymentPausedReason]`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason: …`

      The caller invoked the pause endpoint on the deployment.

      - `type: Literal["manual"]`

        - `"manual"`

    - `class BetaManagedAgentsErrorDeploymentPausedReason: …`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …`

          The deployment's environment was archived.

          - `type: Literal["environment_archived_error"]`

            - `"environment_archived_error"`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …`

          The deployment's agent was archived.

          - `type: Literal["agent_archived_error"]`

            - `"agent_archived_error"`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …`

          The deployment's environment no longer exists.

          - `type: Literal["environment_not_found_error"]`

            - `"environment_not_found_error"`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …`

          A vault referenced by the deployment no longer exists.

          - `type: Literal["vault_not_found_error"]`

            - `"vault_not_found_error"`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …`

          A file resource referenced by the deployment no longer exists.

          - `type: Literal["file_not_found_error"]`

            - `"file_not_found_error"`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …`

          A referenced resource no longer exists and its kind was not reported.

          - `type: Literal["session_resource_not_found_error"]`

            - `"session_resource_not_found_error"`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …`

          The deployment's workspace was archived.

          - `type: Literal["workspace_archived_error"]`

            - `"workspace_archived_error"`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …`

          The deployment's organization is disabled.

          - `type: Literal["organization_disabled_error"]`

            - `"organization_disabled_error"`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …`

          A memory store referenced by the deployment is archived.

          - `type: Literal["memory_store_archived_error"]`

            - `"memory_store_archived_error"`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …`

          A skill referenced by the deployment's agent no longer exists.

          - `type: Literal["skill_not_found_error"]`

            - `"skill_not_found_error"`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …`

          A vault referenced by the deployment is archived.

          - `type: Literal["vault_archived_error"]`

            - `"vault_archived_error"`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError: …`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: Literal["unknown_error"]`

            - `"unknown_error"`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: Literal["self_hosted_resources_unsupported_error"]`

            - `"self_hosted_resources_unsupported_error"`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: Literal["mcp_egress_blocked_error"]`

            - `"mcp_egress_blocked_error"`

      - `type: Literal["error"]`

        - `"error"`

  - `resources: List[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig: …`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: Literal["github_repository"]`

        - `"github_repository"`

      - `url: str`

        Github URL of the repository

      - `checkout: Optional[Checkout]`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout: …`

          - `name: str`

            Branch name to check out.

          - `type: Literal["branch"]`

            - `"branch"`

        - `class BetaManagedAgentsCommitCheckout: …`

          - `sha: str`

            Full commit SHA to check out.

          - `type: Literal["commit"]`

            - `"commit"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig: …`

      A file mounted into each session's container.

      - `file_id: str`

        ID of a previously uploaded file.

      - `type: Literal["file"]`

        - `"file"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig: …`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: Literal["memory_store"]`

        - `"memory_store"`

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: Optional[BetaManagedAgentsSchedule]`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: str`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: str`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: Literal["cron"]`

      - `"cron"`

    - `last_run_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: Optional[List[datetime]]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: Literal["deployment"]`

    - `"deployment"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `vault_ids: List[str]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_deployment = client.beta.deployments.pause(
    deployment_id="deployment_id",
)
print(beta_managed_agents_deployment.id)
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

`beta.deployments.unpause(strdeployment_id, DeploymentUnpauseParams**kwargs)  -> BetaManagedAgentsDeployment`

**post** `/v1/deployments/{deployment_id}/unpause`

Unpause Deployment

### Parameters

- `deployment_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]`

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

- `class BetaManagedAgentsDeployment: …`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: str`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: str`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `description: Optional[str]`

    Description of what the deployment does.

  - `environment_id: str`

    ID of the `environment` where sessions run.

  - `initial_events: List[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent: …`

      A user message sent to the session.

      - `content: List[Content]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock: …`

          Regular text content.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsImageBlock: …`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource: …`

              Base64-encoded image data.

              - `data: str`

                Base64-encoded image data.

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsURLImageSource: …`

              Image referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource: …`

              Image referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["image"]`

            - `"image"`

        - `class BetaManagedAgentsDocumentBlock: …`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource: …`

              Base64-encoded document data.

              - `data: str`

                Base64-encoded document data.

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsPlainTextDocumentSource: …`

              Plain text document content.

              - `data: str`

                The plain text content.

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: Literal["text"]`

                - `"text"`

            - `class BetaManagedAgentsURLDocumentSource: …`

              Document referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource: …`

              Document referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["document"]`

            - `"document"`

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

      - `type: Literal["user.message"]`

        - `"user.message"`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent: …`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: str`

        What the agent should produce. This is the task specification.

      - `rubric: Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric: …`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: str`

            ID of the rubric file.

          - `type: Literal["file"]`

            - `"file"`

        - `class BetaManagedAgentsTextRubric: …`

          Rubric content provided inline as text.

          - `content: str`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: Literal["text"]`

            - `"text"`

      - `type: Literal["user.define_outcome"]`

        - `"user.define_outcome"`

      - `max_iterations: Optional[int]`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent: …`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: List[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `type: Literal["system.message"]`

        - `"system.message"`

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: str`

    Human-readable name.

  - `paused_reason: Optional[BetaManagedAgentsDeploymentPausedReason]`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason: …`

      The caller invoked the pause endpoint on the deployment.

      - `type: Literal["manual"]`

        - `"manual"`

    - `class BetaManagedAgentsErrorDeploymentPausedReason: …`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …`

          The deployment's environment was archived.

          - `type: Literal["environment_archived_error"]`

            - `"environment_archived_error"`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …`

          The deployment's agent was archived.

          - `type: Literal["agent_archived_error"]`

            - `"agent_archived_error"`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …`

          The deployment's environment no longer exists.

          - `type: Literal["environment_not_found_error"]`

            - `"environment_not_found_error"`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …`

          A vault referenced by the deployment no longer exists.

          - `type: Literal["vault_not_found_error"]`

            - `"vault_not_found_error"`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …`

          A file resource referenced by the deployment no longer exists.

          - `type: Literal["file_not_found_error"]`

            - `"file_not_found_error"`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …`

          A referenced resource no longer exists and its kind was not reported.

          - `type: Literal["session_resource_not_found_error"]`

            - `"session_resource_not_found_error"`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …`

          The deployment's workspace was archived.

          - `type: Literal["workspace_archived_error"]`

            - `"workspace_archived_error"`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …`

          The deployment's organization is disabled.

          - `type: Literal["organization_disabled_error"]`

            - `"organization_disabled_error"`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …`

          A memory store referenced by the deployment is archived.

          - `type: Literal["memory_store_archived_error"]`

            - `"memory_store_archived_error"`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …`

          A skill referenced by the deployment's agent no longer exists.

          - `type: Literal["skill_not_found_error"]`

            - `"skill_not_found_error"`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …`

          A vault referenced by the deployment is archived.

          - `type: Literal["vault_archived_error"]`

            - `"vault_archived_error"`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError: …`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: Literal["unknown_error"]`

            - `"unknown_error"`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: Literal["self_hosted_resources_unsupported_error"]`

            - `"self_hosted_resources_unsupported_error"`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: Literal["mcp_egress_blocked_error"]`

            - `"mcp_egress_blocked_error"`

      - `type: Literal["error"]`

        - `"error"`

  - `resources: List[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig: …`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: Literal["github_repository"]`

        - `"github_repository"`

      - `url: str`

        Github URL of the repository

      - `checkout: Optional[Checkout]`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout: …`

          - `name: str`

            Branch name to check out.

          - `type: Literal["branch"]`

            - `"branch"`

        - `class BetaManagedAgentsCommitCheckout: …`

          - `sha: str`

            Full commit SHA to check out.

          - `type: Literal["commit"]`

            - `"commit"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig: …`

      A file mounted into each session's container.

      - `file_id: str`

        ID of a previously uploaded file.

      - `type: Literal["file"]`

        - `"file"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig: …`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: Literal["memory_store"]`

        - `"memory_store"`

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: Optional[BetaManagedAgentsSchedule]`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: str`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: str`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: Literal["cron"]`

      - `"cron"`

    - `last_run_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: Optional[List[datetime]]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: Literal["deployment"]`

    - `"deployment"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `vault_ids: List[str]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_deployment = client.beta.deployments.unpause(
    deployment_id="deployment_id",
)
print(beta_managed_agents_deployment.id)
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

- `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …`

  The deployment's agent was archived.

  - `type: Literal["agent_archived_error"]`

    - `"agent_archived_error"`

### Beta Managed Agents Cron Schedule

- `class BetaManagedAgentsCronSchedule: …`

  5-field POSIX cron schedule with computed runtime timestamps.

  - `expression: str`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `timezone: str`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

  - `type: Literal["cron"]`

    - `"cron"`

  - `last_run_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `upcoming_runs_at: Optional[List[datetime]]`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Cron Schedule Params

- `class BetaManagedAgentsCronScheduleParams: …`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `expression: str`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `timezone: str`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `type: Literal["cron"]`

    - `"cron"`

### Beta Managed Agents Deployment

- `class BetaManagedAgentsDeployment: …`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: str`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: str`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `description: Optional[str]`

    Description of what the deployment does.

  - `environment_id: str`

    ID of the `environment` where sessions run.

  - `initial_events: List[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent: …`

      A user message sent to the session.

      - `content: List[Content]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock: …`

          Regular text content.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsImageBlock: …`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource: …`

              Base64-encoded image data.

              - `data: str`

                Base64-encoded image data.

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsURLImageSource: …`

              Image referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource: …`

              Image referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["image"]`

            - `"image"`

        - `class BetaManagedAgentsDocumentBlock: …`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource: …`

              Base64-encoded document data.

              - `data: str`

                Base64-encoded document data.

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsPlainTextDocumentSource: …`

              Plain text document content.

              - `data: str`

                The plain text content.

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: Literal["text"]`

                - `"text"`

            - `class BetaManagedAgentsURLDocumentSource: …`

              Document referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource: …`

              Document referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["document"]`

            - `"document"`

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

      - `type: Literal["user.message"]`

        - `"user.message"`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent: …`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: str`

        What the agent should produce. This is the task specification.

      - `rubric: Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric: …`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: str`

            ID of the rubric file.

          - `type: Literal["file"]`

            - `"file"`

        - `class BetaManagedAgentsTextRubric: …`

          Rubric content provided inline as text.

          - `content: str`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: Literal["text"]`

            - `"text"`

      - `type: Literal["user.define_outcome"]`

        - `"user.define_outcome"`

      - `max_iterations: Optional[int]`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `class BetaManagedAgentsDeploymentSystemMessageEvent: …`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: List[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `type: Literal["system.message"]`

        - `"system.message"`

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: str`

    Human-readable name.

  - `paused_reason: Optional[BetaManagedAgentsDeploymentPausedReason]`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason: …`

      The caller invoked the pause endpoint on the deployment.

      - `type: Literal["manual"]`

        - `"manual"`

    - `class BetaManagedAgentsErrorDeploymentPausedReason: …`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …`

          The deployment's environment was archived.

          - `type: Literal["environment_archived_error"]`

            - `"environment_archived_error"`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …`

          The deployment's agent was archived.

          - `type: Literal["agent_archived_error"]`

            - `"agent_archived_error"`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …`

          The deployment's environment no longer exists.

          - `type: Literal["environment_not_found_error"]`

            - `"environment_not_found_error"`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …`

          A vault referenced by the deployment no longer exists.

          - `type: Literal["vault_not_found_error"]`

            - `"vault_not_found_error"`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …`

          A file resource referenced by the deployment no longer exists.

          - `type: Literal["file_not_found_error"]`

            - `"file_not_found_error"`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …`

          A referenced resource no longer exists and its kind was not reported.

          - `type: Literal["session_resource_not_found_error"]`

            - `"session_resource_not_found_error"`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …`

          The deployment's workspace was archived.

          - `type: Literal["workspace_archived_error"]`

            - `"workspace_archived_error"`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …`

          The deployment's organization is disabled.

          - `type: Literal["organization_disabled_error"]`

            - `"organization_disabled_error"`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …`

          A memory store referenced by the deployment is archived.

          - `type: Literal["memory_store_archived_error"]`

            - `"memory_store_archived_error"`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …`

          A skill referenced by the deployment's agent no longer exists.

          - `type: Literal["skill_not_found_error"]`

            - `"skill_not_found_error"`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …`

          A vault referenced by the deployment is archived.

          - `type: Literal["vault_archived_error"]`

            - `"vault_archived_error"`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError: …`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: Literal["unknown_error"]`

            - `"unknown_error"`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: Literal["self_hosted_resources_unsupported_error"]`

            - `"self_hosted_resources_unsupported_error"`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: Literal["mcp_egress_blocked_error"]`

            - `"mcp_egress_blocked_error"`

      - `type: Literal["error"]`

        - `"error"`

  - `resources: List[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig: …`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: Literal["github_repository"]`

        - `"github_repository"`

      - `url: str`

        Github URL of the repository

      - `checkout: Optional[Checkout]`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout: …`

          - `name: str`

            Branch name to check out.

          - `type: Literal["branch"]`

            - `"branch"`

        - `class BetaManagedAgentsCommitCheckout: …`

          - `sha: str`

            Full commit SHA to check out.

          - `type: Literal["commit"]`

            - `"commit"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig: …`

      A file mounted into each session's container.

      - `file_id: str`

        ID of a previously uploaded file.

      - `type: Literal["file"]`

        - `"file"`

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig: …`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: Literal["memory_store"]`

        - `"memory_store"`

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: Optional[BetaManagedAgentsSchedule]`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: str`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: str`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: Literal["cron"]`

      - `"cron"`

    - `last_run_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: Optional[List[datetime]]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: Literal["deployment"]`

    - `"deployment"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `vault_ids: List[str]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Beta Managed Agents Deployment Initial Event

- `BetaManagedAgentsDeploymentInitialEvent`

  An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

  - `class BetaManagedAgentsDeploymentUserMessageEvent: …`

    A user message sent to the session.

    - `content: List[Content]`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `data: str`

              Base64-encoded image data.

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["image"]`

          - `"image"`

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `data: str`

              Base64-encoded document data.

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `data: str`

              The plain text content.

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: Literal["text"]`

              - `"text"`

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["document"]`

          - `"document"`

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

    - `type: Literal["user.message"]`

      - `"user.message"`

  - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent: …`

    An outcome the agent should work toward. The agent begins work on receipt.

    - `description: str`

      What the agent should produce. This is the task specification.

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric: …`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: str`

          ID of the rubric file.

        - `type: Literal["file"]`

          - `"file"`

      - `class BetaManagedAgentsTextRubric: …`

        Rubric content provided inline as text.

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: Literal["text"]`

          - `"text"`

    - `type: Literal["user.define_outcome"]`

      - `"user.define_outcome"`

    - `max_iterations: Optional[int]`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `class BetaManagedAgentsDeploymentSystemMessageEvent: …`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks to append. Text-only.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `type: Literal["system.message"]`

      - `"system.message"`

### Beta Managed Agents Deployment Initial Event Params

- `BetaManagedAgentsDeploymentInitialEventParams`

  An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

  - `class BetaManagedAgentsUserMessageEventParams: …`

    Parameters for sending a user message to the session.

    - `content: List[Content]`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `data: str`

              Base64-encoded image data.

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["image"]`

          - `"image"`

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `data: str`

              Base64-encoded document data.

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `data: str`

              The plain text content.

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: Literal["text"]`

              - `"text"`

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["document"]`

          - `"document"`

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

    - `type: Literal["user.message"]`

      - `"user.message"`

  - `class BetaManagedAgentsUserDefineOutcomeEventParams: …`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `description: str`

      What the agent should produce. This is the task specification.

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubricParams: …`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: str`

          ID of the rubric file.

        - `type: Literal["file"]`

          - `"file"`

      - `class BetaManagedAgentsTextRubricParams: …`

        Rubric content provided inline as text.

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

        - `type: Literal["text"]`

          - `"text"`

    - `type: Literal["user.define_outcome"]`

      - `"user.define_outcome"`

    - `max_iterations: Optional[int]`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `class BetaManagedAgentsSystemMessageEventParams: …`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks to append. Text-only.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `type: Literal["system.message"]`

      - `"system.message"`

### Beta Managed Agents Deployment Paused Reason

- `BetaManagedAgentsDeploymentPausedReason`

  Why a deployment is paused. Non-null exactly when `status` is `paused`.

  - `class BetaManagedAgentsManualDeploymentPausedReason: …`

    The caller invoked the pause endpoint on the deployment.

    - `type: Literal["manual"]`

      - `"manual"`

  - `class BetaManagedAgentsErrorDeploymentPausedReason: …`

    A scheduled fire recorded a failed run whose error auto-pauses the deployment.

    - `error: BetaManagedAgentsDeploymentPausedReasonError`

      The error that triggered an auto-pause. Matches the failed run's `error.type`.

      - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …`

        The deployment's environment was archived.

        - `type: Literal["environment_archived_error"]`

          - `"environment_archived_error"`

      - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …`

        The deployment's agent was archived.

        - `type: Literal["agent_archived_error"]`

          - `"agent_archived_error"`

      - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …`

        The deployment's environment no longer exists.

        - `type: Literal["environment_not_found_error"]`

          - `"environment_not_found_error"`

      - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …`

        A vault referenced by the deployment no longer exists.

        - `type: Literal["vault_not_found_error"]`

          - `"vault_not_found_error"`

      - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …`

        A file resource referenced by the deployment no longer exists.

        - `type: Literal["file_not_found_error"]`

          - `"file_not_found_error"`

      - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …`

        A referenced resource no longer exists and its kind was not reported.

        - `type: Literal["session_resource_not_found_error"]`

          - `"session_resource_not_found_error"`

      - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …`

        The deployment's workspace was archived.

        - `type: Literal["workspace_archived_error"]`

          - `"workspace_archived_error"`

      - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …`

        The deployment's organization is disabled.

        - `type: Literal["organization_disabled_error"]`

          - `"organization_disabled_error"`

      - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …`

        A memory store referenced by the deployment is archived.

        - `type: Literal["memory_store_archived_error"]`

          - `"memory_store_archived_error"`

      - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …`

        A skill referenced by the deployment's agent no longer exists.

        - `type: Literal["skill_not_found_error"]`

          - `"skill_not_found_error"`

      - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …`

        A vault referenced by the deployment is archived.

        - `type: Literal["vault_archived_error"]`

          - `"vault_archived_error"`

      - `class BetaManagedAgentsUnknownDeploymentPausedReasonError: …`

        An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

        - `type: Literal["unknown_error"]`

          - `"unknown_error"`

      - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …`

        The deployment configures resources, but its environment is self-hosted and cannot mount them.

        - `type: Literal["self_hosted_resources_unsupported_error"]`

          - `"self_hosted_resources_unsupported_error"`

      - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …`

        An MCP server host used by the deployment's agent is blocked by the environment's network policy.

        - `type: Literal["mcp_egress_blocked_error"]`

          - `"mcp_egress_blocked_error"`

    - `type: Literal["error"]`

      - `"error"`

### Beta Managed Agents Deployment Paused Reason Error

- `BetaManagedAgentsDeploymentPausedReasonError`

  The error that triggered an auto-pause. Matches the failed run's `error.type`.

  - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …`

    The deployment's environment was archived.

    - `type: Literal["environment_archived_error"]`

      - `"environment_archived_error"`

  - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …`

    The deployment's agent was archived.

    - `type: Literal["agent_archived_error"]`

      - `"agent_archived_error"`

  - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …`

    The deployment's environment no longer exists.

    - `type: Literal["environment_not_found_error"]`

      - `"environment_not_found_error"`

  - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …`

    A vault referenced by the deployment no longer exists.

    - `type: Literal["vault_not_found_error"]`

      - `"vault_not_found_error"`

  - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …`

    A file resource referenced by the deployment no longer exists.

    - `type: Literal["file_not_found_error"]`

      - `"file_not_found_error"`

  - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …`

    A referenced resource no longer exists and its kind was not reported.

    - `type: Literal["session_resource_not_found_error"]`

      - `"session_resource_not_found_error"`

  - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …`

    The deployment's workspace was archived.

    - `type: Literal["workspace_archived_error"]`

      - `"workspace_archived_error"`

  - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …`

    The deployment's organization is disabled.

    - `type: Literal["organization_disabled_error"]`

      - `"organization_disabled_error"`

  - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …`

    A memory store referenced by the deployment is archived.

    - `type: Literal["memory_store_archived_error"]`

      - `"memory_store_archived_error"`

  - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …`

    A skill referenced by the deployment's agent no longer exists.

    - `type: Literal["skill_not_found_error"]`

      - `"skill_not_found_error"`

  - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …`

    A vault referenced by the deployment is archived.

    - `type: Literal["vault_archived_error"]`

      - `"vault_archived_error"`

  - `class BetaManagedAgentsUnknownDeploymentPausedReasonError: …`

    An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

    - `type: Literal["unknown_error"]`

      - `"unknown_error"`

  - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …`

    The deployment configures resources, but its environment is self-hosted and cannot mount them.

    - `type: Literal["self_hosted_resources_unsupported_error"]`

      - `"self_hosted_resources_unsupported_error"`

  - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …`

    An MCP server host used by the deployment's agent is blocked by the environment's network policy.

    - `type: Literal["mcp_egress_blocked_error"]`

      - `"mcp_egress_blocked_error"`

### Beta Managed Agents Deployment Status

- `Literal["active", "paused"]`

  Lifecycle status of a deployment.

  - `"active"`

  - `"paused"`

### Beta Managed Agents Deployment System Message Event

- `class BetaManagedAgentsDeploymentSystemMessageEvent: …`

  Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

  - `content: List[BetaManagedAgentsSystemContentBlock]`

    System content blocks to append. Text-only.

    - `text: str`

      The text content.

    - `type: Literal["text"]`

      - `"text"`

  - `type: Literal["system.message"]`

    - `"system.message"`

### Beta Managed Agents Deployment User Define Outcome Event

- `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent: …`

  An outcome the agent should work toward. The agent begins work on receipt.

  - `description: str`

    What the agent should produce. This is the task specification.

  - `rubric: Rubric`

    Rubric for grading the quality of an outcome.

    - `class BetaManagedAgentsFileRubric: …`

      Rubric referenced by a file uploaded via the Files API.

      - `file_id: str`

        ID of the rubric file.

      - `type: Literal["file"]`

        - `"file"`

    - `class BetaManagedAgentsTextRubric: …`

      Rubric content provided inline as text.

      - `content: str`

        Rubric content. Plain text or markdown — the grader treats it as freeform text.

      - `type: Literal["text"]`

        - `"text"`

  - `type: Literal["user.define_outcome"]`

    - `"user.define_outcome"`

  - `max_iterations: Optional[int]`

    Eval→revision cycles before giving up. Default 3, max 20.

### Beta Managed Agents Deployment User Message Event

- `class BetaManagedAgentsDeploymentUserMessageEvent: …`

  A user message sent to the session.

  - `content: List[Content]`

    Array of content blocks for the user message.

    - `class BetaManagedAgentsTextBlock: …`

      Regular text content.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `class BetaManagedAgentsImageBlock: …`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: Source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource: …`

          Base64-encoded image data.

          - `data: str`

            Base64-encoded image data.

          - `media_type: str`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: Literal["base64"]`

            - `"base64"`

        - `class BetaManagedAgentsURLImageSource: …`

          Image referenced by URL.

          - `type: Literal["url"]`

            - `"url"`

          - `url: str`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource: …`

          Image referenced by file ID.

          - `file_id: str`

            ID of a previously uploaded file.

          - `type: Literal["file"]`

            - `"file"`

      - `type: Literal["image"]`

        - `"image"`

    - `class BetaManagedAgentsDocumentBlock: …`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: Source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource: …`

          Base64-encoded document data.

          - `data: str`

            Base64-encoded document data.

          - `media_type: str`

            MIME type of the document (e.g., "application/pdf").

          - `type: Literal["base64"]`

            - `"base64"`

        - `class BetaManagedAgentsPlainTextDocumentSource: …`

          Plain text document content.

          - `data: str`

            The plain text content.

          - `media_type: Literal["text/plain"]`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsURLDocumentSource: …`

          Document referenced by URL.

          - `type: Literal["url"]`

            - `"url"`

          - `url: str`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource: …`

          Document referenced by file ID.

          - `file_id: str`

            ID of a previously uploaded file.

          - `type: Literal["file"]`

            - `"file"`

      - `type: Literal["document"]`

        - `"document"`

      - `context: Optional[str]`

        Additional context about the document for the model.

      - `title: Optional[str]`

        The title of the document.

  - `type: Literal["user.message"]`

    - `"user.message"`

### Beta Managed Agents Environment Archived Deployment Paused Reason Error

- `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …`

  The deployment's environment was archived.

  - `type: Literal["environment_archived_error"]`

    - `"environment_archived_error"`

### Beta Managed Agents Environment Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …`

  The deployment's environment no longer exists.

  - `type: Literal["environment_not_found_error"]`

    - `"environment_not_found_error"`

### Beta Managed Agents Error Deployment Paused Reason

- `class BetaManagedAgentsErrorDeploymentPausedReason: …`

  A scheduled fire recorded a failed run whose error auto-pauses the deployment.

  - `error: BetaManagedAgentsDeploymentPausedReasonError`

    The error that triggered an auto-pause. Matches the failed run's `error.type`.

    - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError: …`

      The deployment's environment was archived.

      - `type: Literal["environment_archived_error"]`

        - `"environment_archived_error"`

    - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError: …`

      The deployment's agent was archived.

      - `type: Literal["agent_archived_error"]`

        - `"agent_archived_error"`

    - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError: …`

      The deployment's environment no longer exists.

      - `type: Literal["environment_not_found_error"]`

        - `"environment_not_found_error"`

    - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …`

      A vault referenced by the deployment no longer exists.

      - `type: Literal["vault_not_found_error"]`

        - `"vault_not_found_error"`

    - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …`

      A file resource referenced by the deployment no longer exists.

      - `type: Literal["file_not_found_error"]`

        - `"file_not_found_error"`

    - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …`

      A referenced resource no longer exists and its kind was not reported.

      - `type: Literal["session_resource_not_found_error"]`

        - `"session_resource_not_found_error"`

    - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …`

      The deployment's workspace was archived.

      - `type: Literal["workspace_archived_error"]`

        - `"workspace_archived_error"`

    - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …`

      The deployment's organization is disabled.

      - `type: Literal["organization_disabled_error"]`

        - `"organization_disabled_error"`

    - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …`

      A memory store referenced by the deployment is archived.

      - `type: Literal["memory_store_archived_error"]`

        - `"memory_store_archived_error"`

    - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …`

      A skill referenced by the deployment's agent no longer exists.

      - `type: Literal["skill_not_found_error"]`

        - `"skill_not_found_error"`

    - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …`

      A vault referenced by the deployment is archived.

      - `type: Literal["vault_archived_error"]`

        - `"vault_archived_error"`

    - `class BetaManagedAgentsUnknownDeploymentPausedReasonError: …`

      An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

      - `type: Literal["unknown_error"]`

        - `"unknown_error"`

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `type: Literal["self_hosted_resources_unsupported_error"]`

        - `"self_hosted_resources_unsupported_error"`

    - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `type: Literal["mcp_egress_blocked_error"]`

        - `"mcp_egress_blocked_error"`

  - `type: Literal["error"]`

    - `"error"`

### Beta Managed Agents File Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError: …`

  A file resource referenced by the deployment no longer exists.

  - `type: Literal["file_not_found_error"]`

    - `"file_not_found_error"`

### Beta Managed Agents File Resource Config

- `class BetaManagedAgentsFileResourceConfig: …`

  A file mounted into each session's container.

  - `file_id: str`

    ID of a previously uploaded file.

  - `type: Literal["file"]`

    - `"file"`

  - `mount_path: Optional[str]`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

### Beta Managed Agents GitHub Repository Resource Config

- `class BetaManagedAgentsGitHubRepositoryResourceConfig: …`

  A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

  - `type: Literal["github_repository"]`

    - `"github_repository"`

  - `url: str`

    Github URL of the repository

  - `checkout: Optional[Checkout]`

    Branch or commit to check out. Defaults to the repository's default branch.

    - `class BetaManagedAgentsBranchCheckout: …`

      - `name: str`

        Branch name to check out.

      - `type: Literal["branch"]`

        - `"branch"`

    - `class BetaManagedAgentsCommitCheckout: …`

      - `sha: str`

        Full commit SHA to check out.

      - `type: Literal["commit"]`

        - `"commit"`

  - `mount_path: Optional[str]`

    Mount path in the container. Defaults to `/workspace/<repo-name>`.

### Beta Managed Agents Manual Deployment Paused Reason

- `class BetaManagedAgentsManualDeploymentPausedReason: …`

  The caller invoked the pause endpoint on the deployment.

  - `type: Literal["manual"]`

    - `"manual"`

### Beta Managed Agents MCP Egress Blocked Deployment Paused Reason Error

- `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError: …`

  An MCP server host used by the deployment's agent is blocked by the environment's network policy.

  - `type: Literal["mcp_egress_blocked_error"]`

    - `"mcp_egress_blocked_error"`

### Beta Managed Agents Memory Store Archived Deployment Paused Reason Error

- `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError: …`

  A memory store referenced by the deployment is archived.

  - `type: Literal["memory_store_archived_error"]`

    - `"memory_store_archived_error"`

### Beta Managed Agents Memory Store Resource Config

- `class BetaManagedAgentsMemoryStoreResourceConfig: …`

  A memory store attached to each session created from this deployment.

  - `memory_store_id: str`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `type: Literal["memory_store"]`

    - `"memory_store"`

  - `access: Optional[Literal["read_write", "read_only"]]`

    Access mode for an attached memory store.

    - `"read_write"`

    - `"read_only"`

  - `instructions: Optional[str]`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Organization Disabled Deployment Paused Reason Error

- `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError: …`

  The deployment's organization is disabled.

  - `type: Literal["organization_disabled_error"]`

    - `"organization_disabled_error"`

### Beta Managed Agents Schedule

- `class BetaManagedAgentsSchedule: …`

  5-field POSIX cron schedule with computed runtime timestamps.

  - `expression: str`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `timezone: str`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

  - `type: Literal["cron"]`

    - `"cron"`

  - `last_run_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `upcoming_runs_at: Optional[List[datetime]]`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Schedule Params

- `class BetaManagedAgentsScheduleParams: …`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `expression: str`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `timezone: str`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `type: Literal["cron"]`

    - `"cron"`

### Beta Managed Agents Self Hosted Resources Unsupported Deployment Paused Reason Error

- `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError: …`

  The deployment configures resources, but its environment is self-hosted and cannot mount them.

  - `type: Literal["self_hosted_resources_unsupported_error"]`

    - `"self_hosted_resources_unsupported_error"`

### Beta Managed Agents Session Resource Config

- `BetaManagedAgentsSessionResourceConfig`

  A configured session resource. Echoes the input minus write-only credentials.

  - `class BetaManagedAgentsGitHubRepositoryResourceConfig: …`

    A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

    - `type: Literal["github_repository"]`

      - `"github_repository"`

    - `url: str`

      Github URL of the repository

    - `checkout: Optional[Checkout]`

      Branch or commit to check out. Defaults to the repository's default branch.

      - `class BetaManagedAgentsBranchCheckout: …`

        - `name: str`

          Branch name to check out.

        - `type: Literal["branch"]`

          - `"branch"`

      - `class BetaManagedAgentsCommitCheckout: …`

        - `sha: str`

          Full commit SHA to check out.

        - `type: Literal["commit"]`

          - `"commit"`

    - `mount_path: Optional[str]`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

  - `class BetaManagedAgentsFileResourceConfig: …`

    A file mounted into each session's container.

    - `file_id: str`

      ID of a previously uploaded file.

    - `type: Literal["file"]`

      - `"file"`

    - `mount_path: Optional[str]`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  - `class BetaManagedAgentsMemoryStoreResourceConfig: …`

    A memory store attached to each session created from this deployment.

    - `memory_store_id: str`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: Literal["memory_store"]`

      - `"memory_store"`

    - `access: Optional[Literal["read_write", "read_only"]]`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `instructions: Optional[str]`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Session Resource Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError: …`

  A referenced resource no longer exists and its kind was not reported.

  - `type: Literal["session_resource_not_found_error"]`

    - `"session_resource_not_found_error"`

### Beta Managed Agents Skill Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError: …`

  A skill referenced by the deployment's agent no longer exists.

  - `type: Literal["skill_not_found_error"]`

    - `"skill_not_found_error"`

### Beta Managed Agents Unknown Deployment Paused Reason Error

- `class BetaManagedAgentsUnknownDeploymentPausedReasonError: …`

  An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

  - `type: Literal["unknown_error"]`

    - `"unknown_error"`

### Beta Managed Agents Vault Archived Deployment Paused Reason Error

- `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError: …`

  A vault referenced by the deployment is archived.

  - `type: Literal["vault_archived_error"]`

    - `"vault_archived_error"`

### Beta Managed Agents Vault Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError: …`

  A vault referenced by the deployment no longer exists.

  - `type: Literal["vault_not_found_error"]`

    - `"vault_not_found_error"`

### Beta Managed Agents Workspace Archived Deployment Paused Reason Error

- `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError: …`

  The deployment's workspace was archived.

  - `type: Literal["workspace_archived_error"]`

    - `"workspace_archived_error"`
