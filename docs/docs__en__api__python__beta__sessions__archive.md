## Archive

`beta.sessions.archive(strsession_id, SessionArchiveParams**kwargs)  -> BetaManagedAgentsSession`

**post** `/v1/sessions/{session_id}/archive`

Archive Session

### Parameters

- `session_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 18 more]`

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

### Returns

- `class BetaManagedAgentsSession: …`

  A Managed Agents `session`.

  - `id: str`

  - `agent: BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `id: str`

    - `description: Optional[str]`

    - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

      - `name: str`

      - `type: Literal["url"]`

        - `"url"`

      - `url: str`

    - `model: BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `Literal["claude-opus-4-6", "claude-sonnet-4-6", "claude-haiku-4-5", 5 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-opus-4-6` - Most intelligent model for building agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
          - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

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

    - `version: int`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `environment_id: str`

  - `metadata: Dict[str, str]`

  - `resources: List[BetaManagedAgentsSessionResource]`

    - `class BetaManagedAgentsGitHubRepositoryResource: …`

      - `id: str`

      - `created_at: datetime`

        A timestamp in RFC 3339 format

      - `mount_path: str`

      - `type: Literal["github_repository"]`

        - `"github_repository"`

      - `updated_at: datetime`

        A timestamp in RFC 3339 format

      - `url: str`

      - `checkout: Optional[Checkout]`

        - `class BetaManagedAgentsBranchCheckout: …`

          - `name: str`

            Branch name to check out.

          - `type: Literal["branch"]`

            - `"branch"`

        - `class BetaManagedAgentsCommitCheckout: …`

          - `sha: str`

            Full commit SHA to check out.

          - `type: Literal["commit"]`

            - `"commit"`

    - `class BetaManagedAgentsFileResource: …`

      - `id: str`

      - `created_at: datetime`

        A timestamp in RFC 3339 format

      - `file_id: str`

      - `mount_path: str`

      - `type: Literal["file"]`

        - `"file"`

      - `updated_at: datetime`

        A timestamp in RFC 3339 format

  - `stats: BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

    - `duration_seconds: Optional[float]`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

  - `status: Literal["rescheduling", "running", "idle", "terminated"]`

    SessionStatus enum

    - `"rescheduling"`

    - `"running"`

    - `"idle"`

    - `"terminated"`

  - `title: Optional[str]`

  - `type: Literal["session"]`

    - `"session"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `usage: BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

    - `cache_creation: Optional[BetaManagedAgentsCacheCreationUsage]`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: Optional[int]`

        Tokens used to create 1-hour ephemeral cache entries.

      - `ephemeral_5m_input_tokens: Optional[int]`

        Tokens used to create 5-minute ephemeral cache entries.

    - `cache_read_input_tokens: Optional[int]`

      Total tokens read from prompt cache.

    - `input_tokens: Optional[int]`

      Total input tokens consumed across all turns.

    - `output_tokens: Optional[int]`

      Total output tokens generated across all turns.

  - `vault_ids: List[str]`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_session = client.beta.sessions.archive(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
print(beta_managed_agents_session.id)
```
