## List

**get** `/v1/memory_stores/{memory_store_id}/memory_versions`

ListMemoryVersions

### Path Parameters

- `memory_store_id: string`

### Query Parameters

- `api_key_id: optional string`

  Query parameter for api_key_id

- `"created_at[gte]": optional string`

  Return versions created at or after this time (inclusive).

- `"created_at[lte]": optional string`

  Return versions created at or before this time (inclusive).

- `limit: optional number`

  Query parameter for limit

- `memory_id: optional string`

  Query parameter for memory_id

- `operation: optional BetaManagedAgentsMemoryVersionOperation`

  Query parameter for operation

  - `"created"`

  - `"modified"`

  - `"deleted"`

- `page: optional string`

  Query parameter for page

- `session_id: optional string`

  Query parameter for session_id

- `view: optional BetaManagedAgentsMemoryView`

  Query parameter for view

  - `"basic"`

  - `"full"`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 19 more`

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

    - `"advisor-tool-2026-03-01"`

### Returns

- `data: optional array of BetaManagedAgentsMemoryVersion`

  - `id: string`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `memory_id: string`

  - `memory_store_id: string`

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    MemoryVersionOperation enum

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `type: "memory_version"`

    - `"memory_version"`

  - `content: optional string`

  - `content_sha256: optional string`

  - `content_size_bytes: optional number`

  - `created_by: optional BetaManagedAgentsActor`

    - `BetaManagedAgentsSessionActor = object { session_id, type }`

      - `session_id: string`

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor = object { api_key_id, type }`

      - `api_key_id: string`

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor = object { type, user_id }`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

  - `path: optional string`

  - `redacted_at: optional string`

    A timestamp in RFC 3339 format

  - `redacted_by: optional BetaManagedAgentsActor`

    - `BetaManagedAgentsSessionActor = object { session_id, type }`

      - `session_id: string`

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor = object { api_key_id, type }`

      - `api_key_id: string`

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor = object { type, user_id }`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

- `next_page: optional string`

### Example

```http
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memory_versions \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```
