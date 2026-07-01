## List Agents

`beta.agents.list(**kwargs) -> PageCursor<BetaManagedAgentsAgent>`

**get** `/v1/agents`

List Agents

### Parameters

- `created_at_gte: Time`

  Return agents created at or after this time (inclusive).

- `created_at_lte: Time`

  Return agents created at or before this time (inclusive).

- `include_archived: bool`

  Include archived agents in results. Defaults to false.

- `limit: Integer`

  Maximum results per page. Default 20, maximum 100.

- `page: String`

  Opaque pagination cursor from a previous response.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 25 more`

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

    - `:"server-side-fallback-2026-06-01"`

    - `:"fallback-credit-2026-06-01"`

### Returns

- `class BetaManagedAgentsAgent`

  A Managed Agents `agent`.

  - `id: String`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `description: String`

  - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

    - `name: String`

    - `type: :url`

      - `:url`

    - `url: String`

  - `metadata: Hash[Symbol, String]`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-4-8" | 9 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-sonnet-5"`

          High-performance model for coding and agents

        - `:"claude-fable-5"`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `:"claude-opus-4-8"`

          Frontier intelligence for long-running agents and coding

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

  - `multiagent: BetaManagedAgentsMultiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: Array[BetaManagedAgentsAgentReference]`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `id: String`

      - `type: :agent`

        - `:agent`

      - `version: Integer`

    - `type: :coordinator`

      - `:coordinator`

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

        - `type: :object`

          - `:object`

        - `properties: Hash[Symbol, untyped]`

        - `required: Array[String]`

      - `name: String`

      - `type: :custom`

        - `:custom`

  - `type: :agent`

    - `:agent`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `version: Integer`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.agents.list

puts(page)
```

#### Response

```json
{
  "data": [
    {
      "id": "agent_011CZkYpogX7uDKUyvBTophP",
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "description": "A general-purpose starter agent.",
      "mcp_servers": [
        {
          "name": "example-mcp",
          "type": "url",
          "url": "https://example-server.modelcontextprotocol.io/sse"
        }
      ],
      "metadata": {
        "foo": "bar"
      },
      "model": {
        "id": "claude-sonnet-4-6",
        "speed": "standard"
      },
      "multiagent": {
        "agents": [
          {
            "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
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
      "updated_at": "2026-03-15T10:00:00Z",
      "version": 1
    }
  ],
  "next_page": "next_page"
}
```
