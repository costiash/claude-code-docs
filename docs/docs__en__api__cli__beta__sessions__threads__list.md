## List

`$ ant beta:sessions:threads list`

**get** `/v1/sessions/{session_id}/threads`

List Session Threads

### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--limit: optional number`

  Query param: Maximum results per page. Defaults to 1000.

- `--page: optional string`

  Query param: Opaque pagination cursor from a previous response's next_page. Forward-only.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsListSessionThreads: object { data, next_page }`

  Paginated list of threads within a `session`.

  - `data: optional array of BetaManagedAgentsSessionThread`

    Threads in the session, primary first then children in spawn order.

    - `id: string`

      Unique identifier for this thread.

    - `agent: object { id, description, mcp_servers, 7 more }`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

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

    - `parent_thread_id: string`

      Parent thread that spawned this thread. Null for the primary thread.

    - `session_id: string`

      The session this thread belongs to.

    - `stats: object { active_seconds, duration_seconds, startup_seconds }`

      Timing statistics for a session thread.

      - `active_seconds: optional number`

        Cumulative time in seconds the thread spent actively running. Excludes idle time.

      - `duration_seconds: optional number`

        Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      - `startup_seconds: optional number`

        Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

    - `status: "running" or "idle" or "rescheduling" or "terminated"`

      SessionThreadStatus enum

      - `"running"`

      - `"idle"`

      - `"rescheduling"`

      - `"terminated"`

    - `type: "session_thread"`

      - `"session_thread"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

    - `usage: object { cache_creation, cache_read_input_tokens, input_tokens, output_tokens }`

      Cumulative token usage for a session thread across all turns.

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

  - `next_page: optional string`

    Opaque cursor for the next page. Null when no more results.

### Example

```cli
ant beta:sessions:threads list \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7
```
