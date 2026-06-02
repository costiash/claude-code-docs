## Poll for Work

`BetaSelfHostedWork beta().environments().work().poll(WorkPollParamsparams = WorkPollParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/environments/{environment_id}/work/poll`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Long poll for work items in the queue.

### Parameters

- `WorkPollParams params`

  - `Optional<String> environmentId`

  - `Optional<Long> blockMs`

    How long to wait for work to arrive before returning. Must be 1-999 in milliseconds. Defaults to non-blocking (returns immediately if no work is available).

  - `Optional<Long> reclaimOlderThanMs`

    Reclaim unacknowledged work items older than this many milliseconds. If omitted, uses the default (5000ms).

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

  - `Optional<String> anthropicWorkerId`

    Unique identifier for the specific worker polling, used to track aggregated environment-level work metrics in Console

### Returns

- `class BetaSelfHostedWork:`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `String id`

    Work identifier (e.g., 'work_...')

  - `Optional<String> acknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `String createdAt`

    RFC 3339 timestamp when work was created

  - `BetaSessionWorkData data`

    The actual work to be performed

    - `String id`

      Session identifier (e.g., 'session_...')

    - `JsonValue; type "session"constant`

      Type of work data

      - `SESSION("session")`

  - `String environmentId`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `Optional<String> latestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `Metadata metadata`

    User-provided metadata key-value pairs associated with this work item

  - `Optional<String> startedAt`

    RFC 3339 timestamp when work execution started

  - `State state`

    Current state of the work item

    - `QUEUED("queued")`

    - `STARTING("starting")`

    - `ACTIVE("active")`

    - `STOPPING("stopping")`

    - `STOPPED("stopped")`

  - `Optional<String> stopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `Optional<String> stoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `JsonValue; type "work"constant`

    The type of object (always 'work')

    - `WORK("work")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.environments.work.BetaSelfHostedWork;
import com.anthropic.models.beta.environments.work.WorkPollParams;
import java.util.Optional;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        Optional<BetaSelfHostedWork> betaSelfHostedWork = client.beta().environments().work().poll("env_011CZkZ9X2dpNyB7HsEFoRfW");
    }
}
```

#### Response

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```
