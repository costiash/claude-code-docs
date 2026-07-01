# Sessions

## Create Session

`beta.sessions.create(SessionCreateParams**kwargs)  -> BetaManagedAgentsSession`

**post** `/v1/sessions`

Create Session

### Parameters

- `agent: Agent`

  Agent identifier. Accepts the `agent` ID string, which pins the latest version for the session, or an `agent` object with both id and version specified.

  - `str`

  - `class BetaManagedAgentsAgentParams: …`

    Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

    - `id: str`

      The `agent` ID.

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: Optional[int]`

      The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

  - `class BetaManagedAgentsAgentWithOverridesParams: …`

    Reference to an `agent` plus optional configuration overrides. Each provided field replaces the agent's value for the caller's use; the agent resource is unchanged.

    - `id: str`

      The `agent` ID.

    - `type: Literal["agent_with_overrides"]`

      - `"agent_with_overrides"`

    - `mcp_servers: Optional[List[BetaManagedAgentsURLMCPServerParams]]`

      Replacement MCP server list. Full replacement: the provided array becomes the MCP servers. Send an empty array to clear; omit to preserve the agent's servers.

      - `name: str`

        Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

      - `type: Literal["url"]`

        - `"url"`

      - `url: str`

        Endpoint URL for the MCP server.

    - `model: Optional[Model]`

      Replacement model. Accepts the model string, e.g. `claude-opus-4-6`, or a `model_config` object. Omit to use the agent's model.

      - `Union[Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more], str]`

        - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-6` - Most intelligent model for building agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
          - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

          - `"claude-sonnet-5"`

            High-performance model for coding and agents

          - `"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-4-8"`

            Frontier intelligence for long-running agents and coding

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

      - `class BetaManagedAgentsModelConfigParams: …`

        An object that defines additional configuration control over model use

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `claude-sonnet-5` - High-performance model for coding and agents
            - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
            - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
            - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
            - `claude-opus-4-6` - Most intelligent model for building agents and coding
            - `claude-sonnet-4-6` - Best combination of speed and intelligence
            - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
            - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
            - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
            - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
            - `claude-sonnet-4-5` - High-performance model for agents and coding
            - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

          - `str`

        - `speed: Optional[Literal["standard", "fast"]]`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

    - `skills: Optional[List[BetaManagedAgentsSkillParams]]`

      Replacement skill list. Full replacement: the provided array becomes the skills. Send an empty array to clear; omit to preserve the agent's skills.

      - `class BetaManagedAgentsAnthropicSkillParams: …`

        An Anthropic-managed skill.

        - `skill_id: str`

          Identifier of the Anthropic skill (e.g., "xlsx").

        - `type: Literal["anthropic"]`

          - `"anthropic"`

        - `version: Optional[str]`

          Version to pin. Defaults to latest if omitted.

      - `class BetaManagedAgentsCustomSkillParams: …`

        A user-created custom skill.

        - `skill_id: str`

          Tagged ID of the custom skill (e.g., "skill_01XJ5...").

        - `type: Literal["custom"]`

          - `"custom"`

        - `version: Optional[str]`

          Version to pin. Defaults to latest if omitted.

    - `system: Optional[str]`

      Replacement system prompt. Up to 100,000 characters. Set to null to clear the agent's system prompt; omit to preserve it.

    - `tools: Optional[List[Tool]]`

      Replacement tool list. Full replacement: the provided array becomes the tool configuration. Send an empty array to clear; omit to preserve the agent's tools.

      - `class BetaManagedAgentsAgentToolset20260401Params: …`

        Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

        - `type: Literal["agent_toolset_20260401"]`

          - `"agent_toolset_20260401"`

        - `configs: Optional[List[BetaManagedAgentsAgentToolConfigParams]]`

          Per-tool configuration overrides.

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

          - `enabled: Optional[bool]`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

              - `type: Literal["always_allow"]`

                - `"always_allow"`

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

              - `type: Literal["always_ask"]`

                - `"always_ask"`

        - `default_config: Optional[BetaManagedAgentsAgentToolsetDefaultConfigParams]`

          Default configuration for all tools in a toolset.

          - `enabled: Optional[bool]`

            Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

      - `class BetaManagedAgentsMCPToolsetParams: …`

        Configuration for tools from an MCP server defined in `mcp_servers`.

        - `mcp_server_name: str`

          Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

        - `type: Literal["mcp_toolset"]`

          - `"mcp_toolset"`

        - `configs: Optional[List[BetaManagedAgentsMCPToolConfigParams]]`

          Per-tool configuration overrides.

          - `name: str`

            Name of the MCP tool to configure. 1-128 characters.

          - `enabled: Optional[bool]`

            Whether this tool is enabled. Overrides the `default_config` setting.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `default_config: Optional[BetaManagedAgentsMCPToolsetDefaultConfigParams]`

          Default configuration for all tools from an MCP server.

          - `enabled: Optional[bool]`

            Whether tools are enabled by default. Defaults to true if not specified.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

      - `class BetaManagedAgentsCustomToolParams: …`

        A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

        - `description: str`

          Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `type: Literal["object"]`

            - `"object"`

          - `properties: Optional[Dict[str, object]]`

          - `required: Optional[List[str]]`

        - `name: str`

          Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

        - `type: Literal["custom"]`

          - `"custom"`

    - `version: Optional[int]`

      The specific `agent` version to use. Omit to use the latest version.

- `environment_id: str`

  ID of the `environment` defining the container configuration for this session.

- `metadata: Optional[Dict[str, str]]`

  Arbitrary key-value metadata attached to the session. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `resources: Optional[Iterable[Resource]]`

  Resources (e.g. repositories, files) to mount into the session's container.

  - `class BetaManagedAgentsGitHubRepositoryResourceParams: …`

    Mount a GitHub repository into the session's container.

    - `authorization_token: str`

      GitHub authorization token used to clone the repository.

    - `type: Literal["github_repository"]`

      - `"github_repository"`

    - `url: str`

      Github URL of the repository

    - `checkout: Optional[Checkout]`

      Branch or commit to check out. Defaults to the repository's default branch.

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

    - `mount_path: Optional[str]`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

  - `class BetaManagedAgentsFileResourceParams: …`

    Mount a file uploaded via the Files API into the session.

    - `file_id: str`

      ID of a previously uploaded file.

    - `type: Literal["file"]`

      - `"file"`

    - `mount_path: Optional[str]`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  - `class BetaManagedAgentsMemoryStoreResourceParam: …`

    Parameters for attaching a memory store to an agent session.

    - `memory_store_id: str`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: Literal["memory_store"]`

      - `"memory_store"`

    - `access: Optional[Literal["read_write", "read_only"]]`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `instructions: Optional[str]`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

- `title: Optional[str]`

  Human-readable session title.

- `vault_ids: Optional[Sequence[str]]`

  Vault IDs for stored credentials the agent can use during the session.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]`

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

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

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

        - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-6` - Most intelligent model for building agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
          - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

          - `"claude-sonnet-5"`

            High-performance model for coding and agents

          - `"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-4-8"`

            Frontier intelligence for long-running agents and coding

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

          - `url: str`

        - `model: BetaManagedAgentsModelConfig`

          Model identifier and configuration.

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

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

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

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

            - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

              Resolved default configuration for all tools from an MCP server.

              - `enabled: bool`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

            - `mcp_server_name: str`

            - `type: Literal["mcp_toolset"]`

              - `"mcp_toolset"`

          - `class BetaManagedAgentsCustomTool: …`

            A custom tool as returned in API responses.

            - `description: str`

            - `input_schema: BetaManagedAgentsCustomToolInputSchema`

              JSON Schema for custom tool input parameters.

              - `type: Literal["object"]`

                - `"object"`

              - `properties: Optional[Dict[str, object]]`

              - `required: Optional[List[str]]`

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

      - `class BetaManagedAgentsCustomSkill: …`

        A resolved user-created custom skill.

    - `system: Optional[str]`

    - `tools: List[Tool]`

      - `class BetaManagedAgentsAgentToolset20260401: …`

      - `class BetaManagedAgentsMCPToolset: …`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

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

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

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

  - `deployment_id: Optional[str]`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_session = client.beta.sessions.create(
    agent="agent_011CZkYpogX7uDKUyvBTophP",
    environment_id="env_011CZkZ9X2dpNyB7HsEFoRfW",
)
print(beta_managed_agents_session.id)
```

#### Response

```json
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
  ],
  "deployment_id": "deployment_id"
}
```

## List Sessions

`beta.sessions.list(SessionListParams**kwargs)  -> SyncBidirectionalPageCursor[BetaManagedAgentsSession]`

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

- `deployment_id: Optional[str]`

  Filter sessions created by this deployment ID.

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

  Opaque pagination cursor from a previous response.

- `statuses: Optional[List[Literal["rescheduling", "running", "idle", "terminated"]]]`

  Filter by session status. Repeat the parameter to match any of multiple statuses.

  - `"rescheduling"`

  - `"running"`

  - `"idle"`

  - `"terminated"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]`

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

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

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

        - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-6` - Most intelligent model for building agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
          - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

          - `"claude-sonnet-5"`

            High-performance model for coding and agents

          - `"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-4-8"`

            Frontier intelligence for long-running agents and coding

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

          - `url: str`

        - `model: BetaManagedAgentsModelConfig`

          Model identifier and configuration.

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

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

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

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

            - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

              Resolved default configuration for all tools from an MCP server.

              - `enabled: bool`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

            - `mcp_server_name: str`

            - `type: Literal["mcp_toolset"]`

              - `"mcp_toolset"`

          - `class BetaManagedAgentsCustomTool: …`

            A custom tool as returned in API responses.

            - `description: str`

            - `input_schema: BetaManagedAgentsCustomToolInputSchema`

              JSON Schema for custom tool input parameters.

              - `type: Literal["object"]`

                - `"object"`

              - `properties: Optional[Dict[str, object]]`

              - `required: Optional[List[str]]`

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

      - `class BetaManagedAgentsCustomSkill: …`

        A resolved user-created custom skill.

    - `system: Optional[str]`

    - `tools: List[Tool]`

      - `class BetaManagedAgentsAgentToolset20260401: …`

      - `class BetaManagedAgentsMCPToolset: …`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

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

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

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

  - `deployment_id: Optional[str]`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

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
      ],
      "deployment_id": "deployment_id"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo=",
  "prev_page": "page_MjAyNS0wNS0xM1QwMDowMDowMFo="
}
```

## Get Session

`beta.sessions.retrieve(strsession_id, SessionRetrieveParams**kwargs)  -> BetaManagedAgentsSession`

**get** `/v1/sessions/{session_id}`

Get Session

### Parameters

- `session_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]`

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

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

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

        - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-6` - Most intelligent model for building agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
          - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

          - `"claude-sonnet-5"`

            High-performance model for coding and agents

          - `"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-4-8"`

            Frontier intelligence for long-running agents and coding

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

          - `url: str`

        - `model: BetaManagedAgentsModelConfig`

          Model identifier and configuration.

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

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

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

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

            - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

              Resolved default configuration for all tools from an MCP server.

              - `enabled: bool`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

            - `mcp_server_name: str`

            - `type: Literal["mcp_toolset"]`

              - `"mcp_toolset"`

          - `class BetaManagedAgentsCustomTool: …`

            A custom tool as returned in API responses.

            - `description: str`

            - `input_schema: BetaManagedAgentsCustomToolInputSchema`

              JSON Schema for custom tool input parameters.

              - `type: Literal["object"]`

                - `"object"`

              - `properties: Optional[Dict[str, object]]`

              - `required: Optional[List[str]]`

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

      - `class BetaManagedAgentsCustomSkill: …`

        A resolved user-created custom skill.

    - `system: Optional[str]`

    - `tools: List[Tool]`

      - `class BetaManagedAgentsAgentToolset20260401: …`

      - `class BetaManagedAgentsMCPToolset: …`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

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

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

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

  - `deployment_id: Optional[str]`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_session = client.beta.sessions.retrieve(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
print(beta_managed_agents_session.id)
```

#### Response

```json
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
  ],
  "deployment_id": "deployment_id"
}
```

## Update Session

`beta.sessions.update(strsession_id, SessionUpdateParams**kwargs)  -> BetaManagedAgentsSession`

**post** `/v1/sessions/{session_id}`

Update Session

### Parameters

- `session_id: str`

- `agent: Optional[BetaManagedAgentsSessionAgentUpdateParam]`

  Mid-session agent configuration update. Only `tools` and `mcp_servers` are updatable. Full replacement: the provided array becomes the new value. To preserve existing entries, GET the session, modify the array, and POST it back.

  - `mcp_servers: Optional[List[BetaManagedAgentsURLMCPServerParams]]`

    Replacement MCP server list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

    - `name: str`

      Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

    - `type: Literal["url"]`

      - `"url"`

    - `url: str`

      Endpoint URL for the MCP server.

  - `tools: Optional[List[Tool]]`

    Replacement tool list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

    - `class BetaManagedAgentsAgentToolset20260401Params: …`

      Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

      - `type: Literal["agent_toolset_20260401"]`

        - `"agent_toolset_20260401"`

      - `configs: Optional[List[BetaManagedAgentsAgentToolConfigParams]]`

        Per-tool configuration overrides.

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

        - `enabled: Optional[bool]`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: Optional[PermissionPolicy]`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy: …`

            Tool calls are automatically approved without user confirmation.

            - `type: Literal["always_allow"]`

              - `"always_allow"`

          - `class BetaManagedAgentsAlwaysAskPolicy: …`

            Tool calls require user confirmation before execution.

            - `type: Literal["always_ask"]`

              - `"always_ask"`

      - `default_config: Optional[BetaManagedAgentsAgentToolsetDefaultConfigParams]`

        Default configuration for all tools in a toolset.

        - `enabled: Optional[bool]`

          Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

        - `permission_policy: Optional[PermissionPolicy]`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy: …`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy: …`

            Tool calls require user confirmation before execution.

    - `class BetaManagedAgentsMCPToolsetParams: …`

      Configuration for tools from an MCP server defined in `mcp_servers`.

      - `mcp_server_name: str`

        Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

      - `type: Literal["mcp_toolset"]`

        - `"mcp_toolset"`

      - `configs: Optional[List[BetaManagedAgentsMCPToolConfigParams]]`

        Per-tool configuration overrides.

        - `name: str`

          Name of the MCP tool to configure. 1-128 characters.

        - `enabled: Optional[bool]`

          Whether this tool is enabled. Overrides the `default_config` setting.

        - `permission_policy: Optional[PermissionPolicy]`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy: …`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy: …`

            Tool calls require user confirmation before execution.

      - `default_config: Optional[BetaManagedAgentsMCPToolsetDefaultConfigParams]`

        Default configuration for all tools from an MCP server.

        - `enabled: Optional[bool]`

          Whether tools are enabled by default. Defaults to true if not specified.

        - `permission_policy: Optional[PermissionPolicy]`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy: …`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy: …`

            Tool calls require user confirmation before execution.

    - `class BetaManagedAgentsCustomToolParams: …`

      A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

      - `description: str`

        Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: Literal["object"]`

          - `"object"`

        - `properties: Optional[Dict[str, object]]`

        - `required: Optional[List[str]]`

      - `name: str`

        Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

      - `type: Literal["custom"]`

        - `"custom"`

- `metadata: Optional[Dict[str, Optional[str]]]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve.

- `title: Optional[str]`

  Human-readable session title.

- `vault_ids: Optional[Sequence[str]]`

  Vault IDs (`vlt_*`) to attach to the session. Not yet supported; requests setting this field are rejected. Reserved for future use.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]`

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

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

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

        - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-6` - Most intelligent model for building agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
          - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

          - `"claude-sonnet-5"`

            High-performance model for coding and agents

          - `"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-4-8"`

            Frontier intelligence for long-running agents and coding

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

          - `url: str`

        - `model: BetaManagedAgentsModelConfig`

          Model identifier and configuration.

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

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

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

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

            - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

              Resolved default configuration for all tools from an MCP server.

              - `enabled: bool`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

            - `mcp_server_name: str`

            - `type: Literal["mcp_toolset"]`

              - `"mcp_toolset"`

          - `class BetaManagedAgentsCustomTool: …`

            A custom tool as returned in API responses.

            - `description: str`

            - `input_schema: BetaManagedAgentsCustomToolInputSchema`

              JSON Schema for custom tool input parameters.

              - `type: Literal["object"]`

                - `"object"`

              - `properties: Optional[Dict[str, object]]`

              - `required: Optional[List[str]]`

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

      - `class BetaManagedAgentsCustomSkill: …`

        A resolved user-created custom skill.

    - `system: Optional[str]`

    - `tools: List[Tool]`

      - `class BetaManagedAgentsAgentToolset20260401: …`

      - `class BetaManagedAgentsMCPToolset: …`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

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

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

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

  - `deployment_id: Optional[str]`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_session = client.beta.sessions.update(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
print(beta_managed_agents_session.id)
```

#### Response

```json
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
  ],
  "deployment_id": "deployment_id"
}
```

## Delete Session

`beta.sessions.delete(strsession_id, SessionDeleteParams**kwargs)  -> BetaManagedAgentsDeletedSession`

**delete** `/v1/sessions/{session_id}`

Delete Session

### Parameters

- `session_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]`

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

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

### Returns

- `class BetaManagedAgentsDeletedSession: …`

  Confirmation that a `session` has been permanently deleted.

  - `id: str`

  - `type: Literal["session_deleted"]`

    - `"session_deleted"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_deleted_session = client.beta.sessions.delete(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
print(beta_managed_agents_deleted_session.id)
```

#### Response

```json
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "type": "session_deleted"
}
```

## Archive Session

`beta.sessions.archive(strsession_id, SessionArchiveParams**kwargs)  -> BetaManagedAgentsSession`

**post** `/v1/sessions/{session_id}/archive`

Archive Session

### Parameters

- `session_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]`

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

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

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

        - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-6` - Most intelligent model for building agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
          - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

          - `"claude-sonnet-5"`

            High-performance model for coding and agents

          - `"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-4-8"`

            Frontier intelligence for long-running agents and coding

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

          - `url: str`

        - `model: BetaManagedAgentsModelConfig`

          Model identifier and configuration.

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

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

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

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

            - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

              Resolved default configuration for all tools from an MCP server.

              - `enabled: bool`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

            - `mcp_server_name: str`

            - `type: Literal["mcp_toolset"]`

              - `"mcp_toolset"`

          - `class BetaManagedAgentsCustomTool: …`

            A custom tool as returned in API responses.

            - `description: str`

            - `input_schema: BetaManagedAgentsCustomToolInputSchema`

              JSON Schema for custom tool input parameters.

              - `type: Literal["object"]`

                - `"object"`

              - `properties: Optional[Dict[str, object]]`

              - `required: Optional[List[str]]`

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

      - `class BetaManagedAgentsCustomSkill: …`

        A resolved user-created custom skill.

    - `system: Optional[str]`

    - `tools: List[Tool]`

      - `class BetaManagedAgentsAgentToolset20260401: …`

      - `class BetaManagedAgentsMCPToolset: …`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

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

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

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

  - `deployment_id: Optional[str]`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_session = client.beta.sessions.archive(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
print(beta_managed_agents_session.id)
```

#### Response

```json
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
  ],
  "deployment_id": "deployment_id"
}
```

## Domain Types

### Beta Managed Agents Agent Message Preview

- `class BetaManagedAgentsAgentMessagePreview: …`

  - `id: str`

    The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

  - `type: Literal["agent.message"]`

    - `"agent.message"`

### Beta Managed Agents Agent Params

- `class BetaManagedAgentsAgentParams: …`

  Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

  - `id: str`

    The `agent` ID.

  - `type: Literal["agent"]`

    - `"agent"`

  - `version: Optional[int]`

    The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

### Beta Managed Agents Agent Thinking Preview

- `class BetaManagedAgentsAgentThinkingPreview: …`

  - `id: str`

    The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

  - `type: Literal["agent.thinking"]`

    - `"agent.thinking"`

### Beta Managed Agents Agent With Overrides Params

- `class BetaManagedAgentsAgentWithOverridesParams: …`

  Reference to an `agent` plus optional configuration overrides. Each provided field replaces the agent's value for the caller's use; the agent resource is unchanged.

  - `id: str`

    The `agent` ID.

  - `type: Literal["agent_with_overrides"]`

    - `"agent_with_overrides"`

  - `mcp_servers: Optional[List[BetaManagedAgentsURLMCPServerParams]]`

    Replacement MCP server list. Full replacement: the provided array becomes the MCP servers. Send an empty array to clear; omit to preserve the agent's servers.

    - `name: str`

      Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

    - `type: Literal["url"]`

      - `"url"`

    - `url: str`

      Endpoint URL for the MCP server.

  - `model: Optional[Model]`

    Replacement model. Accepts the model string, e.g. `claude-opus-4-6`, or a `model_config` object. Omit to use the agent's model.

    - `Union[Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more], str]`

      - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `claude-sonnet-5` - High-performance model for coding and agents
        - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
        - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
        - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
        - `claude-opus-4-6` - Most intelligent model for building agents and coding
        - `claude-sonnet-4-6` - Best combination of speed and intelligence
        - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
        - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
        - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
        - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
        - `claude-sonnet-4-5` - High-performance model for agents and coding
        - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

        - `"claude-sonnet-5"`

          High-performance model for coding and agents

        - `"claude-fable-5"`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `"claude-opus-4-8"`

          Frontier intelligence for long-running agents and coding

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

    - `class BetaManagedAgentsModelConfigParams: …`

      An object that defines additional configuration control over model use

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-6` - Most intelligent model for building agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
          - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

        - `str`

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `skills: Optional[List[BetaManagedAgentsSkillParams]]`

    Replacement skill list. Full replacement: the provided array becomes the skills. Send an empty array to clear; omit to preserve the agent's skills.

    - `class BetaManagedAgentsAnthropicSkillParams: …`

      An Anthropic-managed skill.

      - `skill_id: str`

        Identifier of the Anthropic skill (e.g., "xlsx").

      - `type: Literal["anthropic"]`

        - `"anthropic"`

      - `version: Optional[str]`

        Version to pin. Defaults to latest if omitted.

    - `class BetaManagedAgentsCustomSkillParams: …`

      A user-created custom skill.

      - `skill_id: str`

        Tagged ID of the custom skill (e.g., "skill_01XJ5...").

      - `type: Literal["custom"]`

        - `"custom"`

      - `version: Optional[str]`

        Version to pin. Defaults to latest if omitted.

  - `system: Optional[str]`

    Replacement system prompt. Up to 100,000 characters. Set to null to clear the agent's system prompt; omit to preserve it.

  - `tools: Optional[List[Tool]]`

    Replacement tool list. Full replacement: the provided array becomes the tool configuration. Send an empty array to clear; omit to preserve the agent's tools.

    - `class BetaManagedAgentsAgentToolset20260401Params: …`

      Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

      - `type: Literal["agent_toolset_20260401"]`

        - `"agent_toolset_20260401"`

      - `configs: Optional[List[BetaManagedAgentsAgentToolConfigParams]]`

        Per-tool configuration overrides.

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

        - `enabled: Optional[bool]`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: Optional[PermissionPolicy]`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy: …`

            Tool calls are automatically approved without user confirmation.

            - `type: Literal["always_allow"]`

              - `"always_allow"`

          - `class BetaManagedAgentsAlwaysAskPolicy: …`

            Tool calls require user confirmation before execution.

            - `type: Literal["always_ask"]`

              - `"always_ask"`

      - `default_config: Optional[BetaManagedAgentsAgentToolsetDefaultConfigParams]`

        Default configuration for all tools in a toolset.

        - `enabled: Optional[bool]`

          Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

        - `permission_policy: Optional[PermissionPolicy]`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy: …`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy: …`

            Tool calls require user confirmation before execution.

    - `class BetaManagedAgentsMCPToolsetParams: …`

      Configuration for tools from an MCP server defined in `mcp_servers`.

      - `mcp_server_name: str`

        Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

      - `type: Literal["mcp_toolset"]`

        - `"mcp_toolset"`

      - `configs: Optional[List[BetaManagedAgentsMCPToolConfigParams]]`

        Per-tool configuration overrides.

        - `name: str`

          Name of the MCP tool to configure. 1-128 characters.

        - `enabled: Optional[bool]`

          Whether this tool is enabled. Overrides the `default_config` setting.

        - `permission_policy: Optional[PermissionPolicy]`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy: …`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy: …`

            Tool calls require user confirmation before execution.

      - `default_config: Optional[BetaManagedAgentsMCPToolsetDefaultConfigParams]`

        Default configuration for all tools from an MCP server.

        - `enabled: Optional[bool]`

          Whether tools are enabled by default. Defaults to true if not specified.

        - `permission_policy: Optional[PermissionPolicy]`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy: …`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy: …`

            Tool calls require user confirmation before execution.

    - `class BetaManagedAgentsCustomToolParams: …`

      A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

      - `description: str`

        Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: Literal["object"]`

          - `"object"`

        - `properties: Optional[Dict[str, object]]`

        - `required: Optional[List[str]]`

      - `name: str`

        Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

      - `type: Literal["custom"]`

        - `"custom"`

  - `version: Optional[int]`

    The specific `agent` version to use. Omit to use the latest version.

### Beta Managed Agents Branch Checkout

- `class BetaManagedAgentsBranchCheckout: …`

  - `name: str`

    Branch name to check out.

  - `type: Literal["branch"]`

    - `"branch"`

### Beta Managed Agents Cache Creation Usage

- `class BetaManagedAgentsCacheCreationUsage: …`

  Prompt-cache creation token usage broken down by cache lifetime.

  - `ephemeral_1h_input_tokens: Optional[int]`

    Tokens used to create 1-hour ephemeral cache entries.

  - `ephemeral_5m_input_tokens: Optional[int]`

    Tokens used to create 5-minute ephemeral cache entries.

### Beta Managed Agents Commit Checkout

- `class BetaManagedAgentsCommitCheckout: …`

  - `sha: str`

    Full commit SHA to check out.

  - `type: Literal["commit"]`

    - `"commit"`

### Beta Managed Agents Deleted Session

- `class BetaManagedAgentsDeletedSession: …`

  Confirmation that a `session` has been permanently deleted.

  - `id: str`

  - `type: Literal["session_deleted"]`

    - `"session_deleted"`

### Beta Managed Agents Delta Content

- `class BetaManagedAgentsDeltaContent: …`

  - `content: BetaManagedAgentsTextBlock`

    Regular text content.

    - `text: str`

      The text content.

    - `type: Literal["text"]`

      - `"text"`

  - `type: Literal["content_delta"]`

    - `"content_delta"`

  - `index: Optional[int]`

    Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

### Beta Managed Agents Delta Event

- `class BetaManagedAgentsDeltaEvent: …`

  An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

  - `delta: BetaManagedAgentsDeltaContent`

    One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

    - `content: BetaManagedAgentsTextBlock`

      Regular text content.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `type: Literal["content_delta"]`

      - `"content_delta"`

    - `index: Optional[int]`

      Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

  - `event_id: str`

    The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

  - `type: Literal["event_delta"]`

    - `"event_delta"`

### Beta Managed Agents Delta Type

- `Literal["agent.message", "agent.thinking"]`

  EventDeltaType enum

  - `"agent.message"`

  - `"agent.thinking"`

### Beta Managed Agents File Resource Params

- `class BetaManagedAgentsFileResourceParams: …`

  Mount a file uploaded via the Files API into the session.

  - `file_id: str`

    ID of a previously uploaded file.

  - `type: Literal["file"]`

    - `"file"`

  - `mount_path: Optional[str]`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

### Beta Managed Agents GitHub Repository Resource Params

- `class BetaManagedAgentsGitHubRepositoryResourceParams: …`

  Mount a GitHub repository into the session's container.

  - `authorization_token: str`

    GitHub authorization token used to clone the repository.

  - `type: Literal["github_repository"]`

    - `"github_repository"`

  - `url: str`

    Github URL of the repository

  - `checkout: Optional[Checkout]`

    Branch or commit to check out. Defaults to the repository's default branch.

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

  - `mount_path: Optional[str]`

    Mount path in the container. Defaults to `/workspace/<repo-name>`.

### Beta Managed Agents Memory Store Resource Param

- `class BetaManagedAgentsMemoryStoreResourceParam: …`

  Parameters for attaching a memory store to an agent session.

  - `memory_store_id: str`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `type: Literal["memory_store"]`

    - `"memory_store"`

  - `access: Optional[Literal["read_write", "read_only"]]`

    Access mode for an attached memory store.

    - `"read_write"`

    - `"read_only"`

  - `instructions: Optional[str]`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Multiagent

- `class BetaManagedAgentsMultiagent: …`

  Resolved coordinator topology with a concrete agent roster.

  - `agents: List[BetaManagedAgentsAgentReference]`

    Agents the coordinator may spawn as session threads, each resolved to a specific version.

    - `id: str`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `type: Literal["coordinator"]`

    - `"coordinator"`

### Beta Managed Agents Multiagent Params

- `class BetaManagedAgentsMultiagentParams: …`

  A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

  - `agents: Sequence[BetaManagedAgentsMultiagentRosterEntryParams]`

    Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

    - `str`

    - `class BetaManagedAgentsAgentParams: …`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `id: str`

        The `agent` ID.

      - `type: Literal["agent"]`

        - `"agent"`

      - `version: Optional[int]`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

    - `class BetaManagedAgentsMultiagentSelfParams: …`

      Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

      - `type: Literal["self"]`

        - `"self"`

  - `type: Literal["coordinator"]`

    - `"coordinator"`

### Beta Managed Agents Multiagent Roster Entry Params

- `BetaManagedAgentsMultiagentRosterEntryParams`

  An entry in a multiagent roster: an agent ID string, a versioned agent reference, or `self`.

  - `str`

  - `class BetaManagedAgentsAgentParams: …`

    Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

    - `id: str`

      The `agent` ID.

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: Optional[int]`

      The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

  - `class BetaManagedAgentsMultiagentSelfParams: …`

    Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

    - `type: Literal["self"]`

      - `"self"`

### Beta Managed Agents Outcome Evaluation Resource

- `class BetaManagedAgentsOutcomeEvaluationResource: …`

  Evaluation state for a single outcome defined via a define_outcome event.

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

    Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

  - `type: Literal["outcome_evaluation"]`

    - `"outcome_evaluation"`

### Beta Managed Agents Session

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

        - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-6` - Most intelligent model for building agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
          - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

          - `"claude-sonnet-5"`

            High-performance model for coding and agents

          - `"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-4-8"`

            Frontier intelligence for long-running agents and coding

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

          - `url: str`

        - `model: BetaManagedAgentsModelConfig`

          Model identifier and configuration.

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

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

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

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

            - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

              Resolved default configuration for all tools from an MCP server.

              - `enabled: bool`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

            - `mcp_server_name: str`

            - `type: Literal["mcp_toolset"]`

              - `"mcp_toolset"`

          - `class BetaManagedAgentsCustomTool: …`

            A custom tool as returned in API responses.

            - `description: str`

            - `input_schema: BetaManagedAgentsCustomToolInputSchema`

              JSON Schema for custom tool input parameters.

              - `type: Literal["object"]`

                - `"object"`

              - `properties: Optional[Dict[str, object]]`

              - `required: Optional[List[str]]`

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

      - `class BetaManagedAgentsCustomSkill: …`

        A resolved user-created custom skill.

    - `system: Optional[str]`

    - `tools: List[Tool]`

      - `class BetaManagedAgentsAgentToolset20260401: …`

      - `class BetaManagedAgentsMCPToolset: …`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

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

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

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

  - `deployment_id: Optional[str]`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Beta Managed Agents Session Agent

- `class BetaManagedAgentsSessionAgent: …`

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

      - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `claude-sonnet-5` - High-performance model for coding and agents
        - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
        - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
        - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
        - `claude-opus-4-6` - Most intelligent model for building agents and coding
        - `claude-sonnet-4-6` - Best combination of speed and intelligence
        - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
        - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
        - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
        - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
        - `claude-sonnet-4-5` - High-performance model for agents and coding
        - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

        - `"claude-sonnet-5"`

          High-performance model for coding and agents

        - `"claude-fable-5"`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `"claude-opus-4-8"`

          Frontier intelligence for long-running agents and coding

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

        - `url: str`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

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

              - `class BetaManagedAgentsAlwaysAskPolicy: …`

                Tool calls require user confirmation before execution.

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

              - `class BetaManagedAgentsAlwaysAskPolicy: …`

                Tool calls require user confirmation before execution.

          - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `enabled: bool`

            - `permission_policy: PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy: …`

                Tool calls require user confirmation before execution.

          - `mcp_server_name: str`

          - `type: Literal["mcp_toolset"]`

            - `"mcp_toolset"`

        - `class BetaManagedAgentsCustomTool: …`

          A custom tool as returned in API responses.

          - `description: str`

          - `input_schema: BetaManagedAgentsCustomToolInputSchema`

            JSON Schema for custom tool input parameters.

            - `type: Literal["object"]`

              - `"object"`

            - `properties: Optional[Dict[str, object]]`

            - `required: Optional[List[str]]`

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

    - `class BetaManagedAgentsCustomSkill: …`

      A resolved user-created custom skill.

  - `system: Optional[str]`

  - `tools: List[Tool]`

    - `class BetaManagedAgentsAgentToolset20260401: …`

    - `class BetaManagedAgentsMCPToolset: …`

    - `class BetaManagedAgentsCustomTool: …`

      A custom tool as returned in API responses.

  - `type: Literal["agent"]`

    - `"agent"`

  - `version: int`

### Beta Managed Agents Session Agent Update

- `class BetaManagedAgentsSessionAgentUpdate: …`

  Mid-session agent configuration update. Only `tools` and `mcp_servers` are updatable. Full replacement: the provided array becomes the new value. To preserve existing entries, GET the session, modify the array, and POST it back.

  - `mcp_servers: Optional[List[BetaManagedAgentsURLMCPServerParams]]`

    Replacement MCP server list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

    - `name: str`

      Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

    - `type: Literal["url"]`

      - `"url"`

    - `url: str`

      Endpoint URL for the MCP server.

  - `tools: Optional[List[Tool]]`

    Replacement tool list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

    - `class BetaManagedAgentsAgentToolset20260401Params: …`

      Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

      - `type: Literal["agent_toolset_20260401"]`

        - `"agent_toolset_20260401"`

      - `configs: Optional[List[BetaManagedAgentsAgentToolConfigParams]]`

        Per-tool configuration overrides.

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

        - `enabled: Optional[bool]`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: Optional[PermissionPolicy]`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy: …`

            Tool calls are automatically approved without user confirmation.

            - `type: Literal["always_allow"]`

              - `"always_allow"`

          - `class BetaManagedAgentsAlwaysAskPolicy: …`

            Tool calls require user confirmation before execution.

            - `type: Literal["always_ask"]`

              - `"always_ask"`

      - `default_config: Optional[BetaManagedAgentsAgentToolsetDefaultConfigParams]`

        Default configuration for all tools in a toolset.

        - `enabled: Optional[bool]`

          Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

        - `permission_policy: Optional[PermissionPolicy]`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy: …`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy: …`

            Tool calls require user confirmation before execution.

    - `class BetaManagedAgentsMCPToolsetParams: …`

      Configuration for tools from an MCP server defined in `mcp_servers`.

      - `mcp_server_name: str`

        Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

      - `type: Literal["mcp_toolset"]`

        - `"mcp_toolset"`

      - `configs: Optional[List[BetaManagedAgentsMCPToolConfigParams]]`

        Per-tool configuration overrides.

        - `name: str`

          Name of the MCP tool to configure. 1-128 characters.

        - `enabled: Optional[bool]`

          Whether this tool is enabled. Overrides the `default_config` setting.

        - `permission_policy: Optional[PermissionPolicy]`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy: …`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy: …`

            Tool calls require user confirmation before execution.

      - `default_config: Optional[BetaManagedAgentsMCPToolsetDefaultConfigParams]`

        Default configuration for all tools from an MCP server.

        - `enabled: Optional[bool]`

          Whether tools are enabled by default. Defaults to true if not specified.

        - `permission_policy: Optional[PermissionPolicy]`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy: …`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy: …`

            Tool calls require user confirmation before execution.

    - `class BetaManagedAgentsCustomToolParams: …`

      A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

      - `description: str`

        Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: Literal["object"]`

          - `"object"`

        - `properties: Optional[Dict[str, object]]`

        - `required: Optional[List[str]]`

      - `name: str`

        Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

      - `type: Literal["custom"]`

        - `"custom"`

### Beta Managed Agents Session Multiagent Coordinator

- `class BetaManagedAgentsSessionMultiagentCoordinator: …`

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

        - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-6` - Most intelligent model for building agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
          - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

          - `"claude-sonnet-5"`

            High-performance model for coding and agents

          - `"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-4-8"`

            Frontier intelligence for long-running agents and coding

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

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

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

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: bool`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `mcp_server_name: str`

        - `type: Literal["mcp_toolset"]`

          - `"mcp_toolset"`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

        - `description: str`

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `type: Literal["object"]`

            - `"object"`

          - `properties: Optional[Dict[str, object]]`

          - `required: Optional[List[str]]`

        - `name: str`

        - `type: Literal["custom"]`

          - `"custom"`

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `type: Literal["coordinator"]`

    - `"coordinator"`

### Beta Managed Agents Session Stats

- `class BetaManagedAgentsSessionStats: …`

  Timing statistics for a session.

  - `active_seconds: Optional[float]`

    Cumulative time in seconds the session spent in running status. Excludes idle time.

  - `duration_seconds: Optional[float]`

    Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

### Beta Managed Agents Session Updated Event

- `class BetaManagedAgentsSessionUpdatedEvent: …`

  Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

  - `id: str`

    Unique identifier for this event.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `type: Literal["session.updated"]`

    - `"session.updated"`

  - `agent: Optional[BetaManagedAgentsSessionAgent]`

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

        - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-6` - Most intelligent model for building agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
          - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

          - `"claude-sonnet-5"`

            High-performance model for coding and agents

          - `"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-4-8"`

            Frontier intelligence for long-running agents and coding

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

          - `url: str`

        - `model: BetaManagedAgentsModelConfig`

          Model identifier and configuration.

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

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

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

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

            - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

              Resolved default configuration for all tools from an MCP server.

              - `enabled: bool`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

            - `mcp_server_name: str`

            - `type: Literal["mcp_toolset"]`

              - `"mcp_toolset"`

          - `class BetaManagedAgentsCustomTool: …`

            A custom tool as returned in API responses.

            - `description: str`

            - `input_schema: BetaManagedAgentsCustomToolInputSchema`

              JSON Schema for custom tool input parameters.

              - `type: Literal["object"]`

                - `"object"`

              - `properties: Optional[Dict[str, object]]`

              - `required: Optional[List[str]]`

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

      - `class BetaManagedAgentsCustomSkill: …`

        A resolved user-created custom skill.

    - `system: Optional[str]`

    - `tools: List[Tool]`

      - `class BetaManagedAgentsAgentToolset20260401: …`

      - `class BetaManagedAgentsMCPToolset: …`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

    - `type: Literal["agent"]`

      - `"agent"`

    - `version: int`

  - `metadata: Optional[Dict[str, str]]`

    The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

  - `title: Optional[str]`

    The session's new title. Present only when the update changed it.

### Beta Managed Agents Session Usage

- `class BetaManagedAgentsSessionUsage: …`

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

### Beta Managed Agents Start Event

- `class BetaManagedAgentsStartEvent: …`

  Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

  - `event: BetaManagedAgentsStartEventPreview`

    The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

    - `class BetaManagedAgentsAgentMessagePreview: …`

      - `id: str`

        The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

      - `type: Literal["agent.message"]`

        - `"agent.message"`

    - `class BetaManagedAgentsAgentThinkingPreview: …`

      - `id: str`

        The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

      - `type: Literal["agent.thinking"]`

        - `"agent.thinking"`

  - `type: Literal["event_start"]`

    - `"event_start"`

### Beta Managed Agents Start Event Preview

- `BetaManagedAgentsStartEventPreview`

  - `class BetaManagedAgentsAgentMessagePreview: …`

    - `id: str`

      The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

    - `type: Literal["agent.message"]`

      - `"agent.message"`

  - `class BetaManagedAgentsAgentThinkingPreview: …`

    - `id: str`

      The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

    - `type: Literal["agent.thinking"]`

      - `"agent.thinking"`

### Beta Managed Agents System Content Block

- `class BetaManagedAgentsSystemContentBlock: …`

  Regular text content.

  - `text: str`

    The text content.

  - `type: Literal["text"]`

    - `"text"`

### Beta Managed Agents System Message Event

- `class BetaManagedAgentsSystemMessageEvent: …`

  A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

  - `id: str`

    Unique identifier for this event.

  - `content: List[BetaManagedAgentsSystemContentBlock]`

    System content blocks. Text-only.

    - `text: str`

      The text content.

    - `type: Literal["text"]`

      - `"text"`

  - `type: Literal["system.message"]`

    - `"system.message"`

  - `processed_at: Optional[datetime]`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Tool Result Event

- `class BetaManagedAgentsUserToolResultEvent: …`

  Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

  - `id: str`

    Unique identifier for this event.

  - `tool_use_id: str`

    The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `type: Literal["user.tool_result"]`

    - `"user.tool_result"`

  - `content: Optional[List[Content]]`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock: …`

      Regular text content.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `class BetaManagedAgentsImageBlock: …`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: Source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource: …`

          Base64-encoded image data.

          - `data: str`

            Base64-encoded image data.

          - `media_type: str`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: Literal["base64"]`

            - `"base64"`

        - `class BetaManagedAgentsURLImageSource: …`

          Image referenced by URL.

          - `type: Literal["url"]`

            - `"url"`

          - `url: str`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource: …`

          Image referenced by file ID.

          - `file_id: str`

            ID of a previously uploaded file.

          - `type: Literal["file"]`

            - `"file"`

      - `type: Literal["image"]`

        - `"image"`

    - `class BetaManagedAgentsDocumentBlock: …`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: Source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource: …`

          Base64-encoded document data.

          - `data: str`

            Base64-encoded document data.

          - `media_type: str`

            MIME type of the document (e.g., "application/pdf").

          - `type: Literal["base64"]`

            - `"base64"`

        - `class BetaManagedAgentsPlainTextDocumentSource: …`

          Plain text document content.

          - `data: str`

            The plain text content.

          - `media_type: Literal["text/plain"]`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsURLDocumentSource: …`

          Document referenced by URL.

          - `type: Literal["url"]`

            - `"url"`

          - `url: str`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource: …`

          Document referenced by file ID.

          - `file_id: str`

            ID of a previously uploaded file.

          - `type: Literal["file"]`

            - `"file"`

      - `type: Literal["document"]`

        - `"document"`

      - `context: Optional[str]`

        Additional context about the document for the model.

      - `title: Optional[str]`

        The title of the document.

    - `class BetaManagedAgentsSearchResultBlock: …`

      A block containing a web search result.

      - `citations: BetaManagedAgentsSearchResultCitations`

        Citation settings for a search result.

        - `enabled: bool`

          Whether citations are enabled for this search result.

      - `content: List[BetaManagedAgentsSearchResultContent]`

        Array of text content blocks from the search result.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `source: str`

        The URL source of the search result.

      - `title: str`

        The title of the search result.

      - `type: Literal["search_result"]`

        - `"search_result"`

  - `is_error: Optional[bool]`

    Whether the tool execution resulted in an error.

  - `processed_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `session_thread_id: Optional[str]`

    Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

# Events

## List Events

`beta.sessions.events.list(strsession_id, EventListParams**kwargs)  -> SyncPageCursor[BetaManagedAgentsSessionEvent]`

**get** `/v1/sessions/{session_id}/events`

List Events

### Parameters

- `session_id: str`

- `created_at_gt: Optional[Union[str, datetime]]`

  Return events created after this time (exclusive).

- `created_at_gte: Optional[Union[str, datetime]]`

  Return events created at or after this time (inclusive).

- `created_at_lt: Optional[Union[str, datetime]]`

  Return events created before this time (exclusive).

- `created_at_lte: Optional[Union[str, datetime]]`

  Return events created at or before this time (inclusive).

- `limit: Optional[int]`

  Query parameter for limit

- `order: Optional[Literal["asc", "desc"]]`

  Sort direction for results, ordered by created_at. Defaults to asc (chronological).

  - `"asc"`

  - `"desc"`

- `page: Optional[str]`

  Opaque pagination cursor from a previous response's next_page.

- `types: Optional[Sequence[str]]`

  Filter by event type. Values match the `type` field on returned events (for example, `user.message` or `agent.tool_use`). Omit to return all event types.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]`

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

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

### Returns

- `BetaManagedAgentsSessionEvent`

  Union type for all event types in a session.

  - `class BetaManagedAgentsUserMessageEvent: …`

    A user message event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `data: str`

              Base64-encoded image data.

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["image"]`

          - `"image"`

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `data: str`

              Base64-encoded document data.

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `data: str`

              The plain text content.

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: Literal["text"]`

              - `"text"`

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["document"]`

          - `"document"`

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

    - `type: Literal["user.message"]`

      - `"user.message"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent: …`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: str`

      Unique identifier for this event.

    - `type: Literal["user.interrupt"]`

      - `"user.interrupt"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent: …`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: str`

      Unique identifier for this event.

    - `result: Literal["allow", "deny"]`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: str`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_confirmation"]`

      - `"user.tool_confirmation"`

    - `deny_message: Optional[str]`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent: …`

    Event sent by the client providing the result of a custom tool execution.

    - `id: str`

      Unique identifier for this event.

    - `custom_tool_use_id: str`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.custom_tool_result"]`

      - `"user.custom_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: bool`

            Whether citations are enabled for this search result.

        - `content: List[BetaManagedAgentsSearchResultContent]`

          Array of text content blocks from the search result.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `source: str`

          The URL source of the search result.

        - `title: str`

          The title of the search result.

        - `type: Literal["search_result"]`

          - `"search_result"`

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent: …`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the custom tool being called.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.custom_tool_use"]`

      - `"agent.custom_tool_use"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent: …`

    An agent response event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsTextBlock]`

      Array of text blocks comprising the agent response.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.message"]`

      - `"agent.message"`

  - `class BetaManagedAgentsAgentThinkingEvent: …`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thinking"]`

      - `"agent.thinking"`

  - `class BetaManagedAgentsAgentMCPToolUseEvent: …`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `mcp_server_name: str`

      Name of the MCP server providing the tool.

    - `name: str`

      Name of the MCP tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.mcp_tool_use"]`

      - `"agent.mcp_tool_use"`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMCPToolResultEvent: …`

    Event representing the result of an MCP tool execution.

    - `id: str`

      Unique identifier for this event.

    - `mcp_tool_use_id: str`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.mcp_tool_result"]`

      - `"agent.mcp_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent: …`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the agent tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.tool_use"]`

      - `"agent.tool_use"`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent: …`

    Event representing the result of an agent tool execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: Literal["agent.tool_result"]`

      - `"agent.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent: …`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `from_session_thread_id: str`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thread_message_received"]`

      - `"agent.thread_message_received"`

    - `from_agent_name: Optional[str]`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent: …`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `to_session_thread_id: str`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: Literal["agent.thread_message_sent"]`

      - `"agent.thread_message_sent"`

    - `to_agent_name: Optional[str]`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent: …`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thread_context_compacted"]`

      - `"agent.thread_context_compacted"`

  - `class BetaManagedAgentsSessionErrorEvent: …`

    An error event indicating a problem occurred during session execution.

    - `id: str`

      Unique identifier for this event.

    - `error: Error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError: …`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: Literal["retrying"]`

              - `"retrying"`

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: Literal["exhausted"]`

              - `"exhausted"`

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: Literal["terminal"]`

              - `"terminal"`

        - `type: Literal["unknown_error"]`

          - `"unknown_error"`

      - `class BetaManagedAgentsModelOverloadedError: …`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_overloaded_error"]`

          - `"model_overloaded_error"`

      - `class BetaManagedAgentsModelRateLimitedError: …`

        The model request was rate-limited.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_rate_limited_error"]`

          - `"model_rate_limited_error"`

      - `class BetaManagedAgentsModelRequestFailedError: …`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_request_failed_error"]`

          - `"model_request_failed_error"`

      - `class BetaManagedAgentsMCPConnectionFailedError: …`

        Failed to connect to an MCP server.

        - `mcp_server_name: str`

          Name of the MCP server that failed to connect.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_connection_failed_error"]`

          - `"mcp_connection_failed_error"`

      - `class BetaManagedAgentsMCPAuthenticationFailedError: …`

        Authentication to an MCP server failed.

        - `mcp_server_name: str`

          Name of the MCP server that failed authentication.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_authentication_failed_error"]`

          - `"mcp_authentication_failed_error"`

      - `class BetaManagedAgentsBillingError: …`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["billing_error"]`

          - `"billing_error"`

      - `class BetaManagedAgentsCredentialHostUnreachableError: …`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: str`

          ID of the affected credential.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["credential_host_unreachable_error"]`

          - `"credential_host_unreachable_error"`

        - `vault_id: str`

          ID of the vault containing the affected credential.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.error"]`

      - `"session.error"`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent: …`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_rescheduled"]`

      - `"session.status_rescheduled"`

  - `class BetaManagedAgentsSessionStatusRunningEvent: …`

    Indicates the session is actively running and the agent is working.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_running"]`

      - `"session.status_running"`

  - `class BetaManagedAgentsSessionStatusIdleEvent: …`

    Indicates the agent has paused and is awaiting user input.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: Literal["end_turn"]`

          - `"end_turn"`

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: List[str]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: Literal["requires_action"]`

          - `"requires_action"`

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `type: Literal["retries_exhausted"]`

          - `"retries_exhausted"`

    - `type: Literal["session.status_idle"]`

      - `"session.status_idle"`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent: …`

    Indicates the session has terminated, either due to an error or completion.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_terminated"]`

      - `"session.status_terminated"`

  - `class BetaManagedAgentsSessionThreadCreatedEvent: …`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the callable agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public `sthr_` ID of the newly created thread.

    - `type: Literal["session.thread_created"]`

      - `"session.thread_created"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent: …`

    Emitted when an outcome evaluation cycle begins.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.outcome_evaluation_start"]`

      - `"span.outcome_evaluation_start"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent: …`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `id: str`

      Unique identifier for this event.

    - `explanation: str`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_evaluation_start_id: str`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `result: str`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `type: Literal["span.outcome_evaluation_end"]`

      - `"span.outcome_evaluation_end"`

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: int`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: int`

        Tokens read from prompt cache in this request.

      - `input_tokens: int`

        Input tokens consumed by this request.

      - `output_tokens: int`

        Output tokens generated by this request.

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `class BetaManagedAgentsSpanModelRequestStartEvent: …`

    Emitted when a model request is initiated by the agent.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.model_request_start"]`

      - `"span.model_request_start"`

  - `class BetaManagedAgentsSpanModelRequestEndEvent: …`

    Emitted when a model request completes.

    - `id: str`

      Unique identifier for this event.

    - `is_error: Optional[bool]`

      Whether the model request resulted in an error.

    - `model_request_start_id: str`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.model_request_end"]`

      - `"span.model_request_end"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent: …`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.outcome_evaluation_ongoing"]`

      - `"span.outcome_evaluation_ongoing"`

  - `class BetaManagedAgentsUserDefineOutcomeEvent: …`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: str`

      Unique identifier for this event.

    - `description: str`

      What the agent should produce. Copied from the input event.

    - `max_iterations: Optional[int]`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `outcome_id: str`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric: …`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: str`

          ID of the rubric file.

        - `type: Literal["file"]`

          - `"file"`

      - `class BetaManagedAgentsTextRubric: …`

        Rubric content provided inline as text.

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: Literal["text"]`

          - `"text"`

    - `type: Literal["user.define_outcome"]`

      - `"user.define_outcome"`

  - `class BetaManagedAgentsSessionDeletedEvent: …`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.deleted"]`

      - `"session.deleted"`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent: …`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that started running.

    - `type: Literal["session.thread_status_running"]`

      - `"session.thread_status_running"`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent: …`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

    - `type: Literal["session.thread_status_idle"]`

      - `"session.thread_status_idle"`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent: …`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that terminated.

    - `type: Literal["session.thread_status_terminated"]`

      - `"session.thread_status_terminated"`

  - `class BetaManagedAgentsUserToolResultEvent: …`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: str`

      Unique identifier for this event.

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_result"]`

      - `"user.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent: …`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that is retrying.

    - `type: Literal["session.thread_status_rescheduled"]`

      - `"session.thread_status_rescheduled"`

  - `class BetaManagedAgentsSessionUpdatedEvent: …`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.updated"]`

      - `"session.updated"`

    - `agent: Optional[BetaManagedAgentsSessionAgent]`

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

          - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `claude-sonnet-5` - High-performance model for coding and agents
            - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
            - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
            - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
            - `claude-opus-4-6` - Most intelligent model for building agents and coding
            - `claude-sonnet-4-6` - Best combination of speed and intelligence
            - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
            - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
            - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
            - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
            - `claude-sonnet-4-5` - High-performance model for agents and coding
            - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

            - `"claude-sonnet-5"`

              High-performance model for coding and agents

            - `"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `"claude-opus-4-8"`

              Frontier intelligence for long-running agents and coding

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

            - `url: str`

          - `model: BetaManagedAgentsModelConfig`

            Model identifier and configuration.

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

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

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

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `mcp_server_name: str`

              - `type: Literal["mcp_toolset"]`

                - `"mcp_toolset"`

            - `class BetaManagedAgentsCustomTool: …`

              A custom tool as returned in API responses.

              - `description: str`

              - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `type: Literal["object"]`

                  - `"object"`

                - `properties: Optional[Dict[str, object]]`

                - `required: Optional[List[str]]`

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

        - `class BetaManagedAgentsCustomSkill: …`

          A resolved user-created custom skill.

      - `system: Optional[str]`

      - `tools: List[Tool]`

        - `class BetaManagedAgentsAgentToolset20260401: …`

        - `class BetaManagedAgentsMCPToolset: …`

        - `class BetaManagedAgentsCustomTool: …`

          A custom tool as returned in API responses.

      - `type: Literal["agent"]`

        - `"agent"`

      - `version: int`

    - `metadata: Optional[Dict[str, str]]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: Optional[str]`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsSystemMessageEvent: …`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks. Text-only.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `type: Literal["system.message"]`

      - `"system.message"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.sessions.events.list(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
page = page.data[0]
print(page)
```

#### Response

```json
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sevt_011CZkZHPq1jCdq5lbRTjiVnz",
      "content": [
        {
          "text": "Let me look up order #1234 for you.",
          "type": "text"
        }
      ],
      "processed_at": "2026-03-15T10:00:00Z",
      "type": "agent.message"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Send Events

`beta.sessions.events.send(strsession_id, EventSendParams**kwargs)  -> BetaManagedAgentsSendSessionEvents`

**post** `/v1/sessions/{session_id}/events`

Send Events

### Parameters

- `session_id: str`

- `events: Iterable[BetaManagedAgentsEventParams]`

  Events to send to the `session`.

  - `class BetaManagedAgentsUserMessageEventParams: …`

    Parameters for sending a user message to the session.

    - `content: List[Content]`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `data: str`

              Base64-encoded image data.

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["image"]`

          - `"image"`

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `data: str`

              Base64-encoded document data.

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `data: str`

              The plain text content.

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: Literal["text"]`

              - `"text"`

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["document"]`

          - `"document"`

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

    - `type: Literal["user.message"]`

      - `"user.message"`

  - `class BetaManagedAgentsUserInterruptEventParams: …`

    Parameters for sending an interrupt to pause the agent.

    - `type: Literal["user.interrupt"]`

      - `"user.interrupt"`

    - `session_thread_id: Optional[str]`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEventParams: …`

    Parameters for confirming or denying a tool execution request.

    - `result: Literal["allow", "deny"]`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: str`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_confirmation"]`

      - `"user.tool_confirmation"`

    - `deny_message: Optional[str]`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

  - `class BetaManagedAgentsUserCustomToolResultEventParams: …`

    Parameters for providing the result of a custom tool execution.

    - `custom_tool_use_id: str`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.custom_tool_result"]`

      - `"user.custom_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: bool`

            Whether citations are enabled for this search result.

        - `content: List[BetaManagedAgentsSearchResultContent]`

          Array of text content blocks from the search result.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `source: str`

          The URL source of the search result.

        - `title: str`

          The title of the search result.

        - `type: Literal["search_result"]`

          - `"search_result"`

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsUserDefineOutcomeEventParams: …`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `description: str`

      What the agent should produce. This is the task specification.

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubricParams: …`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: str`

          ID of the rubric file.

        - `type: Literal["file"]`

          - `"file"`

      - `class BetaManagedAgentsTextRubricParams: …`

        Rubric content provided inline as text.

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

        - `type: Literal["text"]`

          - `"text"`

    - `type: Literal["user.define_outcome"]`

      - `"user.define_outcome"`

    - `max_iterations: Optional[int]`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `class BetaManagedAgentsUserToolResultEventParams: …`

    Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_result"]`

      - `"user.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsSystemMessageEventParams: …`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks to append. Text-only.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `type: Literal["system.message"]`

      - `"system.message"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]`

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

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

### Returns

- `class BetaManagedAgentsSendSessionEvents: …`

  Events that were successfully sent to the session.

  - `data: Optional[List[Data]]`

    Sent events

    - `class BetaManagedAgentsUserMessageEvent: …`

      A user message event in the session conversation.

      - `id: str`

        Unique identifier for this event.

      - `content: List[Content]`

        Array of content blocks comprising the user message.

        - `class BetaManagedAgentsTextBlock: …`

          Regular text content.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsImageBlock: …`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource: …`

              Base64-encoded image data.

              - `data: str`

                Base64-encoded image data.

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsURLImageSource: …`

              Image referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource: …`

              Image referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["image"]`

            - `"image"`

        - `class BetaManagedAgentsDocumentBlock: …`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource: …`

              Base64-encoded document data.

              - `data: str`

                Base64-encoded document data.

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsPlainTextDocumentSource: …`

              Plain text document content.

              - `data: str`

                The plain text content.

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: Literal["text"]`

                - `"text"`

            - `class BetaManagedAgentsURLDocumentSource: …`

              Document referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource: …`

              Document referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["document"]`

            - `"document"`

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

      - `type: Literal["user.message"]`

        - `"user.message"`

      - `processed_at: Optional[datetime]`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserInterruptEvent: …`

      An interrupt event that pauses agent execution and returns control to the user.

      - `id: str`

        Unique identifier for this event.

      - `type: Literal["user.interrupt"]`

        - `"user.interrupt"`

      - `processed_at: Optional[datetime]`

        A timestamp in RFC 3339 format

      - `session_thread_id: Optional[str]`

        If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

    - `class BetaManagedAgentsUserToolConfirmationEvent: …`

      A tool confirmation event that approves or denies a pending tool execution.

      - `id: str`

        Unique identifier for this event.

      - `result: Literal["allow", "deny"]`

        UserToolConfirmationResult enum

        - `"allow"`

        - `"deny"`

      - `tool_use_id: str`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: Literal["user.tool_confirmation"]`

        - `"user.tool_confirmation"`

      - `deny_message: Optional[str]`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      - `processed_at: Optional[datetime]`

        A timestamp in RFC 3339 format

      - `session_thread_id: Optional[str]`

        When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

    - `class BetaManagedAgentsUserCustomToolResultEvent: …`

      Event sent by the client providing the result of a custom tool execution.

      - `id: str`

        Unique identifier for this event.

      - `custom_tool_use_id: str`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: Literal["user.custom_tool_result"]`

        - `"user.custom_tool_result"`

      - `content: Optional[List[Content]]`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock: …`

          Regular text content.

        - `class BetaManagedAgentsImageBlock: …`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock: …`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsSearchResultBlock: …`

          A block containing a web search result.

          - `citations: BetaManagedAgentsSearchResultCitations`

            Citation settings for a search result.

            - `enabled: bool`

              Whether citations are enabled for this search result.

          - `content: List[BetaManagedAgentsSearchResultContent]`

            Array of text content blocks from the search result.

            - `text: str`

              The text content.

            - `type: Literal["text"]`

              - `"text"`

          - `source: str`

            The URL source of the search result.

          - `title: str`

            The title of the search result.

          - `type: Literal["search_result"]`

            - `"search_result"`

      - `is_error: Optional[bool]`

        Whether the tool execution resulted in an error.

      - `processed_at: Optional[datetime]`

        A timestamp in RFC 3339 format

      - `session_thread_id: Optional[str]`

        Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

    - `class BetaManagedAgentsUserDefineOutcomeEvent: …`

      Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

      - `id: str`

        Unique identifier for this event.

      - `description: str`

        What the agent should produce. Copied from the input event.

      - `max_iterations: Optional[int]`

        Evaluate-then-revise cycles before giving up. Default 3, max 20.

      - `outcome_id: str`

        Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

      - `processed_at: datetime`

        A timestamp in RFC 3339 format

      - `rubric: Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric: …`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: str`

            ID of the rubric file.

          - `type: Literal["file"]`

            - `"file"`

        - `class BetaManagedAgentsTextRubric: …`

          Rubric content provided inline as text.

          - `content: str`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: Literal["text"]`

            - `"text"`

      - `type: Literal["user.define_outcome"]`

        - `"user.define_outcome"`

    - `class BetaManagedAgentsUserToolResultEvent: …`

      Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

      - `id: str`

        Unique identifier for this event.

      - `tool_use_id: str`

        The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: Literal["user.tool_result"]`

        - `"user.tool_result"`

      - `content: Optional[List[Content]]`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock: …`

          Regular text content.

        - `class BetaManagedAgentsImageBlock: …`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock: …`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsSearchResultBlock: …`

          A block containing a web search result.

      - `is_error: Optional[bool]`

        Whether the tool execution resulted in an error.

      - `processed_at: Optional[datetime]`

        A timestamp in RFC 3339 format

      - `session_thread_id: Optional[str]`

        Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

    - `class BetaManagedAgentsSystemMessageEvent: …`

      A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

      - `id: str`

        Unique identifier for this event.

      - `content: List[BetaManagedAgentsSystemContentBlock]`

        System content blocks. Text-only.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `type: Literal["system.message"]`

        - `"system.message"`

      - `processed_at: Optional[datetime]`

        A timestamp in RFC 3339 format

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_send_session_events = client.beta.sessions.events.send(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
    events=[{
        "content": [{
            "text": "Where is my order #1234?",
            "type": "text",
        }],
        "type": "user.message",
    }],
)
print(beta_managed_agents_send_session_events.data)
```

#### Response

```json
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    }
  ]
}
```

## Stream Events

`beta.sessions.events.stream(strsession_id, EventStreamParams**kwargs)  -> BetaManagedAgentsStreamSessionEvents`

**get** `/v1/sessions/{session_id}/events/stream`

Stream Events

### Parameters

- `session_id: str`

- `event_deltas: Optional[List[BetaManagedAgentsDeltaType]]`

  When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

  - `"agent.message"`

  - `"agent.thinking"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]`

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

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

### Returns

- `BetaManagedAgentsStreamSessionEvents`

  Server-sent event in the session stream.

  - `class BetaManagedAgentsUserMessageEvent: …`

    A user message event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `data: str`

              Base64-encoded image data.

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["image"]`

          - `"image"`

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `data: str`

              Base64-encoded document data.

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `data: str`

              The plain text content.

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: Literal["text"]`

              - `"text"`

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["document"]`

          - `"document"`

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

    - `type: Literal["user.message"]`

      - `"user.message"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent: …`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: str`

      Unique identifier for this event.

    - `type: Literal["user.interrupt"]`

      - `"user.interrupt"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent: …`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: str`

      Unique identifier for this event.

    - `result: Literal["allow", "deny"]`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: str`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_confirmation"]`

      - `"user.tool_confirmation"`

    - `deny_message: Optional[str]`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent: …`

    Event sent by the client providing the result of a custom tool execution.

    - `id: str`

      Unique identifier for this event.

    - `custom_tool_use_id: str`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.custom_tool_result"]`

      - `"user.custom_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: bool`

            Whether citations are enabled for this search result.

        - `content: List[BetaManagedAgentsSearchResultContent]`

          Array of text content blocks from the search result.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `source: str`

          The URL source of the search result.

        - `title: str`

          The title of the search result.

        - `type: Literal["search_result"]`

          - `"search_result"`

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent: …`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the custom tool being called.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.custom_tool_use"]`

      - `"agent.custom_tool_use"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent: …`

    An agent response event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsTextBlock]`

      Array of text blocks comprising the agent response.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.message"]`

      - `"agent.message"`

  - `class BetaManagedAgentsAgentThinkingEvent: …`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thinking"]`

      - `"agent.thinking"`

  - `class BetaManagedAgentsAgentMCPToolUseEvent: …`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `mcp_server_name: str`

      Name of the MCP server providing the tool.

    - `name: str`

      Name of the MCP tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.mcp_tool_use"]`

      - `"agent.mcp_tool_use"`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMCPToolResultEvent: …`

    Event representing the result of an MCP tool execution.

    - `id: str`

      Unique identifier for this event.

    - `mcp_tool_use_id: str`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.mcp_tool_result"]`

      - `"agent.mcp_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent: …`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the agent tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.tool_use"]`

      - `"agent.tool_use"`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent: …`

    Event representing the result of an agent tool execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: Literal["agent.tool_result"]`

      - `"agent.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent: …`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `from_session_thread_id: str`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thread_message_received"]`

      - `"agent.thread_message_received"`

    - `from_agent_name: Optional[str]`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent: …`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `to_session_thread_id: str`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: Literal["agent.thread_message_sent"]`

      - `"agent.thread_message_sent"`

    - `to_agent_name: Optional[str]`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent: …`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thread_context_compacted"]`

      - `"agent.thread_context_compacted"`

  - `class BetaManagedAgentsSessionErrorEvent: …`

    An error event indicating a problem occurred during session execution.

    - `id: str`

      Unique identifier for this event.

    - `error: Error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError: …`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: Literal["retrying"]`

              - `"retrying"`

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: Literal["exhausted"]`

              - `"exhausted"`

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: Literal["terminal"]`

              - `"terminal"`

        - `type: Literal["unknown_error"]`

          - `"unknown_error"`

      - `class BetaManagedAgentsModelOverloadedError: …`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_overloaded_error"]`

          - `"model_overloaded_error"`

      - `class BetaManagedAgentsModelRateLimitedError: …`

        The model request was rate-limited.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_rate_limited_error"]`

          - `"model_rate_limited_error"`

      - `class BetaManagedAgentsModelRequestFailedError: …`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_request_failed_error"]`

          - `"model_request_failed_error"`

      - `class BetaManagedAgentsMCPConnectionFailedError: …`

        Failed to connect to an MCP server.

        - `mcp_server_name: str`

          Name of the MCP server that failed to connect.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_connection_failed_error"]`

          - `"mcp_connection_failed_error"`

      - `class BetaManagedAgentsMCPAuthenticationFailedError: …`

        Authentication to an MCP server failed.

        - `mcp_server_name: str`

          Name of the MCP server that failed authentication.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_authentication_failed_error"]`

          - `"mcp_authentication_failed_error"`

      - `class BetaManagedAgentsBillingError: …`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["billing_error"]`

          - `"billing_error"`

      - `class BetaManagedAgentsCredentialHostUnreachableError: …`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: str`

          ID of the affected credential.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["credential_host_unreachable_error"]`

          - `"credential_host_unreachable_error"`

        - `vault_id: str`

          ID of the vault containing the affected credential.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.error"]`

      - `"session.error"`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent: …`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_rescheduled"]`

      - `"session.status_rescheduled"`

  - `class BetaManagedAgentsSessionStatusRunningEvent: …`

    Indicates the session is actively running and the agent is working.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_running"]`

      - `"session.status_running"`

  - `class BetaManagedAgentsSessionStatusIdleEvent: …`

    Indicates the agent has paused and is awaiting user input.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: Literal["end_turn"]`

          - `"end_turn"`

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: List[str]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: Literal["requires_action"]`

          - `"requires_action"`

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `type: Literal["retries_exhausted"]`

          - `"retries_exhausted"`

    - `type: Literal["session.status_idle"]`

      - `"session.status_idle"`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent: …`

    Indicates the session has terminated, either due to an error or completion.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_terminated"]`

      - `"session.status_terminated"`

  - `class BetaManagedAgentsSessionThreadCreatedEvent: …`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the callable agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public `sthr_` ID of the newly created thread.

    - `type: Literal["session.thread_created"]`

      - `"session.thread_created"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent: …`

    Emitted when an outcome evaluation cycle begins.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.outcome_evaluation_start"]`

      - `"span.outcome_evaluation_start"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent: …`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `id: str`

      Unique identifier for this event.

    - `explanation: str`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_evaluation_start_id: str`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `result: str`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `type: Literal["span.outcome_evaluation_end"]`

      - `"span.outcome_evaluation_end"`

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: int`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: int`

        Tokens read from prompt cache in this request.

      - `input_tokens: int`

        Input tokens consumed by this request.

      - `output_tokens: int`

        Output tokens generated by this request.

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `class BetaManagedAgentsSpanModelRequestStartEvent: …`

    Emitted when a model request is initiated by the agent.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.model_request_start"]`

      - `"span.model_request_start"`

  - `class BetaManagedAgentsSpanModelRequestEndEvent: …`

    Emitted when a model request completes.

    - `id: str`

      Unique identifier for this event.

    - `is_error: Optional[bool]`

      Whether the model request resulted in an error.

    - `model_request_start_id: str`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.model_request_end"]`

      - `"span.model_request_end"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent: …`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.outcome_evaluation_ongoing"]`

      - `"span.outcome_evaluation_ongoing"`

  - `class BetaManagedAgentsUserDefineOutcomeEvent: …`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: str`

      Unique identifier for this event.

    - `description: str`

      What the agent should produce. Copied from the input event.

    - `max_iterations: Optional[int]`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `outcome_id: str`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric: …`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: str`

          ID of the rubric file.

        - `type: Literal["file"]`

          - `"file"`

      - `class BetaManagedAgentsTextRubric: …`

        Rubric content provided inline as text.

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: Literal["text"]`

          - `"text"`

    - `type: Literal["user.define_outcome"]`

      - `"user.define_outcome"`

  - `class BetaManagedAgentsSessionDeletedEvent: …`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.deleted"]`

      - `"session.deleted"`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent: …`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that started running.

    - `type: Literal["session.thread_status_running"]`

      - `"session.thread_status_running"`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent: …`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

    - `type: Literal["session.thread_status_idle"]`

      - `"session.thread_status_idle"`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent: …`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that terminated.

    - `type: Literal["session.thread_status_terminated"]`

      - `"session.thread_status_terminated"`

  - `class BetaManagedAgentsUserToolResultEvent: …`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: str`

      Unique identifier for this event.

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_result"]`

      - `"user.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent: …`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that is retrying.

    - `type: Literal["session.thread_status_rescheduled"]`

      - `"session.thread_status_rescheduled"`

  - `class BetaManagedAgentsSessionUpdatedEvent: …`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.updated"]`

      - `"session.updated"`

    - `agent: Optional[BetaManagedAgentsSessionAgent]`

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

          - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `claude-sonnet-5` - High-performance model for coding and agents
            - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
            - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
            - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
            - `claude-opus-4-6` - Most intelligent model for building agents and coding
            - `claude-sonnet-4-6` - Best combination of speed and intelligence
            - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
            - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
            - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
            - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
            - `claude-sonnet-4-5` - High-performance model for agents and coding
            - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

            - `"claude-sonnet-5"`

              High-performance model for coding and agents

            - `"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `"claude-opus-4-8"`

              Frontier intelligence for long-running agents and coding

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

            - `url: str`

          - `model: BetaManagedAgentsModelConfig`

            Model identifier and configuration.

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

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

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

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `mcp_server_name: str`

              - `type: Literal["mcp_toolset"]`

                - `"mcp_toolset"`

            - `class BetaManagedAgentsCustomTool: …`

              A custom tool as returned in API responses.

              - `description: str`

              - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `type: Literal["object"]`

                  - `"object"`

                - `properties: Optional[Dict[str, object]]`

                - `required: Optional[List[str]]`

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

        - `class BetaManagedAgentsCustomSkill: …`

          A resolved user-created custom skill.

      - `system: Optional[str]`

      - `tools: List[Tool]`

        - `class BetaManagedAgentsAgentToolset20260401: …`

        - `class BetaManagedAgentsMCPToolset: …`

        - `class BetaManagedAgentsCustomTool: …`

          A custom tool as returned in API responses.

      - `type: Literal["agent"]`

        - `"agent"`

      - `version: int`

    - `metadata: Optional[Dict[str, str]]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: Optional[str]`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent: …`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `event: BetaManagedAgentsStartEventPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `class BetaManagedAgentsAgentMessagePreview: …`

        - `id: str`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `type: Literal["agent.message"]`

          - `"agent.message"`

      - `class BetaManagedAgentsAgentThinkingPreview: …`

        - `id: str`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `type: Literal["agent.thinking"]`

          - `"agent.thinking"`

    - `type: Literal["event_start"]`

      - `"event_start"`

  - `class BetaManagedAgentsDeltaEvent: …`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `delta: BetaManagedAgentsDeltaContent`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `content: BetaManagedAgentsTextBlock`

        Regular text content.

      - `type: Literal["content_delta"]`

        - `"content_delta"`

      - `index: Optional[int]`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

    - `event_id: str`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `type: Literal["event_delta"]`

      - `"event_delta"`

  - `class BetaManagedAgentsSystemMessageEvent: …`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks. Text-only.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `type: Literal["system.message"]`

      - `"system.message"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
for event in client.beta.sessions.events.stream(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
):
  print(event)
```

#### Response

```json
{
  "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
  "content": [
    {
      "text": "Where is my order #1234?",
      "type": "text"
    }
  ],
  "type": "user.message",
  "processed_at": "2026-03-15T10:00:00Z"
}
```

## Domain Types

### Beta Managed Agents Agent Custom Tool Use Event

- `class BetaManagedAgentsAgentCustomToolUseEvent: …`

  Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

  - `id: str`

    Unique identifier for this event.

  - `input: Dict[str, object]`

    Input parameters for the tool call.

  - `name: str`

    Name of the custom tool being called.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `type: Literal["agent.custom_tool_use"]`

    - `"agent.custom_tool_use"`

  - `session_thread_id: Optional[str]`

    When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

### Beta Managed Agents Agent MCP Tool Result Event

- `class BetaManagedAgentsAgentMCPToolResultEvent: …`

  Event representing the result of an MCP tool execution.

  - `id: str`

    Unique identifier for this event.

  - `mcp_tool_use_id: str`

    The id of the `agent.mcp_tool_use` event this result corresponds to.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `type: Literal["agent.mcp_tool_result"]`

    - `"agent.mcp_tool_result"`

  - `content: Optional[List[Content]]`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock: …`

      Regular text content.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `class BetaManagedAgentsImageBlock: …`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: Source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource: …`

          Base64-encoded image data.

          - `data: str`

            Base64-encoded image data.

          - `media_type: str`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: Literal["base64"]`

            - `"base64"`

        - `class BetaManagedAgentsURLImageSource: …`

          Image referenced by URL.

          - `type: Literal["url"]`

            - `"url"`

          - `url: str`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource: …`

          Image referenced by file ID.

          - `file_id: str`

            ID of a previously uploaded file.

          - `type: Literal["file"]`

            - `"file"`

      - `type: Literal["image"]`

        - `"image"`

    - `class BetaManagedAgentsDocumentBlock: …`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: Source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource: …`

          Base64-encoded document data.

          - `data: str`

            Base64-encoded document data.

          - `media_type: str`

            MIME type of the document (e.g., "application/pdf").

          - `type: Literal["base64"]`

            - `"base64"`

        - `class BetaManagedAgentsPlainTextDocumentSource: …`

          Plain text document content.

          - `data: str`

            The plain text content.

          - `media_type: Literal["text/plain"]`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsURLDocumentSource: …`

          Document referenced by URL.

          - `type: Literal["url"]`

            - `"url"`

          - `url: str`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource: …`

          Document referenced by file ID.

          - `file_id: str`

            ID of a previously uploaded file.

          - `type: Literal["file"]`

            - `"file"`

      - `type: Literal["document"]`

        - `"document"`

      - `context: Optional[str]`

        Additional context about the document for the model.

      - `title: Optional[str]`

        The title of the document.

    - `class BetaManagedAgentsSearchResultBlock: …`

      A block containing a web search result.

      - `citations: BetaManagedAgentsSearchResultCitations`

        Citation settings for a search result.

        - `enabled: bool`

          Whether citations are enabled for this search result.

      - `content: List[BetaManagedAgentsSearchResultContent]`

        Array of text content blocks from the search result.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `source: str`

        The URL source of the search result.

      - `title: str`

        The title of the search result.

      - `type: Literal["search_result"]`

        - `"search_result"`

  - `is_error: Optional[bool]`

    Whether the tool execution resulted in an error.

### Beta Managed Agents Agent MCP Tool Use Event

- `class BetaManagedAgentsAgentMCPToolUseEvent: …`

  Event emitted when the agent invokes a tool provided by an MCP server.

  - `id: str`

    Unique identifier for this event.

  - `input: Dict[str, object]`

    Input parameters for the tool call.

  - `mcp_server_name: str`

    Name of the MCP server providing the tool.

  - `name: str`

    Name of the MCP tool being used.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `type: Literal["agent.mcp_tool_use"]`

    - `"agent.mcp_tool_use"`

  - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

    AgentEvaluatedPermission enum

    - `"allow"`

    - `"ask"`

    - `"deny"`

  - `session_thread_id: Optional[str]`

    When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

### Beta Managed Agents Agent Message Event

- `class BetaManagedAgentsAgentMessageEvent: …`

  An agent response event in the session conversation.

  - `id: str`

    Unique identifier for this event.

  - `content: List[BetaManagedAgentsTextBlock]`

    Array of text blocks comprising the agent response.

    - `text: str`

      The text content.

    - `type: Literal["text"]`

      - `"text"`

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `type: Literal["agent.message"]`

    - `"agent.message"`

### Beta Managed Agents Agent Thinking Event

- `class BetaManagedAgentsAgentThinkingEvent: …`

  Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

  - `id: str`

    Unique identifier for this event.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `type: Literal["agent.thinking"]`

    - `"agent.thinking"`

### Beta Managed Agents Agent Thread Context Compacted Event

- `class BetaManagedAgentsAgentThreadContextCompactedEvent: …`

  Indicates that context compaction (summarization) occurred during the session.

  - `id: str`

    Unique identifier for this event.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `type: Literal["agent.thread_context_compacted"]`

    - `"agent.thread_context_compacted"`

### Beta Managed Agents Agent Thread Message Received Event

- `class BetaManagedAgentsAgentThreadMessageReceivedEvent: …`

  Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

  - `id: str`

    Unique identifier for this event.

  - `content: List[Content]`

    Message content blocks.

    - `class BetaManagedAgentsTextBlock: …`

      Regular text content.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `class BetaManagedAgentsImageBlock: …`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: Source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource: …`

          Base64-encoded image data.

          - `data: str`

            Base64-encoded image data.

          - `media_type: str`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: Literal["base64"]`

            - `"base64"`

        - `class BetaManagedAgentsURLImageSource: …`

          Image referenced by URL.

          - `type: Literal["url"]`

            - `"url"`

          - `url: str`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource: …`

          Image referenced by file ID.

          - `file_id: str`

            ID of a previously uploaded file.

          - `type: Literal["file"]`

            - `"file"`

      - `type: Literal["image"]`

        - `"image"`

    - `class BetaManagedAgentsDocumentBlock: …`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: Source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource: …`

          Base64-encoded document data.

          - `data: str`

            Base64-encoded document data.

          - `media_type: str`

            MIME type of the document (e.g., "application/pdf").

          - `type: Literal["base64"]`

            - `"base64"`

        - `class BetaManagedAgentsPlainTextDocumentSource: …`

          Plain text document content.

          - `data: str`

            The plain text content.

          - `media_type: Literal["text/plain"]`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsURLDocumentSource: …`

          Document referenced by URL.

          - `type: Literal["url"]`

            - `"url"`

          - `url: str`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource: …`

          Document referenced by file ID.

          - `file_id: str`

            ID of a previously uploaded file.

          - `type: Literal["file"]`

            - `"file"`

      - `type: Literal["document"]`

        - `"document"`

      - `context: Optional[str]`

        Additional context about the document for the model.

      - `title: Optional[str]`

        The title of the document.

  - `from_session_thread_id: str`

    Public `sthr_` ID of the thread that sent the message.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `type: Literal["agent.thread_message_received"]`

    - `"agent.thread_message_received"`

  - `from_agent_name: Optional[str]`

    Name of the callable agent this message came from. Absent when received from the primary agent.

### Beta Managed Agents Agent Thread Message Sent Event

- `class BetaManagedAgentsAgentThreadMessageSentEvent: …`

  Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

  - `id: str`

    Unique identifier for this event.

  - `content: List[Content]`

    Message content blocks.

    - `class BetaManagedAgentsTextBlock: …`

      Regular text content.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `class BetaManagedAgentsImageBlock: …`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: Source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource: …`

          Base64-encoded image data.

          - `data: str`

            Base64-encoded image data.

          - `media_type: str`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: Literal["base64"]`

            - `"base64"`

        - `class BetaManagedAgentsURLImageSource: …`

          Image referenced by URL.

          - `type: Literal["url"]`

            - `"url"`

          - `url: str`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource: …`

          Image referenced by file ID.

          - `file_id: str`

            ID of a previously uploaded file.

          - `type: Literal["file"]`

            - `"file"`

      - `type: Literal["image"]`

        - `"image"`

    - `class BetaManagedAgentsDocumentBlock: …`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: Source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource: …`

          Base64-encoded document data.

          - `data: str`

            Base64-encoded document data.

          - `media_type: str`

            MIME type of the document (e.g., "application/pdf").

          - `type: Literal["base64"]`

            - `"base64"`

        - `class BetaManagedAgentsPlainTextDocumentSource: …`

          Plain text document content.

          - `data: str`

            The plain text content.

          - `media_type: Literal["text/plain"]`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsURLDocumentSource: …`

          Document referenced by URL.

          - `type: Literal["url"]`

            - `"url"`

          - `url: str`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource: …`

          Document referenced by file ID.

          - `file_id: str`

            ID of a previously uploaded file.

          - `type: Literal["file"]`

            - `"file"`

      - `type: Literal["document"]`

        - `"document"`

      - `context: Optional[str]`

        Additional context about the document for the model.

      - `title: Optional[str]`

        The title of the document.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `to_session_thread_id: str`

    Public `sthr_` ID of the thread the message was sent to.

  - `type: Literal["agent.thread_message_sent"]`

    - `"agent.thread_message_sent"`

  - `to_agent_name: Optional[str]`

    Name of the callable agent this message was sent to. Absent when sent to the primary agent.

### Beta Managed Agents Agent Tool Result Event

- `class BetaManagedAgentsAgentToolResultEvent: …`

  Event representing the result of an agent tool execution.

  - `id: str`

    Unique identifier for this event.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `tool_use_id: str`

    The id of the `agent.tool_use` event this result corresponds to.

  - `type: Literal["agent.tool_result"]`

    - `"agent.tool_result"`

  - `content: Optional[List[Content]]`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock: …`

      Regular text content.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `class BetaManagedAgentsImageBlock: …`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: Source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource: …`

          Base64-encoded image data.

          - `data: str`

            Base64-encoded image data.

          - `media_type: str`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: Literal["base64"]`

            - `"base64"`

        - `class BetaManagedAgentsURLImageSource: …`

          Image referenced by URL.

          - `type: Literal["url"]`

            - `"url"`

          - `url: str`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource: …`

          Image referenced by file ID.

          - `file_id: str`

            ID of a previously uploaded file.

          - `type: Literal["file"]`

            - `"file"`

      - `type: Literal["image"]`

        - `"image"`

    - `class BetaManagedAgentsDocumentBlock: …`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: Source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource: …`

          Base64-encoded document data.

          - `data: str`

            Base64-encoded document data.

          - `media_type: str`

            MIME type of the document (e.g., "application/pdf").

          - `type: Literal["base64"]`

            - `"base64"`

        - `class BetaManagedAgentsPlainTextDocumentSource: …`

          Plain text document content.

          - `data: str`

            The plain text content.

          - `media_type: Literal["text/plain"]`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsURLDocumentSource: …`

          Document referenced by URL.

          - `type: Literal["url"]`

            - `"url"`

          - `url: str`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource: …`

          Document referenced by file ID.

          - `file_id: str`

            ID of a previously uploaded file.

          - `type: Literal["file"]`

            - `"file"`

      - `type: Literal["document"]`

        - `"document"`

      - `context: Optional[str]`

        Additional context about the document for the model.

      - `title: Optional[str]`

        The title of the document.

    - `class BetaManagedAgentsSearchResultBlock: …`

      A block containing a web search result.

      - `citations: BetaManagedAgentsSearchResultCitations`

        Citation settings for a search result.

        - `enabled: bool`

          Whether citations are enabled for this search result.

      - `content: List[BetaManagedAgentsSearchResultContent]`

        Array of text content blocks from the search result.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `source: str`

        The URL source of the search result.

      - `title: str`

        The title of the search result.

      - `type: Literal["search_result"]`

        - `"search_result"`

  - `is_error: Optional[bool]`

    Whether the tool execution resulted in an error.

### Beta Managed Agents Agent Tool Use Event

- `class BetaManagedAgentsAgentToolUseEvent: …`

  Event emitted when the agent invokes a built-in agent tool.

  - `id: str`

    Unique identifier for this event.

  - `input: Dict[str, object]`

    Input parameters for the tool call.

  - `name: str`

    Name of the agent tool being used.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `type: Literal["agent.tool_use"]`

    - `"agent.tool_use"`

  - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

    AgentEvaluatedPermission enum

    - `"allow"`

    - `"ask"`

    - `"deny"`

  - `session_thread_id: Optional[str]`

    When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

### Beta Managed Agents Base64 Document Source

- `class BetaManagedAgentsBase64DocumentSource: …`

  Base64-encoded document data.

  - `data: str`

    Base64-encoded document data.

  - `media_type: str`

    MIME type of the document (e.g., "application/pdf").

  - `type: Literal["base64"]`

    - `"base64"`

### Beta Managed Agents Base64 Image Source

- `class BetaManagedAgentsBase64ImageSource: …`

  Base64-encoded image data.

  - `data: str`

    Base64-encoded image data.

  - `media_type: str`

    MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

  - `type: Literal["base64"]`

    - `"base64"`

### Beta Managed Agents Billing Error

- `class BetaManagedAgentsBillingError: …`

  The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

  - `message: str`

    Human-readable error description.

  - `retry_status: RetryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying: …`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: Literal["retrying"]`

        - `"retrying"`

    - `class BetaManagedAgentsRetryStatusExhausted: …`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: Literal["exhausted"]`

        - `"exhausted"`

    - `class BetaManagedAgentsRetryStatusTerminal: …`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: Literal["terminal"]`

        - `"terminal"`

  - `type: Literal["billing_error"]`

    - `"billing_error"`

### Beta Managed Agents Credential Host Unreachable Error

- `class BetaManagedAgentsCredentialHostUnreachableError: …`

  An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

  - `credential_id: str`

    ID of the affected credential.

  - `message: str`

    Human-readable error description.

  - `retry_status: RetryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying: …`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: Literal["retrying"]`

        - `"retrying"`

    - `class BetaManagedAgentsRetryStatusExhausted: …`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: Literal["exhausted"]`

        - `"exhausted"`

    - `class BetaManagedAgentsRetryStatusTerminal: …`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: Literal["terminal"]`

        - `"terminal"`

  - `type: Literal["credential_host_unreachable_error"]`

    - `"credential_host_unreachable_error"`

  - `vault_id: str`

    ID of the vault containing the affected credential.

### Beta Managed Agents Document Block

- `class BetaManagedAgentsDocumentBlock: …`

  Document content, either specified directly as base64 data, as text, or as a reference via a URL.

  - `source: Source`

    Union type for document source variants.

    - `class BetaManagedAgentsBase64DocumentSource: …`

      Base64-encoded document data.

      - `data: str`

        Base64-encoded document data.

      - `media_type: str`

        MIME type of the document (e.g., "application/pdf").

      - `type: Literal["base64"]`

        - `"base64"`

    - `class BetaManagedAgentsPlainTextDocumentSource: …`

      Plain text document content.

      - `data: str`

        The plain text content.

      - `media_type: Literal["text/plain"]`

        MIME type of the text content. Must be "text/plain".

        - `"text/plain"`

      - `type: Literal["text"]`

        - `"text"`

    - `class BetaManagedAgentsURLDocumentSource: …`

      Document referenced by URL.

      - `type: Literal["url"]`

        - `"url"`

      - `url: str`

        URL of the document to fetch.

    - `class BetaManagedAgentsFileDocumentSource: …`

      Document referenced by file ID.

      - `file_id: str`

        ID of a previously uploaded file.

      - `type: Literal["file"]`

        - `"file"`

  - `type: Literal["document"]`

    - `"document"`

  - `context: Optional[str]`

    Additional context about the document for the model.

  - `title: Optional[str]`

    The title of the document.

### Beta Managed Agents Event Params

- `BetaManagedAgentsEventParams`

  Union type for event parameters that can be sent to a session.

  - `class BetaManagedAgentsUserMessageEventParams: …`

    Parameters for sending a user message to the session.

    - `content: List[Content]`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `data: str`

              Base64-encoded image data.

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["image"]`

          - `"image"`

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `data: str`

              Base64-encoded document data.

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `data: str`

              The plain text content.

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: Literal["text"]`

              - `"text"`

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["document"]`

          - `"document"`

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

    - `type: Literal["user.message"]`

      - `"user.message"`

  - `class BetaManagedAgentsUserInterruptEventParams: …`

    Parameters for sending an interrupt to pause the agent.

    - `type: Literal["user.interrupt"]`

      - `"user.interrupt"`

    - `session_thread_id: Optional[str]`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEventParams: …`

    Parameters for confirming or denying a tool execution request.

    - `result: Literal["allow", "deny"]`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: str`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_confirmation"]`

      - `"user.tool_confirmation"`

    - `deny_message: Optional[str]`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

  - `class BetaManagedAgentsUserCustomToolResultEventParams: …`

    Parameters for providing the result of a custom tool execution.

    - `custom_tool_use_id: str`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.custom_tool_result"]`

      - `"user.custom_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: bool`

            Whether citations are enabled for this search result.

        - `content: List[BetaManagedAgentsSearchResultContent]`

          Array of text content blocks from the search result.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `source: str`

          The URL source of the search result.

        - `title: str`

          The title of the search result.

        - `type: Literal["search_result"]`

          - `"search_result"`

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsUserDefineOutcomeEventParams: …`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `description: str`

      What the agent should produce. This is the task specification.

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubricParams: …`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: str`

          ID of the rubric file.

        - `type: Literal["file"]`

          - `"file"`

      - `class BetaManagedAgentsTextRubricParams: …`

        Rubric content provided inline as text.

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

        - `type: Literal["text"]`

          - `"text"`

    - `type: Literal["user.define_outcome"]`

      - `"user.define_outcome"`

    - `max_iterations: Optional[int]`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `class BetaManagedAgentsUserToolResultEventParams: …`

    Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_result"]`

      - `"user.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsSystemMessageEventParams: …`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks to append. Text-only.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `type: Literal["system.message"]`

      - `"system.message"`

### Beta Managed Agents File Document Source

- `class BetaManagedAgentsFileDocumentSource: …`

  Document referenced by file ID.

  - `file_id: str`

    ID of a previously uploaded file.

  - `type: Literal["file"]`

    - `"file"`

### Beta Managed Agents File Image Source

- `class BetaManagedAgentsFileImageSource: …`

  Image referenced by file ID.

  - `file_id: str`

    ID of a previously uploaded file.

  - `type: Literal["file"]`

    - `"file"`

### Beta Managed Agents File Rubric

- `class BetaManagedAgentsFileRubric: …`

  Rubric referenced by a file uploaded via the Files API.

  - `file_id: str`

    ID of the rubric file.

  - `type: Literal["file"]`

    - `"file"`

### Beta Managed Agents File Rubric Params

- `class BetaManagedAgentsFileRubricParams: …`

  Rubric referenced by a file uploaded via the Files API.

  - `file_id: str`

    ID of the rubric file.

  - `type: Literal["file"]`

    - `"file"`

### Beta Managed Agents Image Block

- `class BetaManagedAgentsImageBlock: …`

  Image content specified directly as base64 data or as a reference via a URL.

  - `source: Source`

    Union type for image source variants.

    - `class BetaManagedAgentsBase64ImageSource: …`

      Base64-encoded image data.

      - `data: str`

        Base64-encoded image data.

      - `media_type: str`

        MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

      - `type: Literal["base64"]`

        - `"base64"`

    - `class BetaManagedAgentsURLImageSource: …`

      Image referenced by URL.

      - `type: Literal["url"]`

        - `"url"`

      - `url: str`

        URL of the image to fetch.

    - `class BetaManagedAgentsFileImageSource: …`

      Image referenced by file ID.

      - `file_id: str`

        ID of a previously uploaded file.

      - `type: Literal["file"]`

        - `"file"`

  - `type: Literal["image"]`

    - `"image"`

### Beta Managed Agents MCP Authentication Failed Error

- `class BetaManagedAgentsMCPAuthenticationFailedError: …`

  Authentication to an MCP server failed.

  - `mcp_server_name: str`

    Name of the MCP server that failed authentication.

  - `message: str`

    Human-readable error description.

  - `retry_status: RetryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying: …`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: Literal["retrying"]`

        - `"retrying"`

    - `class BetaManagedAgentsRetryStatusExhausted: …`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: Literal["exhausted"]`

        - `"exhausted"`

    - `class BetaManagedAgentsRetryStatusTerminal: …`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: Literal["terminal"]`

        - `"terminal"`

  - `type: Literal["mcp_authentication_failed_error"]`

    - `"mcp_authentication_failed_error"`

### Beta Managed Agents MCP Connection Failed Error

- `class BetaManagedAgentsMCPConnectionFailedError: …`

  Failed to connect to an MCP server.

  - `mcp_server_name: str`

    Name of the MCP server that failed to connect.

  - `message: str`

    Human-readable error description.

  - `retry_status: RetryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying: …`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: Literal["retrying"]`

        - `"retrying"`

    - `class BetaManagedAgentsRetryStatusExhausted: …`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: Literal["exhausted"]`

        - `"exhausted"`

    - `class BetaManagedAgentsRetryStatusTerminal: …`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: Literal["terminal"]`

        - `"terminal"`

  - `type: Literal["mcp_connection_failed_error"]`

    - `"mcp_connection_failed_error"`

### Beta Managed Agents Model Overloaded Error

- `class BetaManagedAgentsModelOverloadedError: …`

  The model is currently overloaded. Emitted after automatic retries are exhausted.

  - `message: str`

    Human-readable error description.

  - `retry_status: RetryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying: …`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: Literal["retrying"]`

        - `"retrying"`

    - `class BetaManagedAgentsRetryStatusExhausted: …`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: Literal["exhausted"]`

        - `"exhausted"`

    - `class BetaManagedAgentsRetryStatusTerminal: …`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: Literal["terminal"]`

        - `"terminal"`

  - `type: Literal["model_overloaded_error"]`

    - `"model_overloaded_error"`

### Beta Managed Agents Model Rate Limited Error

- `class BetaManagedAgentsModelRateLimitedError: …`

  The model request was rate-limited.

  - `message: str`

    Human-readable error description.

  - `retry_status: RetryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying: …`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: Literal["retrying"]`

        - `"retrying"`

    - `class BetaManagedAgentsRetryStatusExhausted: …`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: Literal["exhausted"]`

        - `"exhausted"`

    - `class BetaManagedAgentsRetryStatusTerminal: …`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: Literal["terminal"]`

        - `"terminal"`

  - `type: Literal["model_rate_limited_error"]`

    - `"model_rate_limited_error"`

### Beta Managed Agents Model Request Failed Error

- `class BetaManagedAgentsModelRequestFailedError: …`

  A model request failed for a reason other than overload or rate-limiting.

  - `message: str`

    Human-readable error description.

  - `retry_status: RetryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying: …`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: Literal["retrying"]`

        - `"retrying"`

    - `class BetaManagedAgentsRetryStatusExhausted: …`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: Literal["exhausted"]`

        - `"exhausted"`

    - `class BetaManagedAgentsRetryStatusTerminal: …`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: Literal["terminal"]`

        - `"terminal"`

  - `type: Literal["model_request_failed_error"]`

    - `"model_request_failed_error"`

### Beta Managed Agents Plain Text Document Source

- `class BetaManagedAgentsPlainTextDocumentSource: …`

  Plain text document content.

  - `data: str`

    The plain text content.

  - `media_type: Literal["text/plain"]`

    MIME type of the text content. Must be "text/plain".

    - `"text/plain"`

  - `type: Literal["text"]`

    - `"text"`

### Beta Managed Agents Retry Status Exhausted

- `class BetaManagedAgentsRetryStatusExhausted: …`

  This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

  - `type: Literal["exhausted"]`

    - `"exhausted"`

### Beta Managed Agents Retry Status Retrying

- `class BetaManagedAgentsRetryStatusRetrying: …`

  The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

  - `type: Literal["retrying"]`

    - `"retrying"`

### Beta Managed Agents Retry Status Terminal

- `class BetaManagedAgentsRetryStatusTerminal: …`

  The session encountered a terminal error and will transition to `terminated` state.

  - `type: Literal["terminal"]`

    - `"terminal"`

### Beta Managed Agents Search Result Block

- `class BetaManagedAgentsSearchResultBlock: …`

  A block containing a web search result.

  - `citations: BetaManagedAgentsSearchResultCitations`

    Citation settings for a search result.

    - `enabled: bool`

      Whether citations are enabled for this search result.

  - `content: List[BetaManagedAgentsSearchResultContent]`

    Array of text content blocks from the search result.

    - `text: str`

      The text content.

    - `type: Literal["text"]`

      - `"text"`

  - `source: str`

    The URL source of the search result.

  - `title: str`

    The title of the search result.

  - `type: Literal["search_result"]`

    - `"search_result"`

### Beta Managed Agents Search Result Citations

- `class BetaManagedAgentsSearchResultCitations: …`

  Citation settings for a search result.

  - `enabled: bool`

    Whether citations are enabled for this search result.

### Beta Managed Agents Search Result Content

- `class BetaManagedAgentsSearchResultContent: …`

  Text content within a search result.

  - `text: str`

    The text content.

  - `type: Literal["text"]`

    - `"text"`

### Beta Managed Agents Send Session Events

- `class BetaManagedAgentsSendSessionEvents: …`

  Events that were successfully sent to the session.

  - `data: Optional[List[Data]]`

    Sent events

    - `class BetaManagedAgentsUserMessageEvent: …`

      A user message event in the session conversation.

      - `id: str`

        Unique identifier for this event.

      - `content: List[Content]`

        Array of content blocks comprising the user message.

        - `class BetaManagedAgentsTextBlock: …`

          Regular text content.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsImageBlock: …`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource: …`

              Base64-encoded image data.

              - `data: str`

                Base64-encoded image data.

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsURLImageSource: …`

              Image referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource: …`

              Image referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["image"]`

            - `"image"`

        - `class BetaManagedAgentsDocumentBlock: …`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource: …`

              Base64-encoded document data.

              - `data: str`

                Base64-encoded document data.

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsPlainTextDocumentSource: …`

              Plain text document content.

              - `data: str`

                The plain text content.

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: Literal["text"]`

                - `"text"`

            - `class BetaManagedAgentsURLDocumentSource: …`

              Document referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource: …`

              Document referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["document"]`

            - `"document"`

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

      - `type: Literal["user.message"]`

        - `"user.message"`

      - `processed_at: Optional[datetime]`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserInterruptEvent: …`

      An interrupt event that pauses agent execution and returns control to the user.

      - `id: str`

        Unique identifier for this event.

      - `type: Literal["user.interrupt"]`

        - `"user.interrupt"`

      - `processed_at: Optional[datetime]`

        A timestamp in RFC 3339 format

      - `session_thread_id: Optional[str]`

        If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

    - `class BetaManagedAgentsUserToolConfirmationEvent: …`

      A tool confirmation event that approves or denies a pending tool execution.

      - `id: str`

        Unique identifier for this event.

      - `result: Literal["allow", "deny"]`

        UserToolConfirmationResult enum

        - `"allow"`

        - `"deny"`

      - `tool_use_id: str`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: Literal["user.tool_confirmation"]`

        - `"user.tool_confirmation"`

      - `deny_message: Optional[str]`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      - `processed_at: Optional[datetime]`

        A timestamp in RFC 3339 format

      - `session_thread_id: Optional[str]`

        When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

    - `class BetaManagedAgentsUserCustomToolResultEvent: …`

      Event sent by the client providing the result of a custom tool execution.

      - `id: str`

        Unique identifier for this event.

      - `custom_tool_use_id: str`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: Literal["user.custom_tool_result"]`

        - `"user.custom_tool_result"`

      - `content: Optional[List[Content]]`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock: …`

          Regular text content.

        - `class BetaManagedAgentsImageBlock: …`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock: …`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsSearchResultBlock: …`

          A block containing a web search result.

          - `citations: BetaManagedAgentsSearchResultCitations`

            Citation settings for a search result.

            - `enabled: bool`

              Whether citations are enabled for this search result.

          - `content: List[BetaManagedAgentsSearchResultContent]`

            Array of text content blocks from the search result.

            - `text: str`

              The text content.

            - `type: Literal["text"]`

              - `"text"`

          - `source: str`

            The URL source of the search result.

          - `title: str`

            The title of the search result.

          - `type: Literal["search_result"]`

            - `"search_result"`

      - `is_error: Optional[bool]`

        Whether the tool execution resulted in an error.

      - `processed_at: Optional[datetime]`

        A timestamp in RFC 3339 format

      - `session_thread_id: Optional[str]`

        Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

    - `class BetaManagedAgentsUserDefineOutcomeEvent: …`

      Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

      - `id: str`

        Unique identifier for this event.

      - `description: str`

        What the agent should produce. Copied from the input event.

      - `max_iterations: Optional[int]`

        Evaluate-then-revise cycles before giving up. Default 3, max 20.

      - `outcome_id: str`

        Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

      - `processed_at: datetime`

        A timestamp in RFC 3339 format

      - `rubric: Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric: …`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: str`

            ID of the rubric file.

          - `type: Literal["file"]`

            - `"file"`

        - `class BetaManagedAgentsTextRubric: …`

          Rubric content provided inline as text.

          - `content: str`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: Literal["text"]`

            - `"text"`

      - `type: Literal["user.define_outcome"]`

        - `"user.define_outcome"`

    - `class BetaManagedAgentsUserToolResultEvent: …`

      Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

      - `id: str`

        Unique identifier for this event.

      - `tool_use_id: str`

        The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: Literal["user.tool_result"]`

        - `"user.tool_result"`

      - `content: Optional[List[Content]]`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock: …`

          Regular text content.

        - `class BetaManagedAgentsImageBlock: …`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock: …`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsSearchResultBlock: …`

          A block containing a web search result.

      - `is_error: Optional[bool]`

        Whether the tool execution resulted in an error.

      - `processed_at: Optional[datetime]`

        A timestamp in RFC 3339 format

      - `session_thread_id: Optional[str]`

        Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

    - `class BetaManagedAgentsSystemMessageEvent: …`

      A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

      - `id: str`

        Unique identifier for this event.

      - `content: List[BetaManagedAgentsSystemContentBlock]`

        System content blocks. Text-only.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `type: Literal["system.message"]`

        - `"system.message"`

      - `processed_at: Optional[datetime]`

        A timestamp in RFC 3339 format

### Beta Managed Agents Session Deleted Event

- `class BetaManagedAgentsSessionDeletedEvent: …`

  Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

  - `id: str`

    Unique identifier for this event.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `type: Literal["session.deleted"]`

    - `"session.deleted"`

### Beta Managed Agents Session End Turn

- `class BetaManagedAgentsSessionEndTurn: …`

  The agent completed its turn naturally and is ready for the next user message.

  - `type: Literal["end_turn"]`

    - `"end_turn"`

### Beta Managed Agents Session Error Event

- `class BetaManagedAgentsSessionErrorEvent: …`

  An error event indicating a problem occurred during session execution.

  - `id: str`

    Unique identifier for this event.

  - `error: Error`

    An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

    - `class BetaManagedAgentsUnknownError: …`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `message: str`

        Human-readable error description.

      - `retry_status: RetryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying: …`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: Literal["retrying"]`

            - `"retrying"`

        - `class BetaManagedAgentsRetryStatusExhausted: …`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: Literal["exhausted"]`

            - `"exhausted"`

        - `class BetaManagedAgentsRetryStatusTerminal: …`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: Literal["terminal"]`

            - `"terminal"`

      - `type: Literal["unknown_error"]`

        - `"unknown_error"`

    - `class BetaManagedAgentsModelOverloadedError: …`

      The model is currently overloaded. Emitted after automatic retries are exhausted.

      - `message: str`

        Human-readable error description.

      - `retry_status: RetryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying: …`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `class BetaManagedAgentsRetryStatusExhausted: …`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `class BetaManagedAgentsRetryStatusTerminal: …`

          The session encountered a terminal error and will transition to `terminated` state.

      - `type: Literal["model_overloaded_error"]`

        - `"model_overloaded_error"`

    - `class BetaManagedAgentsModelRateLimitedError: …`

      The model request was rate-limited.

      - `message: str`

        Human-readable error description.

      - `retry_status: RetryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying: …`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `class BetaManagedAgentsRetryStatusExhausted: …`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `class BetaManagedAgentsRetryStatusTerminal: …`

          The session encountered a terminal error and will transition to `terminated` state.

      - `type: Literal["model_rate_limited_error"]`

        - `"model_rate_limited_error"`

    - `class BetaManagedAgentsModelRequestFailedError: …`

      A model request failed for a reason other than overload or rate-limiting.

      - `message: str`

        Human-readable error description.

      - `retry_status: RetryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying: …`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `class BetaManagedAgentsRetryStatusExhausted: …`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `class BetaManagedAgentsRetryStatusTerminal: …`

          The session encountered a terminal error and will transition to `terminated` state.

      - `type: Literal["model_request_failed_error"]`

        - `"model_request_failed_error"`

    - `class BetaManagedAgentsMCPConnectionFailedError: …`

      Failed to connect to an MCP server.

      - `mcp_server_name: str`

        Name of the MCP server that failed to connect.

      - `message: str`

        Human-readable error description.

      - `retry_status: RetryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying: …`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `class BetaManagedAgentsRetryStatusExhausted: …`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `class BetaManagedAgentsRetryStatusTerminal: …`

          The session encountered a terminal error and will transition to `terminated` state.

      - `type: Literal["mcp_connection_failed_error"]`

        - `"mcp_connection_failed_error"`

    - `class BetaManagedAgentsMCPAuthenticationFailedError: …`

      Authentication to an MCP server failed.

      - `mcp_server_name: str`

        Name of the MCP server that failed authentication.

      - `message: str`

        Human-readable error description.

      - `retry_status: RetryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying: …`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `class BetaManagedAgentsRetryStatusExhausted: …`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `class BetaManagedAgentsRetryStatusTerminal: …`

          The session encountered a terminal error and will transition to `terminated` state.

      - `type: Literal["mcp_authentication_failed_error"]`

        - `"mcp_authentication_failed_error"`

    - `class BetaManagedAgentsBillingError: …`

      The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

      - `message: str`

        Human-readable error description.

      - `retry_status: RetryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying: …`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `class BetaManagedAgentsRetryStatusExhausted: …`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `class BetaManagedAgentsRetryStatusTerminal: …`

          The session encountered a terminal error and will transition to `terminated` state.

      - `type: Literal["billing_error"]`

        - `"billing_error"`

    - `class BetaManagedAgentsCredentialHostUnreachableError: …`

      An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

      - `credential_id: str`

        ID of the affected credential.

      - `message: str`

        Human-readable error description.

      - `retry_status: RetryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying: …`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `class BetaManagedAgentsRetryStatusExhausted: …`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `class BetaManagedAgentsRetryStatusTerminal: …`

          The session encountered a terminal error and will transition to `terminated` state.

      - `type: Literal["credential_host_unreachable_error"]`

        - `"credential_host_unreachable_error"`

      - `vault_id: str`

        ID of the vault containing the affected credential.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `type: Literal["session.error"]`

    - `"session.error"`

### Beta Managed Agents Session Event

- `BetaManagedAgentsSessionEvent`

  Union type for all event types in a session.

  - `class BetaManagedAgentsUserMessageEvent: …`

    A user message event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `data: str`

              Base64-encoded image data.

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["image"]`

          - `"image"`

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `data: str`

              Base64-encoded document data.

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `data: str`

              The plain text content.

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: Literal["text"]`

              - `"text"`

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["document"]`

          - `"document"`

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

    - `type: Literal["user.message"]`

      - `"user.message"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent: …`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: str`

      Unique identifier for this event.

    - `type: Literal["user.interrupt"]`

      - `"user.interrupt"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent: …`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: str`

      Unique identifier for this event.

    - `result: Literal["allow", "deny"]`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: str`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_confirmation"]`

      - `"user.tool_confirmation"`

    - `deny_message: Optional[str]`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent: …`

    Event sent by the client providing the result of a custom tool execution.

    - `id: str`

      Unique identifier for this event.

    - `custom_tool_use_id: str`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.custom_tool_result"]`

      - `"user.custom_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: bool`

            Whether citations are enabled for this search result.

        - `content: List[BetaManagedAgentsSearchResultContent]`

          Array of text content blocks from the search result.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `source: str`

          The URL source of the search result.

        - `title: str`

          The title of the search result.

        - `type: Literal["search_result"]`

          - `"search_result"`

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent: …`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the custom tool being called.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.custom_tool_use"]`

      - `"agent.custom_tool_use"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent: …`

    An agent response event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsTextBlock]`

      Array of text blocks comprising the agent response.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.message"]`

      - `"agent.message"`

  - `class BetaManagedAgentsAgentThinkingEvent: …`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thinking"]`

      - `"agent.thinking"`

  - `class BetaManagedAgentsAgentMCPToolUseEvent: …`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `mcp_server_name: str`

      Name of the MCP server providing the tool.

    - `name: str`

      Name of the MCP tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.mcp_tool_use"]`

      - `"agent.mcp_tool_use"`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMCPToolResultEvent: …`

    Event representing the result of an MCP tool execution.

    - `id: str`

      Unique identifier for this event.

    - `mcp_tool_use_id: str`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.mcp_tool_result"]`

      - `"agent.mcp_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent: …`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the agent tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.tool_use"]`

      - `"agent.tool_use"`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent: …`

    Event representing the result of an agent tool execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: Literal["agent.tool_result"]`

      - `"agent.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent: …`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `from_session_thread_id: str`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thread_message_received"]`

      - `"agent.thread_message_received"`

    - `from_agent_name: Optional[str]`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent: …`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `to_session_thread_id: str`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: Literal["agent.thread_message_sent"]`

      - `"agent.thread_message_sent"`

    - `to_agent_name: Optional[str]`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent: …`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thread_context_compacted"]`

      - `"agent.thread_context_compacted"`

  - `class BetaManagedAgentsSessionErrorEvent: …`

    An error event indicating a problem occurred during session execution.

    - `id: str`

      Unique identifier for this event.

    - `error: Error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError: …`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: Literal["retrying"]`

              - `"retrying"`

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: Literal["exhausted"]`

              - `"exhausted"`

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: Literal["terminal"]`

              - `"terminal"`

        - `type: Literal["unknown_error"]`

          - `"unknown_error"`

      - `class BetaManagedAgentsModelOverloadedError: …`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_overloaded_error"]`

          - `"model_overloaded_error"`

      - `class BetaManagedAgentsModelRateLimitedError: …`

        The model request was rate-limited.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_rate_limited_error"]`

          - `"model_rate_limited_error"`

      - `class BetaManagedAgentsModelRequestFailedError: …`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_request_failed_error"]`

          - `"model_request_failed_error"`

      - `class BetaManagedAgentsMCPConnectionFailedError: …`

        Failed to connect to an MCP server.

        - `mcp_server_name: str`

          Name of the MCP server that failed to connect.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_connection_failed_error"]`

          - `"mcp_connection_failed_error"`

      - `class BetaManagedAgentsMCPAuthenticationFailedError: …`

        Authentication to an MCP server failed.

        - `mcp_server_name: str`

          Name of the MCP server that failed authentication.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_authentication_failed_error"]`

          - `"mcp_authentication_failed_error"`

      - `class BetaManagedAgentsBillingError: …`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["billing_error"]`

          - `"billing_error"`

      - `class BetaManagedAgentsCredentialHostUnreachableError: …`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: str`

          ID of the affected credential.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["credential_host_unreachable_error"]`

          - `"credential_host_unreachable_error"`

        - `vault_id: str`

          ID of the vault containing the affected credential.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.error"]`

      - `"session.error"`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent: …`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_rescheduled"]`

      - `"session.status_rescheduled"`

  - `class BetaManagedAgentsSessionStatusRunningEvent: …`

    Indicates the session is actively running and the agent is working.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_running"]`

      - `"session.status_running"`

  - `class BetaManagedAgentsSessionStatusIdleEvent: …`

    Indicates the agent has paused and is awaiting user input.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: Literal["end_turn"]`

          - `"end_turn"`

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: List[str]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: Literal["requires_action"]`

          - `"requires_action"`

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `type: Literal["retries_exhausted"]`

          - `"retries_exhausted"`

    - `type: Literal["session.status_idle"]`

      - `"session.status_idle"`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent: …`

    Indicates the session has terminated, either due to an error or completion.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_terminated"]`

      - `"session.status_terminated"`

  - `class BetaManagedAgentsSessionThreadCreatedEvent: …`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the callable agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public `sthr_` ID of the newly created thread.

    - `type: Literal["session.thread_created"]`

      - `"session.thread_created"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent: …`

    Emitted when an outcome evaluation cycle begins.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.outcome_evaluation_start"]`

      - `"span.outcome_evaluation_start"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent: …`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `id: str`

      Unique identifier for this event.

    - `explanation: str`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_evaluation_start_id: str`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `result: str`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `type: Literal["span.outcome_evaluation_end"]`

      - `"span.outcome_evaluation_end"`

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: int`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: int`

        Tokens read from prompt cache in this request.

      - `input_tokens: int`

        Input tokens consumed by this request.

      - `output_tokens: int`

        Output tokens generated by this request.

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `class BetaManagedAgentsSpanModelRequestStartEvent: …`

    Emitted when a model request is initiated by the agent.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.model_request_start"]`

      - `"span.model_request_start"`

  - `class BetaManagedAgentsSpanModelRequestEndEvent: …`

    Emitted when a model request completes.

    - `id: str`

      Unique identifier for this event.

    - `is_error: Optional[bool]`

      Whether the model request resulted in an error.

    - `model_request_start_id: str`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.model_request_end"]`

      - `"span.model_request_end"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent: …`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.outcome_evaluation_ongoing"]`

      - `"span.outcome_evaluation_ongoing"`

  - `class BetaManagedAgentsUserDefineOutcomeEvent: …`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: str`

      Unique identifier for this event.

    - `description: str`

      What the agent should produce. Copied from the input event.

    - `max_iterations: Optional[int]`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `outcome_id: str`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric: …`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: str`

          ID of the rubric file.

        - `type: Literal["file"]`

          - `"file"`

      - `class BetaManagedAgentsTextRubric: …`

        Rubric content provided inline as text.

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: Literal["text"]`

          - `"text"`

    - `type: Literal["user.define_outcome"]`

      - `"user.define_outcome"`

  - `class BetaManagedAgentsSessionDeletedEvent: …`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.deleted"]`

      - `"session.deleted"`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent: …`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that started running.

    - `type: Literal["session.thread_status_running"]`

      - `"session.thread_status_running"`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent: …`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

    - `type: Literal["session.thread_status_idle"]`

      - `"session.thread_status_idle"`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent: …`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that terminated.

    - `type: Literal["session.thread_status_terminated"]`

      - `"session.thread_status_terminated"`

  - `class BetaManagedAgentsUserToolResultEvent: …`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: str`

      Unique identifier for this event.

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_result"]`

      - `"user.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent: …`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that is retrying.

    - `type: Literal["session.thread_status_rescheduled"]`

      - `"session.thread_status_rescheduled"`

  - `class BetaManagedAgentsSessionUpdatedEvent: …`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.updated"]`

      - `"session.updated"`

    - `agent: Optional[BetaManagedAgentsSessionAgent]`

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

          - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `claude-sonnet-5` - High-performance model for coding and agents
            - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
            - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
            - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
            - `claude-opus-4-6` - Most intelligent model for building agents and coding
            - `claude-sonnet-4-6` - Best combination of speed and intelligence
            - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
            - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
            - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
            - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
            - `claude-sonnet-4-5` - High-performance model for agents and coding
            - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

            - `"claude-sonnet-5"`

              High-performance model for coding and agents

            - `"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `"claude-opus-4-8"`

              Frontier intelligence for long-running agents and coding

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

            - `url: str`

          - `model: BetaManagedAgentsModelConfig`

            Model identifier and configuration.

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

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

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

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `mcp_server_name: str`

              - `type: Literal["mcp_toolset"]`

                - `"mcp_toolset"`

            - `class BetaManagedAgentsCustomTool: …`

              A custom tool as returned in API responses.

              - `description: str`

              - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `type: Literal["object"]`

                  - `"object"`

                - `properties: Optional[Dict[str, object]]`

                - `required: Optional[List[str]]`

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

        - `class BetaManagedAgentsCustomSkill: …`

          A resolved user-created custom skill.

      - `system: Optional[str]`

      - `tools: List[Tool]`

        - `class BetaManagedAgentsAgentToolset20260401: …`

        - `class BetaManagedAgentsMCPToolset: …`

        - `class BetaManagedAgentsCustomTool: …`

          A custom tool as returned in API responses.

      - `type: Literal["agent"]`

        - `"agent"`

      - `version: int`

    - `metadata: Optional[Dict[str, str]]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: Optional[str]`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsSystemMessageEvent: …`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks. Text-only.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `type: Literal["system.message"]`

      - `"system.message"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

### Beta Managed Agents Session Requires Action

- `class BetaManagedAgentsSessionRequiresAction: …`

  The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

  - `event_ids: List[str]`

    The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

  - `type: Literal["requires_action"]`

    - `"requires_action"`

### Beta Managed Agents Session Retries Exhausted

- `class BetaManagedAgentsSessionRetriesExhausted: …`

  The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

  - `type: Literal["retries_exhausted"]`

    - `"retries_exhausted"`

### Beta Managed Agents Session Status Idle Event

- `class BetaManagedAgentsSessionStatusIdleEvent: …`

  Indicates the agent has paused and is awaiting user input.

  - `id: str`

    Unique identifier for this event.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `stop_reason: StopReason`

    The agent completed its turn naturally and is ready for the next user message.

    - `class BetaManagedAgentsSessionEndTurn: …`

      The agent completed its turn naturally and is ready for the next user message.

      - `type: Literal["end_turn"]`

        - `"end_turn"`

    - `class BetaManagedAgentsSessionRequiresAction: …`

      The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `event_ids: List[str]`

        The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

      - `type: Literal["requires_action"]`

        - `"requires_action"`

    - `class BetaManagedAgentsSessionRetriesExhausted: …`

      The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

      - `type: Literal["retries_exhausted"]`

        - `"retries_exhausted"`

  - `type: Literal["session.status_idle"]`

    - `"session.status_idle"`

### Beta Managed Agents Session Status Rescheduled Event

- `class BetaManagedAgentsSessionStatusRescheduledEvent: …`

  Indicates the session is recovering from an error state and is rescheduled for execution.

  - `id: str`

    Unique identifier for this event.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `type: Literal["session.status_rescheduled"]`

    - `"session.status_rescheduled"`

### Beta Managed Agents Session Status Running Event

- `class BetaManagedAgentsSessionStatusRunningEvent: …`

  Indicates the session is actively running and the agent is working.

  - `id: str`

    Unique identifier for this event.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `type: Literal["session.status_running"]`

    - `"session.status_running"`

### Beta Managed Agents Session Status Terminated Event

- `class BetaManagedAgentsSessionStatusTerminatedEvent: …`

  Indicates the session has terminated, either due to an error or completion.

  - `id: str`

    Unique identifier for this event.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `type: Literal["session.status_terminated"]`

    - `"session.status_terminated"`

### Beta Managed Agents Session Thread Created Event

- `class BetaManagedAgentsSessionThreadCreatedEvent: …`

  Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

  - `id: str`

    Unique identifier for this event.

  - `agent_name: str`

    Name of the callable agent the thread runs.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `session_thread_id: str`

    Public `sthr_` ID of the newly created thread.

  - `type: Literal["session.thread_created"]`

    - `"session.thread_created"`

### Beta Managed Agents Session Thread Status Idle Event

- `class BetaManagedAgentsSessionThreadStatusIdleEvent: …`

  A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

  - `id: str`

    Unique identifier for this event.

  - `agent_name: str`

    Name of the agent the thread runs.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `session_thread_id: str`

    Public sthr_ ID of the thread that went idle.

  - `stop_reason: StopReason`

    The agent completed its turn naturally and is ready for the next user message.

    - `class BetaManagedAgentsSessionEndTurn: …`

      The agent completed its turn naturally and is ready for the next user message.

      - `type: Literal["end_turn"]`

        - `"end_turn"`

    - `class BetaManagedAgentsSessionRequiresAction: …`

      The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `event_ids: List[str]`

        The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

      - `type: Literal["requires_action"]`

        - `"requires_action"`

    - `class BetaManagedAgentsSessionRetriesExhausted: …`

      The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

      - `type: Literal["retries_exhausted"]`

        - `"retries_exhausted"`

  - `type: Literal["session.thread_status_idle"]`

    - `"session.thread_status_idle"`

### Beta Managed Agents Session Thread Status Rescheduled Event

- `class BetaManagedAgentsSessionThreadStatusRescheduledEvent: …`

  A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

  - `id: str`

    Unique identifier for this event.

  - `agent_name: str`

    Name of the agent the thread runs.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `session_thread_id: str`

    Public sthr_ ID of the thread that is retrying.

  - `type: Literal["session.thread_status_rescheduled"]`

    - `"session.thread_status_rescheduled"`

### Beta Managed Agents Session Thread Status Running Event

- `class BetaManagedAgentsSessionThreadStatusRunningEvent: …`

  A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

  - `id: str`

    Unique identifier for this event.

  - `agent_name: str`

    Name of the agent the thread runs.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `session_thread_id: str`

    Public sthr_ ID of the thread that started running.

  - `type: Literal["session.thread_status_running"]`

    - `"session.thread_status_running"`

### Beta Managed Agents Session Thread Status Terminated Event

- `class BetaManagedAgentsSessionThreadStatusTerminatedEvent: …`

  A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

  - `id: str`

    Unique identifier for this event.

  - `agent_name: str`

    Name of the agent the thread runs.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `session_thread_id: str`

    Public sthr_ ID of the thread that terminated.

  - `type: Literal["session.thread_status_terminated"]`

    - `"session.thread_status_terminated"`

### Beta Managed Agents Span Model Request End Event

- `class BetaManagedAgentsSpanModelRequestEndEvent: …`

  Emitted when a model request completes.

  - `id: str`

    Unique identifier for this event.

  - `is_error: Optional[bool]`

    Whether the model request resulted in an error.

  - `model_request_start_id: str`

    The id of the corresponding `span.model_request_start` event.

  - `model_usage: BetaManagedAgentsSpanModelUsage`

    Token usage for a single model request.

    - `cache_creation_input_tokens: int`

      Tokens used to create prompt cache in this request.

    - `cache_read_input_tokens: int`

      Tokens read from prompt cache in this request.

    - `input_tokens: int`

      Input tokens consumed by this request.

    - `output_tokens: int`

      Output tokens generated by this request.

    - `speed: Optional[Literal["standard", "fast"]]`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `type: Literal["span.model_request_end"]`

    - `"span.model_request_end"`

### Beta Managed Agents Span Model Request Start Event

- `class BetaManagedAgentsSpanModelRequestStartEvent: …`

  Emitted when a model request is initiated by the agent.

  - `id: str`

    Unique identifier for this event.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `type: Literal["span.model_request_start"]`

    - `"span.model_request_start"`

### Beta Managed Agents Span Model Usage

- `class BetaManagedAgentsSpanModelUsage: …`

  Token usage for a single model request.

  - `cache_creation_input_tokens: int`

    Tokens used to create prompt cache in this request.

  - `cache_read_input_tokens: int`

    Tokens read from prompt cache in this request.

  - `input_tokens: int`

    Input tokens consumed by this request.

  - `output_tokens: int`

    Output tokens generated by this request.

  - `speed: Optional[Literal["standard", "fast"]]`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"`

    - `"fast"`

### Beta Managed Agents Span Outcome Evaluation End Event

- `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent: …`

  Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

  - `id: str`

    Unique identifier for this event.

  - `explanation: str`

    Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

  - `iteration: int`

    0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

  - `outcome_evaluation_start_id: str`

    The id of the corresponding `span.outcome_evaluation_start` event.

  - `outcome_id: str`

    The `outc_` ID of the outcome being evaluated.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `result: str`

    Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

  - `type: Literal["span.outcome_evaluation_end"]`

    - `"span.outcome_evaluation_end"`

  - `usage: BetaManagedAgentsSpanModelUsage`

    Token usage for a single model request.

    - `cache_creation_input_tokens: int`

      Tokens used to create prompt cache in this request.

    - `cache_read_input_tokens: int`

      Tokens read from prompt cache in this request.

    - `input_tokens: int`

      Input tokens consumed by this request.

    - `output_tokens: int`

      Output tokens generated by this request.

    - `speed: Optional[Literal["standard", "fast"]]`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

### Beta Managed Agents Span Outcome Evaluation Ongoing Event

- `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent: …`

  Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

  - `id: str`

    Unique identifier for this event.

  - `iteration: int`

    0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

  - `outcome_id: str`

    The `outc_` ID of the outcome being evaluated.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `type: Literal["span.outcome_evaluation_ongoing"]`

    - `"span.outcome_evaluation_ongoing"`

### Beta Managed Agents Span Outcome Evaluation Start Event

- `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent: …`

  Emitted when an outcome evaluation cycle begins.

  - `id: str`

    Unique identifier for this event.

  - `iteration: int`

    0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

  - `outcome_id: str`

    The `outc_` ID of the outcome being evaluated.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `type: Literal["span.outcome_evaluation_start"]`

    - `"span.outcome_evaluation_start"`

### Beta Managed Agents Stream Session Events

- `BetaManagedAgentsStreamSessionEvents`

  Server-sent event in the session stream.

  - `class BetaManagedAgentsUserMessageEvent: …`

    A user message event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `data: str`

              Base64-encoded image data.

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["image"]`

          - `"image"`

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `data: str`

              Base64-encoded document data.

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `data: str`

              The plain text content.

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: Literal["text"]`

              - `"text"`

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["document"]`

          - `"document"`

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

    - `type: Literal["user.message"]`

      - `"user.message"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent: …`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: str`

      Unique identifier for this event.

    - `type: Literal["user.interrupt"]`

      - `"user.interrupt"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent: …`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: str`

      Unique identifier for this event.

    - `result: Literal["allow", "deny"]`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: str`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_confirmation"]`

      - `"user.tool_confirmation"`

    - `deny_message: Optional[str]`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent: …`

    Event sent by the client providing the result of a custom tool execution.

    - `id: str`

      Unique identifier for this event.

    - `custom_tool_use_id: str`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.custom_tool_result"]`

      - `"user.custom_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: bool`

            Whether citations are enabled for this search result.

        - `content: List[BetaManagedAgentsSearchResultContent]`

          Array of text content blocks from the search result.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `source: str`

          The URL source of the search result.

        - `title: str`

          The title of the search result.

        - `type: Literal["search_result"]`

          - `"search_result"`

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent: …`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the custom tool being called.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.custom_tool_use"]`

      - `"agent.custom_tool_use"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent: …`

    An agent response event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsTextBlock]`

      Array of text blocks comprising the agent response.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.message"]`

      - `"agent.message"`

  - `class BetaManagedAgentsAgentThinkingEvent: …`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thinking"]`

      - `"agent.thinking"`

  - `class BetaManagedAgentsAgentMCPToolUseEvent: …`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `mcp_server_name: str`

      Name of the MCP server providing the tool.

    - `name: str`

      Name of the MCP tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.mcp_tool_use"]`

      - `"agent.mcp_tool_use"`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMCPToolResultEvent: …`

    Event representing the result of an MCP tool execution.

    - `id: str`

      Unique identifier for this event.

    - `mcp_tool_use_id: str`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.mcp_tool_result"]`

      - `"agent.mcp_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent: …`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the agent tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.tool_use"]`

      - `"agent.tool_use"`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent: …`

    Event representing the result of an agent tool execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: Literal["agent.tool_result"]`

      - `"agent.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent: …`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `from_session_thread_id: str`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thread_message_received"]`

      - `"agent.thread_message_received"`

    - `from_agent_name: Optional[str]`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent: …`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `to_session_thread_id: str`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: Literal["agent.thread_message_sent"]`

      - `"agent.thread_message_sent"`

    - `to_agent_name: Optional[str]`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent: …`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thread_context_compacted"]`

      - `"agent.thread_context_compacted"`

  - `class BetaManagedAgentsSessionErrorEvent: …`

    An error event indicating a problem occurred during session execution.

    - `id: str`

      Unique identifier for this event.

    - `error: Error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError: …`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: Literal["retrying"]`

              - `"retrying"`

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: Literal["exhausted"]`

              - `"exhausted"`

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: Literal["terminal"]`

              - `"terminal"`

        - `type: Literal["unknown_error"]`

          - `"unknown_error"`

      - `class BetaManagedAgentsModelOverloadedError: …`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_overloaded_error"]`

          - `"model_overloaded_error"`

      - `class BetaManagedAgentsModelRateLimitedError: …`

        The model request was rate-limited.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_rate_limited_error"]`

          - `"model_rate_limited_error"`

      - `class BetaManagedAgentsModelRequestFailedError: …`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_request_failed_error"]`

          - `"model_request_failed_error"`

      - `class BetaManagedAgentsMCPConnectionFailedError: …`

        Failed to connect to an MCP server.

        - `mcp_server_name: str`

          Name of the MCP server that failed to connect.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_connection_failed_error"]`

          - `"mcp_connection_failed_error"`

      - `class BetaManagedAgentsMCPAuthenticationFailedError: …`

        Authentication to an MCP server failed.

        - `mcp_server_name: str`

          Name of the MCP server that failed authentication.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_authentication_failed_error"]`

          - `"mcp_authentication_failed_error"`

      - `class BetaManagedAgentsBillingError: …`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["billing_error"]`

          - `"billing_error"`

      - `class BetaManagedAgentsCredentialHostUnreachableError: …`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: str`

          ID of the affected credential.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["credential_host_unreachable_error"]`

          - `"credential_host_unreachable_error"`

        - `vault_id: str`

          ID of the vault containing the affected credential.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.error"]`

      - `"session.error"`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent: …`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_rescheduled"]`

      - `"session.status_rescheduled"`

  - `class BetaManagedAgentsSessionStatusRunningEvent: …`

    Indicates the session is actively running and the agent is working.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_running"]`

      - `"session.status_running"`

  - `class BetaManagedAgentsSessionStatusIdleEvent: …`

    Indicates the agent has paused and is awaiting user input.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: Literal["end_turn"]`

          - `"end_turn"`

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: List[str]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: Literal["requires_action"]`

          - `"requires_action"`

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `type: Literal["retries_exhausted"]`

          - `"retries_exhausted"`

    - `type: Literal["session.status_idle"]`

      - `"session.status_idle"`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent: …`

    Indicates the session has terminated, either due to an error or completion.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_terminated"]`

      - `"session.status_terminated"`

  - `class BetaManagedAgentsSessionThreadCreatedEvent: …`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the callable agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public `sthr_` ID of the newly created thread.

    - `type: Literal["session.thread_created"]`

      - `"session.thread_created"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent: …`

    Emitted when an outcome evaluation cycle begins.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.outcome_evaluation_start"]`

      - `"span.outcome_evaluation_start"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent: …`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `id: str`

      Unique identifier for this event.

    - `explanation: str`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_evaluation_start_id: str`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `result: str`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `type: Literal["span.outcome_evaluation_end"]`

      - `"span.outcome_evaluation_end"`

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: int`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: int`

        Tokens read from prompt cache in this request.

      - `input_tokens: int`

        Input tokens consumed by this request.

      - `output_tokens: int`

        Output tokens generated by this request.

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `class BetaManagedAgentsSpanModelRequestStartEvent: …`

    Emitted when a model request is initiated by the agent.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.model_request_start"]`

      - `"span.model_request_start"`

  - `class BetaManagedAgentsSpanModelRequestEndEvent: …`

    Emitted when a model request completes.

    - `id: str`

      Unique identifier for this event.

    - `is_error: Optional[bool]`

      Whether the model request resulted in an error.

    - `model_request_start_id: str`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.model_request_end"]`

      - `"span.model_request_end"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent: …`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.outcome_evaluation_ongoing"]`

      - `"span.outcome_evaluation_ongoing"`

  - `class BetaManagedAgentsUserDefineOutcomeEvent: …`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: str`

      Unique identifier for this event.

    - `description: str`

      What the agent should produce. Copied from the input event.

    - `max_iterations: Optional[int]`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `outcome_id: str`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric: …`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: str`

          ID of the rubric file.

        - `type: Literal["file"]`

          - `"file"`

      - `class BetaManagedAgentsTextRubric: …`

        Rubric content provided inline as text.

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: Literal["text"]`

          - `"text"`

    - `type: Literal["user.define_outcome"]`

      - `"user.define_outcome"`

  - `class BetaManagedAgentsSessionDeletedEvent: …`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.deleted"]`

      - `"session.deleted"`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent: …`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that started running.

    - `type: Literal["session.thread_status_running"]`

      - `"session.thread_status_running"`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent: …`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

    - `type: Literal["session.thread_status_idle"]`

      - `"session.thread_status_idle"`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent: …`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that terminated.

    - `type: Literal["session.thread_status_terminated"]`

      - `"session.thread_status_terminated"`

  - `class BetaManagedAgentsUserToolResultEvent: …`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: str`

      Unique identifier for this event.

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_result"]`

      - `"user.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent: …`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that is retrying.

    - `type: Literal["session.thread_status_rescheduled"]`

      - `"session.thread_status_rescheduled"`

  - `class BetaManagedAgentsSessionUpdatedEvent: …`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.updated"]`

      - `"session.updated"`

    - `agent: Optional[BetaManagedAgentsSessionAgent]`

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

          - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `claude-sonnet-5` - High-performance model for coding and agents
            - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
            - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
            - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
            - `claude-opus-4-6` - Most intelligent model for building agents and coding
            - `claude-sonnet-4-6` - Best combination of speed and intelligence
            - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
            - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
            - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
            - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
            - `claude-sonnet-4-5` - High-performance model for agents and coding
            - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

            - `"claude-sonnet-5"`

              High-performance model for coding and agents

            - `"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `"claude-opus-4-8"`

              Frontier intelligence for long-running agents and coding

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

            - `url: str`

          - `model: BetaManagedAgentsModelConfig`

            Model identifier and configuration.

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

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

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

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `mcp_server_name: str`

              - `type: Literal["mcp_toolset"]`

                - `"mcp_toolset"`

            - `class BetaManagedAgentsCustomTool: …`

              A custom tool as returned in API responses.

              - `description: str`

              - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `type: Literal["object"]`

                  - `"object"`

                - `properties: Optional[Dict[str, object]]`

                - `required: Optional[List[str]]`

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

        - `class BetaManagedAgentsCustomSkill: …`

          A resolved user-created custom skill.

      - `system: Optional[str]`

      - `tools: List[Tool]`

        - `class BetaManagedAgentsAgentToolset20260401: …`

        - `class BetaManagedAgentsMCPToolset: …`

        - `class BetaManagedAgentsCustomTool: …`

          A custom tool as returned in API responses.

      - `type: Literal["agent"]`

        - `"agent"`

      - `version: int`

    - `metadata: Optional[Dict[str, str]]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: Optional[str]`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent: …`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `event: BetaManagedAgentsStartEventPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `class BetaManagedAgentsAgentMessagePreview: …`

        - `id: str`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `type: Literal["agent.message"]`

          - `"agent.message"`

      - `class BetaManagedAgentsAgentThinkingPreview: …`

        - `id: str`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `type: Literal["agent.thinking"]`

          - `"agent.thinking"`

    - `type: Literal["event_start"]`

      - `"event_start"`

  - `class BetaManagedAgentsDeltaEvent: …`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `delta: BetaManagedAgentsDeltaContent`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `content: BetaManagedAgentsTextBlock`

        Regular text content.

      - `type: Literal["content_delta"]`

        - `"content_delta"`

      - `index: Optional[int]`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

    - `event_id: str`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `type: Literal["event_delta"]`

      - `"event_delta"`

  - `class BetaManagedAgentsSystemMessageEvent: …`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks. Text-only.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `type: Literal["system.message"]`

      - `"system.message"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

### Beta Managed Agents System Message Event Params

- `class BetaManagedAgentsSystemMessageEventParams: …`

  Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

  - `content: List[BetaManagedAgentsSystemContentBlock]`

    System content blocks to append. Text-only.

    - `text: str`

      The text content.

    - `type: Literal["text"]`

      - `"text"`

  - `type: Literal["system.message"]`

    - `"system.message"`

### Beta Managed Agents Text Block

- `class BetaManagedAgentsTextBlock: …`

  Regular text content.

  - `text: str`

    The text content.

  - `type: Literal["text"]`

    - `"text"`

### Beta Managed Agents Text Rubric

- `class BetaManagedAgentsTextRubric: …`

  Rubric content provided inline as text.

  - `content: str`

    Rubric content. Plain text or markdown — the grader treats it as freeform text.

  - `type: Literal["text"]`

    - `"text"`

### Beta Managed Agents Text Rubric Params

- `class BetaManagedAgentsTextRubricParams: …`

  Rubric content provided inline as text.

  - `content: str`

    Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

  - `type: Literal["text"]`

    - `"text"`

### Beta Managed Agents Unknown Error

- `class BetaManagedAgentsUnknownError: …`

  An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

  - `message: str`

    Human-readable error description.

  - `retry_status: RetryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying: …`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: Literal["retrying"]`

        - `"retrying"`

    - `class BetaManagedAgentsRetryStatusExhausted: …`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: Literal["exhausted"]`

        - `"exhausted"`

    - `class BetaManagedAgentsRetryStatusTerminal: …`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: Literal["terminal"]`

        - `"terminal"`

  - `type: Literal["unknown_error"]`

    - `"unknown_error"`

### Beta Managed Agents URL Document Source

- `class BetaManagedAgentsURLDocumentSource: …`

  Document referenced by URL.

  - `type: Literal["url"]`

    - `"url"`

  - `url: str`

    URL of the document to fetch.

### Beta Managed Agents URL Image Source

- `class BetaManagedAgentsURLImageSource: …`

  Image referenced by URL.

  - `type: Literal["url"]`

    - `"url"`

  - `url: str`

    URL of the image to fetch.

### Beta Managed Agents User Custom Tool Result Event

- `class BetaManagedAgentsUserCustomToolResultEvent: …`

  Event sent by the client providing the result of a custom tool execution.

  - `id: str`

    Unique identifier for this event.

  - `custom_tool_use_id: str`

    The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `type: Literal["user.custom_tool_result"]`

    - `"user.custom_tool_result"`

  - `content: Optional[List[Content]]`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock: …`

      Regular text content.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `class BetaManagedAgentsImageBlock: …`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: Source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource: …`

          Base64-encoded image data.

          - `data: str`

            Base64-encoded image data.

          - `media_type: str`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: Literal["base64"]`

            - `"base64"`

        - `class BetaManagedAgentsURLImageSource: …`

          Image referenced by URL.

          - `type: Literal["url"]`

            - `"url"`

          - `url: str`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource: …`

          Image referenced by file ID.

          - `file_id: str`

            ID of a previously uploaded file.

          - `type: Literal["file"]`

            - `"file"`

      - `type: Literal["image"]`

        - `"image"`

    - `class BetaManagedAgentsDocumentBlock: …`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: Source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource: …`

          Base64-encoded document data.

          - `data: str`

            Base64-encoded document data.

          - `media_type: str`

            MIME type of the document (e.g., "application/pdf").

          - `type: Literal["base64"]`

            - `"base64"`

        - `class BetaManagedAgentsPlainTextDocumentSource: …`

          Plain text document content.

          - `data: str`

            The plain text content.

          - `media_type: Literal["text/plain"]`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsURLDocumentSource: …`

          Document referenced by URL.

          - `type: Literal["url"]`

            - `"url"`

          - `url: str`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource: …`

          Document referenced by file ID.

          - `file_id: str`

            ID of a previously uploaded file.

          - `type: Literal["file"]`

            - `"file"`

      - `type: Literal["document"]`

        - `"document"`

      - `context: Optional[str]`

        Additional context about the document for the model.

      - `title: Optional[str]`

        The title of the document.

    - `class BetaManagedAgentsSearchResultBlock: …`

      A block containing a web search result.

      - `citations: BetaManagedAgentsSearchResultCitations`

        Citation settings for a search result.

        - `enabled: bool`

          Whether citations are enabled for this search result.

      - `content: List[BetaManagedAgentsSearchResultContent]`

        Array of text content blocks from the search result.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `source: str`

        The URL source of the search result.

      - `title: str`

        The title of the search result.

      - `type: Literal["search_result"]`

        - `"search_result"`

  - `is_error: Optional[bool]`

    Whether the tool execution resulted in an error.

  - `processed_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `session_thread_id: Optional[str]`

    Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

### Beta Managed Agents User Custom Tool Result Event Params

- `class BetaManagedAgentsUserCustomToolResultEventParams: …`

  Parameters for providing the result of a custom tool execution.

  - `custom_tool_use_id: str`

    The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `type: Literal["user.custom_tool_result"]`

    - `"user.custom_tool_result"`

  - `content: Optional[List[Content]]`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock: …`

      Regular text content.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `class BetaManagedAgentsImageBlock: …`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: Source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource: …`

          Base64-encoded image data.

          - `data: str`

            Base64-encoded image data.

          - `media_type: str`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: Literal["base64"]`

            - `"base64"`

        - `class BetaManagedAgentsURLImageSource: …`

          Image referenced by URL.

          - `type: Literal["url"]`

            - `"url"`

          - `url: str`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource: …`

          Image referenced by file ID.

          - `file_id: str`

            ID of a previously uploaded file.

          - `type: Literal["file"]`

            - `"file"`

      - `type: Literal["image"]`

        - `"image"`

    - `class BetaManagedAgentsDocumentBlock: …`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: Source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource: …`

          Base64-encoded document data.

          - `data: str`

            Base64-encoded document data.

          - `media_type: str`

            MIME type of the document (e.g., "application/pdf").

          - `type: Literal["base64"]`

            - `"base64"`

        - `class BetaManagedAgentsPlainTextDocumentSource: …`

          Plain text document content.

          - `data: str`

            The plain text content.

          - `media_type: Literal["text/plain"]`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsURLDocumentSource: …`

          Document referenced by URL.

          - `type: Literal["url"]`

            - `"url"`

          - `url: str`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource: …`

          Document referenced by file ID.

          - `file_id: str`

            ID of a previously uploaded file.

          - `type: Literal["file"]`

            - `"file"`

      - `type: Literal["document"]`

        - `"document"`

      - `context: Optional[str]`

        Additional context about the document for the model.

      - `title: Optional[str]`

        The title of the document.

    - `class BetaManagedAgentsSearchResultBlock: …`

      A block containing a web search result.

      - `citations: BetaManagedAgentsSearchResultCitations`

        Citation settings for a search result.

        - `enabled: bool`

          Whether citations are enabled for this search result.

      - `content: List[BetaManagedAgentsSearchResultContent]`

        Array of text content blocks from the search result.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `source: str`

        The URL source of the search result.

      - `title: str`

        The title of the search result.

      - `type: Literal["search_result"]`

        - `"search_result"`

  - `is_error: Optional[bool]`

    Whether the tool execution resulted in an error.

### Beta Managed Agents User Define Outcome Event

- `class BetaManagedAgentsUserDefineOutcomeEvent: …`

  Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

  - `id: str`

    Unique identifier for this event.

  - `description: str`

    What the agent should produce. Copied from the input event.

  - `max_iterations: Optional[int]`

    Evaluate-then-revise cycles before giving up. Default 3, max 20.

  - `outcome_id: str`

    Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

  - `rubric: Rubric`

    Rubric for grading the quality of an outcome.

    - `class BetaManagedAgentsFileRubric: …`

      Rubric referenced by a file uploaded via the Files API.

      - `file_id: str`

        ID of the rubric file.

      - `type: Literal["file"]`

        - `"file"`

    - `class BetaManagedAgentsTextRubric: …`

      Rubric content provided inline as text.

      - `content: str`

        Rubric content. Plain text or markdown — the grader treats it as freeform text.

      - `type: Literal["text"]`

        - `"text"`

  - `type: Literal["user.define_outcome"]`

    - `"user.define_outcome"`

### Beta Managed Agents User Define Outcome Event Params

- `class BetaManagedAgentsUserDefineOutcomeEventParams: …`

  Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

  - `description: str`

    What the agent should produce. This is the task specification.

  - `rubric: Rubric`

    Rubric for grading the quality of an outcome.

    - `class BetaManagedAgentsFileRubricParams: …`

      Rubric referenced by a file uploaded via the Files API.

      - `file_id: str`

        ID of the rubric file.

      - `type: Literal["file"]`

        - `"file"`

    - `class BetaManagedAgentsTextRubricParams: …`

      Rubric content provided inline as text.

      - `content: str`

        Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

      - `type: Literal["text"]`

        - `"text"`

  - `type: Literal["user.define_outcome"]`

    - `"user.define_outcome"`

  - `max_iterations: Optional[int]`

    Eval→revision cycles before giving up. Default 3, max 20.

### Beta Managed Agents User Interrupt Event

- `class BetaManagedAgentsUserInterruptEvent: …`

  An interrupt event that pauses agent execution and returns control to the user.

  - `id: str`

    Unique identifier for this event.

  - `type: Literal["user.interrupt"]`

    - `"user.interrupt"`

  - `processed_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `session_thread_id: Optional[str]`

    If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

### Beta Managed Agents User Interrupt Event Params

- `class BetaManagedAgentsUserInterruptEventParams: …`

  Parameters for sending an interrupt to pause the agent.

  - `type: Literal["user.interrupt"]`

    - `"user.interrupt"`

  - `session_thread_id: Optional[str]`

    If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

### Beta Managed Agents User Message Event

- `class BetaManagedAgentsUserMessageEvent: …`

  A user message event in the session conversation.

  - `id: str`

    Unique identifier for this event.

  - `content: List[Content]`

    Array of content blocks comprising the user message.

    - `class BetaManagedAgentsTextBlock: …`

      Regular text content.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `class BetaManagedAgentsImageBlock: …`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: Source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource: …`

          Base64-encoded image data.

          - `data: str`

            Base64-encoded image data.

          - `media_type: str`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: Literal["base64"]`

            - `"base64"`

        - `class BetaManagedAgentsURLImageSource: …`

          Image referenced by URL.

          - `type: Literal["url"]`

            - `"url"`

          - `url: str`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource: …`

          Image referenced by file ID.

          - `file_id: str`

            ID of a previously uploaded file.

          - `type: Literal["file"]`

            - `"file"`

      - `type: Literal["image"]`

        - `"image"`

    - `class BetaManagedAgentsDocumentBlock: …`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: Source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource: …`

          Base64-encoded document data.

          - `data: str`

            Base64-encoded document data.

          - `media_type: str`

            MIME type of the document (e.g., "application/pdf").

          - `type: Literal["base64"]`

            - `"base64"`

        - `class BetaManagedAgentsPlainTextDocumentSource: …`

          Plain text document content.

          - `data: str`

            The plain text content.

          - `media_type: Literal["text/plain"]`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsURLDocumentSource: …`

          Document referenced by URL.

          - `type: Literal["url"]`

            - `"url"`

          - `url: str`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource: …`

          Document referenced by file ID.

          - `file_id: str`

            ID of a previously uploaded file.

          - `type: Literal["file"]`

            - `"file"`

      - `type: Literal["document"]`

        - `"document"`

      - `context: Optional[str]`

        Additional context about the document for the model.

      - `title: Optional[str]`

        The title of the document.

  - `type: Literal["user.message"]`

    - `"user.message"`

  - `processed_at: Optional[datetime]`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Message Event Params

- `class BetaManagedAgentsUserMessageEventParams: …`

  Parameters for sending a user message to the session.

  - `content: List[Content]`

    Array of content blocks for the user message.

    - `class BetaManagedAgentsTextBlock: …`

      Regular text content.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `class BetaManagedAgentsImageBlock: …`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: Source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource: …`

          Base64-encoded image data.

          - `data: str`

            Base64-encoded image data.

          - `media_type: str`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: Literal["base64"]`

            - `"base64"`

        - `class BetaManagedAgentsURLImageSource: …`

          Image referenced by URL.

          - `type: Literal["url"]`

            - `"url"`

          - `url: str`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource: …`

          Image referenced by file ID.

          - `file_id: str`

            ID of a previously uploaded file.

          - `type: Literal["file"]`

            - `"file"`

      - `type: Literal["image"]`

        - `"image"`

    - `class BetaManagedAgentsDocumentBlock: …`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: Source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource: …`

          Base64-encoded document data.

          - `data: str`

            Base64-encoded document data.

          - `media_type: str`

            MIME type of the document (e.g., "application/pdf").

          - `type: Literal["base64"]`

            - `"base64"`

        - `class BetaManagedAgentsPlainTextDocumentSource: …`

          Plain text document content.

          - `data: str`

            The plain text content.

          - `media_type: Literal["text/plain"]`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsURLDocumentSource: …`

          Document referenced by URL.

          - `type: Literal["url"]`

            - `"url"`

          - `url: str`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource: …`

          Document referenced by file ID.

          - `file_id: str`

            ID of a previously uploaded file.

          - `type: Literal["file"]`

            - `"file"`

      - `type: Literal["document"]`

        - `"document"`

      - `context: Optional[str]`

        Additional context about the document for the model.

      - `title: Optional[str]`

        The title of the document.

  - `type: Literal["user.message"]`

    - `"user.message"`

### Beta Managed Agents User Tool Confirmation Event

- `class BetaManagedAgentsUserToolConfirmationEvent: …`

  A tool confirmation event that approves or denies a pending tool execution.

  - `id: str`

    Unique identifier for this event.

  - `result: Literal["allow", "deny"]`

    UserToolConfirmationResult enum

    - `"allow"`

    - `"deny"`

  - `tool_use_id: str`

    The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `type: Literal["user.tool_confirmation"]`

    - `"user.tool_confirmation"`

  - `deny_message: Optional[str]`

    Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

  - `processed_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `session_thread_id: Optional[str]`

    When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

### Beta Managed Agents User Tool Confirmation Event Params

- `class BetaManagedAgentsUserToolConfirmationEventParams: …`

  Parameters for confirming or denying a tool execution request.

  - `result: Literal["allow", "deny"]`

    UserToolConfirmationResult enum

    - `"allow"`

    - `"deny"`

  - `tool_use_id: str`

    The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `type: Literal["user.tool_confirmation"]`

    - `"user.tool_confirmation"`

  - `deny_message: Optional[str]`

    Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

### Beta Managed Agents User Tool Result Event Params

- `class BetaManagedAgentsUserToolResultEventParams: …`

  Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

  - `tool_use_id: str`

    The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `type: Literal["user.tool_result"]`

    - `"user.tool_result"`

  - `content: Optional[List[Content]]`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock: …`

      Regular text content.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `class BetaManagedAgentsImageBlock: …`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: Source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource: …`

          Base64-encoded image data.

          - `data: str`

            Base64-encoded image data.

          - `media_type: str`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: Literal["base64"]`

            - `"base64"`

        - `class BetaManagedAgentsURLImageSource: …`

          Image referenced by URL.

          - `type: Literal["url"]`

            - `"url"`

          - `url: str`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource: …`

          Image referenced by file ID.

          - `file_id: str`

            ID of a previously uploaded file.

          - `type: Literal["file"]`

            - `"file"`

      - `type: Literal["image"]`

        - `"image"`

    - `class BetaManagedAgentsDocumentBlock: …`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: Source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource: …`

          Base64-encoded document data.

          - `data: str`

            Base64-encoded document data.

          - `media_type: str`

            MIME type of the document (e.g., "application/pdf").

          - `type: Literal["base64"]`

            - `"base64"`

        - `class BetaManagedAgentsPlainTextDocumentSource: …`

          Plain text document content.

          - `data: str`

            The plain text content.

          - `media_type: Literal["text/plain"]`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsURLDocumentSource: …`

          Document referenced by URL.

          - `type: Literal["url"]`

            - `"url"`

          - `url: str`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource: …`

          Document referenced by file ID.

          - `file_id: str`

            ID of a previously uploaded file.

          - `type: Literal["file"]`

            - `"file"`

      - `type: Literal["document"]`

        - `"document"`

      - `context: Optional[str]`

        Additional context about the document for the model.

      - `title: Optional[str]`

        The title of the document.

    - `class BetaManagedAgentsSearchResultBlock: …`

      A block containing a web search result.

      - `citations: BetaManagedAgentsSearchResultCitations`

        Citation settings for a search result.

        - `enabled: bool`

          Whether citations are enabled for this search result.

      - `content: List[BetaManagedAgentsSearchResultContent]`

        Array of text content blocks from the search result.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `source: str`

        The URL source of the search result.

      - `title: str`

        The title of the search result.

      - `type: Literal["search_result"]`

        - `"search_result"`

  - `is_error: Optional[bool]`

    Whether the tool execution resulted in an error.

# Resources

## Add Session Resource

`beta.sessions.resources.add(strsession_id, ResourceAddParams**kwargs)  -> BetaManagedAgentsFileResource`

**post** `/v1/sessions/{session_id}/resources`

Add Session Resource

### Parameters

- `session_id: str`

- `file_id: str`

  ID of a previously uploaded file.

- `type: Literal["file"]`

  - `"file"`

- `mount_path: Optional[str]`

  Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]`

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

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

### Returns

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

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_file_resource = client.beta.sessions.resources.add(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
    file_id="file_011CNha8iCJcU1wXNR6q4V8w",
    type="file",
)
print(beta_managed_agents_file_resource.id)
```

#### Response

```json
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "created_at": "2026-03-15T10:00:00Z",
  "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "mount_path": "/uploads/receipt.pdf",
  "type": "file",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## List Session Resources

`beta.sessions.resources.list(strsession_id, ResourceListParams**kwargs)  -> SyncPageCursor[BetaManagedAgentsSessionResource]`

**get** `/v1/sessions/{session_id}/resources`

List Session Resources

### Parameters

- `session_id: str`

- `limit: Optional[int]`

  Maximum number of resources to return per page (max 1000). If omitted, returns all resources.

- `page: Optional[str]`

  Opaque cursor from a previous response's next_page field.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]`

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

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

### Returns

- `BetaManagedAgentsSessionResource`

  A memory store attached to an agent session.

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

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.sessions.resources.list(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
page = page.data[0]
print(page)
```

#### Response

```json
{
  "data": [
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
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Session Resource

`beta.sessions.resources.retrieve(strresource_id, ResourceRetrieveParams**kwargs)  -> ResourceRetrieveResponse`

**get** `/v1/sessions/{session_id}/resources/{resource_id}`

Get Session Resource

### Parameters

- `session_id: str`

- `resource_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]`

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

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

### Returns

- `ResourceRetrieveResponse`

  The requested session resource.

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

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
resource = client.beta.sessions.resources.retrieve(
    resource_id="sesrsc_011CZkZBJq5dWxk9fVLNcPht",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
print(resource)
```

#### Response

```json
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
```

## Update Session Resource

`beta.sessions.resources.update(strresource_id, ResourceUpdateParams**kwargs)  -> ResourceUpdateResponse`

**post** `/v1/sessions/{session_id}/resources/{resource_id}`

Update Session Resource

### Parameters

- `session_id: str`

- `resource_id: str`

- `authorization_token: str`

  New authorization token for the resource. Currently only `github_repository` resources support token rotation.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]`

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

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

### Returns

- `ResourceUpdateResponse`

  The updated session resource.

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

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
resource = client.beta.sessions.resources.update(
    resource_id="sesrsc_011CZkZBJq5dWxk9fVLNcPht",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
    authorization_token="ghp_exampletoken",
)
print(resource)
```

#### Response

```json
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
```

## Delete Session Resource

`beta.sessions.resources.delete(strresource_id, ResourceDeleteParams**kwargs)  -> BetaManagedAgentsDeleteSessionResource`

**delete** `/v1/sessions/{session_id}/resources/{resource_id}`

Delete Session Resource

### Parameters

- `session_id: str`

- `resource_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]`

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

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

### Returns

- `class BetaManagedAgentsDeleteSessionResource: …`

  Confirmation of resource deletion.

  - `id: str`

  - `type: Literal["session_resource_deleted"]`

    - `"session_resource_deleted"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_delete_session_resource = client.beta.sessions.resources.delete(
    resource_id="sesrsc_011CZkZBJq5dWxk9fVLNcPht",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
print(beta_managed_agents_delete_session_resource.id)
```

#### Response

```json
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "type": "session_resource_deleted"
}
```

## Domain Types

### Beta Managed Agents Delete Session Resource

- `class BetaManagedAgentsDeleteSessionResource: …`

  Confirmation of resource deletion.

  - `id: str`

  - `type: Literal["session_resource_deleted"]`

    - `"session_resource_deleted"`

### Beta Managed Agents File Resource

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

### Beta Managed Agents GitHub Repository Resource

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

### Beta Managed Agents Memory Store Resource

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

### Beta Managed Agents Session Resource

- `BetaManagedAgentsSessionResource`

  A memory store attached to an agent session.

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

### Resource Retrieve Response

- `ResourceRetrieveResponse`

  The requested session resource.

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

### Resource Update Response

- `ResourceUpdateResponse`

  The updated session resource.

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

# Threads

## List Session Threads

`beta.sessions.threads.list(strsession_id, ThreadListParams**kwargs)  -> SyncPageCursor[BetaManagedAgentsSessionThread]`

**get** `/v1/sessions/{session_id}/threads`

List Session Threads

### Parameters

- `session_id: str`

- `limit: Optional[int]`

  Maximum results per page. Defaults to 1000.

- `page: Optional[str]`

  Opaque pagination cursor from a previous response's next_page. Forward-only.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]`

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

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

### Returns

- `class BetaManagedAgentsSessionThread: …`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `id: str`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

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

        - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-6` - Most intelligent model for building agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
          - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

          - `"claude-sonnet-5"`

            High-performance model for coding and agents

          - `"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-4-8"`

            Frontier intelligence for long-running agents and coding

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

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

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

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: bool`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `mcp_server_name: str`

        - `type: Literal["mcp_toolset"]`

          - `"mcp_toolset"`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

        - `description: str`

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `type: Literal["object"]`

            - `"object"`

          - `properties: Optional[Dict[str, object]]`

          - `required: Optional[List[str]]`

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

  - `parent_thread_id: Optional[str]`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: str`

    The session this thread belongs to.

  - `stats: Optional[BetaManagedAgentsSessionThreadStats]`

    Timing statistics for a session thread.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `duration_seconds: Optional[float]`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `startup_seconds: Optional[float]`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `status: BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `type: Literal["session_thread"]`

    - `"session_thread"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `usage: Optional[BetaManagedAgentsSessionThreadUsage]`

    Cumulative token usage for a session thread across all turns.

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

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.sessions.threads.list(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
page = page.data[0]
print(page.id)
```

#### Response

```json
{
  "data": [
    {
      "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
      "agent": {
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
      },
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "parent_thread_id": null,
      "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
      "stats": {
        "active_seconds": 0,
        "duration_seconds": 0,
        "startup_seconds": 0
      },
      "status": "idle",
      "type": "session_thread",
      "updated_at": "2026-03-15T10:00:00Z",
      "usage": {
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 0
        },
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "output_tokens": 0
      }
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Session Thread

`beta.sessions.threads.retrieve(strthread_id, ThreadRetrieveParams**kwargs)  -> BetaManagedAgentsSessionThread`

**get** `/v1/sessions/{session_id}/threads/{thread_id}`

Get Session Thread

### Parameters

- `session_id: str`

- `thread_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]`

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

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

### Returns

- `class BetaManagedAgentsSessionThread: …`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `id: str`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

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

        - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-6` - Most intelligent model for building agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
          - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

          - `"claude-sonnet-5"`

            High-performance model for coding and agents

          - `"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-4-8"`

            Frontier intelligence for long-running agents and coding

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

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

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

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: bool`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `mcp_server_name: str`

        - `type: Literal["mcp_toolset"]`

          - `"mcp_toolset"`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

        - `description: str`

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `type: Literal["object"]`

            - `"object"`

          - `properties: Optional[Dict[str, object]]`

          - `required: Optional[List[str]]`

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

  - `parent_thread_id: Optional[str]`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: str`

    The session this thread belongs to.

  - `stats: Optional[BetaManagedAgentsSessionThreadStats]`

    Timing statistics for a session thread.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `duration_seconds: Optional[float]`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `startup_seconds: Optional[float]`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `status: BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `type: Literal["session_thread"]`

    - `"session_thread"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `usage: Optional[BetaManagedAgentsSessionThreadUsage]`

    Cumulative token usage for a session thread across all turns.

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

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_session_thread = client.beta.sessions.threads.retrieve(
    thread_id="sthr_011CZkZVWa6oIjw0rgXZpnBt",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
print(beta_managed_agents_session_thread.id)
```

#### Response

```json
{
  "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  "agent": {
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
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "parent_thread_id": null,
  "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0,
    "startup_seconds": 0
  },
  "status": "idle",
  "type": "session_thread",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

## Archive Session Thread

`beta.sessions.threads.archive(strthread_id, ThreadArchiveParams**kwargs)  -> BetaManagedAgentsSessionThread`

**post** `/v1/sessions/{session_id}/threads/{thread_id}/archive`

Archive Session Thread

### Parameters

- `session_id: str`

- `thread_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]`

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

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

### Returns

- `class BetaManagedAgentsSessionThread: …`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `id: str`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

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

        - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-6` - Most intelligent model for building agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
          - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

          - `"claude-sonnet-5"`

            High-performance model for coding and agents

          - `"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-4-8"`

            Frontier intelligence for long-running agents and coding

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

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

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

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: bool`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `mcp_server_name: str`

        - `type: Literal["mcp_toolset"]`

          - `"mcp_toolset"`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

        - `description: str`

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `type: Literal["object"]`

            - `"object"`

          - `properties: Optional[Dict[str, object]]`

          - `required: Optional[List[str]]`

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

  - `parent_thread_id: Optional[str]`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: str`

    The session this thread belongs to.

  - `stats: Optional[BetaManagedAgentsSessionThreadStats]`

    Timing statistics for a session thread.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `duration_seconds: Optional[float]`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `startup_seconds: Optional[float]`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `status: BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `type: Literal["session_thread"]`

    - `"session_thread"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `usage: Optional[BetaManagedAgentsSessionThreadUsage]`

    Cumulative token usage for a session thread across all turns.

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

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_session_thread = client.beta.sessions.threads.archive(
    thread_id="sthr_011CZkZVWa6oIjw0rgXZpnBt",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
print(beta_managed_agents_session_thread.id)
```

#### Response

```json
{
  "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  "agent": {
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
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "parent_thread_id": null,
  "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0,
    "startup_seconds": 0
  },
  "status": "idle",
  "type": "session_thread",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

## Domain Types

### Beta Managed Agents Session Thread

- `class BetaManagedAgentsSessionThread: …`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `id: str`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

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

        - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-6` - Most intelligent model for building agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
          - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

          - `"claude-sonnet-5"`

            High-performance model for coding and agents

          - `"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-4-8"`

            Frontier intelligence for long-running agents and coding

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

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

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

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: bool`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `mcp_server_name: str`

        - `type: Literal["mcp_toolset"]`

          - `"mcp_toolset"`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

        - `description: str`

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `type: Literal["object"]`

            - `"object"`

          - `properties: Optional[Dict[str, object]]`

          - `required: Optional[List[str]]`

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

  - `parent_thread_id: Optional[str]`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: str`

    The session this thread belongs to.

  - `stats: Optional[BetaManagedAgentsSessionThreadStats]`

    Timing statistics for a session thread.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `duration_seconds: Optional[float]`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `startup_seconds: Optional[float]`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `status: BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `type: Literal["session_thread"]`

    - `"session_thread"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `usage: Optional[BetaManagedAgentsSessionThreadUsage]`

    Cumulative token usage for a session thread across all turns.

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

### Beta Managed Agents Session Thread Stats

- `class BetaManagedAgentsSessionThreadStats: …`

  Timing statistics for a session thread.

  - `active_seconds: Optional[float]`

    Cumulative time in seconds the thread spent actively running. Excludes idle time.

  - `duration_seconds: Optional[float]`

    Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

  - `startup_seconds: Optional[float]`

    Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

### Beta Managed Agents Session Thread Status

- `Literal["running", "idle", "rescheduling", "terminated"]`

  SessionThreadStatus enum

  - `"running"`

  - `"idle"`

  - `"rescheduling"`

  - `"terminated"`

### Beta Managed Agents Session Thread Usage

- `class BetaManagedAgentsSessionThreadUsage: …`

  Cumulative token usage for a session thread across all turns.

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

### Beta Managed Agents Stream Session Thread Events

- `BetaManagedAgentsStreamSessionThreadEvents`

  Server-sent event in a single thread's stream.

  - `class BetaManagedAgentsUserMessageEvent: …`

    A user message event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `data: str`

              Base64-encoded image data.

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["image"]`

          - `"image"`

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `data: str`

              Base64-encoded document data.

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `data: str`

              The plain text content.

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: Literal["text"]`

              - `"text"`

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["document"]`

          - `"document"`

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

    - `type: Literal["user.message"]`

      - `"user.message"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent: …`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: str`

      Unique identifier for this event.

    - `type: Literal["user.interrupt"]`

      - `"user.interrupt"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent: …`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: str`

      Unique identifier for this event.

    - `result: Literal["allow", "deny"]`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: str`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_confirmation"]`

      - `"user.tool_confirmation"`

    - `deny_message: Optional[str]`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent: …`

    Event sent by the client providing the result of a custom tool execution.

    - `id: str`

      Unique identifier for this event.

    - `custom_tool_use_id: str`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.custom_tool_result"]`

      - `"user.custom_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: bool`

            Whether citations are enabled for this search result.

        - `content: List[BetaManagedAgentsSearchResultContent]`

          Array of text content blocks from the search result.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `source: str`

          The URL source of the search result.

        - `title: str`

          The title of the search result.

        - `type: Literal["search_result"]`

          - `"search_result"`

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent: …`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the custom tool being called.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.custom_tool_use"]`

      - `"agent.custom_tool_use"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent: …`

    An agent response event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsTextBlock]`

      Array of text blocks comprising the agent response.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.message"]`

      - `"agent.message"`

  - `class BetaManagedAgentsAgentThinkingEvent: …`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thinking"]`

      - `"agent.thinking"`

  - `class BetaManagedAgentsAgentMCPToolUseEvent: …`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `mcp_server_name: str`

      Name of the MCP server providing the tool.

    - `name: str`

      Name of the MCP tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.mcp_tool_use"]`

      - `"agent.mcp_tool_use"`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMCPToolResultEvent: …`

    Event representing the result of an MCP tool execution.

    - `id: str`

      Unique identifier for this event.

    - `mcp_tool_use_id: str`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.mcp_tool_result"]`

      - `"agent.mcp_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent: …`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the agent tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.tool_use"]`

      - `"agent.tool_use"`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent: …`

    Event representing the result of an agent tool execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: Literal["agent.tool_result"]`

      - `"agent.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent: …`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `from_session_thread_id: str`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thread_message_received"]`

      - `"agent.thread_message_received"`

    - `from_agent_name: Optional[str]`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent: …`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `to_session_thread_id: str`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: Literal["agent.thread_message_sent"]`

      - `"agent.thread_message_sent"`

    - `to_agent_name: Optional[str]`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent: …`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thread_context_compacted"]`

      - `"agent.thread_context_compacted"`

  - `class BetaManagedAgentsSessionErrorEvent: …`

    An error event indicating a problem occurred during session execution.

    - `id: str`

      Unique identifier for this event.

    - `error: Error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError: …`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: Literal["retrying"]`

              - `"retrying"`

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: Literal["exhausted"]`

              - `"exhausted"`

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: Literal["terminal"]`

              - `"terminal"`

        - `type: Literal["unknown_error"]`

          - `"unknown_error"`

      - `class BetaManagedAgentsModelOverloadedError: …`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_overloaded_error"]`

          - `"model_overloaded_error"`

      - `class BetaManagedAgentsModelRateLimitedError: …`

        The model request was rate-limited.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_rate_limited_error"]`

          - `"model_rate_limited_error"`

      - `class BetaManagedAgentsModelRequestFailedError: …`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_request_failed_error"]`

          - `"model_request_failed_error"`

      - `class BetaManagedAgentsMCPConnectionFailedError: …`

        Failed to connect to an MCP server.

        - `mcp_server_name: str`

          Name of the MCP server that failed to connect.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_connection_failed_error"]`

          - `"mcp_connection_failed_error"`

      - `class BetaManagedAgentsMCPAuthenticationFailedError: …`

        Authentication to an MCP server failed.

        - `mcp_server_name: str`

          Name of the MCP server that failed authentication.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_authentication_failed_error"]`

          - `"mcp_authentication_failed_error"`

      - `class BetaManagedAgentsBillingError: …`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["billing_error"]`

          - `"billing_error"`

      - `class BetaManagedAgentsCredentialHostUnreachableError: …`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: str`

          ID of the affected credential.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["credential_host_unreachable_error"]`

          - `"credential_host_unreachable_error"`

        - `vault_id: str`

          ID of the vault containing the affected credential.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.error"]`

      - `"session.error"`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent: …`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_rescheduled"]`

      - `"session.status_rescheduled"`

  - `class BetaManagedAgentsSessionStatusRunningEvent: …`

    Indicates the session is actively running and the agent is working.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_running"]`

      - `"session.status_running"`

  - `class BetaManagedAgentsSessionStatusIdleEvent: …`

    Indicates the agent has paused and is awaiting user input.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: Literal["end_turn"]`

          - `"end_turn"`

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: List[str]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: Literal["requires_action"]`

          - `"requires_action"`

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `type: Literal["retries_exhausted"]`

          - `"retries_exhausted"`

    - `type: Literal["session.status_idle"]`

      - `"session.status_idle"`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent: …`

    Indicates the session has terminated, either due to an error or completion.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_terminated"]`

      - `"session.status_terminated"`

  - `class BetaManagedAgentsSessionThreadCreatedEvent: …`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the callable agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public `sthr_` ID of the newly created thread.

    - `type: Literal["session.thread_created"]`

      - `"session.thread_created"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent: …`

    Emitted when an outcome evaluation cycle begins.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.outcome_evaluation_start"]`

      - `"span.outcome_evaluation_start"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent: …`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `id: str`

      Unique identifier for this event.

    - `explanation: str`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_evaluation_start_id: str`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `result: str`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `type: Literal["span.outcome_evaluation_end"]`

      - `"span.outcome_evaluation_end"`

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: int`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: int`

        Tokens read from prompt cache in this request.

      - `input_tokens: int`

        Input tokens consumed by this request.

      - `output_tokens: int`

        Output tokens generated by this request.

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `class BetaManagedAgentsSpanModelRequestStartEvent: …`

    Emitted when a model request is initiated by the agent.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.model_request_start"]`

      - `"span.model_request_start"`

  - `class BetaManagedAgentsSpanModelRequestEndEvent: …`

    Emitted when a model request completes.

    - `id: str`

      Unique identifier for this event.

    - `is_error: Optional[bool]`

      Whether the model request resulted in an error.

    - `model_request_start_id: str`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.model_request_end"]`

      - `"span.model_request_end"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent: …`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.outcome_evaluation_ongoing"]`

      - `"span.outcome_evaluation_ongoing"`

  - `class BetaManagedAgentsUserDefineOutcomeEvent: …`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: str`

      Unique identifier for this event.

    - `description: str`

      What the agent should produce. Copied from the input event.

    - `max_iterations: Optional[int]`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `outcome_id: str`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric: …`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: str`

          ID of the rubric file.

        - `type: Literal["file"]`

          - `"file"`

      - `class BetaManagedAgentsTextRubric: …`

        Rubric content provided inline as text.

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: Literal["text"]`

          - `"text"`

    - `type: Literal["user.define_outcome"]`

      - `"user.define_outcome"`

  - `class BetaManagedAgentsSessionDeletedEvent: …`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.deleted"]`

      - `"session.deleted"`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent: …`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that started running.

    - `type: Literal["session.thread_status_running"]`

      - `"session.thread_status_running"`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent: …`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

    - `type: Literal["session.thread_status_idle"]`

      - `"session.thread_status_idle"`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent: …`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that terminated.

    - `type: Literal["session.thread_status_terminated"]`

      - `"session.thread_status_terminated"`

  - `class BetaManagedAgentsUserToolResultEvent: …`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: str`

      Unique identifier for this event.

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_result"]`

      - `"user.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent: …`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that is retrying.

    - `type: Literal["session.thread_status_rescheduled"]`

      - `"session.thread_status_rescheduled"`

  - `class BetaManagedAgentsSessionUpdatedEvent: …`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.updated"]`

      - `"session.updated"`

    - `agent: Optional[BetaManagedAgentsSessionAgent]`

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

          - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `claude-sonnet-5` - High-performance model for coding and agents
            - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
            - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
            - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
            - `claude-opus-4-6` - Most intelligent model for building agents and coding
            - `claude-sonnet-4-6` - Best combination of speed and intelligence
            - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
            - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
            - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
            - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
            - `claude-sonnet-4-5` - High-performance model for agents and coding
            - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

            - `"claude-sonnet-5"`

              High-performance model for coding and agents

            - `"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `"claude-opus-4-8"`

              Frontier intelligence for long-running agents and coding

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

            - `url: str`

          - `model: BetaManagedAgentsModelConfig`

            Model identifier and configuration.

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

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

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

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `mcp_server_name: str`

              - `type: Literal["mcp_toolset"]`

                - `"mcp_toolset"`

            - `class BetaManagedAgentsCustomTool: …`

              A custom tool as returned in API responses.

              - `description: str`

              - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `type: Literal["object"]`

                  - `"object"`

                - `properties: Optional[Dict[str, object]]`

                - `required: Optional[List[str]]`

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

        - `class BetaManagedAgentsCustomSkill: …`

          A resolved user-created custom skill.

      - `system: Optional[str]`

      - `tools: List[Tool]`

        - `class BetaManagedAgentsAgentToolset20260401: …`

        - `class BetaManagedAgentsMCPToolset: …`

        - `class BetaManagedAgentsCustomTool: …`

          A custom tool as returned in API responses.

      - `type: Literal["agent"]`

        - `"agent"`

      - `version: int`

    - `metadata: Optional[Dict[str, str]]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: Optional[str]`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent: …`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `event: BetaManagedAgentsStartEventPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `class BetaManagedAgentsAgentMessagePreview: …`

        - `id: str`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `type: Literal["agent.message"]`

          - `"agent.message"`

      - `class BetaManagedAgentsAgentThinkingPreview: …`

        - `id: str`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `type: Literal["agent.thinking"]`

          - `"agent.thinking"`

    - `type: Literal["event_start"]`

      - `"event_start"`

  - `class BetaManagedAgentsDeltaEvent: …`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `delta: BetaManagedAgentsDeltaContent`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `content: BetaManagedAgentsTextBlock`

        Regular text content.

      - `type: Literal["content_delta"]`

        - `"content_delta"`

      - `index: Optional[int]`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

    - `event_id: str`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `type: Literal["event_delta"]`

      - `"event_delta"`

  - `class BetaManagedAgentsSystemMessageEvent: …`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks. Text-only.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `type: Literal["system.message"]`

      - `"system.message"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

# Events

## List Session Thread Events

`beta.sessions.threads.events.list(strthread_id, EventListParams**kwargs)  -> SyncPageCursor[BetaManagedAgentsSessionEvent]`

**get** `/v1/sessions/{session_id}/threads/{thread_id}/events`

List Session Thread Events

### Parameters

- `session_id: str`

- `thread_id: str`

- `limit: Optional[int]`

  Query parameter for limit

- `page: Optional[str]`

  Query parameter for page

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]`

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

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

### Returns

- `BetaManagedAgentsSessionEvent`

  Union type for all event types in a session.

  - `class BetaManagedAgentsUserMessageEvent: …`

    A user message event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `data: str`

              Base64-encoded image data.

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["image"]`

          - `"image"`

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `data: str`

              Base64-encoded document data.

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `data: str`

              The plain text content.

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: Literal["text"]`

              - `"text"`

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["document"]`

          - `"document"`

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

    - `type: Literal["user.message"]`

      - `"user.message"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent: …`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: str`

      Unique identifier for this event.

    - `type: Literal["user.interrupt"]`

      - `"user.interrupt"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent: …`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: str`

      Unique identifier for this event.

    - `result: Literal["allow", "deny"]`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: str`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_confirmation"]`

      - `"user.tool_confirmation"`

    - `deny_message: Optional[str]`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent: …`

    Event sent by the client providing the result of a custom tool execution.

    - `id: str`

      Unique identifier for this event.

    - `custom_tool_use_id: str`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.custom_tool_result"]`

      - `"user.custom_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: bool`

            Whether citations are enabled for this search result.

        - `content: List[BetaManagedAgentsSearchResultContent]`

          Array of text content blocks from the search result.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `source: str`

          The URL source of the search result.

        - `title: str`

          The title of the search result.

        - `type: Literal["search_result"]`

          - `"search_result"`

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent: …`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the custom tool being called.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.custom_tool_use"]`

      - `"agent.custom_tool_use"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent: …`

    An agent response event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsTextBlock]`

      Array of text blocks comprising the agent response.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.message"]`

      - `"agent.message"`

  - `class BetaManagedAgentsAgentThinkingEvent: …`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thinking"]`

      - `"agent.thinking"`

  - `class BetaManagedAgentsAgentMCPToolUseEvent: …`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `mcp_server_name: str`

      Name of the MCP server providing the tool.

    - `name: str`

      Name of the MCP tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.mcp_tool_use"]`

      - `"agent.mcp_tool_use"`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMCPToolResultEvent: …`

    Event representing the result of an MCP tool execution.

    - `id: str`

      Unique identifier for this event.

    - `mcp_tool_use_id: str`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.mcp_tool_result"]`

      - `"agent.mcp_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent: …`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the agent tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.tool_use"]`

      - `"agent.tool_use"`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent: …`

    Event representing the result of an agent tool execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: Literal["agent.tool_result"]`

      - `"agent.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent: …`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `from_session_thread_id: str`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thread_message_received"]`

      - `"agent.thread_message_received"`

    - `from_agent_name: Optional[str]`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent: …`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `to_session_thread_id: str`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: Literal["agent.thread_message_sent"]`

      - `"agent.thread_message_sent"`

    - `to_agent_name: Optional[str]`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent: …`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thread_context_compacted"]`

      - `"agent.thread_context_compacted"`

  - `class BetaManagedAgentsSessionErrorEvent: …`

    An error event indicating a problem occurred during session execution.

    - `id: str`

      Unique identifier for this event.

    - `error: Error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError: …`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: Literal["retrying"]`

              - `"retrying"`

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: Literal["exhausted"]`

              - `"exhausted"`

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: Literal["terminal"]`

              - `"terminal"`

        - `type: Literal["unknown_error"]`

          - `"unknown_error"`

      - `class BetaManagedAgentsModelOverloadedError: …`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_overloaded_error"]`

          - `"model_overloaded_error"`

      - `class BetaManagedAgentsModelRateLimitedError: …`

        The model request was rate-limited.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_rate_limited_error"]`

          - `"model_rate_limited_error"`

      - `class BetaManagedAgentsModelRequestFailedError: …`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_request_failed_error"]`

          - `"model_request_failed_error"`

      - `class BetaManagedAgentsMCPConnectionFailedError: …`

        Failed to connect to an MCP server.

        - `mcp_server_name: str`

          Name of the MCP server that failed to connect.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_connection_failed_error"]`

          - `"mcp_connection_failed_error"`

      - `class BetaManagedAgentsMCPAuthenticationFailedError: …`

        Authentication to an MCP server failed.

        - `mcp_server_name: str`

          Name of the MCP server that failed authentication.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_authentication_failed_error"]`

          - `"mcp_authentication_failed_error"`

      - `class BetaManagedAgentsBillingError: …`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["billing_error"]`

          - `"billing_error"`

      - `class BetaManagedAgentsCredentialHostUnreachableError: …`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: str`

          ID of the affected credential.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["credential_host_unreachable_error"]`

          - `"credential_host_unreachable_error"`

        - `vault_id: str`

          ID of the vault containing the affected credential.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.error"]`

      - `"session.error"`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent: …`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_rescheduled"]`

      - `"session.status_rescheduled"`

  - `class BetaManagedAgentsSessionStatusRunningEvent: …`

    Indicates the session is actively running and the agent is working.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_running"]`

      - `"session.status_running"`

  - `class BetaManagedAgentsSessionStatusIdleEvent: …`

    Indicates the agent has paused and is awaiting user input.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: Literal["end_turn"]`

          - `"end_turn"`

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: List[str]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: Literal["requires_action"]`

          - `"requires_action"`

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `type: Literal["retries_exhausted"]`

          - `"retries_exhausted"`

    - `type: Literal["session.status_idle"]`

      - `"session.status_idle"`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent: …`

    Indicates the session has terminated, either due to an error or completion.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_terminated"]`

      - `"session.status_terminated"`

  - `class BetaManagedAgentsSessionThreadCreatedEvent: …`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the callable agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public `sthr_` ID of the newly created thread.

    - `type: Literal["session.thread_created"]`

      - `"session.thread_created"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent: …`

    Emitted when an outcome evaluation cycle begins.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.outcome_evaluation_start"]`

      - `"span.outcome_evaluation_start"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent: …`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `id: str`

      Unique identifier for this event.

    - `explanation: str`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_evaluation_start_id: str`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `result: str`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `type: Literal["span.outcome_evaluation_end"]`

      - `"span.outcome_evaluation_end"`

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: int`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: int`

        Tokens read from prompt cache in this request.

      - `input_tokens: int`

        Input tokens consumed by this request.

      - `output_tokens: int`

        Output tokens generated by this request.

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `class BetaManagedAgentsSpanModelRequestStartEvent: …`

    Emitted when a model request is initiated by the agent.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.model_request_start"]`

      - `"span.model_request_start"`

  - `class BetaManagedAgentsSpanModelRequestEndEvent: …`

    Emitted when a model request completes.

    - `id: str`

      Unique identifier for this event.

    - `is_error: Optional[bool]`

      Whether the model request resulted in an error.

    - `model_request_start_id: str`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.model_request_end"]`

      - `"span.model_request_end"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent: …`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.outcome_evaluation_ongoing"]`

      - `"span.outcome_evaluation_ongoing"`

  - `class BetaManagedAgentsUserDefineOutcomeEvent: …`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: str`

      Unique identifier for this event.

    - `description: str`

      What the agent should produce. Copied from the input event.

    - `max_iterations: Optional[int]`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `outcome_id: str`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric: …`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: str`

          ID of the rubric file.

        - `type: Literal["file"]`

          - `"file"`

      - `class BetaManagedAgentsTextRubric: …`

        Rubric content provided inline as text.

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: Literal["text"]`

          - `"text"`

    - `type: Literal["user.define_outcome"]`

      - `"user.define_outcome"`

  - `class BetaManagedAgentsSessionDeletedEvent: …`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.deleted"]`

      - `"session.deleted"`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent: …`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that started running.

    - `type: Literal["session.thread_status_running"]`

      - `"session.thread_status_running"`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent: …`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

    - `type: Literal["session.thread_status_idle"]`

      - `"session.thread_status_idle"`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent: …`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that terminated.

    - `type: Literal["session.thread_status_terminated"]`

      - `"session.thread_status_terminated"`

  - `class BetaManagedAgentsUserToolResultEvent: …`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: str`

      Unique identifier for this event.

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_result"]`

      - `"user.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent: …`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that is retrying.

    - `type: Literal["session.thread_status_rescheduled"]`

      - `"session.thread_status_rescheduled"`

  - `class BetaManagedAgentsSessionUpdatedEvent: …`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.updated"]`

      - `"session.updated"`

    - `agent: Optional[BetaManagedAgentsSessionAgent]`

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

          - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `claude-sonnet-5` - High-performance model for coding and agents
            - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
            - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
            - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
            - `claude-opus-4-6` - Most intelligent model for building agents and coding
            - `claude-sonnet-4-6` - Best combination of speed and intelligence
            - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
            - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
            - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
            - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
            - `claude-sonnet-4-5` - High-performance model for agents and coding
            - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

            - `"claude-sonnet-5"`

              High-performance model for coding and agents

            - `"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `"claude-opus-4-8"`

              Frontier intelligence for long-running agents and coding

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

            - `url: str`

          - `model: BetaManagedAgentsModelConfig`

            Model identifier and configuration.

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

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

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

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `mcp_server_name: str`

              - `type: Literal["mcp_toolset"]`

                - `"mcp_toolset"`

            - `class BetaManagedAgentsCustomTool: …`

              A custom tool as returned in API responses.

              - `description: str`

              - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `type: Literal["object"]`

                  - `"object"`

                - `properties: Optional[Dict[str, object]]`

                - `required: Optional[List[str]]`

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

        - `class BetaManagedAgentsCustomSkill: …`

          A resolved user-created custom skill.

      - `system: Optional[str]`

      - `tools: List[Tool]`

        - `class BetaManagedAgentsAgentToolset20260401: …`

        - `class BetaManagedAgentsMCPToolset: …`

        - `class BetaManagedAgentsCustomTool: …`

          A custom tool as returned in API responses.

      - `type: Literal["agent"]`

        - `"agent"`

      - `version: int`

    - `metadata: Optional[Dict[str, str]]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: Optional[str]`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsSystemMessageEvent: …`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks. Text-only.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `type: Literal["system.message"]`

      - `"system.message"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.sessions.threads.events.list(
    thread_id="sthr_011CZkZVWa6oIjw0rgXZpnBt",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
page = page.data[0]
print(page)
```

#### Response

```json
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "next_page"
}
```

## Stream Session Thread Events

`beta.sessions.threads.events.stream(strthread_id, EventStreamParams**kwargs)  -> BetaManagedAgentsStreamSessionThreadEvents`

**get** `/v1/sessions/{session_id}/threads/{thread_id}/stream`

Stream Session Thread Events

### Parameters

- `session_id: str`

- `thread_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]`

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

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

### Returns

- `BetaManagedAgentsStreamSessionThreadEvents`

  Server-sent event in a single thread's stream.

  - `class BetaManagedAgentsUserMessageEvent: …`

    A user message event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `data: str`

              Base64-encoded image data.

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["image"]`

          - `"image"`

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `data: str`

              Base64-encoded document data.

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `data: str`

              The plain text content.

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: Literal["text"]`

              - `"text"`

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["document"]`

          - `"document"`

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

    - `type: Literal["user.message"]`

      - `"user.message"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent: …`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: str`

      Unique identifier for this event.

    - `type: Literal["user.interrupt"]`

      - `"user.interrupt"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent: …`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: str`

      Unique identifier for this event.

    - `result: Literal["allow", "deny"]`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: str`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_confirmation"]`

      - `"user.tool_confirmation"`

    - `deny_message: Optional[str]`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent: …`

    Event sent by the client providing the result of a custom tool execution.

    - `id: str`

      Unique identifier for this event.

    - `custom_tool_use_id: str`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.custom_tool_result"]`

      - `"user.custom_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: bool`

            Whether citations are enabled for this search result.

        - `content: List[BetaManagedAgentsSearchResultContent]`

          Array of text content blocks from the search result.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `source: str`

          The URL source of the search result.

        - `title: str`

          The title of the search result.

        - `type: Literal["search_result"]`

          - `"search_result"`

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent: …`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the custom tool being called.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.custom_tool_use"]`

      - `"agent.custom_tool_use"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent: …`

    An agent response event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsTextBlock]`

      Array of text blocks comprising the agent response.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.message"]`

      - `"agent.message"`

  - `class BetaManagedAgentsAgentThinkingEvent: …`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thinking"]`

      - `"agent.thinking"`

  - `class BetaManagedAgentsAgentMCPToolUseEvent: …`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `mcp_server_name: str`

      Name of the MCP server providing the tool.

    - `name: str`

      Name of the MCP tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.mcp_tool_use"]`

      - `"agent.mcp_tool_use"`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMCPToolResultEvent: …`

    Event representing the result of an MCP tool execution.

    - `id: str`

      Unique identifier for this event.

    - `mcp_tool_use_id: str`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.mcp_tool_result"]`

      - `"agent.mcp_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent: …`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the agent tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.tool_use"]`

      - `"agent.tool_use"`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent: …`

    Event representing the result of an agent tool execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: Literal["agent.tool_result"]`

      - `"agent.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent: …`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `from_session_thread_id: str`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thread_message_received"]`

      - `"agent.thread_message_received"`

    - `from_agent_name: Optional[str]`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent: …`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `to_session_thread_id: str`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: Literal["agent.thread_message_sent"]`

      - `"agent.thread_message_sent"`

    - `to_agent_name: Optional[str]`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent: …`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thread_context_compacted"]`

      - `"agent.thread_context_compacted"`

  - `class BetaManagedAgentsSessionErrorEvent: …`

    An error event indicating a problem occurred during session execution.

    - `id: str`

      Unique identifier for this event.

    - `error: Error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError: …`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: Literal["retrying"]`

              - `"retrying"`

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: Literal["exhausted"]`

              - `"exhausted"`

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: Literal["terminal"]`

              - `"terminal"`

        - `type: Literal["unknown_error"]`

          - `"unknown_error"`

      - `class BetaManagedAgentsModelOverloadedError: …`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_overloaded_error"]`

          - `"model_overloaded_error"`

      - `class BetaManagedAgentsModelRateLimitedError: …`

        The model request was rate-limited.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_rate_limited_error"]`

          - `"model_rate_limited_error"`

      - `class BetaManagedAgentsModelRequestFailedError: …`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_request_failed_error"]`

          - `"model_request_failed_error"`

      - `class BetaManagedAgentsMCPConnectionFailedError: …`

        Failed to connect to an MCP server.

        - `mcp_server_name: str`

          Name of the MCP server that failed to connect.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_connection_failed_error"]`

          - `"mcp_connection_failed_error"`

      - `class BetaManagedAgentsMCPAuthenticationFailedError: …`

        Authentication to an MCP server failed.

        - `mcp_server_name: str`

          Name of the MCP server that failed authentication.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_authentication_failed_error"]`

          - `"mcp_authentication_failed_error"`

      - `class BetaManagedAgentsBillingError: …`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["billing_error"]`

          - `"billing_error"`

      - `class BetaManagedAgentsCredentialHostUnreachableError: …`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: str`

          ID of the affected credential.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["credential_host_unreachable_error"]`

          - `"credential_host_unreachable_error"`

        - `vault_id: str`

          ID of the vault containing the affected credential.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.error"]`

      - `"session.error"`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent: …`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_rescheduled"]`

      - `"session.status_rescheduled"`

  - `class BetaManagedAgentsSessionStatusRunningEvent: …`

    Indicates the session is actively running and the agent is working.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_running"]`

      - `"session.status_running"`

  - `class BetaManagedAgentsSessionStatusIdleEvent: …`

    Indicates the agent has paused and is awaiting user input.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: Literal["end_turn"]`

          - `"end_turn"`

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: List[str]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: Literal["requires_action"]`

          - `"requires_action"`

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `type: Literal["retries_exhausted"]`

          - `"retries_exhausted"`

    - `type: Literal["session.status_idle"]`

      - `"session.status_idle"`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent: …`

    Indicates the session has terminated, either due to an error or completion.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_terminated"]`

      - `"session.status_terminated"`

  - `class BetaManagedAgentsSessionThreadCreatedEvent: …`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the callable agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public `sthr_` ID of the newly created thread.

    - `type: Literal["session.thread_created"]`

      - `"session.thread_created"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent: …`

    Emitted when an outcome evaluation cycle begins.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.outcome_evaluation_start"]`

      - `"span.outcome_evaluation_start"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent: …`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `id: str`

      Unique identifier for this event.

    - `explanation: str`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_evaluation_start_id: str`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `result: str`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `type: Literal["span.outcome_evaluation_end"]`

      - `"span.outcome_evaluation_end"`

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: int`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: int`

        Tokens read from prompt cache in this request.

      - `input_tokens: int`

        Input tokens consumed by this request.

      - `output_tokens: int`

        Output tokens generated by this request.

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `class BetaManagedAgentsSpanModelRequestStartEvent: …`

    Emitted when a model request is initiated by the agent.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.model_request_start"]`

      - `"span.model_request_start"`

  - `class BetaManagedAgentsSpanModelRequestEndEvent: …`

    Emitted when a model request completes.

    - `id: str`

      Unique identifier for this event.

    - `is_error: Optional[bool]`

      Whether the model request resulted in an error.

    - `model_request_start_id: str`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.model_request_end"]`

      - `"span.model_request_end"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent: …`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.outcome_evaluation_ongoing"]`

      - `"span.outcome_evaluation_ongoing"`

  - `class BetaManagedAgentsUserDefineOutcomeEvent: …`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: str`

      Unique identifier for this event.

    - `description: str`

      What the agent should produce. Copied from the input event.

    - `max_iterations: Optional[int]`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `outcome_id: str`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric: …`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: str`

          ID of the rubric file.

        - `type: Literal["file"]`

          - `"file"`

      - `class BetaManagedAgentsTextRubric: …`

        Rubric content provided inline as text.

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: Literal["text"]`

          - `"text"`

    - `type: Literal["user.define_outcome"]`

      - `"user.define_outcome"`

  - `class BetaManagedAgentsSessionDeletedEvent: …`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.deleted"]`

      - `"session.deleted"`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent: …`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that started running.

    - `type: Literal["session.thread_status_running"]`

      - `"session.thread_status_running"`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent: …`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

    - `type: Literal["session.thread_status_idle"]`

      - `"session.thread_status_idle"`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent: …`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that terminated.

    - `type: Literal["session.thread_status_terminated"]`

      - `"session.thread_status_terminated"`

  - `class BetaManagedAgentsUserToolResultEvent: …`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: str`

      Unique identifier for this event.

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_result"]`

      - `"user.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent: …`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that is retrying.

    - `type: Literal["session.thread_status_rescheduled"]`

      - `"session.thread_status_rescheduled"`

  - `class BetaManagedAgentsSessionUpdatedEvent: …`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.updated"]`

      - `"session.updated"`

    - `agent: Optional[BetaManagedAgentsSessionAgent]`

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

          - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `claude-sonnet-5` - High-performance model for coding and agents
            - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
            - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
            - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
            - `claude-opus-4-6` - Most intelligent model for building agents and coding
            - `claude-sonnet-4-6` - Best combination of speed and intelligence
            - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
            - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
            - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
            - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
            - `claude-sonnet-4-5` - High-performance model for agents and coding
            - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

            - `"claude-sonnet-5"`

              High-performance model for coding and agents

            - `"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `"claude-opus-4-8"`

              Frontier intelligence for long-running agents and coding

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

            - `url: str`

          - `model: BetaManagedAgentsModelConfig`

            Model identifier and configuration.

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

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

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

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `mcp_server_name: str`

              - `type: Literal["mcp_toolset"]`

                - `"mcp_toolset"`

            - `class BetaManagedAgentsCustomTool: …`

              A custom tool as returned in API responses.

              - `description: str`

              - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `type: Literal["object"]`

                  - `"object"`

                - `properties: Optional[Dict[str, object]]`

                - `required: Optional[List[str]]`

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

        - `class BetaManagedAgentsCustomSkill: …`

          A resolved user-created custom skill.

      - `system: Optional[str]`

      - `tools: List[Tool]`

        - `class BetaManagedAgentsAgentToolset20260401: …`

        - `class BetaManagedAgentsMCPToolset: …`

        - `class BetaManagedAgentsCustomTool: …`

          A custom tool as returned in API responses.

      - `type: Literal["agent"]`

        - `"agent"`

      - `version: int`

    - `metadata: Optional[Dict[str, str]]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: Optional[str]`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent: …`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `event: BetaManagedAgentsStartEventPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `class BetaManagedAgentsAgentMessagePreview: …`

        - `id: str`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `type: Literal["agent.message"]`

          - `"agent.message"`

      - `class BetaManagedAgentsAgentThinkingPreview: …`

        - `id: str`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `type: Literal["agent.thinking"]`

          - `"agent.thinking"`

    - `type: Literal["event_start"]`

      - `"event_start"`

  - `class BetaManagedAgentsDeltaEvent: …`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `delta: BetaManagedAgentsDeltaContent`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `content: BetaManagedAgentsTextBlock`

        Regular text content.

      - `type: Literal["content_delta"]`

        - `"content_delta"`

      - `index: Optional[int]`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

    - `event_id: str`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `type: Literal["event_delta"]`

      - `"event_delta"`

  - `class BetaManagedAgentsSystemMessageEvent: …`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks. Text-only.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `type: Literal["system.message"]`

      - `"system.message"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
for event in client.beta.sessions.threads.events.stream(
    thread_id="sthr_011CZkZVWa6oIjw0rgXZpnBt",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
):
  print(event)
```

#### Response

```json
{
  "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
  "content": [
    {
      "text": "Where is my order #1234?",
      "type": "text"
    }
  ],
  "type": "user.message",
  "processed_at": "2026-03-15T10:00:00Z"
}
```
