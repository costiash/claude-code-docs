## Update

`$ ant beta:memory-stores update`

**post** `/v1/memory_stores/{memory_store_id}`

UpdateMemoryStore

### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--description: optional string`

  Body param

- `--metadata: optional map[string]`

  Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `--name: optional string`

  Body param

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_memory_store: object { id, type, archived_at, 5 more }`

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

### Example

```cli
ant beta:memory-stores update \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```
