## Update

`BetaManagedAgentsAgent Beta.Agents.Update(AgentUpdateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/agents/{agent_id}`

Update Agent

### Parameters

- `AgentUpdateParams parameters`

  - `required string agentID`

    Path param: Path parameter agent_id

  - `required Int version`

    Body param: The agent's current version, used to prevent concurrent overwrites. Obtain this value from a create or retrieve response. The request fails if this does not match the server's current version.

  - `string? description`

    Body param: Description. Up to 2048 characters. Omit to preserve; send empty string or null to clear.

  - `IReadOnlyList<BetaManagedAgentsUrlMcpServerParams>? mcpServers`

    Body param: MCP servers. Full replacement. Omit to preserve; send empty array or null to clear. Names must be unique. Maximum 20.

    - `required string Name`

      Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

    - `required Type Type`

      - `"url"Url`

    - `required string Url`

      Endpoint URL for the MCP server.

  - `IReadOnlyDictionary<string, string>? metadata`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `Model model`

    Body param: Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-4-6`, or a `model_config` object for additional configuration control. Omit to preserve. Cannot be cleared.

    - `enum BetaManagedAgentsModel:`

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

    - `class BetaManagedAgentsModelConfigParams:`

      An object that defines additional configuration control over model use

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

      - `Speed? Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"Standard`

        - `"fast"Fast`

  - `string name`

    Body param: Human-readable name. 1-256 characters. Omit to preserve. Cannot be cleared.

  - `IReadOnlyList<BetaManagedAgentsSkillParams>? skills`

    Body param: Skills. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 20.

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

  - `string? system`

    Body param: System prompt. Up to 100,000 characters. Omit to preserve; send empty string or null to clear.

  - `IReadOnlyList<Tool>? tools`

    Body param: Tool configurations available to the agent. Full replacement. Omit to preserve; send empty array or null to clear. Maximum of 128 tools across all toolsets allowed.

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

            - `required Type Type`

              - `"always_allow"AlwaysAllow`

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

            - `required Type Type`

              - `"always_ask"AlwaysAsk`

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

            - `required Type Type`

              - `"always_allow"AlwaysAllow`

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

            - `required Type Type`

              - `"always_ask"AlwaysAsk`

      - `BetaManagedAgentsMcpToolsetDefaultConfigParams? DefaultConfig`

        Default configuration for all tools from an MCP server.

        - `Boolean? Enabled`

          Whether tools are enabled by default. Defaults to true if not specified.

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

    - `class BetaManagedAgentsCustomToolParams:`

      A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

      - `required string Description`

        Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

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

        Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

      - `required Type Type`

        - `"custom"Custom`

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

- `class BetaManagedAgentsAgent:`

  A Managed Agents `agent`.

  - `required string ID`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? Description`

  - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

    - `required string Name`

    - `required Type Type`

      - `"url"Url`

    - `required string Url`

  - `required IReadOnlyDictionary<string, string> Metadata`

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

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required Int Version`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```csharp
AgentUpdateParams parameters = new()
{
    AgentID = "agent_011CZkYpogX7uDKUyvBTophP",
    Version = 1,
};

var betaManagedAgentsAgent = await client.Beta.Agents.Update(parameters);

Console.WriteLine(betaManagedAgentsAgent);
```
