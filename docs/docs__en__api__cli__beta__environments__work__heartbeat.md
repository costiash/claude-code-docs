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
