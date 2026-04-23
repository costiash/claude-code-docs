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
