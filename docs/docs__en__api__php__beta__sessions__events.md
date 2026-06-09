# Events

## List Events

`$client->beta->sessions->events->list(string sessionID, ?\Datetime createdAtGt, ?\Datetime createdAtGte, ?\Datetime createdAtLt, ?\Datetime createdAtLte, ?int limit, ?Order order, ?string page, ?list<string> types, ?list<AnthropicBeta> betas): PageCursor<ManagedAgentsSessionEvent>`

**get** `/v1/sessions/{session_id}/events`

List Events

### Parameters

- `sessionID: string`

- `createdAtGt?:optional \Datetime`

  Return events created after this time (exclusive).

- `createdAtGte?:optional \Datetime`

  Return events created at or after this time (inclusive).

- `createdAtLt?:optional \Datetime`

  Return events created before this time (exclusive).

- `createdAtLte?:optional \Datetime`

  Return events created at or before this time (inclusive).

- `limit?:optional int`

  Query parameter for limit

- `order?:optional Order`

  Sort direction for results, ordered by created_at. Defaults to asc (chronological).

- `page?:optional string`

  Opaque pagination cursor from a previous response's next_page.

- `types?:optional list<string>`

  Filter by event type. Values match the `type` field on returned events (for example, `user.message` or `agent.tool_use`). Omit to return all event types.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsSessionEvent`

  - `ManagedAgentsUserMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of content blocks comprising the user message.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `ManagedAgentsUserInterruptEvent`

    - `string id`

      Unique identifier for this event.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `ManagedAgentsUserToolConfirmationEvent`

    - `string id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

    - `string toolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?string denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `ManagedAgentsUserCustomToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string customToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `ManagedAgentsAgentCustomToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the custom tool being called.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `ManagedAgentsAgentMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<ManagedAgentsTextBlock> content`

      Array of text blocks comprising the agent response.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsAgentThinkingEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsAgentMCPToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string mcpServerName`

      Name of the MCP server providing the tool.

    - `string name`

      Name of the MCP tool being used.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `ManagedAgentsAgentMCPToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string mcpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `ManagedAgentsAgentToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the agent tool being used.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `ManagedAgentsAgentToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `ManagedAgentsAgentThreadMessageReceivedEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `string fromSessionThreadID`

      Public `sthr_` ID of the thread that sent the message.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?string fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `ManagedAgentsAgentThreadMessageSentEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string toSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type type`

    - `?string toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `ManagedAgentsAgentThreadContextCompactedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionErrorEvent`

    - `string id`

      Unique identifier for this event.

    - `Error error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusRescheduledEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusRunningEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusIdleEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

    - `Type type`

  - `ManagedAgentsSessionStatusTerminatedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionThreadCreatedEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the callable agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public `sthr_` ID of the newly created thread.

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationStartEvent`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationEndEvent`

    - `string id`

      Unique identifier for this event.

    - `string explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type type`

    - `ManagedAgentsSpanModelUsage usage`

      Token usage for a single model request.

  - `ManagedAgentsSpanModelRequestStartEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanModelRequestEndEvent`

    - `string id`

      Unique identifier for this event.

    - `?bool isError`

      Whether the model request resulted in an error.

    - `string modelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `ManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsUserDefineOutcomeEvent`

    - `string id`

      Unique identifier for this event.

    - `string description`

      What the agent should produce. Copied from the input event.

    - `?int maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `string outcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

    - `Type type`

  - `ManagedAgentsSessionDeletedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionThreadStatusRunningEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that started running.

    - `Type type`

  - `ManagedAgentsSessionThreadStatusIdleEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

    - `Type type`

  - `ManagedAgentsSessionThreadStatusTerminatedEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that terminated.

    - `Type type`

  - `BetaManagedAgentsUserToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `ManagedAgentsSessionThreadStatusRescheduledEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that is retrying.

    - `Type type`

  - `BetaManagedAgentsSessionUpdatedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?BetaManagedAgentsSessionAgent agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `?array<string,string> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `?string title`

      The session's new title. Present only when the update changed it.

  - `BetaManagedAgentsSystemMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->sessions->events->list(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  createdAtGt: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtGte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLt: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  limit: 0,
  order: 'asc',
  page: 'page',
  types: ['string'],
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
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
    },
    {
      "id": "sevt_011CZkZHPq1jCdq5lbRTjiVnz",
      "content": [
        {
          "text": "Let me look up order #1234 for you.",
          "type": "text"
        }
      ],
      "processed_at": "2026-03-15T10:00:00Z",
      "type": "agent.message"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Send Events

`$client->beta->sessions->events->send(string sessionID, list<ManagedAgentsEventParams> events, ?list<AnthropicBeta> betas): ManagedAgentsSendSessionEvents`

**post** `/v1/sessions/{session_id}/events`

Send Events

### Parameters

- `sessionID: string`

- `events: list<ManagedAgentsEventParams>`

  Events to send to the `session`.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsSendSessionEvents`

  - `?list<Data> data`

    Sent events

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsSendSessionEvents = $client->beta->sessions->events->send(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  events: [
    [
      'content' => [['text' => 'Where is my order #1234?', 'type' => 'text']],
      'type' => 'user.message',
    ],
  ],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsSendSessionEvents);
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
  ]
}
```

## Stream Events

`$client->beta->sessions->events->stream(string sessionID, ?list<AnthropicBeta> betas): ManagedAgentsStreamSessionEvents`

**get** `/v1/sessions/{session_id}/events/stream`

Stream Events

### Parameters

- `sessionID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsStreamSessionEvents`

  - `ManagedAgentsUserMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of content blocks comprising the user message.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `ManagedAgentsUserInterruptEvent`

    - `string id`

      Unique identifier for this event.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `ManagedAgentsUserToolConfirmationEvent`

    - `string id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

    - `string toolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?string denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `ManagedAgentsUserCustomToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string customToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `ManagedAgentsAgentCustomToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the custom tool being called.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `ManagedAgentsAgentMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<ManagedAgentsTextBlock> content`

      Array of text blocks comprising the agent response.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsAgentThinkingEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsAgentMCPToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string mcpServerName`

      Name of the MCP server providing the tool.

    - `string name`

      Name of the MCP tool being used.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `ManagedAgentsAgentMCPToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string mcpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `ManagedAgentsAgentToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the agent tool being used.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `ManagedAgentsAgentToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `ManagedAgentsAgentThreadMessageReceivedEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `string fromSessionThreadID`

      Public `sthr_` ID of the thread that sent the message.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?string fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `ManagedAgentsAgentThreadMessageSentEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string toSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type type`

    - `?string toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `ManagedAgentsAgentThreadContextCompactedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionErrorEvent`

    - `string id`

      Unique identifier for this event.

    - `Error error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusRescheduledEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusRunningEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusIdleEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

    - `Type type`

  - `ManagedAgentsSessionStatusTerminatedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionThreadCreatedEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the callable agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public `sthr_` ID of the newly created thread.

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationStartEvent`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationEndEvent`

    - `string id`

      Unique identifier for this event.

    - `string explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type type`

    - `ManagedAgentsSpanModelUsage usage`

      Token usage for a single model request.

  - `ManagedAgentsSpanModelRequestStartEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanModelRequestEndEvent`

    - `string id`

      Unique identifier for this event.

    - `?bool isError`

      Whether the model request resulted in an error.

    - `string modelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `ManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsUserDefineOutcomeEvent`

    - `string id`

      Unique identifier for this event.

    - `string description`

      What the agent should produce. Copied from the input event.

    - `?int maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `string outcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

    - `Type type`

  - `ManagedAgentsSessionDeletedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionThreadStatusRunningEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that started running.

    - `Type type`

  - `ManagedAgentsSessionThreadStatusIdleEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

    - `Type type`

  - `ManagedAgentsSessionThreadStatusTerminatedEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that terminated.

    - `Type type`

  - `BetaManagedAgentsUserToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `ManagedAgentsSessionThreadStatusRescheduledEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that is retrying.

    - `Type type`

  - `BetaManagedAgentsSessionUpdatedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?BetaManagedAgentsSessionAgent agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `?array<string,string> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `?string title`

      The session's new title. Present only when the update changed it.

  - `BetaManagedAgentsSystemMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsStreamSessionEvents = $client
  ->beta
  ->sessions
  ->events
  ->streamStream(
  'sesn_011CZkZAtmR3yMPDzynEDxu7', betas: ['message-batches-2024-09-24']
);

var_dump($betaManagedAgentsStreamSessionEvents);
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

## Domain Types

### Beta Managed Agents Agent Custom Tool Use Event

- `ManagedAgentsAgentCustomToolUseEvent`

  - `string id`

    Unique identifier for this event.

  - `array<string,mixed> input`

    Input parameters for the tool call.

  - `string name`

    Name of the custom tool being called.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

  - `?string sessionThreadID`

    When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

### Beta Managed Agents Agent MCP Tool Result Event

- `ManagedAgentsAgentMCPToolResultEvent`

  - `string id`

    Unique identifier for this event.

  - `string mcpToolUseID`

    The id of the `agent.mcp_tool_use` event this result corresponds to.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

  - `?list<Content> content`

    The result content returned by the tool.

  - `?bool isError`

    Whether the tool execution resulted in an error.

### Beta Managed Agents Agent MCP Tool Use Event

- `ManagedAgentsAgentMCPToolUseEvent`

  - `string id`

    Unique identifier for this event.

  - `array<string,mixed> input`

    Input parameters for the tool call.

  - `string mcpServerName`

    Name of the MCP server providing the tool.

  - `string name`

    Name of the MCP tool being used.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

  - `?EvaluatedPermission evaluatedPermission`

    AgentEvaluatedPermission enum

  - `?string sessionThreadID`

    When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

### Beta Managed Agents Agent Message Event

- `ManagedAgentsAgentMessageEvent`

  - `string id`

    Unique identifier for this event.

  - `list<ManagedAgentsTextBlock> content`

    Array of text blocks comprising the agent response.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

### Beta Managed Agents Agent Thinking Event

- `ManagedAgentsAgentThinkingEvent`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

### Beta Managed Agents Agent Thread Context Compacted Event

- `ManagedAgentsAgentThreadContextCompactedEvent`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

### Beta Managed Agents Agent Thread Message Received Event

- `ManagedAgentsAgentThreadMessageReceivedEvent`

  - `string id`

    Unique identifier for this event.

  - `list<Content> content`

    Message content blocks.

  - `string fromSessionThreadID`

    Public `sthr_` ID of the thread that sent the message.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

  - `?string fromAgentName`

    Name of the callable agent this message came from. Absent when received from the primary agent.

### Beta Managed Agents Agent Thread Message Sent Event

- `ManagedAgentsAgentThreadMessageSentEvent`

  - `string id`

    Unique identifier for this event.

  - `list<Content> content`

    Message content blocks.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `string toSessionThreadID`

    Public `sthr_` ID of the thread the message was sent to.

  - `Type type`

  - `?string toAgentName`

    Name of the callable agent this message was sent to. Absent when sent to the primary agent.

### Beta Managed Agents Agent Tool Result Event

- `ManagedAgentsAgentToolResultEvent`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `string toolUseID`

    The id of the `agent.tool_use` event this result corresponds to.

  - `Type type`

  - `?list<Content> content`

    The result content returned by the tool.

  - `?bool isError`

    Whether the tool execution resulted in an error.

### Beta Managed Agents Agent Tool Use Event

- `ManagedAgentsAgentToolUseEvent`

  - `string id`

    Unique identifier for this event.

  - `array<string,mixed> input`

    Input parameters for the tool call.

  - `string name`

    Name of the agent tool being used.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

  - `?EvaluatedPermission evaluatedPermission`

    AgentEvaluatedPermission enum

  - `?string sessionThreadID`

    When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

### Beta Managed Agents Base64 Document Source

- `ManagedAgentsBase64DocumentSource`

  - `string data`

    Base64-encoded document data.

  - `string mediaType`

    MIME type of the document (e.g., "application/pdf").

  - `Type type`

### Beta Managed Agents Base64 Image Source

- `ManagedAgentsBase64ImageSource`

  - `string data`

    Base64-encoded image data.

  - `string mediaType`

    MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

  - `Type type`

### Beta Managed Agents Billing Error

- `ManagedAgentsBillingError`

  - `string message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

  - `Type type`

### Beta Managed Agents Credential Host Unreachable Error

- `ManagedAgentsCredentialHostUnreachableError`

  - `string credentialID`

    ID of the affected credential.

  - `string message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

  - `Type type`

  - `string vaultID`

    ID of the vault containing the affected credential.

### Beta Managed Agents Document Block

- `ManagedAgentsDocumentBlock`

  - `Source source`

    Union type for document source variants.

  - `Type type`

  - `?string context`

    Additional context about the document for the model.

  - `?string title`

    The title of the document.

### Beta Managed Agents Event Params

- `ManagedAgentsEventParams`

  - `ManagedAgentsUserMessageEventParams`

    - `list<Content> content`

      Array of content blocks for the user message.

    - `Type type`

  - `ManagedAgentsUserInterruptEventParams`

    - `Type type`

    - `?string sessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `ManagedAgentsUserToolConfirmationEventParams`

    - `Result result`

      UserToolConfirmationResult enum

    - `string toolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?string denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

  - `ManagedAgentsUserCustomToolResultEventParams`

    - `string customToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `ManagedAgentsUserDefineOutcomeEventParams`

    - `string description`

      What the agent should produce. This is the task specification.

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

    - `Type type`

    - `?int maxIterations`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `ManagedAgentsUserToolResultEventParams`

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `ManagedAgentsSystemMessageEventParams`

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks to append. Text-only.

    - `Type type`

### Beta Managed Agents File Document Source

- `ManagedAgentsFileDocumentSource`

  - `string fileID`

    ID of a previously uploaded file.

  - `Type type`

### Beta Managed Agents File Image Source

- `ManagedAgentsFileImageSource`

  - `string fileID`

    ID of a previously uploaded file.

  - `Type type`

### Beta Managed Agents File Rubric

- `ManagedAgentsFileRubric`

  - `string fileID`

    ID of the rubric file.

  - `Type type`

### Beta Managed Agents File Rubric Params

- `ManagedAgentsFileRubricParams`

  - `string fileID`

    ID of the rubric file.

  - `Type type`

### Beta Managed Agents Image Block

- `ManagedAgentsImageBlock`

  - `Source source`

    Union type for image source variants.

  - `Type type`

### Beta Managed Agents MCP Authentication Failed Error

- `ManagedAgentsMCPAuthenticationFailedError`

  - `string mcpServerName`

    Name of the MCP server that failed authentication.

  - `string message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

  - `Type type`

### Beta Managed Agents MCP Connection Failed Error

- `ManagedAgentsMCPConnectionFailedError`

  - `string mcpServerName`

    Name of the MCP server that failed to connect.

  - `string message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

  - `Type type`

### Beta Managed Agents Model Overloaded Error

- `ManagedAgentsModelOverloadedError`

  - `string message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

  - `Type type`

### Beta Managed Agents Model Rate Limited Error

- `ManagedAgentsModelRateLimitedError`

  - `string message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

  - `Type type`

### Beta Managed Agents Model Request Failed Error

- `ManagedAgentsModelRequestFailedError`

  - `string message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

  - `Type type`

### Beta Managed Agents Plain Text Document Source

- `ManagedAgentsPlainTextDocumentSource`

  - `string data`

    The plain text content.

  - `MediaType mediaType`

    MIME type of the text content. Must be "text/plain".

  - `Type type`

### Beta Managed Agents Retry Status Exhausted

- `ManagedAgentsRetryStatusExhausted`

  - `Type type`

### Beta Managed Agents Retry Status Retrying

- `ManagedAgentsRetryStatusRetrying`

  - `Type type`

### Beta Managed Agents Retry Status Terminal

- `ManagedAgentsRetryStatusTerminal`

  - `Type type`

### Beta Managed Agents Search Result Block

- `ManagedAgentsSearchResultBlock`

  - `ManagedAgentsSearchResultCitations citations`

    Citation settings for a search result.

  - `list<ManagedAgentsSearchResultContent> content`

    Array of text content blocks from the search result.

  - `string source`

    The URL source of the search result.

  - `string title`

    The title of the search result.

  - `Type type`

### Beta Managed Agents Search Result Citations

- `ManagedAgentsSearchResultCitations`

  - `bool enabled`

    Whether citations are enabled for this search result.

### Beta Managed Agents Search Result Content

- `ManagedAgentsSearchResultContent`

  - `string text`

    The text content.

  - `Type type`

### Beta Managed Agents Send Session Events

- `ManagedAgentsSendSessionEvents`

  - `?list<Data> data`

    Sent events

### Beta Managed Agents Session Deleted Event

- `ManagedAgentsSessionDeletedEvent`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

### Beta Managed Agents Session End Turn

- `ManagedAgentsSessionEndTurn`

  - `Type type`

### Beta Managed Agents Session Error Event

- `ManagedAgentsSessionErrorEvent`

  - `string id`

    Unique identifier for this event.

  - `Error error`

    An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

### Beta Managed Agents Session Event

- `ManagedAgentsSessionEvent`

  - `ManagedAgentsUserMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of content blocks comprising the user message.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `ManagedAgentsUserInterruptEvent`

    - `string id`

      Unique identifier for this event.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `ManagedAgentsUserToolConfirmationEvent`

    - `string id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

    - `string toolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?string denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `ManagedAgentsUserCustomToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string customToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `ManagedAgentsAgentCustomToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the custom tool being called.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `ManagedAgentsAgentMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<ManagedAgentsTextBlock> content`

      Array of text blocks comprising the agent response.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsAgentThinkingEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsAgentMCPToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string mcpServerName`

      Name of the MCP server providing the tool.

    - `string name`

      Name of the MCP tool being used.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `ManagedAgentsAgentMCPToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string mcpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `ManagedAgentsAgentToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the agent tool being used.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `ManagedAgentsAgentToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `ManagedAgentsAgentThreadMessageReceivedEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `string fromSessionThreadID`

      Public `sthr_` ID of the thread that sent the message.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?string fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `ManagedAgentsAgentThreadMessageSentEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string toSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type type`

    - `?string toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `ManagedAgentsAgentThreadContextCompactedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionErrorEvent`

    - `string id`

      Unique identifier for this event.

    - `Error error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusRescheduledEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusRunningEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusIdleEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

    - `Type type`

  - `ManagedAgentsSessionStatusTerminatedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionThreadCreatedEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the callable agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public `sthr_` ID of the newly created thread.

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationStartEvent`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationEndEvent`

    - `string id`

      Unique identifier for this event.

    - `string explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type type`

    - `ManagedAgentsSpanModelUsage usage`

      Token usage for a single model request.

  - `ManagedAgentsSpanModelRequestStartEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanModelRequestEndEvent`

    - `string id`

      Unique identifier for this event.

    - `?bool isError`

      Whether the model request resulted in an error.

    - `string modelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `ManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsUserDefineOutcomeEvent`

    - `string id`

      Unique identifier for this event.

    - `string description`

      What the agent should produce. Copied from the input event.

    - `?int maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `string outcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

    - `Type type`

  - `ManagedAgentsSessionDeletedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionThreadStatusRunningEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that started running.

    - `Type type`

  - `ManagedAgentsSessionThreadStatusIdleEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

    - `Type type`

  - `ManagedAgentsSessionThreadStatusTerminatedEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that terminated.

    - `Type type`

  - `BetaManagedAgentsUserToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `ManagedAgentsSessionThreadStatusRescheduledEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that is retrying.

    - `Type type`

  - `BetaManagedAgentsSessionUpdatedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?BetaManagedAgentsSessionAgent agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `?array<string,string> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `?string title`

      The session's new title. Present only when the update changed it.

  - `BetaManagedAgentsSystemMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

### Beta Managed Agents Session Requires Action

- `ManagedAgentsSessionRequiresAction`

  - `list<string> eventIDs`

    The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

  - `Type type`

### Beta Managed Agents Session Retries Exhausted

- `ManagedAgentsSessionRetriesExhausted`

  - `Type type`

### Beta Managed Agents Session Status Idle Event

- `ManagedAgentsSessionStatusIdleEvent`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `StopReason stopReason`

    The agent completed its turn naturally and is ready for the next user message.

  - `Type type`

### Beta Managed Agents Session Status Rescheduled Event

- `ManagedAgentsSessionStatusRescheduledEvent`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

### Beta Managed Agents Session Status Running Event

- `ManagedAgentsSessionStatusRunningEvent`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

### Beta Managed Agents Session Status Terminated Event

- `ManagedAgentsSessionStatusTerminatedEvent`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

### Beta Managed Agents Session Thread Created Event

- `ManagedAgentsSessionThreadCreatedEvent`

  - `string id`

    Unique identifier for this event.

  - `string agentName`

    Name of the callable agent the thread runs.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `string sessionThreadID`

    Public `sthr_` ID of the newly created thread.

  - `Type type`

### Beta Managed Agents Session Thread Status Idle Event

- `ManagedAgentsSessionThreadStatusIdleEvent`

  - `string id`

    Unique identifier for this event.

  - `string agentName`

    Name of the agent the thread runs.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `string sessionThreadID`

    Public sthr_ ID of the thread that went idle.

  - `StopReason stopReason`

    The agent completed its turn naturally and is ready for the next user message.

  - `Type type`

### Beta Managed Agents Session Thread Status Rescheduled Event

- `ManagedAgentsSessionThreadStatusRescheduledEvent`

  - `string id`

    Unique identifier for this event.

  - `string agentName`

    Name of the agent the thread runs.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `string sessionThreadID`

    Public sthr_ ID of the thread that is retrying.

  - `Type type`

### Beta Managed Agents Session Thread Status Running Event

- `ManagedAgentsSessionThreadStatusRunningEvent`

  - `string id`

    Unique identifier for this event.

  - `string agentName`

    Name of the agent the thread runs.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `string sessionThreadID`

    Public sthr_ ID of the thread that started running.

  - `Type type`

### Beta Managed Agents Session Thread Status Terminated Event

- `ManagedAgentsSessionThreadStatusTerminatedEvent`

  - `string id`

    Unique identifier for this event.

  - `string agentName`

    Name of the agent the thread runs.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `string sessionThreadID`

    Public sthr_ ID of the thread that terminated.

  - `Type type`

### Beta Managed Agents Span Model Request End Event

- `ManagedAgentsSpanModelRequestEndEvent`

  - `string id`

    Unique identifier for this event.

  - `?bool isError`

    Whether the model request resulted in an error.

  - `string modelRequestStartID`

    The id of the corresponding `span.model_request_start` event.

  - `ManagedAgentsSpanModelUsage modelUsage`

    Token usage for a single model request.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

### Beta Managed Agents Span Model Request Start Event

- `ManagedAgentsSpanModelRequestStartEvent`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

### Beta Managed Agents Span Model Usage

- `ManagedAgentsSpanModelUsage`

  - `int cacheCreationInputTokens`

    Tokens used to create prompt cache in this request.

  - `int cacheReadInputTokens`

    Tokens read from prompt cache in this request.

  - `int inputTokens`

    Input tokens consumed by this request.

  - `int outputTokens`

    Output tokens generated by this request.

  - `?Speed speed`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

### Beta Managed Agents Span Outcome Evaluation End Event

- `ManagedAgentsSpanOutcomeEvaluationEndEvent`

  - `string id`

    Unique identifier for this event.

  - `string explanation`

    Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

  - `int iteration`

    0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

  - `string outcomeEvaluationStartID`

    The id of the corresponding `span.outcome_evaluation_start` event.

  - `string outcomeID`

    The `outc_` ID of the outcome being evaluated.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `string result`

    Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

  - `Type type`

  - `ManagedAgentsSpanModelUsage usage`

    Token usage for a single model request.

### Beta Managed Agents Span Outcome Evaluation Ongoing Event

- `ManagedAgentsSpanOutcomeEvaluationOngoingEvent`

  - `string id`

    Unique identifier for this event.

  - `int iteration`

    0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

  - `string outcomeID`

    The `outc_` ID of the outcome being evaluated.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

### Beta Managed Agents Span Outcome Evaluation Start Event

- `ManagedAgentsSpanOutcomeEvaluationStartEvent`

  - `string id`

    Unique identifier for this event.

  - `int iteration`

    0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

  - `string outcomeID`

    The `outc_` ID of the outcome being evaluated.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

### Beta Managed Agents Stream Session Events

- `ManagedAgentsStreamSessionEvents`

  - `ManagedAgentsUserMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of content blocks comprising the user message.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `ManagedAgentsUserInterruptEvent`

    - `string id`

      Unique identifier for this event.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `ManagedAgentsUserToolConfirmationEvent`

    - `string id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

    - `string toolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?string denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `ManagedAgentsUserCustomToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string customToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `ManagedAgentsAgentCustomToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the custom tool being called.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `ManagedAgentsAgentMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<ManagedAgentsTextBlock> content`

      Array of text blocks comprising the agent response.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsAgentThinkingEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsAgentMCPToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string mcpServerName`

      Name of the MCP server providing the tool.

    - `string name`

      Name of the MCP tool being used.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `ManagedAgentsAgentMCPToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string mcpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `ManagedAgentsAgentToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the agent tool being used.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `ManagedAgentsAgentToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `ManagedAgentsAgentThreadMessageReceivedEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `string fromSessionThreadID`

      Public `sthr_` ID of the thread that sent the message.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?string fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `ManagedAgentsAgentThreadMessageSentEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string toSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type type`

    - `?string toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `ManagedAgentsAgentThreadContextCompactedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionErrorEvent`

    - `string id`

      Unique identifier for this event.

    - `Error error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusRescheduledEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusRunningEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusIdleEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

    - `Type type`

  - `ManagedAgentsSessionStatusTerminatedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionThreadCreatedEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the callable agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public `sthr_` ID of the newly created thread.

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationStartEvent`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationEndEvent`

    - `string id`

      Unique identifier for this event.

    - `string explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type type`

    - `ManagedAgentsSpanModelUsage usage`

      Token usage for a single model request.

  - `ManagedAgentsSpanModelRequestStartEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanModelRequestEndEvent`

    - `string id`

      Unique identifier for this event.

    - `?bool isError`

      Whether the model request resulted in an error.

    - `string modelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `ManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsUserDefineOutcomeEvent`

    - `string id`

      Unique identifier for this event.

    - `string description`

      What the agent should produce. Copied from the input event.

    - `?int maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `string outcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

    - `Type type`

  - `ManagedAgentsSessionDeletedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionThreadStatusRunningEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that started running.

    - `Type type`

  - `ManagedAgentsSessionThreadStatusIdleEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

    - `Type type`

  - `ManagedAgentsSessionThreadStatusTerminatedEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that terminated.

    - `Type type`

  - `BetaManagedAgentsUserToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `ManagedAgentsSessionThreadStatusRescheduledEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that is retrying.

    - `Type type`

  - `BetaManagedAgentsSessionUpdatedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?BetaManagedAgentsSessionAgent agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `?array<string,string> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `?string title`

      The session's new title. Present only when the update changed it.

  - `BetaManagedAgentsSystemMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

### Beta Managed Agents System Message Event Params

- `ManagedAgentsSystemMessageEventParams`

  - `list<BetaManagedAgentsSystemContentBlock> content`

    System content blocks to append. Text-only.

  - `Type type`

### Beta Managed Agents Text Block

- `ManagedAgentsTextBlock`

  - `string text`

    The text content.

  - `Type type`

### Beta Managed Agents Text Rubric

- `ManagedAgentsTextRubric`

  - `string content`

    Rubric content. Plain text or markdown — the grader treats it as freeform text.

  - `Type type`

### Beta Managed Agents Text Rubric Params

- `ManagedAgentsTextRubricParams`

  - `string content`

    Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

  - `Type type`

### Beta Managed Agents Unknown Error

- `ManagedAgentsUnknownError`

  - `string message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

  - `Type type`

### Beta Managed Agents URL Document Source

- `ManagedAgentsURLDocumentSource`

  - `Type type`

  - `string url`

    URL of the document to fetch.

### Beta Managed Agents URL Image Source

- `ManagedAgentsURLImageSource`

  - `Type type`

  - `string url`

    URL of the image to fetch.

### Beta Managed Agents User Custom Tool Result Event

- `ManagedAgentsUserCustomToolResultEvent`

  - `string id`

    Unique identifier for this event.

  - `string customToolUseID`

    The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `Type type`

  - `?list<Content> content`

    The result content returned by the tool.

  - `?bool isError`

    Whether the tool execution resulted in an error.

  - `?\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `?string sessionThreadID`

    Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

### Beta Managed Agents User Custom Tool Result Event Params

- `ManagedAgentsUserCustomToolResultEventParams`

  - `string customToolUseID`

    The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `Type type`

  - `?list<Content> content`

    The result content returned by the tool.

  - `?bool isError`

    Whether the tool execution resulted in an error.

### Beta Managed Agents User Define Outcome Event

- `ManagedAgentsUserDefineOutcomeEvent`

  - `string id`

    Unique identifier for this event.

  - `string description`

    What the agent should produce. Copied from the input event.

  - `?int maxIterations`

    Evaluate-then-revise cycles before giving up. Default 3, max 20.

  - `string outcomeID`

    Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Rubric rubric`

    Rubric for grading the quality of an outcome.

  - `Type type`

### Beta Managed Agents User Define Outcome Event Params

- `ManagedAgentsUserDefineOutcomeEventParams`

  - `string description`

    What the agent should produce. This is the task specification.

  - `Rubric rubric`

    Rubric for grading the quality of an outcome.

  - `Type type`

  - `?int maxIterations`

    Eval→revision cycles before giving up. Default 3, max 20.

### Beta Managed Agents User Interrupt Event

- `ManagedAgentsUserInterruptEvent`

  - `string id`

    Unique identifier for this event.

  - `Type type`

  - `?\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `?string sessionThreadID`

    If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

### Beta Managed Agents User Interrupt Event Params

- `ManagedAgentsUserInterruptEventParams`

  - `Type type`

  - `?string sessionThreadID`

    If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

### Beta Managed Agents User Message Event

- `ManagedAgentsUserMessageEvent`

  - `string id`

    Unique identifier for this event.

  - `list<Content> content`

    Array of content blocks comprising the user message.

  - `Type type`

  - `?\Datetime processedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Message Event Params

- `ManagedAgentsUserMessageEventParams`

  - `list<Content> content`

    Array of content blocks for the user message.

  - `Type type`

### Beta Managed Agents User Tool Confirmation Event

- `ManagedAgentsUserToolConfirmationEvent`

  - `string id`

    Unique identifier for this event.

  - `Result result`

    UserToolConfirmationResult enum

  - `string toolUseID`

    The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `Type type`

  - `?string denyMessage`

    Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

  - `?\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `?string sessionThreadID`

    When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

### Beta Managed Agents User Tool Confirmation Event Params

- `ManagedAgentsUserToolConfirmationEventParams`

  - `Result result`

    UserToolConfirmationResult enum

  - `string toolUseID`

    The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `Type type`

  - `?string denyMessage`

    Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

### Beta Managed Agents User Tool Result Event Params

- `ManagedAgentsUserToolResultEventParams`

  - `string toolUseID`

    The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `Type type`

  - `?list<Content> content`

    The result content returned by the tool.

  - `?bool isError`

    Whether the tool execution resulted in an error.
