# Work

## Get Work Item

`BetaSelfHostedWork Beta.Environments.Work.Retrieve(WorkRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/environments/{environment_id}/work/{work_id}`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Retrieve detailed information about a specific work item.

### Parameters

- `WorkRetrieveParams parameters`

  - `required string environmentID`

    Path param

  - `required string workID`

    Path param

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

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"mid-conversation-system-2026-04-07"MidConversationSystem2026_04_07`

### Returns

- `class BetaSelfHostedWork:`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `required string ID`

    Work identifier (e.g., 'work_...')

  - `required string? AcknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `required string CreatedAt`

    RFC 3339 timestamp when work was created

  - `required BetaSessionWorkData Data`

    The actual work to be performed

    - `required string ID`

      Session identifier (e.g., 'session_...')

    - `JsonElement Type "session"constant`

      Type of work data

  - `required string EnvironmentID`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `required string? LatestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `required IReadOnlyDictionary<string, string> Metadata`

    User-provided metadata key-value pairs associated with this work item

  - `required string? StartedAt`

    RFC 3339 timestamp when work execution started

  - `required State State`

    Current state of the work item

    - `"queued"Queued`

    - `"starting"Starting`

    - `"active"Active`

    - `"stopping"Stopping`

    - `"stopped"Stopped`

  - `required string? StopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `required string? StoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `JsonElement Type "work"constant`

    The type of object (always 'work')

### Example

```csharp
WorkRetrieveParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW",
    WorkID = "work_id",
};

var betaSelfHostedWork = await client.Beta.Environments.Work.Retrieve(parameters);

Console.WriteLine(betaSelfHostedWork);
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

## Poll for Work

`BetaSelfHostedWork? Beta.Environments.Work.Poll(WorkPollParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/environments/{environment_id}/work/poll`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Long poll for work items in the queue.

### Parameters

- `WorkPollParams parameters`

  - `required string environmentID`

    Path param

  - `Long? blockMs`

    Query param: How long to wait for work to arrive before returning. Must be 1-999 in milliseconds. Defaults to non-blocking (returns immediately if no work is available).

  - `Long? reclaimOlderThanMs`

    Query param: Reclaim unacknowledged work items older than this many milliseconds. If omitted, uses the default (5000ms).

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

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"mid-conversation-system-2026-04-07"MidConversationSystem2026_04_07`

  - `string anthropicWorkerID`

    Header param: Unique identifier for the specific worker polling, used to track aggregated environment-level work metrics in Console

### Returns

- `class BetaSelfHostedWork:`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `required string ID`

    Work identifier (e.g., 'work_...')

  - `required string? AcknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `required string CreatedAt`

    RFC 3339 timestamp when work was created

  - `required BetaSessionWorkData Data`

    The actual work to be performed

    - `required string ID`

      Session identifier (e.g., 'session_...')

    - `JsonElement Type "session"constant`

      Type of work data

  - `required string EnvironmentID`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `required string? LatestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `required IReadOnlyDictionary<string, string> Metadata`

    User-provided metadata key-value pairs associated with this work item

  - `required string? StartedAt`

    RFC 3339 timestamp when work execution started

  - `required State State`

    Current state of the work item

    - `"queued"Queued`

    - `"starting"Starting`

    - `"active"Active`

    - `"stopping"Stopping`

    - `"stopped"Stopped`

  - `required string? StopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `required string? StoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `JsonElement Type "work"constant`

    The type of object (always 'work')

### Example

```csharp
WorkPollParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW"
};

var betaSelfHostedWork = await client.Beta.Environments.Work.Poll(parameters);

Console.WriteLine(betaSelfHostedWork);
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

## Acknowledge Work

`BetaSelfHostedWork Beta.Environments.Work.Ack(WorkAckParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/environments/{environment_id}/work/{work_id}/ack`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Acknowledge receipt of a work item, transitioning it from 'queued' to 'starting' and removing it from the queue.

### Parameters

- `WorkAckParams parameters`

  - `required string environmentID`

    Path param

  - `required string workID`

    Path param

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

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"mid-conversation-system-2026-04-07"MidConversationSystem2026_04_07`

### Returns

- `class BetaSelfHostedWork:`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `required string ID`

    Work identifier (e.g., 'work_...')

  - `required string? AcknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `required string CreatedAt`

    RFC 3339 timestamp when work was created

  - `required BetaSessionWorkData Data`

    The actual work to be performed

    - `required string ID`

      Session identifier (e.g., 'session_...')

    - `JsonElement Type "session"constant`

      Type of work data

  - `required string EnvironmentID`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `required string? LatestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `required IReadOnlyDictionary<string, string> Metadata`

    User-provided metadata key-value pairs associated with this work item

  - `required string? StartedAt`

    RFC 3339 timestamp when work execution started

  - `required State State`

    Current state of the work item

    - `"queued"Queued`

    - `"starting"Starting`

    - `"active"Active`

    - `"stopping"Stopping`

    - `"stopped"Stopped`

  - `required string? StopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `required string? StoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `JsonElement Type "work"constant`

    The type of object (always 'work')

### Example

```csharp
WorkAckParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW",
    WorkID = "work_id",
};

var betaSelfHostedWork = await client.Beta.Environments.Work.Ack(parameters);

Console.WriteLine(betaSelfHostedWork);
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

## Record Heartbeat

`BetaSelfHostedWorkHeartbeatResponse Beta.Environments.Work.Heartbeat(WorkHeartbeatParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/environments/{environment_id}/work/{work_id}/heartbeat`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Record a heartbeat for a work item to maintain the lease.

### Parameters

- `WorkHeartbeatParams parameters`

  - `required string environmentID`

    Path param

  - `required string workID`

    Path param

  - `Long? desiredTtlSeconds`

    Query param: Desired TTL in seconds

  - `string? expectedLastHeartbeat`

    Query param: Expected last_heartbeat for conditional update (optimistic concurrency). Use literal 'NO_HEARTBEAT' to claim an unclaimed lease (first heartbeat). For subsequent heartbeats, echo the server's previous last_heartbeat value exactly. Returns 412 Precondition Failed if the actual value doesn't match.

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

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"mid-conversation-system-2026-04-07"MidConversationSystem2026_04_07`

### Returns

- `class BetaSelfHostedWorkHeartbeatResponse:`

  Response after recording a heartbeat for a work item.

  - `required string LastHeartbeat`

    RFC 3339 timestamp of the actual heartbeat from DB

  - `required Boolean LeaseExtended`

    Whether the heartbeat succeeded in extending the lease

  - `required State State`

    Current state of the work item (active/stopping/stopped)

    - `"queued"Queued`

    - `"starting"Starting`

    - `"active"Active`

    - `"stopping"Stopping`

    - `"stopped"Stopped`

  - `required Long TtlSeconds`

    Effective TTL applied to the lease

  - `JsonElement Type "work_heartbeat"constant`

    The type of response

### Example

```csharp
WorkHeartbeatParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW",
    WorkID = "work_id",
};

var betaSelfHostedWorkHeartbeatResponse = await client.Beta.Environments.Work.Heartbeat(parameters);

Console.WriteLine(betaSelfHostedWorkHeartbeatResponse);
```

#### Response

```json
{
  "last_heartbeat": "last_heartbeat",
  "lease_extended": true,
  "state": "queued",
  "ttl_seconds": 0,
  "type": "work_heartbeat"
}
```

## Stop Work

`BetaSelfHostedWork Beta.Environments.Work.Stop(WorkStopParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/environments/{environment_id}/work/{work_id}/stop`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Stop a work item, initiating graceful or forced shutdown.

### Parameters

- `WorkStopParams parameters`

  - `required string environmentID`

    Path param

  - `required string workID`

    Path param

  - `Boolean force`

    Body param: If true, immediately stop work without graceful shutdown

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

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"mid-conversation-system-2026-04-07"MidConversationSystem2026_04_07`

### Returns

- `class BetaSelfHostedWork:`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `required string ID`

    Work identifier (e.g., 'work_...')

  - `required string? AcknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `required string CreatedAt`

    RFC 3339 timestamp when work was created

  - `required BetaSessionWorkData Data`

    The actual work to be performed

    - `required string ID`

      Session identifier (e.g., 'session_...')

    - `JsonElement Type "session"constant`

      Type of work data

  - `required string EnvironmentID`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `required string? LatestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `required IReadOnlyDictionary<string, string> Metadata`

    User-provided metadata key-value pairs associated with this work item

  - `required string? StartedAt`

    RFC 3339 timestamp when work execution started

  - `required State State`

    Current state of the work item

    - `"queued"Queued`

    - `"starting"Starting`

    - `"active"Active`

    - `"stopping"Stopping`

    - `"stopped"Stopped`

  - `required string? StopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `required string? StoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `JsonElement Type "work"constant`

    The type of object (always 'work')

### Example

```csharp
WorkStopParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW",
    WorkID = "work_id",
};

var betaSelfHostedWork = await client.Beta.Environments.Work.Stop(parameters);

Console.WriteLine(betaSelfHostedWork);
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

## List Work Items

`BetaSelfHostedWorkListResponse Beta.Environments.Work.List(WorkListParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/environments/{environment_id}/work`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

List work items in an environment.

### Parameters

- `WorkListParams parameters`

  - `required string environmentID`

    Path param

  - `Long limit`

    Query param: Maximum number of work items to return

  - `string? page`

    Query param: Opaque cursor from previous response for pagination

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

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"mid-conversation-system-2026-04-07"MidConversationSystem2026_04_07`

### Returns

- `class BetaSelfHostedWorkListResponse:`

  Response when listing work items with cursor-based pagination.

  - `required IReadOnlyList<BetaSelfHostedWork> Data`

    List of work items

    - `required string ID`

      Work identifier (e.g., 'work_...')

    - `required string? AcknowledgedAt`

      RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

    - `required string CreatedAt`

      RFC 3339 timestamp when work was created

    - `required BetaSessionWorkData Data`

      The actual work to be performed

      - `required string ID`

        Session identifier (e.g., 'session_...')

      - `JsonElement Type "session"constant`

        Type of work data

    - `required string EnvironmentID`

      Environment identifier this work belongs to (e.g., `env_...`)

    - `required string? LatestHeartbeatAt`

      RFC 3339 timestamp of the most recent heartbeat

    - `required IReadOnlyDictionary<string, string> Metadata`

      User-provided metadata key-value pairs associated with this work item

    - `required string? StartedAt`

      RFC 3339 timestamp when work execution started

    - `required State State`

      Current state of the work item

      - `"queued"Queued`

      - `"starting"Starting`

      - `"active"Active`

      - `"stopping"Stopping`

      - `"stopped"Stopped`

    - `required string? StopRequestedAt`

      RFC 3339 timestamp when stop was requested

    - `required string? StoppedAt`

      RFC 3339 timestamp when work execution stopped

    - `JsonElement Type "work"constant`

      The type of object (always 'work')

  - `required string? NextPage`

    Opaque cursor for fetching the next page of results

### Example

```csharp
WorkListParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW"
};

var page = await client.Beta.Environments.Work.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

#### Response

```json
{
  "data": [
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
  ],
  "next_page": "next_page"
}
```

## Update Work Item

`BetaSelfHostedWork Beta.Environments.Work.Update(WorkUpdateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/environments/{environment_id}/work/{work_id}`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Update work item metadata with merge semantics.

### Parameters

- `WorkUpdateParams parameters`

  - `required string environmentID`

    Path param

  - `required string workID`

    Path param

  - `required IReadOnlyDictionary<string, string> metadata`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

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

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"mid-conversation-system-2026-04-07"MidConversationSystem2026_04_07`

### Returns

- `class BetaSelfHostedWork:`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `required string ID`

    Work identifier (e.g., 'work_...')

  - `required string? AcknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `required string CreatedAt`

    RFC 3339 timestamp when work was created

  - `required BetaSessionWorkData Data`

    The actual work to be performed

    - `required string ID`

      Session identifier (e.g., 'session_...')

    - `JsonElement Type "session"constant`

      Type of work data

  - `required string EnvironmentID`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `required string? LatestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `required IReadOnlyDictionary<string, string> Metadata`

    User-provided metadata key-value pairs associated with this work item

  - `required string? StartedAt`

    RFC 3339 timestamp when work execution started

  - `required State State`

    Current state of the work item

    - `"queued"Queued`

    - `"starting"Starting`

    - `"active"Active`

    - `"stopping"Stopping`

    - `"stopped"Stopped`

  - `required string? StopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `required string? StoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `JsonElement Type "work"constant`

    The type of object (always 'work')

### Example

```csharp
WorkUpdateParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW",
    WorkID = "work_id",
    Metadata = new Dictionary<string, string?>() { { "foo", "string" } },
};

var betaSelfHostedWork = await client.Beta.Environments.Work.Update(parameters);

Console.WriteLine(betaSelfHostedWork);
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

## Get Queue Statistics

`BetaSelfHostedWorkQueueStats Beta.Environments.Work.Stats(WorkStatsParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/environments/{environment_id}/work/stats`

Get statistics about the work queue for an environment.

### Parameters

- `WorkStatsParams parameters`

  - `required string environmentID`

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

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

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"mid-conversation-system-2026-04-07"MidConversationSystem2026_04_07`

### Returns

- `class BetaSelfHostedWorkQueueStats:`

  Statistics about the work queue for an environment.

  Uses Redis Stream consumer group metrics for O(1) queries.

  - `required Long Depth`

    Number of work items waiting to be picked up (lag from consumer group)

  - `required string? OldestQueuedAt`

    RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

  - `required Long Pending`

    Number of work items being processed (polled but not acknowledged)

  - `JsonElement Type "work_queue_stats"constant`

    The type of object

  - `required Long? WorkersPolling`

    Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.

### Example

```csharp
WorkStatsParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW"
};

var betaSelfHostedWorkQueueStats = await client.Beta.Environments.Work.Stats(parameters);

Console.WriteLine(betaSelfHostedWorkQueueStats);
```

#### Response

```json
{
  "depth": 0,
  "oldest_queued_at": "oldest_queued_at",
  "pending": 0,
  "type": "work_queue_stats",
  "workers_polling": 0
}
```

## Domain Types

### Beta Self Hosted Work

- `class BetaSelfHostedWork:`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `required string ID`

    Work identifier (e.g., 'work_...')

  - `required string? AcknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `required string CreatedAt`

    RFC 3339 timestamp when work was created

  - `required BetaSessionWorkData Data`

    The actual work to be performed

    - `required string ID`

      Session identifier (e.g., 'session_...')

    - `JsonElement Type "session"constant`

      Type of work data

  - `required string EnvironmentID`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `required string? LatestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `required IReadOnlyDictionary<string, string> Metadata`

    User-provided metadata key-value pairs associated with this work item

  - `required string? StartedAt`

    RFC 3339 timestamp when work execution started

  - `required State State`

    Current state of the work item

    - `"queued"Queued`

    - `"starting"Starting`

    - `"active"Active`

    - `"stopping"Stopping`

    - `"stopped"Stopped`

  - `required string? StopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `required string? StoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `JsonElement Type "work"constant`

    The type of object (always 'work')

### Beta Self Hosted Work Heartbeat Response

- `class BetaSelfHostedWorkHeartbeatResponse:`

  Response after recording a heartbeat for a work item.

  - `required string LastHeartbeat`

    RFC 3339 timestamp of the actual heartbeat from DB

  - `required Boolean LeaseExtended`

    Whether the heartbeat succeeded in extending the lease

  - `required State State`

    Current state of the work item (active/stopping/stopped)

    - `"queued"Queued`

    - `"starting"Starting`

    - `"active"Active`

    - `"stopping"Stopping`

    - `"stopped"Stopped`

  - `required Long TtlSeconds`

    Effective TTL applied to the lease

  - `JsonElement Type "work_heartbeat"constant`

    The type of response

### Beta Self Hosted Work List Response

- `class BetaSelfHostedWorkListResponse:`

  Response when listing work items with cursor-based pagination.

  - `required IReadOnlyList<BetaSelfHostedWork> Data`

    List of work items

    - `required string ID`

      Work identifier (e.g., 'work_...')

    - `required string? AcknowledgedAt`

      RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

    - `required string CreatedAt`

      RFC 3339 timestamp when work was created

    - `required BetaSessionWorkData Data`

      The actual work to be performed

      - `required string ID`

        Session identifier (e.g., 'session_...')

      - `JsonElement Type "session"constant`

        Type of work data

    - `required string EnvironmentID`

      Environment identifier this work belongs to (e.g., `env_...`)

    - `required string? LatestHeartbeatAt`

      RFC 3339 timestamp of the most recent heartbeat

    - `required IReadOnlyDictionary<string, string> Metadata`

      User-provided metadata key-value pairs associated with this work item

    - `required string? StartedAt`

      RFC 3339 timestamp when work execution started

    - `required State State`

      Current state of the work item

      - `"queued"Queued`

      - `"starting"Starting`

      - `"active"Active`

      - `"stopping"Stopping`

      - `"stopped"Stopped`

    - `required string? StopRequestedAt`

      RFC 3339 timestamp when stop was requested

    - `required string? StoppedAt`

      RFC 3339 timestamp when work execution stopped

    - `JsonElement Type "work"constant`

      The type of object (always 'work')

  - `required string? NextPage`

    Opaque cursor for fetching the next page of results

### Beta Self Hosted Work Queue Stats

- `class BetaSelfHostedWorkQueueStats:`

  Statistics about the work queue for an environment.

  Uses Redis Stream consumer group metrics for O(1) queries.

  - `required Long Depth`

    Number of work items waiting to be picked up (lag from consumer group)

  - `required string? OldestQueuedAt`

    RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

  - `required Long Pending`

    Number of work items being processed (polled but not acknowledged)

  - `JsonElement Type "work_queue_stats"constant`

    The type of object

  - `required Long? WorkersPolling`

    Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.

### Beta Self Hosted Work Stop Request

- `class BetaSelfHostedWorkStopRequest:`

  Request to stop a work item.

  - `Boolean Force`

    If true, immediately stop work without graceful shutdown

### Beta Self Hosted Work Update Request

- `class BetaSelfHostedWorkUpdateRequest:`

  Request to update work item metadata.

  - `required IReadOnlyDictionary<string, string> Metadata`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

### Beta Session Work Data

- `class BetaSessionWorkData:`

  Work data for session work items.

  This resource type is used when work represents a session that needs to be executed
  in a self-hosted environment.

  - `required string ID`

    Session identifier (e.g., 'session_...')

  - `JsonElement Type "session"constant`

    Type of work data
