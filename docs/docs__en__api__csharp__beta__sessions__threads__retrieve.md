## Get Session Thread

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

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

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
