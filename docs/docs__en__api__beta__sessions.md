# Sessions

## Create

**post** `/v1/sessions`

Create Session

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 20 more`

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

    - `"user-profiles-2026-03-24"`

### Body Parameters

- `agent: string or BetaManagedAgentsAgentParams`

  Agent identifier. Accepts the `agent` ID string, which pins the latest version for the session, or an `agent` object with both id and version specified.

  - `UnionMember0 = string`

  - `BetaManagedAgentsAgentParams = object { id, type, version }`

    Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

    - `id: string`

      The `agent` ID.

    - `type: "agent"`

      - `"agent"`

    - `version: optional number`

      The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

- `environment_id: string`

  ID of the `environment` defining the container configuration for this session.

- `metadata: optional map[string]`

  Arbitrary key-value metadata attached to the session. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `resources: optional array of BetaManagedAgentsGitHubRepositoryResourceParams or BetaManagedAgentsFileResourceParams`

  Resources (e.g. repositories, files) to mount into the session's container.

  - `BetaManagedAgentsGitHubRepositoryResourceParams = object { authorization_token, type, url, 2 more }`

    Mount a GitHub repository into the session's container.

    - `authorization_token: string`

      GitHub authorization token used to clone the repository.

    - `type: "github_repository"`

      - `"github_repository"`

    - `url: string`

      Github URL of the repository

    - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

      Branch or commit to check out. Defaults to the repository's default branch.

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

    - `mount_path: optional string`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

  - `BetaManagedAgentsFileResourceParams = object { file_id, type, mount_path }`

    Mount a file uploaded via the Files API into the session.

    - `file_id: string`

      ID of a previously uploaded file.

    - `type: "file"`

      - `"file"`

    - `mount_path: optional string`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

- `title: optional string`

  Human-readable session title.

- `vault_ids: optional array of string`

  Vault IDs for stored credentials the agent can use during the session.

### Returns

- `BetaManagedAgentsSession = object { id, agent, archived_at, 11 more }`

  A Managed Agents `session`.

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

### Example

```http
curl https://api.anthropic.com/v1/sessions \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "agent": "agent_011CZkYpogX7uDKUyvBTophP",
          "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW"
        }'
```

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

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 20 more`

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

    - `"user-profiles-2026-03-24"`

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

## Retrieve

**get** `/v1/sessions/{session_id}`

Get Session

### Path Parameters

- `session_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 20 more`

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

    - `"user-profiles-2026-03-24"`

### Returns

- `BetaManagedAgentsSession = object { id, agent, archived_at, 11 more }`

  A Managed Agents `session`.

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

### Example

```http
curl https://api.anthropic.com/v1/sessions/$SESSION_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Update

**post** `/v1/sessions/{session_id}`

Update Session

### Path Parameters

- `session_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 20 more`

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

    - `"user-profiles-2026-03-24"`

### Body Parameters

- `metadata: optional map[string]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve.

- `title: optional string`

  Human-readable session title.

- `vault_ids: optional array of string`

  Vault IDs (`vlt_*`) to attach to the session. Not yet supported; requests setting this field are rejected. Reserved for future use.

### Returns

- `BetaManagedAgentsSession = object { id, agent, archived_at, 11 more }`

  A Managed Agents `session`.

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

### Example

```http
curl https://api.anthropic.com/v1/sessions/$SESSION_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{}'
```

## Delete

**delete** `/v1/sessions/{session_id}`

Delete Session

### Path Parameters

- `session_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 20 more`

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

    - `"user-profiles-2026-03-24"`

### Returns

- `BetaManagedAgentsDeletedSession = object { id, type }`

  Confirmation that a `session` has been permanently deleted.

  - `id: string`

  - `type: "session_deleted"`

    - `"session_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/sessions/$SESSION_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Archive

**post** `/v1/sessions/{session_id}/archive`

Archive Session

### Path Parameters

- `session_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 20 more`

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

    - `"user-profiles-2026-03-24"`

### Returns

- `BetaManagedAgentsSession = object { id, agent, archived_at, 11 more }`

  A Managed Agents `session`.

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

### Example

```http
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Domain Types

### Beta Managed Agents Agent Params

- `BetaManagedAgentsAgentParams = object { id, type, version }`

  Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

  - `id: string`

    The `agent` ID.

  - `type: "agent"`

    - `"agent"`

  - `version: optional number`

    The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

### Beta Managed Agents Branch Checkout

- `BetaManagedAgentsBranchCheckout = object { name, type }`

  - `name: string`

    Branch name to check out.

  - `type: "branch"`

    - `"branch"`

### Beta Managed Agents Cache Creation Usage

- `BetaManagedAgentsCacheCreationUsage = object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

  Prompt-cache creation token usage broken down by cache lifetime.

  - `ephemeral_1h_input_tokens: optional number`

    Tokens used to create 1-hour ephemeral cache entries.

  - `ephemeral_5m_input_tokens: optional number`

    Tokens used to create 5-minute ephemeral cache entries.

### Beta Managed Agents Commit Checkout

- `BetaManagedAgentsCommitCheckout = object { sha, type }`

  - `sha: string`

    Full commit SHA to check out.

  - `type: "commit"`

    - `"commit"`

### Beta Managed Agents Deleted Session

- `BetaManagedAgentsDeletedSession = object { id, type }`

  Confirmation that a `session` has been permanently deleted.

  - `id: string`

  - `type: "session_deleted"`

    - `"session_deleted"`

### Beta Managed Agents File Resource Params

- `BetaManagedAgentsFileResourceParams = object { file_id, type, mount_path }`

  Mount a file uploaded via the Files API into the session.

  - `file_id: string`

    ID of a previously uploaded file.

  - `type: "file"`

    - `"file"`

  - `mount_path: optional string`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

### Beta Managed Agents GitHub Repository Resource Params

- `BetaManagedAgentsGitHubRepositoryResourceParams = object { authorization_token, type, url, 2 more }`

  Mount a GitHub repository into the session's container.

  - `authorization_token: string`

    GitHub authorization token used to clone the repository.

  - `type: "github_repository"`

    - `"github_repository"`

  - `url: string`

    Github URL of the repository

  - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

    Branch or commit to check out. Defaults to the repository's default branch.

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

  - `mount_path: optional string`

    Mount path in the container. Defaults to `/workspace/<repo-name>`.

### Beta Managed Agents Session

- `BetaManagedAgentsSession = object { id, agent, archived_at, 11 more }`

  A Managed Agents `session`.

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

### Beta Managed Agents Session Agent

- `BetaManagedAgentsSessionAgent = object { id, description, mcp_servers, 7 more }`

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

### Beta Managed Agents Session Stats

- `BetaManagedAgentsSessionStats = object { active_seconds, duration_seconds }`

  Timing statistics for a session.

  - `active_seconds: optional number`

    Cumulative time in seconds the session spent in running status. Excludes idle time.

  - `duration_seconds: optional number`

    Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

### Beta Managed Agents Session Usage

- `BetaManagedAgentsSessionUsage = object { cache_creation, cache_read_input_tokens, input_tokens, output_tokens }`

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

# Events

## List

**get** `/v1/sessions/{session_id}/events`

List Events

### Path Parameters

- `session_id: string`

### Query Parameters

- `limit: optional number`

  Query parameter for limit

- `order: optional "asc" or "desc"`

  Sort direction for results, ordered by created_at. Defaults to asc (chronological).

  - `"asc"`

  - `"desc"`

- `page: optional string`

  Opaque pagination cursor from a previous response's next_page.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 20 more`

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

    - `"user-profiles-2026-03-24"`

### Returns

- `data: optional array of BetaManagedAgentsSessionEvent`

  Events for the session, ordered by `created_at`.

  - `BetaManagedAgentsUserMessageEvent = object { id, content, type, processed_at }`

    A user message event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      Array of content blocks comprising the user message.

      - `BetaManagedAgentsTextBlock = object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock = object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource = object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource = object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource = object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

  - `BetaManagedAgentsUserInterruptEvent = object { id, type, processed_at }`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: string`

      Unique identifier for this event.

    - `type: "user.interrupt"`

      - `"user.interrupt"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

  - `BetaManagedAgentsUserToolConfirmationEvent = object { id, result, tool_use_id, 3 more }`

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

  - `BetaManagedAgentsUserCustomToolResultEvent = object { id, custom_tool_use_id, type, 3 more }`

    Event sent by the client providing the result of a custom tool execution.

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.custom_tool_result"`

      - `"user.custom_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock = object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock = object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource = object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource = object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource = object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

  - `BetaManagedAgentsAgentCustomToolUseEvent = object { id, input, name, 2 more }`

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

  - `BetaManagedAgentsAgentMessageEvent = object { id, content, processed_at, type }`

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

  - `BetaManagedAgentsAgentThinkingEvent = object { id, processed_at, type }`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.thinking"`

      - `"agent.thinking"`

  - `BetaManagedAgentsAgentMCPToolUseEvent = object { id, input, mcp_server_name, 4 more }`

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

  - `BetaManagedAgentsAgentMCPToolResultEvent = object { id, mcp_tool_use_id, processed_at, 3 more }`

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

      - `BetaManagedAgentsTextBlock = object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock = object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource = object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource = object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource = object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

  - `BetaManagedAgentsAgentToolUseEvent = object { id, input, name, 3 more }`

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

  - `BetaManagedAgentsAgentToolResultEvent = object { id, processed_at, tool_use_id, 3 more }`

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

      - `BetaManagedAgentsTextBlock = object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock = object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource = object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource = object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource = object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

  - `BetaManagedAgentsAgentThreadContextCompactedEvent = object { id, processed_at, type }`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.thread_context_compacted"`

      - `"agent.thread_context_compacted"`

  - `BetaManagedAgentsSessionErrorEvent = object { id, error, processed_at, type }`

    An error event indicating a problem occurred during session execution.

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 4 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `BetaManagedAgentsUnknownError = object { message, retry_status, type }`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "unknown_error"`

          - `"unknown_error"`

      - `BetaManagedAgentsModelOverloadedError = object { message, retry_status, type }`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "model_overloaded_error"`

          - `"model_overloaded_error"`

      - `BetaManagedAgentsModelRateLimitedError = object { message, retry_status, type }`

        The model request was rate-limited.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "model_rate_limited_error"`

          - `"model_rate_limited_error"`

      - `BetaManagedAgentsModelRequestFailedError = object { message, retry_status, type }`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "model_request_failed_error"`

          - `"model_request_failed_error"`

      - `BetaManagedAgentsMCPConnectionFailedError = object { mcp_server_name, message, retry_status, type }`

        Failed to connect to an MCP server.

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "mcp_connection_failed_error"`

          - `"mcp_connection_failed_error"`

      - `BetaManagedAgentsMCPAuthenticationFailedError = object { mcp_server_name, message, retry_status, type }`

        Authentication to an MCP server failed.

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "mcp_authentication_failed_error"`

          - `"mcp_authentication_failed_error"`

      - `BetaManagedAgentsBillingError = object { message, retry_status, type }`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "billing_error"`

          - `"billing_error"`

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.error"`

      - `"session.error"`

  - `BetaManagedAgentsSessionStatusRescheduledEvent = object { id, processed_at, type }`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_rescheduled"`

      - `"session.status_rescheduled"`

  - `BetaManagedAgentsSessionStatusRunningEvent = object { id, processed_at, type }`

    Indicates the session is actively running and the agent is working.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_running"`

      - `"session.status_running"`

  - `BetaManagedAgentsSessionStatusIdleEvent = object { id, processed_at, stop_reason, type }`

    Indicates the agent has paused and is awaiting user input.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn = object { type }`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

          - `"end_turn"`

      - `BetaManagedAgentsSessionRequiresAction = object { event_ids, type }`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: array of string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: "requires_action"`

          - `"requires_action"`

      - `BetaManagedAgentsSessionRetriesExhausted = object { type }`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `type: "retries_exhausted"`

          - `"retries_exhausted"`

    - `type: "session.status_idle"`

      - `"session.status_idle"`

  - `BetaManagedAgentsSessionStatusTerminatedEvent = object { id, processed_at, type }`

    Indicates the session has terminated, either due to an error or completion.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_terminated"`

      - `"session.status_terminated"`

  - `BetaManagedAgentsSpanModelRequestStartEvent = object { id, processed_at, type }`

    Emitted when a model request is initiated by the agent.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "span.model_request_start"`

      - `"span.model_request_start"`

  - `BetaManagedAgentsSpanModelRequestEndEvent = object { id, is_error, model_request_start_id, 3 more }`

    Emitted when a model request completes.

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

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

  - `BetaManagedAgentsSessionDeletedEvent = object { id, processed_at, type }`

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

```http
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/events \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Send

**post** `/v1/sessions/{session_id}/events`

Send Events

### Path Parameters

- `session_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 20 more`

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

    - `"user-profiles-2026-03-24"`

### Body Parameters

- `events: array of BetaManagedAgentsEventParams`

  Events to send to the `session`.

  - `BetaManagedAgentsUserMessageEventParams = object { content, type }`

    Parameters for sending a user message to the session.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      Array of content blocks for the user message.

      - `BetaManagedAgentsTextBlock = object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock = object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource = object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource = object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource = object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

  - `BetaManagedAgentsUserInterruptEventParams = object { type }`

    Parameters for sending an interrupt to pause the agent.

    - `type: "user.interrupt"`

      - `"user.interrupt"`

  - `BetaManagedAgentsUserToolConfirmationEventParams = object { result, tool_use_id, type, deny_message }`

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

  - `BetaManagedAgentsUserCustomToolResultEventParams = object { custom_tool_use_id, type, content, is_error }`

    Parameters for providing the result of a custom tool execution.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.custom_tool_result"`

      - `"user.custom_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock = object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock = object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource = object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource = object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource = object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

### Returns

- `BetaManagedAgentsSendSessionEvents = object { data }`

  Events that were successfully sent to the session.

  - `data: optional array of BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or BetaManagedAgentsUserCustomToolResultEvent`

    Sent events

    - `BetaManagedAgentsUserMessageEvent = object { id, content, type, processed_at }`

      A user message event in the session conversation.

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        Array of content blocks comprising the user message.

        - `BetaManagedAgentsTextBlock = object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsImageBlock = object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsURLImageSource = object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `BetaManagedAgentsFileImageSource = object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `BetaManagedAgentsURLDocumentSource = object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

    - `BetaManagedAgentsUserInterruptEvent = object { id, type, processed_at }`

      An interrupt event that pauses agent execution and returns control to the user.

      - `id: string`

        Unique identifier for this event.

      - `type: "user.interrupt"`

        - `"user.interrupt"`

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

    - `BetaManagedAgentsUserToolConfirmationEvent = object { id, result, tool_use_id, 3 more }`

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

    - `BetaManagedAgentsUserCustomToolResultEvent = object { id, custom_tool_use_id, type, 3 more }`

      Event sent by the client providing the result of a custom tool execution.

      - `id: string`

        Unique identifier for this event.

      - `custom_tool_use_id: string`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: "user.custom_tool_result"`

        - `"user.custom_tool_result"`

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        The result content returned by the tool.

        - `BetaManagedAgentsTextBlock = object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsImageBlock = object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsURLImageSource = object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `BetaManagedAgentsFileImageSource = object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `BetaManagedAgentsURLDocumentSource = object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

```http
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/events \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "events": [
            {
              "content": [
                {
                  "text": "Where is my order #1234?",
                  "type": "text"
                }
              ],
              "type": "user.message"
            }
          ]
        }'
```

## Stream

**get** `/v1/sessions/{session_id}/events/stream`

Stream Events

### Path Parameters

- `session_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 20 more`

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

    - `"user-profiles-2026-03-24"`

### Returns

- `BetaManagedAgentsStreamSessionEvents = BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or 17 more`

  Server-sent event in the session stream.

  - `BetaManagedAgentsUserMessageEvent = object { id, content, type, processed_at }`

    A user message event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      Array of content blocks comprising the user message.

      - `BetaManagedAgentsTextBlock = object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock = object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource = object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource = object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource = object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

  - `BetaManagedAgentsUserInterruptEvent = object { id, type, processed_at }`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: string`

      Unique identifier for this event.

    - `type: "user.interrupt"`

      - `"user.interrupt"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

  - `BetaManagedAgentsUserToolConfirmationEvent = object { id, result, tool_use_id, 3 more }`

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

  - `BetaManagedAgentsUserCustomToolResultEvent = object { id, custom_tool_use_id, type, 3 more }`

    Event sent by the client providing the result of a custom tool execution.

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.custom_tool_result"`

      - `"user.custom_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock = object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock = object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource = object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource = object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource = object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

  - `BetaManagedAgentsAgentCustomToolUseEvent = object { id, input, name, 2 more }`

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

  - `BetaManagedAgentsAgentMessageEvent = object { id, content, processed_at, type }`

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

  - `BetaManagedAgentsAgentThinkingEvent = object { id, processed_at, type }`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.thinking"`

      - `"agent.thinking"`

  - `BetaManagedAgentsAgentMCPToolUseEvent = object { id, input, mcp_server_name, 4 more }`

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

  - `BetaManagedAgentsAgentMCPToolResultEvent = object { id, mcp_tool_use_id, processed_at, 3 more }`

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

      - `BetaManagedAgentsTextBlock = object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock = object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource = object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource = object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource = object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

  - `BetaManagedAgentsAgentToolUseEvent = object { id, input, name, 3 more }`

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

  - `BetaManagedAgentsAgentToolResultEvent = object { id, processed_at, tool_use_id, 3 more }`

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

      - `BetaManagedAgentsTextBlock = object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock = object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource = object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource = object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource = object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

  - `BetaManagedAgentsAgentThreadContextCompactedEvent = object { id, processed_at, type }`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.thread_context_compacted"`

      - `"agent.thread_context_compacted"`

  - `BetaManagedAgentsSessionErrorEvent = object { id, error, processed_at, type }`

    An error event indicating a problem occurred during session execution.

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 4 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `BetaManagedAgentsUnknownError = object { message, retry_status, type }`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "unknown_error"`

          - `"unknown_error"`

      - `BetaManagedAgentsModelOverloadedError = object { message, retry_status, type }`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "model_overloaded_error"`

          - `"model_overloaded_error"`

      - `BetaManagedAgentsModelRateLimitedError = object { message, retry_status, type }`

        The model request was rate-limited.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "model_rate_limited_error"`

          - `"model_rate_limited_error"`

      - `BetaManagedAgentsModelRequestFailedError = object { message, retry_status, type }`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "model_request_failed_error"`

          - `"model_request_failed_error"`

      - `BetaManagedAgentsMCPConnectionFailedError = object { mcp_server_name, message, retry_status, type }`

        Failed to connect to an MCP server.

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "mcp_connection_failed_error"`

          - `"mcp_connection_failed_error"`

      - `BetaManagedAgentsMCPAuthenticationFailedError = object { mcp_server_name, message, retry_status, type }`

        Authentication to an MCP server failed.

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "mcp_authentication_failed_error"`

          - `"mcp_authentication_failed_error"`

      - `BetaManagedAgentsBillingError = object { message, retry_status, type }`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "billing_error"`

          - `"billing_error"`

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.error"`

      - `"session.error"`

  - `BetaManagedAgentsSessionStatusRescheduledEvent = object { id, processed_at, type }`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_rescheduled"`

      - `"session.status_rescheduled"`

  - `BetaManagedAgentsSessionStatusRunningEvent = object { id, processed_at, type }`

    Indicates the session is actively running and the agent is working.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_running"`

      - `"session.status_running"`

  - `BetaManagedAgentsSessionStatusIdleEvent = object { id, processed_at, stop_reason, type }`

    Indicates the agent has paused and is awaiting user input.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn = object { type }`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

          - `"end_turn"`

      - `BetaManagedAgentsSessionRequiresAction = object { event_ids, type }`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: array of string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: "requires_action"`

          - `"requires_action"`

      - `BetaManagedAgentsSessionRetriesExhausted = object { type }`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `type: "retries_exhausted"`

          - `"retries_exhausted"`

    - `type: "session.status_idle"`

      - `"session.status_idle"`

  - `BetaManagedAgentsSessionStatusTerminatedEvent = object { id, processed_at, type }`

    Indicates the session has terminated, either due to an error or completion.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_terminated"`

      - `"session.status_terminated"`

  - `BetaManagedAgentsSpanModelRequestStartEvent = object { id, processed_at, type }`

    Emitted when a model request is initiated by the agent.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "span.model_request_start"`

      - `"span.model_request_start"`

  - `BetaManagedAgentsSpanModelRequestEndEvent = object { id, is_error, model_request_start_id, 3 more }`

    Emitted when a model request completes.

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

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

  - `BetaManagedAgentsSessionDeletedEvent = object { id, processed_at, type }`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.deleted"`

      - `"session.deleted"`

### Example

```http
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/events/stream \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Domain Types

### Beta Managed Agents Agent Custom Tool Use Event

- `BetaManagedAgentsAgentCustomToolUseEvent = object { id, input, name, 2 more }`

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

- `BetaManagedAgentsAgentMCPToolResultEvent = object { id, mcp_tool_use_id, processed_at, 3 more }`

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

    - `BetaManagedAgentsTextBlock = object { text, type }`

      Regular text content.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `BetaManagedAgentsImageBlock = object { source, type }`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: "base64"`

            - `"base64"`

        - `BetaManagedAgentsURLImageSource = object { type, url }`

          Image referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the image to fetch.

        - `BetaManagedAgentsFileImageSource = object { file_id, type }`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "image"`

        - `"image"`

    - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

          - `type: "base64"`

            - `"base64"`

        - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

          Plain text document content.

          - `data: string`

            The plain text content.

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsURLDocumentSource = object { type, url }`

          Document referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the document to fetch.

        - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

- `BetaManagedAgentsAgentMCPToolUseEvent = object { id, input, mcp_server_name, 4 more }`

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

- `BetaManagedAgentsAgentMessageEvent = object { id, content, processed_at, type }`

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

- `BetaManagedAgentsAgentThinkingEvent = object { id, processed_at, type }`

  Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

  - `type: "agent.thinking"`

    - `"agent.thinking"`

### Beta Managed Agents Agent Thread Context Compacted Event

- `BetaManagedAgentsAgentThreadContextCompactedEvent = object { id, processed_at, type }`

  Indicates that context compaction (summarization) occurred during the session.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

  - `type: "agent.thread_context_compacted"`

    - `"agent.thread_context_compacted"`

### Beta Managed Agents Agent Tool Result Event

- `BetaManagedAgentsAgentToolResultEvent = object { id, processed_at, tool_use_id, 3 more }`

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

    - `BetaManagedAgentsTextBlock = object { text, type }`

      Regular text content.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `BetaManagedAgentsImageBlock = object { source, type }`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: "base64"`

            - `"base64"`

        - `BetaManagedAgentsURLImageSource = object { type, url }`

          Image referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the image to fetch.

        - `BetaManagedAgentsFileImageSource = object { file_id, type }`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "image"`

        - `"image"`

    - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

          - `type: "base64"`

            - `"base64"`

        - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

          Plain text document content.

          - `data: string`

            The plain text content.

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsURLDocumentSource = object { type, url }`

          Document referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the document to fetch.

        - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

- `BetaManagedAgentsAgentToolUseEvent = object { id, input, name, 3 more }`

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

- `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

  Base64-encoded document data.

  - `data: string`

    Base64-encoded document data.

  - `media_type: string`

    MIME type of the document (e.g., "application/pdf").

  - `type: "base64"`

    - `"base64"`

### Beta Managed Agents Base64 Image Source

- `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

  Base64-encoded image data.

  - `data: string`

    Base64-encoded image data.

  - `media_type: string`

    MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

  - `type: "base64"`

    - `"base64"`

### Beta Managed Agents Billing Error

- `BetaManagedAgentsBillingError = object { message, retry_status, type }`

  The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `BetaManagedAgentsRetryStatusRetrying = object { type }`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

        - `"retrying"`

    - `BetaManagedAgentsRetryStatusExhausted = object { type }`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

        - `"exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal = object { type }`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

        - `"terminal"`

  - `type: "billing_error"`

    - `"billing_error"`

### Beta Managed Agents Document Block

- `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

  Document content, either specified directly as base64 data, as text, or as a reference via a URL.

  - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

    Union type for document source variants.

    - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

      Base64-encoded document data.

      - `data: string`

        Base64-encoded document data.

      - `media_type: string`

        MIME type of the document (e.g., "application/pdf").

      - `type: "base64"`

        - `"base64"`

    - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

      Plain text document content.

      - `data: string`

        The plain text content.

      - `media_type: "text/plain"`

        MIME type of the text content. Must be "text/plain".

        - `"text/plain"`

      - `type: "text"`

        - `"text"`

    - `BetaManagedAgentsURLDocumentSource = object { type, url }`

      Document referenced by URL.

      - `type: "url"`

        - `"url"`

      - `url: string`

        URL of the document to fetch.

    - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

- `BetaManagedAgentsEventParams = BetaManagedAgentsUserMessageEventParams or BetaManagedAgentsUserInterruptEventParams or BetaManagedAgentsUserToolConfirmationEventParams or BetaManagedAgentsUserCustomToolResultEventParams`

  Union type for event parameters that can be sent to a session.

  - `BetaManagedAgentsUserMessageEventParams = object { content, type }`

    Parameters for sending a user message to the session.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      Array of content blocks for the user message.

      - `BetaManagedAgentsTextBlock = object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock = object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource = object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource = object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource = object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

  - `BetaManagedAgentsUserInterruptEventParams = object { type }`

    Parameters for sending an interrupt to pause the agent.

    - `type: "user.interrupt"`

      - `"user.interrupt"`

  - `BetaManagedAgentsUserToolConfirmationEventParams = object { result, tool_use_id, type, deny_message }`

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

  - `BetaManagedAgentsUserCustomToolResultEventParams = object { custom_tool_use_id, type, content, is_error }`

    Parameters for providing the result of a custom tool execution.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.custom_tool_result"`

      - `"user.custom_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock = object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock = object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource = object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource = object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource = object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

- `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

  Document referenced by file ID.

  - `file_id: string`

    ID of a previously uploaded file.

  - `type: "file"`

    - `"file"`

### Beta Managed Agents File Image Source

- `BetaManagedAgentsFileImageSource = object { file_id, type }`

  Image referenced by file ID.

  - `file_id: string`

    ID of a previously uploaded file.

  - `type: "file"`

    - `"file"`

### Beta Managed Agents Image Block

- `BetaManagedAgentsImageBlock = object { source, type }`

  Image content specified directly as base64 data or as a reference via a URL.

  - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

    Union type for image source variants.

    - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

      Base64-encoded image data.

      - `data: string`

        Base64-encoded image data.

      - `media_type: string`

        MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

      - `type: "base64"`

        - `"base64"`

    - `BetaManagedAgentsURLImageSource = object { type, url }`

      Image referenced by URL.

      - `type: "url"`

        - `"url"`

      - `url: string`

        URL of the image to fetch.

    - `BetaManagedAgentsFileImageSource = object { file_id, type }`

      Image referenced by file ID.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

  - `type: "image"`

    - `"image"`

### Beta Managed Agents MCP Authentication Failed Error

- `BetaManagedAgentsMCPAuthenticationFailedError = object { mcp_server_name, message, retry_status, type }`

  Authentication to an MCP server failed.

  - `mcp_server_name: string`

    Name of the MCP server that failed authentication.

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `BetaManagedAgentsRetryStatusRetrying = object { type }`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

        - `"retrying"`

    - `BetaManagedAgentsRetryStatusExhausted = object { type }`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

        - `"exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal = object { type }`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

        - `"terminal"`

  - `type: "mcp_authentication_failed_error"`

    - `"mcp_authentication_failed_error"`

### Beta Managed Agents MCP Connection Failed Error

- `BetaManagedAgentsMCPConnectionFailedError = object { mcp_server_name, message, retry_status, type }`

  Failed to connect to an MCP server.

  - `mcp_server_name: string`

    Name of the MCP server that failed to connect.

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `BetaManagedAgentsRetryStatusRetrying = object { type }`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

        - `"retrying"`

    - `BetaManagedAgentsRetryStatusExhausted = object { type }`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

        - `"exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal = object { type }`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

        - `"terminal"`

  - `type: "mcp_connection_failed_error"`

    - `"mcp_connection_failed_error"`

### Beta Managed Agents Model Overloaded Error

- `BetaManagedAgentsModelOverloadedError = object { message, retry_status, type }`

  The model is currently overloaded. Emitted after automatic retries are exhausted.

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `BetaManagedAgentsRetryStatusRetrying = object { type }`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

        - `"retrying"`

    - `BetaManagedAgentsRetryStatusExhausted = object { type }`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

        - `"exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal = object { type }`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

        - `"terminal"`

  - `type: "model_overloaded_error"`

    - `"model_overloaded_error"`

### Beta Managed Agents Model Rate Limited Error

- `BetaManagedAgentsModelRateLimitedError = object { message, retry_status, type }`

  The model request was rate-limited.

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `BetaManagedAgentsRetryStatusRetrying = object { type }`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

        - `"retrying"`

    - `BetaManagedAgentsRetryStatusExhausted = object { type }`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

        - `"exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal = object { type }`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

        - `"terminal"`

  - `type: "model_rate_limited_error"`

    - `"model_rate_limited_error"`

### Beta Managed Agents Model Request Failed Error

- `BetaManagedAgentsModelRequestFailedError = object { message, retry_status, type }`

  A model request failed for a reason other than overload or rate-limiting.

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `BetaManagedAgentsRetryStatusRetrying = object { type }`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

        - `"retrying"`

    - `BetaManagedAgentsRetryStatusExhausted = object { type }`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

        - `"exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal = object { type }`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

        - `"terminal"`

  - `type: "model_request_failed_error"`

    - `"model_request_failed_error"`

### Beta Managed Agents Plain Text Document Source

- `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

  Plain text document content.

  - `data: string`

    The plain text content.

  - `media_type: "text/plain"`

    MIME type of the text content. Must be "text/plain".

    - `"text/plain"`

  - `type: "text"`

    - `"text"`

### Beta Managed Agents Retry Status Exhausted

- `BetaManagedAgentsRetryStatusExhausted = object { type }`

  This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

  - `type: "exhausted"`

    - `"exhausted"`

### Beta Managed Agents Retry Status Retrying

- `BetaManagedAgentsRetryStatusRetrying = object { type }`

  The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

  - `type: "retrying"`

    - `"retrying"`

### Beta Managed Agents Retry Status Terminal

- `BetaManagedAgentsRetryStatusTerminal = object { type }`

  The session encountered a terminal error and will transition to `terminated` state.

  - `type: "terminal"`

    - `"terminal"`

### Beta Managed Agents Send Session Events

- `BetaManagedAgentsSendSessionEvents = object { data }`

  Events that were successfully sent to the session.

  - `data: optional array of BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or BetaManagedAgentsUserCustomToolResultEvent`

    Sent events

    - `BetaManagedAgentsUserMessageEvent = object { id, content, type, processed_at }`

      A user message event in the session conversation.

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        Array of content blocks comprising the user message.

        - `BetaManagedAgentsTextBlock = object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsImageBlock = object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsURLImageSource = object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `BetaManagedAgentsFileImageSource = object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `BetaManagedAgentsURLDocumentSource = object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

    - `BetaManagedAgentsUserInterruptEvent = object { id, type, processed_at }`

      An interrupt event that pauses agent execution and returns control to the user.

      - `id: string`

        Unique identifier for this event.

      - `type: "user.interrupt"`

        - `"user.interrupt"`

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

    - `BetaManagedAgentsUserToolConfirmationEvent = object { id, result, tool_use_id, 3 more }`

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

    - `BetaManagedAgentsUserCustomToolResultEvent = object { id, custom_tool_use_id, type, 3 more }`

      Event sent by the client providing the result of a custom tool execution.

      - `id: string`

        Unique identifier for this event.

      - `custom_tool_use_id: string`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: "user.custom_tool_result"`

        - `"user.custom_tool_result"`

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        The result content returned by the tool.

        - `BetaManagedAgentsTextBlock = object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsImageBlock = object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsURLImageSource = object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `BetaManagedAgentsFileImageSource = object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `BetaManagedAgentsURLDocumentSource = object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

- `BetaManagedAgentsSessionDeletedEvent = object { id, processed_at, type }`

  Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

  - `type: "session.deleted"`

    - `"session.deleted"`

### Beta Managed Agents Session End Turn

- `BetaManagedAgentsSessionEndTurn = object { type }`

  The agent completed its turn naturally and is ready for the next user message.

  - `type: "end_turn"`

    - `"end_turn"`

### Beta Managed Agents Session Error Event

- `BetaManagedAgentsSessionErrorEvent = object { id, error, processed_at, type }`

  An error event indicating a problem occurred during session execution.

  - `id: string`

    Unique identifier for this event.

  - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 4 more`

    An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

    - `BetaManagedAgentsUnknownError = object { message, retry_status, type }`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `BetaManagedAgentsRetryStatusRetrying = object { type }`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: "retrying"`

            - `"retrying"`

        - `BetaManagedAgentsRetryStatusExhausted = object { type }`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: "exhausted"`

            - `"exhausted"`

        - `BetaManagedAgentsRetryStatusTerminal = object { type }`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: "terminal"`

            - `"terminal"`

      - `type: "unknown_error"`

        - `"unknown_error"`

    - `BetaManagedAgentsModelOverloadedError = object { message, retry_status, type }`

      The model is currently overloaded. Emitted after automatic retries are exhausted.

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `BetaManagedAgentsRetryStatusRetrying = object { type }`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: "retrying"`

            - `"retrying"`

        - `BetaManagedAgentsRetryStatusExhausted = object { type }`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: "exhausted"`

            - `"exhausted"`

        - `BetaManagedAgentsRetryStatusTerminal = object { type }`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: "terminal"`

            - `"terminal"`

      - `type: "model_overloaded_error"`

        - `"model_overloaded_error"`

    - `BetaManagedAgentsModelRateLimitedError = object { message, retry_status, type }`

      The model request was rate-limited.

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `BetaManagedAgentsRetryStatusRetrying = object { type }`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: "retrying"`

            - `"retrying"`

        - `BetaManagedAgentsRetryStatusExhausted = object { type }`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: "exhausted"`

            - `"exhausted"`

        - `BetaManagedAgentsRetryStatusTerminal = object { type }`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: "terminal"`

            - `"terminal"`

      - `type: "model_rate_limited_error"`

        - `"model_rate_limited_error"`

    - `BetaManagedAgentsModelRequestFailedError = object { message, retry_status, type }`

      A model request failed for a reason other than overload or rate-limiting.

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `BetaManagedAgentsRetryStatusRetrying = object { type }`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: "retrying"`

            - `"retrying"`

        - `BetaManagedAgentsRetryStatusExhausted = object { type }`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: "exhausted"`

            - `"exhausted"`

        - `BetaManagedAgentsRetryStatusTerminal = object { type }`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: "terminal"`

            - `"terminal"`

      - `type: "model_request_failed_error"`

        - `"model_request_failed_error"`

    - `BetaManagedAgentsMCPConnectionFailedError = object { mcp_server_name, message, retry_status, type }`

      Failed to connect to an MCP server.

      - `mcp_server_name: string`

        Name of the MCP server that failed to connect.

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `BetaManagedAgentsRetryStatusRetrying = object { type }`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: "retrying"`

            - `"retrying"`

        - `BetaManagedAgentsRetryStatusExhausted = object { type }`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: "exhausted"`

            - `"exhausted"`

        - `BetaManagedAgentsRetryStatusTerminal = object { type }`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: "terminal"`

            - `"terminal"`

      - `type: "mcp_connection_failed_error"`

        - `"mcp_connection_failed_error"`

    - `BetaManagedAgentsMCPAuthenticationFailedError = object { mcp_server_name, message, retry_status, type }`

      Authentication to an MCP server failed.

      - `mcp_server_name: string`

        Name of the MCP server that failed authentication.

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `BetaManagedAgentsRetryStatusRetrying = object { type }`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: "retrying"`

            - `"retrying"`

        - `BetaManagedAgentsRetryStatusExhausted = object { type }`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: "exhausted"`

            - `"exhausted"`

        - `BetaManagedAgentsRetryStatusTerminal = object { type }`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: "terminal"`

            - `"terminal"`

      - `type: "mcp_authentication_failed_error"`

        - `"mcp_authentication_failed_error"`

    - `BetaManagedAgentsBillingError = object { message, retry_status, type }`

      The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `BetaManagedAgentsRetryStatusRetrying = object { type }`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: "retrying"`

            - `"retrying"`

        - `BetaManagedAgentsRetryStatusExhausted = object { type }`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: "exhausted"`

            - `"exhausted"`

        - `BetaManagedAgentsRetryStatusTerminal = object { type }`

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

- `BetaManagedAgentsSessionEvent = BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or 17 more`

  Union type for all event types in a session.

  - `BetaManagedAgentsUserMessageEvent = object { id, content, type, processed_at }`

    A user message event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      Array of content blocks comprising the user message.

      - `BetaManagedAgentsTextBlock = object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock = object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource = object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource = object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource = object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

  - `BetaManagedAgentsUserInterruptEvent = object { id, type, processed_at }`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: string`

      Unique identifier for this event.

    - `type: "user.interrupt"`

      - `"user.interrupt"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

  - `BetaManagedAgentsUserToolConfirmationEvent = object { id, result, tool_use_id, 3 more }`

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

  - `BetaManagedAgentsUserCustomToolResultEvent = object { id, custom_tool_use_id, type, 3 more }`

    Event sent by the client providing the result of a custom tool execution.

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.custom_tool_result"`

      - `"user.custom_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock = object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock = object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource = object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource = object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource = object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

  - `BetaManagedAgentsAgentCustomToolUseEvent = object { id, input, name, 2 more }`

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

  - `BetaManagedAgentsAgentMessageEvent = object { id, content, processed_at, type }`

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

  - `BetaManagedAgentsAgentThinkingEvent = object { id, processed_at, type }`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.thinking"`

      - `"agent.thinking"`

  - `BetaManagedAgentsAgentMCPToolUseEvent = object { id, input, mcp_server_name, 4 more }`

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

  - `BetaManagedAgentsAgentMCPToolResultEvent = object { id, mcp_tool_use_id, processed_at, 3 more }`

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

      - `BetaManagedAgentsTextBlock = object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock = object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource = object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource = object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource = object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

  - `BetaManagedAgentsAgentToolUseEvent = object { id, input, name, 3 more }`

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

  - `BetaManagedAgentsAgentToolResultEvent = object { id, processed_at, tool_use_id, 3 more }`

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

      - `BetaManagedAgentsTextBlock = object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock = object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource = object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource = object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource = object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

  - `BetaManagedAgentsAgentThreadContextCompactedEvent = object { id, processed_at, type }`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.thread_context_compacted"`

      - `"agent.thread_context_compacted"`

  - `BetaManagedAgentsSessionErrorEvent = object { id, error, processed_at, type }`

    An error event indicating a problem occurred during session execution.

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 4 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `BetaManagedAgentsUnknownError = object { message, retry_status, type }`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "unknown_error"`

          - `"unknown_error"`

      - `BetaManagedAgentsModelOverloadedError = object { message, retry_status, type }`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "model_overloaded_error"`

          - `"model_overloaded_error"`

      - `BetaManagedAgentsModelRateLimitedError = object { message, retry_status, type }`

        The model request was rate-limited.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "model_rate_limited_error"`

          - `"model_rate_limited_error"`

      - `BetaManagedAgentsModelRequestFailedError = object { message, retry_status, type }`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "model_request_failed_error"`

          - `"model_request_failed_error"`

      - `BetaManagedAgentsMCPConnectionFailedError = object { mcp_server_name, message, retry_status, type }`

        Failed to connect to an MCP server.

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "mcp_connection_failed_error"`

          - `"mcp_connection_failed_error"`

      - `BetaManagedAgentsMCPAuthenticationFailedError = object { mcp_server_name, message, retry_status, type }`

        Authentication to an MCP server failed.

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "mcp_authentication_failed_error"`

          - `"mcp_authentication_failed_error"`

      - `BetaManagedAgentsBillingError = object { message, retry_status, type }`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "billing_error"`

          - `"billing_error"`

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.error"`

      - `"session.error"`

  - `BetaManagedAgentsSessionStatusRescheduledEvent = object { id, processed_at, type }`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_rescheduled"`

      - `"session.status_rescheduled"`

  - `BetaManagedAgentsSessionStatusRunningEvent = object { id, processed_at, type }`

    Indicates the session is actively running and the agent is working.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_running"`

      - `"session.status_running"`

  - `BetaManagedAgentsSessionStatusIdleEvent = object { id, processed_at, stop_reason, type }`

    Indicates the agent has paused and is awaiting user input.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn = object { type }`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

          - `"end_turn"`

      - `BetaManagedAgentsSessionRequiresAction = object { event_ids, type }`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: array of string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: "requires_action"`

          - `"requires_action"`

      - `BetaManagedAgentsSessionRetriesExhausted = object { type }`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `type: "retries_exhausted"`

          - `"retries_exhausted"`

    - `type: "session.status_idle"`

      - `"session.status_idle"`

  - `BetaManagedAgentsSessionStatusTerminatedEvent = object { id, processed_at, type }`

    Indicates the session has terminated, either due to an error or completion.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_terminated"`

      - `"session.status_terminated"`

  - `BetaManagedAgentsSpanModelRequestStartEvent = object { id, processed_at, type }`

    Emitted when a model request is initiated by the agent.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "span.model_request_start"`

      - `"span.model_request_start"`

  - `BetaManagedAgentsSpanModelRequestEndEvent = object { id, is_error, model_request_start_id, 3 more }`

    Emitted when a model request completes.

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

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

  - `BetaManagedAgentsSessionDeletedEvent = object { id, processed_at, type }`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.deleted"`

      - `"session.deleted"`

### Beta Managed Agents Session Requires Action

- `BetaManagedAgentsSessionRequiresAction = object { event_ids, type }`

  The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

  - `event_ids: array of string`

    The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

  - `type: "requires_action"`

    - `"requires_action"`

### Beta Managed Agents Session Retries Exhausted

- `BetaManagedAgentsSessionRetriesExhausted = object { type }`

  The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

  - `type: "retries_exhausted"`

    - `"retries_exhausted"`

### Beta Managed Agents Session Status Idle Event

- `BetaManagedAgentsSessionStatusIdleEvent = object { id, processed_at, stop_reason, type }`

  Indicates the agent has paused and is awaiting user input.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

  - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted`

    The agent completed its turn naturally and is ready for the next user message.

    - `BetaManagedAgentsSessionEndTurn = object { type }`

      The agent completed its turn naturally and is ready for the next user message.

      - `type: "end_turn"`

        - `"end_turn"`

    - `BetaManagedAgentsSessionRequiresAction = object { event_ids, type }`

      The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `event_ids: array of string`

        The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

      - `type: "requires_action"`

        - `"requires_action"`

    - `BetaManagedAgentsSessionRetriesExhausted = object { type }`

      The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

      - `type: "retries_exhausted"`

        - `"retries_exhausted"`

  - `type: "session.status_idle"`

    - `"session.status_idle"`

### Beta Managed Agents Session Status Rescheduled Event

- `BetaManagedAgentsSessionStatusRescheduledEvent = object { id, processed_at, type }`

  Indicates the session is recovering from an error state and is rescheduled for execution.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

  - `type: "session.status_rescheduled"`

    - `"session.status_rescheduled"`

### Beta Managed Agents Session Status Running Event

- `BetaManagedAgentsSessionStatusRunningEvent = object { id, processed_at, type }`

  Indicates the session is actively running and the agent is working.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

  - `type: "session.status_running"`

    - `"session.status_running"`

### Beta Managed Agents Session Status Terminated Event

- `BetaManagedAgentsSessionStatusTerminatedEvent = object { id, processed_at, type }`

  Indicates the session has terminated, either due to an error or completion.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

  - `type: "session.status_terminated"`

    - `"session.status_terminated"`

### Beta Managed Agents Span Model Request End Event

- `BetaManagedAgentsSpanModelRequestEndEvent = object { id, is_error, model_request_start_id, 3 more }`

  Emitted when a model request completes.

  - `id: string`

    Unique identifier for this event.

  - `is_error: boolean`

    Whether the model request resulted in an error.

  - `model_request_start_id: string`

    The id of the corresponding `span.model_request_start` event.

  - `model_usage: BetaManagedAgentsSpanModelUsage`

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

- `BetaManagedAgentsSpanModelRequestStartEvent = object { id, processed_at, type }`

  Emitted when a model request is initiated by the agent.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

  - `type: "span.model_request_start"`

    - `"span.model_request_start"`

### Beta Managed Agents Span Model Usage

- `BetaManagedAgentsSpanModelUsage = object { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 2 more }`

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

- `BetaManagedAgentsStreamSessionEvents = BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or 17 more`

  Server-sent event in the session stream.

  - `BetaManagedAgentsUserMessageEvent = object { id, content, type, processed_at }`

    A user message event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      Array of content blocks comprising the user message.

      - `BetaManagedAgentsTextBlock = object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock = object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource = object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource = object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource = object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

  - `BetaManagedAgentsUserInterruptEvent = object { id, type, processed_at }`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: string`

      Unique identifier for this event.

    - `type: "user.interrupt"`

      - `"user.interrupt"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

  - `BetaManagedAgentsUserToolConfirmationEvent = object { id, result, tool_use_id, 3 more }`

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

  - `BetaManagedAgentsUserCustomToolResultEvent = object { id, custom_tool_use_id, type, 3 more }`

    Event sent by the client providing the result of a custom tool execution.

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.custom_tool_result"`

      - `"user.custom_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock = object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock = object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource = object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource = object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource = object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

  - `BetaManagedAgentsAgentCustomToolUseEvent = object { id, input, name, 2 more }`

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

  - `BetaManagedAgentsAgentMessageEvent = object { id, content, processed_at, type }`

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

  - `BetaManagedAgentsAgentThinkingEvent = object { id, processed_at, type }`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.thinking"`

      - `"agent.thinking"`

  - `BetaManagedAgentsAgentMCPToolUseEvent = object { id, input, mcp_server_name, 4 more }`

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

  - `BetaManagedAgentsAgentMCPToolResultEvent = object { id, mcp_tool_use_id, processed_at, 3 more }`

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

      - `BetaManagedAgentsTextBlock = object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock = object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource = object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource = object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource = object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

  - `BetaManagedAgentsAgentToolUseEvent = object { id, input, name, 3 more }`

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

  - `BetaManagedAgentsAgentToolResultEvent = object { id, processed_at, tool_use_id, 3 more }`

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

      - `BetaManagedAgentsTextBlock = object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock = object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource = object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource = object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource = object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

  - `BetaManagedAgentsAgentThreadContextCompactedEvent = object { id, processed_at, type }`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.thread_context_compacted"`

      - `"agent.thread_context_compacted"`

  - `BetaManagedAgentsSessionErrorEvent = object { id, error, processed_at, type }`

    An error event indicating a problem occurred during session execution.

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 4 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `BetaManagedAgentsUnknownError = object { message, retry_status, type }`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "unknown_error"`

          - `"unknown_error"`

      - `BetaManagedAgentsModelOverloadedError = object { message, retry_status, type }`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "model_overloaded_error"`

          - `"model_overloaded_error"`

      - `BetaManagedAgentsModelRateLimitedError = object { message, retry_status, type }`

        The model request was rate-limited.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "model_rate_limited_error"`

          - `"model_rate_limited_error"`

      - `BetaManagedAgentsModelRequestFailedError = object { message, retry_status, type }`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "model_request_failed_error"`

          - `"model_request_failed_error"`

      - `BetaManagedAgentsMCPConnectionFailedError = object { mcp_server_name, message, retry_status, type }`

        Failed to connect to an MCP server.

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "mcp_connection_failed_error"`

          - `"mcp_connection_failed_error"`

      - `BetaManagedAgentsMCPAuthenticationFailedError = object { mcp_server_name, message, retry_status, type }`

        Authentication to an MCP server failed.

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "mcp_authentication_failed_error"`

          - `"mcp_authentication_failed_error"`

      - `BetaManagedAgentsBillingError = object { message, retry_status, type }`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying = object { type }`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted = object { type }`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal = object { type }`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "billing_error"`

          - `"billing_error"`

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.error"`

      - `"session.error"`

  - `BetaManagedAgentsSessionStatusRescheduledEvent = object { id, processed_at, type }`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_rescheduled"`

      - `"session.status_rescheduled"`

  - `BetaManagedAgentsSessionStatusRunningEvent = object { id, processed_at, type }`

    Indicates the session is actively running and the agent is working.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_running"`

      - `"session.status_running"`

  - `BetaManagedAgentsSessionStatusIdleEvent = object { id, processed_at, stop_reason, type }`

    Indicates the agent has paused and is awaiting user input.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn = object { type }`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

          - `"end_turn"`

      - `BetaManagedAgentsSessionRequiresAction = object { event_ids, type }`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: array of string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: "requires_action"`

          - `"requires_action"`

      - `BetaManagedAgentsSessionRetriesExhausted = object { type }`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `type: "retries_exhausted"`

          - `"retries_exhausted"`

    - `type: "session.status_idle"`

      - `"session.status_idle"`

  - `BetaManagedAgentsSessionStatusTerminatedEvent = object { id, processed_at, type }`

    Indicates the session has terminated, either due to an error or completion.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_terminated"`

      - `"session.status_terminated"`

  - `BetaManagedAgentsSpanModelRequestStartEvent = object { id, processed_at, type }`

    Emitted when a model request is initiated by the agent.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "span.model_request_start"`

      - `"span.model_request_start"`

  - `BetaManagedAgentsSpanModelRequestEndEvent = object { id, is_error, model_request_start_id, 3 more }`

    Emitted when a model request completes.

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

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

  - `BetaManagedAgentsSessionDeletedEvent = object { id, processed_at, type }`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.deleted"`

      - `"session.deleted"`

### Beta Managed Agents Text Block

- `BetaManagedAgentsTextBlock = object { text, type }`

  Regular text content.

  - `text: string`

    The text content.

  - `type: "text"`

    - `"text"`

### Beta Managed Agents Unknown Error

- `BetaManagedAgentsUnknownError = object { message, retry_status, type }`

  An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `BetaManagedAgentsRetryStatusRetrying = object { type }`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

        - `"retrying"`

    - `BetaManagedAgentsRetryStatusExhausted = object { type }`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

        - `"exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal = object { type }`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

        - `"terminal"`

  - `type: "unknown_error"`

    - `"unknown_error"`

### Beta Managed Agents URL Document Source

- `BetaManagedAgentsURLDocumentSource = object { type, url }`

  Document referenced by URL.

  - `type: "url"`

    - `"url"`

  - `url: string`

    URL of the document to fetch.

### Beta Managed Agents URL Image Source

- `BetaManagedAgentsURLImageSource = object { type, url }`

  Image referenced by URL.

  - `type: "url"`

    - `"url"`

  - `url: string`

    URL of the image to fetch.

### Beta Managed Agents User Custom Tool Result Event

- `BetaManagedAgentsUserCustomToolResultEvent = object { id, custom_tool_use_id, type, 3 more }`

  Event sent by the client providing the result of a custom tool execution.

  - `id: string`

    Unique identifier for this event.

  - `custom_tool_use_id: string`

    The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `type: "user.custom_tool_result"`

    - `"user.custom_tool_result"`

  - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

    The result content returned by the tool.

    - `BetaManagedAgentsTextBlock = object { text, type }`

      Regular text content.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `BetaManagedAgentsImageBlock = object { source, type }`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: "base64"`

            - `"base64"`

        - `BetaManagedAgentsURLImageSource = object { type, url }`

          Image referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the image to fetch.

        - `BetaManagedAgentsFileImageSource = object { file_id, type }`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "image"`

        - `"image"`

    - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

          - `type: "base64"`

            - `"base64"`

        - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

          Plain text document content.

          - `data: string`

            The plain text content.

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsURLDocumentSource = object { type, url }`

          Document referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the document to fetch.

        - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

- `BetaManagedAgentsUserCustomToolResultEventParams = object { custom_tool_use_id, type, content, is_error }`

  Parameters for providing the result of a custom tool execution.

  - `custom_tool_use_id: string`

    The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `type: "user.custom_tool_result"`

    - `"user.custom_tool_result"`

  - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

    The result content returned by the tool.

    - `BetaManagedAgentsTextBlock = object { text, type }`

      Regular text content.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `BetaManagedAgentsImageBlock = object { source, type }`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: "base64"`

            - `"base64"`

        - `BetaManagedAgentsURLImageSource = object { type, url }`

          Image referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the image to fetch.

        - `BetaManagedAgentsFileImageSource = object { file_id, type }`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "image"`

        - `"image"`

    - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

          - `type: "base64"`

            - `"base64"`

        - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

          Plain text document content.

          - `data: string`

            The plain text content.

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsURLDocumentSource = object { type, url }`

          Document referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the document to fetch.

        - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

- `BetaManagedAgentsUserInterruptEvent = object { id, type, processed_at }`

  An interrupt event that pauses agent execution and returns control to the user.

  - `id: string`

    Unique identifier for this event.

  - `type: "user.interrupt"`

    - `"user.interrupt"`

  - `processed_at: optional string`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Interrupt Event Params

- `BetaManagedAgentsUserInterruptEventParams = object { type }`

  Parameters for sending an interrupt to pause the agent.

  - `type: "user.interrupt"`

    - `"user.interrupt"`

### Beta Managed Agents User Message Event

- `BetaManagedAgentsUserMessageEvent = object { id, content, type, processed_at }`

  A user message event in the session conversation.

  - `id: string`

    Unique identifier for this event.

  - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

    Array of content blocks comprising the user message.

    - `BetaManagedAgentsTextBlock = object { text, type }`

      Regular text content.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `BetaManagedAgentsImageBlock = object { source, type }`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: "base64"`

            - `"base64"`

        - `BetaManagedAgentsURLImageSource = object { type, url }`

          Image referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the image to fetch.

        - `BetaManagedAgentsFileImageSource = object { file_id, type }`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "image"`

        - `"image"`

    - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

          - `type: "base64"`

            - `"base64"`

        - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

          Plain text document content.

          - `data: string`

            The plain text content.

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsURLDocumentSource = object { type, url }`

          Document referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the document to fetch.

        - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

- `BetaManagedAgentsUserMessageEventParams = object { content, type }`

  Parameters for sending a user message to the session.

  - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

    Array of content blocks for the user message.

    - `BetaManagedAgentsTextBlock = object { text, type }`

      Regular text content.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `BetaManagedAgentsImageBlock = object { source, type }`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `BetaManagedAgentsBase64ImageSource = object { data, media_type, type }`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: "base64"`

            - `"base64"`

        - `BetaManagedAgentsURLImageSource = object { type, url }`

          Image referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the image to fetch.

        - `BetaManagedAgentsFileImageSource = object { file_id, type }`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "image"`

        - `"image"`

    - `BetaManagedAgentsDocumentBlock = object { source, type, context, title }`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `BetaManagedAgentsBase64DocumentSource = object { data, media_type, type }`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

          - `type: "base64"`

            - `"base64"`

        - `BetaManagedAgentsPlainTextDocumentSource = object { data, media_type, type }`

          Plain text document content.

          - `data: string`

            The plain text content.

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: "text"`

            - `"text"`

        - `BetaManagedAgentsURLDocumentSource = object { type, url }`

          Document referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the document to fetch.

        - `BetaManagedAgentsFileDocumentSource = object { file_id, type }`

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

- `BetaManagedAgentsUserToolConfirmationEvent = object { id, result, tool_use_id, 3 more }`

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

- `BetaManagedAgentsUserToolConfirmationEventParams = object { result, tool_use_id, type, deny_message }`

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

**post** `/v1/sessions/{session_id}/resources`

Add Session Resource

### Path Parameters

- `session_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 20 more`

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

    - `"user-profiles-2026-03-24"`

### Body Parameters

- `file_id: string`

  ID of a previously uploaded file.

- `type: "file"`

  - `"file"`

- `mount_path: optional string`

  Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

### Returns

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

### Example

```http
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/resources \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
          "type": "file"
        }'
```

## List

**get** `/v1/sessions/{session_id}/resources`

List Session Resources

### Path Parameters

- `session_id: string`

### Query Parameters

- `limit: optional number`

  Maximum number of resources to return per page (max 1000). If omitted, returns all resources.

- `page: optional string`

  Opaque cursor from a previous response's next_page field.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 20 more`

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

    - `"user-profiles-2026-03-24"`

### Returns

- `data: array of BetaManagedAgentsSessionResource`

  Resources for the session, ordered by `created_at`.

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

- `next_page: optional string`

  Opaque cursor for the next page. Null when no more results.

### Example

```http
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/resources \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Retrieve

**get** `/v1/sessions/{session_id}/resources/{resource_id}`

Get Session Resource

### Path Parameters

- `session_id: string`

- `resource_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 20 more`

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

    - `"user-profiles-2026-03-24"`

### Returns

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

### Example

```http
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/resources/$RESOURCE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Update

**post** `/v1/sessions/{session_id}/resources/{resource_id}`

Update Session Resource

### Path Parameters

- `session_id: string`

- `resource_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 20 more`

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

    - `"user-profiles-2026-03-24"`

### Body Parameters

- `authorization_token: string`

  New authorization token for the resource. Currently only `github_repository` resources support token rotation.

### Returns

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

### Example

```http
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/resources/$RESOURCE_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "authorization_token": "ghp_exampletoken"
        }'
```

## Delete

**delete** `/v1/sessions/{session_id}/resources/{resource_id}`

Delete Session Resource

### Path Parameters

- `session_id: string`

- `resource_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 20 more`

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

    - `"user-profiles-2026-03-24"`

### Returns

- `BetaManagedAgentsDeleteSessionResource = object { id, type }`

  Confirmation of resource deletion.

  - `id: string`

  - `type: "session_resource_deleted"`

    - `"session_resource_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/resources/$RESOURCE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Domain Types

### Beta Managed Agents Delete Session Resource

- `BetaManagedAgentsDeleteSessionResource = object { id, type }`

  Confirmation of resource deletion.

  - `id: string`

  - `type: "session_resource_deleted"`

    - `"session_resource_deleted"`

### Beta Managed Agents File Resource

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

### Beta Managed Agents GitHub Repository Resource

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

### Beta Managed Agents Session Resource

- `BetaManagedAgentsSessionResource = BetaManagedAgentsGitHubRepositoryResource or BetaManagedAgentsFileResource`

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

### Resource Retrieve Response

- `ResourceRetrieveResponse = BetaManagedAgentsGitHubRepositoryResource or BetaManagedAgentsFileResource`

  The requested session resource.

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

### Resource Update Response

- `ResourceUpdateResponse = BetaManagedAgentsGitHubRepositoryResource or BetaManagedAgentsFileResource`

  The updated session resource.

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
