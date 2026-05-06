# Threads

## List

`ThreadListPage beta().sessions().threads().list(ThreadListParamsparams = ThreadListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/sessions/{session_id}/threads`

List Session Threads

### Parameters

- `ThreadListParams params`

  - `Optional<String> sessionId`

  - `Optional<Long> limit`

    Maximum results per page. Defaults to 1000.

  - `Optional<String> page`

    Opaque pagination cursor from a previous response's next_page. Forward-only.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

### Returns

- `class BetaManagedAgentsSessionThread:`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `String id`

    Unique identifier for this thread.

  - `BetaManagedAgentsSessionThreadAgent agent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

    - `String id`

    - `Optional<String> description`

    - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

      - `String name`

      - `Type type`

        - `URL("url")`

      - `String url`

    - `BetaManagedAgentsModelConfig model`

      Model identifier and configuration.

      - `BetaManagedAgentsModel id`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

          Frontier intelligence for long-running agents and coding

        - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

          Most intelligent model for building agents and coding

        - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

          Best combination of speed and intelligence

        - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

          Fastest model with near-frontier intelligence

        - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

          Fastest model with near-frontier intelligence

        - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

          Premium model combining maximum intelligence with practical performance

        - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

          Premium model combining maximum intelligence with practical performance

        - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

          High-performance model for agents and coding

        - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

          High-performance model for agents and coding

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

    - `String name`

    - `List<Skill> skills`

      - `class BetaManagedAgentsAnthropicSkill:`

        A resolved Anthropic-managed skill.

        - `String skillId`

        - `Type type`

          - `ANTHROPIC("anthropic")`

        - `String version`

      - `class BetaManagedAgentsCustomSkill:`

        A resolved user-created custom skill.

        - `String skillId`

        - `Type type`

          - `CUSTOM("custom")`

        - `String version`

    - `Optional<String> system`

    - `List<Tool> tools`

      - `class BetaManagedAgentsAgentToolset20260401:`

        - `List<BetaManagedAgentsAgentToolConfig> configs`

          - `boolean enabled`

          - `Name name`

            Built-in agent tool identifier.

            - `BASH("bash")`

            - `EDIT("edit")`

            - `READ("read")`

            - `WRITE("write")`

            - `GLOB("glob")`

            - `GREP("grep")`

            - `WEB_FETCH("web_fetch")`

            - `WEB_SEARCH("web_search")`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `Type type`

                - `ALWAYS_ALLOW("always_allow")`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `Type type`

                - `ALWAYS_ASK("always_ask")`

        - `BetaManagedAgentsAgentToolsetDefaultConfig defaultConfig`

          Resolved default configuration for agent tools.

          - `boolean enabled`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `Type type`

                - `ALWAYS_ALLOW("always_allow")`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `Type type`

                - `ALWAYS_ASK("always_ask")`

        - `Type type`

          - `AGENT_TOOLSET_20260401("agent_toolset_20260401")`

      - `class BetaManagedAgentsMcpToolset:`

        - `List<BetaManagedAgentsMcpToolConfig> configs`

          - `boolean enabled`

          - `String name`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `Type type`

                - `ALWAYS_ALLOW("always_allow")`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `Type type`

                - `ALWAYS_ASK("always_ask")`

        - `BetaManagedAgentsMcpToolsetDefaultConfig defaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `boolean enabled`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `Type type`

                - `ALWAYS_ALLOW("always_allow")`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `Type type`

                - `ALWAYS_ASK("always_ask")`

        - `String mcpServerName`

        - `Type type`

          - `MCP_TOOLSET("mcp_toolset")`

      - `class BetaManagedAgentsCustomTool:`

        A custom tool as returned in API responses.

        - `String description`

        - `BetaManagedAgentsCustomToolInputSchema inputSchema`

          JSON Schema for custom tool input parameters.

          - `Optional<Properties> properties`

            JSON Schema properties defining the tool's input parameters.

          - `Optional<List<String>> required`

            List of required property names.

          - `Optional<Type> type`

            Must be 'object' for tool input schemas.

            - `OBJECT("object")`

        - `String name`

        - `Type type`

          - `CUSTOM("custom")`

    - `Type type`

      - `AGENT("agent")`

    - `long version`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> parentThreadId`

    Parent thread that spawned this thread. Null for the primary thread.

  - `String sessionId`

    The session this thread belongs to.

  - `Optional<BetaManagedAgentsSessionThreadStats> stats`

    Timing statistics for a session thread.

    - `Optional<Double> activeSeconds`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `Optional<Double> durationSeconds`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `Optional<Double> startupSeconds`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `BetaManagedAgentsSessionThreadStatus status`

    SessionThreadStatus enum

    - `RUNNING("running")`

    - `IDLE("idle")`

    - `RESCHEDULING("rescheduling")`

    - `TERMINATED("terminated")`

  - `Type type`

    - `SESSION_THREAD("session_thread")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaManagedAgentsSessionThreadUsage> usage`

    Cumulative token usage for a session thread across all turns.

    - `Optional<BetaManagedAgentsCacheCreationUsage> cacheCreation`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Optional<Long> ephemeral1hInputTokens`

        Tokens used to create 1-hour ephemeral cache entries.

      - `Optional<Long> ephemeral5mInputTokens`

        Tokens used to create 5-minute ephemeral cache entries.

    - `Optional<Long> cacheReadInputTokens`

      Total tokens read from prompt cache.

    - `Optional<Long> inputTokens`

      Total input tokens consumed across all turns.

    - `Optional<Long> outputTokens`

      Total output tokens generated across all turns.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.threads.ThreadListPage;
import com.anthropic.models.beta.sessions.threads.ThreadListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ThreadListPage page = client.beta().sessions().threads().list("sesn_011CZkZAtmR3yMPDzynEDxu7");
    }
}
```

## Retrieve

`BetaManagedAgentsSessionThread beta().sessions().threads().retrieve(ThreadRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/sessions/{session_id}/threads/{thread_id}`

Get Session Thread

### Parameters

- `ThreadRetrieveParams params`

  - `String sessionId`

  - `Optional<String> threadId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

### Returns

- `class BetaManagedAgentsSessionThread:`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `String id`

    Unique identifier for this thread.

  - `BetaManagedAgentsSessionThreadAgent agent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

    - `String id`

    - `Optional<String> description`

    - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

      - `String name`

      - `Type type`

        - `URL("url")`

      - `String url`

    - `BetaManagedAgentsModelConfig model`

      Model identifier and configuration.

      - `BetaManagedAgentsModel id`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

          Frontier intelligence for long-running agents and coding

        - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

          Most intelligent model for building agents and coding

        - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

          Best combination of speed and intelligence

        - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

          Fastest model with near-frontier intelligence

        - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

          Fastest model with near-frontier intelligence

        - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

          Premium model combining maximum intelligence with practical performance

        - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

          Premium model combining maximum intelligence with practical performance

        - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

          High-performance model for agents and coding

        - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

          High-performance model for agents and coding

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

    - `String name`

    - `List<Skill> skills`

      - `class BetaManagedAgentsAnthropicSkill:`

        A resolved Anthropic-managed skill.

        - `String skillId`

        - `Type type`

          - `ANTHROPIC("anthropic")`

        - `String version`

      - `class BetaManagedAgentsCustomSkill:`

        A resolved user-created custom skill.

        - `String skillId`

        - `Type type`

          - `CUSTOM("custom")`

        - `String version`

    - `Optional<String> system`

    - `List<Tool> tools`

      - `class BetaManagedAgentsAgentToolset20260401:`

        - `List<BetaManagedAgentsAgentToolConfig> configs`

          - `boolean enabled`

          - `Name name`

            Built-in agent tool identifier.

            - `BASH("bash")`

            - `EDIT("edit")`

            - `READ("read")`

            - `WRITE("write")`

            - `GLOB("glob")`

            - `GREP("grep")`

            - `WEB_FETCH("web_fetch")`

            - `WEB_SEARCH("web_search")`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `Type type`

                - `ALWAYS_ALLOW("always_allow")`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `Type type`

                - `ALWAYS_ASK("always_ask")`

        - `BetaManagedAgentsAgentToolsetDefaultConfig defaultConfig`

          Resolved default configuration for agent tools.

          - `boolean enabled`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `Type type`

                - `ALWAYS_ALLOW("always_allow")`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `Type type`

                - `ALWAYS_ASK("always_ask")`

        - `Type type`

          - `AGENT_TOOLSET_20260401("agent_toolset_20260401")`

      - `class BetaManagedAgentsMcpToolset:`

        - `List<BetaManagedAgentsMcpToolConfig> configs`

          - `boolean enabled`

          - `String name`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `Type type`

                - `ALWAYS_ALLOW("always_allow")`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `Type type`

                - `ALWAYS_ASK("always_ask")`

        - `BetaManagedAgentsMcpToolsetDefaultConfig defaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `boolean enabled`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `Type type`

                - `ALWAYS_ALLOW("always_allow")`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `Type type`

                - `ALWAYS_ASK("always_ask")`

        - `String mcpServerName`

        - `Type type`

          - `MCP_TOOLSET("mcp_toolset")`

      - `class BetaManagedAgentsCustomTool:`

        A custom tool as returned in API responses.

        - `String description`

        - `BetaManagedAgentsCustomToolInputSchema inputSchema`

          JSON Schema for custom tool input parameters.

          - `Optional<Properties> properties`

            JSON Schema properties defining the tool's input parameters.

          - `Optional<List<String>> required`

            List of required property names.

          - `Optional<Type> type`

            Must be 'object' for tool input schemas.

            - `OBJECT("object")`

        - `String name`

        - `Type type`

          - `CUSTOM("custom")`

    - `Type type`

      - `AGENT("agent")`

    - `long version`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> parentThreadId`

    Parent thread that spawned this thread. Null for the primary thread.

  - `String sessionId`

    The session this thread belongs to.

  - `Optional<BetaManagedAgentsSessionThreadStats> stats`

    Timing statistics for a session thread.

    - `Optional<Double> activeSeconds`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `Optional<Double> durationSeconds`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `Optional<Double> startupSeconds`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `BetaManagedAgentsSessionThreadStatus status`

    SessionThreadStatus enum

    - `RUNNING("running")`

    - `IDLE("idle")`

    - `RESCHEDULING("rescheduling")`

    - `TERMINATED("terminated")`

  - `Type type`

    - `SESSION_THREAD("session_thread")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaManagedAgentsSessionThreadUsage> usage`

    Cumulative token usage for a session thread across all turns.

    - `Optional<BetaManagedAgentsCacheCreationUsage> cacheCreation`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Optional<Long> ephemeral1hInputTokens`

        Tokens used to create 1-hour ephemeral cache entries.

      - `Optional<Long> ephemeral5mInputTokens`

        Tokens used to create 5-minute ephemeral cache entries.

    - `Optional<Long> cacheReadInputTokens`

      Total tokens read from prompt cache.

    - `Optional<Long> inputTokens`

      Total input tokens consumed across all turns.

    - `Optional<Long> outputTokens`

      Total output tokens generated across all turns.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.threads.BetaManagedAgentsSessionThread;
import com.anthropic.models.beta.sessions.threads.ThreadRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ThreadRetrieveParams params = ThreadRetrieveParams.builder()
            .sessionId("sesn_011CZkZAtmR3yMPDzynEDxu7")
            .threadId("sthr_011CZkZVWa6oIjw0rgXZpnBt")
            .build();
        BetaManagedAgentsSessionThread betaManagedAgentsSessionThread = client.beta().sessions().threads().retrieve(params);
    }
}
```

## Archive

`BetaManagedAgentsSessionThread beta().sessions().threads().archive(ThreadArchiveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/sessions/{session_id}/threads/{thread_id}/archive`

Archive Session Thread

### Parameters

- `ThreadArchiveParams params`

  - `String sessionId`

  - `Optional<String> threadId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

### Returns

- `class BetaManagedAgentsSessionThread:`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `String id`

    Unique identifier for this thread.

  - `BetaManagedAgentsSessionThreadAgent agent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

    - `String id`

    - `Optional<String> description`

    - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

      - `String name`

      - `Type type`

        - `URL("url")`

      - `String url`

    - `BetaManagedAgentsModelConfig model`

      Model identifier and configuration.

      - `BetaManagedAgentsModel id`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

          Frontier intelligence for long-running agents and coding

        - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

          Most intelligent model for building agents and coding

        - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

          Best combination of speed and intelligence

        - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

          Fastest model with near-frontier intelligence

        - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

          Fastest model with near-frontier intelligence

        - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

          Premium model combining maximum intelligence with practical performance

        - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

          Premium model combining maximum intelligence with practical performance

        - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

          High-performance model for agents and coding

        - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

          High-performance model for agents and coding

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

    - `String name`

    - `List<Skill> skills`

      - `class BetaManagedAgentsAnthropicSkill:`

        A resolved Anthropic-managed skill.

        - `String skillId`

        - `Type type`

          - `ANTHROPIC("anthropic")`

        - `String version`

      - `class BetaManagedAgentsCustomSkill:`

        A resolved user-created custom skill.

        - `String skillId`

        - `Type type`

          - `CUSTOM("custom")`

        - `String version`

    - `Optional<String> system`

    - `List<Tool> tools`

      - `class BetaManagedAgentsAgentToolset20260401:`

        - `List<BetaManagedAgentsAgentToolConfig> configs`

          - `boolean enabled`

          - `Name name`

            Built-in agent tool identifier.

            - `BASH("bash")`

            - `EDIT("edit")`

            - `READ("read")`

            - `WRITE("write")`

            - `GLOB("glob")`

            - `GREP("grep")`

            - `WEB_FETCH("web_fetch")`

            - `WEB_SEARCH("web_search")`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `Type type`

                - `ALWAYS_ALLOW("always_allow")`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `Type type`

                - `ALWAYS_ASK("always_ask")`

        - `BetaManagedAgentsAgentToolsetDefaultConfig defaultConfig`

          Resolved default configuration for agent tools.

          - `boolean enabled`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `Type type`

                - `ALWAYS_ALLOW("always_allow")`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `Type type`

                - `ALWAYS_ASK("always_ask")`

        - `Type type`

          - `AGENT_TOOLSET_20260401("agent_toolset_20260401")`

      - `class BetaManagedAgentsMcpToolset:`

        - `List<BetaManagedAgentsMcpToolConfig> configs`

          - `boolean enabled`

          - `String name`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `Type type`

                - `ALWAYS_ALLOW("always_allow")`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `Type type`

                - `ALWAYS_ASK("always_ask")`

        - `BetaManagedAgentsMcpToolsetDefaultConfig defaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `boolean enabled`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `Type type`

                - `ALWAYS_ALLOW("always_allow")`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `Type type`

                - `ALWAYS_ASK("always_ask")`

        - `String mcpServerName`

        - `Type type`

          - `MCP_TOOLSET("mcp_toolset")`

      - `class BetaManagedAgentsCustomTool:`

        A custom tool as returned in API responses.

        - `String description`

        - `BetaManagedAgentsCustomToolInputSchema inputSchema`

          JSON Schema for custom tool input parameters.

          - `Optional<Properties> properties`

            JSON Schema properties defining the tool's input parameters.

          - `Optional<List<String>> required`

            List of required property names.

          - `Optional<Type> type`

            Must be 'object' for tool input schemas.

            - `OBJECT("object")`

        - `String name`

        - `Type type`

          - `CUSTOM("custom")`

    - `Type type`

      - `AGENT("agent")`

    - `long version`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> parentThreadId`

    Parent thread that spawned this thread. Null for the primary thread.

  - `String sessionId`

    The session this thread belongs to.

  - `Optional<BetaManagedAgentsSessionThreadStats> stats`

    Timing statistics for a session thread.

    - `Optional<Double> activeSeconds`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `Optional<Double> durationSeconds`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `Optional<Double> startupSeconds`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `BetaManagedAgentsSessionThreadStatus status`

    SessionThreadStatus enum

    - `RUNNING("running")`

    - `IDLE("idle")`

    - `RESCHEDULING("rescheduling")`

    - `TERMINATED("terminated")`

  - `Type type`

    - `SESSION_THREAD("session_thread")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaManagedAgentsSessionThreadUsage> usage`

    Cumulative token usage for a session thread across all turns.

    - `Optional<BetaManagedAgentsCacheCreationUsage> cacheCreation`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Optional<Long> ephemeral1hInputTokens`

        Tokens used to create 1-hour ephemeral cache entries.

      - `Optional<Long> ephemeral5mInputTokens`

        Tokens used to create 5-minute ephemeral cache entries.

    - `Optional<Long> cacheReadInputTokens`

      Total tokens read from prompt cache.

    - `Optional<Long> inputTokens`

      Total input tokens consumed across all turns.

    - `Optional<Long> outputTokens`

      Total output tokens generated across all turns.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.threads.BetaManagedAgentsSessionThread;
import com.anthropic.models.beta.sessions.threads.ThreadArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ThreadArchiveParams params = ThreadArchiveParams.builder()
            .sessionId("sesn_011CZkZAtmR3yMPDzynEDxu7")
            .threadId("sthr_011CZkZVWa6oIjw0rgXZpnBt")
            .build();
        BetaManagedAgentsSessionThread betaManagedAgentsSessionThread = client.beta().sessions().threads().archive(params);
    }
}
```

## Domain Types

### Beta Managed Agents Session Thread

- `class BetaManagedAgentsSessionThread:`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `String id`

    Unique identifier for this thread.

  - `BetaManagedAgentsSessionThreadAgent agent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

    - `String id`

    - `Optional<String> description`

    - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

      - `String name`

      - `Type type`

        - `URL("url")`

      - `String url`

    - `BetaManagedAgentsModelConfig model`

      Model identifier and configuration.

      - `BetaManagedAgentsModel id`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

          Frontier intelligence for long-running agents and coding

        - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

          Most intelligent model for building agents and coding

        - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

          Best combination of speed and intelligence

        - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

          Fastest model with near-frontier intelligence

        - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

          Fastest model with near-frontier intelligence

        - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

          Premium model combining maximum intelligence with practical performance

        - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

          Premium model combining maximum intelligence with practical performance

        - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

          High-performance model for agents and coding

        - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

          High-performance model for agents and coding

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

    - `String name`

    - `List<Skill> skills`

      - `class BetaManagedAgentsAnthropicSkill:`

        A resolved Anthropic-managed skill.

        - `String skillId`

        - `Type type`

          - `ANTHROPIC("anthropic")`

        - `String version`

      - `class BetaManagedAgentsCustomSkill:`

        A resolved user-created custom skill.

        - `String skillId`

        - `Type type`

          - `CUSTOM("custom")`

        - `String version`

    - `Optional<String> system`

    - `List<Tool> tools`

      - `class BetaManagedAgentsAgentToolset20260401:`

        - `List<BetaManagedAgentsAgentToolConfig> configs`

          - `boolean enabled`

          - `Name name`

            Built-in agent tool identifier.

            - `BASH("bash")`

            - `EDIT("edit")`

            - `READ("read")`

            - `WRITE("write")`

            - `GLOB("glob")`

            - `GREP("grep")`

            - `WEB_FETCH("web_fetch")`

            - `WEB_SEARCH("web_search")`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `Type type`

                - `ALWAYS_ALLOW("always_allow")`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `Type type`

                - `ALWAYS_ASK("always_ask")`

        - `BetaManagedAgentsAgentToolsetDefaultConfig defaultConfig`

          Resolved default configuration for agent tools.

          - `boolean enabled`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `Type type`

                - `ALWAYS_ALLOW("always_allow")`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `Type type`

                - `ALWAYS_ASK("always_ask")`

        - `Type type`

          - `AGENT_TOOLSET_20260401("agent_toolset_20260401")`

      - `class BetaManagedAgentsMcpToolset:`

        - `List<BetaManagedAgentsMcpToolConfig> configs`

          - `boolean enabled`

          - `String name`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `Type type`

                - `ALWAYS_ALLOW("always_allow")`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `Type type`

                - `ALWAYS_ASK("always_ask")`

        - `BetaManagedAgentsMcpToolsetDefaultConfig defaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `boolean enabled`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `Type type`

                - `ALWAYS_ALLOW("always_allow")`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `Type type`

                - `ALWAYS_ASK("always_ask")`

        - `String mcpServerName`

        - `Type type`

          - `MCP_TOOLSET("mcp_toolset")`

      - `class BetaManagedAgentsCustomTool:`

        A custom tool as returned in API responses.

        - `String description`

        - `BetaManagedAgentsCustomToolInputSchema inputSchema`

          JSON Schema for custom tool input parameters.

          - `Optional<Properties> properties`

            JSON Schema properties defining the tool's input parameters.

          - `Optional<List<String>> required`

            List of required property names.

          - `Optional<Type> type`

            Must be 'object' for tool input schemas.

            - `OBJECT("object")`

        - `String name`

        - `Type type`

          - `CUSTOM("custom")`

    - `Type type`

      - `AGENT("agent")`

    - `long version`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> parentThreadId`

    Parent thread that spawned this thread. Null for the primary thread.

  - `String sessionId`

    The session this thread belongs to.

  - `Optional<BetaManagedAgentsSessionThreadStats> stats`

    Timing statistics for a session thread.

    - `Optional<Double> activeSeconds`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `Optional<Double> durationSeconds`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `Optional<Double> startupSeconds`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `BetaManagedAgentsSessionThreadStatus status`

    SessionThreadStatus enum

    - `RUNNING("running")`

    - `IDLE("idle")`

    - `RESCHEDULING("rescheduling")`

    - `TERMINATED("terminated")`

  - `Type type`

    - `SESSION_THREAD("session_thread")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaManagedAgentsSessionThreadUsage> usage`

    Cumulative token usage for a session thread across all turns.

    - `Optional<BetaManagedAgentsCacheCreationUsage> cacheCreation`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Optional<Long> ephemeral1hInputTokens`

        Tokens used to create 1-hour ephemeral cache entries.

      - `Optional<Long> ephemeral5mInputTokens`

        Tokens used to create 5-minute ephemeral cache entries.

    - `Optional<Long> cacheReadInputTokens`

      Total tokens read from prompt cache.

    - `Optional<Long> inputTokens`

      Total input tokens consumed across all turns.

    - `Optional<Long> outputTokens`

      Total output tokens generated across all turns.

### Beta Managed Agents Session Thread Agent

- `class BetaManagedAgentsSessionThreadAgent:`

  Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

  - `String id`

  - `Optional<String> description`

  - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

    - `String name`

    - `Type type`

      - `URL("url")`

    - `String url`

  - `BetaManagedAgentsModelConfig model`

    Model identifier and configuration.

    - `BetaManagedAgentsModel id`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

        Frontier intelligence for long-running agents and coding

      - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

        Most intelligent model for building agents and coding

      - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

        Best combination of speed and intelligence

      - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

        Fastest model with near-frontier intelligence

      - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

        Fastest model with near-frontier intelligence

      - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

        Premium model combining maximum intelligence with practical performance

      - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

        Premium model combining maximum intelligence with practical performance

      - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

        High-performance model for agents and coding

      - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

        High-performance model for agents and coding

    - `Optional<Speed> speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `STANDARD("standard")`

      - `FAST("fast")`

  - `String name`

  - `List<Skill> skills`

    - `class BetaManagedAgentsAnthropicSkill:`

      A resolved Anthropic-managed skill.

      - `String skillId`

      - `Type type`

        - `ANTHROPIC("anthropic")`

      - `String version`

    - `class BetaManagedAgentsCustomSkill:`

      A resolved user-created custom skill.

      - `String skillId`

      - `Type type`

        - `CUSTOM("custom")`

      - `String version`

  - `Optional<String> system`

  - `List<Tool> tools`

    - `class BetaManagedAgentsAgentToolset20260401:`

      - `List<BetaManagedAgentsAgentToolConfig> configs`

        - `boolean enabled`

        - `Name name`

          Built-in agent tool identifier.

          - `BASH("bash")`

          - `EDIT("edit")`

          - `READ("read")`

          - `WRITE("write")`

          - `GLOB("glob")`

          - `GREP("grep")`

          - `WEB_FETCH("web_fetch")`

          - `WEB_SEARCH("web_search")`

        - `PermissionPolicy permissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy:`

            Tool calls are automatically approved without user confirmation.

            - `Type type`

              - `ALWAYS_ALLOW("always_allow")`

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

            - `Type type`

              - `ALWAYS_ASK("always_ask")`

      - `BetaManagedAgentsAgentToolsetDefaultConfig defaultConfig`

        Resolved default configuration for agent tools.

        - `boolean enabled`

        - `PermissionPolicy permissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy:`

            Tool calls are automatically approved without user confirmation.

            - `Type type`

              - `ALWAYS_ALLOW("always_allow")`

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

            - `Type type`

              - `ALWAYS_ASK("always_ask")`

      - `Type type`

        - `AGENT_TOOLSET_20260401("agent_toolset_20260401")`

    - `class BetaManagedAgentsMcpToolset:`

      - `List<BetaManagedAgentsMcpToolConfig> configs`

        - `boolean enabled`

        - `String name`

        - `PermissionPolicy permissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy:`

            Tool calls are automatically approved without user confirmation.

            - `Type type`

              - `ALWAYS_ALLOW("always_allow")`

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

            - `Type type`

              - `ALWAYS_ASK("always_ask")`

      - `BetaManagedAgentsMcpToolsetDefaultConfig defaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `boolean enabled`

        - `PermissionPolicy permissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy:`

            Tool calls are automatically approved without user confirmation.

            - `Type type`

              - `ALWAYS_ALLOW("always_allow")`

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

            - `Type type`

              - `ALWAYS_ASK("always_ask")`

      - `String mcpServerName`

      - `Type type`

        - `MCP_TOOLSET("mcp_toolset")`

    - `class BetaManagedAgentsCustomTool:`

      A custom tool as returned in API responses.

      - `String description`

      - `BetaManagedAgentsCustomToolInputSchema inputSchema`

        JSON Schema for custom tool input parameters.

        - `Optional<Properties> properties`

          JSON Schema properties defining the tool's input parameters.

        - `Optional<List<String>> required`

          List of required property names.

        - `Optional<Type> type`

          Must be 'object' for tool input schemas.

          - `OBJECT("object")`

      - `String name`

      - `Type type`

        - `CUSTOM("custom")`

  - `Type type`

    - `AGENT("agent")`

  - `long version`

### Beta Managed Agents Session Thread Stats

- `class BetaManagedAgentsSessionThreadStats:`

  Timing statistics for a session thread.

  - `Optional<Double> activeSeconds`

    Cumulative time in seconds the thread spent actively running. Excludes idle time.

  - `Optional<Double> durationSeconds`

    Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

  - `Optional<Double> startupSeconds`

    Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

### Beta Managed Agents Session Thread Status

- `enum BetaManagedAgentsSessionThreadStatus:`

  SessionThreadStatus enum

  - `RUNNING("running")`

  - `IDLE("idle")`

  - `RESCHEDULING("rescheduling")`

  - `TERMINATED("terminated")`

### Beta Managed Agents Session Thread Usage

- `class BetaManagedAgentsSessionThreadUsage:`

  Cumulative token usage for a session thread across all turns.

  - `Optional<BetaManagedAgentsCacheCreationUsage> cacheCreation`

    Prompt-cache creation token usage broken down by cache lifetime.

    - `Optional<Long> ephemeral1hInputTokens`

      Tokens used to create 1-hour ephemeral cache entries.

    - `Optional<Long> ephemeral5mInputTokens`

      Tokens used to create 5-minute ephemeral cache entries.

  - `Optional<Long> cacheReadInputTokens`

    Total tokens read from prompt cache.

  - `Optional<Long> inputTokens`

    Total input tokens consumed across all turns.

  - `Optional<Long> outputTokens`

    Total output tokens generated across all turns.

### Beta Managed Agents Stream Session Thread Events

- `class BetaManagedAgentsStreamSessionThreadEvents: A class that can be one of several variants.union`

  Server-sent event in a single thread's stream.

  - `class BetaManagedAgentsUserMessageEvent:`

    A user message event in the session conversation.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Type type`

      - `USER_MESSAGE("user.message")`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent:`

    An interrupt event that pauses agent execution and returns control to the user.

    - `String id`

      Unique identifier for this event.

    - `Type type`

      - `USER_INTERRUPT("user.interrupt")`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

    - `Optional<String> sessionThreadId`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent:`

    A tool confirmation event that approves or denies a pending tool execution.

    - `String id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

      - `ALLOW("allow")`

      - `DENY("deny")`

    - `String toolUseId`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

      - `USER_TOOL_CONFIRMATION("user.tool_confirmation")`

    - `Optional<String> denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

    - `Optional<String> sessionThreadId`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent:`

    Event sent by the client providing the result of a custom tool execution.

    - `String id`

      Unique identifier for this event.

    - `String customToolUseId`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

      - `USER_CUSTOM_TOOL_RESULT("user.custom_tool_result")`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

    - `Optional<String> sessionThreadId`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent:`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String name`

      Name of the custom tool being called.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_CUSTOM_TOOL_USE("agent.custom_tool_use")`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent:`

    An agent response event in the session conversation.

    - `String id`

      Unique identifier for this event.

    - `List<BetaManagedAgentsTextBlock> content`

      Array of text blocks comprising the agent response.

      - `String text`

        The text content.

      - `Type type`

        - `TEXT("text")`

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_MESSAGE("agent.message")`

  - `class BetaManagedAgentsAgentThinkingEvent:`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_THINKING("agent.thinking")`

  - `class BetaManagedAgentsAgentMcpToolUseEvent:`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String mcpServerName`

      Name of the MCP server providing the tool.

    - `String name`

      Name of the MCP tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_MCP_TOOL_USE("agent.mcp_tool_use")`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMcpToolResultEvent:`

    Event representing the result of an MCP tool execution.

    - `String id`

      Unique identifier for this event.

    - `String mcpToolUseId`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_MCP_TOOL_RESULT("agent.mcp_tool_result")`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent:`

    Event emitted when the agent invokes a built-in agent tool.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String name`

      Name of the agent tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_TOOL_USE("agent.tool_use")`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent:`

    Event representing the result of an agent tool execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String toolUseId`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type type`

      - `AGENT_TOOL_RESULT("agent.tool_result")`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent:`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `String fromSessionThreadId`

      Public `sthr_` ID of the thread that sent the message.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_THREAD_MESSAGE_RECEIVED("agent.thread_message_received")`

    - `Optional<String> fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent:`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String toSessionThreadId`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type type`

      - `AGENT_THREAD_MESSAGE_SENT("agent.thread_message_sent")`

    - `Optional<String> toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

    Indicates that context compaction (summarization) occurred during the session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_THREAD_CONTEXT_COMPACTED("agent.thread_context_compacted")`

  - `class BetaManagedAgentsSessionErrorEvent:`

    An error event indicating a problem occurred during session execution.

    - `String id`

      Unique identifier for this event.

    - `Error error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError:`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `UNKNOWN_ERROR("unknown_error")`

      - `class BetaManagedAgentsModelOverloadedError:`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MODEL_OVERLOADED_ERROR("model_overloaded_error")`

      - `class BetaManagedAgentsModelRateLimitedError:`

        The model request was rate-limited.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MODEL_RATE_LIMITED_ERROR("model_rate_limited_error")`

      - `class BetaManagedAgentsModelRequestFailedError:`

        A model request failed for a reason other than overload or rate-limiting.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MODEL_REQUEST_FAILED_ERROR("model_request_failed_error")`

      - `class BetaManagedAgentsMcpConnectionFailedError:`

        Failed to connect to an MCP server.

        - `String mcpServerName`

          Name of the MCP server that failed to connect.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MCP_CONNECTION_FAILED_ERROR("mcp_connection_failed_error")`

      - `class BetaManagedAgentsMcpAuthenticationFailedError:`

        Authentication to an MCP server failed.

        - `String mcpServerName`

          Name of the MCP server that failed authentication.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MCP_AUTHENTICATION_FAILED_ERROR("mcp_authentication_failed_error")`

      - `class BetaManagedAgentsBillingError:`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `BILLING_ERROR("billing_error")`

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_ERROR("session.error")`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_STATUS_RESCHEDULED("session.status_rescheduled")`

  - `class BetaManagedAgentsSessionStatusRunningEvent:`

    Indicates the session is actively running and the agent is working.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_STATUS_RUNNING("session.status_running")`

  - `class BetaManagedAgentsSessionStatusIdleEvent:`

    Indicates the agent has paused and is awaiting user input.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type type`

          - `END_TURN("end_turn")`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `List<String> eventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type type`

          - `REQUIRES_ACTION("requires_action")`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `Type type`

          - `RETRIES_EXHAUSTED("retries_exhausted")`

    - `Type type`

      - `SESSION_STATUS_IDLE("session.status_idle")`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

    Indicates the session has terminated, either due to an error or completion.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_STATUS_TERMINATED("session.status_terminated")`

  - `class BetaManagedAgentsSessionThreadCreatedEvent:`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the callable agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String sessionThreadId`

      Public `sthr_` ID of the newly created thread.

    - `Type type`

      - `SESSION_THREAD_CREATED("session.thread_created")`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:`

    Emitted when an outcome evaluation cycle begins.

    - `String id`

      Unique identifier for this event.

    - `long iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SPAN_OUTCOME_EVALUATION_START("span.outcome_evaluation_start")`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `String id`

      Unique identifier for this event.

    - `String explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `long iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `String outcomeEvaluationStartId`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type type`

      - `SPAN_OUTCOME_EVALUATION_END("span.outcome_evaluation_end")`

    - `BetaManagedAgentsSpanModelUsage usage`

      Token usage for a single model request.

      - `long cacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

      - `long cacheReadInputTokens`

        Tokens read from prompt cache in this request.

      - `long inputTokens`

        Input tokens consumed by this request.

      - `long outputTokens`

        Output tokens generated by this request.

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

  - `class BetaManagedAgentsSpanModelRequestStartEvent:`

    Emitted when a model request is initiated by the agent.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SPAN_MODEL_REQUEST_START("span.model_request_start")`

  - `class BetaManagedAgentsSpanModelRequestEndEvent:`

    Emitted when a model request completes.

    - `String id`

      Unique identifier for this event.

    - `Optional<Boolean> isError`

      Whether the model request resulted in an error.

    - `String modelRequestStartId`

      The id of the corresponding `span.model_request_start` event.

    - `BetaManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

      - `long cacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

      - `long cacheReadInputTokens`

        Tokens read from prompt cache in this request.

      - `long inputTokens`

        Input tokens consumed by this request.

      - `long outputTokens`

        Output tokens generated by this request.

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SPAN_MODEL_REQUEST_END("span.model_request_end")`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `String id`

      Unique identifier for this event.

    - `long iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SPAN_OUTCOME_EVALUATION_ONGOING("span.outcome_evaluation_ongoing")`

  - `class BetaManagedAgentsUserDefineOutcomeEvent:`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `String id`

      Unique identifier for this event.

    - `String description`

      What the agent should produce. Copied from the input event.

    - `Optional<Long> maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `String outcomeId`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric:`

        Rubric referenced by a file uploaded via the Files API.

        - `String fileId`

          ID of the rubric file.

        - `Type type`

          - `FILE("file")`

      - `class BetaManagedAgentsTextRubric:`

        Rubric content provided inline as text.

        - `String content`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `Type type`

          - `TEXT("text")`

    - `Type type`

      - `USER_DEFINE_OUTCOME("user.define_outcome")`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_DELETED("session.deleted")`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent:`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String sessionThreadId`

      Public sthr_ ID of the thread that started running.

    - `Type type`

      - `SESSION_THREAD_STATUS_RUNNING("session.thread_status_running")`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent:`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String sessionThreadId`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type type`

          - `END_TURN("end_turn")`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `List<String> eventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type type`

          - `REQUIRES_ACTION("requires_action")`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `Type type`

          - `RETRIES_EXHAUSTED("retries_exhausted")`

    - `Type type`

      - `SESSION_THREAD_STATUS_IDLE("session.thread_status_idle")`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent:`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String sessionThreadId`

      Public sthr_ ID of the thread that terminated.

    - `Type type`

      - `SESSION_THREAD_STATUS_TERMINATED("session.thread_status_terminated")`

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent:`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String sessionThreadId`

      Public sthr_ ID of the thread that is retrying.

    - `Type type`

      - `SESSION_THREAD_STATUS_RESCHEDULED("session.thread_status_rescheduled")`

# Events

## List

`EventListPage beta().sessions().threads().events().list(EventListParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/sessions/{session_id}/threads/{thread_id}/events`

List Session Thread Events

### Parameters

- `EventListParams params`

  - `String sessionId`

  - `Optional<String> threadId`

  - `Optional<Long> limit`

    Query parameter for limit

  - `Optional<String> page`

    Query parameter for page

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

### Returns

- `class BetaManagedAgentsSessionEvent: A class that can be one of several variants.union`

  Union type for all event types in a session.

  - `class BetaManagedAgentsUserMessageEvent:`

    A user message event in the session conversation.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Type type`

      - `USER_MESSAGE("user.message")`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent:`

    An interrupt event that pauses agent execution and returns control to the user.

    - `String id`

      Unique identifier for this event.

    - `Type type`

      - `USER_INTERRUPT("user.interrupt")`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

    - `Optional<String> sessionThreadId`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent:`

    A tool confirmation event that approves or denies a pending tool execution.

    - `String id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

      - `ALLOW("allow")`

      - `DENY("deny")`

    - `String toolUseId`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

      - `USER_TOOL_CONFIRMATION("user.tool_confirmation")`

    - `Optional<String> denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

    - `Optional<String> sessionThreadId`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent:`

    Event sent by the client providing the result of a custom tool execution.

    - `String id`

      Unique identifier for this event.

    - `String customToolUseId`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

      - `USER_CUSTOM_TOOL_RESULT("user.custom_tool_result")`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

    - `Optional<String> sessionThreadId`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent:`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String name`

      Name of the custom tool being called.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_CUSTOM_TOOL_USE("agent.custom_tool_use")`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent:`

    An agent response event in the session conversation.

    - `String id`

      Unique identifier for this event.

    - `List<BetaManagedAgentsTextBlock> content`

      Array of text blocks comprising the agent response.

      - `String text`

        The text content.

      - `Type type`

        - `TEXT("text")`

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_MESSAGE("agent.message")`

  - `class BetaManagedAgentsAgentThinkingEvent:`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_THINKING("agent.thinking")`

  - `class BetaManagedAgentsAgentMcpToolUseEvent:`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String mcpServerName`

      Name of the MCP server providing the tool.

    - `String name`

      Name of the MCP tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_MCP_TOOL_USE("agent.mcp_tool_use")`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMcpToolResultEvent:`

    Event representing the result of an MCP tool execution.

    - `String id`

      Unique identifier for this event.

    - `String mcpToolUseId`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_MCP_TOOL_RESULT("agent.mcp_tool_result")`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent:`

    Event emitted when the agent invokes a built-in agent tool.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String name`

      Name of the agent tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_TOOL_USE("agent.tool_use")`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent:`

    Event representing the result of an agent tool execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String toolUseId`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type type`

      - `AGENT_TOOL_RESULT("agent.tool_result")`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent:`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `String fromSessionThreadId`

      Public `sthr_` ID of the thread that sent the message.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_THREAD_MESSAGE_RECEIVED("agent.thread_message_received")`

    - `Optional<String> fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent:`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String toSessionThreadId`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type type`

      - `AGENT_THREAD_MESSAGE_SENT("agent.thread_message_sent")`

    - `Optional<String> toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

    Indicates that context compaction (summarization) occurred during the session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_THREAD_CONTEXT_COMPACTED("agent.thread_context_compacted")`

  - `class BetaManagedAgentsSessionErrorEvent:`

    An error event indicating a problem occurred during session execution.

    - `String id`

      Unique identifier for this event.

    - `Error error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError:`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `UNKNOWN_ERROR("unknown_error")`

      - `class BetaManagedAgentsModelOverloadedError:`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MODEL_OVERLOADED_ERROR("model_overloaded_error")`

      - `class BetaManagedAgentsModelRateLimitedError:`

        The model request was rate-limited.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MODEL_RATE_LIMITED_ERROR("model_rate_limited_error")`

      - `class BetaManagedAgentsModelRequestFailedError:`

        A model request failed for a reason other than overload or rate-limiting.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MODEL_REQUEST_FAILED_ERROR("model_request_failed_error")`

      - `class BetaManagedAgentsMcpConnectionFailedError:`

        Failed to connect to an MCP server.

        - `String mcpServerName`

          Name of the MCP server that failed to connect.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MCP_CONNECTION_FAILED_ERROR("mcp_connection_failed_error")`

      - `class BetaManagedAgentsMcpAuthenticationFailedError:`

        Authentication to an MCP server failed.

        - `String mcpServerName`

          Name of the MCP server that failed authentication.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MCP_AUTHENTICATION_FAILED_ERROR("mcp_authentication_failed_error")`

      - `class BetaManagedAgentsBillingError:`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `BILLING_ERROR("billing_error")`

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_ERROR("session.error")`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_STATUS_RESCHEDULED("session.status_rescheduled")`

  - `class BetaManagedAgentsSessionStatusRunningEvent:`

    Indicates the session is actively running and the agent is working.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_STATUS_RUNNING("session.status_running")`

  - `class BetaManagedAgentsSessionStatusIdleEvent:`

    Indicates the agent has paused and is awaiting user input.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type type`

          - `END_TURN("end_turn")`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `List<String> eventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type type`

          - `REQUIRES_ACTION("requires_action")`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `Type type`

          - `RETRIES_EXHAUSTED("retries_exhausted")`

    - `Type type`

      - `SESSION_STATUS_IDLE("session.status_idle")`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

    Indicates the session has terminated, either due to an error or completion.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_STATUS_TERMINATED("session.status_terminated")`

  - `class BetaManagedAgentsSessionThreadCreatedEvent:`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the callable agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String sessionThreadId`

      Public `sthr_` ID of the newly created thread.

    - `Type type`

      - `SESSION_THREAD_CREATED("session.thread_created")`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:`

    Emitted when an outcome evaluation cycle begins.

    - `String id`

      Unique identifier for this event.

    - `long iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SPAN_OUTCOME_EVALUATION_START("span.outcome_evaluation_start")`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `String id`

      Unique identifier for this event.

    - `String explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `long iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `String outcomeEvaluationStartId`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type type`

      - `SPAN_OUTCOME_EVALUATION_END("span.outcome_evaluation_end")`

    - `BetaManagedAgentsSpanModelUsage usage`

      Token usage for a single model request.

      - `long cacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

      - `long cacheReadInputTokens`

        Tokens read from prompt cache in this request.

      - `long inputTokens`

        Input tokens consumed by this request.

      - `long outputTokens`

        Output tokens generated by this request.

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

  - `class BetaManagedAgentsSpanModelRequestStartEvent:`

    Emitted when a model request is initiated by the agent.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SPAN_MODEL_REQUEST_START("span.model_request_start")`

  - `class BetaManagedAgentsSpanModelRequestEndEvent:`

    Emitted when a model request completes.

    - `String id`

      Unique identifier for this event.

    - `Optional<Boolean> isError`

      Whether the model request resulted in an error.

    - `String modelRequestStartId`

      The id of the corresponding `span.model_request_start` event.

    - `BetaManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

      - `long cacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

      - `long cacheReadInputTokens`

        Tokens read from prompt cache in this request.

      - `long inputTokens`

        Input tokens consumed by this request.

      - `long outputTokens`

        Output tokens generated by this request.

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SPAN_MODEL_REQUEST_END("span.model_request_end")`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `String id`

      Unique identifier for this event.

    - `long iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SPAN_OUTCOME_EVALUATION_ONGOING("span.outcome_evaluation_ongoing")`

  - `class BetaManagedAgentsUserDefineOutcomeEvent:`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `String id`

      Unique identifier for this event.

    - `String description`

      What the agent should produce. Copied from the input event.

    - `Optional<Long> maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `String outcomeId`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric:`

        Rubric referenced by a file uploaded via the Files API.

        - `String fileId`

          ID of the rubric file.

        - `Type type`

          - `FILE("file")`

      - `class BetaManagedAgentsTextRubric:`

        Rubric content provided inline as text.

        - `String content`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `Type type`

          - `TEXT("text")`

    - `Type type`

      - `USER_DEFINE_OUTCOME("user.define_outcome")`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_DELETED("session.deleted")`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent:`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String sessionThreadId`

      Public sthr_ ID of the thread that started running.

    - `Type type`

      - `SESSION_THREAD_STATUS_RUNNING("session.thread_status_running")`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent:`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String sessionThreadId`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type type`

          - `END_TURN("end_turn")`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `List<String> eventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type type`

          - `REQUIRES_ACTION("requires_action")`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `Type type`

          - `RETRIES_EXHAUSTED("retries_exhausted")`

    - `Type type`

      - `SESSION_THREAD_STATUS_IDLE("session.thread_status_idle")`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent:`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String sessionThreadId`

      Public sthr_ ID of the thread that terminated.

    - `Type type`

      - `SESSION_THREAD_STATUS_TERMINATED("session.thread_status_terminated")`

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent:`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String sessionThreadId`

      Public sthr_ ID of the thread that is retrying.

    - `Type type`

      - `SESSION_THREAD_STATUS_RESCHEDULED("session.thread_status_rescheduled")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.threads.events.EventListPage;
import com.anthropic.models.beta.sessions.threads.events.EventListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        EventListParams params = EventListParams.builder()
            .sessionId("sesn_011CZkZAtmR3yMPDzynEDxu7")
            .threadId("sthr_011CZkZVWa6oIjw0rgXZpnBt")
            .build();
        EventListPage page = client.beta().sessions().threads().events().list(params);
    }
}
```

## Stream

`BetaManagedAgentsStreamSessionThreadEvents beta().sessions().threads().events().streamStreaming(EventStreamParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/sessions/{session_id}/threads/{thread_id}/stream`

Stream Session Thread Events

### Parameters

- `EventStreamParams params`

  - `String sessionId`

  - `Optional<String> threadId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

### Returns

- `class BetaManagedAgentsStreamSessionThreadEvents: A class that can be one of several variants.union`

  Server-sent event in a single thread's stream.

  - `class BetaManagedAgentsUserMessageEvent:`

    A user message event in the session conversation.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Type type`

      - `USER_MESSAGE("user.message")`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent:`

    An interrupt event that pauses agent execution and returns control to the user.

    - `String id`

      Unique identifier for this event.

    - `Type type`

      - `USER_INTERRUPT("user.interrupt")`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

    - `Optional<String> sessionThreadId`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent:`

    A tool confirmation event that approves or denies a pending tool execution.

    - `String id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

      - `ALLOW("allow")`

      - `DENY("deny")`

    - `String toolUseId`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

      - `USER_TOOL_CONFIRMATION("user.tool_confirmation")`

    - `Optional<String> denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

    - `Optional<String> sessionThreadId`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent:`

    Event sent by the client providing the result of a custom tool execution.

    - `String id`

      Unique identifier for this event.

    - `String customToolUseId`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

      - `USER_CUSTOM_TOOL_RESULT("user.custom_tool_result")`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

    - `Optional<String> sessionThreadId`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent:`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String name`

      Name of the custom tool being called.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_CUSTOM_TOOL_USE("agent.custom_tool_use")`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent:`

    An agent response event in the session conversation.

    - `String id`

      Unique identifier for this event.

    - `List<BetaManagedAgentsTextBlock> content`

      Array of text blocks comprising the agent response.

      - `String text`

        The text content.

      - `Type type`

        - `TEXT("text")`

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_MESSAGE("agent.message")`

  - `class BetaManagedAgentsAgentThinkingEvent:`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_THINKING("agent.thinking")`

  - `class BetaManagedAgentsAgentMcpToolUseEvent:`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String mcpServerName`

      Name of the MCP server providing the tool.

    - `String name`

      Name of the MCP tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_MCP_TOOL_USE("agent.mcp_tool_use")`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMcpToolResultEvent:`

    Event representing the result of an MCP tool execution.

    - `String id`

      Unique identifier for this event.

    - `String mcpToolUseId`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_MCP_TOOL_RESULT("agent.mcp_tool_result")`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent:`

    Event emitted when the agent invokes a built-in agent tool.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String name`

      Name of the agent tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_TOOL_USE("agent.tool_use")`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent:`

    Event representing the result of an agent tool execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String toolUseId`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type type`

      - `AGENT_TOOL_RESULT("agent.tool_result")`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent:`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `String fromSessionThreadId`

      Public `sthr_` ID of the thread that sent the message.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_THREAD_MESSAGE_RECEIVED("agent.thread_message_received")`

    - `Optional<String> fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent:`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String toSessionThreadId`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type type`

      - `AGENT_THREAD_MESSAGE_SENT("agent.thread_message_sent")`

    - `Optional<String> toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

    Indicates that context compaction (summarization) occurred during the session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_THREAD_CONTEXT_COMPACTED("agent.thread_context_compacted")`

  - `class BetaManagedAgentsSessionErrorEvent:`

    An error event indicating a problem occurred during session execution.

    - `String id`

      Unique identifier for this event.

    - `Error error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError:`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `UNKNOWN_ERROR("unknown_error")`

      - `class BetaManagedAgentsModelOverloadedError:`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MODEL_OVERLOADED_ERROR("model_overloaded_error")`

      - `class BetaManagedAgentsModelRateLimitedError:`

        The model request was rate-limited.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MODEL_RATE_LIMITED_ERROR("model_rate_limited_error")`

      - `class BetaManagedAgentsModelRequestFailedError:`

        A model request failed for a reason other than overload or rate-limiting.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MODEL_REQUEST_FAILED_ERROR("model_request_failed_error")`

      - `class BetaManagedAgentsMcpConnectionFailedError:`

        Failed to connect to an MCP server.

        - `String mcpServerName`

          Name of the MCP server that failed to connect.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MCP_CONNECTION_FAILED_ERROR("mcp_connection_failed_error")`

      - `class BetaManagedAgentsMcpAuthenticationFailedError:`

        Authentication to an MCP server failed.

        - `String mcpServerName`

          Name of the MCP server that failed authentication.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MCP_AUTHENTICATION_FAILED_ERROR("mcp_authentication_failed_error")`

      - `class BetaManagedAgentsBillingError:`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `BILLING_ERROR("billing_error")`

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_ERROR("session.error")`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_STATUS_RESCHEDULED("session.status_rescheduled")`

  - `class BetaManagedAgentsSessionStatusRunningEvent:`

    Indicates the session is actively running and the agent is working.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_STATUS_RUNNING("session.status_running")`

  - `class BetaManagedAgentsSessionStatusIdleEvent:`

    Indicates the agent has paused and is awaiting user input.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type type`

          - `END_TURN("end_turn")`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `List<String> eventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type type`

          - `REQUIRES_ACTION("requires_action")`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `Type type`

          - `RETRIES_EXHAUSTED("retries_exhausted")`

    - `Type type`

      - `SESSION_STATUS_IDLE("session.status_idle")`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

    Indicates the session has terminated, either due to an error or completion.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_STATUS_TERMINATED("session.status_terminated")`

  - `class BetaManagedAgentsSessionThreadCreatedEvent:`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the callable agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String sessionThreadId`

      Public `sthr_` ID of the newly created thread.

    - `Type type`

      - `SESSION_THREAD_CREATED("session.thread_created")`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:`

    Emitted when an outcome evaluation cycle begins.

    - `String id`

      Unique identifier for this event.

    - `long iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SPAN_OUTCOME_EVALUATION_START("span.outcome_evaluation_start")`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `String id`

      Unique identifier for this event.

    - `String explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `long iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `String outcomeEvaluationStartId`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type type`

      - `SPAN_OUTCOME_EVALUATION_END("span.outcome_evaluation_end")`

    - `BetaManagedAgentsSpanModelUsage usage`

      Token usage for a single model request.

      - `long cacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

      - `long cacheReadInputTokens`

        Tokens read from prompt cache in this request.

      - `long inputTokens`

        Input tokens consumed by this request.

      - `long outputTokens`

        Output tokens generated by this request.

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

  - `class BetaManagedAgentsSpanModelRequestStartEvent:`

    Emitted when a model request is initiated by the agent.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SPAN_MODEL_REQUEST_START("span.model_request_start")`

  - `class BetaManagedAgentsSpanModelRequestEndEvent:`

    Emitted when a model request completes.

    - `String id`

      Unique identifier for this event.

    - `Optional<Boolean> isError`

      Whether the model request resulted in an error.

    - `String modelRequestStartId`

      The id of the corresponding `span.model_request_start` event.

    - `BetaManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

      - `long cacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

      - `long cacheReadInputTokens`

        Tokens read from prompt cache in this request.

      - `long inputTokens`

        Input tokens consumed by this request.

      - `long outputTokens`

        Output tokens generated by this request.

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SPAN_MODEL_REQUEST_END("span.model_request_end")`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `String id`

      Unique identifier for this event.

    - `long iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SPAN_OUTCOME_EVALUATION_ONGOING("span.outcome_evaluation_ongoing")`

  - `class BetaManagedAgentsUserDefineOutcomeEvent:`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `String id`

      Unique identifier for this event.

    - `String description`

      What the agent should produce. Copied from the input event.

    - `Optional<Long> maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `String outcomeId`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric:`

        Rubric referenced by a file uploaded via the Files API.

        - `String fileId`

          ID of the rubric file.

        - `Type type`

          - `FILE("file")`

      - `class BetaManagedAgentsTextRubric:`

        Rubric content provided inline as text.

        - `String content`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `Type type`

          - `TEXT("text")`

    - `Type type`

      - `USER_DEFINE_OUTCOME("user.define_outcome")`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_DELETED("session.deleted")`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent:`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String sessionThreadId`

      Public sthr_ ID of the thread that started running.

    - `Type type`

      - `SESSION_THREAD_STATUS_RUNNING("session.thread_status_running")`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent:`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String sessionThreadId`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type type`

          - `END_TURN("end_turn")`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `List<String> eventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type type`

          - `REQUIRES_ACTION("requires_action")`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `Type type`

          - `RETRIES_EXHAUSTED("retries_exhausted")`

    - `Type type`

      - `SESSION_THREAD_STATUS_IDLE("session.thread_status_idle")`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent:`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String sessionThreadId`

      Public sthr_ ID of the thread that terminated.

    - `Type type`

      - `SESSION_THREAD_STATUS_TERMINATED("session.thread_status_terminated")`

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent:`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String sessionThreadId`

      Public sthr_ ID of the thread that is retrying.

    - `Type type`

      - `SESSION_THREAD_STATUS_RESCHEDULED("session.thread_status_rescheduled")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.http.StreamResponse;
import com.anthropic.models.beta.sessions.threads.BetaManagedAgentsStreamSessionThreadEvents;
import com.anthropic.models.beta.sessions.threads.events.EventStreamParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        EventStreamParams params = EventStreamParams.builder()
            .sessionId("sesn_011CZkZAtmR3yMPDzynEDxu7")
            .threadId("sthr_011CZkZVWa6oIjw0rgXZpnBt")
            .build();
        StreamResponse<BetaManagedAgentsStreamSessionThreadEvents> betaManagedAgentsStreamSessionThreadEvents = client.beta().sessions().threads().events().streamStreaming(params);
    }
}
```
