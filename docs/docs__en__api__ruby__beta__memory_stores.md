# Memory Stores

## Create

`beta.memory_stores.create(**kwargs) -> BetaManagedAgentsMemoryStore`

**post** `/v1/memory_stores`

CreateMemoryStore

### Parameters

- `name: String`

- `description: String`

- `metadata: Hash[Symbol, String]`

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

- `class BetaManagedAgentsMemoryStore`

  - `id: String`

  - `type: :memory_store`

    - `:memory_store`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `description: String`

  - `metadata: Hash[Symbol, String]`

  - `name: String`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory_store = anthropic.beta.memory_stores.create(name: "x")

puts(beta_managed_agents_memory_store)
```

## List

`beta.memory_stores.list(**kwargs) -> PageCursor<BetaManagedAgentsMemoryStore>`

**get** `/v1/memory_stores`

ListMemoryStores

### Parameters

- `created_at_gte: Time`

  Return stores created at or after this time (inclusive).

- `created_at_lte: Time`

  Return stores created at or before this time (inclusive).

- `include_archived: bool`

  Query parameter for include_archived

- `limit: Integer`

  Query parameter for limit

- `page: String`

  Query parameter for page

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

- `class BetaManagedAgentsMemoryStore`

  - `id: String`

  - `type: :memory_store`

    - `:memory_store`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `description: String`

  - `metadata: Hash[Symbol, String]`

  - `name: String`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.memory_stores.list

puts(page)
```

## Retrieve

`beta.memory_stores.retrieve(memory_store_id, **kwargs) -> BetaManagedAgentsMemoryStore`

**get** `/v1/memory_stores/{memory_store_id}`

GetMemoryStore

### Parameters

- `memory_store_id: String`

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

- `class BetaManagedAgentsMemoryStore`

  - `id: String`

  - `type: :memory_store`

    - `:memory_store`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `description: String`

  - `metadata: Hash[Symbol, String]`

  - `name: String`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory_store = anthropic.beta.memory_stores.retrieve("memory_store_id")

puts(beta_managed_agents_memory_store)
```

## Update

`beta.memory_stores.update(memory_store_id, **kwargs) -> BetaManagedAgentsMemoryStore`

**post** `/v1/memory_stores/{memory_store_id}`

UpdateMemoryStore

### Parameters

- `memory_store_id: String`

- `description: String`

- `metadata: Hash[Symbol, String]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `name: String`

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

- `class BetaManagedAgentsMemoryStore`

  - `id: String`

  - `type: :memory_store`

    - `:memory_store`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `description: String`

  - `metadata: Hash[Symbol, String]`

  - `name: String`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory_store = anthropic.beta.memory_stores.update("memory_store_id")

puts(beta_managed_agents_memory_store)
```

## Delete

`beta.memory_stores.delete(memory_store_id, **kwargs) -> BetaManagedAgentsDeletedMemoryStore`

**delete** `/v1/memory_stores/{memory_store_id}`

DeleteMemoryStore

### Parameters

- `memory_store_id: String`

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

- `class BetaManagedAgentsDeletedMemoryStore`

  - `id: String`

  - `type: :memory_store_deleted`

    - `:memory_store_deleted`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_deleted_memory_store = anthropic.beta.memory_stores.delete("memory_store_id")

puts(beta_managed_agents_deleted_memory_store)
```

## Archive

`beta.memory_stores.archive(memory_store_id, **kwargs) -> BetaManagedAgentsMemoryStore`

**post** `/v1/memory_stores/{memory_store_id}/archive`

ArchiveMemoryStore

### Parameters

- `memory_store_id: String`

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

- `class BetaManagedAgentsMemoryStore`

  - `id: String`

  - `type: :memory_store`

    - `:memory_store`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `description: String`

  - `metadata: Hash[Symbol, String]`

  - `name: String`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory_store = anthropic.beta.memory_stores.archive("memory_store_id")

puts(beta_managed_agents_memory_store)
```

## Domain Types

### Beta Managed Agents Deleted Memory Store

- `class BetaManagedAgentsDeletedMemoryStore`

  - `id: String`

  - `type: :memory_store_deleted`

    - `:memory_store_deleted`

### Beta Managed Agents Memory Store

- `class BetaManagedAgentsMemoryStore`

  - `id: String`

  - `type: :memory_store`

    - `:memory_store`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `description: String`

  - `metadata: Hash[Symbol, String]`

  - `name: String`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

# Memories

## Create

`beta.memory_stores.memories.create(memory_store_id, **kwargs) -> BetaManagedAgentsMemory`

**post** `/v1/memory_stores/{memory_store_id}/memories`

CreateMemory

### Parameters

- `memory_store_id: String`

- `content: String`

- `path: String`

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

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory = anthropic.beta.memory_stores.memories.create("memory_store_id", content: "content", path: "xx")

puts(beta_managed_agents_memory)
```

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

## Retrieve

`beta.memory_stores.memories.retrieve(memory_id, **kwargs) -> BetaManagedAgentsMemory`

**get** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

GetMemory

### Parameters

- `memory_store_id: String`

- `memory_id: String`

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

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory = anthropic.beta.memory_stores.memories.retrieve("memory_id", memory_store_id: "memory_store_id")

puts(beta_managed_agents_memory)
```

## Update

`beta.memory_stores.memories.update(memory_id, **kwargs) -> BetaManagedAgentsMemory`

**post** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

UpdateMemory

### Parameters

- `memory_store_id: String`

- `memory_id: String`

- `view: BetaManagedAgentsMemoryView`

  Query parameter for view

  - `:basic`

  - `:full`

- `content: String`

- `path: String`

- `precondition: BetaManagedAgentsPrecondition`

  - `type: :content_sha256`

    - `:content_sha256`

  - `content_sha256: String`

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

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory = anthropic.beta.memory_stores.memories.update("memory_id", memory_store_id: "memory_store_id")

puts(beta_managed_agents_memory)
```

## Delete

`beta.memory_stores.memories.delete(memory_id, **kwargs) -> BetaManagedAgentsDeletedMemory`

**delete** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

DeleteMemory

### Parameters

- `memory_store_id: String`

- `memory_id: String`

- `expected_content_sha256: String`

  Query parameter for expected_content_sha256

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

- `class BetaManagedAgentsDeletedMemory`

  - `id: String`

  - `type: :memory_deleted`

    - `:memory_deleted`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_deleted_memory = anthropic.beta.memory_stores.memories.delete("memory_id", memory_store_id: "memory_store_id")

puts(beta_managed_agents_deleted_memory)
```

## Domain Types

### Beta Managed Agents Content Sha256 Precondition

- `class BetaManagedAgentsContentSha256Precondition`

  - `type: :content_sha256`

    - `:content_sha256`

  - `content_sha256: String`

### Beta Managed Agents Deleted Memory

- `class BetaManagedAgentsDeletedMemory`

  - `id: String`

  - `type: :memory_deleted`

    - `:memory_deleted`

### Beta Managed Agents Memory

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

### Beta Managed Agents Memory List Item

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

### Beta Managed Agents Memory Path Conflict Error

- `class BetaManagedAgentsMemoryPathConflictError`

  - `type: :memory_path_conflict_error`

    - `:memory_path_conflict_error`

  - `conflicting_memory_id: String`

  - `conflicting_path: String`

  - `message: String`

### Beta Managed Agents Memory Precondition Failed Error

- `class BetaManagedAgentsMemoryPreconditionFailedError`

  - `type: :memory_precondition_failed_error`

    - `:memory_precondition_failed_error`

  - `message: String`

### Beta Managed Agents Memory Prefix

- `class BetaManagedAgentsMemoryPrefix`

  - `path: String`

  - `type: :memory_prefix`

    - `:memory_prefix`

### Beta Managed Agents Memory View

- `BetaManagedAgentsMemoryView = :basic | :full`

  MemoryView enum

  - `:basic`

  - `:full`

### Beta Managed Agents Precondition

- `class BetaManagedAgentsPrecondition`

  - `type: :content_sha256`

    - `:content_sha256`

  - `content_sha256: String`

# Memory Versions

## List

`beta.memory_stores.memory_versions.list(memory_store_id, **kwargs) -> PageCursor<BetaManagedAgentsMemoryVersion>`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions`

ListMemoryVersions

### Parameters

- `memory_store_id: String`

- `api_key_id: String`

  Query parameter for api_key_id

- `created_at_gte: Time`

  Return versions created at or after this time (inclusive).

- `created_at_lte: Time`

  Return versions created at or before this time (inclusive).

- `limit: Integer`

  Query parameter for limit

- `memory_id: String`

  Query parameter for memory_id

- `operation: BetaManagedAgentsMemoryVersionOperation`

  Query parameter for operation

  - `:created`

  - `:modified`

  - `:deleted`

- `page: String`

  Query parameter for page

- `session_id: String`

  Query parameter for session_id

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

- `class BetaManagedAgentsMemoryVersion`

  - `id: String`

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `memory_id: String`

  - `memory_store_id: String`

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    MemoryVersionOperation enum

    - `:created`

    - `:modified`

    - `:deleted`

  - `type: :memory_version`

    - `:memory_version`

  - `content: String`

  - `content_sha256: String`

  - `content_size_bytes: Integer`

  - `created_by: BetaManagedAgentsActor`

    - `class BetaManagedAgentsSessionActor`

      - `session_id: String`

      - `type: :session_actor`

        - `:session_actor`

    - `class BetaManagedAgentsAPIActor`

      - `api_key_id: String`

      - `type: :api_actor`

        - `:api_actor`

    - `class BetaManagedAgentsUserActor`

      - `type: :user_actor`

        - `:user_actor`

      - `user_id: String`

  - `path: String`

  - `redacted_at: Time`

    A timestamp in RFC 3339 format

  - `redacted_by: BetaManagedAgentsActor`

    - `class BetaManagedAgentsSessionActor`

      - `session_id: String`

      - `type: :session_actor`

        - `:session_actor`

    - `class BetaManagedAgentsAPIActor`

      - `api_key_id: String`

      - `type: :api_actor`

        - `:api_actor`

    - `class BetaManagedAgentsUserActor`

      - `type: :user_actor`

        - `:user_actor`

      - `user_id: String`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.memory_stores.memory_versions.list("memory_store_id")

puts(page)
```

## Retrieve

`beta.memory_stores.memory_versions.retrieve(memory_version_id, **kwargs) -> BetaManagedAgentsMemoryVersion`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

GetMemoryVersion

### Parameters

- `memory_store_id: String`

- `memory_version_id: String`

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

- `class BetaManagedAgentsMemoryVersion`

  - `id: String`

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `memory_id: String`

  - `memory_store_id: String`

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    MemoryVersionOperation enum

    - `:created`

    - `:modified`

    - `:deleted`

  - `type: :memory_version`

    - `:memory_version`

  - `content: String`

  - `content_sha256: String`

  - `content_size_bytes: Integer`

  - `created_by: BetaManagedAgentsActor`

    - `class BetaManagedAgentsSessionActor`

      - `session_id: String`

      - `type: :session_actor`

        - `:session_actor`

    - `class BetaManagedAgentsAPIActor`

      - `api_key_id: String`

      - `type: :api_actor`

        - `:api_actor`

    - `class BetaManagedAgentsUserActor`

      - `type: :user_actor`

        - `:user_actor`

      - `user_id: String`

  - `path: String`

  - `redacted_at: Time`

    A timestamp in RFC 3339 format

  - `redacted_by: BetaManagedAgentsActor`

    - `class BetaManagedAgentsSessionActor`

      - `session_id: String`

      - `type: :session_actor`

        - `:session_actor`

    - `class BetaManagedAgentsAPIActor`

      - `api_key_id: String`

      - `type: :api_actor`

        - `:api_actor`

    - `class BetaManagedAgentsUserActor`

      - `type: :user_actor`

        - `:user_actor`

      - `user_id: String`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory_version = anthropic.beta.memory_stores.memory_versions.retrieve(
  "memory_version_id",
  memory_store_id: "memory_store_id"
)

puts(beta_managed_agents_memory_version)
```

## Redact

`beta.memory_stores.memory_versions.redact(memory_version_id, **kwargs) -> BetaManagedAgentsMemoryVersion`

**post** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

RedactMemoryVersion

### Parameters

- `memory_store_id: String`

- `memory_version_id: String`

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

- `class BetaManagedAgentsMemoryVersion`

  - `id: String`

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `memory_id: String`

  - `memory_store_id: String`

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    MemoryVersionOperation enum

    - `:created`

    - `:modified`

    - `:deleted`

  - `type: :memory_version`

    - `:memory_version`

  - `content: String`

  - `content_sha256: String`

  - `content_size_bytes: Integer`

  - `created_by: BetaManagedAgentsActor`

    - `class BetaManagedAgentsSessionActor`

      - `session_id: String`

      - `type: :session_actor`

        - `:session_actor`

    - `class BetaManagedAgentsAPIActor`

      - `api_key_id: String`

      - `type: :api_actor`

        - `:api_actor`

    - `class BetaManagedAgentsUserActor`

      - `type: :user_actor`

        - `:user_actor`

      - `user_id: String`

  - `path: String`

  - `redacted_at: Time`

    A timestamp in RFC 3339 format

  - `redacted_by: BetaManagedAgentsActor`

    - `class BetaManagedAgentsSessionActor`

      - `session_id: String`

      - `type: :session_actor`

        - `:session_actor`

    - `class BetaManagedAgentsAPIActor`

      - `api_key_id: String`

      - `type: :api_actor`

        - `:api_actor`

    - `class BetaManagedAgentsUserActor`

      - `type: :user_actor`

        - `:user_actor`

      - `user_id: String`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory_version = anthropic.beta.memory_stores.memory_versions.redact(
  "memory_version_id",
  memory_store_id: "memory_store_id"
)

puts(beta_managed_agents_memory_version)
```

## Domain Types

### Beta Managed Agents Actor

- `BetaManagedAgentsActor = BetaManagedAgentsSessionActor | BetaManagedAgentsAPIActor | BetaManagedAgentsUserActor`

  - `class BetaManagedAgentsSessionActor`

    - `session_id: String`

    - `type: :session_actor`

      - `:session_actor`

  - `class BetaManagedAgentsAPIActor`

    - `api_key_id: String`

    - `type: :api_actor`

      - `:api_actor`

  - `class BetaManagedAgentsUserActor`

    - `type: :user_actor`

      - `:user_actor`

    - `user_id: String`

### Beta Managed Agents API Actor

- `class BetaManagedAgentsAPIActor`

  - `api_key_id: String`

  - `type: :api_actor`

    - `:api_actor`

### Beta Managed Agents Memory Version

- `class BetaManagedAgentsMemoryVersion`

  - `id: String`

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `memory_id: String`

  - `memory_store_id: String`

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    MemoryVersionOperation enum

    - `:created`

    - `:modified`

    - `:deleted`

  - `type: :memory_version`

    - `:memory_version`

  - `content: String`

  - `content_sha256: String`

  - `content_size_bytes: Integer`

  - `created_by: BetaManagedAgentsActor`

    - `class BetaManagedAgentsSessionActor`

      - `session_id: String`

      - `type: :session_actor`

        - `:session_actor`

    - `class BetaManagedAgentsAPIActor`

      - `api_key_id: String`

      - `type: :api_actor`

        - `:api_actor`

    - `class BetaManagedAgentsUserActor`

      - `type: :user_actor`

        - `:user_actor`

      - `user_id: String`

  - `path: String`

  - `redacted_at: Time`

    A timestamp in RFC 3339 format

  - `redacted_by: BetaManagedAgentsActor`

    - `class BetaManagedAgentsSessionActor`

      - `session_id: String`

      - `type: :session_actor`

        - `:session_actor`

    - `class BetaManagedAgentsAPIActor`

      - `api_key_id: String`

      - `type: :api_actor`

        - `:api_actor`

    - `class BetaManagedAgentsUserActor`

      - `type: :user_actor`

        - `:user_actor`

      - `user_id: String`

### Beta Managed Agents Memory Version Operation

- `BetaManagedAgentsMemoryVersionOperation = :created | :modified | :deleted`

  MemoryVersionOperation enum

  - `:created`

  - `:modified`

  - `:deleted`

### Beta Managed Agents Session Actor

- `class BetaManagedAgentsSessionActor`

  - `session_id: String`

  - `type: :session_actor`

    - `:session_actor`

### Beta Managed Agents User Actor

- `class BetaManagedAgentsUserActor`

  - `type: :user_actor`

    - `:user_actor`

  - `user_id: String`
