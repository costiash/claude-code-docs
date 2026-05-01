# Sessions

## Create

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

              - `required Type Type`

                - `"always_allow"AlwaysAllow`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `required Type Type`

                - `"always_ask"AlwaysAsk`

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

              - `required Type Type`

                - `"always_allow"AlwaysAllow`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `required Type Type`

                - `"always_ask"AlwaysAsk`

        - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `required Boolean Enabled`

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

        - `required string McpServerName`

        - `required Type Type`

          - `"mcp_toolset"McpToolset`

      - `class BetaManagedAgentsCustomTool:`

        A custom tool as returned in API responses.

        - `required string Description`

        - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

          JSON Schema for custom tool input parameters.

          - `IReadOnlyDictionary<string, JsonElement>? Properties`

            JSON Schema properties defining the tool's input parameters.

          - `IReadOnlyList<string> Required`

            List of required property names.

          - `Type Type`

            Must be 'object' for tool input schemas.

            - `"object"Object`

        - `required string Name`

        - `required Type Type`

          - `"custom"Custom`

    - `required Type Type`

      - `"agent"Agent`

    - `required Int Version`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string EnvironmentID`

  - `required IReadOnlyDictionary<string, string> Metadata`

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

## List

`SessionListPageResponse Beta.Sessions.List(SessionListParams?parameters, CancellationTokencancellationToken = default)`

**get** `/v1/sessions`

List Sessions

### Parameters

- `SessionListParams parameters`

  - `string agentID`

    Query param: Filter sessions created with this agent ID.

  - `Int agentVersion`

    Query param: Filter by agent version. Only applies when agent_id is also set.

  - `DateTimeOffset createdAtGt`

    Query param: Return sessions created after this time (exclusive).

  - `DateTimeOffset createdAtGte`

    Query param: Return sessions created at or after this time (inclusive).

  - `DateTimeOffset createdAtLt`

    Query param: Return sessions created before this time (exclusive).

  - `DateTimeOffset createdAtLte`

    Query param: Return sessions created at or before this time (inclusive).

  - `Boolean includeArchived`

    Query param: When true, includes archived sessions. Default: false (exclude archived).

  - `Int limit`

    Query param: Maximum number of results to return.

  - `string memoryStoreID`

    Query param: Filter sessions whose resources contain a memory_store with this memory store ID.

  - `Order order`

    Query param: Sort direction for results, ordered by created_at. Defaults to desc (newest first).

    - `"asc"Asc`

    - `"desc"Desc`

  - `string page`

    Query param: Opaque pagination cursor from a previous response's next_page.

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

### Returns

- `class SessionListPageResponse:`

  Paginated list of sessions.

  - `IReadOnlyList<BetaManagedAgentsSession> Data`

    List of sessions.

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

                - `required Type Type`

                  - `"always_allow"AlwaysAllow`

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

                - `required Type Type`

                  - `"always_ask"AlwaysAsk`

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

                - `required Type Type`

                  - `"always_allow"AlwaysAllow`

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

                - `required Type Type`

                  - `"always_ask"AlwaysAsk`

          - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `required Boolean Enabled`

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

          - `required string McpServerName`

          - `required Type Type`

            - `"mcp_toolset"McpToolset`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

          - `required string Description`

          - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

            JSON Schema for custom tool input parameters.

            - `IReadOnlyDictionary<string, JsonElement>? Properties`

              JSON Schema properties defining the tool's input parameters.

            - `IReadOnlyList<string> Required`

              List of required property names.

            - `Type Type`

              Must be 'object' for tool input schemas.

              - `"object"Object`

          - `required string Name`

          - `required Type Type`

            - `"custom"Custom`

      - `required Type Type`

        - `"agent"Agent`

      - `required Int Version`

    - `required DateTimeOffset? ArchivedAt`

      A timestamp in RFC 3339 format

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required string EnvironmentID`

    - `required IReadOnlyDictionary<string, string> Metadata`

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

  - `string? NextPage`

    Opaque cursor for the next page. Null when no more results.

### Example

```csharp
SessionListParams parameters = new();

var page = await client.Beta.Sessions.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

## Retrieve

`BetaManagedAgentsSession Beta.Sessions.Retrieve(SessionRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/sessions/{session_id}`

Get Session

### Parameters

- `SessionRetrieveParams parameters`

  - `required string sessionID`

    Path parameter session_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

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

              - `required Type Type`

                - `"always_allow"AlwaysAllow`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `required Type Type`

                - `"always_ask"AlwaysAsk`

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

              - `required Type Type`

                - `"always_allow"AlwaysAllow`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `required Type Type`

                - `"always_ask"AlwaysAsk`

        - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `required Boolean Enabled`

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

        - `required string McpServerName`

        - `required Type Type`

          - `"mcp_toolset"McpToolset`

      - `class BetaManagedAgentsCustomTool:`

        A custom tool as returned in API responses.

        - `required string Description`

        - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

          JSON Schema for custom tool input parameters.

          - `IReadOnlyDictionary<string, JsonElement>? Properties`

            JSON Schema properties defining the tool's input parameters.

          - `IReadOnlyList<string> Required`

            List of required property names.

          - `Type Type`

            Must be 'object' for tool input schemas.

            - `"object"Object`

        - `required string Name`

        - `required Type Type`

          - `"custom"Custom`

    - `required Type Type`

      - `"agent"Agent`

    - `required Int Version`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string EnvironmentID`

  - `required IReadOnlyDictionary<string, string> Metadata`

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

### Example

```csharp
SessionRetrieveParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7"
};

var betaManagedAgentsSession = await client.Beta.Sessions.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsSession);
```

## Update

`BetaManagedAgentsSession Beta.Sessions.Update(SessionUpdateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/sessions/{session_id}`

Update Session

### Parameters

- `SessionUpdateParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `IReadOnlyDictionary<string, string>? metadata`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve.

  - `string? title`

    Body param: Human-readable session title.

  - `IReadOnlyList<string> vaultIds`

    Body param: Vault IDs (`vlt_*`) to attach to the session. Not yet supported; requests setting this field are rejected. Reserved for future use.

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

              - `required Type Type`

                - `"always_allow"AlwaysAllow`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `required Type Type`

                - `"always_ask"AlwaysAsk`

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

              - `required Type Type`

                - `"always_allow"AlwaysAllow`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `required Type Type`

                - `"always_ask"AlwaysAsk`

        - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `required Boolean Enabled`

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

        - `required string McpServerName`

        - `required Type Type`

          - `"mcp_toolset"McpToolset`

      - `class BetaManagedAgentsCustomTool:`

        A custom tool as returned in API responses.

        - `required string Description`

        - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

          JSON Schema for custom tool input parameters.

          - `IReadOnlyDictionary<string, JsonElement>? Properties`

            JSON Schema properties defining the tool's input parameters.

          - `IReadOnlyList<string> Required`

            List of required property names.

          - `Type Type`

            Must be 'object' for tool input schemas.

            - `"object"Object`

        - `required string Name`

        - `required Type Type`

          - `"custom"Custom`

    - `required Type Type`

      - `"agent"Agent`

    - `required Int Version`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string EnvironmentID`

  - `required IReadOnlyDictionary<string, string> Metadata`

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

### Example

```csharp
SessionUpdateParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7"
};

var betaManagedAgentsSession = await client.Beta.Sessions.Update(parameters);

Console.WriteLine(betaManagedAgentsSession);
```

## Delete

`BetaManagedAgentsDeletedSession Beta.Sessions.Delete(SessionDeleteParamsparameters, CancellationTokencancellationToken = default)`

**delete** `/v1/sessions/{session_id}`

Delete Session

### Parameters

- `SessionDeleteParams parameters`

  - `required string sessionID`

    Path parameter session_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

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

### Returns

- `class BetaManagedAgentsDeletedSession:`

  Confirmation that a `session` has been permanently deleted.

  - `required string ID`

  - `required Type Type`

    - `"session_deleted"SessionDeleted`

### Example

```csharp
SessionDeleteParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7"
};

var betaManagedAgentsDeletedSession = await client.Beta.Sessions.Delete(parameters);

Console.WriteLine(betaManagedAgentsDeletedSession);
```

## Archive

`BetaManagedAgentsSession Beta.Sessions.Archive(SessionArchiveParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/sessions/{session_id}/archive`

Archive Session

### Parameters

- `SessionArchiveParams parameters`

  - `required string sessionID`

    Path parameter session_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

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

              - `required Type Type`

                - `"always_allow"AlwaysAllow`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `required Type Type`

                - `"always_ask"AlwaysAsk`

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

              - `required Type Type`

                - `"always_allow"AlwaysAllow`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `required Type Type`

                - `"always_ask"AlwaysAsk`

        - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `required Boolean Enabled`

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

        - `required string McpServerName`

        - `required Type Type`

          - `"mcp_toolset"McpToolset`

      - `class BetaManagedAgentsCustomTool:`

        A custom tool as returned in API responses.

        - `required string Description`

        - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

          JSON Schema for custom tool input parameters.

          - `IReadOnlyDictionary<string, JsonElement>? Properties`

            JSON Schema properties defining the tool's input parameters.

          - `IReadOnlyList<string> Required`

            List of required property names.

          - `Type Type`

            Must be 'object' for tool input schemas.

            - `"object"Object`

        - `required string Name`

        - `required Type Type`

          - `"custom"Custom`

    - `required Type Type`

      - `"agent"Agent`

    - `required Int Version`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string EnvironmentID`

  - `required IReadOnlyDictionary<string, string> Metadata`

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

### Example

```csharp
SessionArchiveParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7"
};

var betaManagedAgentsSession = await client.Beta.Sessions.Archive(parameters);

Console.WriteLine(betaManagedAgentsSession);
```

## Domain Types

### Beta Managed Agents Agent Params

- `class BetaManagedAgentsAgentParams:`

  Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

  - `required string ID`

    The `agent` ID.

  - `required Type Type`

    - `"agent"Agent`

  - `Int Version`

    The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

### Beta Managed Agents Branch Checkout

- `class BetaManagedAgentsBranchCheckout:`

  - `required string Name`

    Branch name to check out.

  - `required Type Type`

    - `"branch"Branch`

### Beta Managed Agents Cache Creation Usage

- `class BetaManagedAgentsCacheCreationUsage:`

  Prompt-cache creation token usage broken down by cache lifetime.

  - `Int Ephemeral1hInputTokens`

    Tokens used to create 1-hour ephemeral cache entries.

  - `Int Ephemeral5mInputTokens`

    Tokens used to create 5-minute ephemeral cache entries.

### Beta Managed Agents Commit Checkout

- `class BetaManagedAgentsCommitCheckout:`

  - `required string Sha`

    Full commit SHA to check out.

  - `required Type Type`

    - `"commit"Commit`

### Beta Managed Agents Deleted Session

- `class BetaManagedAgentsDeletedSession:`

  Confirmation that a `session` has been permanently deleted.

  - `required string ID`

  - `required Type Type`

    - `"session_deleted"SessionDeleted`

### Beta Managed Agents File Resource Params

- `class BetaManagedAgentsFileResourceParams:`

  Mount a file uploaded via the Files API into the session.

  - `required string FileID`

    ID of a previously uploaded file.

  - `required Type Type`

    - `"file"File`

  - `string? MountPath`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

### Beta Managed Agents GitHub Repository Resource Params

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

### Beta Managed Agents Memory Store Resource Param

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

### Beta Managed Agents Session

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

              - `required Type Type`

                - `"always_allow"AlwaysAllow`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `required Type Type`

                - `"always_ask"AlwaysAsk`

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

              - `required Type Type`

                - `"always_allow"AlwaysAllow`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `required Type Type`

                - `"always_ask"AlwaysAsk`

        - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `required Boolean Enabled`

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

        - `required string McpServerName`

        - `required Type Type`

          - `"mcp_toolset"McpToolset`

      - `class BetaManagedAgentsCustomTool:`

        A custom tool as returned in API responses.

        - `required string Description`

        - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

          JSON Schema for custom tool input parameters.

          - `IReadOnlyDictionary<string, JsonElement>? Properties`

            JSON Schema properties defining the tool's input parameters.

          - `IReadOnlyList<string> Required`

            List of required property names.

          - `Type Type`

            Must be 'object' for tool input schemas.

            - `"object"Object`

        - `required string Name`

        - `required Type Type`

          - `"custom"Custom`

    - `required Type Type`

      - `"agent"Agent`

    - `required Int Version`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string EnvironmentID`

  - `required IReadOnlyDictionary<string, string> Metadata`

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

### Beta Managed Agents Session Agent

- `class BetaManagedAgentsSessionAgent:`

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

            - `required Type Type`

              - `"always_allow"AlwaysAllow`

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

            - `required Type Type`

              - `"always_ask"AlwaysAsk`

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

            - `required Type Type`

              - `"always_allow"AlwaysAllow`

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

            - `required Type Type`

              - `"always_ask"AlwaysAsk`

      - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `required Boolean Enabled`

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

      - `required string McpServerName`

      - `required Type Type`

        - `"mcp_toolset"McpToolset`

    - `class BetaManagedAgentsCustomTool:`

      A custom tool as returned in API responses.

      - `required string Description`

      - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

        JSON Schema for custom tool input parameters.

        - `IReadOnlyDictionary<string, JsonElement>? Properties`

          JSON Schema properties defining the tool's input parameters.

        - `IReadOnlyList<string> Required`

          List of required property names.

        - `Type Type`

          Must be 'object' for tool input schemas.

          - `"object"Object`

      - `required string Name`

      - `required Type Type`

        - `"custom"Custom`

  - `required Type Type`

    - `"agent"Agent`

  - `required Int Version`

### Beta Managed Agents Session Stats

- `class BetaManagedAgentsSessionStats:`

  Timing statistics for a session.

  - `Double ActiveSeconds`

    Cumulative time in seconds the session spent in running status. Excludes idle time.

  - `Double DurationSeconds`

    Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

### Beta Managed Agents Session Usage

- `class BetaManagedAgentsSessionUsage:`

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

# Events

## List

`EventListPageResponse Beta.Sessions.Events.List(EventListParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/sessions/{session_id}/events`

List Events

### Parameters

- `EventListParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `Int limit`

    Query param: Query parameter for limit

  - `Order order`

    Query param: Sort direction for results, ordered by created_at. Defaults to asc (chronological).

    - `"asc"Asc`

    - `"desc"Desc`

  - `string page`

    Query param: Opaque pagination cursor from a previous response's next_page.

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

### Returns

- `class EventListPageResponse:`

  Paginated list of events for a `session`.

  - `IReadOnlyList<BetaManagedAgentsSessionEvent> Data`

    Events for the session, ordered by `created_at`.

    - `class BetaManagedAgentsUserMessageEvent:`

      A user message event in the session conversation.

      - `required string ID`

        Unique identifier for this event.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks comprising the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

      - `required Type Type`

        - `"user.message"UserMessage`

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserInterruptEvent:`

      An interrupt event that pauses agent execution and returns control to the user.

      - `required string ID`

        Unique identifier for this event.

      - `required Type Type`

        - `"user.interrupt"UserInterrupt`

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserToolConfirmationEvent:`

      A tool confirmation event that approves or denies a pending tool execution.

      - `required string ID`

        Unique identifier for this event.

      - `required Result Result`

        UserToolConfirmationResult enum

        - `"allow"Allow`

        - `"deny"Deny`

      - `required string ToolUseID`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `required Type Type`

        - `"user.tool_confirmation"UserToolConfirmation`

      - `string? DenyMessage`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserCustomToolResultEvent:`

      Event sent by the client providing the result of a custom tool execution.

      - `required string ID`

        Unique identifier for this event.

      - `required string CustomToolUseID`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `required Type Type`

        - `"user.custom_tool_result"UserCustomToolResult`

      - `IReadOnlyList<Content> Content`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

      - `Boolean? IsError`

        Whether the tool execution resulted in an error.

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsAgentCustomToolUseEvent:`

      Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

      - `required string ID`

        Unique identifier for this event.

      - `required IReadOnlyDictionary<string, JsonElement> Input`

        Input parameters for the tool call.

      - `required string Name`

        Name of the custom tool being called.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"agent.custom_tool_use"AgentCustomToolUse`

    - `class BetaManagedAgentsAgentMessageEvent:`

      An agent response event in the session conversation.

      - `required string ID`

        Unique identifier for this event.

      - `required IReadOnlyList<BetaManagedAgentsTextBlock> Content`

        Array of text blocks comprising the agent response.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"agent.message"AgentMessage`

    - `class BetaManagedAgentsAgentThinkingEvent:`

      Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"agent.thinking"AgentThinking`

    - `class BetaManagedAgentsAgentMcpToolUseEvent:`

      Event emitted when the agent invokes a tool provided by an MCP server.

      - `required string ID`

        Unique identifier for this event.

      - `required IReadOnlyDictionary<string, JsonElement> Input`

        Input parameters for the tool call.

      - `required string McpServerName`

        Name of the MCP server providing the tool.

      - `required string Name`

        Name of the MCP tool being used.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"agent.mcp_tool_use"AgentMcpToolUse`

      - `EvaluatedPermission EvaluatedPermission`

        AgentEvaluatedPermission enum

        - `"allow"Allow`

        - `"ask"Ask`

        - `"deny"Deny`

    - `class BetaManagedAgentsAgentMcpToolResultEvent:`

      Event representing the result of an MCP tool execution.

      - `required string ID`

        Unique identifier for this event.

      - `required string McpToolUseID`

        The id of the `agent.mcp_tool_use` event this result corresponds to.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"agent.mcp_tool_result"AgentMcpToolResult`

      - `IReadOnlyList<Content> Content`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

      - `Boolean? IsError`

        Whether the tool execution resulted in an error.

    - `class BetaManagedAgentsAgentToolUseEvent:`

      Event emitted when the agent invokes a built-in agent tool.

      - `required string ID`

        Unique identifier for this event.

      - `required IReadOnlyDictionary<string, JsonElement> Input`

        Input parameters for the tool call.

      - `required string Name`

        Name of the agent tool being used.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"agent.tool_use"AgentToolUse`

      - `EvaluatedPermission EvaluatedPermission`

        AgentEvaluatedPermission enum

        - `"allow"Allow`

        - `"ask"Ask`

        - `"deny"Deny`

    - `class BetaManagedAgentsAgentToolResultEvent:`

      Event representing the result of an agent tool execution.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required string ToolUseID`

        The id of the `agent.tool_use` event this result corresponds to.

      - `required Type Type`

        - `"agent.tool_result"AgentToolResult`

      - `IReadOnlyList<Content> Content`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

      - `Boolean? IsError`

        Whether the tool execution resulted in an error.

    - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

      Indicates that context compaction (summarization) occurred during the session.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"agent.thread_context_compacted"AgentThreadContextCompacted`

    - `class BetaManagedAgentsSessionErrorEvent:`

      An error event indicating a problem occurred during session execution.

      - `required string ID`

        Unique identifier for this event.

      - `required Error Error`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `class BetaManagedAgentsUnknownError:`

          An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

          - `required string Message`

            Human-readable error description.

          - `required RetryStatus RetryStatus`

            What the client should do next in response to this error.

            - `class BetaManagedAgentsRetryStatusRetrying:`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

              - `required Type Type`

                - `"retrying"Retrying`

            - `class BetaManagedAgentsRetryStatusExhausted:`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

              - `required Type Type`

                - `"exhausted"Exhausted`

            - `class BetaManagedAgentsRetryStatusTerminal:`

              The session encountered a terminal error and will transition to `terminated` state.

              - `required Type Type`

                - `"terminal"Terminal`

          - `required Type Type`

            - `"unknown_error"UnknownError`

        - `class BetaManagedAgentsModelOverloadedError:`

          The model is currently overloaded. Emitted after automatic retries are exhausted.

          - `required string Message`

            Human-readable error description.

          - `required RetryStatus RetryStatus`

            What the client should do next in response to this error.

            - `class BetaManagedAgentsRetryStatusRetrying:`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

              - `required Type Type`

                - `"retrying"Retrying`

            - `class BetaManagedAgentsRetryStatusExhausted:`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

              - `required Type Type`

                - `"exhausted"Exhausted`

            - `class BetaManagedAgentsRetryStatusTerminal:`

              The session encountered a terminal error and will transition to `terminated` state.

              - `required Type Type`

                - `"terminal"Terminal`

          - `required Type Type`

            - `"model_overloaded_error"ModelOverloadedError`

        - `class BetaManagedAgentsModelRateLimitedError:`

          The model request was rate-limited.

          - `required string Message`

            Human-readable error description.

          - `required RetryStatus RetryStatus`

            What the client should do next in response to this error.

            - `class BetaManagedAgentsRetryStatusRetrying:`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

              - `required Type Type`

                - `"retrying"Retrying`

            - `class BetaManagedAgentsRetryStatusExhausted:`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

              - `required Type Type`

                - `"exhausted"Exhausted`

            - `class BetaManagedAgentsRetryStatusTerminal:`

              The session encountered a terminal error and will transition to `terminated` state.

              - `required Type Type`

                - `"terminal"Terminal`

          - `required Type Type`

            - `"model_rate_limited_error"ModelRateLimitedError`

        - `class BetaManagedAgentsModelRequestFailedError:`

          A model request failed for a reason other than overload or rate-limiting.

          - `required string Message`

            Human-readable error description.

          - `required RetryStatus RetryStatus`

            What the client should do next in response to this error.

            - `class BetaManagedAgentsRetryStatusRetrying:`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

              - `required Type Type`

                - `"retrying"Retrying`

            - `class BetaManagedAgentsRetryStatusExhausted:`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

              - `required Type Type`

                - `"exhausted"Exhausted`

            - `class BetaManagedAgentsRetryStatusTerminal:`

              The session encountered a terminal error and will transition to `terminated` state.

              - `required Type Type`

                - `"terminal"Terminal`

          - `required Type Type`

            - `"model_request_failed_error"ModelRequestFailedError`

        - `class BetaManagedAgentsMcpConnectionFailedError:`

          Failed to connect to an MCP server.

          - `required string McpServerName`

            Name of the MCP server that failed to connect.

          - `required string Message`

            Human-readable error description.

          - `required RetryStatus RetryStatus`

            What the client should do next in response to this error.

            - `class BetaManagedAgentsRetryStatusRetrying:`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

              - `required Type Type`

                - `"retrying"Retrying`

            - `class BetaManagedAgentsRetryStatusExhausted:`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

              - `required Type Type`

                - `"exhausted"Exhausted`

            - `class BetaManagedAgentsRetryStatusTerminal:`

              The session encountered a terminal error and will transition to `terminated` state.

              - `required Type Type`

                - `"terminal"Terminal`

          - `required Type Type`

            - `"mcp_connection_failed_error"McpConnectionFailedError`

        - `class BetaManagedAgentsMcpAuthenticationFailedError:`

          Authentication to an MCP server failed.

          - `required string McpServerName`

            Name of the MCP server that failed authentication.

          - `required string Message`

            Human-readable error description.

          - `required RetryStatus RetryStatus`

            What the client should do next in response to this error.

            - `class BetaManagedAgentsRetryStatusRetrying:`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

              - `required Type Type`

                - `"retrying"Retrying`

            - `class BetaManagedAgentsRetryStatusExhausted:`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

              - `required Type Type`

                - `"exhausted"Exhausted`

            - `class BetaManagedAgentsRetryStatusTerminal:`

              The session encountered a terminal error and will transition to `terminated` state.

              - `required Type Type`

                - `"terminal"Terminal`

          - `required Type Type`

            - `"mcp_authentication_failed_error"McpAuthenticationFailedError`

        - `class BetaManagedAgentsBillingError:`

          The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

          - `required string Message`

            Human-readable error description.

          - `required RetryStatus RetryStatus`

            What the client should do next in response to this error.

            - `class BetaManagedAgentsRetryStatusRetrying:`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

              - `required Type Type`

                - `"retrying"Retrying`

            - `class BetaManagedAgentsRetryStatusExhausted:`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

              - `required Type Type`

                - `"exhausted"Exhausted`

            - `class BetaManagedAgentsRetryStatusTerminal:`

              The session encountered a terminal error and will transition to `terminated` state.

              - `required Type Type`

                - `"terminal"Terminal`

          - `required Type Type`

            - `"billing_error"BillingError`

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"session.error"SessionError`

    - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

      Indicates the session is recovering from an error state and is rescheduled for execution.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"session.status_rescheduled"SessionStatusRescheduled`

    - `class BetaManagedAgentsSessionStatusRunningEvent:`

      Indicates the session is actively running and the agent is working.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"session.status_running"SessionStatusRunning`

    - `class BetaManagedAgentsSessionStatusIdleEvent:`

      Indicates the agent has paused and is awaiting user input.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required StopReason StopReason`

        The agent completed its turn naturally and is ready for the next user message.

        - `class BetaManagedAgentsSessionEndTurn:`

          The agent completed its turn naturally and is ready for the next user message.

          - `required Type Type`

            - `"end_turn"EndTurn`

        - `class BetaManagedAgentsSessionRequiresAction:`

          The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

          - `required IReadOnlyList<string> EventIds`

            The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

          - `required Type Type`

            - `"requires_action"RequiresAction`

        - `class BetaManagedAgentsSessionRetriesExhausted:`

          The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

          - `required Type Type`

            - `"retries_exhausted"RetriesExhausted`

      - `required Type Type`

        - `"session.status_idle"SessionStatusIdle`

    - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

      Indicates the session has terminated, either due to an error or completion.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"session.status_terminated"SessionStatusTerminated`

    - `class BetaManagedAgentsSpanModelRequestStartEvent:`

      Emitted when a model request is initiated by the agent.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"span.model_request_start"SpanModelRequestStart`

    - `class BetaManagedAgentsSpanModelRequestEndEvent:`

      Emitted when a model request completes.

      - `required string ID`

        Unique identifier for this event.

      - `required Boolean? IsError`

        Whether the model request resulted in an error.

      - `required string ModelRequestStartID`

        The id of the corresponding `span.model_request_start` event.

      - `required BetaManagedAgentsSpanModelUsage ModelUsage`

        Token usage for a single model request.

        - `required Int CacheCreationInputTokens`

          Tokens used to create prompt cache in this request.

        - `required Int CacheReadInputTokens`

          Tokens read from prompt cache in this request.

        - `required Int InputTokens`

          Input tokens consumed by this request.

        - `required Int OutputTokens`

          Output tokens generated by this request.

        - `Speed? Speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"Standard`

          - `"fast"Fast`

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"span.model_request_end"SpanModelRequestEnd`

    - `class BetaManagedAgentsSessionDeletedEvent:`

      Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"session.deleted"SessionDeleted`

  - `string? NextPage`

    Opaque cursor for the next page. Null when no more results.

### Example

```csharp
EventListParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7"
};

var page = await client.Beta.Sessions.Events.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

## Send

`BetaManagedAgentsSendSessionEvents Beta.Sessions.Events.Send(EventSendParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/sessions/{session_id}/events`

Send Events

### Parameters

- `EventSendParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required IReadOnlyList<BetaManagedAgentsEventParams> events`

    Body param: Events to send to the `session`.

    - `class BetaManagedAgentsUserMessageEventParams:`

      Parameters for sending a user message to the session.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

      - `required Type Type`

        - `"user.message"UserMessage`

    - `class BetaManagedAgentsUserInterruptEventParams:`

      Parameters for sending an interrupt to pause the agent.

      - `required Type Type`

        - `"user.interrupt"UserInterrupt`

    - `class BetaManagedAgentsUserToolConfirmationEventParams:`

      Parameters for confirming or denying a tool execution request.

      - `required Result Result`

        UserToolConfirmationResult enum

        - `"allow"Allow`

        - `"deny"Deny`

      - `required string ToolUseID`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `required Type Type`

        - `"user.tool_confirmation"UserToolConfirmation`

      - `string? DenyMessage`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `class BetaManagedAgentsUserCustomToolResultEventParams:`

      Parameters for providing the result of a custom tool execution.

      - `required string CustomToolUseID`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `required Type Type`

        - `"user.custom_tool_result"UserCustomToolResult`

      - `IReadOnlyList<Content> Content`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

      - `Boolean? IsError`

        Whether the tool execution resulted in an error.

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

### Returns

- `class BetaManagedAgentsSendSessionEvents:`

  Events that were successfully sent to the session.

  - `IReadOnlyList<Data> Data`

    Sent events

    - `class BetaManagedAgentsUserMessageEvent:`

      A user message event in the session conversation.

      - `required string ID`

        Unique identifier for this event.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks comprising the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

      - `required Type Type`

        - `"user.message"UserMessage`

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserInterruptEvent:`

      An interrupt event that pauses agent execution and returns control to the user.

      - `required string ID`

        Unique identifier for this event.

      - `required Type Type`

        - `"user.interrupt"UserInterrupt`

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserToolConfirmationEvent:`

      A tool confirmation event that approves or denies a pending tool execution.

      - `required string ID`

        Unique identifier for this event.

      - `required Result Result`

        UserToolConfirmationResult enum

        - `"allow"Allow`

        - `"deny"Deny`

      - `required string ToolUseID`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `required Type Type`

        - `"user.tool_confirmation"UserToolConfirmation`

      - `string? DenyMessage`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserCustomToolResultEvent:`

      Event sent by the client providing the result of a custom tool execution.

      - `required string ID`

        Unique identifier for this event.

      - `required string CustomToolUseID`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `required Type Type`

        - `"user.custom_tool_result"UserCustomToolResult`

      - `IReadOnlyList<Content> Content`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

      - `Boolean? IsError`

        Whether the tool execution resulted in an error.

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

### Example

```csharp
EventSendParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    Events =
    [
        new BetaManagedAgentsUserMessageEventParams()
        {
            Content =
            [
                new BetaManagedAgentsTextBlock()
                {
                    Text = "Where is my order #1234?",
                    Type = Type.Text,
                },
            ],
            Type = Type.UserMessage,
        },
    ],
};

var betaManagedAgentsSendSessionEvents = await client.Beta.Sessions.Events.Send(parameters);

Console.WriteLine(betaManagedAgentsSendSessionEvents);
```

## Stream

`BetaManagedAgentsStreamSessionEvents Beta.Sessions.Events.StreamStreaming(EventStreamParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/sessions/{session_id}/events/stream`

Stream Events

### Parameters

- `EventStreamParams parameters`

  - `required string sessionID`

    Path parameter session_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

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

### Returns

- `class BetaManagedAgentsStreamSessionEvents: A class that can be one of several variants.union`

  Server-sent event in the session stream.

  - `class BetaManagedAgentsUserMessageEvent:`

    A user message event in the session conversation.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"image"Image`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"TextPlain`

            - `required Type Type`

              - `"text"Text`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"document"Document`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

    - `required Type Type`

      - `"user.message"UserMessage`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent:`

    An interrupt event that pauses agent execution and returns control to the user.

    - `required string ID`

      Unique identifier for this event.

    - `required Type Type`

      - `"user.interrupt"UserInterrupt`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserToolConfirmationEvent:`

    A tool confirmation event that approves or denies a pending tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required Result Result`

      UserToolConfirmationResult enum

      - `"allow"Allow`

      - `"deny"Deny`

    - `required string ToolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

      - `"user.tool_confirmation"UserToolConfirmation`

    - `string? DenyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserCustomToolResultEvent:`

    Event sent by the client providing the result of a custom tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required string CustomToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

      - `"user.custom_tool_result"UserCustomToolResult`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"image"Image`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"TextPlain`

            - `required Type Type`

              - `"text"Text`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"document"Document`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

    - `Boolean? IsError`

      Whether the tool execution resulted in an error.

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsAgentCustomToolUseEvent:`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string Name`

      Name of the custom tool being called.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.custom_tool_use"AgentCustomToolUse`

  - `class BetaManagedAgentsAgentMessageEvent:`

    An agent response event in the session conversation.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<BetaManagedAgentsTextBlock> Content`

      Array of text blocks comprising the agent response.

      - `required string Text`

        The text content.

      - `required Type Type`

        - `"text"Text`

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.message"AgentMessage`

  - `class BetaManagedAgentsAgentThinkingEvent:`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.thinking"AgentThinking`

  - `class BetaManagedAgentsAgentMcpToolUseEvent:`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string McpServerName`

      Name of the MCP server providing the tool.

    - `required string Name`

      Name of the MCP tool being used.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.mcp_tool_use"AgentMcpToolUse`

    - `EvaluatedPermission EvaluatedPermission`

      AgentEvaluatedPermission enum

      - `"allow"Allow`

      - `"ask"Ask`

      - `"deny"Deny`

  - `class BetaManagedAgentsAgentMcpToolResultEvent:`

    Event representing the result of an MCP tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required string McpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.mcp_tool_result"AgentMcpToolResult`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"image"Image`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"TextPlain`

            - `required Type Type`

              - `"text"Text`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"document"Document`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

    - `Boolean? IsError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent:`

    Event emitted when the agent invokes a built-in agent tool.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string Name`

      Name of the agent tool being used.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.tool_use"AgentToolUse`

    - `EvaluatedPermission EvaluatedPermission`

      AgentEvaluatedPermission enum

      - `"allow"Allow`

      - `"ask"Ask`

      - `"deny"Deny`

  - `class BetaManagedAgentsAgentToolResultEvent:`

    Event representing the result of an agent tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string ToolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `required Type Type`

      - `"agent.tool_result"AgentToolResult`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"image"Image`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"TextPlain`

            - `required Type Type`

              - `"text"Text`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"document"Document`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

    - `Boolean? IsError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

    Indicates that context compaction (summarization) occurred during the session.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.thread_context_compacted"AgentThreadContextCompacted`

  - `class BetaManagedAgentsSessionErrorEvent:`

    An error event indicating a problem occurred during session execution.

    - `required string ID`

      Unique identifier for this event.

    - `required Error Error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError:`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"unknown_error"UnknownError`

      - `class BetaManagedAgentsModelOverloadedError:`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"model_overloaded_error"ModelOverloadedError`

      - `class BetaManagedAgentsModelRateLimitedError:`

        The model request was rate-limited.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"model_rate_limited_error"ModelRateLimitedError`

      - `class BetaManagedAgentsModelRequestFailedError:`

        A model request failed for a reason other than overload or rate-limiting.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"model_request_failed_error"ModelRequestFailedError`

      - `class BetaManagedAgentsMcpConnectionFailedError:`

        Failed to connect to an MCP server.

        - `required string McpServerName`

          Name of the MCP server that failed to connect.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"mcp_connection_failed_error"McpConnectionFailedError`

      - `class BetaManagedAgentsMcpAuthenticationFailedError:`

        Authentication to an MCP server failed.

        - `required string McpServerName`

          Name of the MCP server that failed authentication.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"mcp_authentication_failed_error"McpAuthenticationFailedError`

      - `class BetaManagedAgentsBillingError:`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"billing_error"BillingError`

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.error"SessionError`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.status_rescheduled"SessionStatusRescheduled`

  - `class BetaManagedAgentsSessionStatusRunningEvent:`

    Indicates the session is actively running and the agent is working.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.status_running"SessionStatusRunning`

  - `class BetaManagedAgentsSessionStatusIdleEvent:`

    Indicates the agent has paused and is awaiting user input.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required StopReason StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `required Type Type`

          - `"end_turn"EndTurn`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `required IReadOnlyList<string> EventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `required Type Type`

          - `"requires_action"RequiresAction`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `required Type Type`

          - `"retries_exhausted"RetriesExhausted`

    - `required Type Type`

      - `"session.status_idle"SessionStatusIdle`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

    Indicates the session has terminated, either due to an error or completion.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.status_terminated"SessionStatusTerminated`

  - `class BetaManagedAgentsSpanModelRequestStartEvent:`

    Emitted when a model request is initiated by the agent.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"span.model_request_start"SpanModelRequestStart`

  - `class BetaManagedAgentsSpanModelRequestEndEvent:`

    Emitted when a model request completes.

    - `required string ID`

      Unique identifier for this event.

    - `required Boolean? IsError`

      Whether the model request resulted in an error.

    - `required string ModelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `required BetaManagedAgentsSpanModelUsage ModelUsage`

      Token usage for a single model request.

      - `required Int CacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

      - `required Int CacheReadInputTokens`

        Tokens read from prompt cache in this request.

      - `required Int InputTokens`

        Input tokens consumed by this request.

      - `required Int OutputTokens`

        Output tokens generated by this request.

      - `Speed? Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"Standard`

        - `"fast"Fast`

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"span.model_request_end"SpanModelRequestEnd`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.deleted"SessionDeleted`

### Example

```csharp
EventStreamParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7"
};

await foreach (var betaManagedAgentsStreamSessionEvents in client.Beta.Sessions.Events.StreamStreaming(parameters))
{
    Console.WriteLine(betaManagedAgentsStreamSessionEvents);
}
```

## Domain Types

### Beta Managed Agents Agent Custom Tool Use Event

- `class BetaManagedAgentsAgentCustomToolUseEvent:`

  Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

  - `required string ID`

    Unique identifier for this event.

  - `required IReadOnlyDictionary<string, JsonElement> Input`

    Input parameters for the tool call.

  - `required string Name`

    Name of the custom tool being called.

  - `required DateTimeOffset ProcessedAt`

    A timestamp in RFC 3339 format

  - `required Type Type`

    - `"agent.custom_tool_use"AgentCustomToolUse`

### Beta Managed Agents Agent MCP Tool Result Event

- `class BetaManagedAgentsAgentMcpToolResultEvent:`

  Event representing the result of an MCP tool execution.

  - `required string ID`

    Unique identifier for this event.

  - `required string McpToolUseID`

    The id of the `agent.mcp_tool_use` event this result corresponds to.

  - `required DateTimeOffset ProcessedAt`

    A timestamp in RFC 3339 format

  - `required Type Type`

    - `"agent.mcp_tool_result"AgentMcpToolResult`

  - `IReadOnlyList<Content> Content`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock:`

      Regular text content.

      - `required string Text`

        The text content.

      - `required Type Type`

        - `"text"Text`

    - `class BetaManagedAgentsImageBlock:`

      Image content specified directly as base64 data or as a reference via a URL.

      - `required Source Source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource:`

          Base64-encoded image data.

          - `required string Data`

            Base64-encoded image data.

          - `required string MediaType`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `required Type Type`

            - `"base64"Base64`

        - `class BetaManagedAgentsUrlImageSource:`

          Image referenced by URL.

          - `required Type Type`

            - `"url"Url`

          - `required string Url`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource:`

          Image referenced by file ID.

          - `required string FileID`

            ID of a previously uploaded file.

          - `required Type Type`

            - `"file"File`

      - `required Type Type`

        - `"image"Image`

    - `class BetaManagedAgentsDocumentBlock:`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `required Source Source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource:`

          Base64-encoded document data.

          - `required string Data`

            Base64-encoded document data.

          - `required string MediaType`

            MIME type of the document (e.g., "application/pdf").

          - `required Type Type`

            - `"base64"Base64`

        - `class BetaManagedAgentsPlainTextDocumentSource:`

          Plain text document content.

          - `required string Data`

            The plain text content.

          - `required MediaType MediaType`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"TextPlain`

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsUrlDocumentSource:`

          Document referenced by URL.

          - `required Type Type`

            - `"url"Url`

          - `required string Url`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource:`

          Document referenced by file ID.

          - `required string FileID`

            ID of a previously uploaded file.

          - `required Type Type`

            - `"file"File`

      - `required Type Type`

        - `"document"Document`

      - `string? Context`

        Additional context about the document for the model.

      - `string? Title`

        The title of the document.

  - `Boolean? IsError`

    Whether the tool execution resulted in an error.

### Beta Managed Agents Agent MCP Tool Use Event

- `class BetaManagedAgentsAgentMcpToolUseEvent:`

  Event emitted when the agent invokes a tool provided by an MCP server.

  - `required string ID`

    Unique identifier for this event.

  - `required IReadOnlyDictionary<string, JsonElement> Input`

    Input parameters for the tool call.

  - `required string McpServerName`

    Name of the MCP server providing the tool.

  - `required string Name`

    Name of the MCP tool being used.

  - `required DateTimeOffset ProcessedAt`

    A timestamp in RFC 3339 format

  - `required Type Type`

    - `"agent.mcp_tool_use"AgentMcpToolUse`

  - `EvaluatedPermission EvaluatedPermission`

    AgentEvaluatedPermission enum

    - `"allow"Allow`

    - `"ask"Ask`

    - `"deny"Deny`

### Beta Managed Agents Agent Message Event

- `class BetaManagedAgentsAgentMessageEvent:`

  An agent response event in the session conversation.

  - `required string ID`

    Unique identifier for this event.

  - `required IReadOnlyList<BetaManagedAgentsTextBlock> Content`

    Array of text blocks comprising the agent response.

    - `required string Text`

      The text content.

    - `required Type Type`

      - `"text"Text`

  - `required DateTimeOffset ProcessedAt`

    A timestamp in RFC 3339 format

  - `required Type Type`

    - `"agent.message"AgentMessage`

### Beta Managed Agents Agent Thinking Event

- `class BetaManagedAgentsAgentThinkingEvent:`

  Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

  - `required string ID`

    Unique identifier for this event.

  - `required DateTimeOffset ProcessedAt`

    A timestamp in RFC 3339 format

  - `required Type Type`

    - `"agent.thinking"AgentThinking`

### Beta Managed Agents Agent Thread Context Compacted Event

- `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

  Indicates that context compaction (summarization) occurred during the session.

  - `required string ID`

    Unique identifier for this event.

  - `required DateTimeOffset ProcessedAt`

    A timestamp in RFC 3339 format

  - `required Type Type`

    - `"agent.thread_context_compacted"AgentThreadContextCompacted`

### Beta Managed Agents Agent Tool Result Event

- `class BetaManagedAgentsAgentToolResultEvent:`

  Event representing the result of an agent tool execution.

  - `required string ID`

    Unique identifier for this event.

  - `required DateTimeOffset ProcessedAt`

    A timestamp in RFC 3339 format

  - `required string ToolUseID`

    The id of the `agent.tool_use` event this result corresponds to.

  - `required Type Type`

    - `"agent.tool_result"AgentToolResult`

  - `IReadOnlyList<Content> Content`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock:`

      Regular text content.

      - `required string Text`

        The text content.

      - `required Type Type`

        - `"text"Text`

    - `class BetaManagedAgentsImageBlock:`

      Image content specified directly as base64 data or as a reference via a URL.

      - `required Source Source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource:`

          Base64-encoded image data.

          - `required string Data`

            Base64-encoded image data.

          - `required string MediaType`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `required Type Type`

            - `"base64"Base64`

        - `class BetaManagedAgentsUrlImageSource:`

          Image referenced by URL.

          - `required Type Type`

            - `"url"Url`

          - `required string Url`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource:`

          Image referenced by file ID.

          - `required string FileID`

            ID of a previously uploaded file.

          - `required Type Type`

            - `"file"File`

      - `required Type Type`

        - `"image"Image`

    - `class BetaManagedAgentsDocumentBlock:`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `required Source Source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource:`

          Base64-encoded document data.

          - `required string Data`

            Base64-encoded document data.

          - `required string MediaType`

            MIME type of the document (e.g., "application/pdf").

          - `required Type Type`

            - `"base64"Base64`

        - `class BetaManagedAgentsPlainTextDocumentSource:`

          Plain text document content.

          - `required string Data`

            The plain text content.

          - `required MediaType MediaType`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"TextPlain`

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsUrlDocumentSource:`

          Document referenced by URL.

          - `required Type Type`

            - `"url"Url`

          - `required string Url`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource:`

          Document referenced by file ID.

          - `required string FileID`

            ID of a previously uploaded file.

          - `required Type Type`

            - `"file"File`

      - `required Type Type`

        - `"document"Document`

      - `string? Context`

        Additional context about the document for the model.

      - `string? Title`

        The title of the document.

  - `Boolean? IsError`

    Whether the tool execution resulted in an error.

### Beta Managed Agents Agent Tool Use Event

- `class BetaManagedAgentsAgentToolUseEvent:`

  Event emitted when the agent invokes a built-in agent tool.

  - `required string ID`

    Unique identifier for this event.

  - `required IReadOnlyDictionary<string, JsonElement> Input`

    Input parameters for the tool call.

  - `required string Name`

    Name of the agent tool being used.

  - `required DateTimeOffset ProcessedAt`

    A timestamp in RFC 3339 format

  - `required Type Type`

    - `"agent.tool_use"AgentToolUse`

  - `EvaluatedPermission EvaluatedPermission`

    AgentEvaluatedPermission enum

    - `"allow"Allow`

    - `"ask"Ask`

    - `"deny"Deny`

### Beta Managed Agents Base64 Document Source

- `class BetaManagedAgentsBase64DocumentSource:`

  Base64-encoded document data.

  - `required string Data`

    Base64-encoded document data.

  - `required string MediaType`

    MIME type of the document (e.g., "application/pdf").

  - `required Type Type`

    - `"base64"Base64`

### Beta Managed Agents Base64 Image Source

- `class BetaManagedAgentsBase64ImageSource:`

  Base64-encoded image data.

  - `required string Data`

    Base64-encoded image data.

  - `required string MediaType`

    MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

  - `required Type Type`

    - `"base64"Base64`

### Beta Managed Agents Billing Error

- `class BetaManagedAgentsBillingError:`

  The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

  - `required string Message`

    Human-readable error description.

  - `required RetryStatus RetryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying:`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `required Type Type`

        - `"retrying"Retrying`

    - `class BetaManagedAgentsRetryStatusExhausted:`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `required Type Type`

        - `"exhausted"Exhausted`

    - `class BetaManagedAgentsRetryStatusTerminal:`

      The session encountered a terminal error and will transition to `terminated` state.

      - `required Type Type`

        - `"terminal"Terminal`

  - `required Type Type`

    - `"billing_error"BillingError`

### Beta Managed Agents Document Block

- `class BetaManagedAgentsDocumentBlock:`

  Document content, either specified directly as base64 data, as text, or as a reference via a URL.

  - `required Source Source`

    Union type for document source variants.

    - `class BetaManagedAgentsBase64DocumentSource:`

      Base64-encoded document data.

      - `required string Data`

        Base64-encoded document data.

      - `required string MediaType`

        MIME type of the document (e.g., "application/pdf").

      - `required Type Type`

        - `"base64"Base64`

    - `class BetaManagedAgentsPlainTextDocumentSource:`

      Plain text document content.

      - `required string Data`

        The plain text content.

      - `required MediaType MediaType`

        MIME type of the text content. Must be "text/plain".

        - `"text/plain"TextPlain`

      - `required Type Type`

        - `"text"Text`

    - `class BetaManagedAgentsUrlDocumentSource:`

      Document referenced by URL.

      - `required Type Type`

        - `"url"Url`

      - `required string Url`

        URL of the document to fetch.

    - `class BetaManagedAgentsFileDocumentSource:`

      Document referenced by file ID.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

        - `"file"File`

  - `required Type Type`

    - `"document"Document`

  - `string? Context`

    Additional context about the document for the model.

  - `string? Title`

    The title of the document.

### Beta Managed Agents Event Params

- `class BetaManagedAgentsEventParams: A class that can be one of several variants.union`

  Union type for event parameters that can be sent to a session.

  - `class BetaManagedAgentsUserMessageEventParams:`

    Parameters for sending a user message to the session.

    - `required IReadOnlyList<Content> Content`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"image"Image`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"TextPlain`

            - `required Type Type`

              - `"text"Text`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"document"Document`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

    - `required Type Type`

      - `"user.message"UserMessage`

  - `class BetaManagedAgentsUserInterruptEventParams:`

    Parameters for sending an interrupt to pause the agent.

    - `required Type Type`

      - `"user.interrupt"UserInterrupt`

  - `class BetaManagedAgentsUserToolConfirmationEventParams:`

    Parameters for confirming or denying a tool execution request.

    - `required Result Result`

      UserToolConfirmationResult enum

      - `"allow"Allow`

      - `"deny"Deny`

    - `required string ToolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

      - `"user.tool_confirmation"UserToolConfirmation`

    - `string? DenyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

  - `class BetaManagedAgentsUserCustomToolResultEventParams:`

    Parameters for providing the result of a custom tool execution.

    - `required string CustomToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

      - `"user.custom_tool_result"UserCustomToolResult`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"image"Image`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"TextPlain`

            - `required Type Type`

              - `"text"Text`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"document"Document`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

    - `Boolean? IsError`

      Whether the tool execution resulted in an error.

### Beta Managed Agents File Document Source

- `class BetaManagedAgentsFileDocumentSource:`

  Document referenced by file ID.

  - `required string FileID`

    ID of a previously uploaded file.

  - `required Type Type`

    - `"file"File`

### Beta Managed Agents File Image Source

- `class BetaManagedAgentsFileImageSource:`

  Image referenced by file ID.

  - `required string FileID`

    ID of a previously uploaded file.

  - `required Type Type`

    - `"file"File`

### Beta Managed Agents Image Block

- `class BetaManagedAgentsImageBlock:`

  Image content specified directly as base64 data or as a reference via a URL.

  - `required Source Source`

    Union type for image source variants.

    - `class BetaManagedAgentsBase64ImageSource:`

      Base64-encoded image data.

      - `required string Data`

        Base64-encoded image data.

      - `required string MediaType`

        MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

      - `required Type Type`

        - `"base64"Base64`

    - `class BetaManagedAgentsUrlImageSource:`

      Image referenced by URL.

      - `required Type Type`

        - `"url"Url`

      - `required string Url`

        URL of the image to fetch.

    - `class BetaManagedAgentsFileImageSource:`

      Image referenced by file ID.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

        - `"file"File`

  - `required Type Type`

    - `"image"Image`

### Beta Managed Agents MCP Authentication Failed Error

- `class BetaManagedAgentsMcpAuthenticationFailedError:`

  Authentication to an MCP server failed.

  - `required string McpServerName`

    Name of the MCP server that failed authentication.

  - `required string Message`

    Human-readable error description.

  - `required RetryStatus RetryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying:`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `required Type Type`

        - `"retrying"Retrying`

    - `class BetaManagedAgentsRetryStatusExhausted:`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `required Type Type`

        - `"exhausted"Exhausted`

    - `class BetaManagedAgentsRetryStatusTerminal:`

      The session encountered a terminal error and will transition to `terminated` state.

      - `required Type Type`

        - `"terminal"Terminal`

  - `required Type Type`

    - `"mcp_authentication_failed_error"McpAuthenticationFailedError`

### Beta Managed Agents MCP Connection Failed Error

- `class BetaManagedAgentsMcpConnectionFailedError:`

  Failed to connect to an MCP server.

  - `required string McpServerName`

    Name of the MCP server that failed to connect.

  - `required string Message`

    Human-readable error description.

  - `required RetryStatus RetryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying:`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `required Type Type`

        - `"retrying"Retrying`

    - `class BetaManagedAgentsRetryStatusExhausted:`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `required Type Type`

        - `"exhausted"Exhausted`

    - `class BetaManagedAgentsRetryStatusTerminal:`

      The session encountered a terminal error and will transition to `terminated` state.

      - `required Type Type`

        - `"terminal"Terminal`

  - `required Type Type`

    - `"mcp_connection_failed_error"McpConnectionFailedError`

### Beta Managed Agents Model Overloaded Error

- `class BetaManagedAgentsModelOverloadedError:`

  The model is currently overloaded. Emitted after automatic retries are exhausted.

  - `required string Message`

    Human-readable error description.

  - `required RetryStatus RetryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying:`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `required Type Type`

        - `"retrying"Retrying`

    - `class BetaManagedAgentsRetryStatusExhausted:`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `required Type Type`

        - `"exhausted"Exhausted`

    - `class BetaManagedAgentsRetryStatusTerminal:`

      The session encountered a terminal error and will transition to `terminated` state.

      - `required Type Type`

        - `"terminal"Terminal`

  - `required Type Type`

    - `"model_overloaded_error"ModelOverloadedError`

### Beta Managed Agents Model Rate Limited Error

- `class BetaManagedAgentsModelRateLimitedError:`

  The model request was rate-limited.

  - `required string Message`

    Human-readable error description.

  - `required RetryStatus RetryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying:`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `required Type Type`

        - `"retrying"Retrying`

    - `class BetaManagedAgentsRetryStatusExhausted:`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `required Type Type`

        - `"exhausted"Exhausted`

    - `class BetaManagedAgentsRetryStatusTerminal:`

      The session encountered a terminal error and will transition to `terminated` state.

      - `required Type Type`

        - `"terminal"Terminal`

  - `required Type Type`

    - `"model_rate_limited_error"ModelRateLimitedError`

### Beta Managed Agents Model Request Failed Error

- `class BetaManagedAgentsModelRequestFailedError:`

  A model request failed for a reason other than overload or rate-limiting.

  - `required string Message`

    Human-readable error description.

  - `required RetryStatus RetryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying:`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `required Type Type`

        - `"retrying"Retrying`

    - `class BetaManagedAgentsRetryStatusExhausted:`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `required Type Type`

        - `"exhausted"Exhausted`

    - `class BetaManagedAgentsRetryStatusTerminal:`

      The session encountered a terminal error and will transition to `terminated` state.

      - `required Type Type`

        - `"terminal"Terminal`

  - `required Type Type`

    - `"model_request_failed_error"ModelRequestFailedError`

### Beta Managed Agents Plain Text Document Source

- `class BetaManagedAgentsPlainTextDocumentSource:`

  Plain text document content.

  - `required string Data`

    The plain text content.

  - `required MediaType MediaType`

    MIME type of the text content. Must be "text/plain".

    - `"text/plain"TextPlain`

  - `required Type Type`

    - `"text"Text`

### Beta Managed Agents Retry Status Exhausted

- `class BetaManagedAgentsRetryStatusExhausted:`

  This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

  - `required Type Type`

    - `"exhausted"Exhausted`

### Beta Managed Agents Retry Status Retrying

- `class BetaManagedAgentsRetryStatusRetrying:`

  The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

  - `required Type Type`

    - `"retrying"Retrying`

### Beta Managed Agents Retry Status Terminal

- `class BetaManagedAgentsRetryStatusTerminal:`

  The session encountered a terminal error and will transition to `terminated` state.

  - `required Type Type`

    - `"terminal"Terminal`

### Beta Managed Agents Send Session Events

- `class BetaManagedAgentsSendSessionEvents:`

  Events that were successfully sent to the session.

  - `IReadOnlyList<Data> Data`

    Sent events

    - `class BetaManagedAgentsUserMessageEvent:`

      A user message event in the session conversation.

      - `required string ID`

        Unique identifier for this event.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks comprising the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

      - `required Type Type`

        - `"user.message"UserMessage`

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserInterruptEvent:`

      An interrupt event that pauses agent execution and returns control to the user.

      - `required string ID`

        Unique identifier for this event.

      - `required Type Type`

        - `"user.interrupt"UserInterrupt`

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserToolConfirmationEvent:`

      A tool confirmation event that approves or denies a pending tool execution.

      - `required string ID`

        Unique identifier for this event.

      - `required Result Result`

        UserToolConfirmationResult enum

        - `"allow"Allow`

        - `"deny"Deny`

      - `required string ToolUseID`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `required Type Type`

        - `"user.tool_confirmation"UserToolConfirmation`

      - `string? DenyMessage`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserCustomToolResultEvent:`

      Event sent by the client providing the result of a custom tool execution.

      - `required string ID`

        Unique identifier for this event.

      - `required string CustomToolUseID`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `required Type Type`

        - `"user.custom_tool_result"UserCustomToolResult`

      - `IReadOnlyList<Content> Content`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"image"Image`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

              - `required Type Type`

                - `"base64"Base64`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"TextPlain`

              - `required Type Type`

                - `"text"Text`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

                - `"url"Url`

              - `required string Url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

              - `required Type Type`

                - `"file"File`

          - `required Type Type`

            - `"document"Document`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

      - `Boolean? IsError`

        Whether the tool execution resulted in an error.

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

### Beta Managed Agents Session Deleted Event

- `class BetaManagedAgentsSessionDeletedEvent:`

  Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

  - `required string ID`

    Unique identifier for this event.

  - `required DateTimeOffset ProcessedAt`

    A timestamp in RFC 3339 format

  - `required Type Type`

    - `"session.deleted"SessionDeleted`

### Beta Managed Agents Session End Turn

- `class BetaManagedAgentsSessionEndTurn:`

  The agent completed its turn naturally and is ready for the next user message.

  - `required Type Type`

    - `"end_turn"EndTurn`

### Beta Managed Agents Session Error Event

- `class BetaManagedAgentsSessionErrorEvent:`

  An error event indicating a problem occurred during session execution.

  - `required string ID`

    Unique identifier for this event.

  - `required Error Error`

    An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

    - `class BetaManagedAgentsUnknownError:`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `required string Message`

        Human-readable error description.

      - `required RetryStatus RetryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying:`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `required Type Type`

            - `"retrying"Retrying`

        - `class BetaManagedAgentsRetryStatusExhausted:`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `required Type Type`

            - `"exhausted"Exhausted`

        - `class BetaManagedAgentsRetryStatusTerminal:`

          The session encountered a terminal error and will transition to `terminated` state.

          - `required Type Type`

            - `"terminal"Terminal`

      - `required Type Type`

        - `"unknown_error"UnknownError`

    - `class BetaManagedAgentsModelOverloadedError:`

      The model is currently overloaded. Emitted after automatic retries are exhausted.

      - `required string Message`

        Human-readable error description.

      - `required RetryStatus RetryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying:`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `required Type Type`

            - `"retrying"Retrying`

        - `class BetaManagedAgentsRetryStatusExhausted:`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `required Type Type`

            - `"exhausted"Exhausted`

        - `class BetaManagedAgentsRetryStatusTerminal:`

          The session encountered a terminal error and will transition to `terminated` state.

          - `required Type Type`

            - `"terminal"Terminal`

      - `required Type Type`

        - `"model_overloaded_error"ModelOverloadedError`

    - `class BetaManagedAgentsModelRateLimitedError:`

      The model request was rate-limited.

      - `required string Message`

        Human-readable error description.

      - `required RetryStatus RetryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying:`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `required Type Type`

            - `"retrying"Retrying`

        - `class BetaManagedAgentsRetryStatusExhausted:`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `required Type Type`

            - `"exhausted"Exhausted`

        - `class BetaManagedAgentsRetryStatusTerminal:`

          The session encountered a terminal error and will transition to `terminated` state.

          - `required Type Type`

            - `"terminal"Terminal`

      - `required Type Type`

        - `"model_rate_limited_error"ModelRateLimitedError`

    - `class BetaManagedAgentsModelRequestFailedError:`

      A model request failed for a reason other than overload or rate-limiting.

      - `required string Message`

        Human-readable error description.

      - `required RetryStatus RetryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying:`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `required Type Type`

            - `"retrying"Retrying`

        - `class BetaManagedAgentsRetryStatusExhausted:`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `required Type Type`

            - `"exhausted"Exhausted`

        - `class BetaManagedAgentsRetryStatusTerminal:`

          The session encountered a terminal error and will transition to `terminated` state.

          - `required Type Type`

            - `"terminal"Terminal`

      - `required Type Type`

        - `"model_request_failed_error"ModelRequestFailedError`

    - `class BetaManagedAgentsMcpConnectionFailedError:`

      Failed to connect to an MCP server.

      - `required string McpServerName`

        Name of the MCP server that failed to connect.

      - `required string Message`

        Human-readable error description.

      - `required RetryStatus RetryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying:`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `required Type Type`

            - `"retrying"Retrying`

        - `class BetaManagedAgentsRetryStatusExhausted:`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `required Type Type`

            - `"exhausted"Exhausted`

        - `class BetaManagedAgentsRetryStatusTerminal:`

          The session encountered a terminal error and will transition to `terminated` state.

          - `required Type Type`

            - `"terminal"Terminal`

      - `required Type Type`

        - `"mcp_connection_failed_error"McpConnectionFailedError`

    - `class BetaManagedAgentsMcpAuthenticationFailedError:`

      Authentication to an MCP server failed.

      - `required string McpServerName`

        Name of the MCP server that failed authentication.

      - `required string Message`

        Human-readable error description.

      - `required RetryStatus RetryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying:`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `required Type Type`

            - `"retrying"Retrying`

        - `class BetaManagedAgentsRetryStatusExhausted:`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `required Type Type`

            - `"exhausted"Exhausted`

        - `class BetaManagedAgentsRetryStatusTerminal:`

          The session encountered a terminal error and will transition to `terminated` state.

          - `required Type Type`

            - `"terminal"Terminal`

      - `required Type Type`

        - `"mcp_authentication_failed_error"McpAuthenticationFailedError`

    - `class BetaManagedAgentsBillingError:`

      The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

      - `required string Message`

        Human-readable error description.

      - `required RetryStatus RetryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying:`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `required Type Type`

            - `"retrying"Retrying`

        - `class BetaManagedAgentsRetryStatusExhausted:`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `required Type Type`

            - `"exhausted"Exhausted`

        - `class BetaManagedAgentsRetryStatusTerminal:`

          The session encountered a terminal error and will transition to `terminated` state.

          - `required Type Type`

            - `"terminal"Terminal`

      - `required Type Type`

        - `"billing_error"BillingError`

  - `required DateTimeOffset ProcessedAt`

    A timestamp in RFC 3339 format

  - `required Type Type`

    - `"session.error"SessionError`

### Beta Managed Agents Session Event

- `class BetaManagedAgentsSessionEvent: A class that can be one of several variants.union`

  Union type for all event types in a session.

  - `class BetaManagedAgentsUserMessageEvent:`

    A user message event in the session conversation.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"image"Image`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"TextPlain`

            - `required Type Type`

              - `"text"Text`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"document"Document`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

    - `required Type Type`

      - `"user.message"UserMessage`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent:`

    An interrupt event that pauses agent execution and returns control to the user.

    - `required string ID`

      Unique identifier for this event.

    - `required Type Type`

      - `"user.interrupt"UserInterrupt`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserToolConfirmationEvent:`

    A tool confirmation event that approves or denies a pending tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required Result Result`

      UserToolConfirmationResult enum

      - `"allow"Allow`

      - `"deny"Deny`

    - `required string ToolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

      - `"user.tool_confirmation"UserToolConfirmation`

    - `string? DenyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserCustomToolResultEvent:`

    Event sent by the client providing the result of a custom tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required string CustomToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

      - `"user.custom_tool_result"UserCustomToolResult`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"image"Image`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"TextPlain`

            - `required Type Type`

              - `"text"Text`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"document"Document`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

    - `Boolean? IsError`

      Whether the tool execution resulted in an error.

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsAgentCustomToolUseEvent:`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string Name`

      Name of the custom tool being called.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.custom_tool_use"AgentCustomToolUse`

  - `class BetaManagedAgentsAgentMessageEvent:`

    An agent response event in the session conversation.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<BetaManagedAgentsTextBlock> Content`

      Array of text blocks comprising the agent response.

      - `required string Text`

        The text content.

      - `required Type Type`

        - `"text"Text`

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.message"AgentMessage`

  - `class BetaManagedAgentsAgentThinkingEvent:`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.thinking"AgentThinking`

  - `class BetaManagedAgentsAgentMcpToolUseEvent:`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string McpServerName`

      Name of the MCP server providing the tool.

    - `required string Name`

      Name of the MCP tool being used.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.mcp_tool_use"AgentMcpToolUse`

    - `EvaluatedPermission EvaluatedPermission`

      AgentEvaluatedPermission enum

      - `"allow"Allow`

      - `"ask"Ask`

      - `"deny"Deny`

  - `class BetaManagedAgentsAgentMcpToolResultEvent:`

    Event representing the result of an MCP tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required string McpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.mcp_tool_result"AgentMcpToolResult`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"image"Image`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"TextPlain`

            - `required Type Type`

              - `"text"Text`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"document"Document`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

    - `Boolean? IsError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent:`

    Event emitted when the agent invokes a built-in agent tool.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string Name`

      Name of the agent tool being used.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.tool_use"AgentToolUse`

    - `EvaluatedPermission EvaluatedPermission`

      AgentEvaluatedPermission enum

      - `"allow"Allow`

      - `"ask"Ask`

      - `"deny"Deny`

  - `class BetaManagedAgentsAgentToolResultEvent:`

    Event representing the result of an agent tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string ToolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `required Type Type`

      - `"agent.tool_result"AgentToolResult`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"image"Image`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"TextPlain`

            - `required Type Type`

              - `"text"Text`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"document"Document`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

    - `Boolean? IsError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

    Indicates that context compaction (summarization) occurred during the session.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.thread_context_compacted"AgentThreadContextCompacted`

  - `class BetaManagedAgentsSessionErrorEvent:`

    An error event indicating a problem occurred during session execution.

    - `required string ID`

      Unique identifier for this event.

    - `required Error Error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError:`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"unknown_error"UnknownError`

      - `class BetaManagedAgentsModelOverloadedError:`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"model_overloaded_error"ModelOverloadedError`

      - `class BetaManagedAgentsModelRateLimitedError:`

        The model request was rate-limited.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"model_rate_limited_error"ModelRateLimitedError`

      - `class BetaManagedAgentsModelRequestFailedError:`

        A model request failed for a reason other than overload or rate-limiting.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"model_request_failed_error"ModelRequestFailedError`

      - `class BetaManagedAgentsMcpConnectionFailedError:`

        Failed to connect to an MCP server.

        - `required string McpServerName`

          Name of the MCP server that failed to connect.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"mcp_connection_failed_error"McpConnectionFailedError`

      - `class BetaManagedAgentsMcpAuthenticationFailedError:`

        Authentication to an MCP server failed.

        - `required string McpServerName`

          Name of the MCP server that failed authentication.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"mcp_authentication_failed_error"McpAuthenticationFailedError`

      - `class BetaManagedAgentsBillingError:`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"billing_error"BillingError`

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.error"SessionError`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.status_rescheduled"SessionStatusRescheduled`

  - `class BetaManagedAgentsSessionStatusRunningEvent:`

    Indicates the session is actively running and the agent is working.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.status_running"SessionStatusRunning`

  - `class BetaManagedAgentsSessionStatusIdleEvent:`

    Indicates the agent has paused and is awaiting user input.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required StopReason StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `required Type Type`

          - `"end_turn"EndTurn`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `required IReadOnlyList<string> EventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `required Type Type`

          - `"requires_action"RequiresAction`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `required Type Type`

          - `"retries_exhausted"RetriesExhausted`

    - `required Type Type`

      - `"session.status_idle"SessionStatusIdle`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

    Indicates the session has terminated, either due to an error or completion.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.status_terminated"SessionStatusTerminated`

  - `class BetaManagedAgentsSpanModelRequestStartEvent:`

    Emitted when a model request is initiated by the agent.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"span.model_request_start"SpanModelRequestStart`

  - `class BetaManagedAgentsSpanModelRequestEndEvent:`

    Emitted when a model request completes.

    - `required string ID`

      Unique identifier for this event.

    - `required Boolean? IsError`

      Whether the model request resulted in an error.

    - `required string ModelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `required BetaManagedAgentsSpanModelUsage ModelUsage`

      Token usage for a single model request.

      - `required Int CacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

      - `required Int CacheReadInputTokens`

        Tokens read from prompt cache in this request.

      - `required Int InputTokens`

        Input tokens consumed by this request.

      - `required Int OutputTokens`

        Output tokens generated by this request.

      - `Speed? Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"Standard`

        - `"fast"Fast`

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"span.model_request_end"SpanModelRequestEnd`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.deleted"SessionDeleted`

### Beta Managed Agents Session Requires Action

- `class BetaManagedAgentsSessionRequiresAction:`

  The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

  - `required IReadOnlyList<string> EventIds`

    The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

  - `required Type Type`

    - `"requires_action"RequiresAction`

### Beta Managed Agents Session Retries Exhausted

- `class BetaManagedAgentsSessionRetriesExhausted:`

  The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

  - `required Type Type`

    - `"retries_exhausted"RetriesExhausted`

### Beta Managed Agents Session Status Idle Event

- `class BetaManagedAgentsSessionStatusIdleEvent:`

  Indicates the agent has paused and is awaiting user input.

  - `required string ID`

    Unique identifier for this event.

  - `required DateTimeOffset ProcessedAt`

    A timestamp in RFC 3339 format

  - `required StopReason StopReason`

    The agent completed its turn naturally and is ready for the next user message.

    - `class BetaManagedAgentsSessionEndTurn:`

      The agent completed its turn naturally and is ready for the next user message.

      - `required Type Type`

        - `"end_turn"EndTurn`

    - `class BetaManagedAgentsSessionRequiresAction:`

      The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `required IReadOnlyList<string> EventIds`

        The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

      - `required Type Type`

        - `"requires_action"RequiresAction`

    - `class BetaManagedAgentsSessionRetriesExhausted:`

      The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

      - `required Type Type`

        - `"retries_exhausted"RetriesExhausted`

  - `required Type Type`

    - `"session.status_idle"SessionStatusIdle`

### Beta Managed Agents Session Status Rescheduled Event

- `class BetaManagedAgentsSessionStatusRescheduledEvent:`

  Indicates the session is recovering from an error state and is rescheduled for execution.

  - `required string ID`

    Unique identifier for this event.

  - `required DateTimeOffset ProcessedAt`

    A timestamp in RFC 3339 format

  - `required Type Type`

    - `"session.status_rescheduled"SessionStatusRescheduled`

### Beta Managed Agents Session Status Running Event

- `class BetaManagedAgentsSessionStatusRunningEvent:`

  Indicates the session is actively running and the agent is working.

  - `required string ID`

    Unique identifier for this event.

  - `required DateTimeOffset ProcessedAt`

    A timestamp in RFC 3339 format

  - `required Type Type`

    - `"session.status_running"SessionStatusRunning`

### Beta Managed Agents Session Status Terminated Event

- `class BetaManagedAgentsSessionStatusTerminatedEvent:`

  Indicates the session has terminated, either due to an error or completion.

  - `required string ID`

    Unique identifier for this event.

  - `required DateTimeOffset ProcessedAt`

    A timestamp in RFC 3339 format

  - `required Type Type`

    - `"session.status_terminated"SessionStatusTerminated`

### Beta Managed Agents Span Model Request End Event

- `class BetaManagedAgentsSpanModelRequestEndEvent:`

  Emitted when a model request completes.

  - `required string ID`

    Unique identifier for this event.

  - `required Boolean? IsError`

    Whether the model request resulted in an error.

  - `required string ModelRequestStartID`

    The id of the corresponding `span.model_request_start` event.

  - `required BetaManagedAgentsSpanModelUsage ModelUsage`

    Token usage for a single model request.

    - `required Int CacheCreationInputTokens`

      Tokens used to create prompt cache in this request.

    - `required Int CacheReadInputTokens`

      Tokens read from prompt cache in this request.

    - `required Int InputTokens`

      Input tokens consumed by this request.

    - `required Int OutputTokens`

      Output tokens generated by this request.

    - `Speed? Speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"Standard`

      - `"fast"Fast`

  - `required DateTimeOffset ProcessedAt`

    A timestamp in RFC 3339 format

  - `required Type Type`

    - `"span.model_request_end"SpanModelRequestEnd`

### Beta Managed Agents Span Model Request Start Event

- `class BetaManagedAgentsSpanModelRequestStartEvent:`

  Emitted when a model request is initiated by the agent.

  - `required string ID`

    Unique identifier for this event.

  - `required DateTimeOffset ProcessedAt`

    A timestamp in RFC 3339 format

  - `required Type Type`

    - `"span.model_request_start"SpanModelRequestStart`

### Beta Managed Agents Span Model Usage

- `class BetaManagedAgentsSpanModelUsage:`

  Token usage for a single model request.

  - `required Int CacheCreationInputTokens`

    Tokens used to create prompt cache in this request.

  - `required Int CacheReadInputTokens`

    Tokens read from prompt cache in this request.

  - `required Int InputTokens`

    Input tokens consumed by this request.

  - `required Int OutputTokens`

    Output tokens generated by this request.

  - `Speed? Speed`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"Standard`

    - `"fast"Fast`

### Beta Managed Agents Stream Session Events

- `class BetaManagedAgentsStreamSessionEvents: A class that can be one of several variants.union`

  Server-sent event in the session stream.

  - `class BetaManagedAgentsUserMessageEvent:`

    A user message event in the session conversation.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"image"Image`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"TextPlain`

            - `required Type Type`

              - `"text"Text`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"document"Document`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

    - `required Type Type`

      - `"user.message"UserMessage`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent:`

    An interrupt event that pauses agent execution and returns control to the user.

    - `required string ID`

      Unique identifier for this event.

    - `required Type Type`

      - `"user.interrupt"UserInterrupt`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserToolConfirmationEvent:`

    A tool confirmation event that approves or denies a pending tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required Result Result`

      UserToolConfirmationResult enum

      - `"allow"Allow`

      - `"deny"Deny`

    - `required string ToolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

      - `"user.tool_confirmation"UserToolConfirmation`

    - `string? DenyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserCustomToolResultEvent:`

    Event sent by the client providing the result of a custom tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required string CustomToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

      - `"user.custom_tool_result"UserCustomToolResult`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"image"Image`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"TextPlain`

            - `required Type Type`

              - `"text"Text`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"document"Document`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

    - `Boolean? IsError`

      Whether the tool execution resulted in an error.

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsAgentCustomToolUseEvent:`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string Name`

      Name of the custom tool being called.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.custom_tool_use"AgentCustomToolUse`

  - `class BetaManagedAgentsAgentMessageEvent:`

    An agent response event in the session conversation.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<BetaManagedAgentsTextBlock> Content`

      Array of text blocks comprising the agent response.

      - `required string Text`

        The text content.

      - `required Type Type`

        - `"text"Text`

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.message"AgentMessage`

  - `class BetaManagedAgentsAgentThinkingEvent:`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.thinking"AgentThinking`

  - `class BetaManagedAgentsAgentMcpToolUseEvent:`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string McpServerName`

      Name of the MCP server providing the tool.

    - `required string Name`

      Name of the MCP tool being used.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.mcp_tool_use"AgentMcpToolUse`

    - `EvaluatedPermission EvaluatedPermission`

      AgentEvaluatedPermission enum

      - `"allow"Allow`

      - `"ask"Ask`

      - `"deny"Deny`

  - `class BetaManagedAgentsAgentMcpToolResultEvent:`

    Event representing the result of an MCP tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required string McpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.mcp_tool_result"AgentMcpToolResult`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"image"Image`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"TextPlain`

            - `required Type Type`

              - `"text"Text`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"document"Document`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

    - `Boolean? IsError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent:`

    Event emitted when the agent invokes a built-in agent tool.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string Name`

      Name of the agent tool being used.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.tool_use"AgentToolUse`

    - `EvaluatedPermission EvaluatedPermission`

      AgentEvaluatedPermission enum

      - `"allow"Allow`

      - `"ask"Ask`

      - `"deny"Deny`

  - `class BetaManagedAgentsAgentToolResultEvent:`

    Event representing the result of an agent tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string ToolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `required Type Type`

      - `"agent.tool_result"AgentToolResult`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"image"Image`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"TextPlain`

            - `required Type Type`

              - `"text"Text`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"document"Document`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

    - `Boolean? IsError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

    Indicates that context compaction (summarization) occurred during the session.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.thread_context_compacted"AgentThreadContextCompacted`

  - `class BetaManagedAgentsSessionErrorEvent:`

    An error event indicating a problem occurred during session execution.

    - `required string ID`

      Unique identifier for this event.

    - `required Error Error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError:`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"unknown_error"UnknownError`

      - `class BetaManagedAgentsModelOverloadedError:`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"model_overloaded_error"ModelOverloadedError`

      - `class BetaManagedAgentsModelRateLimitedError:`

        The model request was rate-limited.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"model_rate_limited_error"ModelRateLimitedError`

      - `class BetaManagedAgentsModelRequestFailedError:`

        A model request failed for a reason other than overload or rate-limiting.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"model_request_failed_error"ModelRequestFailedError`

      - `class BetaManagedAgentsMcpConnectionFailedError:`

        Failed to connect to an MCP server.

        - `required string McpServerName`

          Name of the MCP server that failed to connect.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"mcp_connection_failed_error"McpConnectionFailedError`

      - `class BetaManagedAgentsMcpAuthenticationFailedError:`

        Authentication to an MCP server failed.

        - `required string McpServerName`

          Name of the MCP server that failed authentication.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"mcp_authentication_failed_error"McpAuthenticationFailedError`

      - `class BetaManagedAgentsBillingError:`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"billing_error"BillingError`

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.error"SessionError`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.status_rescheduled"SessionStatusRescheduled`

  - `class BetaManagedAgentsSessionStatusRunningEvent:`

    Indicates the session is actively running and the agent is working.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.status_running"SessionStatusRunning`

  - `class BetaManagedAgentsSessionStatusIdleEvent:`

    Indicates the agent has paused and is awaiting user input.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required StopReason StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `required Type Type`

          - `"end_turn"EndTurn`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `required IReadOnlyList<string> EventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `required Type Type`

          - `"requires_action"RequiresAction`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `required Type Type`

          - `"retries_exhausted"RetriesExhausted`

    - `required Type Type`

      - `"session.status_idle"SessionStatusIdle`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

    Indicates the session has terminated, either due to an error or completion.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.status_terminated"SessionStatusTerminated`

  - `class BetaManagedAgentsSpanModelRequestStartEvent:`

    Emitted when a model request is initiated by the agent.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"span.model_request_start"SpanModelRequestStart`

  - `class BetaManagedAgentsSpanModelRequestEndEvent:`

    Emitted when a model request completes.

    - `required string ID`

      Unique identifier for this event.

    - `required Boolean? IsError`

      Whether the model request resulted in an error.

    - `required string ModelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `required BetaManagedAgentsSpanModelUsage ModelUsage`

      Token usage for a single model request.

      - `required Int CacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

      - `required Int CacheReadInputTokens`

        Tokens read from prompt cache in this request.

      - `required Int InputTokens`

        Input tokens consumed by this request.

      - `required Int OutputTokens`

        Output tokens generated by this request.

      - `Speed? Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"Standard`

        - `"fast"Fast`

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"span.model_request_end"SpanModelRequestEnd`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.deleted"SessionDeleted`

### Beta Managed Agents Text Block

- `class BetaManagedAgentsTextBlock:`

  Regular text content.

  - `required string Text`

    The text content.

  - `required Type Type`

    - `"text"Text`

### Beta Managed Agents Unknown Error

- `class BetaManagedAgentsUnknownError:`

  An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

  - `required string Message`

    Human-readable error description.

  - `required RetryStatus RetryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying:`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `required Type Type`

        - `"retrying"Retrying`

    - `class BetaManagedAgentsRetryStatusExhausted:`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `required Type Type`

        - `"exhausted"Exhausted`

    - `class BetaManagedAgentsRetryStatusTerminal:`

      The session encountered a terminal error and will transition to `terminated` state.

      - `required Type Type`

        - `"terminal"Terminal`

  - `required Type Type`

    - `"unknown_error"UnknownError`

### Beta Managed Agents URL Document Source

- `class BetaManagedAgentsUrlDocumentSource:`

  Document referenced by URL.

  - `required Type Type`

    - `"url"Url`

  - `required string Url`

    URL of the document to fetch.

### Beta Managed Agents URL Image Source

- `class BetaManagedAgentsUrlImageSource:`

  Image referenced by URL.

  - `required Type Type`

    - `"url"Url`

  - `required string Url`

    URL of the image to fetch.

### Beta Managed Agents User Custom Tool Result Event

- `class BetaManagedAgentsUserCustomToolResultEvent:`

  Event sent by the client providing the result of a custom tool execution.

  - `required string ID`

    Unique identifier for this event.

  - `required string CustomToolUseID`

    The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `required Type Type`

    - `"user.custom_tool_result"UserCustomToolResult`

  - `IReadOnlyList<Content> Content`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock:`

      Regular text content.

      - `required string Text`

        The text content.

      - `required Type Type`

        - `"text"Text`

    - `class BetaManagedAgentsImageBlock:`

      Image content specified directly as base64 data or as a reference via a URL.

      - `required Source Source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource:`

          Base64-encoded image data.

          - `required string Data`

            Base64-encoded image data.

          - `required string MediaType`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `required Type Type`

            - `"base64"Base64`

        - `class BetaManagedAgentsUrlImageSource:`

          Image referenced by URL.

          - `required Type Type`

            - `"url"Url`

          - `required string Url`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource:`

          Image referenced by file ID.

          - `required string FileID`

            ID of a previously uploaded file.

          - `required Type Type`

            - `"file"File`

      - `required Type Type`

        - `"image"Image`

    - `class BetaManagedAgentsDocumentBlock:`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `required Source Source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource:`

          Base64-encoded document data.

          - `required string Data`

            Base64-encoded document data.

          - `required string MediaType`

            MIME type of the document (e.g., "application/pdf").

          - `required Type Type`

            - `"base64"Base64`

        - `class BetaManagedAgentsPlainTextDocumentSource:`

          Plain text document content.

          - `required string Data`

            The plain text content.

          - `required MediaType MediaType`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"TextPlain`

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsUrlDocumentSource:`

          Document referenced by URL.

          - `required Type Type`

            - `"url"Url`

          - `required string Url`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource:`

          Document referenced by file ID.

          - `required string FileID`

            ID of a previously uploaded file.

          - `required Type Type`

            - `"file"File`

      - `required Type Type`

        - `"document"Document`

      - `string? Context`

        Additional context about the document for the model.

      - `string? Title`

        The title of the document.

  - `Boolean? IsError`

    Whether the tool execution resulted in an error.

  - `DateTimeOffset? ProcessedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Custom Tool Result Event Params

- `class BetaManagedAgentsUserCustomToolResultEventParams:`

  Parameters for providing the result of a custom tool execution.

  - `required string CustomToolUseID`

    The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `required Type Type`

    - `"user.custom_tool_result"UserCustomToolResult`

  - `IReadOnlyList<Content> Content`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock:`

      Regular text content.

      - `required string Text`

        The text content.

      - `required Type Type`

        - `"text"Text`

    - `class BetaManagedAgentsImageBlock:`

      Image content specified directly as base64 data or as a reference via a URL.

      - `required Source Source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource:`

          Base64-encoded image data.

          - `required string Data`

            Base64-encoded image data.

          - `required string MediaType`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `required Type Type`

            - `"base64"Base64`

        - `class BetaManagedAgentsUrlImageSource:`

          Image referenced by URL.

          - `required Type Type`

            - `"url"Url`

          - `required string Url`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource:`

          Image referenced by file ID.

          - `required string FileID`

            ID of a previously uploaded file.

          - `required Type Type`

            - `"file"File`

      - `required Type Type`

        - `"image"Image`

    - `class BetaManagedAgentsDocumentBlock:`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `required Source Source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource:`

          Base64-encoded document data.

          - `required string Data`

            Base64-encoded document data.

          - `required string MediaType`

            MIME type of the document (e.g., "application/pdf").

          - `required Type Type`

            - `"base64"Base64`

        - `class BetaManagedAgentsPlainTextDocumentSource:`

          Plain text document content.

          - `required string Data`

            The plain text content.

          - `required MediaType MediaType`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"TextPlain`

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsUrlDocumentSource:`

          Document referenced by URL.

          - `required Type Type`

            - `"url"Url`

          - `required string Url`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource:`

          Document referenced by file ID.

          - `required string FileID`

            ID of a previously uploaded file.

          - `required Type Type`

            - `"file"File`

      - `required Type Type`

        - `"document"Document`

      - `string? Context`

        Additional context about the document for the model.

      - `string? Title`

        The title of the document.

  - `Boolean? IsError`

    Whether the tool execution resulted in an error.

### Beta Managed Agents User Interrupt Event

- `class BetaManagedAgentsUserInterruptEvent:`

  An interrupt event that pauses agent execution and returns control to the user.

  - `required string ID`

    Unique identifier for this event.

  - `required Type Type`

    - `"user.interrupt"UserInterrupt`

  - `DateTimeOffset? ProcessedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Interrupt Event Params

- `class BetaManagedAgentsUserInterruptEventParams:`

  Parameters for sending an interrupt to pause the agent.

  - `required Type Type`

    - `"user.interrupt"UserInterrupt`

### Beta Managed Agents User Message Event

- `class BetaManagedAgentsUserMessageEvent:`

  A user message event in the session conversation.

  - `required string ID`

    Unique identifier for this event.

  - `required IReadOnlyList<Content> Content`

    Array of content blocks comprising the user message.

    - `class BetaManagedAgentsTextBlock:`

      Regular text content.

      - `required string Text`

        The text content.

      - `required Type Type`

        - `"text"Text`

    - `class BetaManagedAgentsImageBlock:`

      Image content specified directly as base64 data or as a reference via a URL.

      - `required Source Source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource:`

          Base64-encoded image data.

          - `required string Data`

            Base64-encoded image data.

          - `required string MediaType`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `required Type Type`

            - `"base64"Base64`

        - `class BetaManagedAgentsUrlImageSource:`

          Image referenced by URL.

          - `required Type Type`

            - `"url"Url`

          - `required string Url`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource:`

          Image referenced by file ID.

          - `required string FileID`

            ID of a previously uploaded file.

          - `required Type Type`

            - `"file"File`

      - `required Type Type`

        - `"image"Image`

    - `class BetaManagedAgentsDocumentBlock:`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `required Source Source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource:`

          Base64-encoded document data.

          - `required string Data`

            Base64-encoded document data.

          - `required string MediaType`

            MIME type of the document (e.g., "application/pdf").

          - `required Type Type`

            - `"base64"Base64`

        - `class BetaManagedAgentsPlainTextDocumentSource:`

          Plain text document content.

          - `required string Data`

            The plain text content.

          - `required MediaType MediaType`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"TextPlain`

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsUrlDocumentSource:`

          Document referenced by URL.

          - `required Type Type`

            - `"url"Url`

          - `required string Url`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource:`

          Document referenced by file ID.

          - `required string FileID`

            ID of a previously uploaded file.

          - `required Type Type`

            - `"file"File`

      - `required Type Type`

        - `"document"Document`

      - `string? Context`

        Additional context about the document for the model.

      - `string? Title`

        The title of the document.

  - `required Type Type`

    - `"user.message"UserMessage`

  - `DateTimeOffset? ProcessedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Message Event Params

- `class BetaManagedAgentsUserMessageEventParams:`

  Parameters for sending a user message to the session.

  - `required IReadOnlyList<Content> Content`

    Array of content blocks for the user message.

    - `class BetaManagedAgentsTextBlock:`

      Regular text content.

      - `required string Text`

        The text content.

      - `required Type Type`

        - `"text"Text`

    - `class BetaManagedAgentsImageBlock:`

      Image content specified directly as base64 data or as a reference via a URL.

      - `required Source Source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource:`

          Base64-encoded image data.

          - `required string Data`

            Base64-encoded image data.

          - `required string MediaType`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `required Type Type`

            - `"base64"Base64`

        - `class BetaManagedAgentsUrlImageSource:`

          Image referenced by URL.

          - `required Type Type`

            - `"url"Url`

          - `required string Url`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource:`

          Image referenced by file ID.

          - `required string FileID`

            ID of a previously uploaded file.

          - `required Type Type`

            - `"file"File`

      - `required Type Type`

        - `"image"Image`

    - `class BetaManagedAgentsDocumentBlock:`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `required Source Source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource:`

          Base64-encoded document data.

          - `required string Data`

            Base64-encoded document data.

          - `required string MediaType`

            MIME type of the document (e.g., "application/pdf").

          - `required Type Type`

            - `"base64"Base64`

        - `class BetaManagedAgentsPlainTextDocumentSource:`

          Plain text document content.

          - `required string Data`

            The plain text content.

          - `required MediaType MediaType`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"TextPlain`

          - `required Type Type`

            - `"text"Text`

        - `class BetaManagedAgentsUrlDocumentSource:`

          Document referenced by URL.

          - `required Type Type`

            - `"url"Url`

          - `required string Url`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource:`

          Document referenced by file ID.

          - `required string FileID`

            ID of a previously uploaded file.

          - `required Type Type`

            - `"file"File`

      - `required Type Type`

        - `"document"Document`

      - `string? Context`

        Additional context about the document for the model.

      - `string? Title`

        The title of the document.

  - `required Type Type`

    - `"user.message"UserMessage`

### Beta Managed Agents User Tool Confirmation Event

- `class BetaManagedAgentsUserToolConfirmationEvent:`

  A tool confirmation event that approves or denies a pending tool execution.

  - `required string ID`

    Unique identifier for this event.

  - `required Result Result`

    UserToolConfirmationResult enum

    - `"allow"Allow`

    - `"deny"Deny`

  - `required string ToolUseID`

    The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `required Type Type`

    - `"user.tool_confirmation"UserToolConfirmation`

  - `string? DenyMessage`

    Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

  - `DateTimeOffset? ProcessedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Tool Confirmation Event Params

- `class BetaManagedAgentsUserToolConfirmationEventParams:`

  Parameters for confirming or denying a tool execution request.

  - `required Result Result`

    UserToolConfirmationResult enum

    - `"allow"Allow`

    - `"deny"Deny`

  - `required string ToolUseID`

    The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `required Type Type`

    - `"user.tool_confirmation"UserToolConfirmation`

  - `string? DenyMessage`

    Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

# Resources

## Add

`BetaManagedAgentsFileResource Beta.Sessions.Resources.Add(ResourceAddParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/sessions/{session_id}/resources`

Add Session Resource

### Parameters

- `ResourceAddParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string fileID`

    Body param: ID of a previously uploaded file.

  - `required Type type`

    Body param

    - `"file"File`

  - `string? mountPath`

    Body param: Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

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

### Returns

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

### Example

```csharp
ResourceAddParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    FileID = "file_011CNha8iCJcU1wXNR6q4V8w",
    Type = Type.File,
};

var betaManagedAgentsFileResource = await client.Beta.Sessions.Resources.Add(parameters);

Console.WriteLine(betaManagedAgentsFileResource);
```

## List

`ResourceListPageResponse Beta.Sessions.Resources.List(ResourceListParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/sessions/{session_id}/resources`

List Session Resources

### Parameters

- `ResourceListParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `Int limit`

    Query param: Maximum number of resources to return per page (max 1000). If omitted, returns all resources.

  - `string page`

    Query param: Opaque cursor from a previous response's next_page field.

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

### Returns

- `class ResourceListPageResponse:`

  Paginated list of resources attached to a session.

  - `required IReadOnlyList<BetaManagedAgentsSessionResource> Data`

    Resources for the session, ordered by `created_at`.

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

  - `string? NextPage`

    Opaque cursor for the next page. Null when no more results.

### Example

```csharp
ResourceListParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7"
};

var page = await client.Beta.Sessions.Resources.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

## Retrieve

`ResourceRetrieveResponse Beta.Sessions.Resources.Retrieve(ResourceRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/sessions/{session_id}/resources/{resource_id}`

Get Session Resource

### Parameters

- `ResourceRetrieveParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string resourceID`

    Path param: Path parameter resource_id

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

### Returns

- `class ResourceRetrieveResponse: A class that can be one of several variants.union`

  The requested session resource.

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

### Example

```csharp
ResourceRetrieveParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ResourceID = "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
};

var resource = await client.Beta.Sessions.Resources.Retrieve(parameters);

Console.WriteLine(resource);
```

## Update

`ResourceUpdateResponse Beta.Sessions.Resources.Update(ResourceUpdateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/sessions/{session_id}/resources/{resource_id}`

Update Session Resource

### Parameters

- `ResourceUpdateParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string resourceID`

    Path param: Path parameter resource_id

  - `required string authorizationToken`

    Body param: New authorization token for the resource. Currently only `github_repository` resources support token rotation.

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

### Returns

- `class ResourceUpdateResponse: A class that can be one of several variants.union`

  The updated session resource.

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

### Example

```csharp
ResourceUpdateParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ResourceID = "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
    AuthorizationToken = "ghp_exampletoken",
};

var resource = await client.Beta.Sessions.Resources.Update(parameters);

Console.WriteLine(resource);
```

## Delete

`BetaManagedAgentsDeleteSessionResource Beta.Sessions.Resources.Delete(ResourceDeleteParamsparameters, CancellationTokencancellationToken = default)`

**delete** `/v1/sessions/{session_id}/resources/{resource_id}`

Delete Session Resource

### Parameters

- `ResourceDeleteParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string resourceID`

    Path param: Path parameter resource_id

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

### Returns

- `class BetaManagedAgentsDeleteSessionResource:`

  Confirmation of resource deletion.

  - `required string ID`

  - `required Type Type`

    - `"session_resource_deleted"SessionResourceDeleted`

### Example

```csharp
ResourceDeleteParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ResourceID = "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
};

var betaManagedAgentsDeleteSessionResource = await client.Beta.Sessions.Resources.Delete(parameters);

Console.WriteLine(betaManagedAgentsDeleteSessionResource);
```

## Domain Types

### Beta Managed Agents Delete Session Resource

- `class BetaManagedAgentsDeleteSessionResource:`

  Confirmation of resource deletion.

  - `required string ID`

  - `required Type Type`

    - `"session_resource_deleted"SessionResourceDeleted`

### Beta Managed Agents File Resource

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

### Beta Managed Agents GitHub Repository Resource

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

### Beta Managed Agents Memory Store Resource

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

### Beta Managed Agents Session Resource

- `class BetaManagedAgentsSessionResource: A class that can be one of several variants.union`

  A memory store attached to an agent session.

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
