# Threads

## List

`ThreadListPageResponse Beta.Sessions.Threads.List(ThreadListParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/sessions/{session_id}/threads`

List Session Threads

### Parameters

- `ThreadListParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `Int limit`

    Query param: Maximum results per page. Defaults to 1000.

  - `string page`

    Query param: Opaque pagination cursor from a previous response's next_page. Forward-only.

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

### Returns

- `class ThreadListPageResponse:`

  Paginated list of threads within a `session`.

  - `IReadOnlyList<BetaManagedAgentsSessionThread> Data`

    Threads in the session, primary first then children in spawn order.

    - `required string ID`

      Unique identifier for this thread.

    - `required BetaManagedAgentsSessionThreadAgent Agent`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

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

    - `required string? ParentThreadID`

      Parent thread that spawned this thread. Null for the primary thread.

    - `required string SessionID`

      The session this thread belongs to.

    - `required BetaManagedAgentsSessionThreadStats? Stats`

      Timing statistics for a session thread.

      - `Double ActiveSeconds`

        Cumulative time in seconds the thread spent actively running. Excludes idle time.

      - `Double DurationSeconds`

        Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      - `Double StartupSeconds`

        Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

    - `required BetaManagedAgentsSessionThreadStatus Status`

      SessionThreadStatus enum

      - `"running"Running`

      - `"idle"Idle`

      - `"rescheduling"Rescheduling`

      - `"terminated"Terminated`

    - `required Type Type`

      - `"session_thread"SessionThread`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

    - `required BetaManagedAgentsSessionThreadUsage? Usage`

      Cumulative token usage for a session thread across all turns.

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

  - `string? NextPage`

    Opaque cursor for the next page. Null when no more results.

### Example

```csharp
ThreadListParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7"
};

var page = await client.Beta.Sessions.Threads.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

## Retrieve

`BetaManagedAgentsSessionThread Beta.Sessions.Threads.Retrieve(ThreadRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/sessions/{session_id}/threads/{thread_id}`

Get Session Thread

### Parameters

- `ThreadRetrieveParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string threadID`

    Path param: Path parameter thread_id

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

### Returns

- `class BetaManagedAgentsSessionThread:`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `required string ID`

    Unique identifier for this thread.

  - `required BetaManagedAgentsSessionThreadAgent Agent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

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

  - `required string? ParentThreadID`

    Parent thread that spawned this thread. Null for the primary thread.

  - `required string SessionID`

    The session this thread belongs to.

  - `required BetaManagedAgentsSessionThreadStats? Stats`

    Timing statistics for a session thread.

    - `Double ActiveSeconds`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `Double DurationSeconds`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `Double StartupSeconds`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `required BetaManagedAgentsSessionThreadStatus Status`

    SessionThreadStatus enum

    - `"running"Running`

    - `"idle"Idle`

    - `"rescheduling"Rescheduling`

    - `"terminated"Terminated`

  - `required Type Type`

    - `"session_thread"SessionThread`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required BetaManagedAgentsSessionThreadUsage? Usage`

    Cumulative token usage for a session thread across all turns.

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

### Example

```csharp
ThreadRetrieveParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ThreadID = "sthr_011CZkZVWa6oIjw0rgXZpnBt",
};

var betaManagedAgentsSessionThread = await client.Beta.Sessions.Threads.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsSessionThread);
```

## Archive

`BetaManagedAgentsSessionThread Beta.Sessions.Threads.Archive(ThreadArchiveParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/sessions/{session_id}/threads/{thread_id}/archive`

Archive Session Thread

### Parameters

- `ThreadArchiveParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string threadID`

    Path param: Path parameter thread_id

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

### Returns

- `class BetaManagedAgentsSessionThread:`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `required string ID`

    Unique identifier for this thread.

  - `required BetaManagedAgentsSessionThreadAgent Agent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

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

  - `required string? ParentThreadID`

    Parent thread that spawned this thread. Null for the primary thread.

  - `required string SessionID`

    The session this thread belongs to.

  - `required BetaManagedAgentsSessionThreadStats? Stats`

    Timing statistics for a session thread.

    - `Double ActiveSeconds`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `Double DurationSeconds`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `Double StartupSeconds`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `required BetaManagedAgentsSessionThreadStatus Status`

    SessionThreadStatus enum

    - `"running"Running`

    - `"idle"Idle`

    - `"rescheduling"Rescheduling`

    - `"terminated"Terminated`

  - `required Type Type`

    - `"session_thread"SessionThread`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required BetaManagedAgentsSessionThreadUsage? Usage`

    Cumulative token usage for a session thread across all turns.

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

### Example

```csharp
ThreadArchiveParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ThreadID = "sthr_011CZkZVWa6oIjw0rgXZpnBt",
};

var betaManagedAgentsSessionThread = await client.Beta.Sessions.Threads.Archive(parameters);

Console.WriteLine(betaManagedAgentsSessionThread);
```

## Domain Types

### Beta Managed Agents Session Thread

- `class BetaManagedAgentsSessionThread:`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `required string ID`

    Unique identifier for this thread.

  - `required BetaManagedAgentsSessionThreadAgent Agent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

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

  - `required string? ParentThreadID`

    Parent thread that spawned this thread. Null for the primary thread.

  - `required string SessionID`

    The session this thread belongs to.

  - `required BetaManagedAgentsSessionThreadStats? Stats`

    Timing statistics for a session thread.

    - `Double ActiveSeconds`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `Double DurationSeconds`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `Double StartupSeconds`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `required BetaManagedAgentsSessionThreadStatus Status`

    SessionThreadStatus enum

    - `"running"Running`

    - `"idle"Idle`

    - `"rescheduling"Rescheduling`

    - `"terminated"Terminated`

  - `required Type Type`

    - `"session_thread"SessionThread`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required BetaManagedAgentsSessionThreadUsage? Usage`

    Cumulative token usage for a session thread across all turns.

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

### Beta Managed Agents Session Thread Agent

- `class BetaManagedAgentsSessionThreadAgent:`

  Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

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

### Beta Managed Agents Session Thread Stats

- `class BetaManagedAgentsSessionThreadStats:`

  Timing statistics for a session thread.

  - `Double ActiveSeconds`

    Cumulative time in seconds the thread spent actively running. Excludes idle time.

  - `Double DurationSeconds`

    Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

  - `Double StartupSeconds`

    Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

### Beta Managed Agents Session Thread Status

- `enum BetaManagedAgentsSessionThreadStatus:`

  SessionThreadStatus enum

  - `"running"Running`

  - `"idle"Idle`

  - `"rescheduling"Rescheduling`

  - `"terminated"Terminated`

### Beta Managed Agents Session Thread Usage

- `class BetaManagedAgentsSessionThreadUsage:`

  Cumulative token usage for a session thread across all turns.

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

### Beta Managed Agents Stream Session Thread Events

- `class BetaManagedAgentsStreamSessionThreadEvents: A class that can be one of several variants.union`

  Server-sent event in a single thread's stream.

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

    - `string? SessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

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

    - `string? SessionThreadID`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

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

    - `string? SessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

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

    - `string? SessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

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

    - `string? SessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

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

    - `string? SessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

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

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent:`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Message content blocks.

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

    - `required string FromSessionThreadID`

      Public `sthr_` ID of the thread that sent the message.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.thread_message_received"AgentThreadMessageReceived`

    - `string? FromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent:`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Message content blocks.

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

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string ToSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `required Type Type`

      - `"agent.thread_message_sent"AgentThreadMessageSent`

    - `string? ToAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

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

  - `class BetaManagedAgentsSessionThreadCreatedEvent:`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the callable agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string SessionThreadID`

      Public `sthr_` ID of the newly created thread.

    - `required Type Type`

      - `"session.thread_created"SessionThreadCreated`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:`

    Emitted when an outcome evaluation cycle begins.

    - `required string ID`

      Unique identifier for this event.

    - `required Int Iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"span.outcome_evaluation_start"SpanOutcomeEvaluationStart`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `required string ID`

      Unique identifier for this event.

    - `required string Explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `required Int Iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `required string OutcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string Result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `required Type Type`

      - `"span.outcome_evaluation_end"SpanOutcomeEvaluationEnd`

    - `required BetaManagedAgentsSpanModelUsage Usage`

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

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `required string ID`

      Unique identifier for this event.

    - `required Int Iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"span.outcome_evaluation_ongoing"SpanOutcomeEvaluationOngoing`

  - `class BetaManagedAgentsUserDefineOutcomeEvent:`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `required string ID`

      Unique identifier for this event.

    - `required string Description`

      What the agent should produce. Copied from the input event.

    - `required Int? MaxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `required string OutcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Rubric Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric:`

        Rubric referenced by a file uploaded via the Files API.

        - `required string FileID`

          ID of the rubric file.

        - `required Type Type`

          - `"file"File`

      - `class BetaManagedAgentsTextRubric:`

        Rubric content provided inline as text.

        - `required string Content`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `required Type Type`

          - `"text"Text`

    - `required Type Type`

      - `"user.define_outcome"UserDefineOutcome`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.deleted"SessionDeleted`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent:`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that started running.

    - `required Type Type`

      - `"session.thread_status_running"SessionThreadStatusRunning`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent:`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that went idle.

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

      - `"session.thread_status_idle"SessionThreadStatusIdle`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent:`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that terminated.

    - `required Type Type`

      - `"session.thread_status_terminated"SessionThreadStatusTerminated`

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent:`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that is retrying.

    - `required Type Type`

      - `"session.thread_status_rescheduled"SessionThreadStatusRescheduled`

# Events

## List

`EventListPageResponse Beta.Sessions.Threads.Events.List(EventListParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/sessions/{session_id}/threads/{thread_id}/events`

List Session Thread Events

### Parameters

- `EventListParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string threadID`

    Path param: Path parameter thread_id

  - `Int limit`

    Query param: Query parameter for limit

  - `string page`

    Query param: Query parameter for page

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

### Returns

- `class EventListPageResponse:`

  Paginated list of events for a single thread within a `session`.

  - `IReadOnlyList<BetaManagedAgentsSessionEvent> Data`

    Events for the thread, ordered by `created_at`.

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

      - `string? SessionThreadID`

        If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

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

      - `string? SessionThreadID`

        When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

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

      - `string? SessionThreadID`

        Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

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

      - `string? SessionThreadID`

        When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

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

      - `string? SessionThreadID`

        When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

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

      - `string? SessionThreadID`

        When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

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

    - `class BetaManagedAgentsAgentThreadMessageReceivedEvent:`

      Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

      - `required string ID`

        Unique identifier for this event.

      - `required IReadOnlyList<Content> Content`

        Message content blocks.

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

      - `required string FromSessionThreadID`

        Public `sthr_` ID of the thread that sent the message.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"agent.thread_message_received"AgentThreadMessageReceived`

      - `string? FromAgentName`

        Name of the callable agent this message came from. Absent when received from the primary agent.

    - `class BetaManagedAgentsAgentThreadMessageSentEvent:`

      Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

      - `required string ID`

        Unique identifier for this event.

      - `required IReadOnlyList<Content> Content`

        Message content blocks.

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

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required string ToSessionThreadID`

        Public `sthr_` ID of the thread the message was sent to.

      - `required Type Type`

        - `"agent.thread_message_sent"AgentThreadMessageSent`

      - `string? ToAgentName`

        Name of the callable agent this message was sent to. Absent when sent to the primary agent.

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

    - `class BetaManagedAgentsSessionThreadCreatedEvent:`

      Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

      - `required string ID`

        Unique identifier for this event.

      - `required string AgentName`

        Name of the callable agent the thread runs.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required string SessionThreadID`

        Public `sthr_` ID of the newly created thread.

      - `required Type Type`

        - `"session.thread_created"SessionThreadCreated`

    - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:`

      Emitted when an outcome evaluation cycle begins.

      - `required string ID`

        Unique identifier for this event.

      - `required Int Iteration`

        0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      - `required string OutcomeID`

        The `outc_` ID of the outcome being evaluated.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"span.outcome_evaluation_start"SpanOutcomeEvaluationStart`

    - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:`

      Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

      - `required string ID`

        Unique identifier for this event.

      - `required string Explanation`

        Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

      - `required Int Iteration`

        0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      - `required string OutcomeEvaluationStartID`

        The id of the corresponding `span.outcome_evaluation_start` event.

      - `required string OutcomeID`

        The `outc_` ID of the outcome being evaluated.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required string Result`

        Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

      - `required Type Type`

        - `"span.outcome_evaluation_end"SpanOutcomeEvaluationEnd`

      - `required BetaManagedAgentsSpanModelUsage Usage`

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

    - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:`

      Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

      - `required string ID`

        Unique identifier for this event.

      - `required Int Iteration`

        0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      - `required string OutcomeID`

        The `outc_` ID of the outcome being evaluated.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"span.outcome_evaluation_ongoing"SpanOutcomeEvaluationOngoing`

    - `class BetaManagedAgentsUserDefineOutcomeEvent:`

      Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

      - `required string ID`

        Unique identifier for this event.

      - `required string Description`

        What the agent should produce. Copied from the input event.

      - `required Int? MaxIterations`

        Evaluate-then-revise cycles before giving up. Default 3, max 20.

      - `required string OutcomeID`

        Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Rubric Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `required string FileID`

            ID of the rubric file.

          - `required Type Type`

            - `"file"File`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `required Type Type`

            - `"text"Text`

      - `required Type Type`

        - `"user.define_outcome"UserDefineOutcome`

    - `class BetaManagedAgentsSessionDeletedEvent:`

      Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required Type Type`

        - `"session.deleted"SessionDeleted`

    - `class BetaManagedAgentsSessionThreadStatusRunningEvent:`

      A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

      - `required string ID`

        Unique identifier for this event.

      - `required string AgentName`

        Name of the agent the thread runs.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required string SessionThreadID`

        Public sthr_ ID of the thread that started running.

      - `required Type Type`

        - `"session.thread_status_running"SessionThreadStatusRunning`

    - `class BetaManagedAgentsSessionThreadStatusIdleEvent:`

      A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

      - `required string ID`

        Unique identifier for this event.

      - `required string AgentName`

        Name of the agent the thread runs.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required string SessionThreadID`

        Public sthr_ ID of the thread that went idle.

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

        - `"session.thread_status_idle"SessionThreadStatusIdle`

    - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent:`

      A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

      - `required string ID`

        Unique identifier for this event.

      - `required string AgentName`

        Name of the agent the thread runs.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required string SessionThreadID`

        Public sthr_ ID of the thread that terminated.

      - `required Type Type`

        - `"session.thread_status_terminated"SessionThreadStatusTerminated`

    - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent:`

      A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

      - `required string ID`

        Unique identifier for this event.

      - `required string AgentName`

        Name of the agent the thread runs.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

      - `required string SessionThreadID`

        Public sthr_ ID of the thread that is retrying.

      - `required Type Type`

        - `"session.thread_status_rescheduled"SessionThreadStatusRescheduled`

  - `string? NextPage`

    Opaque cursor for the next page. Null when no more results.

### Example

```csharp
EventListParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ThreadID = "sthr_011CZkZVWa6oIjw0rgXZpnBt",
};

var page = await client.Beta.Sessions.Threads.Events.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

## Stream

`BetaManagedAgentsStreamSessionThreadEvents Beta.Sessions.Threads.Events.StreamStreaming(EventStreamParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/sessions/{session_id}/threads/{thread_id}/stream`

Stream Session Thread Events

### Parameters

- `EventStreamParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string threadID`

    Path param: Path parameter thread_id

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

### Returns

- `class BetaManagedAgentsStreamSessionThreadEvents: A class that can be one of several variants.union`

  Server-sent event in a single thread's stream.

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

    - `string? SessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

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

    - `string? SessionThreadID`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

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

    - `string? SessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

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

    - `string? SessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

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

    - `string? SessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

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

    - `string? SessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

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

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent:`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Message content blocks.

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

    - `required string FromSessionThreadID`

      Public `sthr_` ID of the thread that sent the message.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.thread_message_received"AgentThreadMessageReceived`

    - `string? FromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent:`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Message content blocks.

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

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string ToSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `required Type Type`

      - `"agent.thread_message_sent"AgentThreadMessageSent`

    - `string? ToAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

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

  - `class BetaManagedAgentsSessionThreadCreatedEvent:`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the callable agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string SessionThreadID`

      Public `sthr_` ID of the newly created thread.

    - `required Type Type`

      - `"session.thread_created"SessionThreadCreated`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:`

    Emitted when an outcome evaluation cycle begins.

    - `required string ID`

      Unique identifier for this event.

    - `required Int Iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"span.outcome_evaluation_start"SpanOutcomeEvaluationStart`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `required string ID`

      Unique identifier for this event.

    - `required string Explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `required Int Iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `required string OutcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string Result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `required Type Type`

      - `"span.outcome_evaluation_end"SpanOutcomeEvaluationEnd`

    - `required BetaManagedAgentsSpanModelUsage Usage`

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

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `required string ID`

      Unique identifier for this event.

    - `required Int Iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"span.outcome_evaluation_ongoing"SpanOutcomeEvaluationOngoing`

  - `class BetaManagedAgentsUserDefineOutcomeEvent:`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `required string ID`

      Unique identifier for this event.

    - `required string Description`

      What the agent should produce. Copied from the input event.

    - `required Int? MaxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `required string OutcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Rubric Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric:`

        Rubric referenced by a file uploaded via the Files API.

        - `required string FileID`

          ID of the rubric file.

        - `required Type Type`

          - `"file"File`

      - `class BetaManagedAgentsTextRubric:`

        Rubric content provided inline as text.

        - `required string Content`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `required Type Type`

          - `"text"Text`

    - `required Type Type`

      - `"user.define_outcome"UserDefineOutcome`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.deleted"SessionDeleted`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent:`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that started running.

    - `required Type Type`

      - `"session.thread_status_running"SessionThreadStatusRunning`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent:`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that went idle.

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

      - `"session.thread_status_idle"SessionThreadStatusIdle`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent:`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that terminated.

    - `required Type Type`

      - `"session.thread_status_terminated"SessionThreadStatusTerminated`

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent:`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that is retrying.

    - `required Type Type`

      - `"session.thread_status_rescheduled"SessionThreadStatusRescheduled`

### Example

```csharp
EventStreamParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ThreadID = "sthr_011CZkZVWa6oIjw0rgXZpnBt",
};

await foreach (var betaManagedAgentsStreamSessionThreadEvents in client.Beta.Sessions.Threads.Events.StreamStreaming(parameters))
{
    Console.WriteLine(betaManagedAgentsStreamSessionThreadEvents);
}
```
