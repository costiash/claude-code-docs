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
