## Update

`$ ant beta:memory-stores:memories update`

**post** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

UpdateMemory

### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--memory-id: string`

  Path param: Path parameter memory_id

- `--view: optional "basic" or "full"`

  Query param: Query parameter for view

- `--content: optional string`

  Body param

- `--path: optional string`

  Body param

- `--precondition: optional object { type, content_sha256 }`

  Body param

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

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

### Example

```cli
ant beta:memory-stores:memories update \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id \
  --memory-id memory_id
```
