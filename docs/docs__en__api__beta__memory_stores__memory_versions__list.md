## List

**get** `/v1/memory_stores/{memory_store_id}/memory_versions`

List memory versions

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

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 20 more`

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

### Returns

- `data: optional array of BetaManagedAgentsMemoryVersion`

  One page of `memory_version` objects, ordered by `created_at` descending (newest first), with `id` as tiebreak.

  - `id: string`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `memory_id: string`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `memory_store_id: string`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `type: "memory_version"`

    - `"memory_version"`

  - `content: optional string`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: optional string`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: optional number`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `created_by: optional BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `BetaManagedAgentsSessionActor = object { session_id, type }`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `session_id: string`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor = object { api_key_id, type }`

      Attribution for a write made directly via the public API (outside of any session).

      - `api_key_id: string`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor = object { type, user_id }`

      Attribution for a write made by a human user through the Anthropic Console.

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

        ID of the user who performed the write (a `user_...` value).

  - `path: optional string`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: optional string`

    A timestamp in RFC 3339 format

  - `redacted_by: optional BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `BetaManagedAgentsSessionActor = object { session_id, type }`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `session_id: string`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor = object { api_key_id, type }`

      Attribution for a write made directly via the public API (outside of any session).

      - `api_key_id: string`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor = object { type, user_id }`

      Attribution for a write made by a human user through the Anthropic Console.

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

        ID of the user who performed the write (a `user_...` value).

- `next_page: optional string`

  Opaque cursor for the next page (a `page_...` value), or `null` if there are no more results. Pass as `page` on the next request.

### Example

```http
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memory_versions \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```
