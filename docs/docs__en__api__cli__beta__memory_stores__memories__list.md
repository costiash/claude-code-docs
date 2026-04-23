## List

`$ ant beta:memory-stores:memories list`

**get** `/v1/memory_stores/{memory_store_id}/memories`

ListMemories

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

  - `data: optional array of BetaManagedAgentsMemoryListItem`

    - `beta_managed_agents_memory: object { id, content_sha256, content_size_bytes, 7 more }`

      - `id: string`

      - `content_sha256: string`

      - `content_size_bytes: number`

      - `created_at: string`

        A timestamp in RFC 3339 format

      - `memory_store_id: string`

      - `memory_version_id: string`

      - `path: string`

      - `type: "memory"`

        - `"memory"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

      - `content: optional string`

    - `beta_managed_agents_memory_prefix: object { path, type }`

      - `path: string`

      - `type: "memory_prefix"`

        - `"memory_prefix"`

  - `next_page: optional string`

### Example

```cli
ant beta:memory-stores:memories list \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```
