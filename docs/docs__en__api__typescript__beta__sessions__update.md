## Update

`client.beta.sessions.update(stringsessionID, SessionUpdateParamsparams, RequestOptionsoptions?): BetaManagedAgentsSession`

**post** `/v1/sessions/{session_id}`

Update Session

### Parameters

- `sessionID: string`

- `params: SessionUpdateParams`

  - `agent?: BetaManagedAgentsSessionAgentUpdate`

    Body param: Mid-session agent configuration update. Only `tools` and `mcp_servers` are updatable. Full replacement: the provided array becomes the new value. To preserve existing entries, GET the session, modify the array, and POST it back.

    - `mcp_servers?: Array<BetaManagedAgentsURLMCPServerParams>`

      Replacement MCP server list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

      - `name: string`

        Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

      - `type: "url"`

        - `"url"`

      - `url: string`

        Endpoint URL for the MCP server.

    - `tools?: Array<BetaManagedAgentsAgentToolset20260401Params | BetaManagedAgentsMCPToolsetParams | BetaManagedAgentsCustomToolParams>`

      Replacement tool list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

      - `BetaManagedAgentsAgentToolset20260401Params`

        Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

        - `type: "agent_toolset_20260401"`

          - `"agent_toolset_20260401"`

        - `configs?: Array<BetaManagedAgentsAgentToolConfigParams>`

          Per-tool configuration overrides.

          - `name: "bash" | "edit" | "read" | 5 more`

            Built-in agent tool identifier.

            - `"bash"`

            - `"edit"`

            - `"read"`

            - `"write"`

            - `"glob"`

            - `"grep"`

            - `"web_fetch"`

            - `"web_search"`

          - `enabled?: boolean | null`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | null`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `default_config?: BetaManagedAgentsAgentToolsetDefaultConfigParams | null`

          Default configuration for all tools in a toolset.

          - `enabled?: boolean | null`

            Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

          - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | null`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

      - `BetaManagedAgentsMCPToolsetParams`

        Configuration for tools from an MCP server defined in `mcp_servers`.

        - `mcp_server_name: string`

          Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

        - `type: "mcp_toolset"`

          - `"mcp_toolset"`

        - `configs?: Array<BetaManagedAgentsMCPToolConfigParams>`

          Per-tool configuration overrides.

          - `name: string`

            Name of the MCP tool to configure. 1-128 characters.

          - `enabled?: boolean | null`

            Whether this tool is enabled. Overrides the `default_config` setting.

          - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | null`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `default_config?: BetaManagedAgentsMCPToolsetDefaultConfigParams | null`

          Default configuration for all tools from an MCP server.

          - `enabled?: boolean | null`

            Whether tools are enabled by default. Defaults to true if not specified.

          - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | null`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

      - `BetaManagedAgentsCustomToolParams`

        A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

        - `description: string`

          Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `properties?: Record<string, unknown> | null`

            JSON Schema properties defining the tool's input parameters.

          - `required?: Array<string>`

            List of required property names.

          - `type?: "object"`

            Must be 'object' for tool input schemas.

            - `"object"`

        - `name: string`

          Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

        - `type: "custom"`

          - `"custom"`

  - `metadata?: Record<string, string | null> | null`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve.

  - `title?: string | null`

    Body param: Human-readable session title.

  - `vault_ids?: Array<string>`

    Body param: Vault IDs (`vlt_*`) to attach to the session. Not yet supported; requests setting this field are rejected. Reserved for future use.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 22 more`

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

      - `"user-profiles-2026-03-24"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

### Returns

- `BetaManagedAgentsSession`

  A Managed Agents `session`.

  - `id: string`

  - `agent: BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `id: string`

    - `description: string | null`

    - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

      - `name: string`

      - `type: "url"`

        - `"url"`

      - `url: string`

    - `model: BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `"claude-opus-4-7" | "claude-opus-4-6" | "claude-sonnet-4-6" | 6 more`

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

        - `(string & {})`

      - `speed?: "standard" | "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `multiagent: BetaManagedAgentsSessionMultiagentCoordinator | null`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `agents: Array<BetaManagedAgentsSessionThreadAgent>`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `id: string`

        - `description: string | null`

        - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

          - `name: string`

          - `type: "url"`

            - `"url"`

          - `url: string`

        - `model: BetaManagedAgentsModelConfig`

          Model identifier and configuration.

          - `id: BetaManagedAgentsModel`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `"claude-opus-4-7" | "claude-opus-4-6" | "claude-sonnet-4-6" | 6 more`

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

            - `(string & {})`

          - `speed?: "standard" | "fast"`

            Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `"standard"`

            - `"fast"`

        - `name: string`

        - `skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>`

          - `BetaManagedAgentsAnthropicSkill`

            A resolved Anthropic-managed skill.

            - `skill_id: string`

            - `type: "anthropic"`

              - `"anthropic"`

            - `version: string`

          - `BetaManagedAgentsCustomSkill`

            A resolved user-created custom skill.

            - `skill_id: string`

            - `type: "custom"`

              - `"custom"`

            - `version: string`

        - `system: string | null`

        - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

          - `BetaManagedAgentsAgentToolset20260401`

            - `configs: Array<BetaManagedAgentsAgentToolConfig>`

              - `enabled: boolean`

              - `name: "bash" | "edit" | "read" | 5 more`

                Built-in agent tool identifier.

                - `"bash"`

                - `"edit"`

                - `"read"`

                - `"write"`

                - `"glob"`

                - `"grep"`

                - `"web_fetch"`

                - `"web_search"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                  - `type: "always_allow"`

                    - `"always_allow"`

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

                  - `type: "always_ask"`

                    - `"always_ask"`

            - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

              Resolved default configuration for agent tools.

              - `enabled: boolean`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                  - `type: "always_allow"`

                    - `"always_allow"`

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

                  - `type: "always_ask"`

                    - `"always_ask"`

            - `type: "agent_toolset_20260401"`

              - `"agent_toolset_20260401"`

          - `BetaManagedAgentsMCPToolset`

            - `configs: Array<BetaManagedAgentsMCPToolConfig>`

              - `enabled: boolean`

              - `name: string`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                  - `type: "always_allow"`

                    - `"always_allow"`

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

                  - `type: "always_ask"`

                    - `"always_ask"`

            - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

              Resolved default configuration for all tools from an MCP server.

              - `enabled: boolean`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                  - `type: "always_allow"`

                    - `"always_allow"`

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

                  - `type: "always_ask"`

                    - `"always_ask"`

            - `mcp_server_name: string`

            - `type: "mcp_toolset"`

              - `"mcp_toolset"`

          - `BetaManagedAgentsCustomTool`

            A custom tool as returned in API responses.

            - `description: string`

            - `input_schema: BetaManagedAgentsCustomToolInputSchema`

              JSON Schema for custom tool input parameters.

              - `properties?: Record<string, unknown> | null`

                JSON Schema properties defining the tool's input parameters.

              - `required?: Array<string>`

                List of required property names.

              - `type?: "object"`

                Must be 'object' for tool input schemas.

                - `"object"`

            - `name: string`

            - `type: "custom"`

              - `"custom"`

        - `type: "agent"`

          - `"agent"`

        - `version: number`

      - `type: "coordinator"`

        - `"coordinator"`

    - `name: string`

    - `skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>`

      - `BetaManagedAgentsAnthropicSkill`

        A resolved Anthropic-managed skill.

        - `skill_id: string`

        - `type: "anthropic"`

          - `"anthropic"`

        - `version: string`

      - `BetaManagedAgentsCustomSkill`

        A resolved user-created custom skill.

        - `skill_id: string`

        - `type: "custom"`

          - `"custom"`

        - `version: string`

    - `system: string | null`

    - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

      - `BetaManagedAgentsAgentToolset20260401`

        - `configs: Array<BetaManagedAgentsAgentToolConfig>`

          - `enabled: boolean`

          - `name: "bash" | "edit" | "read" | 5 more`

            Built-in agent tool identifier.

            - `"bash"`

            - `"edit"`

            - `"read"`

            - `"write"`

            - `"glob"`

            - `"grep"`

            - `"web_fetch"`

            - `"web_search"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

          Resolved default configuration for agent tools.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `type: "agent_toolset_20260401"`

          - `"agent_toolset_20260401"`

      - `BetaManagedAgentsMCPToolset`

        - `configs: Array<BetaManagedAgentsMCPToolConfig>`

          - `enabled: boolean`

          - `name: string`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

        - `mcp_server_name: string`

        - `type: "mcp_toolset"`

          - `"mcp_toolset"`

      - `BetaManagedAgentsCustomTool`

        A custom tool as returned in API responses.

        - `description: string`

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `properties?: Record<string, unknown> | null`

            JSON Schema properties defining the tool's input parameters.

          - `required?: Array<string>`

            List of required property names.

          - `type?: "object"`

            Must be 'object' for tool input schemas.

            - `"object"`

        - `name: string`

        - `type: "custom"`

          - `"custom"`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `environment_id: string`

  - `metadata: Record<string, string>`

  - `outcome_evaluations: Array<BetaManagedAgentsOutcomeEvaluationResource>`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

    - `completed_at: string | null`

      A timestamp in RFC 3339 format

    - `description: string`

      What the agent should produce.

    - `explanation: string | null`

      Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

    - `iteration: number`

      0-indexed revision cycle the outcome is currently on.

    - `outcome_id: string`

      Server-generated outc_ ID for this outcome.

    - `result: string`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `type: "outcome_evaluation"`

      - `"outcome_evaluation"`

  - `resources: Array<BetaManagedAgentsSessionResource>`

    - `BetaManagedAgentsGitHubRepositoryResource`

      - `id: string`

      - `created_at: string`

        A timestamp in RFC 3339 format

      - `mount_path: string`

      - `type: "github_repository"`

        - `"github_repository"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

      - `url: string`

      - `checkout?: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout | null`

        - `BetaManagedAgentsBranchCheckout`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `BetaManagedAgentsCommitCheckout`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

    - `BetaManagedAgentsFileResource`

      - `id: string`

      - `created_at: string`

        A timestamp in RFC 3339 format

      - `file_id: string`

      - `mount_path: string`

      - `type: "file"`

        - `"file"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

    - `BetaManagedAgentsMemoryStoreResource`

      A memory store attached to an agent session.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access?: "read_write" | "read_only" | null`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `description?: string`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `instructions?: string | null`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      - `mount_path?: string | null`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `name?: string | null`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `stats: BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `active_seconds?: number`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

    - `duration_seconds?: number`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

  - `status: "rescheduling" | "running" | "idle" | "terminated"`

    SessionStatus enum

    - `"rescheduling"`

    - `"running"`

    - `"idle"`

    - `"terminated"`

  - `title: string | null`

  - `type: "session"`

    - `"session"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `usage: BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

    - `cache_creation?: BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens?: number`

        Tokens used to create 1-hour ephemeral cache entries.

      - `ephemeral_5m_input_tokens?: number`

        Tokens used to create 5-minute ephemeral cache entries.

    - `cache_read_input_tokens?: number`

      Total tokens read from prompt cache.

    - `input_tokens?: number`

      Total input tokens consumed across all turns.

    - `output_tokens?: number`

      Total output tokens generated across all turns.

  - `vault_ids: Array<string>`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsSession = await client.beta.sessions.update('sesn_011CZkZAtmR3yMPDzynEDxu7');

console.log(betaManagedAgentsSession.id);
```
