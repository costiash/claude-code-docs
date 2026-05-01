## Update

`beta.agents.update(stragent_id, AgentUpdateParams**kwargs)  -> BetaManagedAgentsAgent`

**post** `/v1/agents/{agent_id}`

Update Agent

### Parameters

- `agent_id: str`

- `version: int`

  The agent's current version, used to prevent concurrent overwrites. Obtain this value from a create or retrieve response. The request fails if this does not match the server's current version.

- `description: Optional[str]`

  Description. Up to 2048 characters. Omit to preserve; send empty string or null to clear.

- `mcp_servers: Optional[Iterable[BetaManagedAgentsURLMCPServerParams]]`

  MCP servers. Full replacement. Omit to preserve; send empty array or null to clear. Names must be unique. Maximum 20.

  - `name: str`

    Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

  - `type: Literal["url"]`

    - `"url"`

  - `url: str`

    Endpoint URL for the MCP server.

- `metadata: Optional[Dict[str, Optional[str]]]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `model: Optional[Model]`

  Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-4-6`, or a `model_config` object for additional configuration control. Omit to preserve. Cannot be cleared.

  - `Union[Literal["claude-opus-4-7", "claude-opus-4-6", "claude-sonnet-4-6", 6 more], str]`

    - `Literal["claude-opus-4-7", "claude-opus-4-6", "claude-sonnet-4-6", 6 more]`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
      - `claude-opus-4-6` - Most intelligent model for building agents and coding
      - `claude-sonnet-4-6` - Best combination of speed and intelligence
      - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
      - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
      - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
      - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
      - `claude-sonnet-4-5` - High-performance model for agents and coding
      - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

      - `"claude-opus-4-7"`

        Frontier intelligence for long-running agents and coding

      - `"claude-opus-4-6"`

        Most intelligent model for building agents and coding

      - `"claude-sonnet-4-6"`

        Best combination of speed and intelligence

      - `"claude-haiku-4-5"`

        Fastest model with near-frontier intelligence

      - `"claude-haiku-4-5-20251001"`

        Fastest model with near-frontier intelligence

      - `"claude-opus-4-5"`

        Premium model combining maximum intelligence with practical performance

      - `"claude-opus-4-5-20251101"`

        Premium model combining maximum intelligence with practical performance

      - `"claude-sonnet-4-5"`

        High-performance model for agents and coding

      - `"claude-sonnet-4-5-20250929"`

        High-performance model for agents and coding

    - `str`

  - `class BetaManagedAgentsModelConfigParams: …`

    An object that defines additional configuration control over model use

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `Literal["claude-opus-4-7", "claude-opus-4-6", "claude-sonnet-4-6", 6 more]`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
        - `claude-opus-4-6` - Most intelligent model for building agents and coding
        - `claude-sonnet-4-6` - Best combination of speed and intelligence
        - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
        - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
        - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
        - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
        - `claude-sonnet-4-5` - High-performance model for agents and coding
        - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

        - `"claude-opus-4-7"`

          Frontier intelligence for long-running agents and coding

        - `"claude-opus-4-6"`

          Most intelligent model for building agents and coding

        - `"claude-sonnet-4-6"`

          Best combination of speed and intelligence

        - `"claude-haiku-4-5"`

          Fastest model with near-frontier intelligence

        - `"claude-haiku-4-5-20251001"`

          Fastest model with near-frontier intelligence

        - `"claude-opus-4-5"`

          Premium model combining maximum intelligence with practical performance

        - `"claude-opus-4-5-20251101"`

          Premium model combining maximum intelligence with practical performance

        - `"claude-sonnet-4-5"`

          High-performance model for agents and coding

        - `"claude-sonnet-4-5-20250929"`

          High-performance model for agents and coding

      - `str`

    - `speed: Optional[Literal["standard", "fast"]]`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

- `name: Optional[str]`

  Human-readable name. 1-256 characters. Omit to preserve. Cannot be cleared.

- `skills: Optional[Iterable[BetaManagedAgentsSkillParams]]`

  Skills. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 20.

  - `class BetaManagedAgentsAnthropicSkillParams: …`

    An Anthropic-managed skill.

    - `skill_id: str`

      Identifier of the Anthropic skill (e.g., "xlsx").

    - `type: Literal["anthropic"]`

      - `"anthropic"`

    - `version: Optional[str]`

      Version to pin. Defaults to latest if omitted.

  - `class BetaManagedAgentsCustomSkillParams: …`

    A user-created custom skill.

    - `skill_id: str`

      Tagged ID of the custom skill (e.g., "skill_01XJ5...").

    - `type: Literal["custom"]`

      - `"custom"`

    - `version: Optional[str]`

      Version to pin. Defaults to latest if omitted.

- `system: Optional[str]`

  System prompt. Up to 100,000 characters. Omit to preserve; send empty string or null to clear.

- `tools: Optional[Iterable[Tool]]`

  Tool configurations available to the agent. Full replacement. Omit to preserve; send empty array or null to clear. Maximum of 128 tools across all toolsets allowed.

  - `class BetaManagedAgentsAgentToolset20260401Params: …`

    Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

    - `type: Literal["agent_toolset_20260401"]`

      - `"agent_toolset_20260401"`

    - `configs: Optional[List[BetaManagedAgentsAgentToolConfigParams]]`

      Per-tool configuration overrides.

      - `name: Literal["bash", "edit", "read", 5 more]`

        Built-in agent tool identifier.

        - `"bash"`

        - `"edit"`

        - `"read"`

        - `"write"`

        - `"glob"`

        - `"grep"`

        - `"web_fetch"`

        - `"web_search"`

      - `enabled: Optional[bool]`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `permission_policy: Optional[PermissionPolicy]`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy: …`

          Tool calls are automatically approved without user confirmation.

          - `type: Literal["always_allow"]`

            - `"always_allow"`

        - `class BetaManagedAgentsAlwaysAskPolicy: …`

          Tool calls require user confirmation before execution.

          - `type: Literal["always_ask"]`

            - `"always_ask"`

    - `default_config: Optional[BetaManagedAgentsAgentToolsetDefaultConfigParams]`

      Default configuration for all tools in a toolset.

      - `enabled: Optional[bool]`

        Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

      - `permission_policy: Optional[PermissionPolicy]`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy: …`

          Tool calls are automatically approved without user confirmation.

          - `type: Literal["always_allow"]`

            - `"always_allow"`

        - `class BetaManagedAgentsAlwaysAskPolicy: …`

          Tool calls require user confirmation before execution.

          - `type: Literal["always_ask"]`

            - `"always_ask"`

  - `class BetaManagedAgentsMCPToolsetParams: …`

    Configuration for tools from an MCP server defined in `mcp_servers`.

    - `mcp_server_name: str`

      Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

    - `type: Literal["mcp_toolset"]`

      - `"mcp_toolset"`

    - `configs: Optional[List[BetaManagedAgentsMCPToolConfigParams]]`

      Per-tool configuration overrides.

      - `name: str`

        Name of the MCP tool to configure. 1-128 characters.

      - `enabled: Optional[bool]`

        Whether this tool is enabled. Overrides the `default_config` setting.

      - `permission_policy: Optional[PermissionPolicy]`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy: …`

          Tool calls are automatically approved without user confirmation.

          - `type: Literal["always_allow"]`

            - `"always_allow"`

        - `class BetaManagedAgentsAlwaysAskPolicy: …`

          Tool calls require user confirmation before execution.

          - `type: Literal["always_ask"]`

            - `"always_ask"`

    - `default_config: Optional[BetaManagedAgentsMCPToolsetDefaultConfigParams]`

      Default configuration for all tools from an MCP server.

      - `enabled: Optional[bool]`

        Whether tools are enabled by default. Defaults to true if not specified.

      - `permission_policy: Optional[PermissionPolicy]`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy: …`

          Tool calls are automatically approved without user confirmation.

          - `type: Literal["always_allow"]`

            - `"always_allow"`

        - `class BetaManagedAgentsAlwaysAskPolicy: …`

          Tool calls require user confirmation before execution.

          - `type: Literal["always_ask"]`

            - `"always_ask"`

  - `class BetaManagedAgentsCustomToolParams: …`

    A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

    - `description: str`

      Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

    - `input_schema: BetaManagedAgentsCustomToolInputSchema`

      JSON Schema for custom tool input parameters.

      - `properties: Optional[Dict[str, object]]`

        JSON Schema properties defining the tool's input parameters.

      - `required: Optional[List[str]]`

        List of required property names.

      - `type: Optional[Literal["object"]]`

        Must be 'object' for tool input schemas.

        - `"object"`

    - `name: str`

      Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

    - `type: Literal["custom"]`

      - `"custom"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 20 more]`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"advisor-tool-2026-03-01"`

### Returns

- `class BetaManagedAgentsAgent: …`

  A Managed Agents `agent`.

  - `id: str`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `description: Optional[str]`

  - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

    - `name: str`

    - `type: Literal["url"]`

      - `"url"`

    - `url: str`

  - `metadata: Dict[str, str]`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `Literal["claude-opus-4-7", "claude-opus-4-6", "claude-sonnet-4-6", 6 more]`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
        - `claude-opus-4-6` - Most intelligent model for building agents and coding
        - `claude-sonnet-4-6` - Best combination of speed and intelligence
        - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
        - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
        - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
        - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
        - `claude-sonnet-4-5` - High-performance model for agents and coding
        - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

        - `"claude-opus-4-7"`

          Frontier intelligence for long-running agents and coding

        - `"claude-opus-4-6"`

          Most intelligent model for building agents and coding

        - `"claude-sonnet-4-6"`

          Best combination of speed and intelligence

        - `"claude-haiku-4-5"`

          Fastest model with near-frontier intelligence

        - `"claude-haiku-4-5-20251001"`

          Fastest model with near-frontier intelligence

        - `"claude-opus-4-5"`

          Premium model combining maximum intelligence with practical performance

        - `"claude-opus-4-5-20251101"`

          Premium model combining maximum intelligence with practical performance

        - `"claude-sonnet-4-5"`

          High-performance model for agents and coding

        - `"claude-sonnet-4-5-20250929"`

          High-performance model for agents and coding

      - `str`

    - `speed: Optional[Literal["standard", "fast"]]`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `name: str`

  - `skills: List[Skill]`

    - `class BetaManagedAgentsAnthropicSkill: …`

      A resolved Anthropic-managed skill.

      - `skill_id: str`

      - `type: Literal["anthropic"]`

        - `"anthropic"`

      - `version: str`

    - `class BetaManagedAgentsCustomSkill: …`

      A resolved user-created custom skill.

      - `skill_id: str`

      - `type: Literal["custom"]`

        - `"custom"`

      - `version: str`

  - `system: Optional[str]`

  - `tools: List[Tool]`

    - `class BetaManagedAgentsAgentToolset20260401: …`

      - `configs: List[BetaManagedAgentsAgentToolConfig]`

        - `enabled: bool`

        - `name: Literal["bash", "edit", "read", 5 more]`

          Built-in agent tool identifier.

          - `"bash"`

          - `"edit"`

          - `"read"`

          - `"write"`

          - `"glob"`

          - `"grep"`

          - `"web_fetch"`

          - `"web_search"`

        - `permission_policy: PermissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy: …`

            Tool calls are automatically approved without user confirmation.

            - `type: Literal["always_allow"]`

              - `"always_allow"`

          - `class BetaManagedAgentsAlwaysAskPolicy: …`

            Tool calls require user confirmation before execution.

            - `type: Literal["always_ask"]`

              - `"always_ask"`

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: bool`

        - `permission_policy: PermissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy: …`

            Tool calls are automatically approved without user confirmation.

            - `type: Literal["always_allow"]`

              - `"always_allow"`

          - `class BetaManagedAgentsAlwaysAskPolicy: …`

            Tool calls require user confirmation before execution.

            - `type: Literal["always_ask"]`

              - `"always_ask"`

      - `type: Literal["agent_toolset_20260401"]`

        - `"agent_toolset_20260401"`

    - `class BetaManagedAgentsMCPToolset: …`

      - `configs: List[BetaManagedAgentsMCPToolConfig]`

        - `enabled: bool`

        - `name: str`

        - `permission_policy: PermissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy: …`

            Tool calls are automatically approved without user confirmation.

            - `type: Literal["always_allow"]`

              - `"always_allow"`

          - `class BetaManagedAgentsAlwaysAskPolicy: …`

            Tool calls require user confirmation before execution.

            - `type: Literal["always_ask"]`

              - `"always_ask"`

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: bool`

        - `permission_policy: PermissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy: …`

            Tool calls are automatically approved without user confirmation.

            - `type: Literal["always_allow"]`

              - `"always_allow"`

          - `class BetaManagedAgentsAlwaysAskPolicy: …`

            Tool calls require user confirmation before execution.

            - `type: Literal["always_ask"]`

              - `"always_ask"`

      - `mcp_server_name: str`

      - `type: Literal["mcp_toolset"]`

        - `"mcp_toolset"`

    - `class BetaManagedAgentsCustomTool: …`

      A custom tool as returned in API responses.

      - `description: str`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `properties: Optional[Dict[str, object]]`

          JSON Schema properties defining the tool's input parameters.

        - `required: Optional[List[str]]`

          List of required property names.

        - `type: Optional[Literal["object"]]`

          Must be 'object' for tool input schemas.

          - `"object"`

      - `name: str`

      - `type: Literal["custom"]`

        - `"custom"`

  - `type: Literal["agent"]`

    - `"agent"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `version: int`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_agent = client.beta.agents.update(
    agent_id="agent_011CZkYpogX7uDKUyvBTophP",
    version=1,
)
print(beta_managed_agents_agent.id)
```
