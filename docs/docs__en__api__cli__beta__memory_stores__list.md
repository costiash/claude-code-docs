## List

`$ ant beta:memory-stores list`

**get** `/v1/memory_stores`

List memory stores

### Parameters

- `--created-at-gte: optional string`

  Query param: Return only stores whose `created_at` is at or after this time (inclusive). Sent on the wire as `created_at[gte]`.

- `--created-at-lte: optional string`

  Query param: Return only stores whose `created_at` is at or before this time (inclusive). Sent on the wire as `created_at[lte]`.

- `--include-archived: optional boolean`

  Query param: When `true`, archived stores are included in the results. Defaults to `false` (archived stores are excluded).

- `--limit: optional number`

  Query param: Maximum number of stores to return per page. Must be between 1 and 100. Defaults to 20 when omitted.

- `--page: optional string`

  Query param: Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsListMemoryStoresResponse: object { data, next_page }`

  A page of `memory_store` results, ordered by `created_at` descending (newest first).

  - `data: optional array of BetaManagedAgentsMemoryStore`

    Memory stores on this page, newest first. Empty when there are no stores matching the filters.

    - `id: string`

      Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `name: string`

      Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

    - `type: "memory_store"`

      - `"memory_store"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

    - `archived_at: optional string`

      A timestamp in RFC 3339 format

    - `description: optional string`

      Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

    - `metadata: optional map[string]`

      Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

  - `next_page: optional string`

    Opaque cursor for the next page (a `page_...` value). Pass as `page` on the next request. `null` when there are no more results.

### Example

```cli
ant beta:memory-stores list \
  --api-key my-anthropic-api-key
```
