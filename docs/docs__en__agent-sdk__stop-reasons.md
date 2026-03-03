# Handle stop reasons

Understand why Claude stopped generating and handle refusals, token limits, and other termination conditions

---

When Claude finishes generating a response, the underlying API reports a `stop_reason` indicating why: the response completed normally, hit a token limit, was declined as a refusal, or ended for another reason. This is useful for building robust agents that can distinguish between a successful completion and an early termination that might need a retry or a reformulated prompt.

The Agent SDK surfaces `stop_reason` on the final result message so you can check it without parsing individual stream events. Common use cases include detecting refusals (to log or surface a friendlier error to end users), catching `max_tokens` cutoffs (to retry with a higher limit or ask Claude to continue), and logging termination types for observability.

This guide covers:

- [Read `stop_reason`](#read-stop_reason) from result messages in TypeScript
- The [full list of possible values](#available-stop-reasons) and what each means
- How `stop_reason` [interacts with error result subtypes](#stop-reasons-on-error-results) like `error_max_turns`
- A [Python workaround](#read-stop_reason-in-python) using stream events, since `ResultMessage` doesn't include this field yet

<Note>
Direct `stop_reason` access on result messages is currently **TypeScript-only**. The Python SDK's `ResultMessage` does not include this field. For Python, see [Read stop_reason in Python](#read-stop_reason-in-python) for a workaround using stream events.
</Note>

## Read stop_reason

The `stop_reason` field is present on both success and error result messages. Check it after iterating through the message stream:

```typescript TypeScript
import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const message of query({
  prompt: "Write a poem about the ocean"
})) {
  if (message.type === "result") {
    console.log("Stop reason:", message.stop_reason);
    if (message.stop_reason === "refusal") {
      console.log("The model declined this request.");
    }
  }
}
```

## Available stop reasons

| Stop reason | Meaning |
|:------------|:--------|
| `end_turn` | The model finished generating its response normally. |
| `max_tokens` | The response reached the maximum output token limit. |
| `stop_sequence` | The model generated a configured stop sequence. |
| `refusal` | The model declined to fulfill the request. |
| `tool_use` | The model's final output was a tool call. This is uncommon in SDK results because tool calls are normally executed before the result is returned. |
| `null` | No API response was received; for example, an error occurred before the first request, or the result was replayed from a cached session. |

## Stop reasons on error results

Error results (such as `error_max_turns` or `error_during_execution`) also carry `stop_reason`. The value reflects the last assistant message received before the error occurred:

| Result variant | `stop_reason` value |
|:---------------|:-------------------|
| `success` | The stop reason from the final assistant message. |
| `error_max_turns` | The stop reason from the last assistant message before the turn limit was hit. |
| `error_max_budget_usd` | The stop reason from the last assistant message before the budget was exceeded. |
| `error_max_structured_output_retries` | The stop reason from the last assistant message before the retry limit was hit. |
| `error_during_execution` | The last stop reason seen, or `null` if the error occurred before any API response. |

```typescript TypeScript
import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const message of query({
  prompt: "Refactor this module",
  options: { maxTurns: 3 }
})) {
  if (message.type === "result" && message.subtype === "error_max_turns") {
    console.log("Hit turn limit. Last stop reason:", message.stop_reason);
    // stop_reason might be "end_turn" or "tool_use"
    // depending on what the model was doing when the limit hit
  }
}
```

## Detect refusals

Check `stop_reason === "refusal"` to detect when the model declines a request. Previously, detecting refusals required enabling partial message streaming and manually scanning stream events for `message_delta` events. With `stop_reason` on the result message, you can check directly:

```typescript TypeScript
import { query } from "@anthropic-ai/claude-agent-sdk";

async function safeQuery(prompt: string): Promise<string | null> {
  for await (const message of query({ prompt })) {
    if (message.type === "result") {
      if (message.stop_reason === "refusal") {
        console.log("Request was declined. Please revise your prompt.");
        return null;
      }
      if (message.subtype === "success") {
        return message.result;
      }
      return null;
    }
  }
  return null;
}
```

## Read stop_reason in Python

The Python SDK doesn't expose `stop_reason` on `ResultMessage` directly. To access it, enable partial message streaming and scan `StreamEvent` messages for `message_delta` events:

```python Python
from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage
from claude_agent_sdk.types import StreamEvent
import asyncio


async def get_stop_reason(prompt: str):
    stop_reason = None
    result = None
    options = ClaudeAgentOptions(include_partial_messages=True)

    async for message in query(prompt=prompt, options=options):
        if isinstance(message, StreamEvent):
            if message.event.get("type") == "message_delta":
                delta = message.event.get("delta", {})
                if "stop_reason" in delta:
                    stop_reason = delta["stop_reason"]
        elif isinstance(message, ResultMessage):
            result = message.result

    return stop_reason, result


stop_reason, result = asyncio.run(get_stop_reason("Summarize this article"))
print(f"stop_reason: {stop_reason}")  # e.g. "end_turn", "refusal", "tool_use"
print(result)
```

## Next steps

- [Stream responses in real-time](/docs/en/agent-sdk/streaming-output): access raw API events including `message_delta` as they arrive
- [Structured outputs](/docs/en/agent-sdk/structured-outputs): get typed JSON responses from the agent
- [Tracking costs and usage](/docs/en/agent-sdk/cost-tracking): understand token usage and billing from result messages