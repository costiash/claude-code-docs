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
