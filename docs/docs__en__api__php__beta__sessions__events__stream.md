## Stream Events

`$client->beta->sessions->events->stream(string sessionID, ?list<BetaManagedAgentsDeltaType> eventDeltas, ?list<AnthropicBeta> betas): ManagedAgentsStreamSessionEvents`

**get** `/v1/sessions/{session_id}/events/stream`

Stream Events

### Parameters

- `sessionID: string`

- `eventDeltas?:optional list<BetaManagedAgentsDeltaType>`

  When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

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

  - `BetaManagedAgentsStartEvent`

    - `BetaManagedAgentsStartEventPreview event`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

    - `Type type`

  - `BetaManagedAgentsDeltaEvent`

    - `BetaManagedAgentsDeltaContent delta`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

    - `string eventID`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `Type type`

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
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  eventDeltas: [BetaManagedAgentsDeltaType::AGENT_MESSAGE],
  betas: ['message-batches-2024-09-24'],
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
