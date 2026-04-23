## List

`$ ant beta:memory-stores:memory-versions list`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions`

ListMemoryVersions

### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--api-key-id: optional string`

  Query param: Query parameter for api_key_id

- `--created-at-gte: optional string`

  Query param: Return versions created at or after this time (inclusive).

- `--created-at-lte: optional string`

  Query param: Return versions created at or before this time (inclusive).

- `--limit: optional number`

  Query param: Query parameter for limit

- `--memory-id: optional string`

  Query param: Query parameter for memory_id

- `--operation: optional "created" or "modified" or "deleted"`

  Query param: Query parameter for operation

- `--page: optional string`

  Query param: Query parameter for page

- `--session-id: optional string`

  Query param: Query parameter for session_id

- `--view: optional "basic" or "full"`

  Query param: Query parameter for view

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsListMemoryVersionsResult: object { data, next_page }`

  - `data: optional array of BetaManagedAgentsMemoryVersion`

    - `id: string`

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `memory_id: string`

    - `memory_store_id: string`

    - `operation: "created" or "modified" or "deleted"`

      MemoryVersionOperation enum

      - `"created"`

      - `"modified"`

      - `"deleted"`

    - `type: "memory_version"`

      - `"memory_version"`

    - `content: optional string`

    - `content_sha256: optional string`

    - `content_size_bytes: optional number`

    - `created_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor`

      - `beta_managed_agents_session_actor: object { session_id, type }`

        - `session_id: string`

        - `type: "session_actor"`

          - `"session_actor"`

      - `beta_managed_agents_api_actor: object { api_key_id, type }`

        - `api_key_id: string`

        - `type: "api_actor"`

          - `"api_actor"`

      - `beta_managed_agents_user_actor: object { type, user_id }`

        - `type: "user_actor"`

          - `"user_actor"`

        - `user_id: string`

    - `path: optional string`

    - `redacted_at: optional string`

      A timestamp in RFC 3339 format

    - `redacted_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor`

      - `beta_managed_agents_session_actor: object { session_id, type }`

        - `session_id: string`

        - `type: "session_actor"`

          - `"session_actor"`

      - `beta_managed_agents_api_actor: object { api_key_id, type }`

        - `api_key_id: string`

        - `type: "api_actor"`

          - `"api_actor"`

      - `beta_managed_agents_user_actor: object { type, user_id }`

        - `type: "user_actor"`

          - `"user_actor"`

        - `user_id: string`

  - `next_page: optional string`

### Example

```cli
ant beta:memory-stores:memory-versions list \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```
