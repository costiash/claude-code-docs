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
