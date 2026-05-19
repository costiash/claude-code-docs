## Poll

`$ ant beta:environments:work poll`

**get** `/v1/environments/{environment_id}/work/poll`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Long poll for work items in the queue.

### Parameters

- `--environment-id: string`

  Path param

- `--block-ms: optional number`

  Query param: How long to wait for work to arrive before returning. Must be 1-999 in milliseconds. Defaults to non-blocking (returns immediately if no work is available).

- `--reclaim-older-than-ms: optional number`

  Query param: Reclaim unacknowledged work items older than this many milliseconds. If omitted, uses the default (5000ms).

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

- `--anthropic-worker-id: optional string`

  Header param: Unique identifier for the specific worker polling, used to track aggregated environment-level work metrics in Console

### Returns

- `beta_self_hosted_work: object { id, acknowledged_at, created_at, 9 more }`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `id: string`

    Work identifier (e.g., 'work_...')

  - `acknowledged_at: string`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `created_at: string`

    RFC 3339 timestamp when work was created

  - `data: object { id, type }`

    The actual work to be performed

    - `id: string`

      Session identifier (e.g., 'session_...')

    - `type: "session"`

      Type of work data

  - `environment_id: string`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `latest_heartbeat_at: string`

    RFC 3339 timestamp of the most recent heartbeat

  - `metadata: map[string]`

    User-provided metadata key-value pairs associated with this work item

  - `started_at: string`

    RFC 3339 timestamp when work execution started

  - `state: "queued" or "starting" or "active" or 2 more`

    Current state of the work item

    - `"queued"`

    - `"starting"`

    - `"active"`

    - `"stopping"`

    - `"stopped"`

  - `stop_requested_at: string`

    RFC 3339 timestamp when stop was requested

  - `stopped_at: string`

    RFC 3339 timestamp when work execution stopped

  - `type: "work"`

    The type of object (always 'work')

### Example

```cli
ant beta:environments:work poll \
  --api-key my-anthropic-api-key \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW
```
