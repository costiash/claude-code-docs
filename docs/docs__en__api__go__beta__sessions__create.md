## Create Session

`client.Beta.Sessions.New(ctx, params) (*BetaManagedAgentsSession, error)`

**post** `/v1/sessions`

Create Session

### Parameters

- `params BetaSessionNewParams`

  - `Agent param.Field[BetaSessionNewParamsAgentUnion]`

    Body param: Agent identifier. Accepts the `agent` ID string, which pins the latest version for the session, or an `agent` object with both id and version specified.

    - `string`

    - `type BetaManagedAgentsAgentParamsResp struct{…}`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `ID string`

        The `agent` ID.

      - `Type BetaManagedAgentsAgentParamsType`

        - `const BetaManagedAgentsAgentParamsTypeAgent BetaManagedAgentsAgentParamsType = "agent"`

      - `Version int64`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

    - `type BetaManagedAgentsAgentWithOverridesParamsResp struct{…}`

      Reference to an `agent` plus optional configuration overrides. Each provided field replaces the agent's value for the caller's use; the agent resource is unchanged.

      - `ID string`

        The `agent` ID.

      - `Type BetaManagedAgentsAgentWithOverridesParamsType`

        - `const BetaManagedAgentsAgentWithOverridesParamsTypeAgentWithOverrides BetaManagedAgentsAgentWithOverridesParamsType = "agent_with_overrides"`

      - `MCPServers []BetaManagedAgentsURLMCPServerParamsResp`

        Replacement MCP server list. Full replacement: the provided array becomes the MCP servers. Send an empty array to clear; omit to preserve the agent's servers.

        - `Name string`

          Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

        - `Type BetaManagedAgentsURLMCPServerParamsType`

          - `const BetaManagedAgentsURLMCPServerParamsTypeURL BetaManagedAgentsURLMCPServerParamsType = "url"`

        - `URL string`

          Endpoint URL for the MCP server.

      - `Model BetaManagedAgentsModelConfigParamsResp`

        Replacement model. Accepts the model string, e.g. `claude-opus-4-6`, or a `model_config` object. Omit to use the agent's model.

        - `type BetaManagedAgentsModelConfigParamsResp struct{…}`

          An object that defines additional configuration control over model use

          - `ID BetaManagedAgentsModel`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `type BetaManagedAgentsModel string`

              The model that will power your agent.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `const BetaManagedAgentsModelClaudeSonnet5 BetaManagedAgentsModel = "claude-sonnet-5"`

                High-performance model for coding and agents

              - `const BetaManagedAgentsModelClaudeFable5 BetaManagedAgentsModel = "claude-fable-5"`

                Next generation of intelligence for the hardest knowledge work and coding problems

              - `const BetaManagedAgentsModelClaudeOpus4_8 BetaManagedAgentsModel = "claude-opus-4-8"`

                Frontier intelligence for long-running agents and coding

              - `const BetaManagedAgentsModelClaudeOpus4_7 BetaManagedAgentsModel = "claude-opus-4-7"`

                Frontier intelligence for long-running agents and coding

              - `const BetaManagedAgentsModelClaudeOpus4_6 BetaManagedAgentsModel = "claude-opus-4-6"`

                Most intelligent model for building agents and coding

              - `const BetaManagedAgentsModelClaudeSonnet4_6 BetaManagedAgentsModel = "claude-sonnet-4-6"`

                Best combination of speed and intelligence

              - `const BetaManagedAgentsModelClaudeHaiku4_5 BetaManagedAgentsModel = "claude-haiku-4-5"`

                Fastest model with near-frontier intelligence

              - `const BetaManagedAgentsModelClaudeHaiku4_5_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"`

                Fastest model with near-frontier intelligence

              - `const BetaManagedAgentsModelClaudeOpus4_5 BetaManagedAgentsModel = "claude-opus-4-5"`

                Premium model combining maximum intelligence with practical performance

              - `const BetaManagedAgentsModelClaudeOpus4_5_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"`

                Premium model combining maximum intelligence with practical performance

              - `const BetaManagedAgentsModelClaudeSonnet4_5 BetaManagedAgentsModel = "claude-sonnet-4-5"`

                High-performance model for agents and coding

              - `const BetaManagedAgentsModelClaudeSonnet4_5_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"`

                High-performance model for agents and coding

            - `string`

          - `Speed BetaManagedAgentsModelConfigParamsSpeed`

            Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `const BetaManagedAgentsModelConfigParamsSpeedStandard BetaManagedAgentsModelConfigParamsSpeed = "standard"`

            - `const BetaManagedAgentsModelConfigParamsSpeedFast BetaManagedAgentsModelConfigParamsSpeed = "fast"`

      - `Skills []BetaManagedAgentsSkillParamsUnionResp`

        Replacement skill list. Full replacement: the provided array becomes the skills. Send an empty array to clear; omit to preserve the agent's skills.

        - `type BetaManagedAgentsAnthropicSkillParamsResp struct{…}`

          An Anthropic-managed skill.

          - `SkillID string`

            Identifier of the Anthropic skill (e.g., "xlsx").

          - `Type BetaManagedAgentsAnthropicSkillParamsType`

            - `const BetaManagedAgentsAnthropicSkillParamsTypeAnthropic BetaManagedAgentsAnthropicSkillParamsType = "anthropic"`

          - `Version string`

            Version to pin. Defaults to latest if omitted.

        - `type BetaManagedAgentsCustomSkillParamsResp struct{…}`

          A user-created custom skill.

          - `SkillID string`

            Tagged ID of the custom skill (e.g., "skill_01XJ5...").

          - `Type BetaManagedAgentsCustomSkillParamsType`

            - `const BetaManagedAgentsCustomSkillParamsTypeCustom BetaManagedAgentsCustomSkillParamsType = "custom"`

          - `Version string`

            Version to pin. Defaults to latest if omitted.

      - `System string`

        Replacement system prompt. Up to 100,000 characters. Set to null to clear the agent's system prompt; omit to preserve it.

      - `Tools []BetaManagedAgentsAgentWithOverridesParamsToolUnionResp`

        Replacement tool list. Full replacement: the provided array becomes the tool configuration. Send an empty array to clear; omit to preserve the agent's tools.

        - `type BetaManagedAgentsAgentToolset20260401ParamsResp struct{…}`

          Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

          - `Type BetaManagedAgentsAgentToolset20260401ParamsType`

            - `const BetaManagedAgentsAgentToolset20260401ParamsTypeAgentToolset20260401 BetaManagedAgentsAgentToolset20260401ParamsType = "agent_toolset_20260401"`

          - `Configs []BetaManagedAgentsAgentToolConfigParamsResp`

            Per-tool configuration overrides.

            - `Name BetaManagedAgentsAgentToolConfigParamsName`

              Built-in agent tool identifier.

              - `const BetaManagedAgentsAgentToolConfigParamsNameBash BetaManagedAgentsAgentToolConfigParamsName = "bash"`

              - `const BetaManagedAgentsAgentToolConfigParamsNameEdit BetaManagedAgentsAgentToolConfigParamsName = "edit"`

              - `const BetaManagedAgentsAgentToolConfigParamsNameRead BetaManagedAgentsAgentToolConfigParamsName = "read"`

              - `const BetaManagedAgentsAgentToolConfigParamsNameWrite BetaManagedAgentsAgentToolConfigParamsName = "write"`

              - `const BetaManagedAgentsAgentToolConfigParamsNameGlob BetaManagedAgentsAgentToolConfigParamsName = "glob"`

              - `const BetaManagedAgentsAgentToolConfigParamsNameGrep BetaManagedAgentsAgentToolConfigParamsName = "grep"`

              - `const BetaManagedAgentsAgentToolConfigParamsNameWebFetch BetaManagedAgentsAgentToolConfigParamsName = "web_fetch"`

              - `const BetaManagedAgentsAgentToolConfigParamsNameWebSearch BetaManagedAgentsAgentToolConfigParamsName = "web_search"`

            - `Enabled bool`

              Whether this tool is enabled and available to Claude. Overrides the default_config setting.

            - `PermissionPolicy BetaManagedAgentsAgentToolConfigParamsPermissionPolicyUnionResp`

              Permission policy for tool execution.

              - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                Tool calls are automatically approved without user confirmation.

                - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                  - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

              - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                Tool calls require user confirmation before execution.

                - `Type BetaManagedAgentsAlwaysAskPolicyType`

                  - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

          - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfigParamsResp`

            Default configuration for all tools in a toolset.

            - `Enabled bool`

              Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

            - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigParamsPermissionPolicyUnionResp`

              Permission policy for tool execution.

              - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                Tool calls are automatically approved without user confirmation.

              - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                Tool calls require user confirmation before execution.

        - `type BetaManagedAgentsMCPToolsetParamsResp struct{…}`

          Configuration for tools from an MCP server defined in `mcp_servers`.

          - `MCPServerName string`

            Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

          - `Type BetaManagedAgentsMCPToolsetParamsType`

            - `const BetaManagedAgentsMCPToolsetParamsTypeMCPToolset BetaManagedAgentsMCPToolsetParamsType = "mcp_toolset"`

          - `Configs []BetaManagedAgentsMCPToolConfigParamsResp`

            Per-tool configuration overrides.

            - `Name string`

              Name of the MCP tool to configure. 1-128 characters.

            - `Enabled bool`

              Whether this tool is enabled. Overrides the `default_config` setting.

            - `PermissionPolicy BetaManagedAgentsMCPToolConfigParamsPermissionPolicyUnionResp`

              Permission policy for tool execution.

              - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                Tool calls are automatically approved without user confirmation.

              - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                Tool calls require user confirmation before execution.

          - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfigParamsResp`

            Default configuration for all tools from an MCP server.

            - `Enabled bool`

              Whether tools are enabled by default. Defaults to true if not specified.

            - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigParamsPermissionPolicyUnionResp`

              Permission policy for tool execution.

              - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                Tool calls are automatically approved without user confirmation.

              - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                Tool calls require user confirmation before execution.

        - `type BetaManagedAgentsCustomToolParamsResp struct{…}`

          A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

          - `Description string`

            Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-4096 characters.

          - `InputSchema BetaManagedAgentsCustomToolInputSchema`

            JSON Schema for custom tool input parameters.

            - `Type Object`

              - `const ObjectObject Object = "object"`

            - `Properties map[string, any]`

            - `Required []string`

          - `Name string`

            Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

          - `Type BetaManagedAgentsCustomToolParamsType`

            - `const BetaManagedAgentsCustomToolParamsTypeCustom BetaManagedAgentsCustomToolParamsType = "custom"`

      - `Version int64`

        The specific `agent` version to use. Omit to use the latest version.

  - `EnvironmentID param.Field[string]`

    Body param: ID of the `environment` defining the container configuration for this session.

  - `Metadata param.Field[map[string, string]]`

    Body param: Arbitrary key-value metadata attached to the session. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `Resources param.Field[[]BetaSessionNewParamsResourceUnion]`

    Body param: Resources (e.g. repositories, files) to mount into the session's container.

    - `type BetaManagedAgentsGitHubRepositoryResourceParamsResp struct{…}`

      Mount a GitHub repository into the session's container.

      - `AuthorizationToken string`

        GitHub authorization token used to clone the repository.

      - `Type BetaManagedAgentsGitHubRepositoryResourceParamsType`

        - `const BetaManagedAgentsGitHubRepositoryResourceParamsTypeGitHubRepository BetaManagedAgentsGitHubRepositoryResourceParamsType = "github_repository"`

      - `URL string`

        Github URL of the repository

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceParamsCheckoutUnionResp`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

          - `Type BetaManagedAgentsBranchCheckoutType`

            - `const BetaManagedAgentsBranchCheckoutTypeBranch BetaManagedAgentsBranchCheckoutType = "branch"`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

          - `Type BetaManagedAgentsCommitCheckoutType`

            - `const BetaManagedAgentsCommitCheckoutTypeCommit BetaManagedAgentsCommitCheckoutType = "commit"`

      - `MountPath string`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `type BetaManagedAgentsFileResourceParamsResp struct{…}`

      Mount a file uploaded via the Files API into the session.

      - `FileID string`

        ID of a previously uploaded file.

      - `Type BetaManagedAgentsFileResourceParamsType`

        - `const BetaManagedAgentsFileResourceParamsTypeFile BetaManagedAgentsFileResourceParamsType = "file"`

      - `MountPath string`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `type BetaManagedAgentsMemoryStoreResourceParamResp struct{…}`

      Parameters for attaching a memory store to an agent session.

      - `MemoryStoreID string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type BetaManagedAgentsMemoryStoreResourceParamType`

        - `const BetaManagedAgentsMemoryStoreResourceParamTypeMemoryStore BetaManagedAgentsMemoryStoreResourceParamType = "memory_store"`

      - `Access BetaManagedAgentsMemoryStoreResourceParamAccess`

        Access mode for an attached memory store.

        - `const BetaManagedAgentsMemoryStoreResourceParamAccessReadWrite BetaManagedAgentsMemoryStoreResourceParamAccess = "read_write"`

        - `const BetaManagedAgentsMemoryStoreResourceParamAccessReadOnly BetaManagedAgentsMemoryStoreResourceParamAccess = "read_only"`

      - `Instructions string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `Title param.Field[string]`

    Body param: Human-readable session title.

  - `VaultIDs param.Field[[]string]`

    Body param: Vault IDs for stored credentials the agent can use during the session.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsSession struct{…}`

  A Managed Agents `session`.

  - `ID string`

  - `Agent BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `ID string`

    - `Description string`

    - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

      - `Name string`

      - `Type BetaManagedAgentsMCPServerURLDefinitionType`

        - `const BetaManagedAgentsMCPServerURLDefinitionTypeURL BetaManagedAgentsMCPServerURLDefinitionType = "url"`

      - `URL string`

    - `Model BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `ID BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `type BetaManagedAgentsModel string`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `const BetaManagedAgentsModelClaudeSonnet5 BetaManagedAgentsModel = "claude-sonnet-5"`

            High-performance model for coding and agents

          - `const BetaManagedAgentsModelClaudeFable5 BetaManagedAgentsModel = "claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `const BetaManagedAgentsModelClaudeOpus4_8 BetaManagedAgentsModel = "claude-opus-4-8"`

            Frontier intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_7 BetaManagedAgentsModel = "claude-opus-4-7"`

            Frontier intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_6 BetaManagedAgentsModel = "claude-opus-4-6"`

            Most intelligent model for building agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_6 BetaManagedAgentsModel = "claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `const BetaManagedAgentsModelClaudeHaiku4_5 BetaManagedAgentsModel = "claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `const BetaManagedAgentsModelClaudeHaiku4_5_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `const BetaManagedAgentsModelClaudeOpus4_5 BetaManagedAgentsModel = "claude-opus-4-5"`

            Premium model combining maximum intelligence with practical performance

          - `const BetaManagedAgentsModelClaudeOpus4_5_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"`

            Premium model combining maximum intelligence with practical performance

          - `const BetaManagedAgentsModelClaudeSonnet4_5 BetaManagedAgentsModel = "claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_5_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `string`

      - `Speed BetaManagedAgentsModelConfigSpeed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"`

        - `const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"`

    - `Multiagent BetaManagedAgentsSessionMultiagentCoordinator`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `Agents []BetaManagedAgentsSessionThreadAgent`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `ID string`

        - `Description string`

        - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

          - `Name string`

          - `Type BetaManagedAgentsMCPServerURLDefinitionType`

          - `URL string`

        - `Model BetaManagedAgentsModelConfig`

          Model identifier and configuration.

        - `Name string`

        - `Skills []BetaManagedAgentsSessionThreadAgentSkillUnion`

          - `type BetaManagedAgentsAnthropicSkill struct{…}`

            A resolved Anthropic-managed skill.

            - `SkillID string`

            - `Type BetaManagedAgentsAnthropicSkillType`

              - `const BetaManagedAgentsAnthropicSkillTypeAnthropic BetaManagedAgentsAnthropicSkillType = "anthropic"`

            - `Version string`

          - `type BetaManagedAgentsCustomSkill struct{…}`

            A resolved user-created custom skill.

            - `SkillID string`

            - `Type BetaManagedAgentsCustomSkillType`

              - `const BetaManagedAgentsCustomSkillTypeCustom BetaManagedAgentsCustomSkillType = "custom"`

            - `Version string`

        - `System string`

        - `Tools []BetaManagedAgentsSessionThreadAgentToolUnion`

          - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

            - `Configs []BetaManagedAgentsAgentToolConfig`

              - `Enabled bool`

              - `Name BetaManagedAgentsAgentToolConfigName`

                Built-in agent tool identifier.

                - `const BetaManagedAgentsAgentToolConfigNameBash BetaManagedAgentsAgentToolConfigName = "bash"`

                - `const BetaManagedAgentsAgentToolConfigNameEdit BetaManagedAgentsAgentToolConfigName = "edit"`

                - `const BetaManagedAgentsAgentToolConfigNameRead BetaManagedAgentsAgentToolConfigName = "read"`

                - `const BetaManagedAgentsAgentToolConfigNameWrite BetaManagedAgentsAgentToolConfigName = "write"`

                - `const BetaManagedAgentsAgentToolConfigNameGlob BetaManagedAgentsAgentToolConfigName = "glob"`

                - `const BetaManagedAgentsAgentToolConfigNameGrep BetaManagedAgentsAgentToolConfigName = "grep"`

                - `const BetaManagedAgentsAgentToolConfigNameWebFetch BetaManagedAgentsAgentToolConfigName = "web_fetch"`

                - `const BetaManagedAgentsAgentToolConfigNameWebSearch BetaManagedAgentsAgentToolConfigName = "web_search"`

              - `PermissionPolicy BetaManagedAgentsAgentToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                  - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                    - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

                  - `Type BetaManagedAgentsAlwaysAskPolicyType`

                    - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

            - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfig`

              Resolved default configuration for agent tools.

              - `Enabled bool`

              - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

            - `Type BetaManagedAgentsAgentToolset20260401Type`

              - `const BetaManagedAgentsAgentToolset20260401TypeAgentToolset20260401 BetaManagedAgentsAgentToolset20260401Type = "agent_toolset_20260401"`

          - `type BetaManagedAgentsMCPToolset struct{…}`

            - `Configs []BetaManagedAgentsMCPToolConfig`

              - `Enabled bool`

              - `Name string`

              - `PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

            - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfig`

              Resolved default configuration for all tools from an MCP server.

              - `Enabled bool`

              - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

            - `MCPServerName string`

            - `Type BetaManagedAgentsMCPToolsetType`

              - `const BetaManagedAgentsMCPToolsetTypeMCPToolset BetaManagedAgentsMCPToolsetType = "mcp_toolset"`

          - `type BetaManagedAgentsCustomTool struct{…}`

            A custom tool as returned in API responses.

            - `Description string`

            - `InputSchema BetaManagedAgentsCustomToolInputSchema`

              JSON Schema for custom tool input parameters.

              - `Type Object`

                - `const ObjectObject Object = "object"`

              - `Properties map[string, any]`

              - `Required []string`

            - `Name string`

            - `Type BetaManagedAgentsCustomToolType`

              - `const BetaManagedAgentsCustomToolTypeCustom BetaManagedAgentsCustomToolType = "custom"`

        - `Type BetaManagedAgentsSessionThreadAgentType`

          - `const BetaManagedAgentsSessionThreadAgentTypeAgent BetaManagedAgentsSessionThreadAgentType = "agent"`

        - `Version int64`

      - `Type BetaManagedAgentsSessionMultiagentCoordinatorType`

        - `const BetaManagedAgentsSessionMultiagentCoordinatorTypeCoordinator BetaManagedAgentsSessionMultiagentCoordinatorType = "coordinator"`

    - `Name string`

    - `Skills []BetaManagedAgentsSessionAgentSkillUnion`

      - `type BetaManagedAgentsAnthropicSkill struct{…}`

        A resolved Anthropic-managed skill.

      - `type BetaManagedAgentsCustomSkill struct{…}`

        A resolved user-created custom skill.

    - `System string`

    - `Tools []BetaManagedAgentsSessionAgentToolUnion`

      - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

      - `type BetaManagedAgentsMCPToolset struct{…}`

      - `type BetaManagedAgentsCustomTool struct{…}`

        A custom tool as returned in API responses.

    - `Type BetaManagedAgentsSessionAgentType`

      - `const BetaManagedAgentsSessionAgentTypeAgent BetaManagedAgentsSessionAgentType = "agent"`

    - `Version int64`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `EnvironmentID string`

  - `Metadata map[string, string]`

  - `OutcomeEvaluations []BetaManagedAgentsOutcomeEvaluationResource`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

    - `CompletedAt Time`

      A timestamp in RFC 3339 format

    - `Description string`

      What the agent should produce.

    - `Explanation string`

      Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

    - `Iteration int64`

      0-indexed revision cycle the outcome is currently on.

    - `OutcomeID string`

      Server-generated outc_ ID for this outcome.

    - `Result string`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `Type BetaManagedAgentsOutcomeEvaluationResourceType`

      - `const BetaManagedAgentsOutcomeEvaluationResourceTypeOutcomeEvaluation BetaManagedAgentsOutcomeEvaluationResourceType = "outcome_evaluation"`

  - `Resources []BetaManagedAgentsSessionResourceUnion`

    - `type BetaManagedAgentsGitHubRepositoryResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

      - `MountPath string`

      - `Type BetaManagedAgentsGitHubRepositoryResourceType`

        - `const BetaManagedAgentsGitHubRepositoryResourceTypeGitHubRepository BetaManagedAgentsGitHubRepositoryResourceType = "github_repository"`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

      - `URL string`

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnion`

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

          - `Type BetaManagedAgentsBranchCheckoutType`

            - `const BetaManagedAgentsBranchCheckoutTypeBranch BetaManagedAgentsBranchCheckoutType = "branch"`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

          - `Type BetaManagedAgentsCommitCheckoutType`

            - `const BetaManagedAgentsCommitCheckoutTypeCommit BetaManagedAgentsCommitCheckoutType = "commit"`

    - `type BetaManagedAgentsFileResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

      - `FileID string`

      - `MountPath string`

      - `Type BetaManagedAgentsFileResourceType`

        - `const BetaManagedAgentsFileResourceTypeFile BetaManagedAgentsFileResourceType = "file"`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

    - `type BetaManagedAgentsMemoryStoreResource struct{…}`

      A memory store attached to an agent session.

      - `MemoryStoreID string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type BetaManagedAgentsMemoryStoreResourceType`

        - `const BetaManagedAgentsMemoryStoreResourceTypeMemoryStore BetaManagedAgentsMemoryStoreResourceType = "memory_store"`

      - `Access BetaManagedAgentsMemoryStoreResourceAccess`

        Access mode for an attached memory store.

        - `const BetaManagedAgentsMemoryStoreResourceAccessReadWrite BetaManagedAgentsMemoryStoreResourceAccess = "read_write"`

        - `const BetaManagedAgentsMemoryStoreResourceAccessReadOnly BetaManagedAgentsMemoryStoreResourceAccess = "read_only"`

      - `Description string`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `Instructions string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      - `MountPath string`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `Name string`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `Stats BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `ActiveSeconds float64`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

    - `DurationSeconds float64`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

  - `Status BetaManagedAgentsSessionStatus`

    SessionStatus enum

    - `const BetaManagedAgentsSessionStatusRescheduling BetaManagedAgentsSessionStatus = "rescheduling"`

    - `const BetaManagedAgentsSessionStatusRunning BetaManagedAgentsSessionStatus = "running"`

    - `const BetaManagedAgentsSessionStatusIdle BetaManagedAgentsSessionStatus = "idle"`

    - `const BetaManagedAgentsSessionStatusTerminated BetaManagedAgentsSessionStatus = "terminated"`

  - `Title string`

  - `Type BetaManagedAgentsSessionType`

    - `const BetaManagedAgentsSessionTypeSession BetaManagedAgentsSessionType = "session"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Usage BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

    - `CacheCreation BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Ephemeral1hInputTokens int64`

        Tokens used to create 1-hour ephemeral cache entries.

      - `Ephemeral5mInputTokens int64`

        Tokens used to create 5-minute ephemeral cache entries.

    - `CacheReadInputTokens int64`

      Total tokens read from prompt cache.

    - `InputTokens int64`

      Total input tokens consumed across all turns.

    - `OutputTokens int64`

      Total output tokens generated across all turns.

  - `VaultIDs []string`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `DeploymentID string`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaManagedAgentsSession, err := client.Beta.Sessions.New(context.TODO(), anthropic.BetaSessionNewParams{
    Agent: anthropic.BetaSessionNewParamsAgentUnion{
      OfString: anthropic.String("agent_011CZkYpogX7uDKUyvBTophP"),
    },
    EnvironmentID: "env_011CZkZ9X2dpNyB7HsEFoRfW",
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsSession.ID)
}
```

#### Response

```json
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "description": "A general-purpose starter agent.",
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
    "multiagent": {
      "agents": [
        {
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
        }
      ],
      "type": "coordinator"
    },
    "name": "My First Agent",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      },
      {
        "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
        "type": "custom",
        "version": "2"
      }
    ],
    "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
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
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "metadata": {},
  "outcome_evaluations": [
    {
      "completed_at": "2026-03-15T10:02:31Z",
      "description": "Produce a 2-page summary as summary.md",
      "explanation": "All five sections present with inline citations.",
      "iteration": 0,
      "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
      "result": "satisfied",
      "type": "outcome_evaluation"
    }
  ],
  "resources": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0
  },
  "status": "idle",
  "title": "Order #1234 inquiry",
  "type": "session",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  },
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "deployment_id": "deployment_id"
}
```
