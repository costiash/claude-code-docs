# Sessions

## Create

`$ ant beta:sessions create`

**post** `/v1/sessions`

Create Session

### Parameters

- `--agent: string or BetaManagedAgentsAgentParams`

  Body param: Agent identifier. Accepts the `agent` ID string, which pins the latest version for the session, or an `agent` object with both id and version specified.

- `--environment-id: string`

  Body param: ID of the `environment` defining the container configuration for this session.

- `--metadata: optional map[string]`

  Body param: Arbitrary key-value metadata attached to the session. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `--resource: optional array of BetaManagedAgentsGitHubRepositoryResourceParams or BetaManagedAgentsFileResourceParams or BetaManagedAgentsMemoryStoreResourceParam`

  Body param: Resources (e.g. repositories, files) to mount into the session's container.

- `--title: optional string`

  Body param: Human-readable session title.

- `--vault-id: optional array of string`

  Body param: Vault IDs for stored credentials the agent can use during the session.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_session: object { id, agent, archived_at, 11 more }`

  A Managed Agents `session`.

  - `id: string`

  - `agent: object { id, description, mcp_servers, 7 more }`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `id: string`

    - `description: string`

    - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

      - `name: string`

      - `type: "url"`

        - `"url"`

      - `url: string`

    - `model: object { id, speed }`

      Model identifier and configuration.

      - `id: "claude-opus-4-7" or "claude-opus-4-6" or "claude-sonnet-4-6" or 6 more or string`

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

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `name: string`

    - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

      - `beta_managed_agents_anthropic_skill: object { skill_id, type, version }`

        A resolved Anthropic-managed skill.

        - `skill_id: string`

        - `type: "anthropic"`

          - `"anthropic"`

        - `version: string`

      - `beta_managed_agents_custom_skill: object { skill_id, type, version }`

        A resolved user-created custom skill.

        - `skill_id: string`

        - `type: "custom"`

          - `"custom"`

        - `version: string`

    - `system: string`

    - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

      - `beta_managed_agents_agent_toolset20260401: object { configs, default_config, type }`

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

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `default_config: object { enabled, permission_policy }`

          Resolved default configuration for agent tools.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `type: "agent_toolset_20260401"`

          - `"agent_toolset_20260401"`

      - `beta_managed_agents_mcp_toolset: object { configs, default_config, mcp_server_name, type }`

        - `configs: array of BetaManagedAgentsMCPToolConfig`

          - `enabled: boolean`

          - `name: string`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `default_config: object { enabled, permission_policy }`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `mcp_server_name: string`

        - `type: "mcp_toolset"`

          - `"mcp_toolset"`

      - `beta_managed_agents_custom_tool: object { description, input_schema, name, type }`

        A custom tool as returned in API responses.

        - `description: string`

        - `input_schema: object { properties, required, type }`

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

    - `beta_managed_agents_github_repository_resource: object { id, created_at, mount_path, 4 more }`

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

        - `beta_managed_agents_branch_checkout: object { name, type }`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `beta_managed_agents_commit_checkout: object { sha, type }`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

    - `beta_managed_agents_file_resource: object { id, created_at, file_id, 3 more }`

      - `id: string`

      - `created_at: string`

        A timestamp in RFC 3339 format

      - `file_id: string`

      - `mount_path: string`

      - `type: "file"`

        - `"file"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

    - `beta_managed_agents_memory_store_resource: object { memory_store_id, type, access, 4 more }`

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

  - `stats: object { active_seconds, duration_seconds }`

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

  - `usage: object { cache_creation, cache_read_input_tokens, input_tokens, output_tokens }`

    Cumulative token usage for a session across all turns.

    - `cache_creation: optional object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

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

### Example

```cli
ant beta:sessions create \
  --api-key my-anthropic-api-key \
  --agent agent_011CZkYpogX7uDKUyvBTophP \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW
```

## List

`$ ant beta:sessions list`

**get** `/v1/sessions`

List Sessions

### Parameters

- `--agent-id: optional string`

  Query param: Filter sessions created with this agent ID.

- `--agent-version: optional number`

  Query param: Filter by agent version. Only applies when agent_id is also set.

- `--created-at-gt: optional string`

  Query param: Return sessions created after this time (exclusive).

- `--created-at-gte: optional string`

  Query param: Return sessions created at or after this time (inclusive).

- `--created-at-lt: optional string`

  Query param: Return sessions created before this time (exclusive).

- `--created-at-lte: optional string`

  Query param: Return sessions created at or before this time (inclusive).

- `--include-archived: optional boolean`

  Query param: When true, includes archived sessions. Default: false (exclude archived).

- `--limit: optional number`

  Query param: Maximum number of results to return.

- `--memory-store-id: optional string`

  Query param: Filter sessions whose resources contain a memory_store with this memory store ID.

- `--order: optional "asc" or "desc"`

  Query param: Sort direction for results, ordered by created_at. Defaults to desc (newest first).

- `--page: optional string`

  Query param: Opaque pagination cursor from a previous response's next_page.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsListSessions: object { data, next_page }`

  Paginated list of sessions.

  - `data: optional array of BetaManagedAgentsSession`

    List of sessions.

    - `id: string`

    - `agent: object { id, description, mcp_servers, 7 more }`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `id: string`

      - `description: string`

      - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

        - `name: string`

        - `type: "url"`

          - `"url"`

        - `url: string`

      - `model: object { id, speed }`

        Model identifier and configuration.

        - `id: "claude-opus-4-7" or "claude-opus-4-6" or "claude-sonnet-4-6" or 6 more or string`

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

        - `speed: optional "standard" or "fast"`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `name: string`

      - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

        - `beta_managed_agents_anthropic_skill: object { skill_id, type, version }`

          A resolved Anthropic-managed skill.

          - `skill_id: string`

          - `type: "anthropic"`

            - `"anthropic"`

          - `version: string`

        - `beta_managed_agents_custom_skill: object { skill_id, type, version }`

          A resolved user-created custom skill.

          - `skill_id: string`

          - `type: "custom"`

            - `"custom"`

          - `version: string`

      - `system: string`

      - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

        - `beta_managed_agents_agent_toolset20260401: object { configs, default_config, type }`

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

              - `beta_managed_agents_always_allow_policy: object { type }`

                Tool calls are automatically approved without user confirmation.

                - `type: "always_allow"`

                  - `"always_allow"`

              - `beta_managed_agents_always_ask_policy: object { type }`

                Tool calls require user confirmation before execution.

                - `type: "always_ask"`

                  - `"always_ask"`

          - `default_config: object { enabled, permission_policy }`

            Resolved default configuration for agent tools.

            - `enabled: boolean`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object { type }`

                Tool calls are automatically approved without user confirmation.

                - `type: "always_allow"`

                  - `"always_allow"`

              - `beta_managed_agents_always_ask_policy: object { type }`

                Tool calls require user confirmation before execution.

                - `type: "always_ask"`

                  - `"always_ask"`

          - `type: "agent_toolset_20260401"`

            - `"agent_toolset_20260401"`

        - `beta_managed_agents_mcp_toolset: object { configs, default_config, mcp_server_name, type }`

          - `configs: array of BetaManagedAgentsMCPToolConfig`

            - `enabled: boolean`

            - `name: string`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object { type }`

                Tool calls are automatically approved without user confirmation.

                - `type: "always_allow"`

                  - `"always_allow"`

              - `beta_managed_agents_always_ask_policy: object { type }`

                Tool calls require user confirmation before execution.

                - `type: "always_ask"`

                  - `"always_ask"`

          - `default_config: object { enabled, permission_policy }`

            Resolved default configuration for all tools from an MCP server.

            - `enabled: boolean`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object { type }`

                Tool calls are automatically approved without user confirmation.

                - `type: "always_allow"`

                  - `"always_allow"`

              - `beta_managed_agents_always_ask_policy: object { type }`

                Tool calls require user confirmation before execution.

                - `type: "always_ask"`

                  - `"always_ask"`

          - `mcp_server_name: string`

          - `type: "mcp_toolset"`

            - `"mcp_toolset"`

        - `beta_managed_agents_custom_tool: object { description, input_schema, name, type }`

          A custom tool as returned in API responses.

          - `description: string`

          - `input_schema: object { properties, required, type }`

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

      - `beta_managed_agents_github_repository_resource: object { id, created_at, mount_path, 4 more }`

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

          - `beta_managed_agents_branch_checkout: object { name, type }`

            - `name: string`

              Branch name to check out.

            - `type: "branch"`

              - `"branch"`

          - `beta_managed_agents_commit_checkout: object { sha, type }`

            - `sha: string`

              Full commit SHA to check out.

            - `type: "commit"`

              - `"commit"`

      - `beta_managed_agents_file_resource: object { id, created_at, file_id, 3 more }`

        - `id: string`

        - `created_at: string`

          A timestamp in RFC 3339 format

        - `file_id: string`

        - `mount_path: string`

        - `type: "file"`

          - `"file"`

        - `updated_at: string`

          A timestamp in RFC 3339 format

      - `beta_managed_agents_memory_store_resource: object { memory_store_id, type, access, 4 more }`

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

    - `stats: object { active_seconds, duration_seconds }`

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

    - `usage: object { cache_creation, cache_read_input_tokens, input_tokens, output_tokens }`

      Cumulative token usage for a session across all turns.

      - `cache_creation: optional object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

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

```cli
ant beta:sessions list \
  --api-key my-anthropic-api-key
```

## Retrieve

`$ ant beta:sessions retrieve`

**get** `/v1/sessions/{session_id}`

Get Session

### Parameters

- `--session-id: string`

  Path parameter session_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_session: object { id, agent, archived_at, 11 more }`

  A Managed Agents `session`.

  - `id: string`

  - `agent: object { id, description, mcp_servers, 7 more }`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `id: string`

    - `description: string`

    - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

      - `name: string`

      - `type: "url"`

        - `"url"`

      - `url: string`

    - `model: object { id, speed }`

      Model identifier and configuration.

      - `id: "claude-opus-4-7" or "claude-opus-4-6" or "claude-sonnet-4-6" or 6 more or string`

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

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `name: string`

    - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

      - `beta_managed_agents_anthropic_skill: object { skill_id, type, version }`

        A resolved Anthropic-managed skill.

        - `skill_id: string`

        - `type: "anthropic"`

          - `"anthropic"`

        - `version: string`

      - `beta_managed_agents_custom_skill: object { skill_id, type, version }`

        A resolved user-created custom skill.

        - `skill_id: string`

        - `type: "custom"`

          - `"custom"`

        - `version: string`

    - `system: string`

    - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

      - `beta_managed_agents_agent_toolset20260401: object { configs, default_config, type }`

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

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `default_config: object { enabled, permission_policy }`

          Resolved default configuration for agent tools.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `type: "agent_toolset_20260401"`

          - `"agent_toolset_20260401"`

      - `beta_managed_agents_mcp_toolset: object { configs, default_config, mcp_server_name, type }`

        - `configs: array of BetaManagedAgentsMCPToolConfig`

          - `enabled: boolean`

          - `name: string`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `default_config: object { enabled, permission_policy }`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `mcp_server_name: string`

        - `type: "mcp_toolset"`

          - `"mcp_toolset"`

      - `beta_managed_agents_custom_tool: object { description, input_schema, name, type }`

        A custom tool as returned in API responses.

        - `description: string`

        - `input_schema: object { properties, required, type }`

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

    - `beta_managed_agents_github_repository_resource: object { id, created_at, mount_path, 4 more }`

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

        - `beta_managed_agents_branch_checkout: object { name, type }`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `beta_managed_agents_commit_checkout: object { sha, type }`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

    - `beta_managed_agents_file_resource: object { id, created_at, file_id, 3 more }`

      - `id: string`

      - `created_at: string`

        A timestamp in RFC 3339 format

      - `file_id: string`

      - `mount_path: string`

      - `type: "file"`

        - `"file"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

    - `beta_managed_agents_memory_store_resource: object { memory_store_id, type, access, 4 more }`

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

  - `stats: object { active_seconds, duration_seconds }`

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

  - `usage: object { cache_creation, cache_read_input_tokens, input_tokens, output_tokens }`

    Cumulative token usage for a session across all turns.

    - `cache_creation: optional object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

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

### Example

```cli
ant beta:sessions retrieve \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7
```

## Update

`$ ant beta:sessions update`

**post** `/v1/sessions/{session_id}`

Update Session

### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--metadata: optional map[string]`

  Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve.

- `--title: optional string`

  Body param: Human-readable session title.

- `--vault-id: optional array of string`

  Body param: Vault IDs (`vlt_*`) to attach to the session. Not yet supported; requests setting this field are rejected. Reserved for future use.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_session: object { id, agent, archived_at, 11 more }`

  A Managed Agents `session`.

  - `id: string`

  - `agent: object { id, description, mcp_servers, 7 more }`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `id: string`

    - `description: string`

    - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

      - `name: string`

      - `type: "url"`

        - `"url"`

      - `url: string`

    - `model: object { id, speed }`

      Model identifier and configuration.

      - `id: "claude-opus-4-7" or "claude-opus-4-6" or "claude-sonnet-4-6" or 6 more or string`

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

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `name: string`

    - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

      - `beta_managed_agents_anthropic_skill: object { skill_id, type, version }`

        A resolved Anthropic-managed skill.

        - `skill_id: string`

        - `type: "anthropic"`

          - `"anthropic"`

        - `version: string`

      - `beta_managed_agents_custom_skill: object { skill_id, type, version }`

        A resolved user-created custom skill.

        - `skill_id: string`

        - `type: "custom"`

          - `"custom"`

        - `version: string`

    - `system: string`

    - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

      - `beta_managed_agents_agent_toolset20260401: object { configs, default_config, type }`

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

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `default_config: object { enabled, permission_policy }`

          Resolved default configuration for agent tools.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `type: "agent_toolset_20260401"`

          - `"agent_toolset_20260401"`

      - `beta_managed_agents_mcp_toolset: object { configs, default_config, mcp_server_name, type }`

        - `configs: array of BetaManagedAgentsMCPToolConfig`

          - `enabled: boolean`

          - `name: string`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `default_config: object { enabled, permission_policy }`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `mcp_server_name: string`

        - `type: "mcp_toolset"`

          - `"mcp_toolset"`

      - `beta_managed_agents_custom_tool: object { description, input_schema, name, type }`

        A custom tool as returned in API responses.

        - `description: string`

        - `input_schema: object { properties, required, type }`

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

    - `beta_managed_agents_github_repository_resource: object { id, created_at, mount_path, 4 more }`

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

        - `beta_managed_agents_branch_checkout: object { name, type }`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `beta_managed_agents_commit_checkout: object { sha, type }`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

    - `beta_managed_agents_file_resource: object { id, created_at, file_id, 3 more }`

      - `id: string`

      - `created_at: string`

        A timestamp in RFC 3339 format

      - `file_id: string`

      - `mount_path: string`

      - `type: "file"`

        - `"file"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

    - `beta_managed_agents_memory_store_resource: object { memory_store_id, type, access, 4 more }`

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

  - `stats: object { active_seconds, duration_seconds }`

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

  - `usage: object { cache_creation, cache_read_input_tokens, input_tokens, output_tokens }`

    Cumulative token usage for a session across all turns.

    - `cache_creation: optional object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

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

### Example

```cli
ant beta:sessions update \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7
```

## Delete

`$ ant beta:sessions delete`

**delete** `/v1/sessions/{session_id}`

Delete Session

### Parameters

- `--session-id: string`

  Path parameter session_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deleted_session: object { id, type }`

  Confirmation that a `session` has been permanently deleted.

  - `id: string`

  - `type: "session_deleted"`

    - `"session_deleted"`

### Example

```cli
ant beta:sessions delete \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7
```

## Archive

`$ ant beta:sessions archive`

**post** `/v1/sessions/{session_id}/archive`

Archive Session

### Parameters

- `--session-id: string`

  Path parameter session_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_session: object { id, agent, archived_at, 11 more }`

  A Managed Agents `session`.

  - `id: string`

  - `agent: object { id, description, mcp_servers, 7 more }`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `id: string`

    - `description: string`

    - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

      - `name: string`

      - `type: "url"`

        - `"url"`

      - `url: string`

    - `model: object { id, speed }`

      Model identifier and configuration.

      - `id: "claude-opus-4-7" or "claude-opus-4-6" or "claude-sonnet-4-6" or 6 more or string`

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

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `name: string`

    - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

      - `beta_managed_agents_anthropic_skill: object { skill_id, type, version }`

        A resolved Anthropic-managed skill.

        - `skill_id: string`

        - `type: "anthropic"`

          - `"anthropic"`

        - `version: string`

      - `beta_managed_agents_custom_skill: object { skill_id, type, version }`

        A resolved user-created custom skill.

        - `skill_id: string`

        - `type: "custom"`

          - `"custom"`

        - `version: string`

    - `system: string`

    - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

      - `beta_managed_agents_agent_toolset20260401: object { configs, default_config, type }`

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

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `default_config: object { enabled, permission_policy }`

          Resolved default configuration for agent tools.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `type: "agent_toolset_20260401"`

          - `"agent_toolset_20260401"`

      - `beta_managed_agents_mcp_toolset: object { configs, default_config, mcp_server_name, type }`

        - `configs: array of BetaManagedAgentsMCPToolConfig`

          - `enabled: boolean`

          - `name: string`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `default_config: object { enabled, permission_policy }`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `mcp_server_name: string`

        - `type: "mcp_toolset"`

          - `"mcp_toolset"`

      - `beta_managed_agents_custom_tool: object { description, input_schema, name, type }`

        A custom tool as returned in API responses.

        - `description: string`

        - `input_schema: object { properties, required, type }`

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

    - `beta_managed_agents_github_repository_resource: object { id, created_at, mount_path, 4 more }`

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

        - `beta_managed_agents_branch_checkout: object { name, type }`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `beta_managed_agents_commit_checkout: object { sha, type }`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

    - `beta_managed_agents_file_resource: object { id, created_at, file_id, 3 more }`

      - `id: string`

      - `created_at: string`

        A timestamp in RFC 3339 format

      - `file_id: string`

      - `mount_path: string`

      - `type: "file"`

        - `"file"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

    - `beta_managed_agents_memory_store_resource: object { memory_store_id, type, access, 4 more }`

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

  - `stats: object { active_seconds, duration_seconds }`

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

  - `usage: object { cache_creation, cache_read_input_tokens, input_tokens, output_tokens }`

    Cumulative token usage for a session across all turns.

    - `cache_creation: optional object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

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

### Example

```cli
ant beta:sessions archive \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7
```

## Domain Types

### Beta Managed Agents Agent Params

- `beta_managed_agents_agent_params: object { id, type, version }`

  Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

  - `id: string`

    The `agent` ID.

  - `type: "agent"`

    - `"agent"`

  - `version: optional number`

    The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

### Beta Managed Agents Branch Checkout

- `beta_managed_agents_branch_checkout: object { name, type }`

  - `name: string`

    Branch name to check out.

  - `type: "branch"`

    - `"branch"`

### Beta Managed Agents Cache Creation Usage

- `beta_managed_agents_cache_creation_usage: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

  Prompt-cache creation token usage broken down by cache lifetime.

  - `ephemeral_1h_input_tokens: optional number`

    Tokens used to create 1-hour ephemeral cache entries.

  - `ephemeral_5m_input_tokens: optional number`

    Tokens used to create 5-minute ephemeral cache entries.

### Beta Managed Agents Commit Checkout

- `beta_managed_agents_commit_checkout: object { sha, type }`

  - `sha: string`

    Full commit SHA to check out.

  - `type: "commit"`

    - `"commit"`

### Beta Managed Agents Deleted Session

- `beta_managed_agents_deleted_session: object { id, type }`

  Confirmation that a `session` has been permanently deleted.

  - `id: string`

  - `type: "session_deleted"`

    - `"session_deleted"`

### Beta Managed Agents File Resource Params

- `beta_managed_agents_file_resource_params: object { file_id, type, mount_path }`

  Mount a file uploaded via the Files API into the session.

  - `file_id: string`

    ID of a previously uploaded file.

  - `type: "file"`

    - `"file"`

  - `mount_path: optional string`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

### Beta Managed Agents GitHub Repository Resource Params

- `beta_managed_agents_github_repository_resource_params: object { authorization_token, type, url, 2 more }`

  Mount a GitHub repository into the session's container.

  - `authorization_token: string`

    GitHub authorization token used to clone the repository.

  - `type: "github_repository"`

    - `"github_repository"`

  - `url: string`

    Github URL of the repository

  - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

    Branch or commit to check out. Defaults to the repository's default branch.

    - `beta_managed_agents_branch_checkout: object { name, type }`

      - `name: string`

        Branch name to check out.

      - `type: "branch"`

        - `"branch"`

    - `beta_managed_agents_commit_checkout: object { sha, type }`

      - `sha: string`

        Full commit SHA to check out.

      - `type: "commit"`

        - `"commit"`

  - `mount_path: optional string`

    Mount path in the container. Defaults to `/workspace/<repo-name>`.

### Beta Managed Agents Memory Store Resource Param

- `beta_managed_agents_memory_store_resource_param: object { memory_store_id, type, access, instructions }`

  Parameters for attaching a memory store to an agent session.

  - `memory_store_id: string`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `type: "memory_store"`

    - `"memory_store"`

  - `access: optional "read_write" or "read_only"`

    Access mode for an attached memory store.

    - `"read_write"`

    - `"read_only"`

  - `instructions: optional string`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Session

- `beta_managed_agents_session: object { id, agent, archived_at, 11 more }`

  A Managed Agents `session`.

  - `id: string`

  - `agent: object { id, description, mcp_servers, 7 more }`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `id: string`

    - `description: string`

    - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

      - `name: string`

      - `type: "url"`

        - `"url"`

      - `url: string`

    - `model: object { id, speed }`

      Model identifier and configuration.

      - `id: "claude-opus-4-7" or "claude-opus-4-6" or "claude-sonnet-4-6" or 6 more or string`

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

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `name: string`

    - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

      - `beta_managed_agents_anthropic_skill: object { skill_id, type, version }`

        A resolved Anthropic-managed skill.

        - `skill_id: string`

        - `type: "anthropic"`

          - `"anthropic"`

        - `version: string`

      - `beta_managed_agents_custom_skill: object { skill_id, type, version }`

        A resolved user-created custom skill.

        - `skill_id: string`

        - `type: "custom"`

          - `"custom"`

        - `version: string`

    - `system: string`

    - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

      - `beta_managed_agents_agent_toolset20260401: object { configs, default_config, type }`

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

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `default_config: object { enabled, permission_policy }`

          Resolved default configuration for agent tools.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `type: "agent_toolset_20260401"`

          - `"agent_toolset_20260401"`

      - `beta_managed_agents_mcp_toolset: object { configs, default_config, mcp_server_name, type }`

        - `configs: array of BetaManagedAgentsMCPToolConfig`

          - `enabled: boolean`

          - `name: string`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `default_config: object { enabled, permission_policy }`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `mcp_server_name: string`

        - `type: "mcp_toolset"`

          - `"mcp_toolset"`

      - `beta_managed_agents_custom_tool: object { description, input_schema, name, type }`

        A custom tool as returned in API responses.

        - `description: string`

        - `input_schema: object { properties, required, type }`

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

    - `beta_managed_agents_github_repository_resource: object { id, created_at, mount_path, 4 more }`

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

        - `beta_managed_agents_branch_checkout: object { name, type }`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `beta_managed_agents_commit_checkout: object { sha, type }`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

    - `beta_managed_agents_file_resource: object { id, created_at, file_id, 3 more }`

      - `id: string`

      - `created_at: string`

        A timestamp in RFC 3339 format

      - `file_id: string`

      - `mount_path: string`

      - `type: "file"`

        - `"file"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

    - `beta_managed_agents_memory_store_resource: object { memory_store_id, type, access, 4 more }`

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

  - `stats: object { active_seconds, duration_seconds }`

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

  - `usage: object { cache_creation, cache_read_input_tokens, input_tokens, output_tokens }`

    Cumulative token usage for a session across all turns.

    - `cache_creation: optional object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

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

### Beta Managed Agents Session Agent

- `beta_managed_agents_session_agent: object { id, description, mcp_servers, 7 more }`

  Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

  - `id: string`

  - `description: string`

  - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

    - `name: string`

    - `type: "url"`

      - `"url"`

    - `url: string`

  - `model: object { id, speed }`

    Model identifier and configuration.

    - `id: "claude-opus-4-7" or "claude-opus-4-6" or "claude-sonnet-4-6" or 6 more or string`

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

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `name: string`

  - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

    - `beta_managed_agents_anthropic_skill: object { skill_id, type, version }`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

        - `"anthropic"`

      - `version: string`

    - `beta_managed_agents_custom_skill: object { skill_id, type, version }`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

        - `"custom"`

      - `version: string`

  - `system: string`

  - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

    - `beta_managed_agents_agent_toolset20260401: object { configs, default_config, type }`

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

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: object { enabled, permission_policy }`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

    - `beta_managed_agents_mcp_toolset: object { configs, default_config, mcp_server_name, type }`

      - `configs: array of BetaManagedAgentsMCPToolConfig`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `default_config: object { enabled, permission_policy }`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

              - `"always_allow"`

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

              - `"always_ask"`

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

    - `beta_managed_agents_custom_tool: object { description, input_schema, name, type }`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: object { properties, required, type }`

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

### Beta Managed Agents Session Stats

- `beta_managed_agents_session_stats: object { active_seconds, duration_seconds }`

  Timing statistics for a session.

  - `active_seconds: optional number`

    Cumulative time in seconds the session spent in running status. Excludes idle time.

  - `duration_seconds: optional number`

    Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

### Beta Managed Agents Session Usage

- `beta_managed_agents_session_usage: object { cache_creation, cache_read_input_tokens, input_tokens, output_tokens }`

  Cumulative token usage for a session across all turns.

  - `cache_creation: optional object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

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

# Events

## List

`$ ant beta:sessions:events list`

**get** `/v1/sessions/{session_id}/events`

List Events

### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--limit: optional number`

  Query param: Query parameter for limit

- `--order: optional "asc" or "desc"`

  Query param: Sort direction for results, ordered by created_at. Defaults to asc (chronological).

- `--page: optional string`

  Query param: Opaque pagination cursor from a previous response's next_page.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsListSessionEvents: object { data, next_page }`

  Paginated list of events for a `session`.

  - `data: optional array of BetaManagedAgentsSessionEvent`

    Events for the session, ordered by `created_at`.

    - `beta_managed_agents_user_message_event: object { id, content, type, processed_at }`

      A user message event in the session conversation.

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        Array of content blocks comprising the user message.

        - `beta_managed_agents_text_block: object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `beta_managed_agents_image_block: object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_url_image_source: object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `beta_managed_agents_file_image_source: object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `beta_managed_agents_document_block: object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `beta_managed_agents_url_document_source: object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `beta_managed_agents_file_document_source: object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

    - `beta_managed_agents_user_interrupt_event: object { id, type, processed_at }`

      An interrupt event that pauses agent execution and returns control to the user.

      - `id: string`

        Unique identifier for this event.

      - `type: "user.interrupt"`

        - `"user.interrupt"`

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

    - `beta_managed_agents_user_tool_confirmation_event: object { id, result, tool_use_id, 3 more }`

      A tool confirmation event that approves or denies a pending tool execution.

      - `id: string`

        Unique identifier for this event.

      - `result: "allow" or "deny"`

        UserToolConfirmationResult enum

        - `"allow"`

        - `"deny"`

      - `tool_use_id: string`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: "user.tool_confirmation"`

        - `"user.tool_confirmation"`

      - `deny_message: optional string`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

    - `beta_managed_agents_user_custom_tool_result_event: object { id, custom_tool_use_id, type, 3 more }`

      Event sent by the client providing the result of a custom tool execution.

      - `id: string`

        Unique identifier for this event.

      - `custom_tool_use_id: string`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: "user.custom_tool_result"`

        - `"user.custom_tool_result"`

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        The result content returned by the tool.

        - `beta_managed_agents_text_block: object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `beta_managed_agents_image_block: object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_url_image_source: object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `beta_managed_agents_file_image_source: object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `beta_managed_agents_document_block: object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `beta_managed_agents_url_document_source: object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `beta_managed_agents_file_document_source: object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `is_error: optional boolean`

        Whether the tool execution resulted in an error.

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

    - `beta_managed_agents_agent_custom_tool_use_event: object { id, input, name, 2 more }`

      Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

      - `id: string`

        Unique identifier for this event.

      - `input: map[unknown]`

        Input parameters for the tool call.

      - `name: string`

        Name of the custom tool being called.

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "agent.custom_tool_use"`

        - `"agent.custom_tool_use"`

    - `beta_managed_agents_agent_message_event: object { id, content, processed_at, type }`

      An agent response event in the session conversation.

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsTextBlock`

        Array of text blocks comprising the agent response.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "agent.message"`

        - `"agent.message"`

    - `beta_managed_agents_agent_thinking_event: object { id, processed_at, type }`

      Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "agent.thinking"`

        - `"agent.thinking"`

    - `beta_managed_agents_agent_mcp_tool_use_event: object { id, input, mcp_server_name, 4 more }`

      Event emitted when the agent invokes a tool provided by an MCP server.

      - `id: string`

        Unique identifier for this event.

      - `input: map[unknown]`

        Input parameters for the tool call.

      - `mcp_server_name: string`

        Name of the MCP server providing the tool.

      - `name: string`

        Name of the MCP tool being used.

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "agent.mcp_tool_use"`

        - `"agent.mcp_tool_use"`

      - `evaluated_permission: optional "allow" or "ask" or "deny"`

        AgentEvaluatedPermission enum

        - `"allow"`

        - `"ask"`

        - `"deny"`

    - `beta_managed_agents_agent_mcp_tool_result_event: object { id, mcp_tool_use_id, processed_at, 3 more }`

      Event representing the result of an MCP tool execution.

      - `id: string`

        Unique identifier for this event.

      - `mcp_tool_use_id: string`

        The id of the `agent.mcp_tool_use` event this result corresponds to.

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "agent.mcp_tool_result"`

        - `"agent.mcp_tool_result"`

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        The result content returned by the tool.

        - `beta_managed_agents_text_block: object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `beta_managed_agents_image_block: object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_url_image_source: object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `beta_managed_agents_file_image_source: object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `beta_managed_agents_document_block: object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `beta_managed_agents_url_document_source: object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `beta_managed_agents_file_document_source: object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `is_error: optional boolean`

        Whether the tool execution resulted in an error.

    - `beta_managed_agents_agent_tool_use_event: object { id, input, name, 3 more }`

      Event emitted when the agent invokes a built-in agent tool.

      - `id: string`

        Unique identifier for this event.

      - `input: map[unknown]`

        Input parameters for the tool call.

      - `name: string`

        Name of the agent tool being used.

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "agent.tool_use"`

        - `"agent.tool_use"`

      - `evaluated_permission: optional "allow" or "ask" or "deny"`

        AgentEvaluatedPermission enum

        - `"allow"`

        - `"ask"`

        - `"deny"`

    - `beta_managed_agents_agent_tool_result_event: object { id, processed_at, tool_use_id, 3 more }`

      Event representing the result of an agent tool execution.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `tool_use_id: string`

        The id of the `agent.tool_use` event this result corresponds to.

      - `type: "agent.tool_result"`

        - `"agent.tool_result"`

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        The result content returned by the tool.

        - `beta_managed_agents_text_block: object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `beta_managed_agents_image_block: object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_url_image_source: object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `beta_managed_agents_file_image_source: object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `beta_managed_agents_document_block: object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `beta_managed_agents_url_document_source: object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `beta_managed_agents_file_document_source: object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `is_error: optional boolean`

        Whether the tool execution resulted in an error.

    - `beta_managed_agents_agent_thread_context_compacted_event: object { id, processed_at, type }`

      Indicates that context compaction (summarization) occurred during the session.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "agent.thread_context_compacted"`

        - `"agent.thread_context_compacted"`

    - `beta_managed_agents_session_error_event: object { id, error, processed_at, type }`

      An error event indicating a problem occurred during session execution.

      - `id: string`

        Unique identifier for this event.

      - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 4 more`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `beta_managed_agents_unknown_error: object { message, retry_status, type }`

          An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object { type }`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

              - `type: "retrying"`

                - `"retrying"`

            - `beta_managed_agents_retry_status_exhausted: object { type }`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

              - `type: "exhausted"`

                - `"exhausted"`

            - `beta_managed_agents_retry_status_terminal: object { type }`

              The session encountered a terminal error and will transition to `terminated` state.

              - `type: "terminal"`

                - `"terminal"`

          - `type: "unknown_error"`

            - `"unknown_error"`

        - `beta_managed_agents_model_overloaded_error: object { message, retry_status, type }`

          The model is currently overloaded. Emitted after automatic retries are exhausted.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object { type }`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

              - `type: "retrying"`

                - `"retrying"`

            - `beta_managed_agents_retry_status_exhausted: object { type }`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

              - `type: "exhausted"`

                - `"exhausted"`

            - `beta_managed_agents_retry_status_terminal: object { type }`

              The session encountered a terminal error and will transition to `terminated` state.

              - `type: "terminal"`

                - `"terminal"`

          - `type: "model_overloaded_error"`

            - `"model_overloaded_error"`

        - `beta_managed_agents_model_rate_limited_error: object { message, retry_status, type }`

          The model request was rate-limited.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object { type }`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

              - `type: "retrying"`

                - `"retrying"`

            - `beta_managed_agents_retry_status_exhausted: object { type }`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

              - `type: "exhausted"`

                - `"exhausted"`

            - `beta_managed_agents_retry_status_terminal: object { type }`

              The session encountered a terminal error and will transition to `terminated` state.

              - `type: "terminal"`

                - `"terminal"`

          - `type: "model_rate_limited_error"`

            - `"model_rate_limited_error"`

        - `beta_managed_agents_model_request_failed_error: object { message, retry_status, type }`

          A model request failed for a reason other than overload or rate-limiting.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object { type }`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

              - `type: "retrying"`

                - `"retrying"`

            - `beta_managed_agents_retry_status_exhausted: object { type }`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

              - `type: "exhausted"`

                - `"exhausted"`

            - `beta_managed_agents_retry_status_terminal: object { type }`

              The session encountered a terminal error and will transition to `terminated` state.

              - `type: "terminal"`

                - `"terminal"`

          - `type: "model_request_failed_error"`

            - `"model_request_failed_error"`

        - `beta_managed_agents_mcp_connection_failed_error: object { mcp_server_name, message, retry_status, type }`

          Failed to connect to an MCP server.

          - `mcp_server_name: string`

            Name of the MCP server that failed to connect.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object { type }`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

              - `type: "retrying"`

                - `"retrying"`

            - `beta_managed_agents_retry_status_exhausted: object { type }`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

              - `type: "exhausted"`

                - `"exhausted"`

            - `beta_managed_agents_retry_status_terminal: object { type }`

              The session encountered a terminal error and will transition to `terminated` state.

              - `type: "terminal"`

                - `"terminal"`

          - `type: "mcp_connection_failed_error"`

            - `"mcp_connection_failed_error"`

        - `beta_managed_agents_mcp_authentication_failed_error: object { mcp_server_name, message, retry_status, type }`

          Authentication to an MCP server failed.

          - `mcp_server_name: string`

            Name of the MCP server that failed authentication.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object { type }`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

              - `type: "retrying"`

                - `"retrying"`

            - `beta_managed_agents_retry_status_exhausted: object { type }`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

              - `type: "exhausted"`

                - `"exhausted"`

            - `beta_managed_agents_retry_status_terminal: object { type }`

              The session encountered a terminal error and will transition to `terminated` state.

              - `type: "terminal"`

                - `"terminal"`

          - `type: "mcp_authentication_failed_error"`

            - `"mcp_authentication_failed_error"`

        - `beta_managed_agents_billing_error: object { message, retry_status, type }`

          The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object { type }`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

              - `type: "retrying"`

                - `"retrying"`

            - `beta_managed_agents_retry_status_exhausted: object { type }`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

              - `type: "exhausted"`

                - `"exhausted"`

            - `beta_managed_agents_retry_status_terminal: object { type }`

              The session encountered a terminal error and will transition to `terminated` state.

              - `type: "terminal"`

                - `"terminal"`

          - `type: "billing_error"`

            - `"billing_error"`

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "session.error"`

        - `"session.error"`

    - `beta_managed_agents_session_status_rescheduled_event: object { id, processed_at, type }`

      Indicates the session is recovering from an error state and is rescheduled for execution.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "session.status_rescheduled"`

        - `"session.status_rescheduled"`

    - `beta_managed_agents_session_status_running_event: object { id, processed_at, type }`

      Indicates the session is actively running and the agent is working.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "session.status_running"`

        - `"session.status_running"`

    - `beta_managed_agents_session_status_idle_event: object { id, processed_at, stop_reason, type }`

      Indicates the agent has paused and is awaiting user input.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted`

        The agent completed its turn naturally and is ready for the next user message.

        - `beta_managed_agents_session_end_turn: object { type }`

          The agent completed its turn naturally and is ready for the next user message.

          - `type: "end_turn"`

            - `"end_turn"`

        - `beta_managed_agents_session_requires_action: object { event_ids, type }`

          The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

          - `event_ids: array of string`

            The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

          - `type: "requires_action"`

            - `"requires_action"`

        - `beta_managed_agents_session_retries_exhausted: object { type }`

          The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

          - `type: "retries_exhausted"`

            - `"retries_exhausted"`

      - `type: "session.status_idle"`

        - `"session.status_idle"`

    - `beta_managed_agents_session_status_terminated_event: object { id, processed_at, type }`

      Indicates the session has terminated, either due to an error or completion.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "session.status_terminated"`

        - `"session.status_terminated"`

    - `beta_managed_agents_span_model_request_start_event: object { id, processed_at, type }`

      Emitted when a model request is initiated by the agent.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "span.model_request_start"`

        - `"span.model_request_start"`

    - `beta_managed_agents_span_model_request_end_event: object { id, is_error, model_request_start_id, 3 more }`

      Emitted when a model request completes.

      - `id: string`

        Unique identifier for this event.

      - `is_error: boolean`

        Whether the model request resulted in an error.

      - `model_request_start_id: string`

        The id of the corresponding `span.model_request_start` event.

      - `model_usage: object { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 2 more }`

        Token usage for a single model request.

        - `cache_creation_input_tokens: number`

          Tokens used to create prompt cache in this request.

        - `cache_read_input_tokens: number`

          Tokens read from prompt cache in this request.

        - `input_tokens: number`

          Input tokens consumed by this request.

        - `output_tokens: number`

          Output tokens generated by this request.

        - `speed: optional "standard" or "fast"`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "span.model_request_end"`

        - `"span.model_request_end"`

    - `beta_managed_agents_session_deleted_event: object { id, processed_at, type }`

      Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "session.deleted"`

        - `"session.deleted"`

  - `next_page: optional string`

    Opaque cursor for the next page. Null when no more results.

### Example

```cli
ant beta:sessions:events list \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7
```

## Send

`$ ant beta:sessions:events send`

**post** `/v1/sessions/{session_id}/events`

Send Events

### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--event: array of BetaManagedAgentsEventParams`

  Body param: Events to send to the `session`.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_send_session_events: object { data }`

  Events that were successfully sent to the session.

  - `data: optional array of BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or BetaManagedAgentsUserCustomToolResultEvent`

    Sent events

    - `beta_managed_agents_user_message_event: object { id, content, type, processed_at }`

      A user message event in the session conversation.

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        Array of content blocks comprising the user message.

        - `beta_managed_agents_text_block: object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `beta_managed_agents_image_block: object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_url_image_source: object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `beta_managed_agents_file_image_source: object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `beta_managed_agents_document_block: object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `beta_managed_agents_url_document_source: object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `beta_managed_agents_file_document_source: object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

    - `beta_managed_agents_user_interrupt_event: object { id, type, processed_at }`

      An interrupt event that pauses agent execution and returns control to the user.

      - `id: string`

        Unique identifier for this event.

      - `type: "user.interrupt"`

        - `"user.interrupt"`

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

    - `beta_managed_agents_user_tool_confirmation_event: object { id, result, tool_use_id, 3 more }`

      A tool confirmation event that approves or denies a pending tool execution.

      - `id: string`

        Unique identifier for this event.

      - `result: "allow" or "deny"`

        UserToolConfirmationResult enum

        - `"allow"`

        - `"deny"`

      - `tool_use_id: string`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: "user.tool_confirmation"`

        - `"user.tool_confirmation"`

      - `deny_message: optional string`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

    - `beta_managed_agents_user_custom_tool_result_event: object { id, custom_tool_use_id, type, 3 more }`

      Event sent by the client providing the result of a custom tool execution.

      - `id: string`

        Unique identifier for this event.

      - `custom_tool_use_id: string`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: "user.custom_tool_result"`

        - `"user.custom_tool_result"`

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        The result content returned by the tool.

        - `beta_managed_agents_text_block: object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `beta_managed_agents_image_block: object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_url_image_source: object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `beta_managed_agents_file_image_source: object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `beta_managed_agents_document_block: object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `beta_managed_agents_url_document_source: object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `beta_managed_agents_file_document_source: object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `is_error: optional boolean`

        Whether the tool execution resulted in an error.

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

### Example

```cli
ant beta:sessions:events send \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --event "{content: [{text: 'Where is my order #1234?', type: text}], type: user.message}"
```

## Stream

`$ ant beta:sessions:events stream`

**get** `/v1/sessions/{session_id}/events/stream`

Stream Events

### Parameters

- `--session-id: string`

  Path parameter session_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_stream_session_events: BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or 17 more`

  Server-sent event in the session stream.

  - `beta_managed_agents_user_message_event: object { id, content, type, processed_at }`

    A user message event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      Array of content blocks comprising the user message.

      - `beta_managed_agents_text_block: object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `beta_managed_agents_image_block: object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_url_image_source: object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `beta_managed_agents_file_image_source: object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `beta_managed_agents_document_block: object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `beta_managed_agents_url_document_source: object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `beta_managed_agents_file_document_source: object { file_id, type }`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

    - `type: "user.message"`

      - `"user.message"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

  - `beta_managed_agents_user_interrupt_event: object { id, type, processed_at }`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: string`

      Unique identifier for this event.

    - `type: "user.interrupt"`

      - `"user.interrupt"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

  - `beta_managed_agents_user_tool_confirmation_event: object { id, result, tool_use_id, 3 more }`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: string`

      Unique identifier for this event.

    - `result: "allow" or "deny"`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_confirmation"`

      - `"user.tool_confirmation"`

    - `deny_message: optional string`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

  - `beta_managed_agents_user_custom_tool_result_event: object { id, custom_tool_use_id, type, 3 more }`

    Event sent by the client providing the result of a custom tool execution.

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.custom_tool_result"`

      - `"user.custom_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `beta_managed_agents_image_block: object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_url_image_source: object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `beta_managed_agents_file_image_source: object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `beta_managed_agents_document_block: object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `beta_managed_agents_url_document_source: object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `beta_managed_agents_file_document_source: object { file_id, type }`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

  - `beta_managed_agents_agent_custom_tool_use_event: object { id, input, name, 2 more }`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the custom tool being called.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.custom_tool_use"`

      - `"agent.custom_tool_use"`

  - `beta_managed_agents_agent_message_event: object { id, content, processed_at, type }`

    An agent response event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock`

      Array of text blocks comprising the agent response.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.message"`

      - `"agent.message"`

  - `beta_managed_agents_agent_thinking_event: object { id, processed_at, type }`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.thinking"`

      - `"agent.thinking"`

  - `beta_managed_agents_agent_mcp_tool_use_event: object { id, input, mcp_server_name, 4 more }`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `mcp_server_name: string`

      Name of the MCP server providing the tool.

    - `name: string`

      Name of the MCP tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.mcp_tool_use"`

      - `"agent.mcp_tool_use"`

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

  - `beta_managed_agents_agent_mcp_tool_result_event: object { id, mcp_tool_use_id, processed_at, 3 more }`

    Event representing the result of an MCP tool execution.

    - `id: string`

      Unique identifier for this event.

    - `mcp_tool_use_id: string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.mcp_tool_result"`

      - `"agent.mcp_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `beta_managed_agents_image_block: object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_url_image_source: object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `beta_managed_agents_file_image_source: object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `beta_managed_agents_document_block: object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `beta_managed_agents_url_document_source: object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `beta_managed_agents_file_document_source: object { file_id, type }`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

  - `beta_managed_agents_agent_tool_use_event: object { id, input, name, 3 more }`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the agent tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.tool_use"`

      - `"agent.tool_use"`

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

  - `beta_managed_agents_agent_tool_result_event: object { id, processed_at, tool_use_id, 3 more }`

    Event representing the result of an agent tool execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: "agent.tool_result"`

      - `"agent.tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `beta_managed_agents_image_block: object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_url_image_source: object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `beta_managed_agents_file_image_source: object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `beta_managed_agents_document_block: object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `beta_managed_agents_url_document_source: object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `beta_managed_agents_file_document_source: object { file_id, type }`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

  - `beta_managed_agents_agent_thread_context_compacted_event: object { id, processed_at, type }`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.thread_context_compacted"`

      - `"agent.thread_context_compacted"`

  - `beta_managed_agents_session_error_event: object { id, error, processed_at, type }`

    An error event indicating a problem occurred during session execution.

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 4 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `beta_managed_agents_unknown_error: object { message, retry_status, type }`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `beta_managed_agents_retry_status_exhausted: object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `beta_managed_agents_retry_status_terminal: object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "unknown_error"`

          - `"unknown_error"`

      - `beta_managed_agents_model_overloaded_error: object { message, retry_status, type }`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `beta_managed_agents_retry_status_exhausted: object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `beta_managed_agents_retry_status_terminal: object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "model_overloaded_error"`

          - `"model_overloaded_error"`

      - `beta_managed_agents_model_rate_limited_error: object { message, retry_status, type }`

        The model request was rate-limited.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `beta_managed_agents_retry_status_exhausted: object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `beta_managed_agents_retry_status_terminal: object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "model_rate_limited_error"`

          - `"model_rate_limited_error"`

      - `beta_managed_agents_model_request_failed_error: object { message, retry_status, type }`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `beta_managed_agents_retry_status_exhausted: object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `beta_managed_agents_retry_status_terminal: object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "model_request_failed_error"`

          - `"model_request_failed_error"`

      - `beta_managed_agents_mcp_connection_failed_error: object { mcp_server_name, message, retry_status, type }`

        Failed to connect to an MCP server.

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `beta_managed_agents_retry_status_exhausted: object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `beta_managed_agents_retry_status_terminal: object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "mcp_connection_failed_error"`

          - `"mcp_connection_failed_error"`

      - `beta_managed_agents_mcp_authentication_failed_error: object { mcp_server_name, message, retry_status, type }`

        Authentication to an MCP server failed.

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `beta_managed_agents_retry_status_exhausted: object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `beta_managed_agents_retry_status_terminal: object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "mcp_authentication_failed_error"`

          - `"mcp_authentication_failed_error"`

      - `beta_managed_agents_billing_error: object { message, retry_status, type }`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `beta_managed_agents_retry_status_exhausted: object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `beta_managed_agents_retry_status_terminal: object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "billing_error"`

          - `"billing_error"`

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.error"`

      - `"session.error"`

  - `beta_managed_agents_session_status_rescheduled_event: object { id, processed_at, type }`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_rescheduled"`

      - `"session.status_rescheduled"`

  - `beta_managed_agents_session_status_running_event: object { id, processed_at, type }`

    Indicates the session is actively running and the agent is working.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_running"`

      - `"session.status_running"`

  - `beta_managed_agents_session_status_idle_event: object { id, processed_at, stop_reason, type }`

    Indicates the agent has paused and is awaiting user input.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted`

      The agent completed its turn naturally and is ready for the next user message.

      - `beta_managed_agents_session_end_turn: object { type }`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

          - `"end_turn"`

      - `beta_managed_agents_session_requires_action: object { event_ids, type }`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: array of string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: "requires_action"`

          - `"requires_action"`

      - `beta_managed_agents_session_retries_exhausted: object { type }`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `type: "retries_exhausted"`

          - `"retries_exhausted"`

    - `type: "session.status_idle"`

      - `"session.status_idle"`

  - `beta_managed_agents_session_status_terminated_event: object { id, processed_at, type }`

    Indicates the session has terminated, either due to an error or completion.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_terminated"`

      - `"session.status_terminated"`

  - `beta_managed_agents_span_model_request_start_event: object { id, processed_at, type }`

    Emitted when a model request is initiated by the agent.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "span.model_request_start"`

      - `"span.model_request_start"`

  - `beta_managed_agents_span_model_request_end_event: object { id, is_error, model_request_start_id, 3 more }`

    Emitted when a model request completes.

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: object { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 2 more }`

      Token usage for a single model request.

      - `cache_creation_input_tokens: number`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: number`

        Tokens read from prompt cache in this request.

      - `input_tokens: number`

        Input tokens consumed by this request.

      - `output_tokens: number`

        Output tokens generated by this request.

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "span.model_request_end"`

      - `"span.model_request_end"`

  - `beta_managed_agents_session_deleted_event: object { id, processed_at, type }`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.deleted"`

      - `"session.deleted"`

### Example

```cli
ant beta:sessions:events stream \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7
```

## Domain Types

### Beta Managed Agents Agent Custom Tool Use Event

- `beta_managed_agents_agent_custom_tool_use_event: object { id, input, name, 2 more }`

  Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

  - `id: string`

    Unique identifier for this event.

  - `input: map[unknown]`

    Input parameters for the tool call.

  - `name: string`

    Name of the custom tool being called.

  - `processed_at: string`

    A timestamp in RFC 3339 format

  - `type: "agent.custom_tool_use"`

    - `"agent.custom_tool_use"`

### Beta Managed Agents Agent MCP Tool Result Event

- `beta_managed_agents_agent_mcp_tool_result_event: object { id, mcp_tool_use_id, processed_at, 3 more }`

  Event representing the result of an MCP tool execution.

  - `id: string`

    Unique identifier for this event.

  - `mcp_tool_use_id: string`

    The id of the `agent.mcp_tool_use` event this result corresponds to.

  - `processed_at: string`

    A timestamp in RFC 3339 format

  - `type: "agent.mcp_tool_result"`

    - `"agent.mcp_tool_result"`

  - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

    The result content returned by the tool.

    - `beta_managed_agents_text_block: object { text, type }`

      Regular text content.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `beta_managed_agents_image_block: object { source, type }`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: "base64"`

            - `"base64"`

        - `beta_managed_agents_url_image_source: object { type, url }`

          Image referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the image to fetch.

        - `beta_managed_agents_file_image_source: object { file_id, type }`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "image"`

        - `"image"`

    - `beta_managed_agents_document_block: object { source, type, context, title }`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

          - `type: "base64"`

            - `"base64"`

        - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

          Plain text document content.

          - `data: string`

            The plain text content.

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: "text"`

            - `"text"`

        - `beta_managed_agents_url_document_source: object { type, url }`

          Document referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the document to fetch.

        - `beta_managed_agents_file_document_source: object { file_id, type }`

          Document referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "document"`

        - `"document"`

      - `context: optional string`

        Additional context about the document for the model.

      - `title: optional string`

        The title of the document.

  - `is_error: optional boolean`

    Whether the tool execution resulted in an error.

### Beta Managed Agents Agent MCP Tool Use Event

- `beta_managed_agents_agent_mcp_tool_use_event: object { id, input, mcp_server_name, 4 more }`

  Event emitted when the agent invokes a tool provided by an MCP server.

  - `id: string`

    Unique identifier for this event.

  - `input: map[unknown]`

    Input parameters for the tool call.

  - `mcp_server_name: string`

    Name of the MCP server providing the tool.

  - `name: string`

    Name of the MCP tool being used.

  - `processed_at: string`

    A timestamp in RFC 3339 format

  - `type: "agent.mcp_tool_use"`

    - `"agent.mcp_tool_use"`

  - `evaluated_permission: optional "allow" or "ask" or "deny"`

    AgentEvaluatedPermission enum

    - `"allow"`

    - `"ask"`

    - `"deny"`

### Beta Managed Agents Agent Message Event

- `beta_managed_agents_agent_message_event: object { id, content, processed_at, type }`

  An agent response event in the session conversation.

  - `id: string`

    Unique identifier for this event.

  - `content: array of BetaManagedAgentsTextBlock`

    Array of text blocks comprising the agent response.

    - `text: string`

      The text content.

    - `type: "text"`

      - `"text"`

  - `processed_at: string`

    A timestamp in RFC 3339 format

  - `type: "agent.message"`

    - `"agent.message"`

### Beta Managed Agents Agent Thinking Event

- `beta_managed_agents_agent_thinking_event: object { id, processed_at, type }`

  Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

  - `type: "agent.thinking"`

    - `"agent.thinking"`

### Beta Managed Agents Agent Thread Context Compacted Event

- `beta_managed_agents_agent_thread_context_compacted_event: object { id, processed_at, type }`

  Indicates that context compaction (summarization) occurred during the session.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

  - `type: "agent.thread_context_compacted"`

    - `"agent.thread_context_compacted"`

### Beta Managed Agents Agent Tool Result Event

- `beta_managed_agents_agent_tool_result_event: object { id, processed_at, tool_use_id, 3 more }`

  Event representing the result of an agent tool execution.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

  - `tool_use_id: string`

    The id of the `agent.tool_use` event this result corresponds to.

  - `type: "agent.tool_result"`

    - `"agent.tool_result"`

  - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

    The result content returned by the tool.

    - `beta_managed_agents_text_block: object { text, type }`

      Regular text content.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `beta_managed_agents_image_block: object { source, type }`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: "base64"`

            - `"base64"`

        - `beta_managed_agents_url_image_source: object { type, url }`

          Image referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the image to fetch.

        - `beta_managed_agents_file_image_source: object { file_id, type }`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "image"`

        - `"image"`

    - `beta_managed_agents_document_block: object { source, type, context, title }`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

          - `type: "base64"`

            - `"base64"`

        - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

          Plain text document content.

          - `data: string`

            The plain text content.

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: "text"`

            - `"text"`

        - `beta_managed_agents_url_document_source: object { type, url }`

          Document referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the document to fetch.

        - `beta_managed_agents_file_document_source: object { file_id, type }`

          Document referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "document"`

        - `"document"`

      - `context: optional string`

        Additional context about the document for the model.

      - `title: optional string`

        The title of the document.

  - `is_error: optional boolean`

    Whether the tool execution resulted in an error.

### Beta Managed Agents Agent Tool Use Event

- `beta_managed_agents_agent_tool_use_event: object { id, input, name, 3 more }`

  Event emitted when the agent invokes a built-in agent tool.

  - `id: string`

    Unique identifier for this event.

  - `input: map[unknown]`

    Input parameters for the tool call.

  - `name: string`

    Name of the agent tool being used.

  - `processed_at: string`

    A timestamp in RFC 3339 format

  - `type: "agent.tool_use"`

    - `"agent.tool_use"`

  - `evaluated_permission: optional "allow" or "ask" or "deny"`

    AgentEvaluatedPermission enum

    - `"allow"`

    - `"ask"`

    - `"deny"`

### Beta Managed Agents Base64 Document Source

- `beta_managed_agents_base64_document_source: object { data, media_type, type }`

  Base64-encoded document data.

  - `data: string`

    Base64-encoded document data.

  - `media_type: string`

    MIME type of the document (e.g., "application/pdf").

  - `type: "base64"`

    - `"base64"`

### Beta Managed Agents Base64 Image Source

- `beta_managed_agents_base64_image_source: object { data, media_type, type }`

  Base64-encoded image data.

  - `data: string`

    Base64-encoded image data.

  - `media_type: string`

    MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

  - `type: "base64"`

    - `"base64"`

### Beta Managed Agents Billing Error

- `beta_managed_agents_billing_error: object { message, retry_status, type }`

  The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `beta_managed_agents_retry_status_retrying: object { type }`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

        - `"retrying"`

    - `beta_managed_agents_retry_status_exhausted: object { type }`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

        - `"exhausted"`

    - `beta_managed_agents_retry_status_terminal: object { type }`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

        - `"terminal"`

  - `type: "billing_error"`

    - `"billing_error"`

### Beta Managed Agents Document Block

- `beta_managed_agents_document_block: object { source, type, context, title }`

  Document content, either specified directly as base64 data, as text, or as a reference via a URL.

  - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

    Union type for document source variants.

    - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

      Base64-encoded document data.

      - `data: string`

        Base64-encoded document data.

      - `media_type: string`

        MIME type of the document (e.g., "application/pdf").

      - `type: "base64"`

        - `"base64"`

    - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

      Plain text document content.

      - `data: string`

        The plain text content.

      - `media_type: "text/plain"`

        MIME type of the text content. Must be "text/plain".

        - `"text/plain"`

      - `type: "text"`

        - `"text"`

    - `beta_managed_agents_url_document_source: object { type, url }`

      Document referenced by URL.

      - `type: "url"`

        - `"url"`

      - `url: string`

        URL of the document to fetch.

    - `beta_managed_agents_file_document_source: object { file_id, type }`

      Document referenced by file ID.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

  - `type: "document"`

    - `"document"`

  - `context: optional string`

    Additional context about the document for the model.

  - `title: optional string`

    The title of the document.

### Beta Managed Agents Event Params

- `beta_managed_agents_event_params: BetaManagedAgentsUserMessageEventParams or BetaManagedAgentsUserInterruptEventParams or BetaManagedAgentsUserToolConfirmationEventParams or BetaManagedAgentsUserCustomToolResultEventParams`

  Union type for event parameters that can be sent to a session.

  - `beta_managed_agents_user_message_event_params: object { content, type }`

    Parameters for sending a user message to the session.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      Array of content blocks for the user message.

      - `beta_managed_agents_text_block: object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `beta_managed_agents_image_block: object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_url_image_source: object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `beta_managed_agents_file_image_source: object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `beta_managed_agents_document_block: object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `beta_managed_agents_url_document_source: object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `beta_managed_agents_file_document_source: object { file_id, type }`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

    - `type: "user.message"`

      - `"user.message"`

  - `beta_managed_agents_user_interrupt_event_params: object { type }`

    Parameters for sending an interrupt to pause the agent.

    - `type: "user.interrupt"`

      - `"user.interrupt"`

  - `beta_managed_agents_user_tool_confirmation_event_params: object { result, tool_use_id, type, deny_message }`

    Parameters for confirming or denying a tool execution request.

    - `result: "allow" or "deny"`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_confirmation"`

      - `"user.tool_confirmation"`

    - `deny_message: optional string`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

  - `beta_managed_agents_user_custom_tool_result_event_params: object { custom_tool_use_id, type, content, is_error }`

    Parameters for providing the result of a custom tool execution.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.custom_tool_result"`

      - `"user.custom_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `beta_managed_agents_image_block: object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_url_image_source: object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `beta_managed_agents_file_image_source: object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `beta_managed_agents_document_block: object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `beta_managed_agents_url_document_source: object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `beta_managed_agents_file_document_source: object { file_id, type }`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

### Beta Managed Agents File Document Source

- `beta_managed_agents_file_document_source: object { file_id, type }`

  Document referenced by file ID.

  - `file_id: string`

    ID of a previously uploaded file.

  - `type: "file"`

    - `"file"`

### Beta Managed Agents File Image Source

- `beta_managed_agents_file_image_source: object { file_id, type }`

  Image referenced by file ID.

  - `file_id: string`

    ID of a previously uploaded file.

  - `type: "file"`

    - `"file"`

### Beta Managed Agents Image Block

- `beta_managed_agents_image_block: object { source, type }`

  Image content specified directly as base64 data or as a reference via a URL.

  - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

    Union type for image source variants.

    - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

      Base64-encoded image data.

      - `data: string`

        Base64-encoded image data.

      - `media_type: string`

        MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

      - `type: "base64"`

        - `"base64"`

    - `beta_managed_agents_url_image_source: object { type, url }`

      Image referenced by URL.

      - `type: "url"`

        - `"url"`

      - `url: string`

        URL of the image to fetch.

    - `beta_managed_agents_file_image_source: object { file_id, type }`

      Image referenced by file ID.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

  - `type: "image"`

    - `"image"`

### Beta Managed Agents MCP Authentication Failed Error

- `beta_managed_agents_mcp_authentication_failed_error: object { mcp_server_name, message, retry_status, type }`

  Authentication to an MCP server failed.

  - `mcp_server_name: string`

    Name of the MCP server that failed authentication.

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `beta_managed_agents_retry_status_retrying: object { type }`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

        - `"retrying"`

    - `beta_managed_agents_retry_status_exhausted: object { type }`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

        - `"exhausted"`

    - `beta_managed_agents_retry_status_terminal: object { type }`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

        - `"terminal"`

  - `type: "mcp_authentication_failed_error"`

    - `"mcp_authentication_failed_error"`

### Beta Managed Agents MCP Connection Failed Error

- `beta_managed_agents_mcp_connection_failed_error: object { mcp_server_name, message, retry_status, type }`

  Failed to connect to an MCP server.

  - `mcp_server_name: string`

    Name of the MCP server that failed to connect.

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `beta_managed_agents_retry_status_retrying: object { type }`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

        - `"retrying"`

    - `beta_managed_agents_retry_status_exhausted: object { type }`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

        - `"exhausted"`

    - `beta_managed_agents_retry_status_terminal: object { type }`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

        - `"terminal"`

  - `type: "mcp_connection_failed_error"`

    - `"mcp_connection_failed_error"`

### Beta Managed Agents Model Overloaded Error

- `beta_managed_agents_model_overloaded_error: object { message, retry_status, type }`

  The model is currently overloaded. Emitted after automatic retries are exhausted.

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `beta_managed_agents_retry_status_retrying: object { type }`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

        - `"retrying"`

    - `beta_managed_agents_retry_status_exhausted: object { type }`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

        - `"exhausted"`

    - `beta_managed_agents_retry_status_terminal: object { type }`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

        - `"terminal"`

  - `type: "model_overloaded_error"`

    - `"model_overloaded_error"`

### Beta Managed Agents Model Rate Limited Error

- `beta_managed_agents_model_rate_limited_error: object { message, retry_status, type }`

  The model request was rate-limited.

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `beta_managed_agents_retry_status_retrying: object { type }`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

        - `"retrying"`

    - `beta_managed_agents_retry_status_exhausted: object { type }`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

        - `"exhausted"`

    - `beta_managed_agents_retry_status_terminal: object { type }`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

        - `"terminal"`

  - `type: "model_rate_limited_error"`

    - `"model_rate_limited_error"`

### Beta Managed Agents Model Request Failed Error

- `beta_managed_agents_model_request_failed_error: object { message, retry_status, type }`

  A model request failed for a reason other than overload or rate-limiting.

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `beta_managed_agents_retry_status_retrying: object { type }`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

        - `"retrying"`

    - `beta_managed_agents_retry_status_exhausted: object { type }`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

        - `"exhausted"`

    - `beta_managed_agents_retry_status_terminal: object { type }`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

        - `"terminal"`

  - `type: "model_request_failed_error"`

    - `"model_request_failed_error"`

### Beta Managed Agents Plain Text Document Source

- `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

  Plain text document content.

  - `data: string`

    The plain text content.

  - `media_type: "text/plain"`

    MIME type of the text content. Must be "text/plain".

    - `"text/plain"`

  - `type: "text"`

    - `"text"`

### Beta Managed Agents Retry Status Exhausted

- `beta_managed_agents_retry_status_exhausted: object { type }`

  This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

  - `type: "exhausted"`

    - `"exhausted"`

### Beta Managed Agents Retry Status Retrying

- `beta_managed_agents_retry_status_retrying: object { type }`

  The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

  - `type: "retrying"`

    - `"retrying"`

### Beta Managed Agents Retry Status Terminal

- `beta_managed_agents_retry_status_terminal: object { type }`

  The session encountered a terminal error and will transition to `terminated` state.

  - `type: "terminal"`

    - `"terminal"`

### Beta Managed Agents Send Session Events

- `beta_managed_agents_send_session_events: object { data }`

  Events that were successfully sent to the session.

  - `data: optional array of BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or BetaManagedAgentsUserCustomToolResultEvent`

    Sent events

    - `beta_managed_agents_user_message_event: object { id, content, type, processed_at }`

      A user message event in the session conversation.

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        Array of content blocks comprising the user message.

        - `beta_managed_agents_text_block: object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `beta_managed_agents_image_block: object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_url_image_source: object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `beta_managed_agents_file_image_source: object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `beta_managed_agents_document_block: object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `beta_managed_agents_url_document_source: object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `beta_managed_agents_file_document_source: object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

    - `beta_managed_agents_user_interrupt_event: object { id, type, processed_at }`

      An interrupt event that pauses agent execution and returns control to the user.

      - `id: string`

        Unique identifier for this event.

      - `type: "user.interrupt"`

        - `"user.interrupt"`

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

    - `beta_managed_agents_user_tool_confirmation_event: object { id, result, tool_use_id, 3 more }`

      A tool confirmation event that approves or denies a pending tool execution.

      - `id: string`

        Unique identifier for this event.

      - `result: "allow" or "deny"`

        UserToolConfirmationResult enum

        - `"allow"`

        - `"deny"`

      - `tool_use_id: string`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: "user.tool_confirmation"`

        - `"user.tool_confirmation"`

      - `deny_message: optional string`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

    - `beta_managed_agents_user_custom_tool_result_event: object { id, custom_tool_use_id, type, 3 more }`

      Event sent by the client providing the result of a custom tool execution.

      - `id: string`

        Unique identifier for this event.

      - `custom_tool_use_id: string`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: "user.custom_tool_result"`

        - `"user.custom_tool_result"`

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        The result content returned by the tool.

        - `beta_managed_agents_text_block: object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `beta_managed_agents_image_block: object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_url_image_source: object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `beta_managed_agents_file_image_source: object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `beta_managed_agents_document_block: object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `beta_managed_agents_url_document_source: object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `beta_managed_agents_file_document_source: object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `is_error: optional boolean`

        Whether the tool execution resulted in an error.

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

### Beta Managed Agents Session Deleted Event

- `beta_managed_agents_session_deleted_event: object { id, processed_at, type }`

  Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

  - `type: "session.deleted"`

    - `"session.deleted"`

### Beta Managed Agents Session End Turn

- `beta_managed_agents_session_end_turn: object { type }`

  The agent completed its turn naturally and is ready for the next user message.

  - `type: "end_turn"`

    - `"end_turn"`

### Beta Managed Agents Session Error Event

- `beta_managed_agents_session_error_event: object { id, error, processed_at, type }`

  An error event indicating a problem occurred during session execution.

  - `id: string`

    Unique identifier for this event.

  - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 4 more`

    An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

    - `beta_managed_agents_unknown_error: object { message, retry_status, type }`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `beta_managed_agents_retry_status_retrying: object { type }`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: "retrying"`

            - `"retrying"`

        - `beta_managed_agents_retry_status_exhausted: object { type }`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: "exhausted"`

            - `"exhausted"`

        - `beta_managed_agents_retry_status_terminal: object { type }`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: "terminal"`

            - `"terminal"`

      - `type: "unknown_error"`

        - `"unknown_error"`

    - `beta_managed_agents_model_overloaded_error: object { message, retry_status, type }`

      The model is currently overloaded. Emitted after automatic retries are exhausted.

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `beta_managed_agents_retry_status_retrying: object { type }`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: "retrying"`

            - `"retrying"`

        - `beta_managed_agents_retry_status_exhausted: object { type }`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: "exhausted"`

            - `"exhausted"`

        - `beta_managed_agents_retry_status_terminal: object { type }`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: "terminal"`

            - `"terminal"`

      - `type: "model_overloaded_error"`

        - `"model_overloaded_error"`

    - `beta_managed_agents_model_rate_limited_error: object { message, retry_status, type }`

      The model request was rate-limited.

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `beta_managed_agents_retry_status_retrying: object { type }`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: "retrying"`

            - `"retrying"`

        - `beta_managed_agents_retry_status_exhausted: object { type }`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: "exhausted"`

            - `"exhausted"`

        - `beta_managed_agents_retry_status_terminal: object { type }`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: "terminal"`

            - `"terminal"`

      - `type: "model_rate_limited_error"`

        - `"model_rate_limited_error"`

    - `beta_managed_agents_model_request_failed_error: object { message, retry_status, type }`

      A model request failed for a reason other than overload or rate-limiting.

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `beta_managed_agents_retry_status_retrying: object { type }`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: "retrying"`

            - `"retrying"`

        - `beta_managed_agents_retry_status_exhausted: object { type }`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: "exhausted"`

            - `"exhausted"`

        - `beta_managed_agents_retry_status_terminal: object { type }`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: "terminal"`

            - `"terminal"`

      - `type: "model_request_failed_error"`

        - `"model_request_failed_error"`

    - `beta_managed_agents_mcp_connection_failed_error: object { mcp_server_name, message, retry_status, type }`

      Failed to connect to an MCP server.

      - `mcp_server_name: string`

        Name of the MCP server that failed to connect.

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `beta_managed_agents_retry_status_retrying: object { type }`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: "retrying"`

            - `"retrying"`

        - `beta_managed_agents_retry_status_exhausted: object { type }`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: "exhausted"`

            - `"exhausted"`

        - `beta_managed_agents_retry_status_terminal: object { type }`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: "terminal"`

            - `"terminal"`

      - `type: "mcp_connection_failed_error"`

        - `"mcp_connection_failed_error"`

    - `beta_managed_agents_mcp_authentication_failed_error: object { mcp_server_name, message, retry_status, type }`

      Authentication to an MCP server failed.

      - `mcp_server_name: string`

        Name of the MCP server that failed authentication.

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `beta_managed_agents_retry_status_retrying: object { type }`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: "retrying"`

            - `"retrying"`

        - `beta_managed_agents_retry_status_exhausted: object { type }`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: "exhausted"`

            - `"exhausted"`

        - `beta_managed_agents_retry_status_terminal: object { type }`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: "terminal"`

            - `"terminal"`

      - `type: "mcp_authentication_failed_error"`

        - `"mcp_authentication_failed_error"`

    - `beta_managed_agents_billing_error: object { message, retry_status, type }`

      The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `beta_managed_agents_retry_status_retrying: object { type }`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: "retrying"`

            - `"retrying"`

        - `beta_managed_agents_retry_status_exhausted: object { type }`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: "exhausted"`

            - `"exhausted"`

        - `beta_managed_agents_retry_status_terminal: object { type }`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: "terminal"`

            - `"terminal"`

      - `type: "billing_error"`

        - `"billing_error"`

  - `processed_at: string`

    A timestamp in RFC 3339 format

  - `type: "session.error"`

    - `"session.error"`

### Beta Managed Agents Session Event

- `beta_managed_agents_session_event: BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or 17 more`

  Union type for all event types in a session.

  - `beta_managed_agents_user_message_event: object { id, content, type, processed_at }`

    A user message event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      Array of content blocks comprising the user message.

      - `beta_managed_agents_text_block: object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `beta_managed_agents_image_block: object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_url_image_source: object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `beta_managed_agents_file_image_source: object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `beta_managed_agents_document_block: object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `beta_managed_agents_url_document_source: object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `beta_managed_agents_file_document_source: object { file_id, type }`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

    - `type: "user.message"`

      - `"user.message"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

  - `beta_managed_agents_user_interrupt_event: object { id, type, processed_at }`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: string`

      Unique identifier for this event.

    - `type: "user.interrupt"`

      - `"user.interrupt"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

  - `beta_managed_agents_user_tool_confirmation_event: object { id, result, tool_use_id, 3 more }`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: string`

      Unique identifier for this event.

    - `result: "allow" or "deny"`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_confirmation"`

      - `"user.tool_confirmation"`

    - `deny_message: optional string`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

  - `beta_managed_agents_user_custom_tool_result_event: object { id, custom_tool_use_id, type, 3 more }`

    Event sent by the client providing the result of a custom tool execution.

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.custom_tool_result"`

      - `"user.custom_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `beta_managed_agents_image_block: object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_url_image_source: object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `beta_managed_agents_file_image_source: object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `beta_managed_agents_document_block: object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `beta_managed_agents_url_document_source: object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `beta_managed_agents_file_document_source: object { file_id, type }`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

  - `beta_managed_agents_agent_custom_tool_use_event: object { id, input, name, 2 more }`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the custom tool being called.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.custom_tool_use"`

      - `"agent.custom_tool_use"`

  - `beta_managed_agents_agent_message_event: object { id, content, processed_at, type }`

    An agent response event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock`

      Array of text blocks comprising the agent response.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.message"`

      - `"agent.message"`

  - `beta_managed_agents_agent_thinking_event: object { id, processed_at, type }`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.thinking"`

      - `"agent.thinking"`

  - `beta_managed_agents_agent_mcp_tool_use_event: object { id, input, mcp_server_name, 4 more }`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `mcp_server_name: string`

      Name of the MCP server providing the tool.

    - `name: string`

      Name of the MCP tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.mcp_tool_use"`

      - `"agent.mcp_tool_use"`

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

  - `beta_managed_agents_agent_mcp_tool_result_event: object { id, mcp_tool_use_id, processed_at, 3 more }`

    Event representing the result of an MCP tool execution.

    - `id: string`

      Unique identifier for this event.

    - `mcp_tool_use_id: string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.mcp_tool_result"`

      - `"agent.mcp_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `beta_managed_agents_image_block: object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_url_image_source: object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `beta_managed_agents_file_image_source: object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `beta_managed_agents_document_block: object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `beta_managed_agents_url_document_source: object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `beta_managed_agents_file_document_source: object { file_id, type }`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

  - `beta_managed_agents_agent_tool_use_event: object { id, input, name, 3 more }`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the agent tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.tool_use"`

      - `"agent.tool_use"`

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

  - `beta_managed_agents_agent_tool_result_event: object { id, processed_at, tool_use_id, 3 more }`

    Event representing the result of an agent tool execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: "agent.tool_result"`

      - `"agent.tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `beta_managed_agents_image_block: object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_url_image_source: object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `beta_managed_agents_file_image_source: object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `beta_managed_agents_document_block: object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `beta_managed_agents_url_document_source: object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `beta_managed_agents_file_document_source: object { file_id, type }`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

  - `beta_managed_agents_agent_thread_context_compacted_event: object { id, processed_at, type }`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.thread_context_compacted"`

      - `"agent.thread_context_compacted"`

  - `beta_managed_agents_session_error_event: object { id, error, processed_at, type }`

    An error event indicating a problem occurred during session execution.

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 4 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `beta_managed_agents_unknown_error: object { message, retry_status, type }`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `beta_managed_agents_retry_status_exhausted: object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `beta_managed_agents_retry_status_terminal: object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "unknown_error"`

          - `"unknown_error"`

      - `beta_managed_agents_model_overloaded_error: object { message, retry_status, type }`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `beta_managed_agents_retry_status_exhausted: object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `beta_managed_agents_retry_status_terminal: object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "model_overloaded_error"`

          - `"model_overloaded_error"`

      - `beta_managed_agents_model_rate_limited_error: object { message, retry_status, type }`

        The model request was rate-limited.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `beta_managed_agents_retry_status_exhausted: object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `beta_managed_agents_retry_status_terminal: object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "model_rate_limited_error"`

          - `"model_rate_limited_error"`

      - `beta_managed_agents_model_request_failed_error: object { message, retry_status, type }`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `beta_managed_agents_retry_status_exhausted: object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `beta_managed_agents_retry_status_terminal: object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "model_request_failed_error"`

          - `"model_request_failed_error"`

      - `beta_managed_agents_mcp_connection_failed_error: object { mcp_server_name, message, retry_status, type }`

        Failed to connect to an MCP server.

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `beta_managed_agents_retry_status_exhausted: object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `beta_managed_agents_retry_status_terminal: object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "mcp_connection_failed_error"`

          - `"mcp_connection_failed_error"`

      - `beta_managed_agents_mcp_authentication_failed_error: object { mcp_server_name, message, retry_status, type }`

        Authentication to an MCP server failed.

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `beta_managed_agents_retry_status_exhausted: object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `beta_managed_agents_retry_status_terminal: object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "mcp_authentication_failed_error"`

          - `"mcp_authentication_failed_error"`

      - `beta_managed_agents_billing_error: object { message, retry_status, type }`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `beta_managed_agents_retry_status_exhausted: object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `beta_managed_agents_retry_status_terminal: object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "billing_error"`

          - `"billing_error"`

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.error"`

      - `"session.error"`

  - `beta_managed_agents_session_status_rescheduled_event: object { id, processed_at, type }`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_rescheduled"`

      - `"session.status_rescheduled"`

  - `beta_managed_agents_session_status_running_event: object { id, processed_at, type }`

    Indicates the session is actively running and the agent is working.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_running"`

      - `"session.status_running"`

  - `beta_managed_agents_session_status_idle_event: object { id, processed_at, stop_reason, type }`

    Indicates the agent has paused and is awaiting user input.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted`

      The agent completed its turn naturally and is ready for the next user message.

      - `beta_managed_agents_session_end_turn: object { type }`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

          - `"end_turn"`

      - `beta_managed_agents_session_requires_action: object { event_ids, type }`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: array of string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: "requires_action"`

          - `"requires_action"`

      - `beta_managed_agents_session_retries_exhausted: object { type }`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `type: "retries_exhausted"`

          - `"retries_exhausted"`

    - `type: "session.status_idle"`

      - `"session.status_idle"`

  - `beta_managed_agents_session_status_terminated_event: object { id, processed_at, type }`

    Indicates the session has terminated, either due to an error or completion.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_terminated"`

      - `"session.status_terminated"`

  - `beta_managed_agents_span_model_request_start_event: object { id, processed_at, type }`

    Emitted when a model request is initiated by the agent.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "span.model_request_start"`

      - `"span.model_request_start"`

  - `beta_managed_agents_span_model_request_end_event: object { id, is_error, model_request_start_id, 3 more }`

    Emitted when a model request completes.

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: object { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 2 more }`

      Token usage for a single model request.

      - `cache_creation_input_tokens: number`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: number`

        Tokens read from prompt cache in this request.

      - `input_tokens: number`

        Input tokens consumed by this request.

      - `output_tokens: number`

        Output tokens generated by this request.

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "span.model_request_end"`

      - `"span.model_request_end"`

  - `beta_managed_agents_session_deleted_event: object { id, processed_at, type }`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.deleted"`

      - `"session.deleted"`

### Beta Managed Agents Session Requires Action

- `beta_managed_agents_session_requires_action: object { event_ids, type }`

  The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

  - `event_ids: array of string`

    The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

  - `type: "requires_action"`

    - `"requires_action"`

### Beta Managed Agents Session Retries Exhausted

- `beta_managed_agents_session_retries_exhausted: object { type }`

  The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

  - `type: "retries_exhausted"`

    - `"retries_exhausted"`

### Beta Managed Agents Session Status Idle Event

- `beta_managed_agents_session_status_idle_event: object { id, processed_at, stop_reason, type }`

  Indicates the agent has paused and is awaiting user input.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

  - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted`

    The agent completed its turn naturally and is ready for the next user message.

    - `beta_managed_agents_session_end_turn: object { type }`

      The agent completed its turn naturally and is ready for the next user message.

      - `type: "end_turn"`

        - `"end_turn"`

    - `beta_managed_agents_session_requires_action: object { event_ids, type }`

      The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `event_ids: array of string`

        The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

      - `type: "requires_action"`

        - `"requires_action"`

    - `beta_managed_agents_session_retries_exhausted: object { type }`

      The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

      - `type: "retries_exhausted"`

        - `"retries_exhausted"`

  - `type: "session.status_idle"`

    - `"session.status_idle"`

### Beta Managed Agents Session Status Rescheduled Event

- `beta_managed_agents_session_status_rescheduled_event: object { id, processed_at, type }`

  Indicates the session is recovering from an error state and is rescheduled for execution.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

  - `type: "session.status_rescheduled"`

    - `"session.status_rescheduled"`

### Beta Managed Agents Session Status Running Event

- `beta_managed_agents_session_status_running_event: object { id, processed_at, type }`

  Indicates the session is actively running and the agent is working.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

  - `type: "session.status_running"`

    - `"session.status_running"`

### Beta Managed Agents Session Status Terminated Event

- `beta_managed_agents_session_status_terminated_event: object { id, processed_at, type }`

  Indicates the session has terminated, either due to an error or completion.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

  - `type: "session.status_terminated"`

    - `"session.status_terminated"`

### Beta Managed Agents Span Model Request End Event

- `beta_managed_agents_span_model_request_end_event: object { id, is_error, model_request_start_id, 3 more }`

  Emitted when a model request completes.

  - `id: string`

    Unique identifier for this event.

  - `is_error: boolean`

    Whether the model request resulted in an error.

  - `model_request_start_id: string`

    The id of the corresponding `span.model_request_start` event.

  - `model_usage: object { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 2 more }`

    Token usage for a single model request.

    - `cache_creation_input_tokens: number`

      Tokens used to create prompt cache in this request.

    - `cache_read_input_tokens: number`

      Tokens read from prompt cache in this request.

    - `input_tokens: number`

      Input tokens consumed by this request.

    - `output_tokens: number`

      Output tokens generated by this request.

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `processed_at: string`

    A timestamp in RFC 3339 format

  - `type: "span.model_request_end"`

    - `"span.model_request_end"`

### Beta Managed Agents Span Model Request Start Event

- `beta_managed_agents_span_model_request_start_event: object { id, processed_at, type }`

  Emitted when a model request is initiated by the agent.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

  - `type: "span.model_request_start"`

    - `"span.model_request_start"`

### Beta Managed Agents Span Model Usage

- `beta_managed_agents_span_model_usage: object { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 2 more }`

  Token usage for a single model request.

  - `cache_creation_input_tokens: number`

    Tokens used to create prompt cache in this request.

  - `cache_read_input_tokens: number`

    Tokens read from prompt cache in this request.

  - `input_tokens: number`

    Input tokens consumed by this request.

  - `output_tokens: number`

    Output tokens generated by this request.

  - `speed: optional "standard" or "fast"`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"`

    - `"fast"`

### Beta Managed Agents Stream Session Events

- `beta_managed_agents_stream_session_events: BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or 17 more`

  Server-sent event in the session stream.

  - `beta_managed_agents_user_message_event: object { id, content, type, processed_at }`

    A user message event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      Array of content blocks comprising the user message.

      - `beta_managed_agents_text_block: object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `beta_managed_agents_image_block: object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_url_image_source: object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `beta_managed_agents_file_image_source: object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `beta_managed_agents_document_block: object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `beta_managed_agents_url_document_source: object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `beta_managed_agents_file_document_source: object { file_id, type }`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

    - `type: "user.message"`

      - `"user.message"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

  - `beta_managed_agents_user_interrupt_event: object { id, type, processed_at }`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: string`

      Unique identifier for this event.

    - `type: "user.interrupt"`

      - `"user.interrupt"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

  - `beta_managed_agents_user_tool_confirmation_event: object { id, result, tool_use_id, 3 more }`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: string`

      Unique identifier for this event.

    - `result: "allow" or "deny"`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_confirmation"`

      - `"user.tool_confirmation"`

    - `deny_message: optional string`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

  - `beta_managed_agents_user_custom_tool_result_event: object { id, custom_tool_use_id, type, 3 more }`

    Event sent by the client providing the result of a custom tool execution.

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.custom_tool_result"`

      - `"user.custom_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `beta_managed_agents_image_block: object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_url_image_source: object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `beta_managed_agents_file_image_source: object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `beta_managed_agents_document_block: object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `beta_managed_agents_url_document_source: object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `beta_managed_agents_file_document_source: object { file_id, type }`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

  - `beta_managed_agents_agent_custom_tool_use_event: object { id, input, name, 2 more }`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the custom tool being called.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.custom_tool_use"`

      - `"agent.custom_tool_use"`

  - `beta_managed_agents_agent_message_event: object { id, content, processed_at, type }`

    An agent response event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock`

      Array of text blocks comprising the agent response.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.message"`

      - `"agent.message"`

  - `beta_managed_agents_agent_thinking_event: object { id, processed_at, type }`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.thinking"`

      - `"agent.thinking"`

  - `beta_managed_agents_agent_mcp_tool_use_event: object { id, input, mcp_server_name, 4 more }`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `mcp_server_name: string`

      Name of the MCP server providing the tool.

    - `name: string`

      Name of the MCP tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.mcp_tool_use"`

      - `"agent.mcp_tool_use"`

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

  - `beta_managed_agents_agent_mcp_tool_result_event: object { id, mcp_tool_use_id, processed_at, 3 more }`

    Event representing the result of an MCP tool execution.

    - `id: string`

      Unique identifier for this event.

    - `mcp_tool_use_id: string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.mcp_tool_result"`

      - `"agent.mcp_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `beta_managed_agents_image_block: object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_url_image_source: object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `beta_managed_agents_file_image_source: object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `beta_managed_agents_document_block: object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `beta_managed_agents_url_document_source: object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `beta_managed_agents_file_document_source: object { file_id, type }`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

  - `beta_managed_agents_agent_tool_use_event: object { id, input, name, 3 more }`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the agent tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.tool_use"`

      - `"agent.tool_use"`

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

  - `beta_managed_agents_agent_tool_result_event: object { id, processed_at, tool_use_id, 3 more }`

    Event representing the result of an agent tool execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: "agent.tool_result"`

      - `"agent.tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `beta_managed_agents_image_block: object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_url_image_source: object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `beta_managed_agents_file_image_source: object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `beta_managed_agents_document_block: object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `beta_managed_agents_url_document_source: object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `beta_managed_agents_file_document_source: object { file_id, type }`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

  - `beta_managed_agents_agent_thread_context_compacted_event: object { id, processed_at, type }`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.thread_context_compacted"`

      - `"agent.thread_context_compacted"`

  - `beta_managed_agents_session_error_event: object { id, error, processed_at, type }`

    An error event indicating a problem occurred during session execution.

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 4 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `beta_managed_agents_unknown_error: object { message, retry_status, type }`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `beta_managed_agents_retry_status_exhausted: object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `beta_managed_agents_retry_status_terminal: object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "unknown_error"`

          - `"unknown_error"`

      - `beta_managed_agents_model_overloaded_error: object { message, retry_status, type }`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `beta_managed_agents_retry_status_exhausted: object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `beta_managed_agents_retry_status_terminal: object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "model_overloaded_error"`

          - `"model_overloaded_error"`

      - `beta_managed_agents_model_rate_limited_error: object { message, retry_status, type }`

        The model request was rate-limited.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `beta_managed_agents_retry_status_exhausted: object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `beta_managed_agents_retry_status_terminal: object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "model_rate_limited_error"`

          - `"model_rate_limited_error"`

      - `beta_managed_agents_model_request_failed_error: object { message, retry_status, type }`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `beta_managed_agents_retry_status_exhausted: object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `beta_managed_agents_retry_status_terminal: object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "model_request_failed_error"`

          - `"model_request_failed_error"`

      - `beta_managed_agents_mcp_connection_failed_error: object { mcp_server_name, message, retry_status, type }`

        Failed to connect to an MCP server.

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `beta_managed_agents_retry_status_exhausted: object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `beta_managed_agents_retry_status_terminal: object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "mcp_connection_failed_error"`

          - `"mcp_connection_failed_error"`

      - `beta_managed_agents_mcp_authentication_failed_error: object { mcp_server_name, message, retry_status, type }`

        Authentication to an MCP server failed.

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `beta_managed_agents_retry_status_exhausted: object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `beta_managed_agents_retry_status_terminal: object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "mcp_authentication_failed_error"`

          - `"mcp_authentication_failed_error"`

      - `beta_managed_agents_billing_error: object { message, retry_status, type }`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `beta_managed_agents_retry_status_exhausted: object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `beta_managed_agents_retry_status_terminal: object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "billing_error"`

          - `"billing_error"`

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.error"`

      - `"session.error"`

  - `beta_managed_agents_session_status_rescheduled_event: object { id, processed_at, type }`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_rescheduled"`

      - `"session.status_rescheduled"`

  - `beta_managed_agents_session_status_running_event: object { id, processed_at, type }`

    Indicates the session is actively running and the agent is working.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_running"`

      - `"session.status_running"`

  - `beta_managed_agents_session_status_idle_event: object { id, processed_at, stop_reason, type }`

    Indicates the agent has paused and is awaiting user input.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted`

      The agent completed its turn naturally and is ready for the next user message.

      - `beta_managed_agents_session_end_turn: object { type }`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

          - `"end_turn"`

      - `beta_managed_agents_session_requires_action: object { event_ids, type }`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: array of string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: "requires_action"`

          - `"requires_action"`

      - `beta_managed_agents_session_retries_exhausted: object { type }`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `type: "retries_exhausted"`

          - `"retries_exhausted"`

    - `type: "session.status_idle"`

      - `"session.status_idle"`

  - `beta_managed_agents_session_status_terminated_event: object { id, processed_at, type }`

    Indicates the session has terminated, either due to an error or completion.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_terminated"`

      - `"session.status_terminated"`

  - `beta_managed_agents_span_model_request_start_event: object { id, processed_at, type }`

    Emitted when a model request is initiated by the agent.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "span.model_request_start"`

      - `"span.model_request_start"`

  - `beta_managed_agents_span_model_request_end_event: object { id, is_error, model_request_start_id, 3 more }`

    Emitted when a model request completes.

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: object { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 2 more }`

      Token usage for a single model request.

      - `cache_creation_input_tokens: number`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: number`

        Tokens read from prompt cache in this request.

      - `input_tokens: number`

        Input tokens consumed by this request.

      - `output_tokens: number`

        Output tokens generated by this request.

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "span.model_request_end"`

      - `"span.model_request_end"`

  - `beta_managed_agents_session_deleted_event: object { id, processed_at, type }`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.deleted"`

      - `"session.deleted"`

### Beta Managed Agents Text Block

- `beta_managed_agents_text_block: object { text, type }`

  Regular text content.

  - `text: string`

    The text content.

  - `type: "text"`

    - `"text"`

### Beta Managed Agents Unknown Error

- `beta_managed_agents_unknown_error: object { message, retry_status, type }`

  An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `beta_managed_agents_retry_status_retrying: object { type }`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

        - `"retrying"`

    - `beta_managed_agents_retry_status_exhausted: object { type }`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

        - `"exhausted"`

    - `beta_managed_agents_retry_status_terminal: object { type }`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

        - `"terminal"`

  - `type: "unknown_error"`

    - `"unknown_error"`

### Beta Managed Agents URL Document Source

- `beta_managed_agents_url_document_source: object { type, url }`

  Document referenced by URL.

  - `type: "url"`

    - `"url"`

  - `url: string`

    URL of the document to fetch.

### Beta Managed Agents URL Image Source

- `beta_managed_agents_url_image_source: object { type, url }`

  Image referenced by URL.

  - `type: "url"`

    - `"url"`

  - `url: string`

    URL of the image to fetch.

### Beta Managed Agents User Custom Tool Result Event

- `beta_managed_agents_user_custom_tool_result_event: object { id, custom_tool_use_id, type, 3 more }`

  Event sent by the client providing the result of a custom tool execution.

  - `id: string`

    Unique identifier for this event.

  - `custom_tool_use_id: string`

    The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `type: "user.custom_tool_result"`

    - `"user.custom_tool_result"`

  - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

    The result content returned by the tool.

    - `beta_managed_agents_text_block: object { text, type }`

      Regular text content.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `beta_managed_agents_image_block: object { source, type }`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: "base64"`

            - `"base64"`

        - `beta_managed_agents_url_image_source: object { type, url }`

          Image referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the image to fetch.

        - `beta_managed_agents_file_image_source: object { file_id, type }`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "image"`

        - `"image"`

    - `beta_managed_agents_document_block: object { source, type, context, title }`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

          - `type: "base64"`

            - `"base64"`

        - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

          Plain text document content.

          - `data: string`

            The plain text content.

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: "text"`

            - `"text"`

        - `beta_managed_agents_url_document_source: object { type, url }`

          Document referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the document to fetch.

        - `beta_managed_agents_file_document_source: object { file_id, type }`

          Document referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "document"`

        - `"document"`

      - `context: optional string`

        Additional context about the document for the model.

      - `title: optional string`

        The title of the document.

  - `is_error: optional boolean`

    Whether the tool execution resulted in an error.

  - `processed_at: optional string`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Custom Tool Result Event Params

- `beta_managed_agents_user_custom_tool_result_event_params: object { custom_tool_use_id, type, content, is_error }`

  Parameters for providing the result of a custom tool execution.

  - `custom_tool_use_id: string`

    The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `type: "user.custom_tool_result"`

    - `"user.custom_tool_result"`

  - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

    The result content returned by the tool.

    - `beta_managed_agents_text_block: object { text, type }`

      Regular text content.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `beta_managed_agents_image_block: object { source, type }`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: "base64"`

            - `"base64"`

        - `beta_managed_agents_url_image_source: object { type, url }`

          Image referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the image to fetch.

        - `beta_managed_agents_file_image_source: object { file_id, type }`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "image"`

        - `"image"`

    - `beta_managed_agents_document_block: object { source, type, context, title }`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

          - `type: "base64"`

            - `"base64"`

        - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

          Plain text document content.

          - `data: string`

            The plain text content.

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: "text"`

            - `"text"`

        - `beta_managed_agents_url_document_source: object { type, url }`

          Document referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the document to fetch.

        - `beta_managed_agents_file_document_source: object { file_id, type }`

          Document referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "document"`

        - `"document"`

      - `context: optional string`

        Additional context about the document for the model.

      - `title: optional string`

        The title of the document.

  - `is_error: optional boolean`

    Whether the tool execution resulted in an error.

### Beta Managed Agents User Interrupt Event

- `beta_managed_agents_user_interrupt_event: object { id, type, processed_at }`

  An interrupt event that pauses agent execution and returns control to the user.

  - `id: string`

    Unique identifier for this event.

  - `type: "user.interrupt"`

    - `"user.interrupt"`

  - `processed_at: optional string`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Interrupt Event Params

- `beta_managed_agents_user_interrupt_event_params: object { type }`

  Parameters for sending an interrupt to pause the agent.

  - `type: "user.interrupt"`

    - `"user.interrupt"`

### Beta Managed Agents User Message Event

- `beta_managed_agents_user_message_event: object { id, content, type, processed_at }`

  A user message event in the session conversation.

  - `id: string`

    Unique identifier for this event.

  - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

    Array of content blocks comprising the user message.

    - `beta_managed_agents_text_block: object { text, type }`

      Regular text content.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `beta_managed_agents_image_block: object { source, type }`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: "base64"`

            - `"base64"`

        - `beta_managed_agents_url_image_source: object { type, url }`

          Image referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the image to fetch.

        - `beta_managed_agents_file_image_source: object { file_id, type }`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "image"`

        - `"image"`

    - `beta_managed_agents_document_block: object { source, type, context, title }`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

          - `type: "base64"`

            - `"base64"`

        - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

          Plain text document content.

          - `data: string`

            The plain text content.

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: "text"`

            - `"text"`

        - `beta_managed_agents_url_document_source: object { type, url }`

          Document referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the document to fetch.

        - `beta_managed_agents_file_document_source: object { file_id, type }`

          Document referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "document"`

        - `"document"`

      - `context: optional string`

        Additional context about the document for the model.

      - `title: optional string`

        The title of the document.

  - `type: "user.message"`

    - `"user.message"`

  - `processed_at: optional string`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Message Event Params

- `beta_managed_agents_user_message_event_params: object { content, type }`

  Parameters for sending a user message to the session.

  - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

    Array of content blocks for the user message.

    - `beta_managed_agents_text_block: object { text, type }`

      Regular text content.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `beta_managed_agents_image_block: object { source, type }`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: "base64"`

            - `"base64"`

        - `beta_managed_agents_url_image_source: object { type, url }`

          Image referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the image to fetch.

        - `beta_managed_agents_file_image_source: object { file_id, type }`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "image"`

        - `"image"`

    - `beta_managed_agents_document_block: object { source, type, context, title }`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

          - `type: "base64"`

            - `"base64"`

        - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

          Plain text document content.

          - `data: string`

            The plain text content.

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: "text"`

            - `"text"`

        - `beta_managed_agents_url_document_source: object { type, url }`

          Document referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the document to fetch.

        - `beta_managed_agents_file_document_source: object { file_id, type }`

          Document referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "document"`

        - `"document"`

      - `context: optional string`

        Additional context about the document for the model.

      - `title: optional string`

        The title of the document.

  - `type: "user.message"`

    - `"user.message"`

### Beta Managed Agents User Tool Confirmation Event

- `beta_managed_agents_user_tool_confirmation_event: object { id, result, tool_use_id, 3 more }`

  A tool confirmation event that approves or denies a pending tool execution.

  - `id: string`

    Unique identifier for this event.

  - `result: "allow" or "deny"`

    UserToolConfirmationResult enum

    - `"allow"`

    - `"deny"`

  - `tool_use_id: string`

    The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `type: "user.tool_confirmation"`

    - `"user.tool_confirmation"`

  - `deny_message: optional string`

    Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

  - `processed_at: optional string`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Tool Confirmation Event Params

- `beta_managed_agents_user_tool_confirmation_event_params: object { result, tool_use_id, type, deny_message }`

  Parameters for confirming or denying a tool execution request.

  - `result: "allow" or "deny"`

    UserToolConfirmationResult enum

    - `"allow"`

    - `"deny"`

  - `tool_use_id: string`

    The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `type: "user.tool_confirmation"`

    - `"user.tool_confirmation"`

  - `deny_message: optional string`

    Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

# Resources

## Add

`$ ant beta:sessions:resources add`

**post** `/v1/sessions/{session_id}/resources`

Add Session Resource

### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--file-id: string`

  Body param: ID of a previously uploaded file.

- `--type: "file"`

  Body param

- `--mount-path: optional string`

  Body param: Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_file_resource: object { id, created_at, file_id, 3 more }`

  - `id: string`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `file_id: string`

  - `mount_path: string`

  - `type: "file"`

    - `"file"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

### Example

```cli
ant beta:sessions:resources add \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --file-id file_011CNha8iCJcU1wXNR6q4V8w \
  --type file
```

## List

`$ ant beta:sessions:resources list`

**get** `/v1/sessions/{session_id}/resources`

List Session Resources

### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--limit: optional number`

  Query param: Maximum number of resources to return per page (max 1000). If omitted, returns all resources.

- `--page: optional string`

  Query param: Opaque cursor from a previous response's next_page field.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsListSessionResources: object { data, next_page }`

  Paginated list of resources attached to a session.

  - `data: array of BetaManagedAgentsSessionResource`

    Resources for the session, ordered by `created_at`.

    - `beta_managed_agents_github_repository_resource: object { id, created_at, mount_path, 4 more }`

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

        - `beta_managed_agents_branch_checkout: object { name, type }`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `beta_managed_agents_commit_checkout: object { sha, type }`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

    - `beta_managed_agents_file_resource: object { id, created_at, file_id, 3 more }`

      - `id: string`

      - `created_at: string`

        A timestamp in RFC 3339 format

      - `file_id: string`

      - `mount_path: string`

      - `type: "file"`

        - `"file"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

    - `beta_managed_agents_memory_store_resource: object { memory_store_id, type, access, 4 more }`

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

  - `next_page: optional string`

    Opaque cursor for the next page. Null when no more results.

### Example

```cli
ant beta:sessions:resources list \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7
```

## Retrieve

`$ ant beta:sessions:resources retrieve`

**get** `/v1/sessions/{session_id}/resources/{resource_id}`

Get Session Resource

### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--resource-id: string`

  Path param: Path parameter resource_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaSessionResourceGetResponse: BetaManagedAgentsGitHubRepositoryResource or BetaManagedAgentsFileResource or BetaManagedAgentsMemoryStoreResource`

  The requested session resource.

  - `beta_managed_agents_github_repository_resource: object { id, created_at, mount_path, 4 more }`

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

      - `beta_managed_agents_branch_checkout: object { name, type }`

        - `name: string`

          Branch name to check out.

        - `type: "branch"`

          - `"branch"`

      - `beta_managed_agents_commit_checkout: object { sha, type }`

        - `sha: string`

          Full commit SHA to check out.

        - `type: "commit"`

          - `"commit"`

  - `beta_managed_agents_file_resource: object { id, created_at, file_id, 3 more }`

    - `id: string`

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `file_id: string`

    - `mount_path: string`

    - `type: "file"`

      - `"file"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

  - `beta_managed_agents_memory_store_resource: object { memory_store_id, type, access, 4 more }`

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

### Example

```cli
ant beta:sessions:resources retrieve \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --resource-id sesrsc_011CZkZBJq5dWxk9fVLNcPht
```

## Update

`$ ant beta:sessions:resources update`

**post** `/v1/sessions/{session_id}/resources/{resource_id}`

Update Session Resource

### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--resource-id: string`

  Path param: Path parameter resource_id

- `--authorization-token: string`

  Body param: New authorization token for the resource. Currently only `github_repository` resources support token rotation.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaSessionResourceUpdateResponse: BetaManagedAgentsGitHubRepositoryResource or BetaManagedAgentsFileResource or BetaManagedAgentsMemoryStoreResource`

  The updated session resource.

  - `beta_managed_agents_github_repository_resource: object { id, created_at, mount_path, 4 more }`

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

      - `beta_managed_agents_branch_checkout: object { name, type }`

        - `name: string`

          Branch name to check out.

        - `type: "branch"`

          - `"branch"`

      - `beta_managed_agents_commit_checkout: object { sha, type }`

        - `sha: string`

          Full commit SHA to check out.

        - `type: "commit"`

          - `"commit"`

  - `beta_managed_agents_file_resource: object { id, created_at, file_id, 3 more }`

    - `id: string`

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `file_id: string`

    - `mount_path: string`

    - `type: "file"`

      - `"file"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

  - `beta_managed_agents_memory_store_resource: object { memory_store_id, type, access, 4 more }`

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

### Example

```cli
ant beta:sessions:resources update \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --resource-id sesrsc_011CZkZBJq5dWxk9fVLNcPht \
  --authorization-token ghp_exampletoken
```

## Delete

`$ ant beta:sessions:resources delete`

**delete** `/v1/sessions/{session_id}/resources/{resource_id}`

Delete Session Resource

### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--resource-id: string`

  Path param: Path parameter resource_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_delete_session_resource: object { id, type }`

  Confirmation of resource deletion.

  - `id: string`

  - `type: "session_resource_deleted"`

    - `"session_resource_deleted"`

### Example

```cli
ant beta:sessions:resources delete \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --resource-id sesrsc_011CZkZBJq5dWxk9fVLNcPht
```

## Domain Types

### Beta Managed Agents Delete Session Resource

- `beta_managed_agents_delete_session_resource: object { id, type }`

  Confirmation of resource deletion.

  - `id: string`

  - `type: "session_resource_deleted"`

    - `"session_resource_deleted"`

### Beta Managed Agents File Resource

- `beta_managed_agents_file_resource: object { id, created_at, file_id, 3 more }`

  - `id: string`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `file_id: string`

  - `mount_path: string`

  - `type: "file"`

    - `"file"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

### Beta Managed Agents GitHub Repository Resource

- `beta_managed_agents_github_repository_resource: object { id, created_at, mount_path, 4 more }`

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

    - `beta_managed_agents_branch_checkout: object { name, type }`

      - `name: string`

        Branch name to check out.

      - `type: "branch"`

        - `"branch"`

    - `beta_managed_agents_commit_checkout: object { sha, type }`

      - `sha: string`

        Full commit SHA to check out.

      - `type: "commit"`

        - `"commit"`

### Beta Managed Agents Memory Store Resource

- `beta_managed_agents_memory_store_resource: object { memory_store_id, type, access, 4 more }`

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

### Beta Managed Agents Session Resource

- `beta_managed_agents_session_resource: BetaManagedAgentsGitHubRepositoryResource or BetaManagedAgentsFileResource or BetaManagedAgentsMemoryStoreResource`

  A memory store attached to an agent session.

  - `beta_managed_agents_github_repository_resource: object { id, created_at, mount_path, 4 more }`

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

      - `beta_managed_agents_branch_checkout: object { name, type }`

        - `name: string`

          Branch name to check out.

        - `type: "branch"`

          - `"branch"`

      - `beta_managed_agents_commit_checkout: object { sha, type }`

        - `sha: string`

          Full commit SHA to check out.

        - `type: "commit"`

          - `"commit"`

  - `beta_managed_agents_file_resource: object { id, created_at, file_id, 3 more }`

    - `id: string`

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `file_id: string`

    - `mount_path: string`

    - `type: "file"`

      - `"file"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

  - `beta_managed_agents_memory_store_resource: object { memory_store_id, type, access, 4 more }`

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
