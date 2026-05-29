## List Sessions

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

- `memory_store_id: String`

  Filter sessions whose resources contain a memory_store with this memory store ID.

- `order: :asc | :desc`

  Sort direction for results, ordered by created_at. Defaults to desc (newest first).

  - `:asc`

  - `:desc`

- `page: String`

  Opaque pagination cursor from a previous response's next_page.

- `statuses: Array[:rescheduling | :running | :idle | :terminated]`

  Filter by session status. Repeat the parameter to match any of multiple statuses.

  - `:rescheduling`

  - `:running`

  - `:idle`

  - `:terminated`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 24 more`

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

    - `:"user-profiles-2026-03-24"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"mid-conversation-system-2026-04-07"`

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

        - `BetaManagedAgentsModel = :"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `:"claude-opus-4-7"`

            Frontier intelligence for long-running agents and coding

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

        - `String = String`

      - `speed: :standard | :fast`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `:standard`

        - `:fast`

    - `multiagent: BetaManagedAgentsSessionMultiagentCoordinator`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `agents: Array[BetaManagedAgentsSessionThreadAgent]`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `id: String`

        - `description: String`

        - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

          - `name: String`

          - `type: :url`

          - `url: String`

        - `model: BetaManagedAgentsModelConfig`

          Model identifier and configuration.

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

                - `class BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

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

                - `class BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

            - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

              Resolved default configuration for all tools from an MCP server.

              - `enabled: bool`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

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

      - `type: :coordinator`

        - `:coordinator`

    - `name: String`

    - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

      - `class BetaManagedAgentsAnthropicSkill`

        A resolved Anthropic-managed skill.

      - `class BetaManagedAgentsCustomSkill`

        A resolved user-created custom skill.

    - `system_: String`

    - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

      - `class BetaManagedAgentsAgentToolset20260401`

      - `class BetaManagedAgentsMCPToolset`

      - `class BetaManagedAgentsCustomTool`

        A custom tool as returned in API responses.

    - `type: :agent`

      - `:agent`

    - `version: Integer`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `environment_id: String`

  - `metadata: Hash[Symbol, String]`

  - `outcome_evaluations: Array[BetaManagedAgentsOutcomeEvaluationResource]`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

    - `completed_at: Time`

      A timestamp in RFC 3339 format

    - `description: String`

      What the agent should produce.

    - `explanation: String`

      Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

    - `iteration: Integer`

      0-indexed revision cycle the outcome is currently on.

    - `outcome_id: String`

      Server-generated outc_ ID for this outcome.

    - `result: String`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `type: :outcome_evaluation`

      - `:outcome_evaluation`

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

#### Response

```json
{
  "data": [
    {
      "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
      "agent": {
        "id": "agent_011CZkYpogX7uDKUyvBTophP",
        "description": "A general-purpose starter agent.",
        "mcp_servers": [
          {
            "name": "example-mcp",
            "type": "url",
            "url": "https://example-server.modelcontextprotocol.io/sse"
          }
        ],
        "model": {
          "id": "claude-sonnet-4-6",
          "speed": "standard"
        },
        "multiagent": {
          "agents": [
            {
              "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
              "description": "A focused research subagent.",
              "mcp_servers": [
                {
                  "name": "example-mcp",
                  "type": "url",
                  "url": "https://example-server.modelcontextprotocol.io/sse"
                }
              ],
              "model": {
                "id": "claude-sonnet-4-6",
                "speed": "standard"
              },
              "name": "Researcher",
              "skills": [
                {
                  "skill_id": "xlsx",
                  "type": "anthropic",
                  "version": "1"
                }
              ],
              "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
              "tools": [
                {
                  "configs": [
                    {
                      "enabled": true,
                      "name": "bash",
                      "permission_policy": {
                        "type": "always_allow"
                      }
                    }
                  ],
                  "default_config": {
                    "enabled": true,
                    "permission_policy": {
                      "type": "always_ask"
                    }
                  },
                  "type": "agent_toolset_20260401"
                }
              ],
              "type": "agent",
              "version": 1
            }
          ],
          "type": "coordinator"
        },
        "name": "My First Agent",
        "skills": [
          {
            "skill_id": "xlsx",
            "type": "anthropic",
            "version": "1"
          },
          {
            "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
            "type": "custom",
            "version": "2"
          }
        ],
        "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
        "tools": [
          {
            "configs": [
              {
                "enabled": true,
                "name": "bash",
                "permission_policy": {
                  "type": "always_allow"
                }
              }
            ],
            "default_config": {
              "enabled": true,
              "permission_policy": {
                "type": "always_ask"
              }
            },
            "type": "agent_toolset_20260401"
          }
        ],
        "type": "agent",
        "version": 1
      },
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
      "metadata": {},
      "outcome_evaluations": [
        {
          "completed_at": "2026-03-15T10:02:31Z",
          "description": "Produce a 2-page summary as summary.md",
          "explanation": "All five sections present with inline citations.",
          "iteration": 0,
          "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
          "result": "satisfied",
          "type": "outcome_evaluation"
        }
      ],
      "resources": [
        {
          "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
          "created_at": "2026-03-15T10:00:00Z",
          "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
          "mount_path": "/uploads/receipt.pdf",
          "type": "file",
          "updated_at": "2026-03-15T10:00:00Z"
        },
        {
          "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
          "created_at": "2026-03-15T10:00:00Z",
          "mount_path": "/workspace/example-repo",
          "type": "github_repository",
          "updated_at": "2026-03-15T10:00:00Z",
          "url": "https://github.com/example-org/example-repo",
          "checkout": {
            "name": "main",
            "type": "branch"
          }
        }
      ],
      "stats": {
        "active_seconds": 0,
        "duration_seconds": 0
      },
      "status": "idle",
      "title": "Order #1234 inquiry",
      "type": "session",
      "updated_at": "2026-03-15T10:00:00Z",
      "usage": {
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 0
        },
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "output_tokens": 0
      },
      "vault_ids": [
        "vlt_011CZkZDLs7fYzm1hXNPeRjv"
      ]
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```
