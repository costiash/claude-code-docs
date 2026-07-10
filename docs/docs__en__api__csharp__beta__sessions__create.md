## Create Session

`BetaManagedAgentsSession Beta.Sessions.Create(SessionCreateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/sessions`

Create Session

### Parameters

- `SessionCreateParams parameters`

  - `required Agent agent`

    Body param: Agent identifier. Accepts the `agent` ID string, which pins the latest version for the session, or an `agent` object with both id and version specified.

    - `string`

    - `class BetaManagedAgentsAgentParams:`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `required string ID`

        The `agent` ID.

      - `required Type Type`

        - `"agent"Agent`

      - `Int Version`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

    - `class BetaManagedAgentsAgentWithOverridesParams:`

      Reference to an `agent` plus optional configuration overrides. Each provided field replaces the agent's value for the caller's use; the agent resource is unchanged.

      - `required string ID`

        The `agent` ID.

      - `required Type Type`

        - `"agent_with_overrides"AgentWithOverrides`

      - `IReadOnlyList<BetaManagedAgentsUrlMcpServerParams> McpServers`

        Replacement MCP server list. Full replacement: the provided array becomes the MCP servers. Send an empty array to clear; omit to preserve the agent's servers.

        - `required string Name`

          Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

        - `required Type Type`

          - `"url"Url`

        - `required string Url`

          Endpoint URL for the MCP server.

      - `Model Model`

        Replacement model. Accepts the model string, e.g. `claude-opus-4-6`, or a `model_config` object. Omit to use the agent's model.

        - `enum BetaManagedAgentsModel:`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-sonnet-5"ClaudeSonnet5`

            High-performance model for coding and agents

          - `"claude-fable-5"ClaudeFable5`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-4-8"ClaudeOpus4_8`

            Frontier intelligence for long-running agents and coding

          - `"claude-opus-4-7"ClaudeOpus4_7`

            Frontier intelligence for long-running agents and coding

          - `"claude-opus-4-6"ClaudeOpus4_6`

            Most intelligent model for building agents and coding

          - `"claude-sonnet-4-6"ClaudeSonnet4_6`

            Best combination of speed and intelligence

          - `"claude-haiku-4-5"ClaudeHaiku4_5`

            Fastest model with near-frontier intelligence

          - `"claude-haiku-4-5-20251001"ClaudeHaiku4_5_20251001`

            Fastest model with near-frontier intelligence

          - `"claude-opus-4-5"ClaudeOpus4_5`

            Premium model combining maximum intelligence with practical performance

          - `"claude-opus-4-5-20251101"ClaudeOpus4_5_20251101`

            Premium model combining maximum intelligence with practical performance

          - `"claude-sonnet-4-5"ClaudeSonnet4_5`

            High-performance model for agents and coding

          - `"claude-sonnet-4-5-20250929"ClaudeSonnet4_5_20250929`

            High-performance model for agents and coding

        - `class BetaManagedAgentsModelConfigParams:`

          An object that defines additional configuration control over model use

          - `required BetaManagedAgentsModel ID`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `"claude-sonnet-5"ClaudeSonnet5`

              High-performance model for coding and agents

            - `"claude-fable-5"ClaudeFable5`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `"claude-opus-4-8"ClaudeOpus4_8`

              Frontier intelligence for long-running agents and coding

            - `"claude-opus-4-7"ClaudeOpus4_7`

              Frontier intelligence for long-running agents and coding

            - `"claude-opus-4-6"ClaudeOpus4_6`

              Most intelligent model for building agents and coding

            - `"claude-sonnet-4-6"ClaudeSonnet4_6`

              Best combination of speed and intelligence

            - `"claude-haiku-4-5"ClaudeHaiku4_5`

              Fastest model with near-frontier intelligence

            - `"claude-haiku-4-5-20251001"ClaudeHaiku4_5_20251001`

              Fastest model with near-frontier intelligence

            - `"claude-opus-4-5"ClaudeOpus4_5`

              Premium model combining maximum intelligence with practical performance

            - `"claude-opus-4-5-20251101"ClaudeOpus4_5_20251101`

              Premium model combining maximum intelligence with practical performance

            - `"claude-sonnet-4-5"ClaudeSonnet4_5`

              High-performance model for agents and coding

            - `"claude-sonnet-4-5-20250929"ClaudeSonnet4_5_20250929`

              High-performance model for agents and coding

          - `Speed? Speed`

            Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `"standard"Standard`

            - `"fast"Fast`

      - `IReadOnlyList<BetaManagedAgentsSkillParams> Skills`

        Replacement skill list. Full replacement: the provided array becomes the skills. Send an empty array to clear; omit to preserve the agent's skills.

        - `class BetaManagedAgentsAnthropicSkillParams:`

          An Anthropic-managed skill.

          - `required string SkillID`

            Identifier of the Anthropic skill (e.g., "xlsx").

          - `required Type Type`

            - `"anthropic"Anthropic`

          - `string? Version`

            Version to pin. Defaults to latest if omitted.

        - `class BetaManagedAgentsCustomSkillParams:`

          A user-created custom skill.

          - `required string SkillID`

            Tagged ID of the custom skill (e.g., "skill_01XJ5...").

          - `required Type Type`

            - `"custom"Custom`

          - `string? Version`

            Version to pin. Defaults to latest if omitted.

      - `string? System`

        Replacement system prompt. Up to 100,000 characters. Set to null to clear the agent's system prompt; omit to preserve it.

      - `IReadOnlyList<Tool> Tools`

        Replacement tool list. Full replacement: the provided array becomes the tool configuration. Send an empty array to clear; omit to preserve the agent's tools.

        - `class BetaManagedAgentsAgentToolset20260401Params:`

          Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

          - `required Type Type`

            - `"agent_toolset_20260401"AgentToolset20260401`

          - `IReadOnlyList<BetaManagedAgentsAgentToolConfigParams> Configs`

            Per-tool configuration overrides.

            - `required Name Name`

              Built-in agent tool identifier.

              - `"bash"Bash`

              - `"edit"Edit`

              - `"read"Read`

              - `"write"Write`

              - `"glob"Glob`

              - `"grep"Grep`

              - `"web_fetch"WebFetch`

              - `"web_search"WebSearch`

            - `Boolean? Enabled`

              Whether this tool is enabled and available to Claude. Overrides the default_config setting.

            - `PermissionPolicy? PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

                - `required Type Type`

                  - `"always_allow"AlwaysAllow`

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

                - `required Type Type`

                  - `"always_ask"AlwaysAsk`

          - `BetaManagedAgentsAgentToolsetDefaultConfigParams? DefaultConfig`

            Default configuration for all tools in a toolset.

            - `Boolean? Enabled`

              Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

            - `PermissionPolicy? PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

        - `class BetaManagedAgentsMcpToolsetParams:`

          Configuration for tools from an MCP server defined in `mcp_servers`.

          - `required string McpServerName`

            Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

          - `required Type Type`

            - `"mcp_toolset"McpToolset`

          - `IReadOnlyList<BetaManagedAgentsMcpToolConfigParams> Configs`

            Per-tool configuration overrides.

            - `required string Name`

              Name of the MCP tool to configure. 1-128 characters.

            - `Boolean? Enabled`

              Whether this tool is enabled. Overrides the `default_config` setting.

            - `PermissionPolicy? PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `BetaManagedAgentsMcpToolsetDefaultConfigParams? DefaultConfig`

            Default configuration for all tools from an MCP server.

            - `Boolean? Enabled`

              Whether tools are enabled by default. Defaults to true if not specified.

            - `PermissionPolicy? PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

        - `class BetaManagedAgentsCustomToolParams:`

          A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

          - `required string Description`

            Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-4096 characters.

          - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

            JSON Schema for custom tool input parameters.

            - `JsonElement Type "object"constant`

            - `IReadOnlyDictionary<string, JsonElement>? Properties`

            - `IReadOnlyList<string>? Required`

          - `required string Name`

            Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

          - `required Type Type`

            - `"custom"Custom`

      - `Int Version`

        The specific `agent` version to use. Omit to use the latest version.

  - `required string environmentID`

    Body param: ID of the `environment` defining the container configuration for this session.

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: Arbitrary key-value metadata attached to the session. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `IReadOnlyList<Resource> resources`

    Body param: Resources (e.g. repositories, files) to mount into the session's container.

    - `class BetaManagedAgentsGitHubRepositoryResourceParams:`

      Mount a GitHub repository into the session's container.

      - `required string AuthorizationToken`

        GitHub authorization token used to clone the repository.

      - `required Type Type`

        - `"github_repository"GitHubRepository`

      - `required string Url`

        Github URL of the repository

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

          - `required Type Type`

            - `"branch"Branch`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

          - `required Type Type`

            - `"commit"Commit`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceParams:`

      Mount a file uploaded via the Files API into the session.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

        - `"file"File`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceParam:`

      Parameters for attaching a memory store to an agent session.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

        - `"memory_store"MemoryStore`

      - `Access? Access`

        Access mode for an attached memory store.

        - `"read_write"ReadWrite`

        - `"read_only"ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `string? title`

    Body param: Human-readable session title.

  - `IReadOnlyList<string> vaultIds`

    Body param: Vault IDs for stored credentials the agent can use during the session.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

### Returns

- `class BetaManagedAgentsSession:`

  A Managed Agents `session`.

  - `required string ID`

  - `required BetaManagedAgentsSessionAgent Agent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `required string ID`

    - `required string? Description`

    - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

      - `required string Name`

      - `required Type Type`

        - `"url"Url`

      - `required string Url`

    - `required BetaManagedAgentsModelConfig Model`

      Model identifier and configuration.

      - `required BetaManagedAgentsModel ID`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `"claude-sonnet-5"ClaudeSonnet5`

          High-performance model for coding and agents

        - `"claude-fable-5"ClaudeFable5`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `"claude-opus-4-8"ClaudeOpus4_8`

          Frontier intelligence for long-running agents and coding

        - `"claude-opus-4-7"ClaudeOpus4_7`

          Frontier intelligence for long-running agents and coding

        - `"claude-opus-4-6"ClaudeOpus4_6`

          Most intelligent model for building agents and coding

        - `"claude-sonnet-4-6"ClaudeSonnet4_6`

          Best combination of speed and intelligence

        - `"claude-haiku-4-5"ClaudeHaiku4_5`

          Fastest model with near-frontier intelligence

        - `"claude-haiku-4-5-20251001"ClaudeHaiku4_5_20251001`

          Fastest model with near-frontier intelligence

        - `"claude-opus-4-5"ClaudeOpus4_5`

          Premium model combining maximum intelligence with practical performance

        - `"claude-opus-4-5-20251101"ClaudeOpus4_5_20251101`

          Premium model combining maximum intelligence with practical performance

        - `"claude-sonnet-4-5"ClaudeSonnet4_5`

          High-performance model for agents and coding

        - `"claude-sonnet-4-5-20250929"ClaudeSonnet4_5_20250929`

          High-performance model for agents and coding

      - `Speed Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"Standard`

        - `"fast"Fast`

    - `required BetaManagedAgentsSessionMultiagentCoordinator? Multiagent`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `required IReadOnlyList<BetaManagedAgentsSessionThreadAgent> Agents`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `required string ID`

        - `required string? Description`

        - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

          - `required string Name`

          - `required Type Type`

          - `required string Url`

        - `required BetaManagedAgentsModelConfig Model`

          Model identifier and configuration.

        - `required string Name`

        - `required IReadOnlyList<Skill> Skills`

          - `class BetaManagedAgentsAnthropicSkill:`

            A resolved Anthropic-managed skill.

            - `required string SkillID`

            - `required Type Type`

              - `"anthropic"Anthropic`

            - `required string Version`

          - `class BetaManagedAgentsCustomSkill:`

            A resolved user-created custom skill.

            - `required string SkillID`

            - `required Type Type`

              - `"custom"Custom`

            - `required string Version`

        - `required string? System`

        - `required IReadOnlyList<Tool> Tools`

          - `class BetaManagedAgentsAgentToolset20260401:`

            - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

              - `required Boolean Enabled`

              - `required Name Name`

                Built-in agent tool identifier.

                - `"bash"Bash`

                - `"edit"Edit`

                - `"read"Read`

                - `"write"Write`

                - `"glob"Glob`

                - `"grep"Grep`

                - `"web_fetch"WebFetch`

                - `"web_search"WebSearch`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                  - `required Type Type`

                    - `"always_allow"AlwaysAllow`

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

                  - `required Type Type`

                    - `"always_ask"AlwaysAsk`

            - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

              Resolved default configuration for agent tools.

              - `required Boolean Enabled`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

            - `required Type Type`

              - `"agent_toolset_20260401"AgentToolset20260401`

          - `class BetaManagedAgentsMcpToolset:`

            - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

              - `required Boolean Enabled`

              - `required string Name`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

            - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

              Resolved default configuration for all tools from an MCP server.

              - `required Boolean Enabled`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

            - `required string McpServerName`

            - `required Type Type`

              - `"mcp_toolset"McpToolset`

          - `class BetaManagedAgentsCustomTool:`

            A custom tool as returned in API responses.

            - `required string Description`

            - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

              JSON Schema for custom tool input parameters.

              - `JsonElement Type "object"constant`

              - `IReadOnlyDictionary<string, JsonElement>? Properties`

              - `IReadOnlyList<string>? Required`

            - `required string Name`

            - `required Type Type`

              - `"custom"Custom`

        - `required Type Type`

          - `"agent"Agent`

        - `required Int Version`

      - `required Type Type`

        - `"coordinator"Coordinator`

    - `required string Name`

    - `required IReadOnlyList<Skill> Skills`

      - `class BetaManagedAgentsAnthropicSkill:`

        A resolved Anthropic-managed skill.

      - `class BetaManagedAgentsCustomSkill:`

        A resolved user-created custom skill.

    - `required string? System`

    - `required IReadOnlyList<Tool> Tools`

      - `class BetaManagedAgentsAgentToolset20260401:`

      - `class BetaManagedAgentsMcpToolset:`

      - `class BetaManagedAgentsCustomTool:`

        A custom tool as returned in API responses.

    - `required Type Type`

      - `"agent"Agent`

    - `required Int Version`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string EnvironmentID`

  - `required IReadOnlyDictionary<string, string> Metadata`

  - `required IReadOnlyList<BetaManagedAgentsOutcomeEvaluationResource> OutcomeEvaluations`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

    - `required DateTimeOffset? CompletedAt`

      A timestamp in RFC 3339 format

    - `required string Description`

      What the agent should produce.

    - `required string? Explanation`

      Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

    - `required Int Iteration`

      0-indexed revision cycle the outcome is currently on.

    - `required string OutcomeID`

      Server-generated outc_ ID for this outcome.

    - `required string Result`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `required Type Type`

      - `"outcome_evaluation"OutcomeEvaluation`

  - `required IReadOnlyList<BetaManagedAgentsSessionResource> Resources`

    - `class BetaManagedAgentsGitHubRepositoryResource:`

      - `required string ID`

      - `required DateTimeOffset CreatedAt`

        A timestamp in RFC 3339 format

      - `required string MountPath`

      - `required Type Type`

        - `"github_repository"GitHubRepository`

      - `required DateTimeOffset UpdatedAt`

        A timestamp in RFC 3339 format

      - `required string Url`

      - `Checkout? Checkout`

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

          - `required Type Type`

            - `"branch"Branch`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

          - `required Type Type`

            - `"commit"Commit`

    - `class BetaManagedAgentsFileResource:`

      - `required string ID`

      - `required DateTimeOffset CreatedAt`

        A timestamp in RFC 3339 format

      - `required string FileID`

      - `required string MountPath`

      - `required Type Type`

        - `"file"File`

      - `required DateTimeOffset UpdatedAt`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsMemoryStoreResource:`

      A memory store attached to an agent session.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

        - `"memory_store"MemoryStore`

      - `Access? Access`

        Access mode for an attached memory store.

        - `"read_write"ReadWrite`

        - `"read_only"ReadOnly`

      - `string Description`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      - `string? MountPath`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `string? Name`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `required BetaManagedAgentsSessionStats Stats`

    Timing statistics for a session.

    - `Double ActiveSeconds`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

    - `Double DurationSeconds`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

  - `required Status Status`

    SessionStatus enum

    - `"rescheduling"Rescheduling`

    - `"running"Running`

    - `"idle"Idle`

    - `"terminated"Terminated`

  - `required string? Title`

  - `required Type Type`

    - `"session"Session`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required BetaManagedAgentsSessionUsage Usage`

    Cumulative token usage for a session across all turns.

    - `BetaManagedAgentsCacheCreationUsage CacheCreation`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Int Ephemeral1hInputTokens`

        Tokens used to create 1-hour ephemeral cache entries.

      - `Int Ephemeral5mInputTokens`

        Tokens used to create 5-minute ephemeral cache entries.

    - `Int CacheReadInputTokens`

      Total tokens read from prompt cache.

    - `Int InputTokens`

      Total input tokens consumed across all turns.

    - `Int OutputTokens`

      Total output tokens generated across all turns.

  - `required IReadOnlyList<string> VaultIds`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `string? DeploymentID`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```csharp
SessionCreateParams parameters = new()
{
    Agent = "agent_011CZkYpogX7uDKUyvBTophP",
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW",
};

var betaManagedAgentsSession = await client.Beta.Sessions.Create(parameters);

Console.WriteLine(betaManagedAgentsSession);
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
