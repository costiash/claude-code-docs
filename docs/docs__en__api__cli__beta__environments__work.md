# Work

## Retrieve

`$ ant beta:environments:work retrieve`

**get** `/v1/environments/{environment_id}/work/{work_id}`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Retrieve detailed information about a specific work item.

### Parameters

- `--environment-id: string`

  Path param

- `--work-id: string`

  Path param

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

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
ant beta:environments:work retrieve \
  --api-key my-anthropic-api-key \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW \
  --work-id work_id
```

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

## Ack

`$ ant beta:environments:work ack`

**post** `/v1/environments/{environment_id}/work/{work_id}/ack`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Acknowledge receipt of a work item, transitioning it from 'queued' to 'starting' and removing it from the queue.

### Parameters

- `--environment-id: string`

  Path param

- `--work-id: string`

  Path param

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

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
ant beta:environments:work ack \
  --api-key my-anthropic-api-key \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW \
  --work-id work_id
```

## Heartbeat

`$ ant beta:environments:work heartbeat`

**post** `/v1/environments/{environment_id}/work/{work_id}/heartbeat`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Record a heartbeat for a work item to maintain the lease.

### Parameters

- `--environment-id: string`

  Path param

- `--work-id: string`

  Path param

- `--desired-ttl-seconds: optional number`

  Query param: Desired TTL in seconds

- `--expected-last-heartbeat: optional string`

  Query param: Expected last_heartbeat for conditional update (optimistic concurrency). Use literal 'NO_HEARTBEAT' to claim an unclaimed lease (first heartbeat). For subsequent heartbeats, echo the server's previous last_heartbeat value exactly. Returns 412 Precondition Failed if the actual value doesn't match.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_self_hosted_work_heartbeat_response: object { last_heartbeat, lease_extended, state, 2 more }`

  Response after recording a heartbeat for a work item.

  - `last_heartbeat: string`

    RFC 3339 timestamp of the actual heartbeat from DB

  - `lease_extended: boolean`

    Whether the heartbeat succeeded in extending the lease

  - `state: "queued" or "starting" or "active" or 2 more`

    Current state of the work item (active/stopping/stopped)

    - `"queued"`

    - `"starting"`

    - `"active"`

    - `"stopping"`

    - `"stopped"`

  - `ttl_seconds: number`

    Effective TTL applied to the lease

  - `type: "work_heartbeat"`

    The type of response

### Example

```cli
ant beta:environments:work heartbeat \
  --api-key my-anthropic-api-key \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW \
  --work-id work_id
```

## Stop

`$ ant beta:environments:work stop`

**post** `/v1/environments/{environment_id}/work/{work_id}/stop`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Stop a work item, initiating graceful or forced shutdown.

### Parameters

- `--environment-id: string`

  Path param

- `--work-id: string`

  Path param

- `--force: optional boolean`

  Body param: If true, immediately stop work without graceful shutdown

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

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
ant beta:environments:work stop \
  --api-key my-anthropic-api-key \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW \
  --work-id work_id
```

## List

`$ ant beta:environments:work list`

**get** `/v1/environments/{environment_id}/work`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

List work items in an environment.

### Parameters

- `--environment-id: string`

  Path param

- `--limit: optional number`

  Query param: Maximum number of work items to return

- `--page: optional string`

  Query param: Opaque cursor from previous response for pagination

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_self_hosted_work_list_response: object { data, next_page }`

  Response when listing work items with cursor-based pagination.

  - `data: array of BetaSelfHostedWork`

    List of work items

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

  - `next_page: string`

    Opaque cursor for fetching the next page of results

### Example

```cli
ant beta:environments:work list \
  --api-key my-anthropic-api-key \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW
```

## Update

`$ ant beta:environments:work update`

**post** `/v1/environments/{environment_id}/work/{work_id}`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Update work item metadata with merge semantics.

### Parameters

- `--environment-id: string`

  Path param

- `--work-id: string`

  Path param

- `--metadata: map[string]`

  Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

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
ant beta:environments:work update \
  --api-key my-anthropic-api-key \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW \
  --work-id work_id \
  --metadata '{foo: string}'
```

## Stats

`$ ant beta:environments:work stats`

**get** `/v1/environments/{environment_id}/work/stats`

Get statistics about the work queue for an environment.

### Parameters

- `--environment-id: string`

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_self_hosted_work_queue_stats: object { depth, oldest_queued_at, pending, 2 more }`

  Statistics about the work queue for an environment.

  Uses Redis Stream consumer group metrics for O(1) queries.

  - `depth: number`

    Number of work items waiting to be picked up (lag from consumer group)

  - `oldest_queued_at: string`

    RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

  - `pending: number`

    Number of work items being processed (polled but not acknowledged)

  - `type: "work_queue_stats"`

    The type of object

  - `workers_polling: number`

    Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.

### Example

```cli
ant beta:environments:work stats \
  --api-key my-anthropic-api-key \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW
```

## Domain Types

### Beta Self Hosted Work

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

### Beta Self Hosted Work Heartbeat Response

- `beta_self_hosted_work_heartbeat_response: object { last_heartbeat, lease_extended, state, 2 more }`

  Response after recording a heartbeat for a work item.

  - `last_heartbeat: string`

    RFC 3339 timestamp of the actual heartbeat from DB

  - `lease_extended: boolean`

    Whether the heartbeat succeeded in extending the lease

  - `state: "queued" or "starting" or "active" or 2 more`

    Current state of the work item (active/stopping/stopped)

    - `"queued"`

    - `"starting"`

    - `"active"`

    - `"stopping"`

    - `"stopped"`

  - `ttl_seconds: number`

    Effective TTL applied to the lease

  - `type: "work_heartbeat"`

    The type of response

### Beta Self Hosted Work List Response

- `beta_self_hosted_work_list_response: object { data, next_page }`

  Response when listing work items with cursor-based pagination.

  - `data: array of BetaSelfHostedWork`

    List of work items

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

  - `next_page: string`

    Opaque cursor for fetching the next page of results

### Beta Self Hosted Work Queue Stats

- `beta_self_hosted_work_queue_stats: object { depth, oldest_queued_at, pending, 2 more }`

  Statistics about the work queue for an environment.

  Uses Redis Stream consumer group metrics for O(1) queries.

  - `depth: number`

    Number of work items waiting to be picked up (lag from consumer group)

  - `oldest_queued_at: string`

    RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

  - `pending: number`

    Number of work items being processed (polled but not acknowledged)

  - `type: "work_queue_stats"`

    The type of object

  - `workers_polling: number`

    Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.

### Beta Self Hosted Work Stop Request

- `beta_self_hosted_work_stop_request: object { force }`

  Request to stop a work item.

  - `force: optional boolean`

    If true, immediately stop work without graceful shutdown

### Beta Self Hosted Work Update Request

- `beta_self_hosted_work_update_request: object { metadata }`

  Request to update work item metadata.

  - `metadata: map[string]`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

### Beta Session Work Data

- `beta_session_work_data: object { id, type }`

  Work data for session work items.

  This resource type is used when work represents a session that needs to be executed
  in a self-hosted environment.

  - `id: string`

    Session identifier (e.g., 'session_...')

  - `type: "session"`

    Type of work data
