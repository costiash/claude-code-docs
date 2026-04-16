## Create

`BetaManagedAgentsSession beta().sessions().create(SessionCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/sessions`

Create Session

### Parameters

- `SessionCreateParams params`

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

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

  - `Agent agent`

    Agent identifier. Accepts the `agent` ID string, which pins the latest version for the session, or an `agent` object with both id and version specified.

    - `String`

    - `class BetaManagedAgentsAgentParams:`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `String id`

        The `agent` ID.

      - `Type type`

        - `AGENT("agent")`

      - `Optional<Long> version`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

  - `String environmentId`

    ID of the `environment` defining the container configuration for this session.

  - `Optional<Metadata> metadata`

    Arbitrary key-value metadata attached to the session. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `Optional<List<Resource>> resources`

    Resources (e.g. repositories, files) to mount into the session's container.

    - `class BetaManagedAgentsGitHubRepositoryResourceParams:`

      Mount a GitHub repository into the session's container.

      - `String authorizationToken`

        GitHub authorization token used to clone the repository.

      - `Type type`

        - `GITHUB_REPOSITORY("github_repository")`

      - `String url`

        Github URL of the repository

      - `Optional<Checkout> checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `String name`

            Branch name to check out.

          - `Type type`

            - `BRANCH("branch")`

        - `class BetaManagedAgentsCommitCheckout:`

          - `String sha`

            Full commit SHA to check out.

          - `Type type`

            - `COMMIT("commit")`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceParams:`

      Mount a file uploaded via the Files API into the session.

      - `String fileId`

        ID of a previously uploaded file.

      - `Type type`

        - `FILE("file")`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  - `Optional<String> title`

    Human-readable session title.

  - `Optional<List<String>> vaultIds`

    Vault IDs for stored credentials the agent can use during the session.

### Returns

- `class BetaManagedAgentsSession:`

  A Managed Agents `session`.

  - `String id`

  - `BetaManagedAgentsSessionAgent agent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

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

  - `String environmentId`

  - `Metadata metadata`

  - `List<BetaManagedAgentsSessionResource> resources`

    - `class BetaManagedAgentsGitHubRepositoryResource:`

      - `String id`

      - `LocalDateTime createdAt`

        A timestamp in RFC 3339 format

      - `String mountPath`

      - `Type type`

        - `GITHUB_REPOSITORY("github_repository")`

      - `LocalDateTime updatedAt`

        A timestamp in RFC 3339 format

      - `String url`

      - `Optional<Checkout> checkout`

        - `class BetaManagedAgentsBranchCheckout:`

          - `String name`

            Branch name to check out.

          - `Type type`

            - `BRANCH("branch")`

        - `class BetaManagedAgentsCommitCheckout:`

          - `String sha`

            Full commit SHA to check out.

          - `Type type`

            - `COMMIT("commit")`

    - `class BetaManagedAgentsFileResource:`

      - `String id`

      - `LocalDateTime createdAt`

        A timestamp in RFC 3339 format

      - `String fileId`

      - `String mountPath`

      - `Type type`

        - `FILE("file")`

      - `LocalDateTime updatedAt`

        A timestamp in RFC 3339 format

  - `BetaManagedAgentsSessionStats stats`

    Timing statistics for a session.

    - `Optional<Double> activeSeconds`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

    - `Optional<Double> durationSeconds`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

  - `Status status`

    SessionStatus enum

    - `RESCHEDULING("rescheduling")`

    - `RUNNING("running")`

    - `IDLE("idle")`

    - `TERMINATED("terminated")`

  - `Optional<String> title`

  - `Type type`

    - `SESSION("session")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `BetaManagedAgentsSessionUsage usage`

    Cumulative token usage for a session across all turns.

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

  - `List<String> vaultIds`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.BetaManagedAgentsSession;
import com.anthropic.models.beta.sessions.SessionCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        SessionCreateParams params = SessionCreateParams.builder()
            .agent("agent_011CZkYpogX7uDKUyvBTophP")
            .environmentId("env_011CZkZ9X2dpNyB7HsEFoRfW")
            .build();
        BetaManagedAgentsSession betaManagedAgentsSession = client.beta().sessions().create(params);
    }
}
```
