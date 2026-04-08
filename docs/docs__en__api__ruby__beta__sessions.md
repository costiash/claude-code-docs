# Sessions

## Create

`beta.sessions.create(**kwargs) -> BetaManagedAgentsSession`

**post** `/v1/sessions`

Create Session

### Parameters

- `agent: String | BetaManagedAgentsAgentParams`

  Agent identifier. Accepts the `agent` ID string, which pins the latest version for the session, or an `agent` object with both id and version specified.

  - `String`

  - `class BetaManagedAgentsAgentParams`

    Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

    - `id: String`

      The `agent` ID.

    - `type: :agent`

      - `:agent`

    - `version: Integer`

      The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

- `environment_id: String`

  ID of the `environment` defining the container configuration for this session.

- `metadata: Hash[Symbol, String]`

  Arbitrary key-value metadata attached to the session.

- `resources: Array[BetaManagedAgentsGitHubRepositoryResourceParams | BetaManagedAgentsFileResourceParams]`

  Resources (e.g. repositories, files) to mount into the session's container.

  - `class BetaManagedAgentsGitHubRepositoryResourceParams`

    Mount a GitHub repository into the session's container.

    - `authorization_token: String`

      GitHub authorization token used to clone the repository.

    - `type: :github_repository`

      - `:github_repository`

    - `url: String`

      Github URL of the repository

    - `checkout: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout`

      Branch or commit to check out. Defaults to the repository's default branch.

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

    - `mount_path: String`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

  - `class BetaManagedAgentsFileResourceParams`

    Mount a file uploaded via the Files API into the session.

    - `file_id: String`

      ID of a previously uploaded file.

    - `type: :file`

      - `:file`

    - `mount_path: String`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

- `title: String`

  Human-readable session title.

- `vault_ids: Array[String]`

  Vault IDs for stored credentials the agent can use during the session.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 18 more`

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

### Returns

- `class BetaManagedAgentsSession`

  A Managed Agents `session`.

  - `id: String`

  - `agent: BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `id: String`

    - `description: String`

    - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

      - `name: String`

      - `type: :url`

        - `:url`

      - `url: String`

    - `model: BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-opus-4-6" | :"claude-sonnet-4-6" | :"claude-haiku-4-5" | 5 more`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `:"claude-opus-4-6"`

            Most intelligent model for building agents and coding

          - `:"claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `:"claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `:"claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `:"claude-opus-4-5"`

            Premium model combining maximum intelligence with practical performance

          - `:"claude-opus-4-5-20251101"`

            Premium model combining maximum intelligence with practical performance

          - `:"claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `:"claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `String`

      - `speed: :standard | :fast`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `:standard`

        - `:fast`

    - `name: String`

    - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

      - `class BetaManagedAgentsAnthropicSkill`

        A resolved Anthropic-managed skill.

        - `skill_id: String`

        - `type: :anthropic`

          - `:anthropic`

        - `version: String`

      - `class BetaManagedAgentsCustomSkill`

        A resolved user-created custom skill.

        - `skill_id: String`

        - `type: :custom`

          - `:custom`

        - `version: String`

    - `system_: String`

    - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

      - `class BetaManagedAgentsAgentToolset20260401`

        - `configs: Array[BetaManagedAgentsAgentToolConfig]`

          - `enabled: bool`

          - `name: :bash | :edit | :read | 5 more`

            Built-in agent tool identifier.

            - `:bash`

            - `:edit`

            - `:read`

            - `:write`

            - `:glob`

            - `:grep`

            - `:web_fetch`

            - `:web_search`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

                - `:always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

                - `:always_ask`

        - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

          Resolved default configuration for agent tools.

          - `enabled: bool`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

                - `:always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

                - `:always_ask`

        - `type: :agent_toolset_20260401`

          - `:agent_toolset_20260401`

      - `class BetaManagedAgentsMCPToolset`

        - `configs: Array[BetaManagedAgentsMCPToolConfig]`

          - `enabled: bool`

          - `name: String`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

                - `:always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

                - `:always_ask`

        - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: bool`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

                - `:always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

                - `:always_ask`

        - `mcp_server_name: String`

        - `type: :mcp_toolset`

          - `:mcp_toolset`

      - `class BetaManagedAgentsCustomTool`

        A custom tool as returned in API responses.

        - `description: String`

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `properties: Hash[Symbol, untyped]`

            JSON Schema properties defining the tool's input parameters.

          - `required: Array[String]`

            List of required property names.

          - `type: :object`

            Must be 'object' for tool input schemas.

            - `:object`

        - `name: String`

        - `type: :custom`

          - `:custom`

    - `type: :agent`

      - `:agent`

    - `version: Integer`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `environment_id: String`

  - `metadata: Hash[Symbol, String]`

  - `resources: Array[BetaManagedAgentsSessionResource]`

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

  - `stats: BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `active_seconds: Float`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

    - `duration_seconds: Float`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

  - `status: :rescheduling | :running | :idle | :terminated`

    SessionStatus enum

    - `:rescheduling`

    - `:running`

    - `:idle`

    - `:terminated`

  - `title: String`

  - `type: :session`

    - `:session`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `usage: BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

    - `cache_creation: BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: Integer`

        Tokens used to create 1-hour ephemeral cache entries.

      - `ephemeral_5m_input_tokens: Integer`

        Tokens used to create 5-minute ephemeral cache entries.

    - `cache_read_input_tokens: Integer`

      Total tokens read from prompt cache.

    - `input_tokens: Integer`

      Total input tokens consumed across all turns.

    - `output_tokens: Integer`

      Total output tokens generated across all turns.

  - `vault_ids: Array[String]`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_session = anthropic.beta.sessions.create(
  agent: "agent_011CZkYpogX7uDKUyvBTophP",
  environment_id: "env_011CZkZ9X2dpNyB7HsEFoRfW"
)

puts(beta_managed_agents_session)
```

## List

`beta.sessions.list(**kwargs) -> PageCursor<BetaManagedAgentsSession>`

**get** `/v1/sessions`

List Sessions

### Parameters

- `agent_id: String`

  Filter sessions created with this agent ID.

- `agent_version: Integer`

  Filter by agent version. Only applies when agent_id is also set.

- `created_at_gt: Time`

  Return sessions created after this time (exclusive).

- `created_at_gte: Time`

  Return sessions created at or after this time (inclusive).

- `created_at_lt: Time`

  Return sessions created before this time (exclusive).

- `created_at_lte: Time`

  Return sessions created at or before this time (inclusive).

- `include_archived: bool`

  When true, includes archived sessions. Default: false (exclude archived).

- `limit: Integer`

  Maximum number of results to return.

- `order: :asc | :desc`

  Sort direction for results, ordered by created_at. Defaults to desc (newest first).

  - `:asc`

  - `:desc`

- `page: String`

  Opaque pagination cursor from a previous response's next_page.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 18 more`

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

### Returns

- `class BetaManagedAgentsSession`

  A Managed Agents `session`.

  - `id: String`

  - `agent: BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `id: String`

    - `description: String`

    - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

      - `name: String`

      - `type: :url`

        - `:url`

      - `url: String`

    - `model: BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-opus-4-6" | :"claude-sonnet-4-6" | :"claude-haiku-4-5" | 5 more`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `:"claude-opus-4-6"`

            Most intelligent model for building agents and coding

          - `:"claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `:"claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `:"claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `:"claude-opus-4-5"`

            Premium model combining maximum intelligence with practical performance

          - `:"claude-opus-4-5-20251101"`

            Premium model combining maximum intelligence with practical performance

          - `:"claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `:"claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `String`

      - `speed: :standard | :fast`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `:standard`

        - `:fast`

    - `name: String`

    - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

      - `class BetaManagedAgentsAnthropicSkill`

        A resolved Anthropic-managed skill.

        - `skill_id: String`

        - `type: :anthropic`

          - `:anthropic`

        - `version: String`

      - `class BetaManagedAgentsCustomSkill`

        A resolved user-created custom skill.

        - `skill_id: String`

        - `type: :custom`

          - `:custom`

        - `version: String`

    - `system_: String`

    - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

      - `class BetaManagedAgentsAgentToolset20260401`

        - `configs: Array[BetaManagedAgentsAgentToolConfig]`

          - `enabled: bool`

          - `name: :bash | :edit | :read | 5 more`

            Built-in agent tool identifier.

            - `:bash`

            - `:edit`

            - `:read`

            - `:write`

            - `:glob`

            - `:grep`

            - `:web_fetch`

            - `:web_search`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

                - `:always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

                - `:always_ask`

        - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

          Resolved default configuration for agent tools.

          - `enabled: bool`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

                - `:always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

                - `:always_ask`

        - `type: :agent_toolset_20260401`

          - `:agent_toolset_20260401`

      - `class BetaManagedAgentsMCPToolset`

        - `configs: Array[BetaManagedAgentsMCPToolConfig]`

          - `enabled: bool`

          - `name: String`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

                - `:always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

                - `:always_ask`

        - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: bool`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

                - `:always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

                - `:always_ask`

        - `mcp_server_name: String`

        - `type: :mcp_toolset`

          - `:mcp_toolset`

      - `class BetaManagedAgentsCustomTool`

        A custom tool as returned in API responses.

        - `description: String`

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `properties: Hash[Symbol, untyped]`

            JSON Schema properties defining the tool's input parameters.

          - `required: Array[String]`

            List of required property names.

          - `type: :object`

            Must be 'object' for tool input schemas.

            - `:object`

        - `name: String`

        - `type: :custom`

          - `:custom`

    - `type: :agent`

      - `:agent`

    - `version: Integer`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `environment_id: String`

  - `metadata: Hash[Symbol, String]`

  - `resources: Array[BetaManagedAgentsSessionResource]`

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

  - `stats: BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `active_seconds: Float`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

    - `duration_seconds: Float`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

  - `status: :rescheduling | :running | :idle | :terminated`

    SessionStatus enum

    - `:rescheduling`

    - `:running`

    - `:idle`

    - `:terminated`

  - `title: String`

  - `type: :session`

    - `:session`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `usage: BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

    - `cache_creation: BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: Integer`

        Tokens used to create 1-hour ephemeral cache entries.

      - `ephemeral_5m_input_tokens: Integer`

        Tokens used to create 5-minute ephemeral cache entries.

    - `cache_read_input_tokens: Integer`

      Total tokens read from prompt cache.

    - `input_tokens: Integer`

      Total input tokens consumed across all turns.

    - `output_tokens: Integer`

      Total output tokens generated across all turns.

  - `vault_ids: Array[String]`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.sessions.list

puts(page)
```

## Retrieve

`beta.sessions.retrieve(session_id, **kwargs) -> BetaManagedAgentsSession`

**get** `/v1/sessions/{session_id}`

Get Session

### Parameters

- `session_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 18 more`

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

### Returns

- `class BetaManagedAgentsSession`

  A Managed Agents `session`.

  - `id: String`

  - `agent: BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `id: String`

    - `description: String`

    - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

      - `name: String`

      - `type: :url`

        - `:url`

      - `url: String`

    - `model: BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-opus-4-6" | :"claude-sonnet-4-6" | :"claude-haiku-4-5" | 5 more`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `:"claude-opus-4-6"`

            Most intelligent model for building agents and coding

          - `:"claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `:"claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `:"claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `:"claude-opus-4-5"`

            Premium model combining maximum intelligence with practical performance

          - `:"claude-opus-4-5-20251101"`

            Premium model combining maximum intelligence with practical performance

          - `:"claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `:"claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `String`

      - `speed: :standard | :fast`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `:standard`

        - `:fast`

    - `name: String`

    - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

      - `class BetaManagedAgentsAnthropicSkill`

        A resolved Anthropic-managed skill.

        - `skill_id: String`

        - `type: :anthropic`

          - `:anthropic`

        - `version: String`

      - `class BetaManagedAgentsCustomSkill`

        A resolved user-created custom skill.

        - `skill_id: String`

        - `type: :custom`

          - `:custom`

        - `version: String`

    - `system_: String`

    - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

      - `class BetaManagedAgentsAgentToolset20260401`

        - `configs: Array[BetaManagedAgentsAgentToolConfig]`

          - `enabled: bool`

          - `name: :bash | :edit | :read | 5 more`

            Built-in agent tool identifier.

            - `:bash`

            - `:edit`

            - `:read`

            - `:write`

            - `:glob`

            - `:grep`

            - `:web_fetch`

            - `:web_search`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

                - `:always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

                - `:always_ask`

        - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

          Resolved default configuration for agent tools.

          - `enabled: bool`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

                - `:always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

                - `:always_ask`

        - `type: :agent_toolset_20260401`

          - `:agent_toolset_20260401`

      - `class BetaManagedAgentsMCPToolset`

        - `configs: Array[BetaManagedAgentsMCPToolConfig]`

          - `enabled: bool`

          - `name: String`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

                - `:always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

                - `:always_ask`

        - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: bool`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

                - `:always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

                - `:always_ask`

        - `mcp_server_name: String`

        - `type: :mcp_toolset`

          - `:mcp_toolset`

      - `class BetaManagedAgentsCustomTool`

        A custom tool as returned in API responses.

        - `description: String`

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `properties: Hash[Symbol, untyped]`

            JSON Schema properties defining the tool's input parameters.

          - `required: Array[String]`

            List of required property names.

          - `type: :object`

            Must be 'object' for tool input schemas.

            - `:object`

        - `name: String`

        - `type: :custom`

          - `:custom`

    - `type: :agent`

      - `:agent`

    - `version: Integer`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `environment_id: String`

  - `metadata: Hash[Symbol, String]`

  - `resources: Array[BetaManagedAgentsSessionResource]`

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

  - `stats: BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `active_seconds: Float`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

    - `duration_seconds: Float`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

  - `status: :rescheduling | :running | :idle | :terminated`

    SessionStatus enum

    - `:rescheduling`

    - `:running`

    - `:idle`

    - `:terminated`

  - `title: String`

  - `type: :session`

    - `:session`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `usage: BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

    - `cache_creation: BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: Integer`

        Tokens used to create 1-hour ephemeral cache entries.

      - `ephemeral_5m_input_tokens: Integer`

        Tokens used to create 5-minute ephemeral cache entries.

    - `cache_read_input_tokens: Integer`

      Total tokens read from prompt cache.

    - `input_tokens: Integer`

      Total input tokens consumed across all turns.

    - `output_tokens: Integer`

      Total output tokens generated across all turns.

  - `vault_ids: Array[String]`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_session = anthropic.beta.sessions.retrieve("sesn_011CZkZAtmR3yMPDzynEDxu7")

puts(beta_managed_agents_session)
```

## Update

`beta.sessions.update(session_id, **kwargs) -> BetaManagedAgentsSession`

**post** `/v1/sessions/{session_id}`

Update Session

### Parameters

- `session_id: String`

- `metadata: Hash[Symbol, String]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve.

- `title: String`

  Human-readable session title.

- `vault_ids: Array[String]`

  Vault IDs (`vlt_*`) to attach to the session. Not yet supported; requests setting this field are rejected. Reserved for future use.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 18 more`

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

### Returns

- `class BetaManagedAgentsSession`

  A Managed Agents `session`.

  - `id: String`

  - `agent: BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `id: String`

    - `description: String`

    - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

      - `name: String`

      - `type: :url`

        - `:url`

      - `url: String`

    - `model: BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-opus-4-6" | :"claude-sonnet-4-6" | :"claude-haiku-4-5" | 5 more`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `:"claude-opus-4-6"`

            Most intelligent model for building agents and coding

          - `:"claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `:"claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `:"claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `:"claude-opus-4-5"`

            Premium model combining maximum intelligence with practical performance

          - `:"claude-opus-4-5-20251101"`

            Premium model combining maximum intelligence with practical performance

          - `:"claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `:"claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `String`

      - `speed: :standard | :fast`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `:standard`

        - `:fast`

    - `name: String`

    - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

      - `class BetaManagedAgentsAnthropicSkill`

        A resolved Anthropic-managed skill.

        - `skill_id: String`

        - `type: :anthropic`

          - `:anthropic`

        - `version: String`

      - `class BetaManagedAgentsCustomSkill`

        A resolved user-created custom skill.

        - `skill_id: String`

        - `type: :custom`

          - `:custom`

        - `version: String`

    - `system_: String`

    - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

      - `class BetaManagedAgentsAgentToolset20260401`

        - `configs: Array[BetaManagedAgentsAgentToolConfig]`

          - `enabled: bool`

          - `name: :bash | :edit | :read | 5 more`

            Built-in agent tool identifier.

            - `:bash`

            - `:edit`

            - `:read`

            - `:write`

            - `:glob`

            - `:grep`

            - `:web_fetch`

            - `:web_search`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

                - `:always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

                - `:always_ask`

        - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

          Resolved default configuration for agent tools.

          - `enabled: bool`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

                - `:always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

                - `:always_ask`

        - `type: :agent_toolset_20260401`

          - `:agent_toolset_20260401`

      - `class BetaManagedAgentsMCPToolset`

        - `configs: Array[BetaManagedAgentsMCPToolConfig]`

          - `enabled: bool`

          - `name: String`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

                - `:always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

                - `:always_ask`

        - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: bool`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

                - `:always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

                - `:always_ask`

        - `mcp_server_name: String`

        - `type: :mcp_toolset`

          - `:mcp_toolset`

      - `class BetaManagedAgentsCustomTool`

        A custom tool as returned in API responses.

        - `description: String`

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `properties: Hash[Symbol, untyped]`

            JSON Schema properties defining the tool's input parameters.

          - `required: Array[String]`

            List of required property names.

          - `type: :object`

            Must be 'object' for tool input schemas.

            - `:object`

        - `name: String`

        - `type: :custom`

          - `:custom`

    - `type: :agent`

      - `:agent`

    - `version: Integer`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `environment_id: String`

  - `metadata: Hash[Symbol, String]`

  - `resources: Array[BetaManagedAgentsSessionResource]`

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

  - `stats: BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `active_seconds: Float`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

    - `duration_seconds: Float`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

  - `status: :rescheduling | :running | :idle | :terminated`

    SessionStatus enum

    - `:rescheduling`

    - `:running`

    - `:idle`

    - `:terminated`

  - `title: String`

  - `type: :session`

    - `:session`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `usage: BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

    - `cache_creation: BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: Integer`

        Tokens used to create 1-hour ephemeral cache entries.

      - `ephemeral_5m_input_tokens: Integer`

        Tokens used to create 5-minute ephemeral cache entries.

    - `cache_read_input_tokens: Integer`

      Total tokens read from prompt cache.

    - `input_tokens: Integer`

      Total input tokens consumed across all turns.

    - `output_tokens: Integer`

      Total output tokens generated across all turns.

  - `vault_ids: Array[String]`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_session = anthropic.beta.sessions.update("sesn_011CZkZAtmR3yMPDzynEDxu7")

puts(beta_managed_agents_session)
```

## Delete

`beta.sessions.delete(session_id, **kwargs) -> BetaManagedAgentsDeletedSession`

**delete** `/v1/sessions/{session_id}`

Delete Session

### Parameters

- `session_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 18 more`

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

### Returns

- `class BetaManagedAgentsDeletedSession`

  Confirmation that a `session` has been permanently deleted.

  - `id: String`

  - `type: :session_deleted`

    - `:session_deleted`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_deleted_session = anthropic.beta.sessions.delete("sesn_011CZkZAtmR3yMPDzynEDxu7")

puts(beta_managed_agents_deleted_session)
```

## Archive

`beta.sessions.archive(session_id, **kwargs) -> BetaManagedAgentsSession`

**post** `/v1/sessions/{session_id}/archive`

Archive Session

### Parameters

- `session_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 18 more`

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

### Returns

- `class BetaManagedAgentsSession`

  A Managed Agents `session`.

  - `id: String`

  - `agent: BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `id: String`

    - `description: String`

    - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

      - `name: String`

      - `type: :url`

        - `:url`

      - `url: String`

    - `model: BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-opus-4-6" | :"claude-sonnet-4-6" | :"claude-haiku-4-5" | 5 more`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `:"claude-opus-4-6"`

            Most intelligent model for building agents and coding

          - `:"claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `:"claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `:"claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `:"claude-opus-4-5"`

            Premium model combining maximum intelligence with practical performance

          - `:"claude-opus-4-5-20251101"`

            Premium model combining maximum intelligence with practical performance

          - `:"claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `:"claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `String`

      - `speed: :standard | :fast`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `:standard`

        - `:fast`

    - `name: String`

    - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

      - `class BetaManagedAgentsAnthropicSkill`

        A resolved Anthropic-managed skill.

        - `skill_id: String`

        - `type: :anthropic`

          - `:anthropic`

        - `version: String`

      - `class BetaManagedAgentsCustomSkill`

        A resolved user-created custom skill.

        - `skill_id: String`

        - `type: :custom`

          - `:custom`

        - `version: String`

    - `system_: String`

    - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

      - `class BetaManagedAgentsAgentToolset20260401`

        - `configs: Array[BetaManagedAgentsAgentToolConfig]`

          - `enabled: bool`

          - `name: :bash | :edit | :read | 5 more`

            Built-in agent tool identifier.

            - `:bash`

            - `:edit`

            - `:read`

            - `:write`

            - `:glob`

            - `:grep`

            - `:web_fetch`

            - `:web_search`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

                - `:always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

                - `:always_ask`

        - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

          Resolved default configuration for agent tools.

          - `enabled: bool`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

                - `:always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

                - `:always_ask`

        - `type: :agent_toolset_20260401`

          - `:agent_toolset_20260401`

      - `class BetaManagedAgentsMCPToolset`

        - `configs: Array[BetaManagedAgentsMCPToolConfig]`

          - `enabled: bool`

          - `name: String`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

                - `:always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

                - `:always_ask`

        - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: bool`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

                - `:always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

                - `:always_ask`

        - `mcp_server_name: String`

        - `type: :mcp_toolset`

          - `:mcp_toolset`

      - `class BetaManagedAgentsCustomTool`

        A custom tool as returned in API responses.

        - `description: String`

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `properties: Hash[Symbol, untyped]`

            JSON Schema properties defining the tool's input parameters.

          - `required: Array[String]`

            List of required property names.

          - `type: :object`

            Must be 'object' for tool input schemas.

            - `:object`

        - `name: String`

        - `type: :custom`

          - `:custom`

    - `type: :agent`

      - `:agent`

    - `version: Integer`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `environment_id: String`

  - `metadata: Hash[Symbol, String]`

  - `resources: Array[BetaManagedAgentsSessionResource]`

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

  - `stats: BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `active_seconds: Float`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

    - `duration_seconds: Float`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

  - `status: :rescheduling | :running | :idle | :terminated`

    SessionStatus enum

    - `:rescheduling`

    - `:running`

    - `:idle`

    - `:terminated`

  - `title: String`

  - `type: :session`

    - `:session`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `usage: BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

    - `cache_creation: BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: Integer`

        Tokens used to create 1-hour ephemeral cache entries.

      - `ephemeral_5m_input_tokens: Integer`

        Tokens used to create 5-minute ephemeral cache entries.

    - `cache_read_input_tokens: Integer`

      Total tokens read from prompt cache.

    - `input_tokens: Integer`

      Total input tokens consumed across all turns.

    - `output_tokens: Integer`

      Total output tokens generated across all turns.

  - `vault_ids: Array[String]`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_session = anthropic.beta.sessions.archive("sesn_011CZkZAtmR3yMPDzynEDxu7")

puts(beta_managed_agents_session)
```

## Domain Types

### Beta Managed Agents Agent Params

- `class BetaManagedAgentsAgentParams`

  Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

  - `id: String`

    The `agent` ID.

  - `type: :agent`

    - `:agent`

  - `version: Integer`

    The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

### Beta Managed Agents Branch Checkout

- `class BetaManagedAgentsBranchCheckout`

  - `name: String`

    Branch name to check out.

  - `type: :branch`

    - `:branch`

### Beta Managed Agents Cache Creation Usage

- `class BetaManagedAgentsCacheCreationUsage`

  Prompt-cache creation token usage broken down by cache lifetime.

  - `ephemeral_1h_input_tokens: Integer`

    Tokens used to create 1-hour ephemeral cache entries.

  - `ephemeral_5m_input_tokens: Integer`

    Tokens used to create 5-minute ephemeral cache entries.

### Beta Managed Agents Commit Checkout

- `class BetaManagedAgentsCommitCheckout`

  - `sha: String`

    Full commit SHA to check out.

  - `type: :commit`

    - `:commit`

### Beta Managed Agents Deleted Session

- `class BetaManagedAgentsDeletedSession`

  Confirmation that a `session` has been permanently deleted.

  - `id: String`

  - `type: :session_deleted`

    - `:session_deleted`

### Beta Managed Agents File Resource Params

- `class BetaManagedAgentsFileResourceParams`

  Mount a file uploaded via the Files API into the session.

  - `file_id: String`

    ID of a previously uploaded file.

  - `type: :file`

    - `:file`

  - `mount_path: String`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

### Beta Managed Agents GitHub Repository Resource Params

- `class BetaManagedAgentsGitHubRepositoryResourceParams`

  Mount a GitHub repository into the session's container.

  - `authorization_token: String`

    GitHub authorization token used to clone the repository.

  - `type: :github_repository`

    - `:github_repository`

  - `url: String`

    Github URL of the repository

  - `checkout: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout`

    Branch or commit to check out. Defaults to the repository's default branch.

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

  - `mount_path: String`

    Mount path in the container. Defaults to `/workspace/<repo-name>`.

### Beta Managed Agents Session

- `class BetaManagedAgentsSession`

  A Managed Agents `session`.

  - `id: String`

  - `agent: BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `id: String`

    - `description: String`

    - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

      - `name: String`

      - `type: :url`

        - `:url`

      - `url: String`

    - `model: BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-opus-4-6" | :"claude-sonnet-4-6" | :"claude-haiku-4-5" | 5 more`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `:"claude-opus-4-6"`

            Most intelligent model for building agents and coding

          - `:"claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `:"claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `:"claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `:"claude-opus-4-5"`

            Premium model combining maximum intelligence with practical performance

          - `:"claude-opus-4-5-20251101"`

            Premium model combining maximum intelligence with practical performance

          - `:"claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `:"claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `String`

      - `speed: :standard | :fast`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `:standard`

        - `:fast`

    - `name: String`

    - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

      - `class BetaManagedAgentsAnthropicSkill`

        A resolved Anthropic-managed skill.

        - `skill_id: String`

        - `type: :anthropic`

          - `:anthropic`

        - `version: String`

      - `class BetaManagedAgentsCustomSkill`

        A resolved user-created custom skill.

        - `skill_id: String`

        - `type: :custom`

          - `:custom`

        - `version: String`

    - `system_: String`

    - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

      - `class BetaManagedAgentsAgentToolset20260401`

        - `configs: Array[BetaManagedAgentsAgentToolConfig]`

          - `enabled: bool`

          - `name: :bash | :edit | :read | 5 more`

            Built-in agent tool identifier.

            - `:bash`

            - `:edit`

            - `:read`

            - `:write`

            - `:glob`

            - `:grep`

            - `:web_fetch`

            - `:web_search`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

                - `:always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

                - `:always_ask`

        - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

          Resolved default configuration for agent tools.

          - `enabled: bool`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

                - `:always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

                - `:always_ask`

        - `type: :agent_toolset_20260401`

          - `:agent_toolset_20260401`

      - `class BetaManagedAgentsMCPToolset`

        - `configs: Array[BetaManagedAgentsMCPToolConfig]`

          - `enabled: bool`

          - `name: String`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

                - `:always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

                - `:always_ask`

        - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: bool`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

                - `:always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

                - `:always_ask`

        - `mcp_server_name: String`

        - `type: :mcp_toolset`

          - `:mcp_toolset`

      - `class BetaManagedAgentsCustomTool`

        A custom tool as returned in API responses.

        - `description: String`

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `properties: Hash[Symbol, untyped]`

            JSON Schema properties defining the tool's input parameters.

          - `required: Array[String]`

            List of required property names.

          - `type: :object`

            Must be 'object' for tool input schemas.

            - `:object`

        - `name: String`

        - `type: :custom`

          - `:custom`

    - `type: :agent`

      - `:agent`

    - `version: Integer`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `environment_id: String`

  - `metadata: Hash[Symbol, String]`

  - `resources: Array[BetaManagedAgentsSessionResource]`

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

  - `stats: BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `active_seconds: Float`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

    - `duration_seconds: Float`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

  - `status: :rescheduling | :running | :idle | :terminated`

    SessionStatus enum

    - `:rescheduling`

    - `:running`

    - `:idle`

    - `:terminated`

  - `title: String`

  - `type: :session`

    - `:session`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `usage: BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

    - `cache_creation: BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: Integer`

        Tokens used to create 1-hour ephemeral cache entries.

      - `ephemeral_5m_input_tokens: Integer`

        Tokens used to create 5-minute ephemeral cache entries.

    - `cache_read_input_tokens: Integer`

      Total tokens read from prompt cache.

    - `input_tokens: Integer`

      Total input tokens consumed across all turns.

    - `output_tokens: Integer`

      Total output tokens generated across all turns.

  - `vault_ids: Array[String]`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

### Beta Managed Agents Session Agent

- `class BetaManagedAgentsSessionAgent`

  Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

  - `id: String`

  - `description: String`

  - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

    - `name: String`

    - `type: :url`

      - `:url`

    - `url: String`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `:"claude-opus-4-6" | :"claude-sonnet-4-6" | :"claude-haiku-4-5" | 5 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-opus-4-6"`

          Most intelligent model for building agents and coding

        - `:"claude-sonnet-4-6"`

          Best combination of speed and intelligence

        - `:"claude-haiku-4-5"`

          Fastest model with near-frontier intelligence

        - `:"claude-haiku-4-5-20251001"`

          Fastest model with near-frontier intelligence

        - `:"claude-opus-4-5"`

          Premium model combining maximum intelligence with practical performance

        - `:"claude-opus-4-5-20251101"`

          Premium model combining maximum intelligence with practical performance

        - `:"claude-sonnet-4-5"`

          High-performance model for agents and coding

        - `:"claude-sonnet-4-5-20250929"`

          High-performance model for agents and coding

      - `String`

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `name: String`

  - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

    - `class BetaManagedAgentsAnthropicSkill`

      A resolved Anthropic-managed skill.

      - `skill_id: String`

      - `type: :anthropic`

        - `:anthropic`

      - `version: String`

    - `class BetaManagedAgentsCustomSkill`

      A resolved user-created custom skill.

      - `skill_id: String`

      - `type: :custom`

        - `:custom`

      - `version: String`

  - `system_: String`

  - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

    - `class BetaManagedAgentsAgentToolset20260401`

      - `configs: Array[BetaManagedAgentsAgentToolConfig]`

        - `enabled: bool`

        - `name: :bash | :edit | :read | 5 more`

          Built-in agent tool identifier.

          - `:bash`

          - `:edit`

          - `:read`

          - `:write`

          - `:glob`

          - `:grep`

          - `:web_fetch`

          - `:web_search`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `type: :agent_toolset_20260401`

        - `:agent_toolset_20260401`

    - `class BetaManagedAgentsMCPToolset`

      - `configs: Array[BetaManagedAgentsMCPToolConfig]`

        - `enabled: bool`

        - `name: String`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

              - `:always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

              - `:always_ask`

      - `mcp_server_name: String`

      - `type: :mcp_toolset`

        - `:mcp_toolset`

    - `class BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: String`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `properties: Hash[Symbol, untyped]`

          JSON Schema properties defining the tool's input parameters.

        - `required: Array[String]`

          List of required property names.

        - `type: :object`

          Must be 'object' for tool input schemas.

          - `:object`

      - `name: String`

      - `type: :custom`

        - `:custom`

  - `type: :agent`

    - `:agent`

  - `version: Integer`

### Beta Managed Agents Session Stats

- `class BetaManagedAgentsSessionStats`

  Timing statistics for a session.

  - `active_seconds: Float`

    Cumulative time in seconds the session spent in running status. Excludes idle time.

  - `duration_seconds: Float`

    Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

### Beta Managed Agents Session Usage

- `class BetaManagedAgentsSessionUsage`

  Cumulative token usage for a session across all turns.

  - `cache_creation: BetaManagedAgentsCacheCreationUsage`

    Prompt-cache creation token usage broken down by cache lifetime.

    - `ephemeral_1h_input_tokens: Integer`

      Tokens used to create 1-hour ephemeral cache entries.

    - `ephemeral_5m_input_tokens: Integer`

      Tokens used to create 5-minute ephemeral cache entries.

  - `cache_read_input_tokens: Integer`

    Total tokens read from prompt cache.

  - `input_tokens: Integer`

    Total input tokens consumed across all turns.

  - `output_tokens: Integer`

    Total output tokens generated across all turns.

# Events

## List

`beta.sessions.events.list(session_id, **kwargs) -> PageCursor<BetaManagedAgentsSessionEvent>`

**get** `/v1/sessions/{session_id}/events`

List Events

### Parameters

- `session_id: String`

- `limit: Integer`

  Query parameter for limit

- `order: :asc | :desc`

  Sort direction for results, ordered by created_at. Defaults to asc (chronological).

  - `:asc`

  - `:desc`

- `page: String`

  Opaque pagination cursor from a previous response's next_page.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 18 more`

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

### Returns

- `BetaManagedAgentsSessionEvent = BetaManagedAgentsUserMessageEvent | BetaManagedAgentsUserInterruptEvent | BetaManagedAgentsUserToolConfirmationEvent | 17 more`

  Union type for all event types in a session.

  - `class BetaManagedAgentsUserMessageEvent`

    A user message event in the session conversation.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `type: :"user.message"`

      - `:"user.message"`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: String`

      Unique identifier for this event.

    - `type: :"user.interrupt"`

      - `:"user.interrupt"`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserToolConfirmationEvent`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: String`

      Unique identifier for this event.

    - `result: :allow | :deny`

      UserToolConfirmationResult enum

      - `:allow`

      - `:deny`

    - `tool_use_id: String`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.tool_confirmation"`

      - `:"user.tool_confirmation"`

    - `deny_message: String`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserCustomToolResultEvent`

    Event sent by the client providing the result of a custom tool execution.

    - `id: String`

      Unique identifier for this event.

    - `custom_tool_use_id: String`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.custom_tool_result"`

      - `:"user.custom_tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsAgentCustomToolUseEvent`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `name: String`

      Name of the custom tool being called.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.custom_tool_use"`

      - `:"agent.custom_tool_use"`

  - `class BetaManagedAgentsAgentMessageEvent`

    An agent response event in the session conversation.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock]`

      Array of text blocks comprising the agent response.

      - `text: String`

        The text content.

      - `type: :text`

        - `:text`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.message"`

      - `:"agent.message"`

  - `class BetaManagedAgentsAgentThinkingEvent`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.thinking"`

      - `:"agent.thinking"`

  - `class BetaManagedAgentsAgentMCPToolUseEvent`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `mcp_server_name: String`

      Name of the MCP server providing the tool.

    - `name: String`

      Name of the MCP tool being used.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.mcp_tool_use"`

      - `:"agent.mcp_tool_use"`

    - `evaluated_permission: :allow | :ask | :deny`

      AgentEvaluatedPermission enum

      - `:allow`

      - `:ask`

      - `:deny`

  - `class BetaManagedAgentsAgentMCPToolResultEvent`

    Event representing the result of an MCP tool execution.

    - `id: String`

      Unique identifier for this event.

    - `mcp_tool_use_id: String`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.mcp_tool_result"`

      - `:"agent.mcp_tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `name: String`

      Name of the agent tool being used.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.tool_use"`

      - `:"agent.tool_use"`

    - `evaluated_permission: :allow | :ask | :deny`

      AgentEvaluatedPermission enum

      - `:allow`

      - `:ask`

      - `:deny`

  - `class BetaManagedAgentsAgentToolResultEvent`

    Event representing the result of an agent tool execution.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `tool_use_id: String`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: :"agent.tool_result"`

      - `:"agent.tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.thread_context_compacted"`

      - `:"agent.thread_context_compacted"`

  - `class BetaManagedAgentsSessionErrorEvent`

    An error event indicating a problem occurred during session execution.

    - `id: String`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError | BetaManagedAgentsModelOverloadedError | BetaManagedAgentsModelRateLimitedError | 4 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :unknown_error`

          - `:unknown_error`

      - `class BetaManagedAgentsModelOverloadedError`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :model_overloaded_error`

          - `:model_overloaded_error`

      - `class BetaManagedAgentsModelRateLimitedError`

        The model request was rate-limited.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :model_rate_limited_error`

          - `:model_rate_limited_error`

      - `class BetaManagedAgentsModelRequestFailedError`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :model_request_failed_error`

          - `:model_request_failed_error`

      - `class BetaManagedAgentsMCPConnectionFailedError`

        Failed to connect to an MCP server.

        - `mcp_server_name: String`

          Name of the MCP server that failed to connect.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :mcp_connection_failed_error`

          - `:mcp_connection_failed_error`

      - `class BetaManagedAgentsMCPAuthenticationFailedError`

        Authentication to an MCP server failed.

        - `mcp_server_name: String`

          Name of the MCP server that failed authentication.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :mcp_authentication_failed_error`

          - `:mcp_authentication_failed_error`

      - `class BetaManagedAgentsBillingError`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :billing_error`

          - `:billing_error`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.error"`

      - `:"session.error"`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.status_rescheduled"`

      - `:"session.status_rescheduled"`

  - `class BetaManagedAgentsSessionStatusRunningEvent`

    Indicates the session is actively running and the agent is working.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.status_running"`

      - `:"session.status_running"`

  - `class BetaManagedAgentsSessionStatusIdleEvent`

    Indicates the agent has paused and is awaiting user input.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: :end_turn`

          - `:end_turn`

      - `class BetaManagedAgentsSessionRequiresAction`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: Array[String]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: :requires_action`

          - `:requires_action`

      - `class BetaManagedAgentsSessionRetriesExhausted`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `type: :retries_exhausted`

          - `:retries_exhausted`

    - `type: :"session.status_idle"`

      - `:"session.status_idle"`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent`

    Indicates the session has terminated, either due to an error or completion.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.status_terminated"`

      - `:"session.status_terminated"`

  - `class BetaManagedAgentsSpanModelRequestStartEvent`

    Emitted when a model request is initiated by the agent.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"span.model_request_start"`

      - `:"span.model_request_start"`

  - `class BetaManagedAgentsSpanModelRequestEndEvent`

    Emitted when a model request completes.

    - `id: String`

      Unique identifier for this event.

    - `is_error: bool`

      Whether the model request resulted in an error.

    - `model_request_start_id: String`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: Integer`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: Integer`

        Tokens read from prompt cache in this request.

      - `input_tokens: Integer`

        Input tokens consumed by this request.

      - `output_tokens: Integer`

        Output tokens generated by this request.

      - `speed: :standard | :fast`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `:standard`

        - `:fast`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"span.model_request_end"`

      - `:"span.model_request_end"`

  - `class BetaManagedAgentsSessionDeletedEvent`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.deleted"`

      - `:"session.deleted"`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.sessions.events.list("sesn_011CZkZAtmR3yMPDzynEDxu7")

puts(page)
```

## Send

`beta.sessions.events.send_(session_id, **kwargs) -> BetaManagedAgentsSendSessionEvents`

**post** `/v1/sessions/{session_id}/events`

Send Events

### Parameters

- `session_id: String`

- `events: Array[BetaManagedAgentsEventParams]`

  Events to send to the `session`.

  - `class BetaManagedAgentsUserMessageEventParams`

    Parameters for sending a user message to the session.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `type: :"user.message"`

      - `:"user.message"`

  - `class BetaManagedAgentsUserInterruptEventParams`

    Parameters for sending an interrupt to pause the agent.

    - `type: :"user.interrupt"`

      - `:"user.interrupt"`

  - `class BetaManagedAgentsUserToolConfirmationEventParams`

    Parameters for confirming or denying a tool execution request.

    - `result: :allow | :deny`

      UserToolConfirmationResult enum

      - `:allow`

      - `:deny`

    - `tool_use_id: String`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.tool_confirmation"`

      - `:"user.tool_confirmation"`

    - `deny_message: String`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

  - `class BetaManagedAgentsUserCustomToolResultEventParams`

    Parameters for providing the result of a custom tool execution.

    - `custom_tool_use_id: String`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.custom_tool_result"`

      - `:"user.custom_tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 18 more`

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

### Returns

- `class BetaManagedAgentsSendSessionEvents`

  Events that were successfully sent to the session.

  - `data: Array[BetaManagedAgentsUserMessageEvent | BetaManagedAgentsUserInterruptEvent | BetaManagedAgentsUserToolConfirmationEvent | BetaManagedAgentsUserCustomToolResultEvent]`

    Sent events

    - `class BetaManagedAgentsUserMessageEvent`

      A user message event in the session conversation.

      - `id: String`

        Unique identifier for this event.

      - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

        Array of content blocks comprising the user message.

        - `class BetaManagedAgentsTextBlock`

          Regular text content.

          - `text: String`

            The text content.

          - `type: :text`

            - `:text`

        - `class BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `data: String`

                Base64-encoded image data.

              - `media_type: String`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: :base64`

                - `:base64`

            - `class BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: :url`

                - `:url`

              - `url: String`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

              - `type: :file`

                - `:file`

          - `type: :image`

            - `:image`

        - `class BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `data: String`

                Base64-encoded document data.

              - `media_type: String`

                MIME type of the document (e.g., "application/pdf").

              - `type: :base64`

                - `:base64`

            - `class BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `data: String`

                The plain text content.

              - `media_type: :"text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `:"text/plain"`

              - `type: :text`

                - `:text`

            - `class BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: :url`

                - `:url`

              - `url: String`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

              - `type: :file`

                - `:file`

          - `type: :document`

            - `:document`

          - `context: String`

            Additional context about the document for the model.

          - `title: String`

            The title of the document.

      - `type: :"user.message"`

        - `:"user.message"`

      - `processed_at: Time`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserInterruptEvent`

      An interrupt event that pauses agent execution and returns control to the user.

      - `id: String`

        Unique identifier for this event.

      - `type: :"user.interrupt"`

        - `:"user.interrupt"`

      - `processed_at: Time`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserToolConfirmationEvent`

      A tool confirmation event that approves or denies a pending tool execution.

      - `id: String`

        Unique identifier for this event.

      - `result: :allow | :deny`

        UserToolConfirmationResult enum

        - `:allow`

        - `:deny`

      - `tool_use_id: String`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: :"user.tool_confirmation"`

        - `:"user.tool_confirmation"`

      - `deny_message: String`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      - `processed_at: Time`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserCustomToolResultEvent`

      Event sent by the client providing the result of a custom tool execution.

      - `id: String`

        Unique identifier for this event.

      - `custom_tool_use_id: String`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: :"user.custom_tool_result"`

        - `:"user.custom_tool_result"`

      - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock`

          Regular text content.

          - `text: String`

            The text content.

          - `type: :text`

            - `:text`

        - `class BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `data: String`

                Base64-encoded image data.

              - `media_type: String`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: :base64`

                - `:base64`

            - `class BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: :url`

                - `:url`

              - `url: String`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

              - `type: :file`

                - `:file`

          - `type: :image`

            - `:image`

        - `class BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `data: String`

                Base64-encoded document data.

              - `media_type: String`

                MIME type of the document (e.g., "application/pdf").

              - `type: :base64`

                - `:base64`

            - `class BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `data: String`

                The plain text content.

              - `media_type: :"text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `:"text/plain"`

              - `type: :text`

                - `:text`

            - `class BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: :url`

                - `:url`

              - `url: String`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

              - `type: :file`

                - `:file`

          - `type: :document`

            - `:document`

          - `context: String`

            Additional context about the document for the model.

          - `title: String`

            The title of the document.

      - `is_error: bool`

        Whether the tool execution resulted in an error.

      - `processed_at: Time`

        A timestamp in RFC 3339 format

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_send_session_events = anthropic.beta.sessions.events.send_(
  "sesn_011CZkZAtmR3yMPDzynEDxu7",
  events: [{content: [{text: "Where is my order #1234?", type: :text}], type: :"user.message"}]
)

puts(beta_managed_agents_send_session_events)
```

## Stream

`beta.sessions.events.stream(session_id, **kwargs) -> BetaManagedAgentsStreamSessionEvents`

**get** `/v1/sessions/{session_id}/events/stream`

Stream Events

### Parameters

- `session_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 18 more`

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

### Returns

- `BetaManagedAgentsStreamSessionEvents = BetaManagedAgentsUserMessageEvent | BetaManagedAgentsUserInterruptEvent | BetaManagedAgentsUserToolConfirmationEvent | 17 more`

  Server-sent event in the session stream.

  - `class BetaManagedAgentsUserMessageEvent`

    A user message event in the session conversation.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `type: :"user.message"`

      - `:"user.message"`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: String`

      Unique identifier for this event.

    - `type: :"user.interrupt"`

      - `:"user.interrupt"`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserToolConfirmationEvent`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: String`

      Unique identifier for this event.

    - `result: :allow | :deny`

      UserToolConfirmationResult enum

      - `:allow`

      - `:deny`

    - `tool_use_id: String`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.tool_confirmation"`

      - `:"user.tool_confirmation"`

    - `deny_message: String`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserCustomToolResultEvent`

    Event sent by the client providing the result of a custom tool execution.

    - `id: String`

      Unique identifier for this event.

    - `custom_tool_use_id: String`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.custom_tool_result"`

      - `:"user.custom_tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsAgentCustomToolUseEvent`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `name: String`

      Name of the custom tool being called.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.custom_tool_use"`

      - `:"agent.custom_tool_use"`

  - `class BetaManagedAgentsAgentMessageEvent`

    An agent response event in the session conversation.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock]`

      Array of text blocks comprising the agent response.

      - `text: String`

        The text content.

      - `type: :text`

        - `:text`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.message"`

      - `:"agent.message"`

  - `class BetaManagedAgentsAgentThinkingEvent`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.thinking"`

      - `:"agent.thinking"`

  - `class BetaManagedAgentsAgentMCPToolUseEvent`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `mcp_server_name: String`

      Name of the MCP server providing the tool.

    - `name: String`

      Name of the MCP tool being used.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.mcp_tool_use"`

      - `:"agent.mcp_tool_use"`

    - `evaluated_permission: :allow | :ask | :deny`

      AgentEvaluatedPermission enum

      - `:allow`

      - `:ask`

      - `:deny`

  - `class BetaManagedAgentsAgentMCPToolResultEvent`

    Event representing the result of an MCP tool execution.

    - `id: String`

      Unique identifier for this event.

    - `mcp_tool_use_id: String`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.mcp_tool_result"`

      - `:"agent.mcp_tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `name: String`

      Name of the agent tool being used.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.tool_use"`

      - `:"agent.tool_use"`

    - `evaluated_permission: :allow | :ask | :deny`

      AgentEvaluatedPermission enum

      - `:allow`

      - `:ask`

      - `:deny`

  - `class BetaManagedAgentsAgentToolResultEvent`

    Event representing the result of an agent tool execution.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `tool_use_id: String`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: :"agent.tool_result"`

      - `:"agent.tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.thread_context_compacted"`

      - `:"agent.thread_context_compacted"`

  - `class BetaManagedAgentsSessionErrorEvent`

    An error event indicating a problem occurred during session execution.

    - `id: String`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError | BetaManagedAgentsModelOverloadedError | BetaManagedAgentsModelRateLimitedError | 4 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :unknown_error`

          - `:unknown_error`

      - `class BetaManagedAgentsModelOverloadedError`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :model_overloaded_error`

          - `:model_overloaded_error`

      - `class BetaManagedAgentsModelRateLimitedError`

        The model request was rate-limited.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :model_rate_limited_error`

          - `:model_rate_limited_error`

      - `class BetaManagedAgentsModelRequestFailedError`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :model_request_failed_error`

          - `:model_request_failed_error`

      - `class BetaManagedAgentsMCPConnectionFailedError`

        Failed to connect to an MCP server.

        - `mcp_server_name: String`

          Name of the MCP server that failed to connect.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :mcp_connection_failed_error`

          - `:mcp_connection_failed_error`

      - `class BetaManagedAgentsMCPAuthenticationFailedError`

        Authentication to an MCP server failed.

        - `mcp_server_name: String`

          Name of the MCP server that failed authentication.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :mcp_authentication_failed_error`

          - `:mcp_authentication_failed_error`

      - `class BetaManagedAgentsBillingError`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :billing_error`

          - `:billing_error`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.error"`

      - `:"session.error"`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.status_rescheduled"`

      - `:"session.status_rescheduled"`

  - `class BetaManagedAgentsSessionStatusRunningEvent`

    Indicates the session is actively running and the agent is working.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.status_running"`

      - `:"session.status_running"`

  - `class BetaManagedAgentsSessionStatusIdleEvent`

    Indicates the agent has paused and is awaiting user input.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: :end_turn`

          - `:end_turn`

      - `class BetaManagedAgentsSessionRequiresAction`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: Array[String]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: :requires_action`

          - `:requires_action`

      - `class BetaManagedAgentsSessionRetriesExhausted`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `type: :retries_exhausted`

          - `:retries_exhausted`

    - `type: :"session.status_idle"`

      - `:"session.status_idle"`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent`

    Indicates the session has terminated, either due to an error or completion.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.status_terminated"`

      - `:"session.status_terminated"`

  - `class BetaManagedAgentsSpanModelRequestStartEvent`

    Emitted when a model request is initiated by the agent.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"span.model_request_start"`

      - `:"span.model_request_start"`

  - `class BetaManagedAgentsSpanModelRequestEndEvent`

    Emitted when a model request completes.

    - `id: String`

      Unique identifier for this event.

    - `is_error: bool`

      Whether the model request resulted in an error.

    - `model_request_start_id: String`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: Integer`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: Integer`

        Tokens read from prompt cache in this request.

      - `input_tokens: Integer`

        Input tokens consumed by this request.

      - `output_tokens: Integer`

        Output tokens generated by this request.

      - `speed: :standard | :fast`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `:standard`

        - `:fast`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"span.model_request_end"`

      - `:"span.model_request_end"`

  - `class BetaManagedAgentsSessionDeletedEvent`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.deleted"`

      - `:"session.deleted"`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_stream_session_events = anthropic.beta.sessions.events.stream("sesn_011CZkZAtmR3yMPDzynEDxu7")

puts(beta_managed_agents_stream_session_events)
```

## Domain Types

### Beta Managed Agents Agent Custom Tool Use Event

- `class BetaManagedAgentsAgentCustomToolUseEvent`

  Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

  - `id: String`

    Unique identifier for this event.

  - `input: Hash[Symbol, untyped]`

    Input parameters for the tool call.

  - `name: String`

    Name of the custom tool being called.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"agent.custom_tool_use"`

    - `:"agent.custom_tool_use"`

### Beta Managed Agents Agent MCP Tool Result Event

- `class BetaManagedAgentsAgentMCPToolResultEvent`

  Event representing the result of an MCP tool execution.

  - `id: String`

    Unique identifier for this event.

  - `mcp_tool_use_id: String`

    The id of the `agent.mcp_tool_use` event this result corresponds to.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"agent.mcp_tool_result"`

    - `:"agent.mcp_tool_result"`

  - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock`

      Regular text content.

      - `text: String`

        The text content.

      - `type: :text`

        - `:text`

    - `class BetaManagedAgentsImageBlock`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource`

          Base64-encoded image data.

          - `data: String`

            Base64-encoded image data.

          - `media_type: String`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: :base64`

            - `:base64`

        - `class BetaManagedAgentsURLImageSource`

          Image referenced by URL.

          - `type: :url`

            - `:url`

          - `url: String`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource`

          Image referenced by file ID.

          - `file_id: String`

            ID of a previously uploaded file.

          - `type: :file`

            - `:file`

      - `type: :image`

        - `:image`

    - `class BetaManagedAgentsDocumentBlock`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource`

          Base64-encoded document data.

          - `data: String`

            Base64-encoded document data.

          - `media_type: String`

            MIME type of the document (e.g., "application/pdf").

          - `type: :base64`

            - `:base64`

        - `class BetaManagedAgentsPlainTextDocumentSource`

          Plain text document content.

          - `data: String`

            The plain text content.

          - `media_type: :"text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `:"text/plain"`

          - `type: :text`

            - `:text`

        - `class BetaManagedAgentsURLDocumentSource`

          Document referenced by URL.

          - `type: :url`

            - `:url`

          - `url: String`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource`

          Document referenced by file ID.

          - `file_id: String`

            ID of a previously uploaded file.

          - `type: :file`

            - `:file`

      - `type: :document`

        - `:document`

      - `context: String`

        Additional context about the document for the model.

      - `title: String`

        The title of the document.

  - `is_error: bool`

    Whether the tool execution resulted in an error.

### Beta Managed Agents Agent MCP Tool Use Event

- `class BetaManagedAgentsAgentMCPToolUseEvent`

  Event emitted when the agent invokes a tool provided by an MCP server.

  - `id: String`

    Unique identifier for this event.

  - `input: Hash[Symbol, untyped]`

    Input parameters for the tool call.

  - `mcp_server_name: String`

    Name of the MCP server providing the tool.

  - `name: String`

    Name of the MCP tool being used.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"agent.mcp_tool_use"`

    - `:"agent.mcp_tool_use"`

  - `evaluated_permission: :allow | :ask | :deny`

    AgentEvaluatedPermission enum

    - `:allow`

    - `:ask`

    - `:deny`

### Beta Managed Agents Agent Message Event

- `class BetaManagedAgentsAgentMessageEvent`

  An agent response event in the session conversation.

  - `id: String`

    Unique identifier for this event.

  - `content: Array[BetaManagedAgentsTextBlock]`

    Array of text blocks comprising the agent response.

    - `text: String`

      The text content.

    - `type: :text`

      - `:text`

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"agent.message"`

    - `:"agent.message"`

### Beta Managed Agents Agent Thinking Event

- `class BetaManagedAgentsAgentThinkingEvent`

  Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

  - `id: String`

    Unique identifier for this event.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"agent.thinking"`

    - `:"agent.thinking"`

### Beta Managed Agents Agent Thread Context Compacted Event

- `class BetaManagedAgentsAgentThreadContextCompactedEvent`

  Indicates that context compaction (summarization) occurred during the session.

  - `id: String`

    Unique identifier for this event.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"agent.thread_context_compacted"`

    - `:"agent.thread_context_compacted"`

### Beta Managed Agents Agent Tool Result Event

- `class BetaManagedAgentsAgentToolResultEvent`

  Event representing the result of an agent tool execution.

  - `id: String`

    Unique identifier for this event.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `tool_use_id: String`

    The id of the `agent.tool_use` event this result corresponds to.

  - `type: :"agent.tool_result"`

    - `:"agent.tool_result"`

  - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock`

      Regular text content.

      - `text: String`

        The text content.

      - `type: :text`

        - `:text`

    - `class BetaManagedAgentsImageBlock`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource`

          Base64-encoded image data.

          - `data: String`

            Base64-encoded image data.

          - `media_type: String`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: :base64`

            - `:base64`

        - `class BetaManagedAgentsURLImageSource`

          Image referenced by URL.

          - `type: :url`

            - `:url`

          - `url: String`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource`

          Image referenced by file ID.

          - `file_id: String`

            ID of a previously uploaded file.

          - `type: :file`

            - `:file`

      - `type: :image`

        - `:image`

    - `class BetaManagedAgentsDocumentBlock`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource`

          Base64-encoded document data.

          - `data: String`

            Base64-encoded document data.

          - `media_type: String`

            MIME type of the document (e.g., "application/pdf").

          - `type: :base64`

            - `:base64`

        - `class BetaManagedAgentsPlainTextDocumentSource`

          Plain text document content.

          - `data: String`

            The plain text content.

          - `media_type: :"text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `:"text/plain"`

          - `type: :text`

            - `:text`

        - `class BetaManagedAgentsURLDocumentSource`

          Document referenced by URL.

          - `type: :url`

            - `:url`

          - `url: String`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource`

          Document referenced by file ID.

          - `file_id: String`

            ID of a previously uploaded file.

          - `type: :file`

            - `:file`

      - `type: :document`

        - `:document`

      - `context: String`

        Additional context about the document for the model.

      - `title: String`

        The title of the document.

  - `is_error: bool`

    Whether the tool execution resulted in an error.

### Beta Managed Agents Agent Tool Use Event

- `class BetaManagedAgentsAgentToolUseEvent`

  Event emitted when the agent invokes a built-in agent tool.

  - `id: String`

    Unique identifier for this event.

  - `input: Hash[Symbol, untyped]`

    Input parameters for the tool call.

  - `name: String`

    Name of the agent tool being used.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"agent.tool_use"`

    - `:"agent.tool_use"`

  - `evaluated_permission: :allow | :ask | :deny`

    AgentEvaluatedPermission enum

    - `:allow`

    - `:ask`

    - `:deny`

### Beta Managed Agents Base64 Document Source

- `class BetaManagedAgentsBase64DocumentSource`

  Base64-encoded document data.

  - `data: String`

    Base64-encoded document data.

  - `media_type: String`

    MIME type of the document (e.g., "application/pdf").

  - `type: :base64`

    - `:base64`

### Beta Managed Agents Base64 Image Source

- `class BetaManagedAgentsBase64ImageSource`

  Base64-encoded image data.

  - `data: String`

    Base64-encoded image data.

  - `media_type: String`

    MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

  - `type: :base64`

    - `:base64`

### Beta Managed Agents Billing Error

- `class BetaManagedAgentsBillingError`

  The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

  - `message: String`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: :retrying`

        - `:retrying`

    - `class BetaManagedAgentsRetryStatusExhausted`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: :exhausted`

        - `:exhausted`

    - `class BetaManagedAgentsRetryStatusTerminal`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: :terminal`

        - `:terminal`

  - `type: :billing_error`

    - `:billing_error`

### Beta Managed Agents Document Block

- `class BetaManagedAgentsDocumentBlock`

  Document content, either specified directly as base64 data, as text, or as a reference via a URL.

  - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

    Union type for document source variants.

    - `class BetaManagedAgentsBase64DocumentSource`

      Base64-encoded document data.

      - `data: String`

        Base64-encoded document data.

      - `media_type: String`

        MIME type of the document (e.g., "application/pdf").

      - `type: :base64`

        - `:base64`

    - `class BetaManagedAgentsPlainTextDocumentSource`

      Plain text document content.

      - `data: String`

        The plain text content.

      - `media_type: :"text/plain"`

        MIME type of the text content. Must be "text/plain".

        - `:"text/plain"`

      - `type: :text`

        - `:text`

    - `class BetaManagedAgentsURLDocumentSource`

      Document referenced by URL.

      - `type: :url`

        - `:url`

      - `url: String`

        URL of the document to fetch.

    - `class BetaManagedAgentsFileDocumentSource`

      Document referenced by file ID.

      - `file_id: String`

        ID of a previously uploaded file.

      - `type: :file`

        - `:file`

  - `type: :document`

    - `:document`

  - `context: String`

    Additional context about the document for the model.

  - `title: String`

    The title of the document.

### Beta Managed Agents Event Params

- `BetaManagedAgentsEventParams = BetaManagedAgentsUserMessageEventParams | BetaManagedAgentsUserInterruptEventParams | BetaManagedAgentsUserToolConfirmationEventParams | BetaManagedAgentsUserCustomToolResultEventParams`

  Union type for event parameters that can be sent to a session.

  - `class BetaManagedAgentsUserMessageEventParams`

    Parameters for sending a user message to the session.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `type: :"user.message"`

      - `:"user.message"`

  - `class BetaManagedAgentsUserInterruptEventParams`

    Parameters for sending an interrupt to pause the agent.

    - `type: :"user.interrupt"`

      - `:"user.interrupt"`

  - `class BetaManagedAgentsUserToolConfirmationEventParams`

    Parameters for confirming or denying a tool execution request.

    - `result: :allow | :deny`

      UserToolConfirmationResult enum

      - `:allow`

      - `:deny`

    - `tool_use_id: String`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.tool_confirmation"`

      - `:"user.tool_confirmation"`

    - `deny_message: String`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

  - `class BetaManagedAgentsUserCustomToolResultEventParams`

    Parameters for providing the result of a custom tool execution.

    - `custom_tool_use_id: String`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.custom_tool_result"`

      - `:"user.custom_tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

### Beta Managed Agents File Document Source

- `class BetaManagedAgentsFileDocumentSource`

  Document referenced by file ID.

  - `file_id: String`

    ID of a previously uploaded file.

  - `type: :file`

    - `:file`

### Beta Managed Agents File Image Source

- `class BetaManagedAgentsFileImageSource`

  Image referenced by file ID.

  - `file_id: String`

    ID of a previously uploaded file.

  - `type: :file`

    - `:file`

### Beta Managed Agents Image Block

- `class BetaManagedAgentsImageBlock`

  Image content specified directly as base64 data or as a reference via a URL.

  - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

    Union type for image source variants.

    - `class BetaManagedAgentsBase64ImageSource`

      Base64-encoded image data.

      - `data: String`

        Base64-encoded image data.

      - `media_type: String`

        MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

      - `type: :base64`

        - `:base64`

    - `class BetaManagedAgentsURLImageSource`

      Image referenced by URL.

      - `type: :url`

        - `:url`

      - `url: String`

        URL of the image to fetch.

    - `class BetaManagedAgentsFileImageSource`

      Image referenced by file ID.

      - `file_id: String`

        ID of a previously uploaded file.

      - `type: :file`

        - `:file`

  - `type: :image`

    - `:image`

### Beta Managed Agents MCP Authentication Failed Error

- `class BetaManagedAgentsMCPAuthenticationFailedError`

  Authentication to an MCP server failed.

  - `mcp_server_name: String`

    Name of the MCP server that failed authentication.

  - `message: String`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: :retrying`

        - `:retrying`

    - `class BetaManagedAgentsRetryStatusExhausted`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: :exhausted`

        - `:exhausted`

    - `class BetaManagedAgentsRetryStatusTerminal`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: :terminal`

        - `:terminal`

  - `type: :mcp_authentication_failed_error`

    - `:mcp_authentication_failed_error`

### Beta Managed Agents MCP Connection Failed Error

- `class BetaManagedAgentsMCPConnectionFailedError`

  Failed to connect to an MCP server.

  - `mcp_server_name: String`

    Name of the MCP server that failed to connect.

  - `message: String`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: :retrying`

        - `:retrying`

    - `class BetaManagedAgentsRetryStatusExhausted`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: :exhausted`

        - `:exhausted`

    - `class BetaManagedAgentsRetryStatusTerminal`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: :terminal`

        - `:terminal`

  - `type: :mcp_connection_failed_error`

    - `:mcp_connection_failed_error`

### Beta Managed Agents Model Overloaded Error

- `class BetaManagedAgentsModelOverloadedError`

  The model is currently overloaded. Emitted after automatic retries are exhausted.

  - `message: String`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: :retrying`

        - `:retrying`

    - `class BetaManagedAgentsRetryStatusExhausted`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: :exhausted`

        - `:exhausted`

    - `class BetaManagedAgentsRetryStatusTerminal`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: :terminal`

        - `:terminal`

  - `type: :model_overloaded_error`

    - `:model_overloaded_error`

### Beta Managed Agents Model Rate Limited Error

- `class BetaManagedAgentsModelRateLimitedError`

  The model request was rate-limited.

  - `message: String`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: :retrying`

        - `:retrying`

    - `class BetaManagedAgentsRetryStatusExhausted`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: :exhausted`

        - `:exhausted`

    - `class BetaManagedAgentsRetryStatusTerminal`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: :terminal`

        - `:terminal`

  - `type: :model_rate_limited_error`

    - `:model_rate_limited_error`

### Beta Managed Agents Model Request Failed Error

- `class BetaManagedAgentsModelRequestFailedError`

  A model request failed for a reason other than overload or rate-limiting.

  - `message: String`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: :retrying`

        - `:retrying`

    - `class BetaManagedAgentsRetryStatusExhausted`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: :exhausted`

        - `:exhausted`

    - `class BetaManagedAgentsRetryStatusTerminal`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: :terminal`

        - `:terminal`

  - `type: :model_request_failed_error`

    - `:model_request_failed_error`

### Beta Managed Agents Plain Text Document Source

- `class BetaManagedAgentsPlainTextDocumentSource`

  Plain text document content.

  - `data: String`

    The plain text content.

  - `media_type: :"text/plain"`

    MIME type of the text content. Must be "text/plain".

    - `:"text/plain"`

  - `type: :text`

    - `:text`

### Beta Managed Agents Retry Status Exhausted

- `class BetaManagedAgentsRetryStatusExhausted`

  This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

  - `type: :exhausted`

    - `:exhausted`

### Beta Managed Agents Retry Status Retrying

- `class BetaManagedAgentsRetryStatusRetrying`

  The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

  - `type: :retrying`

    - `:retrying`

### Beta Managed Agents Retry Status Terminal

- `class BetaManagedAgentsRetryStatusTerminal`

  The session encountered a terminal error and will transition to `terminated` state.

  - `type: :terminal`

    - `:terminal`

### Beta Managed Agents Send Session Events

- `class BetaManagedAgentsSendSessionEvents`

  Events that were successfully sent to the session.

  - `data: Array[BetaManagedAgentsUserMessageEvent | BetaManagedAgentsUserInterruptEvent | BetaManagedAgentsUserToolConfirmationEvent | BetaManagedAgentsUserCustomToolResultEvent]`

    Sent events

    - `class BetaManagedAgentsUserMessageEvent`

      A user message event in the session conversation.

      - `id: String`

        Unique identifier for this event.

      - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

        Array of content blocks comprising the user message.

        - `class BetaManagedAgentsTextBlock`

          Regular text content.

          - `text: String`

            The text content.

          - `type: :text`

            - `:text`

        - `class BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `data: String`

                Base64-encoded image data.

              - `media_type: String`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: :base64`

                - `:base64`

            - `class BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: :url`

                - `:url`

              - `url: String`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

              - `type: :file`

                - `:file`

          - `type: :image`

            - `:image`

        - `class BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `data: String`

                Base64-encoded document data.

              - `media_type: String`

                MIME type of the document (e.g., "application/pdf").

              - `type: :base64`

                - `:base64`

            - `class BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `data: String`

                The plain text content.

              - `media_type: :"text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `:"text/plain"`

              - `type: :text`

                - `:text`

            - `class BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: :url`

                - `:url`

              - `url: String`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

              - `type: :file`

                - `:file`

          - `type: :document`

            - `:document`

          - `context: String`

            Additional context about the document for the model.

          - `title: String`

            The title of the document.

      - `type: :"user.message"`

        - `:"user.message"`

      - `processed_at: Time`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserInterruptEvent`

      An interrupt event that pauses agent execution and returns control to the user.

      - `id: String`

        Unique identifier for this event.

      - `type: :"user.interrupt"`

        - `:"user.interrupt"`

      - `processed_at: Time`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserToolConfirmationEvent`

      A tool confirmation event that approves or denies a pending tool execution.

      - `id: String`

        Unique identifier for this event.

      - `result: :allow | :deny`

        UserToolConfirmationResult enum

        - `:allow`

        - `:deny`

      - `tool_use_id: String`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: :"user.tool_confirmation"`

        - `:"user.tool_confirmation"`

      - `deny_message: String`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      - `processed_at: Time`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserCustomToolResultEvent`

      Event sent by the client providing the result of a custom tool execution.

      - `id: String`

        Unique identifier for this event.

      - `custom_tool_use_id: String`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: :"user.custom_tool_result"`

        - `:"user.custom_tool_result"`

      - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock`

          Regular text content.

          - `text: String`

            The text content.

          - `type: :text`

            - `:text`

        - `class BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `data: String`

                Base64-encoded image data.

              - `media_type: String`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: :base64`

                - `:base64`

            - `class BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: :url`

                - `:url`

              - `url: String`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

              - `type: :file`

                - `:file`

          - `type: :image`

            - `:image`

        - `class BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `data: String`

                Base64-encoded document data.

              - `media_type: String`

                MIME type of the document (e.g., "application/pdf").

              - `type: :base64`

                - `:base64`

            - `class BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `data: String`

                The plain text content.

              - `media_type: :"text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `:"text/plain"`

              - `type: :text`

                - `:text`

            - `class BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: :url`

                - `:url`

              - `url: String`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

              - `type: :file`

                - `:file`

          - `type: :document`

            - `:document`

          - `context: String`

            Additional context about the document for the model.

          - `title: String`

            The title of the document.

      - `is_error: bool`

        Whether the tool execution resulted in an error.

      - `processed_at: Time`

        A timestamp in RFC 3339 format

### Beta Managed Agents Session Deleted Event

- `class BetaManagedAgentsSessionDeletedEvent`

  Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

  - `id: String`

    Unique identifier for this event.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"session.deleted"`

    - `:"session.deleted"`

### Beta Managed Agents Session End Turn

- `class BetaManagedAgentsSessionEndTurn`

  The agent completed its turn naturally and is ready for the next user message.

  - `type: :end_turn`

    - `:end_turn`

### Beta Managed Agents Session Error Event

- `class BetaManagedAgentsSessionErrorEvent`

  An error event indicating a problem occurred during session execution.

  - `id: String`

    Unique identifier for this event.

  - `error: BetaManagedAgentsUnknownError | BetaManagedAgentsModelOverloadedError | BetaManagedAgentsModelRateLimitedError | 4 more`

    An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

    - `class BetaManagedAgentsUnknownError`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `message: String`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: :retrying`

            - `:retrying`

        - `class BetaManagedAgentsRetryStatusExhausted`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: :exhausted`

            - `:exhausted`

        - `class BetaManagedAgentsRetryStatusTerminal`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: :terminal`

            - `:terminal`

      - `type: :unknown_error`

        - `:unknown_error`

    - `class BetaManagedAgentsModelOverloadedError`

      The model is currently overloaded. Emitted after automatic retries are exhausted.

      - `message: String`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: :retrying`

            - `:retrying`

        - `class BetaManagedAgentsRetryStatusExhausted`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: :exhausted`

            - `:exhausted`

        - `class BetaManagedAgentsRetryStatusTerminal`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: :terminal`

            - `:terminal`

      - `type: :model_overloaded_error`

        - `:model_overloaded_error`

    - `class BetaManagedAgentsModelRateLimitedError`

      The model request was rate-limited.

      - `message: String`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: :retrying`

            - `:retrying`

        - `class BetaManagedAgentsRetryStatusExhausted`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: :exhausted`

            - `:exhausted`

        - `class BetaManagedAgentsRetryStatusTerminal`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: :terminal`

            - `:terminal`

      - `type: :model_rate_limited_error`

        - `:model_rate_limited_error`

    - `class BetaManagedAgentsModelRequestFailedError`

      A model request failed for a reason other than overload or rate-limiting.

      - `message: String`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: :retrying`

            - `:retrying`

        - `class BetaManagedAgentsRetryStatusExhausted`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: :exhausted`

            - `:exhausted`

        - `class BetaManagedAgentsRetryStatusTerminal`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: :terminal`

            - `:terminal`

      - `type: :model_request_failed_error`

        - `:model_request_failed_error`

    - `class BetaManagedAgentsMCPConnectionFailedError`

      Failed to connect to an MCP server.

      - `mcp_server_name: String`

        Name of the MCP server that failed to connect.

      - `message: String`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: :retrying`

            - `:retrying`

        - `class BetaManagedAgentsRetryStatusExhausted`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: :exhausted`

            - `:exhausted`

        - `class BetaManagedAgentsRetryStatusTerminal`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: :terminal`

            - `:terminal`

      - `type: :mcp_connection_failed_error`

        - `:mcp_connection_failed_error`

    - `class BetaManagedAgentsMCPAuthenticationFailedError`

      Authentication to an MCP server failed.

      - `mcp_server_name: String`

        Name of the MCP server that failed authentication.

      - `message: String`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: :retrying`

            - `:retrying`

        - `class BetaManagedAgentsRetryStatusExhausted`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: :exhausted`

            - `:exhausted`

        - `class BetaManagedAgentsRetryStatusTerminal`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: :terminal`

            - `:terminal`

      - `type: :mcp_authentication_failed_error`

        - `:mcp_authentication_failed_error`

    - `class BetaManagedAgentsBillingError`

      The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

      - `message: String`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: :retrying`

            - `:retrying`

        - `class BetaManagedAgentsRetryStatusExhausted`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: :exhausted`

            - `:exhausted`

        - `class BetaManagedAgentsRetryStatusTerminal`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: :terminal`

            - `:terminal`

      - `type: :billing_error`

        - `:billing_error`

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"session.error"`

    - `:"session.error"`

### Beta Managed Agents Session Event

- `BetaManagedAgentsSessionEvent = BetaManagedAgentsUserMessageEvent | BetaManagedAgentsUserInterruptEvent | BetaManagedAgentsUserToolConfirmationEvent | 17 more`

  Union type for all event types in a session.

  - `class BetaManagedAgentsUserMessageEvent`

    A user message event in the session conversation.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `type: :"user.message"`

      - `:"user.message"`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: String`

      Unique identifier for this event.

    - `type: :"user.interrupt"`

      - `:"user.interrupt"`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserToolConfirmationEvent`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: String`

      Unique identifier for this event.

    - `result: :allow | :deny`

      UserToolConfirmationResult enum

      - `:allow`

      - `:deny`

    - `tool_use_id: String`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.tool_confirmation"`

      - `:"user.tool_confirmation"`

    - `deny_message: String`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserCustomToolResultEvent`

    Event sent by the client providing the result of a custom tool execution.

    - `id: String`

      Unique identifier for this event.

    - `custom_tool_use_id: String`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.custom_tool_result"`

      - `:"user.custom_tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsAgentCustomToolUseEvent`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `name: String`

      Name of the custom tool being called.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.custom_tool_use"`

      - `:"agent.custom_tool_use"`

  - `class BetaManagedAgentsAgentMessageEvent`

    An agent response event in the session conversation.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock]`

      Array of text blocks comprising the agent response.

      - `text: String`

        The text content.

      - `type: :text`

        - `:text`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.message"`

      - `:"agent.message"`

  - `class BetaManagedAgentsAgentThinkingEvent`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.thinking"`

      - `:"agent.thinking"`

  - `class BetaManagedAgentsAgentMCPToolUseEvent`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `mcp_server_name: String`

      Name of the MCP server providing the tool.

    - `name: String`

      Name of the MCP tool being used.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.mcp_tool_use"`

      - `:"agent.mcp_tool_use"`

    - `evaluated_permission: :allow | :ask | :deny`

      AgentEvaluatedPermission enum

      - `:allow`

      - `:ask`

      - `:deny`

  - `class BetaManagedAgentsAgentMCPToolResultEvent`

    Event representing the result of an MCP tool execution.

    - `id: String`

      Unique identifier for this event.

    - `mcp_tool_use_id: String`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.mcp_tool_result"`

      - `:"agent.mcp_tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `name: String`

      Name of the agent tool being used.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.tool_use"`

      - `:"agent.tool_use"`

    - `evaluated_permission: :allow | :ask | :deny`

      AgentEvaluatedPermission enum

      - `:allow`

      - `:ask`

      - `:deny`

  - `class BetaManagedAgentsAgentToolResultEvent`

    Event representing the result of an agent tool execution.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `tool_use_id: String`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: :"agent.tool_result"`

      - `:"agent.tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.thread_context_compacted"`

      - `:"agent.thread_context_compacted"`

  - `class BetaManagedAgentsSessionErrorEvent`

    An error event indicating a problem occurred during session execution.

    - `id: String`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError | BetaManagedAgentsModelOverloadedError | BetaManagedAgentsModelRateLimitedError | 4 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :unknown_error`

          - `:unknown_error`

      - `class BetaManagedAgentsModelOverloadedError`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :model_overloaded_error`

          - `:model_overloaded_error`

      - `class BetaManagedAgentsModelRateLimitedError`

        The model request was rate-limited.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :model_rate_limited_error`

          - `:model_rate_limited_error`

      - `class BetaManagedAgentsModelRequestFailedError`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :model_request_failed_error`

          - `:model_request_failed_error`

      - `class BetaManagedAgentsMCPConnectionFailedError`

        Failed to connect to an MCP server.

        - `mcp_server_name: String`

          Name of the MCP server that failed to connect.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :mcp_connection_failed_error`

          - `:mcp_connection_failed_error`

      - `class BetaManagedAgentsMCPAuthenticationFailedError`

        Authentication to an MCP server failed.

        - `mcp_server_name: String`

          Name of the MCP server that failed authentication.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :mcp_authentication_failed_error`

          - `:mcp_authentication_failed_error`

      - `class BetaManagedAgentsBillingError`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :billing_error`

          - `:billing_error`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.error"`

      - `:"session.error"`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.status_rescheduled"`

      - `:"session.status_rescheduled"`

  - `class BetaManagedAgentsSessionStatusRunningEvent`

    Indicates the session is actively running and the agent is working.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.status_running"`

      - `:"session.status_running"`

  - `class BetaManagedAgentsSessionStatusIdleEvent`

    Indicates the agent has paused and is awaiting user input.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: :end_turn`

          - `:end_turn`

      - `class BetaManagedAgentsSessionRequiresAction`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: Array[String]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: :requires_action`

          - `:requires_action`

      - `class BetaManagedAgentsSessionRetriesExhausted`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `type: :retries_exhausted`

          - `:retries_exhausted`

    - `type: :"session.status_idle"`

      - `:"session.status_idle"`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent`

    Indicates the session has terminated, either due to an error or completion.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.status_terminated"`

      - `:"session.status_terminated"`

  - `class BetaManagedAgentsSpanModelRequestStartEvent`

    Emitted when a model request is initiated by the agent.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"span.model_request_start"`

      - `:"span.model_request_start"`

  - `class BetaManagedAgentsSpanModelRequestEndEvent`

    Emitted when a model request completes.

    - `id: String`

      Unique identifier for this event.

    - `is_error: bool`

      Whether the model request resulted in an error.

    - `model_request_start_id: String`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: Integer`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: Integer`

        Tokens read from prompt cache in this request.

      - `input_tokens: Integer`

        Input tokens consumed by this request.

      - `output_tokens: Integer`

        Output tokens generated by this request.

      - `speed: :standard | :fast`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `:standard`

        - `:fast`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"span.model_request_end"`

      - `:"span.model_request_end"`

  - `class BetaManagedAgentsSessionDeletedEvent`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.deleted"`

      - `:"session.deleted"`

### Beta Managed Agents Session Requires Action

- `class BetaManagedAgentsSessionRequiresAction`

  The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

  - `event_ids: Array[String]`

    The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

  - `type: :requires_action`

    - `:requires_action`

### Beta Managed Agents Session Retries Exhausted

- `class BetaManagedAgentsSessionRetriesExhausted`

  The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

  - `type: :retries_exhausted`

    - `:retries_exhausted`

### Beta Managed Agents Session Status Idle Event

- `class BetaManagedAgentsSessionStatusIdleEvent`

  Indicates the agent has paused and is awaiting user input.

  - `id: String`

    Unique identifier for this event.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted`

    The agent completed its turn naturally and is ready for the next user message.

    - `class BetaManagedAgentsSessionEndTurn`

      The agent completed its turn naturally and is ready for the next user message.

      - `type: :end_turn`

        - `:end_turn`

    - `class BetaManagedAgentsSessionRequiresAction`

      The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `event_ids: Array[String]`

        The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

      - `type: :requires_action`

        - `:requires_action`

    - `class BetaManagedAgentsSessionRetriesExhausted`

      The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

      - `type: :retries_exhausted`

        - `:retries_exhausted`

  - `type: :"session.status_idle"`

    - `:"session.status_idle"`

### Beta Managed Agents Session Status Rescheduled Event

- `class BetaManagedAgentsSessionStatusRescheduledEvent`

  Indicates the session is recovering from an error state and is rescheduled for execution.

  - `id: String`

    Unique identifier for this event.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"session.status_rescheduled"`

    - `:"session.status_rescheduled"`

### Beta Managed Agents Session Status Running Event

- `class BetaManagedAgentsSessionStatusRunningEvent`

  Indicates the session is actively running and the agent is working.

  - `id: String`

    Unique identifier for this event.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"session.status_running"`

    - `:"session.status_running"`

### Beta Managed Agents Session Status Terminated Event

- `class BetaManagedAgentsSessionStatusTerminatedEvent`

  Indicates the session has terminated, either due to an error or completion.

  - `id: String`

    Unique identifier for this event.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"session.status_terminated"`

    - `:"session.status_terminated"`

### Beta Managed Agents Span Model Request End Event

- `class BetaManagedAgentsSpanModelRequestEndEvent`

  Emitted when a model request completes.

  - `id: String`

    Unique identifier for this event.

  - `is_error: bool`

    Whether the model request resulted in an error.

  - `model_request_start_id: String`

    The id of the corresponding `span.model_request_start` event.

  - `model_usage: BetaManagedAgentsSpanModelUsage`

    Token usage for a single model request.

    - `cache_creation_input_tokens: Integer`

      Tokens used to create prompt cache in this request.

    - `cache_read_input_tokens: Integer`

      Tokens read from prompt cache in this request.

    - `input_tokens: Integer`

      Input tokens consumed by this request.

    - `output_tokens: Integer`

      Output tokens generated by this request.

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"span.model_request_end"`

    - `:"span.model_request_end"`

### Beta Managed Agents Span Model Request Start Event

- `class BetaManagedAgentsSpanModelRequestStartEvent`

  Emitted when a model request is initiated by the agent.

  - `id: String`

    Unique identifier for this event.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"span.model_request_start"`

    - `:"span.model_request_start"`

### Beta Managed Agents Span Model Usage

- `class BetaManagedAgentsSpanModelUsage`

  Token usage for a single model request.

  - `cache_creation_input_tokens: Integer`

    Tokens used to create prompt cache in this request.

  - `cache_read_input_tokens: Integer`

    Tokens read from prompt cache in this request.

  - `input_tokens: Integer`

    Input tokens consumed by this request.

  - `output_tokens: Integer`

    Output tokens generated by this request.

  - `speed: :standard | :fast`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `:standard`

    - `:fast`

### Beta Managed Agents Stream Session Events

- `BetaManagedAgentsStreamSessionEvents = BetaManagedAgentsUserMessageEvent | BetaManagedAgentsUserInterruptEvent | BetaManagedAgentsUserToolConfirmationEvent | 17 more`

  Server-sent event in the session stream.

  - `class BetaManagedAgentsUserMessageEvent`

    A user message event in the session conversation.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `type: :"user.message"`

      - `:"user.message"`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: String`

      Unique identifier for this event.

    - `type: :"user.interrupt"`

      - `:"user.interrupt"`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserToolConfirmationEvent`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: String`

      Unique identifier for this event.

    - `result: :allow | :deny`

      UserToolConfirmationResult enum

      - `:allow`

      - `:deny`

    - `tool_use_id: String`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.tool_confirmation"`

      - `:"user.tool_confirmation"`

    - `deny_message: String`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserCustomToolResultEvent`

    Event sent by the client providing the result of a custom tool execution.

    - `id: String`

      Unique identifier for this event.

    - `custom_tool_use_id: String`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.custom_tool_result"`

      - `:"user.custom_tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsAgentCustomToolUseEvent`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `name: String`

      Name of the custom tool being called.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.custom_tool_use"`

      - `:"agent.custom_tool_use"`

  - `class BetaManagedAgentsAgentMessageEvent`

    An agent response event in the session conversation.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock]`

      Array of text blocks comprising the agent response.

      - `text: String`

        The text content.

      - `type: :text`

        - `:text`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.message"`

      - `:"agent.message"`

  - `class BetaManagedAgentsAgentThinkingEvent`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.thinking"`

      - `:"agent.thinking"`

  - `class BetaManagedAgentsAgentMCPToolUseEvent`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `mcp_server_name: String`

      Name of the MCP server providing the tool.

    - `name: String`

      Name of the MCP tool being used.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.mcp_tool_use"`

      - `:"agent.mcp_tool_use"`

    - `evaluated_permission: :allow | :ask | :deny`

      AgentEvaluatedPermission enum

      - `:allow`

      - `:ask`

      - `:deny`

  - `class BetaManagedAgentsAgentMCPToolResultEvent`

    Event representing the result of an MCP tool execution.

    - `id: String`

      Unique identifier for this event.

    - `mcp_tool_use_id: String`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.mcp_tool_result"`

      - `:"agent.mcp_tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `name: String`

      Name of the agent tool being used.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.tool_use"`

      - `:"agent.tool_use"`

    - `evaluated_permission: :allow | :ask | :deny`

      AgentEvaluatedPermission enum

      - `:allow`

      - `:ask`

      - `:deny`

  - `class BetaManagedAgentsAgentToolResultEvent`

    Event representing the result of an agent tool execution.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `tool_use_id: String`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: :"agent.tool_result"`

      - `:"agent.tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.thread_context_compacted"`

      - `:"agent.thread_context_compacted"`

  - `class BetaManagedAgentsSessionErrorEvent`

    An error event indicating a problem occurred during session execution.

    - `id: String`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError | BetaManagedAgentsModelOverloadedError | BetaManagedAgentsModelRateLimitedError | 4 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :unknown_error`

          - `:unknown_error`

      - `class BetaManagedAgentsModelOverloadedError`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :model_overloaded_error`

          - `:model_overloaded_error`

      - `class BetaManagedAgentsModelRateLimitedError`

        The model request was rate-limited.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :model_rate_limited_error`

          - `:model_rate_limited_error`

      - `class BetaManagedAgentsModelRequestFailedError`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :model_request_failed_error`

          - `:model_request_failed_error`

      - `class BetaManagedAgentsMCPConnectionFailedError`

        Failed to connect to an MCP server.

        - `mcp_server_name: String`

          Name of the MCP server that failed to connect.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :mcp_connection_failed_error`

          - `:mcp_connection_failed_error`

      - `class BetaManagedAgentsMCPAuthenticationFailedError`

        Authentication to an MCP server failed.

        - `mcp_server_name: String`

          Name of the MCP server that failed authentication.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :mcp_authentication_failed_error`

          - `:mcp_authentication_failed_error`

      - `class BetaManagedAgentsBillingError`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :billing_error`

          - `:billing_error`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.error"`

      - `:"session.error"`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.status_rescheduled"`

      - `:"session.status_rescheduled"`

  - `class BetaManagedAgentsSessionStatusRunningEvent`

    Indicates the session is actively running and the agent is working.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.status_running"`

      - `:"session.status_running"`

  - `class BetaManagedAgentsSessionStatusIdleEvent`

    Indicates the agent has paused and is awaiting user input.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: :end_turn`

          - `:end_turn`

      - `class BetaManagedAgentsSessionRequiresAction`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: Array[String]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: :requires_action`

          - `:requires_action`

      - `class BetaManagedAgentsSessionRetriesExhausted`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `type: :retries_exhausted`

          - `:retries_exhausted`

    - `type: :"session.status_idle"`

      - `:"session.status_idle"`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent`

    Indicates the session has terminated, either due to an error or completion.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.status_terminated"`

      - `:"session.status_terminated"`

  - `class BetaManagedAgentsSpanModelRequestStartEvent`

    Emitted when a model request is initiated by the agent.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"span.model_request_start"`

      - `:"span.model_request_start"`

  - `class BetaManagedAgentsSpanModelRequestEndEvent`

    Emitted when a model request completes.

    - `id: String`

      Unique identifier for this event.

    - `is_error: bool`

      Whether the model request resulted in an error.

    - `model_request_start_id: String`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: Integer`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: Integer`

        Tokens read from prompt cache in this request.

      - `input_tokens: Integer`

        Input tokens consumed by this request.

      - `output_tokens: Integer`

        Output tokens generated by this request.

      - `speed: :standard | :fast`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `:standard`

        - `:fast`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"span.model_request_end"`

      - `:"span.model_request_end"`

  - `class BetaManagedAgentsSessionDeletedEvent`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.deleted"`

      - `:"session.deleted"`

### Beta Managed Agents Text Block

- `class BetaManagedAgentsTextBlock`

  Regular text content.

  - `text: String`

    The text content.

  - `type: :text`

    - `:text`

### Beta Managed Agents Unknown Error

- `class BetaManagedAgentsUnknownError`

  An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

  - `message: String`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: :retrying`

        - `:retrying`

    - `class BetaManagedAgentsRetryStatusExhausted`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: :exhausted`

        - `:exhausted`

    - `class BetaManagedAgentsRetryStatusTerminal`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: :terminal`

        - `:terminal`

  - `type: :unknown_error`

    - `:unknown_error`

### Beta Managed Agents URL Document Source

- `class BetaManagedAgentsURLDocumentSource`

  Document referenced by URL.

  - `type: :url`

    - `:url`

  - `url: String`

    URL of the document to fetch.

### Beta Managed Agents URL Image Source

- `class BetaManagedAgentsURLImageSource`

  Image referenced by URL.

  - `type: :url`

    - `:url`

  - `url: String`

    URL of the image to fetch.

### Beta Managed Agents User Custom Tool Result Event

- `class BetaManagedAgentsUserCustomToolResultEvent`

  Event sent by the client providing the result of a custom tool execution.

  - `id: String`

    Unique identifier for this event.

  - `custom_tool_use_id: String`

    The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `type: :"user.custom_tool_result"`

    - `:"user.custom_tool_result"`

  - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock`

      Regular text content.

      - `text: String`

        The text content.

      - `type: :text`

        - `:text`

    - `class BetaManagedAgentsImageBlock`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource`

          Base64-encoded image data.

          - `data: String`

            Base64-encoded image data.

          - `media_type: String`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: :base64`

            - `:base64`

        - `class BetaManagedAgentsURLImageSource`

          Image referenced by URL.

          - `type: :url`

            - `:url`

          - `url: String`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource`

          Image referenced by file ID.

          - `file_id: String`

            ID of a previously uploaded file.

          - `type: :file`

            - `:file`

      - `type: :image`

        - `:image`

    - `class BetaManagedAgentsDocumentBlock`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource`

          Base64-encoded document data.

          - `data: String`

            Base64-encoded document data.

          - `media_type: String`

            MIME type of the document (e.g., "application/pdf").

          - `type: :base64`

            - `:base64`

        - `class BetaManagedAgentsPlainTextDocumentSource`

          Plain text document content.

          - `data: String`

            The plain text content.

          - `media_type: :"text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `:"text/plain"`

          - `type: :text`

            - `:text`

        - `class BetaManagedAgentsURLDocumentSource`

          Document referenced by URL.

          - `type: :url`

            - `:url`

          - `url: String`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource`

          Document referenced by file ID.

          - `file_id: String`

            ID of a previously uploaded file.

          - `type: :file`

            - `:file`

      - `type: :document`

        - `:document`

      - `context: String`

        Additional context about the document for the model.

      - `title: String`

        The title of the document.

  - `is_error: bool`

    Whether the tool execution resulted in an error.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Custom Tool Result Event Params

- `class BetaManagedAgentsUserCustomToolResultEventParams`

  Parameters for providing the result of a custom tool execution.

  - `custom_tool_use_id: String`

    The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `type: :"user.custom_tool_result"`

    - `:"user.custom_tool_result"`

  - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock`

      Regular text content.

      - `text: String`

        The text content.

      - `type: :text`

        - `:text`

    - `class BetaManagedAgentsImageBlock`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource`

          Base64-encoded image data.

          - `data: String`

            Base64-encoded image data.

          - `media_type: String`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: :base64`

            - `:base64`

        - `class BetaManagedAgentsURLImageSource`

          Image referenced by URL.

          - `type: :url`

            - `:url`

          - `url: String`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource`

          Image referenced by file ID.

          - `file_id: String`

            ID of a previously uploaded file.

          - `type: :file`

            - `:file`

      - `type: :image`

        - `:image`

    - `class BetaManagedAgentsDocumentBlock`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource`

          Base64-encoded document data.

          - `data: String`

            Base64-encoded document data.

          - `media_type: String`

            MIME type of the document (e.g., "application/pdf").

          - `type: :base64`

            - `:base64`

        - `class BetaManagedAgentsPlainTextDocumentSource`

          Plain text document content.

          - `data: String`

            The plain text content.

          - `media_type: :"text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `:"text/plain"`

          - `type: :text`

            - `:text`

        - `class BetaManagedAgentsURLDocumentSource`

          Document referenced by URL.

          - `type: :url`

            - `:url`

          - `url: String`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource`

          Document referenced by file ID.

          - `file_id: String`

            ID of a previously uploaded file.

          - `type: :file`

            - `:file`

      - `type: :document`

        - `:document`

      - `context: String`

        Additional context about the document for the model.

      - `title: String`

        The title of the document.

  - `is_error: bool`

    Whether the tool execution resulted in an error.

### Beta Managed Agents User Interrupt Event

- `class BetaManagedAgentsUserInterruptEvent`

  An interrupt event that pauses agent execution and returns control to the user.

  - `id: String`

    Unique identifier for this event.

  - `type: :"user.interrupt"`

    - `:"user.interrupt"`

  - `processed_at: Time`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Interrupt Event Params

- `class BetaManagedAgentsUserInterruptEventParams`

  Parameters for sending an interrupt to pause the agent.

  - `type: :"user.interrupt"`

    - `:"user.interrupt"`

### Beta Managed Agents User Message Event

- `class BetaManagedAgentsUserMessageEvent`

  A user message event in the session conversation.

  - `id: String`

    Unique identifier for this event.

  - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

    Array of content blocks comprising the user message.

    - `class BetaManagedAgentsTextBlock`

      Regular text content.

      - `text: String`

        The text content.

      - `type: :text`

        - `:text`

    - `class BetaManagedAgentsImageBlock`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource`

          Base64-encoded image data.

          - `data: String`

            Base64-encoded image data.

          - `media_type: String`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: :base64`

            - `:base64`

        - `class BetaManagedAgentsURLImageSource`

          Image referenced by URL.

          - `type: :url`

            - `:url`

          - `url: String`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource`

          Image referenced by file ID.

          - `file_id: String`

            ID of a previously uploaded file.

          - `type: :file`

            - `:file`

      - `type: :image`

        - `:image`

    - `class BetaManagedAgentsDocumentBlock`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource`

          Base64-encoded document data.

          - `data: String`

            Base64-encoded document data.

          - `media_type: String`

            MIME type of the document (e.g., "application/pdf").

          - `type: :base64`

            - `:base64`

        - `class BetaManagedAgentsPlainTextDocumentSource`

          Plain text document content.

          - `data: String`

            The plain text content.

          - `media_type: :"text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `:"text/plain"`

          - `type: :text`

            - `:text`

        - `class BetaManagedAgentsURLDocumentSource`

          Document referenced by URL.

          - `type: :url`

            - `:url`

          - `url: String`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource`

          Document referenced by file ID.

          - `file_id: String`

            ID of a previously uploaded file.

          - `type: :file`

            - `:file`

      - `type: :document`

        - `:document`

      - `context: String`

        Additional context about the document for the model.

      - `title: String`

        The title of the document.

  - `type: :"user.message"`

    - `:"user.message"`

  - `processed_at: Time`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Message Event Params

- `class BetaManagedAgentsUserMessageEventParams`

  Parameters for sending a user message to the session.

  - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

    Array of content blocks for the user message.

    - `class BetaManagedAgentsTextBlock`

      Regular text content.

      - `text: String`

        The text content.

      - `type: :text`

        - `:text`

    - `class BetaManagedAgentsImageBlock`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource`

          Base64-encoded image data.

          - `data: String`

            Base64-encoded image data.

          - `media_type: String`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: :base64`

            - `:base64`

        - `class BetaManagedAgentsURLImageSource`

          Image referenced by URL.

          - `type: :url`

            - `:url`

          - `url: String`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource`

          Image referenced by file ID.

          - `file_id: String`

            ID of a previously uploaded file.

          - `type: :file`

            - `:file`

      - `type: :image`

        - `:image`

    - `class BetaManagedAgentsDocumentBlock`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource`

          Base64-encoded document data.

          - `data: String`

            Base64-encoded document data.

          - `media_type: String`

            MIME type of the document (e.g., "application/pdf").

          - `type: :base64`

            - `:base64`

        - `class BetaManagedAgentsPlainTextDocumentSource`

          Plain text document content.

          - `data: String`

            The plain text content.

          - `media_type: :"text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `:"text/plain"`

          - `type: :text`

            - `:text`

        - `class BetaManagedAgentsURLDocumentSource`

          Document referenced by URL.

          - `type: :url`

            - `:url`

          - `url: String`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource`

          Document referenced by file ID.

          - `file_id: String`

            ID of a previously uploaded file.

          - `type: :file`

            - `:file`

      - `type: :document`

        - `:document`

      - `context: String`

        Additional context about the document for the model.

      - `title: String`

        The title of the document.

  - `type: :"user.message"`

    - `:"user.message"`

### Beta Managed Agents User Tool Confirmation Event

- `class BetaManagedAgentsUserToolConfirmationEvent`

  A tool confirmation event that approves or denies a pending tool execution.

  - `id: String`

    Unique identifier for this event.

  - `result: :allow | :deny`

    UserToolConfirmationResult enum

    - `:allow`

    - `:deny`

  - `tool_use_id: String`

    The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `type: :"user.tool_confirmation"`

    - `:"user.tool_confirmation"`

  - `deny_message: String`

    Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Tool Confirmation Event Params

- `class BetaManagedAgentsUserToolConfirmationEventParams`

  Parameters for confirming or denying a tool execution request.

  - `result: :allow | :deny`

    UserToolConfirmationResult enum

    - `:allow`

    - `:deny`

  - `tool_use_id: String`

    The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `type: :"user.tool_confirmation"`

    - `:"user.tool_confirmation"`

  - `deny_message: String`

    Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

# Resources

## Add

`beta.sessions.resources.add(session_id, **kwargs) -> BetaManagedAgentsFileResource`

**post** `/v1/sessions/{session_id}/resources`

Add Session Resource

### Parameters

- `session_id: String`

- `file_id: String`

  ID of a previously uploaded file.

- `type: :file`

  - `:file`

- `mount_path: String`

  Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 18 more`

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

### Returns

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

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_file_resource = anthropic.beta.sessions.resources.add(
  "sesn_011CZkZAtmR3yMPDzynEDxu7",
  file_id: "file_011CNha8iCJcU1wXNR6q4V8w",
  type: :file
)

puts(beta_managed_agents_file_resource)
```

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

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 18 more`

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

### Returns

- `BetaManagedAgentsSessionResource = BetaManagedAgentsGitHubRepositoryResource | BetaManagedAgentsFileResource`

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

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.sessions.resources.list("sesn_011CZkZAtmR3yMPDzynEDxu7")

puts(page)
```

## Retrieve

`beta.sessions.resources.retrieve(resource_id, **kwargs) -> ResourceRetrieveResponse`

**get** `/v1/sessions/{session_id}/resources/{resource_id}`

Get Session Resource

### Parameters

- `session_id: String`

- `resource_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 18 more`

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

### Returns

- `ResourceRetrieveResponse = BetaManagedAgentsGitHubRepositoryResource | BetaManagedAgentsFileResource`

  The requested session resource.

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

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

resource = anthropic.beta.sessions.resources.retrieve(
  "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  session_id: "sesn_011CZkZAtmR3yMPDzynEDxu7"
)

puts(resource)
```

## Update

`beta.sessions.resources.update(resource_id, **kwargs) -> ResourceUpdateResponse`

**post** `/v1/sessions/{session_id}/resources/{resource_id}`

Update Session Resource

### Parameters

- `session_id: String`

- `resource_id: String`

- `authorization_token: String`

  New authorization token for the resource. Currently only `github_repository` resources support token rotation.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 18 more`

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

### Returns

- `ResourceUpdateResponse = BetaManagedAgentsGitHubRepositoryResource | BetaManagedAgentsFileResource`

  The updated session resource.

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

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

resource = anthropic.beta.sessions.resources.update(
  "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  session_id: "sesn_011CZkZAtmR3yMPDzynEDxu7",
  authorization_token: "ghp_exampletoken"
)

puts(resource)
```

## Delete

`beta.sessions.resources.delete(resource_id, **kwargs) -> BetaManagedAgentsDeleteSessionResource`

**delete** `/v1/sessions/{session_id}/resources/{resource_id}`

Delete Session Resource

### Parameters

- `session_id: String`

- `resource_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 18 more`

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

### Returns

- `class BetaManagedAgentsDeleteSessionResource`

  Confirmation of resource deletion.

  - `id: String`

  - `type: :session_resource_deleted`

    - `:session_resource_deleted`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_delete_session_resource = anthropic.beta.sessions.resources.delete(
  "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  session_id: "sesn_011CZkZAtmR3yMPDzynEDxu7"
)

puts(beta_managed_agents_delete_session_resource)
```

## Domain Types

### Beta Managed Agents Delete Session Resource

- `class BetaManagedAgentsDeleteSessionResource`

  Confirmation of resource deletion.

  - `id: String`

  - `type: :session_resource_deleted`

    - `:session_resource_deleted`

### Beta Managed Agents File Resource

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

### Beta Managed Agents GitHub Repository Resource

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

### Beta Managed Agents Session Resource

- `BetaManagedAgentsSessionResource = BetaManagedAgentsGitHubRepositoryResource | BetaManagedAgentsFileResource`

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

### Resource Retrieve Response

- `ResourceRetrieveResponse = BetaManagedAgentsGitHubRepositoryResource | BetaManagedAgentsFileResource`

  The requested session resource.

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

### Resource Update Response

- `ResourceUpdateResponse = BetaManagedAgentsGitHubRepositoryResource | BetaManagedAgentsFileResource`

  The updated session resource.

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
