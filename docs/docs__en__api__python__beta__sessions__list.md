## List

`beta.sessions.list(SessionListParams**kwargs)  -> SyncPageCursor[BetaManagedAgentsSession]`

**get** `/v1/sessions`

List Sessions

### Parameters

- `agent_id: Optional[str]`

  Filter sessions created with this agent ID.

- `agent_version: Optional[int]`

  Filter by agent version. Only applies when agent_id is also set.

- `created_at_gt: Optional[Union[str, datetime]]`

  Return sessions created after this time (exclusive).

- `created_at_gte: Optional[Union[str, datetime]]`

  Return sessions created at or after this time (inclusive).

- `created_at_lt: Optional[Union[str, datetime]]`

  Return sessions created before this time (exclusive).

- `created_at_lte: Optional[Union[str, datetime]]`

  Return sessions created at or before this time (inclusive).

- `include_archived: Optional[bool]`

  When true, includes archived sessions. Default: false (exclude archived).

- `limit: Optional[int]`

  Maximum number of results to return.

- `memory_store_id: Optional[str]`

  Filter sessions whose resources contain a memory_store with this memory store ID.

- `order: Optional[Literal["asc", "desc"]]`

  Sort direction for results, ordered by created_at. Defaults to desc (newest first).

  - `"asc"`

  - `"desc"`

- `page: Optional[str]`

  Opaque pagination cursor from a previous response's next_page.

- `statuses: Optional[List[Literal["rescheduling", "running", "idle", "terminated"]]]`

  Filter by session status. Repeat the parameter to match any of multiple statuses.

  - `"rescheduling"`

  - `"running"`

  - `"idle"`

  - `"terminated"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 21 more]`

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

### Returns

- `class BetaManagedAgentsSession: …`

  A Managed Agents `session`.

  - `id: str`

  - `agent: BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `id: str`

    - `description: Optional[str]`

    - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

      - `name: str`

      - `type: Literal["url"]`

        - `"url"`

      - `url: str`

    - `model: BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `Literal["claude-opus-4-7", "claude-opus-4-6", "claude-sonnet-4-6", 6 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-6` - Most intelligent model for building agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
          - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

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

        - `str`

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `multiagent: Optional[BetaManagedAgentsSessionMultiagentCoordinator]`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `agents: List[BetaManagedAgentsSessionThreadAgent]`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `id: str`

        - `description: Optional[str]`

        - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

          - `name: str`

          - `type: Literal["url"]`

            - `"url"`

          - `url: str`

        - `model: BetaManagedAgentsModelConfig`

          Model identifier and configuration.

          - `id: BetaManagedAgentsModel`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `Literal["claude-opus-4-7", "claude-opus-4-6", "claude-sonnet-4-6", 6 more]`

              The model that will power your agent.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
              - `claude-opus-4-6` - Most intelligent model for building agents and coding
              - `claude-sonnet-4-6` - Best combination of speed and intelligence
              - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
              - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
              - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
              - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
              - `claude-sonnet-4-5` - High-performance model for agents and coding
              - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

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

            - `str`

          - `speed: Optional[Literal["standard", "fast"]]`

            Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `"standard"`

            - `"fast"`

        - `name: str`

        - `skills: List[Skill]`

          - `class BetaManagedAgentsAnthropicSkill: …`

            A resolved Anthropic-managed skill.

            - `skill_id: str`

            - `type: Literal["anthropic"]`

              - `"anthropic"`

            - `version: str`

          - `class BetaManagedAgentsCustomSkill: …`

            A resolved user-created custom skill.

            - `skill_id: str`

            - `type: Literal["custom"]`

              - `"custom"`

            - `version: str`

        - `system: Optional[str]`

        - `tools: List[Tool]`

          - `class BetaManagedAgentsAgentToolset20260401: …`

            - `configs: List[BetaManagedAgentsAgentToolConfig]`

              - `enabled: bool`

              - `name: Literal["bash", "edit", "read", 5 more]`

                Built-in agent tool identifier.

                - `"bash"`

                - `"edit"`

                - `"read"`

                - `"write"`

                - `"glob"`

                - `"grep"`

                - `"web_fetch"`

                - `"web_search"`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                  - `type: Literal["always_allow"]`

                    - `"always_allow"`

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                  - `type: Literal["always_ask"]`

                    - `"always_ask"`

            - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

              Resolved default configuration for agent tools.

              - `enabled: bool`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                  - `type: Literal["always_allow"]`

                    - `"always_allow"`

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                  - `type: Literal["always_ask"]`

                    - `"always_ask"`

            - `type: Literal["agent_toolset_20260401"]`

              - `"agent_toolset_20260401"`

          - `class BetaManagedAgentsMCPToolset: …`

            - `configs: List[BetaManagedAgentsMCPToolConfig]`

              - `enabled: bool`

              - `name: str`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                  - `type: Literal["always_allow"]`

                    - `"always_allow"`

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                  - `type: Literal["always_ask"]`

                    - `"always_ask"`

            - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

              Resolved default configuration for all tools from an MCP server.

              - `enabled: bool`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                  - `type: Literal["always_allow"]`

                    - `"always_allow"`

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                  - `type: Literal["always_ask"]`

                    - `"always_ask"`

            - `mcp_server_name: str`

            - `type: Literal["mcp_toolset"]`

              - `"mcp_toolset"`

          - `class BetaManagedAgentsCustomTool: …`

            A custom tool as returned in API responses.

            - `description: str`

            - `input_schema: BetaManagedAgentsCustomToolInputSchema`

              JSON Schema for custom tool input parameters.

              - `properties: Optional[Dict[str, object]]`

                JSON Schema properties defining the tool's input parameters.

              - `required: Optional[List[str]]`

                List of required property names.

              - `type: Optional[Literal["object"]]`

                Must be 'object' for tool input schemas.

                - `"object"`

            - `name: str`

            - `type: Literal["custom"]`

              - `"custom"`

        - `type: Literal["agent"]`

          - `"agent"`

        - `version: int`

      - `type: Literal["coordinator"]`

        - `"coordinator"`

    - `name: str`

    - `skills: List[Skill]`

      - `class BetaManagedAgentsAnthropicSkill: …`

        A resolved Anthropic-managed skill.

        - `skill_id: str`

        - `type: Literal["anthropic"]`

          - `"anthropic"`

        - `version: str`

      - `class BetaManagedAgentsCustomSkill: …`

        A resolved user-created custom skill.

        - `skill_id: str`

        - `type: Literal["custom"]`

          - `"custom"`

        - `version: str`

    - `system: Optional[str]`

    - `tools: List[Tool]`

      - `class BetaManagedAgentsAgentToolset20260401: …`

        - `configs: List[BetaManagedAgentsAgentToolConfig]`

          - `enabled: bool`

          - `name: Literal["bash", "edit", "read", 5 more]`

            Built-in agent tool identifier.

            - `"bash"`

            - `"edit"`

            - `"read"`

            - `"write"`

            - `"glob"`

            - `"grep"`

            - `"web_fetch"`

            - `"web_search"`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

              - `type: Literal["always_allow"]`

                - `"always_allow"`

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

              - `type: Literal["always_ask"]`

                - `"always_ask"`

        - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

          Resolved default configuration for agent tools.

          - `enabled: bool`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

              - `type: Literal["always_allow"]`

                - `"always_allow"`

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

              - `type: Literal["always_ask"]`

                - `"always_ask"`

        - `type: Literal["agent_toolset_20260401"]`

          - `"agent_toolset_20260401"`

      - `class BetaManagedAgentsMCPToolset: …`

        - `configs: List[BetaManagedAgentsMCPToolConfig]`

          - `enabled: bool`

          - `name: str`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

              - `type: Literal["always_allow"]`

                - `"always_allow"`

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

              - `type: Literal["always_ask"]`

                - `"always_ask"`

        - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: bool`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

              - `type: Literal["always_allow"]`

                - `"always_allow"`

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

              - `type: Literal["always_ask"]`

                - `"always_ask"`

        - `mcp_server_name: str`

        - `type: Literal["mcp_toolset"]`

          - `"mcp_toolset"`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

        - `description: str`

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `properties: Optional[Dict[str, object]]`

            JSON Schema properties defining the tool's input parameters.

          - `required: Optional[List[str]]`

            List of required property names.

          - `type: Optional[Literal["object"]]`

            Must be 'object' for tool input schemas.

            - `"object"`

        - `name: str`

        - `type: Literal["custom"]`

          - `"custom"`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `environment_id: str`

  - `metadata: Dict[str, str]`

  - `outcome_evaluations: List[BetaManagedAgentsOutcomeEvaluationResource]`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

    - `completed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `description: str`

      What the agent should produce.

    - `explanation: Optional[str]`

      Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

    - `iteration: int`

      0-indexed revision cycle the outcome is currently on.

    - `outcome_id: str`

      Server-generated outc_ ID for this outcome.

    - `result: str`

      Current evaluation state. 'pending' before the agent begins work; 'running' while producing or revising; 'evaluating' while the grader scores; 'satisfied'/'max_iterations_reached'/'failed'/'interrupted' are terminal.

    - `type: Literal["outcome_evaluation"]`

      - `"outcome_evaluation"`

  - `resources: List[BetaManagedAgentsSessionResource]`

    - `class BetaManagedAgentsGitHubRepositoryResource: …`

      - `id: str`

      - `created_at: datetime`

        A timestamp in RFC 3339 format

      - `mount_path: str`

      - `type: Literal["github_repository"]`

        - `"github_repository"`

      - `updated_at: datetime`

        A timestamp in RFC 3339 format

      - `url: str`

      - `checkout: Optional[Checkout]`

        - `class BetaManagedAgentsBranchCheckout: …`

          - `name: str`

            Branch name to check out.

          - `type: Literal["branch"]`

            - `"branch"`

        - `class BetaManagedAgentsCommitCheckout: …`

          - `sha: str`

            Full commit SHA to check out.

          - `type: Literal["commit"]`

            - `"commit"`

    - `class BetaManagedAgentsFileResource: …`

      - `id: str`

      - `created_at: datetime`

        A timestamp in RFC 3339 format

      - `file_id: str`

      - `mount_path: str`

      - `type: Literal["file"]`

        - `"file"`

      - `updated_at: datetime`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsMemoryStoreResource: …`

      A memory store attached to an agent session.

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: Literal["memory_store"]`

        - `"memory_store"`

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `description: Optional[str]`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      - `mount_path: Optional[str]`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `name: Optional[str]`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `stats: BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

    - `duration_seconds: Optional[float]`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

  - `status: Literal["rescheduling", "running", "idle", "terminated"]`

    SessionStatus enum

    - `"rescheduling"`

    - `"running"`

    - `"idle"`

    - `"terminated"`

  - `title: Optional[str]`

  - `type: Literal["session"]`

    - `"session"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `usage: BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

    - `cache_creation: Optional[BetaManagedAgentsCacheCreationUsage]`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: Optional[int]`

        Tokens used to create 1-hour ephemeral cache entries.

      - `ephemeral_5m_input_tokens: Optional[int]`

        Tokens used to create 5-minute ephemeral cache entries.

    - `cache_read_input_tokens: Optional[int]`

      Total tokens read from prompt cache.

    - `input_tokens: Optional[int]`

      Total input tokens consumed across all turns.

    - `output_tokens: Optional[int]`

      Total output tokens generated across all turns.

  - `vault_ids: List[str]`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.sessions.list()
page = page.data[0]
print(page.id)
```
