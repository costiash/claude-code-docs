# Memory Stores

## Create

`client.beta.memoryStores.create(MemoryStoreCreateParamsparams, RequestOptionsoptions?): BetaManagedAgentsMemoryStore`

**post** `/v1/memory_stores`

CreateMemoryStore

### Parameters

- `params: MemoryStoreCreateParams`

  - `name: string`

    Body param

  - `description?: string`

    Body param

  - `metadata?: Record<string, string>`

    Body param

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 19 more`

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

- `BetaManagedAgentsMemoryStore`

  - `id: string`

  - `type: "memory_store"`

    - `"memory_store"`

  - `archived_at?: string | null`

    A timestamp in RFC 3339 format

  - `created_at?: string`

    A timestamp in RFC 3339 format

  - `description?: string`

  - `metadata?: Record<string, string>`

  - `name?: string`

  - `updated_at?: string`

    A timestamp in RFC 3339 format

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsMemoryStore = await client.beta.memoryStores.create({ name: 'x' });

console.log(betaManagedAgentsMemoryStore.id);
```

## List

`client.beta.memoryStores.list(MemoryStoreListParamsparams?, RequestOptionsoptions?): PageCursor<BetaManagedAgentsMemoryStore>`

**get** `/v1/memory_stores`

ListMemoryStores

### Parameters

- `params: MemoryStoreListParams`

  - `createdAtGte?: string`

    Query param: Return stores created at or after this time (inclusive).

  - `createdAtLte?: string`

    Query param: Return stores created at or before this time (inclusive).

  - `include_archived?: boolean`

    Query param: Query parameter for include_archived

  - `limit?: number`

    Query param: Query parameter for limit

  - `page?: string`

    Query param: Query parameter for page

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 19 more`

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

- `BetaManagedAgentsMemoryStore`

  - `id: string`

  - `type: "memory_store"`

    - `"memory_store"`

  - `archived_at?: string | null`

    A timestamp in RFC 3339 format

  - `created_at?: string`

    A timestamp in RFC 3339 format

  - `description?: string`

  - `metadata?: Record<string, string>`

  - `name?: string`

  - `updated_at?: string`

    A timestamp in RFC 3339 format

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsMemoryStore of client.beta.memoryStores.list()) {
  console.log(betaManagedAgentsMemoryStore.id);
}
```

## Retrieve

`client.beta.memoryStores.retrieve(stringmemoryStoreID, MemoryStoreRetrieveParamsparams?, RequestOptionsoptions?): BetaManagedAgentsMemoryStore`

**get** `/v1/memory_stores/{memory_store_id}`

GetMemoryStore

### Parameters

- `memoryStoreID: string`

- `params: MemoryStoreRetrieveParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 19 more`

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

- `BetaManagedAgentsMemoryStore`

  - `id: string`

  - `type: "memory_store"`

    - `"memory_store"`

  - `archived_at?: string | null`

    A timestamp in RFC 3339 format

  - `created_at?: string`

    A timestamp in RFC 3339 format

  - `description?: string`

  - `metadata?: Record<string, string>`

  - `name?: string`

  - `updated_at?: string`

    A timestamp in RFC 3339 format

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsMemoryStore = await client.beta.memoryStores.retrieve('memory_store_id');

console.log(betaManagedAgentsMemoryStore.id);
```

## Update

`client.beta.memoryStores.update(stringmemoryStoreID, MemoryStoreUpdateParamsparams, RequestOptionsoptions?): BetaManagedAgentsMemoryStore`

**post** `/v1/memory_stores/{memory_store_id}`

UpdateMemoryStore

### Parameters

- `memoryStoreID: string`

- `params: MemoryStoreUpdateParams`

  - `description?: string | null`

    Body param

  - `metadata?: Record<string, string | null> | null`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `name?: string | null`

    Body param

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 19 more`

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

- `BetaManagedAgentsMemoryStore`

  - `id: string`

  - `type: "memory_store"`

    - `"memory_store"`

  - `archived_at?: string | null`

    A timestamp in RFC 3339 format

  - `created_at?: string`

    A timestamp in RFC 3339 format

  - `description?: string`

  - `metadata?: Record<string, string>`

  - `name?: string`

  - `updated_at?: string`

    A timestamp in RFC 3339 format

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsMemoryStore = await client.beta.memoryStores.update('memory_store_id');

console.log(betaManagedAgentsMemoryStore.id);
```

## Delete

`client.beta.memoryStores.delete(stringmemoryStoreID, MemoryStoreDeleteParamsparams?, RequestOptionsoptions?): BetaManagedAgentsDeletedMemoryStore`

**delete** `/v1/memory_stores/{memory_store_id}`

DeleteMemoryStore

### Parameters

- `memoryStoreID: string`

- `params: MemoryStoreDeleteParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 19 more`

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

- `BetaManagedAgentsDeletedMemoryStore`

  - `id: string`

  - `type: "memory_store_deleted"`

    - `"memory_store_deleted"`

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsDeletedMemoryStore = await client.beta.memoryStores.delete(
  'memory_store_id',
);

console.log(betaManagedAgentsDeletedMemoryStore.id);
```

## Archive

`client.beta.memoryStores.archive(stringmemoryStoreID, MemoryStoreArchiveParamsparams?, RequestOptionsoptions?): BetaManagedAgentsMemoryStore`

**post** `/v1/memory_stores/{memory_store_id}/archive`

ArchiveMemoryStore

### Parameters

- `memoryStoreID: string`

- `params: MemoryStoreArchiveParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 19 more`

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

- `BetaManagedAgentsMemoryStore`

  - `id: string`

  - `type: "memory_store"`

    - `"memory_store"`

  - `archived_at?: string | null`

    A timestamp in RFC 3339 format

  - `created_at?: string`

    A timestamp in RFC 3339 format

  - `description?: string`

  - `metadata?: Record<string, string>`

  - `name?: string`

  - `updated_at?: string`

    A timestamp in RFC 3339 format

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsMemoryStore = await client.beta.memoryStores.archive('memory_store_id');

console.log(betaManagedAgentsMemoryStore.id);
```

## Domain Types

### Beta Managed Agents Deleted Memory Store

- `BetaManagedAgentsDeletedMemoryStore`

  - `id: string`

  - `type: "memory_store_deleted"`

    - `"memory_store_deleted"`

### Beta Managed Agents Memory Store

- `BetaManagedAgentsMemoryStore`

  - `id: string`

  - `type: "memory_store"`

    - `"memory_store"`

  - `archived_at?: string | null`

    A timestamp in RFC 3339 format

  - `created_at?: string`

    A timestamp in RFC 3339 format

  - `description?: string`

  - `metadata?: Record<string, string>`

  - `name?: string`

  - `updated_at?: string`

    A timestamp in RFC 3339 format

# Memories

## Create

`client.beta.memoryStores.memories.create(stringmemoryStoreID, MemoryCreateParamsparams, RequestOptionsoptions?): BetaManagedAgentsMemory`

**post** `/v1/memory_stores/{memory_store_id}/memories`

CreateMemory

### Parameters

- `memoryStoreID: string`

- `params: MemoryCreateParams`

  - `content: string | null`

    Body param

  - `path_: string`

    Body param

  - `view?: BetaManagedAgentsMemoryView`

    Query param: Query parameter for view

    - `"basic"`

    - `"full"`

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 19 more`

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

- `BetaManagedAgentsMemory`

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

  - `content?: string | null`

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsMemory = await client.beta.memoryStores.memories.create('memory_store_id', {
  content: 'content',
  path: 'xx',
});

console.log(betaManagedAgentsMemory.id);
```

## List

`client.beta.memoryStores.memories.list(stringmemoryStoreID, MemoryListParamsparams?, RequestOptionsoptions?): PageCursor<BetaManagedAgentsMemoryListItem>`

**get** `/v1/memory_stores/{memory_store_id}/memories`

ListMemories

### Parameters

- `memoryStoreID: string`

- `params: MemoryListParams`

  - `depth?: number`

    Query param: Query parameter for depth

  - `limit?: number`

    Query param: Query parameter for limit

  - `order?: "asc" | "desc"`

    Query param: Query parameter for order

    - `"asc"`

    - `"desc"`

  - `order_by?: string`

    Query param: Query parameter for order_by

  - `page?: string`

    Query param: Query parameter for page

  - `path_prefix?: string`

    Query param: Optional path prefix filter (raw string-prefix match; include a trailing slash for directory-scoped lists). This value appears in request URLs. Do not include secrets or personally identifiable information.

  - `view?: BetaManagedAgentsMemoryView`

    Query param: Query parameter for view

    - `"basic"`

    - `"full"`

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 19 more`

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

- `BetaManagedAgentsMemoryListItem = BetaManagedAgentsMemory | BetaManagedAgentsMemoryPrefix`

  - `BetaManagedAgentsMemory`

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

    - `content?: string | null`

  - `BetaManagedAgentsMemoryPrefix`

    - `path: string`

    - `type: "memory_prefix"`

      - `"memory_prefix"`

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsMemoryListItem of client.beta.memoryStores.memories.list(
  'memory_store_id',
)) {
  console.log(betaManagedAgentsMemoryListItem);
}
```

## Retrieve

`client.beta.memoryStores.memories.retrieve(stringmemoryID, MemoryRetrieveParamsparams, RequestOptionsoptions?): BetaManagedAgentsMemory`

**get** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

GetMemory

### Parameters

- `memoryID: string`

- `params: MemoryRetrieveParams`

  - `memory_store_id: string`

    Path param: Path parameter memory_store_id

  - `view?: BetaManagedAgentsMemoryView`

    Query param: Query parameter for view

    - `"basic"`

    - `"full"`

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 19 more`

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

- `BetaManagedAgentsMemory`

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

  - `content?: string | null`

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsMemory = await client.beta.memoryStores.memories.retrieve('memory_id', {
  memory_store_id: 'memory_store_id',
});

console.log(betaManagedAgentsMemory.id);
```

## Update

`client.beta.memoryStores.memories.update(stringmemoryID, MemoryUpdateParamsparams, RequestOptionsoptions?): BetaManagedAgentsMemory`

**post** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

UpdateMemory

### Parameters

- `memoryID: string`

- `params: MemoryUpdateParams`

  - `memory_store_id: string`

    Path param: Path parameter memory_store_id

  - `view?: BetaManagedAgentsMemoryView`

    Query param: Query parameter for view

    - `"basic"`

    - `"full"`

  - `content?: string | null`

    Body param

  - `path_?: string | null`

    Body param

  - `precondition?: BetaManagedAgentsPrecondition`

    Body param

    - `type: "content_sha256"`

      - `"content_sha256"`

    - `content_sha256?: string`

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 19 more`

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

- `BetaManagedAgentsMemory`

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

  - `content?: string | null`

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsMemory = await client.beta.memoryStores.memories.update('memory_id', {
  memory_store_id: 'memory_store_id',
});

console.log(betaManagedAgentsMemory.id);
```

## Delete

`client.beta.memoryStores.memories.delete(stringmemoryID, MemoryDeleteParamsparams, RequestOptionsoptions?): BetaManagedAgentsDeletedMemory`

**delete** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

DeleteMemory

### Parameters

- `memoryID: string`

- `params: MemoryDeleteParams`

  - `memory_store_id: string`

    Path param: Path parameter memory_store_id

  - `expected_content_sha256?: string`

    Query param: Query parameter for expected_content_sha256

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 19 more`

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

- `BetaManagedAgentsDeletedMemory`

  - `id: string`

  - `type: "memory_deleted"`

    - `"memory_deleted"`

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsDeletedMemory = await client.beta.memoryStores.memories.delete('memory_id', {
  memory_store_id: 'memory_store_id',
});

console.log(betaManagedAgentsDeletedMemory.id);
```

## Domain Types

### Beta Managed Agents Content Sha256 Precondition

- `BetaManagedAgentsContentSha256Precondition`

  - `type: "content_sha256"`

    - `"content_sha256"`

  - `content_sha256?: string`

### Beta Managed Agents Deleted Memory

- `BetaManagedAgentsDeletedMemory`

  - `id: string`

  - `type: "memory_deleted"`

    - `"memory_deleted"`

### Beta Managed Agents Memory

- `BetaManagedAgentsMemory`

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

  - `content?: string | null`

### Beta Managed Agents Memory List Item

- `BetaManagedAgentsMemoryListItem = BetaManagedAgentsMemory | BetaManagedAgentsMemoryPrefix`

  - `BetaManagedAgentsMemory`

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

    - `content?: string | null`

  - `BetaManagedAgentsMemoryPrefix`

    - `path: string`

    - `type: "memory_prefix"`

      - `"memory_prefix"`

### Beta Managed Agents Memory Path Conflict Error

- `BetaManagedAgentsMemoryPathConflictError`

  - `type: "memory_path_conflict_error"`

    - `"memory_path_conflict_error"`

  - `conflicting_memory_id?: string`

  - `conflicting_path?: string`

  - `message?: string`

### Beta Managed Agents Memory Precondition Failed Error

- `BetaManagedAgentsMemoryPreconditionFailedError`

  - `type: "memory_precondition_failed_error"`

    - `"memory_precondition_failed_error"`

  - `message?: string`

### Beta Managed Agents Memory Prefix

- `BetaManagedAgentsMemoryPrefix`

  - `path: string`

  - `type: "memory_prefix"`

    - `"memory_prefix"`

### Beta Managed Agents Memory View

- `BetaManagedAgentsMemoryView = "basic" | "full"`

  MemoryView enum

  - `"basic"`

  - `"full"`

### Beta Managed Agents Precondition

- `BetaManagedAgentsPrecondition`

  - `type: "content_sha256"`

    - `"content_sha256"`

  - `content_sha256?: string`

# Memory Versions

## List

`client.beta.memoryStores.memoryVersions.list(stringmemoryStoreID, MemoryVersionListParamsparams?, RequestOptionsoptions?): PageCursor<BetaManagedAgentsMemoryVersion>`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions`

ListMemoryVersions

### Parameters

- `memoryStoreID: string`

- `params: MemoryVersionListParams`

  - `api_key_id?: string`

    Query param: Query parameter for api_key_id

  - `createdAtGte?: string`

    Query param: Return versions created at or after this time (inclusive).

  - `createdAtLte?: string`

    Query param: Return versions created at or before this time (inclusive).

  - `limit?: number`

    Query param: Query parameter for limit

  - `memory_id?: string`

    Query param: Query parameter for memory_id

  - `operation?: BetaManagedAgentsMemoryVersionOperation`

    Query param: Query parameter for operation

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `page?: string`

    Query param: Query parameter for page

  - `session_id?: string`

    Query param: Query parameter for session_id

  - `view?: BetaManagedAgentsMemoryView`

    Query param: Query parameter for view

    - `"basic"`

    - `"full"`

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 19 more`

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

- `BetaManagedAgentsMemoryVersion`

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

  - `content?: string | null`

  - `content_sha256?: string | null`

  - `content_size_bytes?: number | null`

  - `created_by?: BetaManagedAgentsActor`

    - `BetaManagedAgentsSessionActor`

      - `session_id: string`

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor`

      - `api_key_id: string`

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

  - `path?: string | null`

  - `redacted_at?: string | null`

    A timestamp in RFC 3339 format

  - `redacted_by?: BetaManagedAgentsActor`

    - `BetaManagedAgentsSessionActor`

      - `session_id: string`

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor`

      - `api_key_id: string`

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsMemoryVersion of client.beta.memoryStores.memoryVersions.list(
  'memory_store_id',
)) {
  console.log(betaManagedAgentsMemoryVersion.id);
}
```

## Retrieve

`client.beta.memoryStores.memoryVersions.retrieve(stringmemoryVersionID, MemoryVersionRetrieveParamsparams, RequestOptionsoptions?): BetaManagedAgentsMemoryVersion`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

GetMemoryVersion

### Parameters

- `memoryVersionID: string`

- `params: MemoryVersionRetrieveParams`

  - `memory_store_id: string`

    Path param: Path parameter memory_store_id

  - `view?: BetaManagedAgentsMemoryView`

    Query param: Query parameter for view

    - `"basic"`

    - `"full"`

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 19 more`

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

- `BetaManagedAgentsMemoryVersion`

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

  - `content?: string | null`

  - `content_sha256?: string | null`

  - `content_size_bytes?: number | null`

  - `created_by?: BetaManagedAgentsActor`

    - `BetaManagedAgentsSessionActor`

      - `session_id: string`

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor`

      - `api_key_id: string`

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

  - `path?: string | null`

  - `redacted_at?: string | null`

    A timestamp in RFC 3339 format

  - `redacted_by?: BetaManagedAgentsActor`

    - `BetaManagedAgentsSessionActor`

      - `session_id: string`

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor`

      - `api_key_id: string`

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsMemoryVersion = await client.beta.memoryStores.memoryVersions.retrieve(
  'memory_version_id',
  { memory_store_id: 'memory_store_id' },
);

console.log(betaManagedAgentsMemoryVersion.id);
```

## Redact

`client.beta.memoryStores.memoryVersions.redact(stringmemoryVersionID, MemoryVersionRedactParamsparams, RequestOptionsoptions?): BetaManagedAgentsMemoryVersion`

**post** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

RedactMemoryVersion

### Parameters

- `memoryVersionID: string`

- `params: MemoryVersionRedactParams`

  - `memory_store_id: string`

    Path param: Path parameter memory_store_id

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 19 more`

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

- `BetaManagedAgentsMemoryVersion`

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

  - `content?: string | null`

  - `content_sha256?: string | null`

  - `content_size_bytes?: number | null`

  - `created_by?: BetaManagedAgentsActor`

    - `BetaManagedAgentsSessionActor`

      - `session_id: string`

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor`

      - `api_key_id: string`

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

  - `path?: string | null`

  - `redacted_at?: string | null`

    A timestamp in RFC 3339 format

  - `redacted_by?: BetaManagedAgentsActor`

    - `BetaManagedAgentsSessionActor`

      - `session_id: string`

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor`

      - `api_key_id: string`

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsMemoryVersion = await client.beta.memoryStores.memoryVersions.redact(
  'memory_version_id',
  { memory_store_id: 'memory_store_id' },
);

console.log(betaManagedAgentsMemoryVersion.id);
```

## Domain Types

### Beta Managed Agents Actor

- `BetaManagedAgentsActor = BetaManagedAgentsSessionActor | BetaManagedAgentsAPIActor | BetaManagedAgentsUserActor`

  - `BetaManagedAgentsSessionActor`

    - `session_id: string`

    - `type: "session_actor"`

      - `"session_actor"`

  - `BetaManagedAgentsAPIActor`

    - `api_key_id: string`

    - `type: "api_actor"`

      - `"api_actor"`

  - `BetaManagedAgentsUserActor`

    - `type: "user_actor"`

      - `"user_actor"`

    - `user_id: string`

### Beta Managed Agents API Actor

- `BetaManagedAgentsAPIActor`

  - `api_key_id: string`

  - `type: "api_actor"`

    - `"api_actor"`

### Beta Managed Agents Memory Version

- `BetaManagedAgentsMemoryVersion`

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

  - `content?: string | null`

  - `content_sha256?: string | null`

  - `content_size_bytes?: number | null`

  - `created_by?: BetaManagedAgentsActor`

    - `BetaManagedAgentsSessionActor`

      - `session_id: string`

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor`

      - `api_key_id: string`

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

  - `path?: string | null`

  - `redacted_at?: string | null`

    A timestamp in RFC 3339 format

  - `redacted_by?: BetaManagedAgentsActor`

    - `BetaManagedAgentsSessionActor`

      - `session_id: string`

      - `type: "session_actor"`

        - `"session_actor"`

    - `BetaManagedAgentsAPIActor`

      - `api_key_id: string`

      - `type: "api_actor"`

        - `"api_actor"`

    - `BetaManagedAgentsUserActor`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

### Beta Managed Agents Memory Version Operation

- `BetaManagedAgentsMemoryVersionOperation = "created" | "modified" | "deleted"`

  MemoryVersionOperation enum

  - `"created"`

  - `"modified"`

  - `"deleted"`

### Beta Managed Agents Session Actor

- `BetaManagedAgentsSessionActor`

  - `session_id: string`

  - `type: "session_actor"`

    - `"session_actor"`

### Beta Managed Agents User Actor

- `BetaManagedAgentsUserActor`

  - `type: "user_actor"`

    - `"user_actor"`

  - `user_id: string`
