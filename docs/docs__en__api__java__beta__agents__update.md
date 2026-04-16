## Update

`BetaManagedAgentsAgent beta().agents().update(AgentUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/agents/{agent_id}`

Update Agent

### Parameters

- `AgentUpdateParams params`

  - `Optional<String> agentId`

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

  - `long version`

    The agent's current version, used to prevent concurrent overwrites. Obtain this value from a create or retrieve response. The request fails if this does not match the server's current version.

  - `Optional<String> description`

    Description. Up to 2048 characters. Omit to preserve; send empty string or null to clear.

  - `Optional<List<BetaManagedAgentsUrlMcpServerParams>> mcpServers`

    MCP servers. Full replacement. Omit to preserve; send empty array or null to clear. Names must be unique. Maximum 20.

    - `String name`

      Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

    - `Type type`

      - `URL("url")`

    - `String url`

      Endpoint URL for the MCP server.

  - `Optional<Metadata> metadata`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `Optional<Model> model`

    Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-4-6`, or a `model_config` object for additional configuration control. Omit to preserve. Cannot be cleared.

    - `enum BetaManagedAgentsModel:`

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

    - `class BetaManagedAgentsModelConfigParams:`

      An object that defines additional configuration control over model use

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

  - `Optional<String> name`

    Human-readable name. 1-256 characters. Omit to preserve. Cannot be cleared.

  - `Optional<List<BetaManagedAgentsSkillParams>> skills`

    Skills. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 20.

    - `class BetaManagedAgentsAnthropicSkillParams:`

      An Anthropic-managed skill.

      - `String skillId`

        Identifier of the Anthropic skill (e.g., "xlsx").

      - `Type type`

        - `ANTHROPIC("anthropic")`

      - `Optional<String> version`

        Version to pin. Defaults to latest if omitted.

    - `class BetaManagedAgentsCustomSkillParams:`

      A user-created custom skill.

      - `String skillId`

        Tagged ID of the custom skill (e.g., "skill_01XJ5...").

      - `Type type`

        - `CUSTOM("custom")`

      - `Optional<String> version`

        Version to pin. Defaults to latest if omitted.

  - `Optional<String> system`

    System prompt. Up to 100,000 characters. Omit to preserve; send empty string or null to clear.

  - `Optional<List<Tool>> tools`

    Tool configurations available to the agent. Full replacement. Omit to preserve; send empty array or null to clear. Maximum of 128 tools across all toolsets allowed.

    - `class BetaManagedAgentsAgentToolset20260401Params:`

      Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

      - `Type type`

        - `AGENT_TOOLSET_20260401("agent_toolset_20260401")`

      - `Optional<List<BetaManagedAgentsAgentToolConfigParams>> configs`

        Per-tool configuration overrides.

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

        - `Optional<Boolean> enabled`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `Optional<PermissionPolicy> permissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy:`

            Tool calls are automatically approved without user confirmation.

            - `Type type`

              - `ALWAYS_ALLOW("always_allow")`

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

            - `Type type`

              - `ALWAYS_ASK("always_ask")`

      - `Optional<BetaManagedAgentsAgentToolsetDefaultConfigParams> defaultConfig`

        Default configuration for all tools in a toolset.

        - `Optional<Boolean> enabled`

          Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

        - `Optional<PermissionPolicy> permissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy:`

            Tool calls are automatically approved without user confirmation.

            - `Type type`

              - `ALWAYS_ALLOW("always_allow")`

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

            - `Type type`

              - `ALWAYS_ASK("always_ask")`

    - `class BetaManagedAgentsMcpToolsetParams:`

      Configuration for tools from an MCP server defined in `mcp_servers`.

      - `String mcpServerName`

        Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

      - `Type type`

        - `MCP_TOOLSET("mcp_toolset")`

      - `Optional<List<BetaManagedAgentsMcpToolConfigParams>> configs`

        Per-tool configuration overrides.

        - `String name`

          Name of the MCP tool to configure. 1-128 characters.

        - `Optional<Boolean> enabled`

          Whether this tool is enabled. Overrides the `default_config` setting.

        - `Optional<PermissionPolicy> permissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy:`

            Tool calls are automatically approved without user confirmation.

            - `Type type`

              - `ALWAYS_ALLOW("always_allow")`

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

            - `Type type`

              - `ALWAYS_ASK("always_ask")`

      - `Optional<BetaManagedAgentsMcpToolsetDefaultConfigParams> defaultConfig`

        Default configuration for all tools from an MCP server.

        - `Optional<Boolean> enabled`

          Whether tools are enabled by default. Defaults to true if not specified.

        - `Optional<PermissionPolicy> permissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy:`

            Tool calls are automatically approved without user confirmation.

            - `Type type`

              - `ALWAYS_ALLOW("always_allow")`

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

            - `Type type`

              - `ALWAYS_ASK("always_ask")`

    - `class BetaManagedAgentsCustomToolParams:`

      A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

      - `String description`

        Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

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

        Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

      - `Type type`

        - `CUSTOM("custom")`

### Returns

- `class BetaManagedAgentsAgent:`

  A Managed Agents `agent`.

  - `String id`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> description`

  - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

    - `String name`

    - `Type type`

      - `URL("url")`

    - `String url`

  - `Metadata metadata`

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

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `long version`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.agents.AgentUpdateParams;
import com.anthropic.models.beta.agents.BetaManagedAgentsAgent;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        AgentUpdateParams params = AgentUpdateParams.builder()
            .agentId("agent_011CZkYpogX7uDKUyvBTophP")
            .version(1)
            .build();
        BetaManagedAgentsAgent betaManagedAgentsAgent = client.beta().agents().update(params);
    }
}
```
