## List Work Items

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

#### Response

```json
{
  "data": [
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
  ],
  "next_page": "next_page"
}
```
