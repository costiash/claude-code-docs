## Archive Session

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

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

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

        - `CLAUDE_OPUS_4_8("claude-opus-4-8")`

          Frontier intelligence for long-running agents and coding

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

    - `Optional<BetaManagedAgentsSessionMultiagentCoordinator> multiagent`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `List<BetaManagedAgentsSessionThreadAgent> agents`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `String id`

        - `Optional<String> description`

        - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

          - `String name`

          - `Type type`

          - `String url`

        - `BetaManagedAgentsModelConfig model`

          Model identifier and configuration.

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

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

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

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

            - `BetaManagedAgentsMcpToolsetDefaultConfig defaultConfig`

              Resolved default configuration for all tools from an MCP server.

              - `boolean enabled`

              - `PermissionPolicy permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

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

      - `Type type`

        - `COORDINATOR("coordinator")`

    - `String name`

    - `List<Skill> skills`

      - `class BetaManagedAgentsAnthropicSkill:`

        A resolved Anthropic-managed skill.

      - `class BetaManagedAgentsCustomSkill:`

        A resolved user-created custom skill.

    - `Optional<String> system`

    - `List<Tool> tools`

      - `class BetaManagedAgentsAgentToolset20260401:`

      - `class BetaManagedAgentsMcpToolset:`

      - `class BetaManagedAgentsCustomTool:`

        A custom tool as returned in API responses.

    - `Type type`

      - `AGENT("agent")`

    - `long version`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String environmentId`

  - `Metadata metadata`

  - `List<BetaManagedAgentsOutcomeEvaluationResource> outcomeEvaluations`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

    - `Optional<LocalDateTime> completedAt`

      A timestamp in RFC 3339 format

    - `String description`

      What the agent should produce.

    - `Optional<String> explanation`

      Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

    - `long iteration`

      0-indexed revision cycle the outcome is currently on.

    - `String outcomeId`

      Server-generated outc_ ID for this outcome.

    - `String result`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `Type type`

      - `OUTCOME_EVALUATION("outcome_evaluation")`

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

    - `class BetaManagedAgentsMemoryStoreResource:`

      A memory store attached to an agent session.

      - `String memoryStoreId`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type type`

        - `MEMORY_STORE("memory_store")`

      - `Optional<Access> access`

        Access mode for an attached memory store.

        - `READ_WRITE("read_write")`

        - `READ_ONLY("read_only")`

      - `Optional<String> description`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `Optional<String> instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      - `Optional<String> mountPath`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `Optional<String> name`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

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
  ]
}
```
