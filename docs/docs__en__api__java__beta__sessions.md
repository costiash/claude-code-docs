# Sessions

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

## List

`SessionListPage beta().sessions().list(SessionListParamsparams = SessionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/sessions`

List Sessions

### Parameters

- `SessionListParams params`

  - `Optional<String> agentId`

    Filter sessions created with this agent ID.

  - `Optional<Long> agentVersion`

    Filter by agent version. Only applies when agent_id is also set.

  - `Optional<LocalDateTime> createdAtGt`

    Return sessions created after this time (exclusive).

  - `Optional<LocalDateTime> createdAtGte`

    Return sessions created at or after this time (inclusive).

  - `Optional<LocalDateTime> createdAtLt`

    Return sessions created before this time (exclusive).

  - `Optional<LocalDateTime> createdAtLte`

    Return sessions created at or before this time (inclusive).

  - `Optional<Boolean> includeArchived`

    When true, includes archived sessions. Default: false (exclude archived).

  - `Optional<Long> limit`

    Maximum number of results to return.

  - `Optional<Order> order`

    Sort direction for results, ordered by created_at. Defaults to desc (newest first).

    - `ASC("asc")`

    - `DESC("desc")`

  - `Optional<String> page`

    Opaque pagination cursor from a previous response's next_page.

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
import com.anthropic.models.beta.sessions.SessionListPage;
import com.anthropic.models.beta.sessions.SessionListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        SessionListPage page = client.beta().sessions().list();
    }
}
```

## Retrieve

`BetaManagedAgentsSession beta().sessions().retrieve(SessionRetrieveParamsparams = SessionRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/sessions/{session_id}`

Get Session

### Parameters

- `SessionRetrieveParams params`

  - `Optional<String> sessionId`

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
import com.anthropic.models.beta.sessions.SessionRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsSession betaManagedAgentsSession = client.beta().sessions().retrieve("sesn_011CZkZAtmR3yMPDzynEDxu7");
    }
}
```

## Update

`BetaManagedAgentsSession beta().sessions().update(SessionUpdateParamsparams = SessionUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/sessions/{session_id}`

Update Session

### Parameters

- `SessionUpdateParams params`

  - `Optional<String> sessionId`

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

  - `Optional<Metadata> metadata`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve.

  - `Optional<String> title`

    Human-readable session title.

  - `Optional<List<String>> vaultIds`

    Vault IDs (`vlt_*`) to attach to the session. Not yet supported; requests setting this field are rejected. Reserved for future use.

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
import com.anthropic.models.beta.sessions.SessionUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsSession betaManagedAgentsSession = client.beta().sessions().update("sesn_011CZkZAtmR3yMPDzynEDxu7");
    }
}
```

## Delete

`BetaManagedAgentsDeletedSession beta().sessions().delete(SessionDeleteParamsparams = SessionDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/v1/sessions/{session_id}`

Delete Session

### Parameters

- `SessionDeleteParams params`

  - `Optional<String> sessionId`

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

### Returns

- `class BetaManagedAgentsDeletedSession:`

  Confirmation that a `session` has been permanently deleted.

  - `String id`

  - `Type type`

    - `SESSION_DELETED("session_deleted")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.BetaManagedAgentsDeletedSession;
import com.anthropic.models.beta.sessions.SessionDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsDeletedSession betaManagedAgentsDeletedSession = client.beta().sessions().delete("sesn_011CZkZAtmR3yMPDzynEDxu7");
    }
}
```

## Archive

`BetaManagedAgentsSession beta().sessions().archive(SessionArchiveParamsparams = SessionArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/sessions/{session_id}/archive`

Archive Session

### Parameters

- `SessionArchiveParams params`

  - `Optional<String> sessionId`

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
import com.anthropic.models.beta.sessions.SessionArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsSession betaManagedAgentsSession = client.beta().sessions().archive("sesn_011CZkZAtmR3yMPDzynEDxu7");
    }
}
```

## Domain Types

### Beta Managed Agents Agent Params

- `class BetaManagedAgentsAgentParams:`

  Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

  - `String id`

    The `agent` ID.

  - `Type type`

    - `AGENT("agent")`

  - `Optional<Long> version`

    The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

### Beta Managed Agents Branch Checkout

- `class BetaManagedAgentsBranchCheckout:`

  - `String name`

    Branch name to check out.

  - `Type type`

    - `BRANCH("branch")`

### Beta Managed Agents Cache Creation Usage

- `class BetaManagedAgentsCacheCreationUsage:`

  Prompt-cache creation token usage broken down by cache lifetime.

  - `Optional<Long> ephemeral1hInputTokens`

    Tokens used to create 1-hour ephemeral cache entries.

  - `Optional<Long> ephemeral5mInputTokens`

    Tokens used to create 5-minute ephemeral cache entries.

### Beta Managed Agents Commit Checkout

- `class BetaManagedAgentsCommitCheckout:`

  - `String sha`

    Full commit SHA to check out.

  - `Type type`

    - `COMMIT("commit")`

### Beta Managed Agents Deleted Session

- `class BetaManagedAgentsDeletedSession:`

  Confirmation that a `session` has been permanently deleted.

  - `String id`

  - `Type type`

    - `SESSION_DELETED("session_deleted")`

### Beta Managed Agents File Resource Params

- `class BetaManagedAgentsFileResourceParams:`

  Mount a file uploaded via the Files API into the session.

  - `String fileId`

    ID of a previously uploaded file.

  - `Type type`

    - `FILE("file")`

  - `Optional<String> mountPath`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

### Beta Managed Agents GitHub Repository Resource Params

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

### Beta Managed Agents Session

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

### Beta Managed Agents Session Agent

- `class BetaManagedAgentsSessionAgent:`

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

### Beta Managed Agents Session Stats

- `class BetaManagedAgentsSessionStats:`

  Timing statistics for a session.

  - `Optional<Double> activeSeconds`

    Cumulative time in seconds the session spent in running status. Excludes idle time.

  - `Optional<Double> durationSeconds`

    Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

### Beta Managed Agents Session Usage

- `class BetaManagedAgentsSessionUsage:`

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

# Events

## List

`EventListPage beta().sessions().events().list(EventListParamsparams = EventListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/sessions/{session_id}/events`

List Events

### Parameters

- `EventListParams params`

  - `Optional<String> sessionId`

  - `Optional<Long> limit`

    Query parameter for limit

  - `Optional<Order> order`

    Sort direction for results, ordered by created_at. Defaults to asc (chronological).

    - `ASC("asc")`

    - `DESC("desc")`

  - `Optional<String> page`

    Opaque pagination cursor from a previous response's next_page.

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

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_DELETED("session.deleted")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.events.EventListPage;
import com.anthropic.models.beta.sessions.events.EventListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        EventListPage page = client.beta().sessions().events().list("sesn_011CZkZAtmR3yMPDzynEDxu7");
    }
}
```

## Send

`BetaManagedAgentsSendSessionEvents beta().sessions().events().send(EventSendParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/sessions/{session_id}/events`

Send Events

### Parameters

- `EventSendParams params`

  - `Optional<String> sessionId`

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

  - `List<BetaManagedAgentsEventParams> events`

    Events to send to the `session`.

    - `class BetaManagedAgentsUserMessageEventParams:`

      Parameters for sending a user message to the session.

      - `List<Content> content`

        Array of content blocks for the user message.

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

    - `class BetaManagedAgentsUserInterruptEventParams:`

      Parameters for sending an interrupt to pause the agent.

      - `Type type`

        - `USER_INTERRUPT("user.interrupt")`

    - `class BetaManagedAgentsUserToolConfirmationEventParams:`

      Parameters for confirming or denying a tool execution request.

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

    - `class BetaManagedAgentsUserCustomToolResultEventParams:`

      Parameters for providing the result of a custom tool execution.

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

### Returns

- `class BetaManagedAgentsSendSessionEvents:`

  Events that were successfully sent to the session.

  - `Optional<List<Data>> data`

    Sent events

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

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.events.BetaManagedAgentsSendSessionEvents;
import com.anthropic.models.beta.sessions.events.BetaManagedAgentsTextBlock;
import com.anthropic.models.beta.sessions.events.BetaManagedAgentsUserMessageEventParams;
import com.anthropic.models.beta.sessions.events.EventSendParams;
import java.util.List;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        EventSendParams params = EventSendParams.builder()
            .sessionId("sesn_011CZkZAtmR3yMPDzynEDxu7")
            .addUserMessageEvent(List.of(BetaManagedAgentsUserMessageEventParams.Content.ofText(BetaManagedAgentsTextBlock.builder()
                .text("Where is my order #1234?")
                .type(BetaManagedAgentsTextBlock.Type.TEXT)
                .build())))
            .build();
        BetaManagedAgentsSendSessionEvents betaManagedAgentsSendSessionEvents = client.beta().sessions().events().send(params);
    }
}
```

## Stream

`BetaManagedAgentsStreamSessionEvents beta().sessions().events().streamStreaming(EventStreamParamsparams = EventStreamParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/sessions/{session_id}/events/stream`

Stream Events

### Parameters

- `EventStreamParams params`

  - `Optional<String> sessionId`

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

### Returns

- `class BetaManagedAgentsStreamSessionEvents: A class that can be one of several variants.union`

  Server-sent event in the session stream.

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

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_DELETED("session.deleted")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.http.StreamResponse;
import com.anthropic.models.beta.sessions.events.BetaManagedAgentsStreamSessionEvents;
import com.anthropic.models.beta.sessions.events.EventStreamParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        StreamResponse<BetaManagedAgentsStreamSessionEvents> betaManagedAgentsStreamSessionEvents = client.beta().sessions().events().streamStreaming("sesn_011CZkZAtmR3yMPDzynEDxu7");
    }
}
```

## Domain Types

### Beta Managed Agents Agent Custom Tool Use Event

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

### Beta Managed Agents Agent MCP Tool Result Event

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

### Beta Managed Agents Agent MCP Tool Use Event

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

### Beta Managed Agents Agent Message Event

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

### Beta Managed Agents Agent Thinking Event

- `class BetaManagedAgentsAgentThinkingEvent:`

  Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

  - `String id`

    Unique identifier for this event.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

    - `AGENT_THINKING("agent.thinking")`

### Beta Managed Agents Agent Thread Context Compacted Event

- `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

  Indicates that context compaction (summarization) occurred during the session.

  - `String id`

    Unique identifier for this event.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

    - `AGENT_THREAD_CONTEXT_COMPACTED("agent.thread_context_compacted")`

### Beta Managed Agents Agent Tool Result Event

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

### Beta Managed Agents Agent Tool Use Event

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

### Beta Managed Agents Base64 Document Source

- `class BetaManagedAgentsBase64DocumentSource:`

  Base64-encoded document data.

  - `String data`

    Base64-encoded document data.

  - `String mediaType`

    MIME type of the document (e.g., "application/pdf").

  - `Type type`

    - `BASE64("base64")`

### Beta Managed Agents Base64 Image Source

- `class BetaManagedAgentsBase64ImageSource:`

  Base64-encoded image data.

  - `String data`

    Base64-encoded image data.

  - `String mediaType`

    MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

  - `Type type`

    - `BASE64("base64")`

### Beta Managed Agents Billing Error

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

### Beta Managed Agents Document Block

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

### Beta Managed Agents Event Params

- `class BetaManagedAgentsEventParams: A class that can be one of several variants.union`

  Union type for event parameters that can be sent to a session.

  - `class BetaManagedAgentsUserMessageEventParams:`

    Parameters for sending a user message to the session.

    - `List<Content> content`

      Array of content blocks for the user message.

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

  - `class BetaManagedAgentsUserInterruptEventParams:`

    Parameters for sending an interrupt to pause the agent.

    - `Type type`

      - `USER_INTERRUPT("user.interrupt")`

  - `class BetaManagedAgentsUserToolConfirmationEventParams:`

    Parameters for confirming or denying a tool execution request.

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

  - `class BetaManagedAgentsUserCustomToolResultEventParams:`

    Parameters for providing the result of a custom tool execution.

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

### Beta Managed Agents File Document Source

- `class BetaManagedAgentsFileDocumentSource:`

  Document referenced by file ID.

  - `String fileId`

    ID of a previously uploaded file.

  - `Type type`

    - `FILE("file")`

### Beta Managed Agents File Image Source

- `class BetaManagedAgentsFileImageSource:`

  Image referenced by file ID.

  - `String fileId`

    ID of a previously uploaded file.

  - `Type type`

    - `FILE("file")`

### Beta Managed Agents Image Block

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

### Beta Managed Agents MCP Authentication Failed Error

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

### Beta Managed Agents MCP Connection Failed Error

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

### Beta Managed Agents Model Overloaded Error

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

### Beta Managed Agents Model Rate Limited Error

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

### Beta Managed Agents Model Request Failed Error

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

### Beta Managed Agents Plain Text Document Source

- `class BetaManagedAgentsPlainTextDocumentSource:`

  Plain text document content.

  - `String data`

    The plain text content.

  - `MediaType mediaType`

    MIME type of the text content. Must be "text/plain".

    - `TEXT_PLAIN("text/plain")`

  - `Type type`

    - `TEXT("text")`

### Beta Managed Agents Retry Status Exhausted

- `class BetaManagedAgentsRetryStatusExhausted:`

  This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

  - `Type type`

    - `EXHAUSTED("exhausted")`

### Beta Managed Agents Retry Status Retrying

- `class BetaManagedAgentsRetryStatusRetrying:`

  The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

  - `Type type`

    - `RETRYING("retrying")`

### Beta Managed Agents Retry Status Terminal

- `class BetaManagedAgentsRetryStatusTerminal:`

  The session encountered a terminal error and will transition to `terminated` state.

  - `Type type`

    - `TERMINAL("terminal")`

### Beta Managed Agents Send Session Events

- `class BetaManagedAgentsSendSessionEvents:`

  Events that were successfully sent to the session.

  - `Optional<List<Data>> data`

    Sent events

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

### Beta Managed Agents Session Deleted Event

- `class BetaManagedAgentsSessionDeletedEvent:`

  Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

  - `String id`

    Unique identifier for this event.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

    - `SESSION_DELETED("session.deleted")`

### Beta Managed Agents Session End Turn

- `class BetaManagedAgentsSessionEndTurn:`

  The agent completed its turn naturally and is ready for the next user message.

  - `Type type`

    - `END_TURN("end_turn")`

### Beta Managed Agents Session Error Event

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

### Beta Managed Agents Session Event

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

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_DELETED("session.deleted")`

### Beta Managed Agents Session Requires Action

- `class BetaManagedAgentsSessionRequiresAction:`

  The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

  - `List<String> eventIds`

    The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

  - `Type type`

    - `REQUIRES_ACTION("requires_action")`

### Beta Managed Agents Session Retries Exhausted

- `class BetaManagedAgentsSessionRetriesExhausted:`

  The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

  - `Type type`

    - `RETRIES_EXHAUSTED("retries_exhausted")`

### Beta Managed Agents Session Status Idle Event

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

### Beta Managed Agents Session Status Rescheduled Event

- `class BetaManagedAgentsSessionStatusRescheduledEvent:`

  Indicates the session is recovering from an error state and is rescheduled for execution.

  - `String id`

    Unique identifier for this event.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

    - `SESSION_STATUS_RESCHEDULED("session.status_rescheduled")`

### Beta Managed Agents Session Status Running Event

- `class BetaManagedAgentsSessionStatusRunningEvent:`

  Indicates the session is actively running and the agent is working.

  - `String id`

    Unique identifier for this event.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

    - `SESSION_STATUS_RUNNING("session.status_running")`

### Beta Managed Agents Session Status Terminated Event

- `class BetaManagedAgentsSessionStatusTerminatedEvent:`

  Indicates the session has terminated, either due to an error or completion.

  - `String id`

    Unique identifier for this event.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

    - `SESSION_STATUS_TERMINATED("session.status_terminated")`

### Beta Managed Agents Span Model Request End Event

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

### Beta Managed Agents Span Model Request Start Event

- `class BetaManagedAgentsSpanModelRequestStartEvent:`

  Emitted when a model request is initiated by the agent.

  - `String id`

    Unique identifier for this event.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

    - `SPAN_MODEL_REQUEST_START("span.model_request_start")`

### Beta Managed Agents Span Model Usage

- `class BetaManagedAgentsSpanModelUsage:`

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

### Beta Managed Agents Stream Session Events

- `class BetaManagedAgentsStreamSessionEvents: A class that can be one of several variants.union`

  Server-sent event in the session stream.

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

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_DELETED("session.deleted")`

### Beta Managed Agents Text Block

- `class BetaManagedAgentsTextBlock:`

  Regular text content.

  - `String text`

    The text content.

  - `Type type`

    - `TEXT("text")`

### Beta Managed Agents Unknown Error

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

### Beta Managed Agents URL Document Source

- `class BetaManagedAgentsUrlDocumentSource:`

  Document referenced by URL.

  - `Type type`

    - `URL("url")`

  - `String url`

    URL of the document to fetch.

### Beta Managed Agents URL Image Source

- `class BetaManagedAgentsUrlImageSource:`

  Image referenced by URL.

  - `Type type`

    - `URL("url")`

  - `String url`

    URL of the image to fetch.

### Beta Managed Agents User Custom Tool Result Event

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

### Beta Managed Agents User Custom Tool Result Event Params

- `class BetaManagedAgentsUserCustomToolResultEventParams:`

  Parameters for providing the result of a custom tool execution.

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

### Beta Managed Agents User Interrupt Event

- `class BetaManagedAgentsUserInterruptEvent:`

  An interrupt event that pauses agent execution and returns control to the user.

  - `String id`

    Unique identifier for this event.

  - `Type type`

    - `USER_INTERRUPT("user.interrupt")`

  - `Optional<LocalDateTime> processedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Interrupt Event Params

- `class BetaManagedAgentsUserInterruptEventParams:`

  Parameters for sending an interrupt to pause the agent.

  - `Type type`

    - `USER_INTERRUPT("user.interrupt")`

### Beta Managed Agents User Message Event

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

### Beta Managed Agents User Message Event Params

- `class BetaManagedAgentsUserMessageEventParams:`

  Parameters for sending a user message to the session.

  - `List<Content> content`

    Array of content blocks for the user message.

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

### Beta Managed Agents User Tool Confirmation Event

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

### Beta Managed Agents User Tool Confirmation Event Params

- `class BetaManagedAgentsUserToolConfirmationEventParams:`

  Parameters for confirming or denying a tool execution request.

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

# Resources

## Add

`BetaManagedAgentsFileResource beta().sessions().resources().add(ResourceAddParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/sessions/{session_id}/resources`

Add Session Resource

### Parameters

- `ResourceAddParams params`

  - `Optional<String> sessionId`

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

  - `BetaManagedAgentsFileResourceParams betaManagedAgentsFileResourceParams`

    Mount a file uploaded via the Files API into the session.

### Returns

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

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.BetaManagedAgentsFileResourceParams;
import com.anthropic.models.beta.sessions.resources.BetaManagedAgentsFileResource;
import com.anthropic.models.beta.sessions.resources.ResourceAddParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ResourceAddParams params = ResourceAddParams.builder()
            .sessionId("sesn_011CZkZAtmR3yMPDzynEDxu7")
            .betaManagedAgentsFileResourceParams(BetaManagedAgentsFileResourceParams.builder()
                .fileId("file_011CNha8iCJcU1wXNR6q4V8w")
                .type(BetaManagedAgentsFileResourceParams.Type.FILE)
                .build())
            .build();
        BetaManagedAgentsFileResource betaManagedAgentsFileResource = client.beta().sessions().resources().add(params);
    }
}
```

## List

`ResourceListPage beta().sessions().resources().list(ResourceListParamsparams = ResourceListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/sessions/{session_id}/resources`

List Session Resources

### Parameters

- `ResourceListParams params`

  - `Optional<String> sessionId`

  - `Optional<Long> limit`

    Maximum number of resources to return per page (max 1000). If omitted, returns all resources.

  - `Optional<String> page`

    Opaque cursor from a previous response's next_page field.

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

### Returns

- `class BetaManagedAgentsSessionResource: A class that can be one of several variants.union`

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

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.resources.ResourceListPage;
import com.anthropic.models.beta.sessions.resources.ResourceListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ResourceListPage page = client.beta().sessions().resources().list("sesn_011CZkZAtmR3yMPDzynEDxu7");
    }
}
```

## Retrieve

`ResourceRetrieveResponse beta().sessions().resources().retrieve(ResourceRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/sessions/{session_id}/resources/{resource_id}`

Get Session Resource

### Parameters

- `ResourceRetrieveParams params`

  - `String sessionId`

  - `Optional<String> resourceId`

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

### Returns

- `class ResourceRetrieveResponse: A class that can be one of several variants.union`

  The requested session resource.

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

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.resources.ResourceRetrieveParams;
import com.anthropic.models.beta.sessions.resources.ResourceRetrieveResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ResourceRetrieveParams params = ResourceRetrieveParams.builder()
            .sessionId("sesn_011CZkZAtmR3yMPDzynEDxu7")
            .resourceId("sesrsc_011CZkZBJq5dWxk9fVLNcPht")
            .build();
        ResourceRetrieveResponse resource = client.beta().sessions().resources().retrieve(params);
    }
}
```

## Update

`ResourceUpdateResponse beta().sessions().resources().update(ResourceUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/sessions/{session_id}/resources/{resource_id}`

Update Session Resource

### Parameters

- `ResourceUpdateParams params`

  - `String sessionId`

  - `Optional<String> resourceId`

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

  - `String authorizationToken`

    New authorization token for the resource. Currently only `github_repository` resources support token rotation.

### Returns

- `class ResourceUpdateResponse: A class that can be one of several variants.union`

  The updated session resource.

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

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.resources.ResourceUpdateParams;
import com.anthropic.models.beta.sessions.resources.ResourceUpdateResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ResourceUpdateParams params = ResourceUpdateParams.builder()
            .sessionId("sesn_011CZkZAtmR3yMPDzynEDxu7")
            .resourceId("sesrsc_011CZkZBJq5dWxk9fVLNcPht")
            .authorizationToken("ghp_exampletoken")
            .build();
        ResourceUpdateResponse resource = client.beta().sessions().resources().update(params);
    }
}
```

## Delete

`BetaManagedAgentsDeleteSessionResource beta().sessions().resources().delete(ResourceDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/v1/sessions/{session_id}/resources/{resource_id}`

Delete Session Resource

### Parameters

- `ResourceDeleteParams params`

  - `String sessionId`

  - `Optional<String> resourceId`

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

### Returns

- `class BetaManagedAgentsDeleteSessionResource:`

  Confirmation of resource deletion.

  - `String id`

  - `Type type`

    - `SESSION_RESOURCE_DELETED("session_resource_deleted")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.resources.BetaManagedAgentsDeleteSessionResource;
import com.anthropic.models.beta.sessions.resources.ResourceDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ResourceDeleteParams params = ResourceDeleteParams.builder()
            .sessionId("sesn_011CZkZAtmR3yMPDzynEDxu7")
            .resourceId("sesrsc_011CZkZBJq5dWxk9fVLNcPht")
            .build();
        BetaManagedAgentsDeleteSessionResource betaManagedAgentsDeleteSessionResource = client.beta().sessions().resources().delete(params);
    }
}
```

## Domain Types

### Beta Managed Agents Delete Session Resource

- `class BetaManagedAgentsDeleteSessionResource:`

  Confirmation of resource deletion.

  - `String id`

  - `Type type`

    - `SESSION_RESOURCE_DELETED("session_resource_deleted")`

### Beta Managed Agents File Resource

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

### Beta Managed Agents GitHub Repository Resource

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

### Beta Managed Agents Session Resource

- `class BetaManagedAgentsSessionResource: A class that can be one of several variants.union`

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
