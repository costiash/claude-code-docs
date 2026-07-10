# Threads

## List Session Threads

`beta.sessions.threads.list(strsession_id, ThreadListParams**kwargs)  -> SyncPageCursor[BetaManagedAgentsSessionThread]`

**get** `/v1/sessions/{session_id}/threads`

List Session Threads

### Parameters

- `session_id: str`

- `limit: Optional[int]`

  Maximum results per page. Defaults to 1000.

- `page: Optional[str]`

  Opaque pagination cursor from a previous response's next_page. Forward-only.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 26 more]`

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

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

    - `"agent-memory-2026-07-22"`

### Returns

- `class BetaManagedAgentsSessionThread: …`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `id: str`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

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

        - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-6` - Most intelligent model for building agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
          - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

          - `"claude-sonnet-5"`

            High-performance model for coding and agents

          - `"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-4-8"`

            Frontier intelligence for long-running agents and coding

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

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

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

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: bool`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `mcp_server_name: str`

        - `type: Literal["mcp_toolset"]`

          - `"mcp_toolset"`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

        - `description: str`

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `type: Literal["object"]`

            - `"object"`

          - `properties: Optional[Dict[str, object]]`

          - `required: Optional[List[str]]`

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

  - `parent_thread_id: Optional[str]`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: str`

    The session this thread belongs to.

  - `stats: Optional[BetaManagedAgentsSessionThreadStats]`

    Timing statistics for a session thread.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `duration_seconds: Optional[float]`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `startup_seconds: Optional[float]`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `status: BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `type: Literal["session_thread"]`

    - `"session_thread"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `usage: Optional[BetaManagedAgentsSessionThreadUsage]`

    Cumulative token usage for a session thread across all turns.

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

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.sessions.threads.list(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
page = page.data[0]
print(page.id)
```

#### Response

```json
{
  "data": [
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Session Thread

`beta.sessions.threads.retrieve(strthread_id, ThreadRetrieveParams**kwargs)  -> BetaManagedAgentsSessionThread`

**get** `/v1/sessions/{session_id}/threads/{thread_id}`

Get Session Thread

### Parameters

- `session_id: str`

- `thread_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 26 more]`

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

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

    - `"agent-memory-2026-07-22"`

### Returns

- `class BetaManagedAgentsSessionThread: …`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `id: str`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

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

        - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-6` - Most intelligent model for building agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
          - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

          - `"claude-sonnet-5"`

            High-performance model for coding and agents

          - `"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-4-8"`

            Frontier intelligence for long-running agents and coding

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

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

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

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: bool`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `mcp_server_name: str`

        - `type: Literal["mcp_toolset"]`

          - `"mcp_toolset"`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

        - `description: str`

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `type: Literal["object"]`

            - `"object"`

          - `properties: Optional[Dict[str, object]]`

          - `required: Optional[List[str]]`

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

  - `parent_thread_id: Optional[str]`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: str`

    The session this thread belongs to.

  - `stats: Optional[BetaManagedAgentsSessionThreadStats]`

    Timing statistics for a session thread.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `duration_seconds: Optional[float]`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `startup_seconds: Optional[float]`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `status: BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `type: Literal["session_thread"]`

    - `"session_thread"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `usage: Optional[BetaManagedAgentsSessionThreadUsage]`

    Cumulative token usage for a session thread across all turns.

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

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_session_thread = client.beta.sessions.threads.retrieve(
    thread_id="sthr_011CZkZVWa6oIjw0rgXZpnBt",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
print(beta_managed_agents_session_thread.id)
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

## Archive Session Thread

`beta.sessions.threads.archive(strthread_id, ThreadArchiveParams**kwargs)  -> BetaManagedAgentsSessionThread`

**post** `/v1/sessions/{session_id}/threads/{thread_id}/archive`

Archive Session Thread

### Parameters

- `session_id: str`

- `thread_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 26 more]`

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

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

    - `"agent-memory-2026-07-22"`

### Returns

- `class BetaManagedAgentsSessionThread: …`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `id: str`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

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

        - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-6` - Most intelligent model for building agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
          - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

          - `"claude-sonnet-5"`

            High-performance model for coding and agents

          - `"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-4-8"`

            Frontier intelligence for long-running agents and coding

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

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

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

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: bool`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `mcp_server_name: str`

        - `type: Literal["mcp_toolset"]`

          - `"mcp_toolset"`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

        - `description: str`

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `type: Literal["object"]`

            - `"object"`

          - `properties: Optional[Dict[str, object]]`

          - `required: Optional[List[str]]`

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

  - `parent_thread_id: Optional[str]`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: str`

    The session this thread belongs to.

  - `stats: Optional[BetaManagedAgentsSessionThreadStats]`

    Timing statistics for a session thread.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `duration_seconds: Optional[float]`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `startup_seconds: Optional[float]`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `status: BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `type: Literal["session_thread"]`

    - `"session_thread"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `usage: Optional[BetaManagedAgentsSessionThreadUsage]`

    Cumulative token usage for a session thread across all turns.

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

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_session_thread = client.beta.sessions.threads.archive(
    thread_id="sthr_011CZkZVWa6oIjw0rgXZpnBt",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
print(beta_managed_agents_session_thread.id)
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

## Domain Types

### Beta Managed Agents Session Thread

- `class BetaManagedAgentsSessionThread: …`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `id: str`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

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

        - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
          - `claude-opus-4-6` - Most intelligent model for building agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
          - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

          - `"claude-sonnet-5"`

            High-performance model for coding and agents

          - `"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-4-8"`

            Frontier intelligence for long-running agents and coding

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

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

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

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: bool`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

        - `mcp_server_name: str`

        - `type: Literal["mcp_toolset"]`

          - `"mcp_toolset"`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

        - `description: str`

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `type: Literal["object"]`

            - `"object"`

          - `properties: Optional[Dict[str, object]]`

          - `required: Optional[List[str]]`

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

  - `parent_thread_id: Optional[str]`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: str`

    The session this thread belongs to.

  - `stats: Optional[BetaManagedAgentsSessionThreadStats]`

    Timing statistics for a session thread.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `duration_seconds: Optional[float]`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `startup_seconds: Optional[float]`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `status: BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `type: Literal["session_thread"]`

    - `"session_thread"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `usage: Optional[BetaManagedAgentsSessionThreadUsage]`

    Cumulative token usage for a session thread across all turns.

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

### Beta Managed Agents Session Thread Stats

- `class BetaManagedAgentsSessionThreadStats: …`

  Timing statistics for a session thread.

  - `active_seconds: Optional[float]`

    Cumulative time in seconds the thread spent actively running. Excludes idle time.

  - `duration_seconds: Optional[float]`

    Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

  - `startup_seconds: Optional[float]`

    Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

### Beta Managed Agents Session Thread Status

- `Literal["running", "idle", "rescheduling", "terminated"]`

  SessionThreadStatus enum

  - `"running"`

  - `"idle"`

  - `"rescheduling"`

  - `"terminated"`

### Beta Managed Agents Session Thread Usage

- `class BetaManagedAgentsSessionThreadUsage: …`

  Cumulative token usage for a session thread across all turns.

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

### Beta Managed Agents Stream Session Thread Events

- `BetaManagedAgentsStreamSessionThreadEvents`

  Server-sent event in a single thread's stream.

  - `class BetaManagedAgentsUserMessageEvent: …`

    A user message event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `data: str`

              Base64-encoded image data.

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["image"]`

          - `"image"`

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `data: str`

              Base64-encoded document data.

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `data: str`

              The plain text content.

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: Literal["text"]`

              - `"text"`

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["document"]`

          - `"document"`

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

    - `type: Literal["user.message"]`

      - `"user.message"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent: …`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: str`

      Unique identifier for this event.

    - `type: Literal["user.interrupt"]`

      - `"user.interrupt"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent: …`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: str`

      Unique identifier for this event.

    - `result: Literal["allow", "deny"]`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: str`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_confirmation"]`

      - `"user.tool_confirmation"`

    - `deny_message: Optional[str]`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent: …`

    Event sent by the client providing the result of a custom tool execution.

    - `id: str`

      Unique identifier for this event.

    - `custom_tool_use_id: str`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.custom_tool_result"]`

      - `"user.custom_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: bool`

            Whether citations are enabled for this search result.

        - `content: List[BetaManagedAgentsSearchResultContent]`

          Array of text content blocks from the search result.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `source: str`

          The URL source of the search result.

        - `title: str`

          The title of the search result.

        - `type: Literal["search_result"]`

          - `"search_result"`

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent: …`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the custom tool being called.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.custom_tool_use"]`

      - `"agent.custom_tool_use"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent: …`

    An agent response event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsTextBlock]`

      Array of text blocks comprising the agent response.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.message"]`

      - `"agent.message"`

  - `class BetaManagedAgentsAgentThinkingEvent: …`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thinking"]`

      - `"agent.thinking"`

  - `class BetaManagedAgentsAgentMCPToolUseEvent: …`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `mcp_server_name: str`

      Name of the MCP server providing the tool.

    - `name: str`

      Name of the MCP tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.mcp_tool_use"]`

      - `"agent.mcp_tool_use"`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMCPToolResultEvent: …`

    Event representing the result of an MCP tool execution.

    - `id: str`

      Unique identifier for this event.

    - `mcp_tool_use_id: str`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.mcp_tool_result"]`

      - `"agent.mcp_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent: …`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the agent tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.tool_use"]`

      - `"agent.tool_use"`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent: …`

    Event representing the result of an agent tool execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: Literal["agent.tool_result"]`

      - `"agent.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent: …`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `from_session_thread_id: str`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thread_message_received"]`

      - `"agent.thread_message_received"`

    - `from_agent_name: Optional[str]`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent: …`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `to_session_thread_id: str`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: Literal["agent.thread_message_sent"]`

      - `"agent.thread_message_sent"`

    - `to_agent_name: Optional[str]`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent: …`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thread_context_compacted"]`

      - `"agent.thread_context_compacted"`

  - `class BetaManagedAgentsSessionErrorEvent: …`

    An error event indicating a problem occurred during session execution.

    - `id: str`

      Unique identifier for this event.

    - `error: Error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError: …`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: Literal["retrying"]`

              - `"retrying"`

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: Literal["exhausted"]`

              - `"exhausted"`

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: Literal["terminal"]`

              - `"terminal"`

        - `type: Literal["unknown_error"]`

          - `"unknown_error"`

      - `class BetaManagedAgentsModelOverloadedError: …`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_overloaded_error"]`

          - `"model_overloaded_error"`

      - `class BetaManagedAgentsModelRateLimitedError: …`

        The model request was rate-limited.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_rate_limited_error"]`

          - `"model_rate_limited_error"`

      - `class BetaManagedAgentsModelRequestFailedError: …`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_request_failed_error"]`

          - `"model_request_failed_error"`

      - `class BetaManagedAgentsMCPConnectionFailedError: …`

        Failed to connect to an MCP server.

        - `mcp_server_name: str`

          Name of the MCP server that failed to connect.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_connection_failed_error"]`

          - `"mcp_connection_failed_error"`

      - `class BetaManagedAgentsMCPAuthenticationFailedError: …`

        Authentication to an MCP server failed.

        - `mcp_server_name: str`

          Name of the MCP server that failed authentication.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_authentication_failed_error"]`

          - `"mcp_authentication_failed_error"`

      - `class BetaManagedAgentsBillingError: …`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["billing_error"]`

          - `"billing_error"`

      - `class BetaManagedAgentsCredentialHostUnreachableError: …`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: str`

          ID of the affected credential.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["credential_host_unreachable_error"]`

          - `"credential_host_unreachable_error"`

        - `vault_id: str`

          ID of the vault containing the affected credential.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.error"]`

      - `"session.error"`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent: …`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_rescheduled"]`

      - `"session.status_rescheduled"`

  - `class BetaManagedAgentsSessionStatusRunningEvent: …`

    Indicates the session is actively running and the agent is working.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_running"]`

      - `"session.status_running"`

  - `class BetaManagedAgentsSessionStatusIdleEvent: …`

    Indicates the agent has paused and is awaiting user input.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: Literal["end_turn"]`

          - `"end_turn"`

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: List[str]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: Literal["requires_action"]`

          - `"requires_action"`

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `type: Literal["retries_exhausted"]`

          - `"retries_exhausted"`

    - `type: Literal["session.status_idle"]`

      - `"session.status_idle"`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent: …`

    Indicates the session has terminated, either due to an error or completion.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_terminated"]`

      - `"session.status_terminated"`

  - `class BetaManagedAgentsSessionThreadCreatedEvent: …`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the callable agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public `sthr_` ID of the newly created thread.

    - `type: Literal["session.thread_created"]`

      - `"session.thread_created"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent: …`

    Emitted when an outcome evaluation cycle begins.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.outcome_evaluation_start"]`

      - `"span.outcome_evaluation_start"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent: …`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `id: str`

      Unique identifier for this event.

    - `explanation: str`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_evaluation_start_id: str`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `result: str`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `type: Literal["span.outcome_evaluation_end"]`

      - `"span.outcome_evaluation_end"`

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: int`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: int`

        Tokens read from prompt cache in this request.

      - `input_tokens: int`

        Input tokens consumed by this request.

      - `output_tokens: int`

        Output tokens generated by this request.

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `class BetaManagedAgentsSpanModelRequestStartEvent: …`

    Emitted when a model request is initiated by the agent.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.model_request_start"]`

      - `"span.model_request_start"`

  - `class BetaManagedAgentsSpanModelRequestEndEvent: …`

    Emitted when a model request completes.

    - `id: str`

      Unique identifier for this event.

    - `is_error: Optional[bool]`

      Whether the model request resulted in an error.

    - `model_request_start_id: str`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.model_request_end"]`

      - `"span.model_request_end"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent: …`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.outcome_evaluation_ongoing"]`

      - `"span.outcome_evaluation_ongoing"`

  - `class BetaManagedAgentsUserDefineOutcomeEvent: …`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: str`

      Unique identifier for this event.

    - `description: str`

      What the agent should produce. Copied from the input event.

    - `max_iterations: Optional[int]`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `outcome_id: str`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric: …`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: str`

          ID of the rubric file.

        - `type: Literal["file"]`

          - `"file"`

      - `class BetaManagedAgentsTextRubric: …`

        Rubric content provided inline as text.

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: Literal["text"]`

          - `"text"`

    - `type: Literal["user.define_outcome"]`

      - `"user.define_outcome"`

  - `class BetaManagedAgentsSessionDeletedEvent: …`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.deleted"]`

      - `"session.deleted"`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent: …`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that started running.

    - `type: Literal["session.thread_status_running"]`

      - `"session.thread_status_running"`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent: …`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

    - `type: Literal["session.thread_status_idle"]`

      - `"session.thread_status_idle"`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent: …`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that terminated.

    - `type: Literal["session.thread_status_terminated"]`

      - `"session.thread_status_terminated"`

  - `class BetaManagedAgentsUserToolResultEvent: …`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: str`

      Unique identifier for this event.

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_result"]`

      - `"user.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent: …`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that is retrying.

    - `type: Literal["session.thread_status_rescheduled"]`

      - `"session.thread_status_rescheduled"`

  - `class BetaManagedAgentsSessionUpdatedEvent: …`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.updated"]`

      - `"session.updated"`

    - `agent: Optional[BetaManagedAgentsSessionAgent]`

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

          - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `claude-sonnet-5` - High-performance model for coding and agents
            - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
            - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
            - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
            - `claude-opus-4-6` - Most intelligent model for building agents and coding
            - `claude-sonnet-4-6` - Best combination of speed and intelligence
            - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
            - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
            - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
            - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
            - `claude-sonnet-4-5` - High-performance model for agents and coding
            - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

            - `"claude-sonnet-5"`

              High-performance model for coding and agents

            - `"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `"claude-opus-4-8"`

              Frontier intelligence for long-running agents and coding

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

      - `multiagent: Optional[BetaManagedAgentsSessionMultiagentCoordinator]`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `agents: List[BetaManagedAgentsSessionThreadAgent]`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `id: str`

          - `description: Optional[str]`

          - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

            - `name: str`

            - `type: Literal["url"]`

            - `url: str`

          - `model: BetaManagedAgentsModelConfig`

            Model identifier and configuration.

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

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

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

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `mcp_server_name: str`

              - `type: Literal["mcp_toolset"]`

                - `"mcp_toolset"`

            - `class BetaManagedAgentsCustomTool: …`

              A custom tool as returned in API responses.

              - `description: str`

              - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `type: Literal["object"]`

                  - `"object"`

                - `properties: Optional[Dict[str, object]]`

                - `required: Optional[List[str]]`

              - `name: str`

              - `type: Literal["custom"]`

                - `"custom"`

          - `type: Literal["agent"]`

            - `"agent"`

          - `version: int`

        - `type: Literal["coordinator"]`

          - `"coordinator"`

      - `name: str`

      - `skills: List[Skill]`

        - `class BetaManagedAgentsAnthropicSkill: …`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill: …`

          A resolved user-created custom skill.

      - `system: Optional[str]`

      - `tools: List[Tool]`

        - `class BetaManagedAgentsAgentToolset20260401: …`

        - `class BetaManagedAgentsMCPToolset: …`

        - `class BetaManagedAgentsCustomTool: …`

          A custom tool as returned in API responses.

      - `type: Literal["agent"]`

        - `"agent"`

      - `version: int`

    - `metadata: Optional[Dict[str, str]]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: Optional[str]`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent: …`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `event: BetaManagedAgentsStartEventPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `class BetaManagedAgentsAgentMessagePreview: …`

        - `id: str`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `type: Literal["agent.message"]`

          - `"agent.message"`

      - `class BetaManagedAgentsAgentThinkingPreview: …`

        - `id: str`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `type: Literal["agent.thinking"]`

          - `"agent.thinking"`

    - `type: Literal["event_start"]`

      - `"event_start"`

  - `class BetaManagedAgentsDeltaEvent: …`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `delta: BetaManagedAgentsDeltaContent`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `content: BetaManagedAgentsTextBlock`

        Regular text content.

      - `type: Literal["content_delta"]`

        - `"content_delta"`

      - `index: Optional[int]`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

    - `event_id: str`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `type: Literal["event_delta"]`

      - `"event_delta"`

  - `class BetaManagedAgentsSystemMessageEvent: …`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks. Text-only.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `type: Literal["system.message"]`

      - `"system.message"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

# Events

## List Session Thread Events

`beta.sessions.threads.events.list(strthread_id, EventListParams**kwargs)  -> SyncPageCursor[BetaManagedAgentsSessionEvent]`

**get** `/v1/sessions/{session_id}/threads/{thread_id}/events`

List Session Thread Events

### Parameters

- `session_id: str`

- `thread_id: str`

- `limit: Optional[int]`

  Query parameter for limit

- `page: Optional[str]`

  Query parameter for page

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 26 more]`

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

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

    - `"agent-memory-2026-07-22"`

### Returns

- `BetaManagedAgentsSessionEvent`

  Union type for all event types in a session.

  - `class BetaManagedAgentsUserMessageEvent: …`

    A user message event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `data: str`

              Base64-encoded image data.

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["image"]`

          - `"image"`

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `data: str`

              Base64-encoded document data.

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `data: str`

              The plain text content.

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: Literal["text"]`

              - `"text"`

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["document"]`

          - `"document"`

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

    - `type: Literal["user.message"]`

      - `"user.message"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent: …`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: str`

      Unique identifier for this event.

    - `type: Literal["user.interrupt"]`

      - `"user.interrupt"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent: …`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: str`

      Unique identifier for this event.

    - `result: Literal["allow", "deny"]`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: str`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_confirmation"]`

      - `"user.tool_confirmation"`

    - `deny_message: Optional[str]`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent: …`

    Event sent by the client providing the result of a custom tool execution.

    - `id: str`

      Unique identifier for this event.

    - `custom_tool_use_id: str`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.custom_tool_result"]`

      - `"user.custom_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: bool`

            Whether citations are enabled for this search result.

        - `content: List[BetaManagedAgentsSearchResultContent]`

          Array of text content blocks from the search result.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `source: str`

          The URL source of the search result.

        - `title: str`

          The title of the search result.

        - `type: Literal["search_result"]`

          - `"search_result"`

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent: …`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the custom tool being called.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.custom_tool_use"]`

      - `"agent.custom_tool_use"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent: …`

    An agent response event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsTextBlock]`

      Array of text blocks comprising the agent response.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.message"]`

      - `"agent.message"`

  - `class BetaManagedAgentsAgentThinkingEvent: …`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thinking"]`

      - `"agent.thinking"`

  - `class BetaManagedAgentsAgentMCPToolUseEvent: …`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `mcp_server_name: str`

      Name of the MCP server providing the tool.

    - `name: str`

      Name of the MCP tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.mcp_tool_use"]`

      - `"agent.mcp_tool_use"`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMCPToolResultEvent: …`

    Event representing the result of an MCP tool execution.

    - `id: str`

      Unique identifier for this event.

    - `mcp_tool_use_id: str`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.mcp_tool_result"]`

      - `"agent.mcp_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent: …`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the agent tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.tool_use"]`

      - `"agent.tool_use"`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent: …`

    Event representing the result of an agent tool execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: Literal["agent.tool_result"]`

      - `"agent.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent: …`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `from_session_thread_id: str`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thread_message_received"]`

      - `"agent.thread_message_received"`

    - `from_agent_name: Optional[str]`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent: …`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `to_session_thread_id: str`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: Literal["agent.thread_message_sent"]`

      - `"agent.thread_message_sent"`

    - `to_agent_name: Optional[str]`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent: …`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thread_context_compacted"]`

      - `"agent.thread_context_compacted"`

  - `class BetaManagedAgentsSessionErrorEvent: …`

    An error event indicating a problem occurred during session execution.

    - `id: str`

      Unique identifier for this event.

    - `error: Error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError: …`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: Literal["retrying"]`

              - `"retrying"`

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: Literal["exhausted"]`

              - `"exhausted"`

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: Literal["terminal"]`

              - `"terminal"`

        - `type: Literal["unknown_error"]`

          - `"unknown_error"`

      - `class BetaManagedAgentsModelOverloadedError: …`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_overloaded_error"]`

          - `"model_overloaded_error"`

      - `class BetaManagedAgentsModelRateLimitedError: …`

        The model request was rate-limited.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_rate_limited_error"]`

          - `"model_rate_limited_error"`

      - `class BetaManagedAgentsModelRequestFailedError: …`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_request_failed_error"]`

          - `"model_request_failed_error"`

      - `class BetaManagedAgentsMCPConnectionFailedError: …`

        Failed to connect to an MCP server.

        - `mcp_server_name: str`

          Name of the MCP server that failed to connect.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_connection_failed_error"]`

          - `"mcp_connection_failed_error"`

      - `class BetaManagedAgentsMCPAuthenticationFailedError: …`

        Authentication to an MCP server failed.

        - `mcp_server_name: str`

          Name of the MCP server that failed authentication.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_authentication_failed_error"]`

          - `"mcp_authentication_failed_error"`

      - `class BetaManagedAgentsBillingError: …`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["billing_error"]`

          - `"billing_error"`

      - `class BetaManagedAgentsCredentialHostUnreachableError: …`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: str`

          ID of the affected credential.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["credential_host_unreachable_error"]`

          - `"credential_host_unreachable_error"`

        - `vault_id: str`

          ID of the vault containing the affected credential.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.error"]`

      - `"session.error"`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent: …`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_rescheduled"]`

      - `"session.status_rescheduled"`

  - `class BetaManagedAgentsSessionStatusRunningEvent: …`

    Indicates the session is actively running and the agent is working.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_running"]`

      - `"session.status_running"`

  - `class BetaManagedAgentsSessionStatusIdleEvent: …`

    Indicates the agent has paused and is awaiting user input.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: Literal["end_turn"]`

          - `"end_turn"`

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: List[str]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: Literal["requires_action"]`

          - `"requires_action"`

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `type: Literal["retries_exhausted"]`

          - `"retries_exhausted"`

    - `type: Literal["session.status_idle"]`

      - `"session.status_idle"`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent: …`

    Indicates the session has terminated, either due to an error or completion.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_terminated"]`

      - `"session.status_terminated"`

  - `class BetaManagedAgentsSessionThreadCreatedEvent: …`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the callable agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public `sthr_` ID of the newly created thread.

    - `type: Literal["session.thread_created"]`

      - `"session.thread_created"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent: …`

    Emitted when an outcome evaluation cycle begins.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.outcome_evaluation_start"]`

      - `"span.outcome_evaluation_start"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent: …`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `id: str`

      Unique identifier for this event.

    - `explanation: str`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_evaluation_start_id: str`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `result: str`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `type: Literal["span.outcome_evaluation_end"]`

      - `"span.outcome_evaluation_end"`

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: int`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: int`

        Tokens read from prompt cache in this request.

      - `input_tokens: int`

        Input tokens consumed by this request.

      - `output_tokens: int`

        Output tokens generated by this request.

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `class BetaManagedAgentsSpanModelRequestStartEvent: …`

    Emitted when a model request is initiated by the agent.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.model_request_start"]`

      - `"span.model_request_start"`

  - `class BetaManagedAgentsSpanModelRequestEndEvent: …`

    Emitted when a model request completes.

    - `id: str`

      Unique identifier for this event.

    - `is_error: Optional[bool]`

      Whether the model request resulted in an error.

    - `model_request_start_id: str`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.model_request_end"]`

      - `"span.model_request_end"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent: …`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.outcome_evaluation_ongoing"]`

      - `"span.outcome_evaluation_ongoing"`

  - `class BetaManagedAgentsUserDefineOutcomeEvent: …`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: str`

      Unique identifier for this event.

    - `description: str`

      What the agent should produce. Copied from the input event.

    - `max_iterations: Optional[int]`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `outcome_id: str`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric: …`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: str`

          ID of the rubric file.

        - `type: Literal["file"]`

          - `"file"`

      - `class BetaManagedAgentsTextRubric: …`

        Rubric content provided inline as text.

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: Literal["text"]`

          - `"text"`

    - `type: Literal["user.define_outcome"]`

      - `"user.define_outcome"`

  - `class BetaManagedAgentsSessionDeletedEvent: …`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.deleted"]`

      - `"session.deleted"`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent: …`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that started running.

    - `type: Literal["session.thread_status_running"]`

      - `"session.thread_status_running"`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent: …`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

    - `type: Literal["session.thread_status_idle"]`

      - `"session.thread_status_idle"`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent: …`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that terminated.

    - `type: Literal["session.thread_status_terminated"]`

      - `"session.thread_status_terminated"`

  - `class BetaManagedAgentsUserToolResultEvent: …`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: str`

      Unique identifier for this event.

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_result"]`

      - `"user.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent: …`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that is retrying.

    - `type: Literal["session.thread_status_rescheduled"]`

      - `"session.thread_status_rescheduled"`

  - `class BetaManagedAgentsSessionUpdatedEvent: …`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.updated"]`

      - `"session.updated"`

    - `agent: Optional[BetaManagedAgentsSessionAgent]`

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

          - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `claude-sonnet-5` - High-performance model for coding and agents
            - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
            - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
            - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
            - `claude-opus-4-6` - Most intelligent model for building agents and coding
            - `claude-sonnet-4-6` - Best combination of speed and intelligence
            - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
            - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
            - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
            - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
            - `claude-sonnet-4-5` - High-performance model for agents and coding
            - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

            - `"claude-sonnet-5"`

              High-performance model for coding and agents

            - `"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `"claude-opus-4-8"`

              Frontier intelligence for long-running agents and coding

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

      - `multiagent: Optional[BetaManagedAgentsSessionMultiagentCoordinator]`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `agents: List[BetaManagedAgentsSessionThreadAgent]`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `id: str`

          - `description: Optional[str]`

          - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

            - `name: str`

            - `type: Literal["url"]`

            - `url: str`

          - `model: BetaManagedAgentsModelConfig`

            Model identifier and configuration.

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

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

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

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `mcp_server_name: str`

              - `type: Literal["mcp_toolset"]`

                - `"mcp_toolset"`

            - `class BetaManagedAgentsCustomTool: …`

              A custom tool as returned in API responses.

              - `description: str`

              - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `type: Literal["object"]`

                  - `"object"`

                - `properties: Optional[Dict[str, object]]`

                - `required: Optional[List[str]]`

              - `name: str`

              - `type: Literal["custom"]`

                - `"custom"`

          - `type: Literal["agent"]`

            - `"agent"`

          - `version: int`

        - `type: Literal["coordinator"]`

          - `"coordinator"`

      - `name: str`

      - `skills: List[Skill]`

        - `class BetaManagedAgentsAnthropicSkill: …`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill: …`

          A resolved user-created custom skill.

      - `system: Optional[str]`

      - `tools: List[Tool]`

        - `class BetaManagedAgentsAgentToolset20260401: …`

        - `class BetaManagedAgentsMCPToolset: …`

        - `class BetaManagedAgentsCustomTool: …`

          A custom tool as returned in API responses.

      - `type: Literal["agent"]`

        - `"agent"`

      - `version: int`

    - `metadata: Optional[Dict[str, str]]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: Optional[str]`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsSystemMessageEvent: …`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks. Text-only.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `type: Literal["system.message"]`

      - `"system.message"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.sessions.threads.events.list(
    thread_id="sthr_011CZkZVWa6oIjw0rgXZpnBt",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
page = page.data[0]
print(page)
```

#### Response

```json
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "next_page"
}
```

## Stream Session Thread Events

`beta.sessions.threads.events.stream(strthread_id, EventStreamParams**kwargs)  -> BetaManagedAgentsStreamSessionThreadEvents`

**get** `/v1/sessions/{session_id}/threads/{thread_id}/stream`

Stream Session Thread Events

### Parameters

- `session_id: str`

- `thread_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 26 more]`

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

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

    - `"agent-memory-2026-07-22"`

### Returns

- `BetaManagedAgentsStreamSessionThreadEvents`

  Server-sent event in a single thread's stream.

  - `class BetaManagedAgentsUserMessageEvent: …`

    A user message event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `data: str`

              Base64-encoded image data.

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["image"]`

          - `"image"`

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `data: str`

              Base64-encoded document data.

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `data: str`

              The plain text content.

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: Literal["text"]`

              - `"text"`

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["document"]`

          - `"document"`

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

    - `type: Literal["user.message"]`

      - `"user.message"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent: …`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: str`

      Unique identifier for this event.

    - `type: Literal["user.interrupt"]`

      - `"user.interrupt"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent: …`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: str`

      Unique identifier for this event.

    - `result: Literal["allow", "deny"]`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: str`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_confirmation"]`

      - `"user.tool_confirmation"`

    - `deny_message: Optional[str]`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent: …`

    Event sent by the client providing the result of a custom tool execution.

    - `id: str`

      Unique identifier for this event.

    - `custom_tool_use_id: str`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.custom_tool_result"]`

      - `"user.custom_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: bool`

            Whether citations are enabled for this search result.

        - `content: List[BetaManagedAgentsSearchResultContent]`

          Array of text content blocks from the search result.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `source: str`

          The URL source of the search result.

        - `title: str`

          The title of the search result.

        - `type: Literal["search_result"]`

          - `"search_result"`

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent: …`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the custom tool being called.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.custom_tool_use"]`

      - `"agent.custom_tool_use"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent: …`

    An agent response event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsTextBlock]`

      Array of text blocks comprising the agent response.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.message"]`

      - `"agent.message"`

  - `class BetaManagedAgentsAgentThinkingEvent: …`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thinking"]`

      - `"agent.thinking"`

  - `class BetaManagedAgentsAgentMCPToolUseEvent: …`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `mcp_server_name: str`

      Name of the MCP server providing the tool.

    - `name: str`

      Name of the MCP tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.mcp_tool_use"]`

      - `"agent.mcp_tool_use"`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMCPToolResultEvent: …`

    Event representing the result of an MCP tool execution.

    - `id: str`

      Unique identifier for this event.

    - `mcp_tool_use_id: str`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.mcp_tool_result"]`

      - `"agent.mcp_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent: …`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the agent tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.tool_use"]`

      - `"agent.tool_use"`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent: …`

    Event representing the result of an agent tool execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: Literal["agent.tool_result"]`

      - `"agent.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent: …`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `from_session_thread_id: str`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thread_message_received"]`

      - `"agent.thread_message_received"`

    - `from_agent_name: Optional[str]`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent: …`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `to_session_thread_id: str`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: Literal["agent.thread_message_sent"]`

      - `"agent.thread_message_sent"`

    - `to_agent_name: Optional[str]`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent: …`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["agent.thread_context_compacted"]`

      - `"agent.thread_context_compacted"`

  - `class BetaManagedAgentsSessionErrorEvent: …`

    An error event indicating a problem occurred during session execution.

    - `id: str`

      Unique identifier for this event.

    - `error: Error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError: …`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: Literal["retrying"]`

              - `"retrying"`

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: Literal["exhausted"]`

              - `"exhausted"`

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: Literal["terminal"]`

              - `"terminal"`

        - `type: Literal["unknown_error"]`

          - `"unknown_error"`

      - `class BetaManagedAgentsModelOverloadedError: …`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_overloaded_error"]`

          - `"model_overloaded_error"`

      - `class BetaManagedAgentsModelRateLimitedError: …`

        The model request was rate-limited.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_rate_limited_error"]`

          - `"model_rate_limited_error"`

      - `class BetaManagedAgentsModelRequestFailedError: …`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_request_failed_error"]`

          - `"model_request_failed_error"`

      - `class BetaManagedAgentsMCPConnectionFailedError: …`

        Failed to connect to an MCP server.

        - `mcp_server_name: str`

          Name of the MCP server that failed to connect.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_connection_failed_error"]`

          - `"mcp_connection_failed_error"`

      - `class BetaManagedAgentsMCPAuthenticationFailedError: …`

        Authentication to an MCP server failed.

        - `mcp_server_name: str`

          Name of the MCP server that failed authentication.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_authentication_failed_error"]`

          - `"mcp_authentication_failed_error"`

      - `class BetaManagedAgentsBillingError: …`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["billing_error"]`

          - `"billing_error"`

      - `class BetaManagedAgentsCredentialHostUnreachableError: …`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: str`

          ID of the affected credential.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["credential_host_unreachable_error"]`

          - `"credential_host_unreachable_error"`

        - `vault_id: str`

          ID of the vault containing the affected credential.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.error"]`

      - `"session.error"`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent: …`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_rescheduled"]`

      - `"session.status_rescheduled"`

  - `class BetaManagedAgentsSessionStatusRunningEvent: …`

    Indicates the session is actively running and the agent is working.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_running"]`

      - `"session.status_running"`

  - `class BetaManagedAgentsSessionStatusIdleEvent: …`

    Indicates the agent has paused and is awaiting user input.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: Literal["end_turn"]`

          - `"end_turn"`

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: List[str]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: Literal["requires_action"]`

          - `"requires_action"`

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `type: Literal["retries_exhausted"]`

          - `"retries_exhausted"`

    - `type: Literal["session.status_idle"]`

      - `"session.status_idle"`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent: …`

    Indicates the session has terminated, either due to an error or completion.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.status_terminated"]`

      - `"session.status_terminated"`

  - `class BetaManagedAgentsSessionThreadCreatedEvent: …`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the callable agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public `sthr_` ID of the newly created thread.

    - `type: Literal["session.thread_created"]`

      - `"session.thread_created"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent: …`

    Emitted when an outcome evaluation cycle begins.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.outcome_evaluation_start"]`

      - `"span.outcome_evaluation_start"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent: …`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `id: str`

      Unique identifier for this event.

    - `explanation: str`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_evaluation_start_id: str`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `result: str`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `type: Literal["span.outcome_evaluation_end"]`

      - `"span.outcome_evaluation_end"`

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: int`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: int`

        Tokens read from prompt cache in this request.

      - `input_tokens: int`

        Input tokens consumed by this request.

      - `output_tokens: int`

        Output tokens generated by this request.

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `class BetaManagedAgentsSpanModelRequestStartEvent: …`

    Emitted when a model request is initiated by the agent.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.model_request_start"]`

      - `"span.model_request_start"`

  - `class BetaManagedAgentsSpanModelRequestEndEvent: …`

    Emitted when a model request completes.

    - `id: str`

      Unique identifier for this event.

    - `is_error: Optional[bool]`

      Whether the model request resulted in an error.

    - `model_request_start_id: str`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.model_request_end"]`

      - `"span.model_request_end"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent: …`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["span.outcome_evaluation_ongoing"]`

      - `"span.outcome_evaluation_ongoing"`

  - `class BetaManagedAgentsUserDefineOutcomeEvent: …`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: str`

      Unique identifier for this event.

    - `description: str`

      What the agent should produce. Copied from the input event.

    - `max_iterations: Optional[int]`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `outcome_id: str`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric: …`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: str`

          ID of the rubric file.

        - `type: Literal["file"]`

          - `"file"`

      - `class BetaManagedAgentsTextRubric: …`

        Rubric content provided inline as text.

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: Literal["text"]`

          - `"text"`

    - `type: Literal["user.define_outcome"]`

      - `"user.define_outcome"`

  - `class BetaManagedAgentsSessionDeletedEvent: …`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.deleted"]`

      - `"session.deleted"`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent: …`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that started running.

    - `type: Literal["session.thread_status_running"]`

      - `"session.thread_status_running"`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent: …`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

    - `type: Literal["session.thread_status_idle"]`

      - `"session.thread_status_idle"`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent: …`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that terminated.

    - `type: Literal["session.thread_status_terminated"]`

      - `"session.thread_status_terminated"`

  - `class BetaManagedAgentsUserToolResultEvent: …`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: str`

      Unique identifier for this event.

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_result"]`

      - `"user.tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent: …`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `session_thread_id: str`

      Public sthr_ ID of the thread that is retrying.

    - `type: Literal["session.thread_status_rescheduled"]`

      - `"session.thread_status_rescheduled"`

  - `class BetaManagedAgentsSessionUpdatedEvent: …`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.updated"]`

      - `"session.updated"`

    - `agent: Optional[BetaManagedAgentsSessionAgent]`

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

          - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-4-8", 9 more]`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `claude-sonnet-5` - High-performance model for coding and agents
            - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
            - `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
            - `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
            - `claude-opus-4-6` - Most intelligent model for building agents and coding
            - `claude-sonnet-4-6` - Best combination of speed and intelligence
            - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
            - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
            - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
            - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
            - `claude-sonnet-4-5` - High-performance model for agents and coding
            - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

            - `"claude-sonnet-5"`

              High-performance model for coding and agents

            - `"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `"claude-opus-4-8"`

              Frontier intelligence for long-running agents and coding

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

      - `multiagent: Optional[BetaManagedAgentsSessionMultiagentCoordinator]`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `agents: List[BetaManagedAgentsSessionThreadAgent]`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `id: str`

          - `description: Optional[str]`

          - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

            - `name: str`

            - `type: Literal["url"]`

            - `url: str`

          - `model: BetaManagedAgentsModelConfig`

            Model identifier and configuration.

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

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

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

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

              - `mcp_server_name: str`

              - `type: Literal["mcp_toolset"]`

                - `"mcp_toolset"`

            - `class BetaManagedAgentsCustomTool: …`

              A custom tool as returned in API responses.

              - `description: str`

              - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `type: Literal["object"]`

                  - `"object"`

                - `properties: Optional[Dict[str, object]]`

                - `required: Optional[List[str]]`

              - `name: str`

              - `type: Literal["custom"]`

                - `"custom"`

          - `type: Literal["agent"]`

            - `"agent"`

          - `version: int`

        - `type: Literal["coordinator"]`

          - `"coordinator"`

      - `name: str`

      - `skills: List[Skill]`

        - `class BetaManagedAgentsAnthropicSkill: …`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill: …`

          A resolved user-created custom skill.

      - `system: Optional[str]`

      - `tools: List[Tool]`

        - `class BetaManagedAgentsAgentToolset20260401: …`

        - `class BetaManagedAgentsMCPToolset: …`

        - `class BetaManagedAgentsCustomTool: …`

          A custom tool as returned in API responses.

      - `type: Literal["agent"]`

        - `"agent"`

      - `version: int`

    - `metadata: Optional[Dict[str, str]]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: Optional[str]`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent: …`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `event: BetaManagedAgentsStartEventPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `class BetaManagedAgentsAgentMessagePreview: …`

        - `id: str`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `type: Literal["agent.message"]`

          - `"agent.message"`

      - `class BetaManagedAgentsAgentThinkingPreview: …`

        - `id: str`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `type: Literal["agent.thinking"]`

          - `"agent.thinking"`

    - `type: Literal["event_start"]`

      - `"event_start"`

  - `class BetaManagedAgentsDeltaEvent: …`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `delta: BetaManagedAgentsDeltaContent`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `content: BetaManagedAgentsTextBlock`

        Regular text content.

      - `type: Literal["content_delta"]`

        - `"content_delta"`

      - `index: Optional[int]`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

    - `event_id: str`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `type: Literal["event_delta"]`

      - `"event_delta"`

  - `class BetaManagedAgentsSystemMessageEvent: …`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks. Text-only.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `type: Literal["system.message"]`

      - `"system.message"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
for event in client.beta.sessions.threads.events.stream(
    thread_id="sthr_011CZkZVWa6oIjw0rgXZpnBt",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
):
  print(event)
```

#### Response

```json
{
  "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
  "content": [
    {
      "text": "Where is my order #1234?",
      "type": "text"
    }
  ],
  "type": "user.message",
  "processed_at": "2026-03-15T10:00:00Z"
}
```
