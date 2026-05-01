## List

`$ ant beta:memory-stores:memories list`

**get** `/v1/memory_stores/{memory_store_id}/memories`

List memories

### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--depth: optional number`

  Query param: Query parameter for depth

- `--limit: optional number`

  Query param: Query parameter for limit

- `--order: optional "asc" or "desc"`

  Query param: Query parameter for order

- `--order-by: optional string`

  Query param: Query parameter for order_by

- `--page: optional string`

  Query param: Query parameter for page

- `--path-prefix: optional string`

  Query param: Optional path prefix filter (raw string-prefix match; include a trailing slash for directory-scoped lists). This value appears in request URLs. Do not include secrets or personally identifiable information.

- `--view: optional "basic" or "full"`

  Query param: Query parameter for view

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsListMemoriesResult: object { data, next_page }`

  Response payload for [List memories](/docs/en/api/beta/memory_stores/memories/list).

  - `data: optional array of BetaManagedAgentsMemoryListItem`

    One page of results. Each item is either a `memory` object or, when `depth` was set, a `memory_prefix` rollup marker. Items appear in the requested `order_by`/`order`.

    - `beta_managed_agents_memory: object { id, content_sha256, content_size_bytes, 7 more }`

      A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

      - `id: string`

        Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

      - `content_sha256: string`

        Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

      - `content_size_bytes: number`

        Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

      - `created_at: string`

        A timestamp in RFC 3339 format

      - `memory_store_id: string`

        ID of the memory store this memory belongs to (a `memstore_...` value).

      - `memory_version_id: string`

        ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

      - `path: string`

        Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

      - `type: "memory"`

        - `"memory"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

      - `content: optional string`

        The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

    - `beta_managed_agents_memory_prefix: object { path, type }`

      A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

      - `path: string`

        The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

      - `type: "memory_prefix"`

        - `"memory_prefix"`

  - `next_page: optional string`

    Opaque cursor for the next page (a `page_...` value), or `null` if there are no more results. Pass as `page` on the next request.

### Example

```cli
ant beta:memory-stores:memories list \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```
