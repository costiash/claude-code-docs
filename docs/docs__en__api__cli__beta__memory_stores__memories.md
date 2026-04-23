# Memories

## Create

`$ ant beta:memory-stores:memories create`

**post** `/v1/memory_stores/{memory_store_id}/memories`

CreateMemory

### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--content: string`

  Body param

- `--path: string`

  Body param

- `--view: optional "basic" or "full"`

  Query param: Query parameter for view

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
ant beta:memory-stores:memories create \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id \
  --content content \
  --path xx
```

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

## Retrieve

`$ ant beta:memory-stores:memories retrieve`

**get** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

GetMemory

### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--memory-id: string`

  Path param: Path parameter memory_id

- `--view: optional "basic" or "full"`

  Query param: Query parameter for view

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
ant beta:memory-stores:memories retrieve \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id \
  --memory-id memory_id
```

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

## Delete

`$ ant beta:memory-stores:memories delete`

**delete** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

DeleteMemory

### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--memory-id: string`

  Path param: Path parameter memory_id

- `--expected-content-sha256: optional string`

  Query param: Query parameter for expected_content_sha256

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deleted_memory: object { id, type }`

  - `id: string`

  - `type: "memory_deleted"`

    - `"memory_deleted"`

### Example

```cli
ant beta:memory-stores:memories delete \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id \
  --memory-id memory_id
```

## Domain Types

### Beta Managed Agents Content Sha256 Precondition

- `beta_managed_agents_content_sha256_precondition: object { type, content_sha256 }`

  - `type: "content_sha256"`

    - `"content_sha256"`

  - `content_sha256: optional string`

### Beta Managed Agents Deleted Memory

- `beta_managed_agents_deleted_memory: object { id, type }`

  - `id: string`

  - `type: "memory_deleted"`

    - `"memory_deleted"`

### Beta Managed Agents Memory

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

### Beta Managed Agents Memory List Item

- `beta_managed_agents_memory_list_item: BetaManagedAgentsMemory or BetaManagedAgentsMemoryPrefix`

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

### Beta Managed Agents Memory Path Conflict Error

- `beta_managed_agents_memory_path_conflict_error: object { type, conflicting_memory_id, conflicting_path, message }`

  - `type: "memory_path_conflict_error"`

    - `"memory_path_conflict_error"`

  - `conflicting_memory_id: optional string`

  - `conflicting_path: optional string`

  - `message: optional string`

### Beta Managed Agents Memory Precondition Failed Error

- `beta_managed_agents_memory_precondition_failed_error: object { type, message }`

  - `type: "memory_precondition_failed_error"`

    - `"memory_precondition_failed_error"`

  - `message: optional string`

### Beta Managed Agents Memory Prefix

- `beta_managed_agents_memory_prefix: object { path, type }`

  - `path: string`

  - `type: "memory_prefix"`

    - `"memory_prefix"`

### Beta Managed Agents Memory View

- `beta_managed_agents_memory_view: "basic" or "full"`

  MemoryView enum

  - `"basic"`

  - `"full"`

### Beta Managed Agents Precondition

- `beta_managed_agents_precondition: object { type, content_sha256 }`

  - `type: "content_sha256"`

    - `"content_sha256"`

  - `content_sha256: optional string`
