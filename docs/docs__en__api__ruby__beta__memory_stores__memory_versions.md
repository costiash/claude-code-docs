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
