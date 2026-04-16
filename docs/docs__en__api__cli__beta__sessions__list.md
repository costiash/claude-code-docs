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
