## List

`beta.memory_stores.memories.list(memory_store_id, **kwargs) -> PageCursor<BetaManagedAgentsMemoryListItem>`

**get** `/v1/memory_stores/{memory_store_id}/memories`

ListMemories

### Parameters

- `memory_store_id: String`

- `depth: Integer`

  Query parameter for depth

- `limit: Integer`

  Query parameter for limit

- `order: :asc | :desc`

  Query parameter for order

  - `:asc`

  - `:desc`

- `order_by: String`

  Query parameter for order_by

- `page: String`

  Query parameter for page

- `path_prefix: String`

  Optional path prefix filter (raw string-prefix match; include a trailing slash for directory-scoped lists). This value appears in request URLs. Do not include secrets or personally identifiable information.

- `view: BetaManagedAgentsMemoryView`

  Query parameter for view

  - `:basic`

  - `:full`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 19 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"advisor-tool-2026-03-01"`

### Returns

- `BetaManagedAgentsMemoryListItem = BetaManagedAgentsMemory | BetaManagedAgentsMemoryPrefix`

  - `class BetaManagedAgentsMemory`

    - `id: String`

    - `content_sha256: String`

    - `content_size_bytes: Integer`

    - `created_at: Time`

      A timestamp in RFC 3339 format

    - `memory_store_id: String`

    - `memory_version_id: String`

    - `path: String`

    - `type: :memory`

      - `:memory`

    - `updated_at: Time`

      A timestamp in RFC 3339 format

    - `content: String`

  - `class BetaManagedAgentsMemoryPrefix`

    - `path: String`

    - `type: :memory_prefix`

      - `:memory_prefix`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.memory_stores.memories.list("memory_store_id")

puts(page)
```
