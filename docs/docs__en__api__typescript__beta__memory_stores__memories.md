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
