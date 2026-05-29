## Stop Work

`beta.environments.work.stop(work_id, **kwargs) -> BetaSelfHostedWork`

**post** `/v1/environments/{environment_id}/work/{work_id}/stop`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Stop a work item, initiating graceful or forced shutdown.

### Parameters

- `environment_id: String`

- `work_id: String`

- `force: bool`

  If true, immediately stop work without graceful shutdown

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 24 more`

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

    - `:"mid-conversation-system-2026-04-07"`

### Returns

- `class BetaSelfHostedWork`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `id: String`

    Work identifier (e.g., 'work_...')

  - `acknowledged_at: String`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `created_at: String`

    RFC 3339 timestamp when work was created

  - `data: BetaSessionWorkData`

    The actual work to be performed

    - `id: String`

      Session identifier (e.g., 'session_...')

    - `type: :session`

      Type of work data

      - `:session`

  - `environment_id: String`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `latest_heartbeat_at: String`

    RFC 3339 timestamp of the most recent heartbeat

  - `metadata: Hash[Symbol, String]`

    User-provided metadata key-value pairs associated with this work item

  - `started_at: String`

    RFC 3339 timestamp when work execution started

  - `state: :queued | :starting | :active | 2 more`

    Current state of the work item

    - `:queued`

    - `:starting`

    - `:active`

    - `:stopping`

    - `:stopped`

  - `stop_requested_at: String`

    RFC 3339 timestamp when stop was requested

  - `stopped_at: String`

    RFC 3339 timestamp when work execution stopped

  - `type: :work`

    The type of object (always 'work')

    - `:work`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_self_hosted_work = anthropic.beta.environments.work.stop("work_id", environment_id: "env_011CZkZ9X2dpNyB7HsEFoRfW")

puts(beta_self_hosted_work)
```

#### Response

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```
