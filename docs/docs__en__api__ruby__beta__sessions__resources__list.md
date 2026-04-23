## List

`beta.sessions.resources.list(session_id, **kwargs) -> PageCursor<BetaManagedAgentsSessionResource>`

**get** `/v1/sessions/{session_id}/resources`

List Session Resources

### Parameters

- `session_id: String`

- `limit: Integer`

  Maximum number of resources to return per page (max 1000). If omitted, returns all resources.

- `page: String`

  Opaque cursor from a previous response's next_page field.

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

- `BetaManagedAgentsSessionResource = BetaManagedAgentsGitHubRepositoryResource | BetaManagedAgentsFileResource | BetaManagedAgentsMemoryStoreResource`

  A memory store attached to an agent session.

  - `class BetaManagedAgentsGitHubRepositoryResource`

    - `id: String`

    - `created_at: Time`

      A timestamp in RFC 3339 format

    - `mount_path: String`

    - `type: :github_repository`

      - `:github_repository`

    - `updated_at: Time`

      A timestamp in RFC 3339 format

    - `url: String`

    - `checkout: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout`

      - `class BetaManagedAgentsBranchCheckout`

        - `name: String`

          Branch name to check out.

        - `type: :branch`

          - `:branch`

      - `class BetaManagedAgentsCommitCheckout`

        - `sha: String`

          Full commit SHA to check out.

        - `type: :commit`

          - `:commit`

  - `class BetaManagedAgentsFileResource`

    - `id: String`

    - `created_at: Time`

      A timestamp in RFC 3339 format

    - `file_id: String`

    - `mount_path: String`

    - `type: :file`

      - `:file`

    - `updated_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsMemoryStoreResource`

    A memory store attached to an agent session.

    - `memory_store_id: String`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: :memory_store`

      - `:memory_store`

    - `access: :read_write | :read_only`

      Access mode for an attached memory store.

      - `:read_write`

      - `:read_only`

    - `description: String`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions: String`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `mount_path: String`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name: String`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.sessions.resources.list("sesn_011CZkZAtmR3yMPDzynEDxu7")

puts(page)
```
