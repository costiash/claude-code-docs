## List

`$ ant beta:memory-stores list`

**get** `/v1/memory_stores`

ListMemoryStores

### Parameters

- `--created-at-gte: optional string`

  Query param: Return stores created at or after this time (inclusive).

- `--created-at-lte: optional string`

  Query param: Return stores created at or before this time (inclusive).

- `--include-archived: optional boolean`

  Query param: Query parameter for include_archived

- `--limit: optional number`

  Query param: Query parameter for limit

- `--page: optional string`

  Query param: Query parameter for page

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsListMemoryStoresResponse: object { data, next_page }`

  - `data: optional array of BetaManagedAgentsMemoryStore`

    - `id: string`

    - `type: "memory_store"`

      - `"memory_store"`

    - `archived_at: optional string`

      A timestamp in RFC 3339 format

    - `created_at: optional string`

      A timestamp in RFC 3339 format

    - `description: optional string`

    - `metadata: optional map[string]`

    - `name: optional string`

    - `updated_at: optional string`

      A timestamp in RFC 3339 format

  - `next_page: optional string`

### Example

```cli
ant beta:memory-stores list \
  --api-key my-anthropic-api-key
```
