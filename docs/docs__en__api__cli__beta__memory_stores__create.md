## Create

`$ ant beta:memory-stores create`

**post** `/v1/memory_stores`

CreateMemoryStore

### Parameters

- `--name: string`

  Body param

- `--description: optional string`

  Body param

- `--metadata: optional map[string]`

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
ant beta:memory-stores create \
  --api-key my-anthropic-api-key \
  --name x
```
