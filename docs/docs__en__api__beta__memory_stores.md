# Memory Stores

## Create

**post** `/v1/memory_stores`

CreateMemoryStore

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 19 more`

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

    - `"advisor-tool-2026-03-01"`

### Body Parameters

- `name: string`

- `description: optional string`

- `metadata: optional map[string]`

### Returns

- `BetaManagedAgentsMemoryStore = object { id, type, archived_at, 5 more }`

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

```http
curl https://api.anthropic.com/v1/memory_stores \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "name": "x"
        }'
```

## List

**get** `/v1/memory_stores`

ListMemoryStores

### Query Parameters

- `"created_at[gte]": optional string`

  Return stores created at or after this time (inclusive).

- `"created_at[lte]": optional string`

  Return stores created at or before this time (inclusive).

- `include_archived: optional boolean`

  Query parameter for include_archived

- `limit: optional number`

  Query parameter for limit

- `page: optional string`

  Query parameter for page

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 19 more`

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

    - `"advisor-tool-2026-03-01"`

### Returns

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

```http
curl https://api.anthropic.com/v1/memory_stores \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Retrieve

**get** `/v1/memory_stores/{memory_store_id}`

GetMemoryStore

### Path Parameters

- `memory_store_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 19 more`

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

    - `"advisor-tool-2026-03-01"`

### Returns

- `BetaManagedAgentsMemoryStore = object { id, type, archived_at, 5 more }`

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

```http
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Update

**post** `/v1/memory_stores/{memory_store_id}`

UpdateMemoryStore

### Path Parameters

- `memory_store_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 19 more`

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

    - `"advisor-tool-2026-03-01"`

### Body Parameters

- `description: optional string`

- `metadata: optional map[string]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `name: optional string`

### Returns

- `BetaManagedAgentsMemoryStore = object { id, type, archived_at, 5 more }`

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

```http
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{}'
```

## Delete

**delete** `/v1/memory_stores/{memory_store_id}`

DeleteMemoryStore

### Path Parameters

- `memory_store_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 19 more`

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

    - `"advisor-tool-2026-03-01"`

### Returns

- `BetaManagedAgentsDeletedMemoryStore = object { id, type }`

  - `id: string`

  - `type: "memory_store_deleted"`

    - `"memory_store_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Archive

**post** `/v1/memory_stores/{memory_store_id}/archive`

ArchiveMemoryStore

### Path Parameters

- `memory_store_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 19 more`

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

    - `"advisor-tool-2026-03-01"`

### Returns

- `BetaManagedAgentsMemoryStore = object { id, type, archived_at, 5 more }`

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

```http
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Domain Types

### Beta Managed Agents Deleted Memory Store

- `BetaManagedAgentsDeletedMemoryStore = object { id, type }`

  - `id: string`

  - `type: "memory_store_deleted"`

    - `"memory_store_deleted"`

### Beta Managed Agents Memory Store

- `BetaManagedAgentsMemoryStore = object { id, type, archived_at, 5 more }`

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

**post** `/v1/memory_stores/{memory_store_id}/memories`

CreateMemory

### Path Parameters

- `memory_store_id: string`

### Query Parameters

- `view: optional BetaManagedAgentsMemoryView`

  Query parameter for view

  - `"basic"`

  - `"full"`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 19 more`

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

    - `"advisor-tool-2026-03-01"`

### Body Parameters

- `content: string`

- `path: string`

### Returns

- `BetaManagedAgentsMemory = object { id, content_sha256, content_size_bytes, 7 more }`

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

```http
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memories \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "content": "content",
          "path": "xx"
        }'
```

## List

**get** `/v1/memory_stores/{memory_store_id}/memories`

ListMemories

### Path Parameters

- `memory_store_id: string`

### Query Parameters

- `depth: optional number`

  Query parameter for depth

- `limit: optional number`

  Query parameter for limit

- `order: optional "asc" or "desc"`

  Query parameter for order

  - `"asc"`

  - `"desc"`

- `order_by: optional string`

  Query parameter for order_by

- `page: optional string`

  Query parameter for page

- `path_prefix: optional string`

  Optional path prefix filter (raw string-prefix match; include a trailing slash for directory-scoped lists). This value appears in request URLs. Do not include secrets or personally identifiable information.

- `view: optional BetaManagedAgentsMemoryView`

  Query parameter for view

  - `"basic"`

  - `"full"`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 19 more`

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

    - `"advisor-tool-2026-03-01"`

### Returns

- `data: optional array of BetaManagedAgentsMemoryListItem`

  - `BetaManagedAgentsMemory = object { id, content_sha256, content_size_bytes, 7 more }`

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

  - `BetaManagedAgentsMemoryPrefix = object { path, type }`

    - `path: string`

    - `type: "memory_prefix"`

      - `"memory_prefix"`

- `next_page: optional string`

### Example

```http
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memories \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Retrieve

**get** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

GetMemory

### Path Parameters

- `memory_store_id: string`

- `memory_id: string`

### Query Parameters

- `view: optional BetaManagedAgentsMemoryView`

  Query parameter for view

  - `"basic"`

  - `"full"`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 19 more`

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

    - `"advisor-tool-2026-03-01"`

### Returns

- `BetaManagedAgentsMemory = object { id, content_sha256, content_size_bytes, 7 more }`

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

```http
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memories/$MEMORY_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Update

**post** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

UpdateMemory

### Path Parameters

- `memory_store_id: string`

- `memory_id: string`

### Query Parameters

- `view: optional BetaManagedAgentsMemoryView`

  Query parameter for view

  - `"basic"`

  - `"full"`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 19 more`

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

    - `"advisor-tool-2026-03-01"`

### Body Parameters

- `content: optional string`

- `path: optional string`

- `precondition: optional BetaManagedAgentsPrecondition`

  - `type: "content_sha256"`

    - `"content_sha256"`

  - `content_sha256: optional string`

### Returns

- `BetaManagedAgentsMemory = object { id, content_sha256, content_size_bytes, 7 more }`

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

```http
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memories/$MEMORY_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{}'
```

## Delete

**delete** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

DeleteMemory

### Path Parameters

- `memory_store_id: string`

- `memory_id: string`

### Query Parameters

- `expected_content_sha256: optional string`

  Query parameter for expected_content_sha256

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 19 more`

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

    - `"advisor-tool-2026-03-01"`

### Returns

- `BetaManagedAgentsDeletedMemory = object { id, type }`

  - `id: string`

  - `type: "memory_deleted"`

    - `"memory_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memories/$MEMORY_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Domain Types

### Beta Managed Agents Content Sha256 Precondition

- `BetaManagedAgentsContentSha256Precondition = object { type, content_sha256 }`

  - `type: "content_sha256"`

    - `"content_sha256"`

  - `content_sha256: optional string`

### Beta Managed Agents Deleted Memory

- `BetaManagedAgentsDeletedMemory = object { id, type }`

  - `id: string`

  - `type: "memory_deleted"`

    - `"memory_deleted"`

### Beta Managed Agents Memory

- `BetaManagedAgentsMemory = object { id, content_sha256, content_size_bytes, 7 more }`

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

- `BetaManagedAgentsMemoryListItem = BetaManagedAgentsMemory or BetaManagedAgentsMemoryPrefix`

  - `BetaManagedAgentsMemory = object { id, content_sha256, content_size_bytes, 7 more }`

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

  - `BetaManagedAgentsMemoryPrefix = object { path, type }`

    - `path: string`

    - `type: "memory_prefix"`

      - `"memory_prefix"`

### Beta Managed Agents Memory Path Conflict Error

- `BetaManagedAgentsMemoryPathConflictError = object { type, conflicting_memory_id, conflicting_path, message }`

  - `type: "memory_path_conflict_error"`

    - `"memory_path_conflict_error"`

  - `conflicting_memory_id: optional string`

  - `conflicting_path: optional string`

  - `message: optional string`

### Beta Managed Agents Memory Precondition Failed Error

- `BetaManagedAgentsMemoryPreconditionFailedError = object { type, message }`

  - `type: "memory_precondition_failed_error"`

    - `"memory_precondition_failed_error"`

  - `message: optional string`

### Beta Managed Agents Memory Prefix

- `BetaManagedAgentsMemoryPrefix = object { path, type }`

  - `path: string`

  - `type: "memory_prefix"`

    - `"memory_prefix"`

### Beta Managed Agents Memory View

- `BetaManagedAgentsMemoryView = "basic" or "full"`

  MemoryView enum

  - `"basic"`

  - `"full"`

### Beta Managed Agents Precondition

- `BetaManagedAgentsPrecondition = object { type, content_sha256 }`

  - `type: "content_sha256"`

    - `"content_sha256"`

  - `content_sha256: optional string`

# Memory Versions

## List

**get** `/v1/memory_stores/{memory_store_id}/memory_versions`

ListMemoryVersions

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

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 19 more`

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

    - `"advisor-tool-2026-03-01"`

### Returns

- `data: optional array of BetaManagedAgentsMemoryVersion`

  - `id: string`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `memory_id: string`

  - `memory_store_id: string`

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    MemoryVersionOperation enum

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `type: "memory_version"`

    - `"memory_version"`

  - `content: optional string`

  - `content_sha256: optional string`

  - `content_size_bytes: optional number`

  - `created_by: optional BetaManagedAgentsActor`

    - `BetaManagedAgentsSessionActor = object { session_id, type }`

      - `session_id: string`

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor = object { api_key_id, type }`

      - `api_key_id: string`

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor = object { type, user_id }`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

  - `path: optional string`

  - `redacted_at: optional string`

    A timestamp in RFC 3339 format

  - `redacted_by: optional BetaManagedAgentsActor`

    - `BetaManagedAgentsSessionActor = object { session_id, type }`

      - `session_id: string`

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor = object { api_key_id, type }`

      - `api_key_id: string`

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor = object { type, user_id }`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

- `next_page: optional string`

### Example

```http
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memory_versions \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Retrieve

**get** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

GetMemoryVersion

### Path Parameters

- `memory_store_id: string`

- `memory_version_id: string`

### Query Parameters

- `view: optional BetaManagedAgentsMemoryView`

  Query parameter for view

  - `"basic"`

  - `"full"`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 19 more`

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

    - `"advisor-tool-2026-03-01"`

### Returns

- `BetaManagedAgentsMemoryVersion = object { id, created_at, memory_id, 10 more }`

  - `id: string`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `memory_id: string`

  - `memory_store_id: string`

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    MemoryVersionOperation enum

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `type: "memory_version"`

    - `"memory_version"`

  - `content: optional string`

  - `content_sha256: optional string`

  - `content_size_bytes: optional number`

  - `created_by: optional BetaManagedAgentsActor`

    - `BetaManagedAgentsSessionActor = object { session_id, type }`

      - `session_id: string`

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor = object { api_key_id, type }`

      - `api_key_id: string`

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor = object { type, user_id }`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

  - `path: optional string`

  - `redacted_at: optional string`

    A timestamp in RFC 3339 format

  - `redacted_by: optional BetaManagedAgentsActor`

    - `BetaManagedAgentsSessionActor = object { session_id, type }`

      - `session_id: string`

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor = object { api_key_id, type }`

      - `api_key_id: string`

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor = object { type, user_id }`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

### Example

```http
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memory_versions/$MEMORY_VERSION_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Redact

**post** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

RedactMemoryVersion

### Path Parameters

- `memory_store_id: string`

- `memory_version_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 19 more`

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

    - `"advisor-tool-2026-03-01"`

### Returns

- `BetaManagedAgentsMemoryVersion = object { id, created_at, memory_id, 10 more }`

  - `id: string`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `memory_id: string`

  - `memory_store_id: string`

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    MemoryVersionOperation enum

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `type: "memory_version"`

    - `"memory_version"`

  - `content: optional string`

  - `content_sha256: optional string`

  - `content_size_bytes: optional number`

  - `created_by: optional BetaManagedAgentsActor`

    - `BetaManagedAgentsSessionActor = object { session_id, type }`

      - `session_id: string`

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor = object { api_key_id, type }`

      - `api_key_id: string`

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor = object { type, user_id }`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

  - `path: optional string`

  - `redacted_at: optional string`

    A timestamp in RFC 3339 format

  - `redacted_by: optional BetaManagedAgentsActor`

    - `BetaManagedAgentsSessionActor = object { session_id, type }`

      - `session_id: string`

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor = object { api_key_id, type }`

      - `api_key_id: string`

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor = object { type, user_id }`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

### Example

```http
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memory_versions/$MEMORY_VERSION_ID/redact \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Domain Types

### Beta Managed Agents Actor

- `BetaManagedAgentsActor = BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor`

  - `BetaManagedAgentsSessionActor = object { session_id, type }`

    - `session_id: string`

    - `type: "session_actor"`

      - `"session_actor"`

  - `BetaManagedAgentsAPIActor = object { api_key_id, type }`

    - `api_key_id: string`

    - `type: "api_actor"`

      - `"api_actor"`

  - `BetaManagedAgentsUserActor = object { type, user_id }`

    - `type: "user_actor"`

      - `"user_actor"`

    - `user_id: string`

### Beta Managed Agents API Actor

- `BetaManagedAgentsAPIActor = object { api_key_id, type }`

  - `api_key_id: string`

  - `type: "api_actor"`

    - `"api_actor"`

### Beta Managed Agents Memory Version

- `BetaManagedAgentsMemoryVersion = object { id, created_at, memory_id, 10 more }`

  - `id: string`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `memory_id: string`

  - `memory_store_id: string`

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    MemoryVersionOperation enum

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `type: "memory_version"`

    - `"memory_version"`

  - `content: optional string`

  - `content_sha256: optional string`

  - `content_size_bytes: optional number`

  - `created_by: optional BetaManagedAgentsActor`

    - `BetaManagedAgentsSessionActor = object { session_id, type }`

      - `session_id: string`

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor = object { api_key_id, type }`

      - `api_key_id: string`

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor = object { type, user_id }`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

  - `path: optional string`

  - `redacted_at: optional string`

    A timestamp in RFC 3339 format

  - `redacted_by: optional BetaManagedAgentsActor`

    - `BetaManagedAgentsSessionActor = object { session_id, type }`

      - `session_id: string`

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor = object { api_key_id, type }`

      - `api_key_id: string`

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor = object { type, user_id }`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

### Beta Managed Agents Memory Version Operation

- `BetaManagedAgentsMemoryVersionOperation = "created" or "modified" or "deleted"`

  MemoryVersionOperation enum

  - `"created"`

  - `"modified"`

  - `"deleted"`

### Beta Managed Agents Session Actor

- `BetaManagedAgentsSessionActor = object { session_id, type }`

  - `session_id: string`

  - `type: "session_actor"`

    - `"session_actor"`

### Beta Managed Agents User Actor

- `BetaManagedAgentsUserActor = object { type, user_id }`

  - `type: "user_actor"`

    - `"user_actor"`

  - `user_id: string`
