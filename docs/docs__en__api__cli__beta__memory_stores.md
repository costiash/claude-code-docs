# Memory Stores

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

## Retrieve

`$ ant beta:memory-stores retrieve`

**get** `/v1/memory_stores/{memory_store_id}`

GetMemoryStore

### Parameters

- `--memory-store-id: string`

  Path parameter memory_store_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

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
ant beta:memory-stores retrieve \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```

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

## Delete

`$ ant beta:memory-stores delete`

**delete** `/v1/memory_stores/{memory_store_id}`

DeleteMemoryStore

### Parameters

- `--memory-store-id: string`

  Path parameter memory_store_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deleted_memory_store: object { id, type }`

  - `id: string`

  - `type: "memory_store_deleted"`

    - `"memory_store_deleted"`

### Example

```cli
ant beta:memory-stores delete \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```

## Archive

`$ ant beta:memory-stores archive`

**post** `/v1/memory_stores/{memory_store_id}/archive`

ArchiveMemoryStore

### Parameters

- `--memory-store-id: string`

  Path parameter memory_store_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

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
ant beta:memory-stores archive \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```

## Domain Types

### Beta Managed Agents Deleted Memory Store

- `beta_managed_agents_deleted_memory_store: object { id, type }`

  - `id: string`

  - `type: "memory_store_deleted"`

    - `"memory_store_deleted"`

### Beta Managed Agents Memory Store

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

# Memory Versions

## List

`$ ant beta:memory-stores:memory-versions list`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions`

ListMemoryVersions

### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--api-key-id: optional string`

  Query param: Query parameter for api_key_id

- `--created-at-gte: optional string`

  Query param: Return versions created at or after this time (inclusive).

- `--created-at-lte: optional string`

  Query param: Return versions created at or before this time (inclusive).

- `--limit: optional number`

  Query param: Query parameter for limit

- `--memory-id: optional string`

  Query param: Query parameter for memory_id

- `--operation: optional "created" or "modified" or "deleted"`

  Query param: Query parameter for operation

- `--page: optional string`

  Query param: Query parameter for page

- `--session-id: optional string`

  Query param: Query parameter for session_id

- `--view: optional "basic" or "full"`

  Query param: Query parameter for view

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsListMemoryVersionsResult: object { data, next_page }`

  - `data: optional array of BetaManagedAgentsMemoryVersion`

    - `id: string`

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `memory_id: string`

    - `memory_store_id: string`

    - `operation: "created" or "modified" or "deleted"`

      MemoryVersionOperation enum

      - `"created"`

      - `"modified"`

      - `"deleted"`

    - `type: "memory_version"`

      - `"memory_version"`

    - `content: optional string`

    - `content_sha256: optional string`

    - `content_size_bytes: optional number`

    - `created_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor`

      - `beta_managed_agents_session_actor: object { session_id, type }`

        - `session_id: string`

        - `type: "session_actor"`

          - `"session_actor"`

      - `beta_managed_agents_api_actor: object { api_key_id, type }`

        - `api_key_id: string`

        - `type: "api_actor"`

          - `"api_actor"`

      - `beta_managed_agents_user_actor: object { type, user_id }`

        - `type: "user_actor"`

          - `"user_actor"`

        - `user_id: string`

    - `path: optional string`

    - `redacted_at: optional string`

      A timestamp in RFC 3339 format

    - `redacted_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor`

      - `beta_managed_agents_session_actor: object { session_id, type }`

        - `session_id: string`

        - `type: "session_actor"`

          - `"session_actor"`

      - `beta_managed_agents_api_actor: object { api_key_id, type }`

        - `api_key_id: string`

        - `type: "api_actor"`

          - `"api_actor"`

      - `beta_managed_agents_user_actor: object { type, user_id }`

        - `type: "user_actor"`

          - `"user_actor"`

        - `user_id: string`

  - `next_page: optional string`

### Example

```cli
ant beta:memory-stores:memory-versions list \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```

## Retrieve

`$ ant beta:memory-stores:memory-versions retrieve`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

GetMemoryVersion

### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--memory-version-id: string`

  Path param: Path parameter memory_version_id

- `--view: optional "basic" or "full"`

  Query param: Query parameter for view

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_memory_version: object { id, created_at, memory_id, 10 more }`

  - `id: string`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `memory_id: string`

  - `memory_store_id: string`

  - `operation: "created" or "modified" or "deleted"`

    MemoryVersionOperation enum

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `type: "memory_version"`

    - `"memory_version"`

  - `content: optional string`

  - `content_sha256: optional string`

  - `content_size_bytes: optional number`

  - `created_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor`

    - `beta_managed_agents_session_actor: object { session_id, type }`

      - `session_id: string`

      - `type: "session_actor"`

        - `"session_actor"`

    - `beta_managed_agents_api_actor: object { api_key_id, type }`

      - `api_key_id: string`

      - `type: "api_actor"`

        - `"api_actor"`

    - `beta_managed_agents_user_actor: object { type, user_id }`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

  - `path: optional string`

  - `redacted_at: optional string`

    A timestamp in RFC 3339 format

  - `redacted_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor`

    - `beta_managed_agents_session_actor: object { session_id, type }`

      - `session_id: string`

      - `type: "session_actor"`

        - `"session_actor"`

    - `beta_managed_agents_api_actor: object { api_key_id, type }`

      - `api_key_id: string`

      - `type: "api_actor"`

        - `"api_actor"`

    - `beta_managed_agents_user_actor: object { type, user_id }`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

### Example

```cli
ant beta:memory-stores:memory-versions retrieve \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id \
  --memory-version-id memory_version_id
```

## Redact

`$ ant beta:memory-stores:memory-versions redact`

**post** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

RedactMemoryVersion

### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--memory-version-id: string`

  Path param: Path parameter memory_version_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_memory_version: object { id, created_at, memory_id, 10 more }`

  - `id: string`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `memory_id: string`

  - `memory_store_id: string`

  - `operation: "created" or "modified" or "deleted"`

    MemoryVersionOperation enum

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `type: "memory_version"`

    - `"memory_version"`

  - `content: optional string`

  - `content_sha256: optional string`

  - `content_size_bytes: optional number`

  - `created_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor`

    - `beta_managed_agents_session_actor: object { session_id, type }`

      - `session_id: string`

      - `type: "session_actor"`

        - `"session_actor"`

    - `beta_managed_agents_api_actor: object { api_key_id, type }`

      - `api_key_id: string`

      - `type: "api_actor"`

        - `"api_actor"`

    - `beta_managed_agents_user_actor: object { type, user_id }`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

  - `path: optional string`

  - `redacted_at: optional string`

    A timestamp in RFC 3339 format

  - `redacted_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor`

    - `beta_managed_agents_session_actor: object { session_id, type }`

      - `session_id: string`

      - `type: "session_actor"`

        - `"session_actor"`

    - `beta_managed_agents_api_actor: object { api_key_id, type }`

      - `api_key_id: string`

      - `type: "api_actor"`

        - `"api_actor"`

    - `beta_managed_agents_user_actor: object { type, user_id }`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

### Example

```cli
ant beta:memory-stores:memory-versions redact \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id \
  --memory-version-id memory_version_id
```

## Domain Types

### Beta Managed Agents Actor

- `beta_managed_agents_actor: BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor`

  - `beta_managed_agents_session_actor: object { session_id, type }`

    - `session_id: string`

    - `type: "session_actor"`

      - `"session_actor"`

  - `beta_managed_agents_api_actor: object { api_key_id, type }`

    - `api_key_id: string`

    - `type: "api_actor"`

      - `"api_actor"`

  - `beta_managed_agents_user_actor: object { type, user_id }`

    - `type: "user_actor"`

      - `"user_actor"`

    - `user_id: string`

### Beta Managed Agents API Actor

- `beta_managed_agents_api_actor: object { api_key_id, type }`

  - `api_key_id: string`

  - `type: "api_actor"`

    - `"api_actor"`

### Beta Managed Agents Memory Version

- `beta_managed_agents_memory_version: object { id, created_at, memory_id, 10 more }`

  - `id: string`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `memory_id: string`

  - `memory_store_id: string`

  - `operation: "created" or "modified" or "deleted"`

    MemoryVersionOperation enum

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `type: "memory_version"`

    - `"memory_version"`

  - `content: optional string`

  - `content_sha256: optional string`

  - `content_size_bytes: optional number`

  - `created_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor`

    - `beta_managed_agents_session_actor: object { session_id, type }`

      - `session_id: string`

      - `type: "session_actor"`

        - `"session_actor"`

    - `beta_managed_agents_api_actor: object { api_key_id, type }`

      - `api_key_id: string`

      - `type: "api_actor"`

        - `"api_actor"`

    - `beta_managed_agents_user_actor: object { type, user_id }`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

  - `path: optional string`

  - `redacted_at: optional string`

    A timestamp in RFC 3339 format

  - `redacted_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor`

    - `beta_managed_agents_session_actor: object { session_id, type }`

      - `session_id: string`

      - `type: "session_actor"`

        - `"session_actor"`

    - `beta_managed_agents_api_actor: object { api_key_id, type }`

      - `api_key_id: string`

      - `type: "api_actor"`

        - `"api_actor"`

    - `beta_managed_agents_user_actor: object { type, user_id }`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

### Beta Managed Agents Memory Version Operation

- `beta_managed_agents_memory_version_operation: "created" or "modified" or "deleted"`

  MemoryVersionOperation enum

  - `"created"`

  - `"modified"`

  - `"deleted"`

### Beta Managed Agents Session Actor

- `beta_managed_agents_session_actor: object { session_id, type }`

  - `session_id: string`

  - `type: "session_actor"`

    - `"session_actor"`

### Beta Managed Agents User Actor

- `beta_managed_agents_user_actor: object { type, user_id }`

  - `type: "user_actor"`

    - `"user_actor"`

  - `user_id: string`
