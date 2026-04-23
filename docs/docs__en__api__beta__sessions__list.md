## List

**get** `/v1/sessions`

List Sessions

### Query Parameters

- `agent_id: optional string`

  Filter sessions created with this agent ID.

- `agent_version: optional number`

  Filter by agent version. Only applies when agent_id is also set.

- `"created_at[gt]": optional string`

  Return sessions created after this time (exclusive).

- `"created_at[gte]": optional string`

  Return sessions created at or after this time (inclusive).

- `"created_at[lt]": optional string`

  Return sessions created before this time (exclusive).

- `"created_at[lte]": optional string`

  Return sessions created at or before this time (inclusive).

- `include_archived: optional boolean`

  When true, includes archived sessions. Default: false (exclude archived).

- `limit: optional number`

  Maximum number of results to return.

- `order: optional "asc" or "desc"`

  Sort direction for results, ordered by created_at. Defaults to desc (newest first).

  - `"asc"`

  - `"desc"`

- `page: optional string`

  Opaque pagination cursor from a previous response's next_page.

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

- `data: optional array of BetaManagedAgentsSession`

  List of sessions.

  - `id: string`

  - `agent: BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `id: string`

    - `description: string`

    - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

      - `name: string`

      - `type: "url"`

        - `"url"`

      - `url: string`

    - `model: BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `UnionMember0 = "claude-opus-4-7" or "claude-opus-4-6" or "claude-sonnet-4-6" or 6 more`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-opus-4-7"`

            Frontier intelligence for long-running agents and coding

          - `"claude-opus-4-6"`

            Most intelligent model for building agents and coding

          - `"claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `"claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `"claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `"claude-opus-4-5"`

            Premium model combining maximum intelligence with practical performance

          - `"claude-opus-4-5-20251101"`

            Premium model combining maximum intelligence with practical performance

          - `"claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `"claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `UnionMember1 = string`

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `name: string`

    - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

      - `BetaManagedAgentsAnthropicSkill = object { skill_id, type, version }`

        A resolved Anthropic-managed skill.

        - `skill_id: string`

        - `type: "anthropic"`

          - `"anthropic"`

        - `version: string`

      - `BetaManagedAgentsCustomSkill = object { skill_id, type, version }`

        A resolved user-created custom skill.

        - `skill_id: string`

        - `type: "custom"`

          - `"custom"`

        - `version: string`

    - `system: string`

    - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

      - `BetaManagedAgentsAgentToolset20260401 = object { configs, default_config, type }`

        - `configs: array of BetaManagedAgentsAgentToolConfig`

          - `enabled: boolean`

          - `name: "bash" or "edit" or "read" or 5 more`

            Built-in agent tool identifier.

            - `"bash"`

            - `"edit"`

            - `"read"`

            - `"write"`

            - `"glob"`

            - `"grep"`

            - `"web_fetch"`

            - `"web_search"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy = object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `BetaManagedAgentsAlwaysAskPolicy = object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

          Resolved default configuration for agent tools.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy = object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `BetaManagedAgentsAlwaysAskPolicy = object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `type: "agent_toolset_20260401"`

          - `"agent_toolset_20260401"`

      - `BetaManagedAgentsMCPToolset = object { configs, default_config, mcp_server_name, type }`

        - `configs: array of BetaManagedAgentsMCPToolConfig`

          - `enabled: boolean`

          - `name: string`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy = object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `BetaManagedAgentsAlwaysAskPolicy = object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy = object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `BetaManagedAgentsAlwaysAskPolicy = object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `mcp_server_name: string`

        - `type: "mcp_toolset"`

          - `"mcp_toolset"`

      - `BetaManagedAgentsCustomTool = object { description, input_schema, name, type }`

        A custom tool as returned in API responses.

        - `description: string`

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `properties: optional map[unknown]`

            JSON Schema properties defining the tool's input parameters.

          - `required: optional array of string`

            List of required property names.

          - `type: optional "object"`

            Must be 'object' for tool input schemas.

            - `"object"`

        - `name: string`

        - `type: "custom"`

          - `"custom"`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `environment_id: string`

  - `metadata: map[string]`

  - `resources: array of BetaManagedAgentsSessionResource`

    - `BetaManagedAgentsGitHubRepositoryResource = object { id, created_at, mount_path, 4 more }`

      - `id: string`

      - `created_at: string`

        A timestamp in RFC 3339 format

      - `mount_path: string`

      - `type: "github_repository"`

        - `"github_repository"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

      - `url: string`

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        - `BetaManagedAgentsBranchCheckout = object { name, type }`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `BetaManagedAgentsCommitCheckout = object { sha, type }`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

    - `BetaManagedAgentsFileResource = object { id, created_at, file_id, 3 more }`

      - `id: string`

      - `created_at: string`

        A timestamp in RFC 3339 format

      - `file_id: string`

      - `mount_path: string`

      - `type: "file"`

        - `"file"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

    - `BetaManagedAgentsMemoryStoreResource = object { memory_store_id, type, access, 4 more }`

      A memory store attached to an agent session.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `description: optional string`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      - `mount_path: optional string`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `name: optional string`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `stats: BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `active_seconds: optional number`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

    - `duration_seconds: optional number`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

  - `status: "rescheduling" or "running" or "idle" or "terminated"`

    SessionStatus enum

    - `"rescheduling"`

    - `"running"`

    - `"idle"`

    - `"terminated"`

  - `title: string`

  - `type: "session"`

    - `"session"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `usage: BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

    - `cache_creation: optional BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: optional number`

        Tokens used to create 1-hour ephemeral cache entries.

      - `ephemeral_5m_input_tokens: optional number`

        Tokens used to create 5-minute ephemeral cache entries.

    - `cache_read_input_tokens: optional number`

      Total tokens read from prompt cache.

    - `input_tokens: optional number`

      Total input tokens consumed across all turns.

    - `output_tokens: optional number`

      Total output tokens generated across all turns.

  - `vault_ids: array of string`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

- `next_page: optional string`

  Opaque cursor for the next page. Null when no more results.

### Example

```http
curl https://api.anthropic.com/v1/sessions \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```
