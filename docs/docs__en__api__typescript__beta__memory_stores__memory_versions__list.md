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
