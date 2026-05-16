# Advisor tool

Pair a faster executor model with a higher-intelligence advisor model that provides strategic guidance mid-generation.

---

The advisor tool lets a faster, lower-cost **executor model** consult a higher-intelligence **advisor model** mid-generation for strategic guidance. The advisor reads the full conversation, produces a plan or course correction (typically 400 to 700 text tokens, 1,400 to 1,800 tokens total including thinking), and the executor continues with the task.

This pattern fits long-horizon agentic workloads (coding agents, computer use, multi-step research pipelines) where most turns are mechanical but having an excellent plan is crucial. You get close to advisor-solo quality while the bulk of token generation happens at executor-model rates.

<Note>
  The advisor tool is in beta. Include the beta header `advisor-tool-2026-03-01`
  in your requests. To request access or share feedback, contact your Anthropic
  account team.
</Note>

<Note>
This feature is eligible for [Zero Data Retention (ZDR)](/docs/en/build-with-claude/api-and-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.
</Note>

## When to use it

Early benchmarks show meaningful gains for these configurations:

- **You currently use Sonnet on complex tasks:** Add Opus as the advisor for a quality lift at similar or lower total cost.
- **You currently use Haiku and want a step up in intelligence:** Add Opus as the advisor. Expect higher cost than Haiku alone, but lower than switching the executor to a larger model.

Results are task-dependent. Evaluate on your own workload.

The advisor is a weaker fit for single-turn Q&A (nothing to plan), pure pass-through model pickers where your users already choose their own cost and quality tradeoff, or workloads where every turn genuinely requires the advisor model's full capability.

## Model compatibility

The executor model (the top-level `model` field) and the advisor model (the `model` field inside the tool definition) must form a valid pair. The advisor must be at least as capable as the executor.

| Executor models                                | Advisor models                      |
| ---------------------------------------------- | ----------------------------------- |
| Claude Haiku 4.5 (`claude-haiku-4-5-20251001`) | Claude Opus 4.7 (`claude-opus-4-7`) |
| Claude Sonnet 4.6 (`claude-sonnet-4-6`)        | Claude Opus 4.7 (`claude-opus-4-7`) |
| Claude Opus 4.6 (`claude-opus-4-6`)            | Claude Opus 4.7 (`claude-opus-4-7`) |
| Claude Opus 4.7 (`claude-opus-4-7`)            | Claude Opus 4.7 (`claude-opus-4-7`) |

If you request an invalid pair, the API returns a `400 invalid_request_error` naming the unsupported combination.

## Platform availability

The advisor tool is available in beta on the Claude API and on [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws). It is not currently available on AWS Bedrock, Vertex AI, or Microsoft Foundry.

## Quick start

<CodeGroup>
```bash cURL
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "anthropic-beta: advisor-tool-2026-03-01" \
    --header "content-type: application/json" \
    --data '{
        "model": "claude-sonnet-4-6",
        "max_tokens": 4096,
        "tools": [
            {
                "type": "advisor_20260301",
                "name": "advisor",
                "model": "claude-opus-4-7"
            }
        ],
        "messages": [{
            "role": "user",
            "content": "Build a concurrent worker pool in Go with graceful shutdown."
        }]
    }'
```

```bash CLI
ant beta:messages create --beta advisor-tool-2026-03-01 <<'YAML'
model: claude-sonnet-4-6
max_tokens: 4096
tools:
  - type: advisor_20260301
    name: advisor
    model: claude-opus-4-7
messages:
  - role: user
    content: Build a concurrent worker pool in Go with graceful shutdown.
YAML
```

```python Python hidelines={1..2}
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=4096,
    betas=["advisor-tool-2026-03-01"],
    tools=[
        {
            "type": "advisor_20260301",
            "name": "advisor",
            "model": "claude-opus-4-7",
        }
    ],
    messages=[
        {
            "role": "user",
            "content": "Build a concurrent worker pool in Go with graceful shutdown.",
        }
    ],
)

print(response)
```

```typescript TypeScript hidelines={1..5,-3..-1}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

async function main() {
  const response = await client.beta.messages.create({
    model: "claude-sonnet-4-6",
    max_tokens: 4096,
    betas: ["advisor-tool-2026-03-01"],
    tools: [
      {
        type: "advisor_20260301",
        name: "advisor",
        model: "claude-opus-4-7"
      }
    ],
    messages: [
      {
        role: "user",
        content: "Build a concurrent worker pool in Go with graceful shutdown."
      }
    ]
  });

  console.log(response);
}

main().catch(console.error);
```

```csharp C# nocheck hidelines={1}
using Anthropic;
using Anthropic.Models.Beta.Messages;
using Messages = Anthropic.Models.Messages;

var client = new AnthropicClient();

var parameters = new MessageCreateParams
{
    Model = Messages::Model.ClaudeSonnet4_6,
    MaxTokens = 4096,
    Tools = new BetaToolUnion[]
    {
        new BetaAdvisorTool20260301
        {
            Model = Messages::Model.ClaudeOpus4_7
        }
    },
    Messages =
    [
        new BetaMessageParam
        {
            Role = Role.User,
            Content = "Build a concurrent worker pool in Go with graceful shutdown."
        }
    ],
    Betas = ["advisor-tool-2026-03-01"]
};

var response = await client.Beta.Messages.Create(parameters);
Console.WriteLine(response);
```

```go Go nocheck hidelines={1..11,-1}
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	response, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
		Model:     anthropic.ModelClaudeSonnet4_6,
		MaxTokens: 4096,
		Tools: []anthropic.BetaToolUnionParam{
			{OfAdvisorTool20260301: &anthropic.BetaAdvisorTool20260301Param{
				Model: anthropic.ModelClaudeOpus4_7,
			}},
		},
		Messages: []anthropic.BetaMessageParam{
			anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Build a concurrent worker pool in Go with graceful shutdown.")),
		},
		Betas: []anthropic.AnthropicBeta{
			anthropic.AnthropicBetaAdvisorTool2026_03_01,
		},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(response)
}
```

```php PHP hidelines={1..4}
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$response = $client->beta->messages->create(
    maxTokens: 4096,
    messages: [
        [
            'role' => 'user',
            'content' => 'Build a concurrent worker pool in Go with graceful shutdown.',
        ],
    ],
    model: 'claude-sonnet-4-6',
    tools: [
        [
            'type' => 'advisor_20260301',
            'name' => 'advisor',
            'model' => 'claude-opus-4-7',
        ],
    ],
    betas: ['advisor-tool-2026-03-01'],
);

echo $response;
```

```ruby Ruby hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

response = client.beta.messages.create(
  model: "claude-sonnet-4-6",
  max_tokens: 4096,
  tools: [
    {
      type: "advisor_20260301",
      name: "advisor",
      model: "claude-opus-4-7"
    }
  ],
  messages: [
    {
      role: "user",
      content: "Build a concurrent worker pool in Go with graceful shutdown."
    }
  ],
  betas: ["advisor-tool-2026-03-01"]
)

puts response
```

</CodeGroup>

## How it works

When you add the advisor tool to your `tools` array, the executor model decides when to call it, just like any other tool. When the executor invokes the advisor:

1. The executor emits a `server_tool_use` block with `name: "advisor"` and an empty `input`. The executor signals timing; the server supplies context.
2. Anthropic runs a separate inference pass on the advisor model server-side, passing the executor's full transcript. The advisor sees the system prompt, all tool definitions, all prior turns, and all prior tool results.
3. The advisor's response returns to the executor as an `advisor_tool_result` block.
4. The executor continues generating, informed by the advice.

All of this happens inside a single `/v1/messages` request. No extra round trips on your side.

The advisor itself runs without tools and without context management. Its thinking blocks are dropped before the result returns; only the advice text reaches the executor.

## Tool parameters

| Parameter               | Type           | Default      | Description                                                                                                                                        |
| ----------------------- | -------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`                  | string         | _required_   | Must be `"advisor_20260301"`.                                                                                                                      |
| `name`                  | string         | _required_   | Must be `"advisor"`.                                                                                                                               |
| `model`                 | string         | _required_   | The advisor model ID, such as `"claude-opus-4-7"`. Billed at this model's rates for the sub-inference.                                             |
| `max_uses`              | integer        | unlimited    | Maximum number of advisor calls allowed in a single request. Once the executor reaches this cap, further advisor calls return an `advisor_tool_result_error` with `error_code: "max_uses_exceeded"` and the executor continues without further advice. This is a per-request cap, not a per-conversation cap; see [Cost control](#cost-control) for conversation-level limits. |
| `caching`               | object \| null | `null` (off) | Enables prompt caching for the advisor's own transcript across calls within a conversation. See [Advisor prompt caching](#advisor-prompt-caching). |

The `caching` object has the shape `{"type": "ephemeral", "ttl": "5m" | "1h"}`. Unlike `cache_control` on content blocks, this is not a breakpoint marker; it is an on/off switch. The server decides where cache boundaries go.

## Response structure

### Successful advisor call

When the advisor is invoked, a `server_tool_use` block is followed by an `advisor_tool_result` block in the assistant's content:

```json
{
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "Let me consult the advisor on this."
    },
    {
      "type": "server_tool_use",
      "id": "srvtoolu_abc123",
      "name": "advisor",
      "input": {}
    },
    {
      "type": "advisor_tool_result",
      "tool_use_id": "srvtoolu_abc123",
      "content": {
        "type": "advisor_result",
        "text": "Use a channel-based coordination pattern. The tricky part is draining in-flight work during shutdown: close the input channel first, then wait on a WaitGroup..."
      }
    },
    {
      "type": "text",
      "text": "Here's the implementation. I'm using a channel-based coordination pattern to avoid writer starvation..."
    }
  ]
}
```

The `server_tool_use.input` is always empty. The server constructs the advisor's view from the full transcript automatically; nothing the executor puts in `input` reaches the advisor.

### Result variants

The `advisor_tool_result.content` field is a discriminated union. For successful calls, the variant depends on the advisor model:

| Variant                   | Fields              | Returned when                                                       |
| ------------------------- | ------------------- | ------------------------------------------------------------------- |
| `advisor_result`          | `text`              | The advisor model returns plaintext (for example, Claude Opus 4.7). |
| `advisor_redacted_result` | `encrypted_content` | The advisor model returns encrypted output.                         |

With `advisor_result`, the `text` field contains human-readable advice. With `advisor_redacted_result`, the `encrypted_content` field contains an opaque blob that you cannot read; on the next turn, the server decrypts it and renders the plaintext into the executor's prompt.

In both cases, round-trip the content verbatim on subsequent turns. If you switch advisor models mid-conversation, branch on `content.type` to handle both shapes.

### Error results

If the advisor call fails, the result carries an error:

```json
{
  "type": "advisor_tool_result",
  "tool_use_id": "srvtoolu_abc123",
  "content": {
    "type": "advisor_tool_result_error",
    "error_code": "overloaded"
  }
}
```

The executor sees the error and continues without further advice. The request itself does not fail.

| `error_code`              | Meaning                                                                                                     |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `max_uses_exceeded`       | The request reached the `max_uses` cap set on the tool definition. Further advisor calls in the same request return this error. |
| `too_many_requests`       | The advisor sub-inference was rate-limited.                                                                 |
| `overloaded`              | The advisor sub-inference hit capacity limits.                                                              |
| `prompt_too_long`         | The transcript exceeded the advisor model's context window.                                                 |
| `execution_time_exceeded` | The advisor sub-inference timed out.                                                                        |
| `unavailable`             | Any other advisor failure.                                                                                  |

Advisor rate limits draw from the same per-model bucket as direct calls to the advisor model. A rate limit on the advisor appears as `too_many_requests` inside the tool result; a rate limit on the executor fails the whole request with HTTP 429.

## Multi-turn conversations

Pass the full assistant content, including `advisor_tool_result` blocks, back to the API on subsequent turns:

```python
import anthropic

client = anthropic.Anthropic()

tools = [
    {
        "type": "advisor_20260301",
        "name": "advisor",
        "model": "claude-opus-4-7",
    }
]

messages = [
    {
        "role": "user",
        "content": "Build a concurrent worker pool in Go with graceful shutdown.",
    }
]

response = client.beta.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=4096,
    betas=["advisor-tool-2026-03-01"],
    tools=tools,
    messages=messages,
)

# Append the full response content, including any advisor_tool_result blocks
messages.append({"role": "assistant", "content": response.content})

# Continue the conversation
messages.append({"role": "user", "content": "Now add a max-in-flight limit of 10."})

response = client.beta.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=4096,
    betas=["advisor-tool-2026-03-01"],
    tools=tools,
    messages=messages,
)
```

If you omit the advisor tool from `tools` on a follow-up turn while the message history still contains `advisor_tool_result` blocks, the API returns a `400 invalid_request_error`.

<Note>
  The advisor tool has no built-in conversation-level cap. To limit advisor
  calls across a conversation, count them client-side. When you reach your
  ceiling, remove the advisor tool from your `tools` array **and** strip all
  `advisor_tool_result` blocks from your message history to avoid a
  `400 invalid_request_error`.
</Note>

## Streaming

The advisor sub-inference does not stream. The executor's stream pauses while the advisor runs, then the full result arrives in a single event.

The `server_tool_use` block with `name: "advisor"` signals that an advisor call is starting. The pause begins when that block closes (`content_block_stop`). During the pause, the stream is quiet except for standard SSE `ping` keepalives emitted roughly every 30 seconds; short advisor calls may show no pings.

When the advisor finishes, the `advisor_tool_result` arrives fully formed in a single `content_block_start` event (no deltas). Executor output then resumes streaming.

A `message_delta` event follows with the updated `usage.iterations` array reflecting the advisor's token counts.

## Usage and billing

Advisor calls run as a separate sub-inference billed at the advisor model's rates. Usage is reported in the `usage.iterations[]` array:

```json
{
  "usage": {
    "input_tokens": 412,
    "cache_read_input_tokens": 0,
    "cache_creation_input_tokens": 0,
    "output_tokens": 531,
    "iterations": [
      {
        "type": "message",
        "input_tokens": 412,
        "cache_read_input_tokens": 0,
        "cache_creation_input_tokens": 0,
        "output_tokens": 89
      },
      {
        "type": "advisor_message",
        "model": "claude-opus-4-7",
        "input_tokens": 823,
        "cache_read_input_tokens": 0,
        "cache_creation_input_tokens": 0,
        "output_tokens": 1612
      },
      {
        "type": "message",
        "input_tokens": 1348,
        "cache_read_input_tokens": 412,
        "cache_creation_input_tokens": 0,
        "output_tokens": 442
      }
    ]
  }
}
```

Top-level `usage` fields reflect executor tokens only. Advisor tokens are not rolled into the top-level totals because they are billed at a different rate. Iterations with `type: "advisor_message"` are billed at the advisor model's rates; iterations with `type: "message"` are billed at the executor model's rates.

The aggregation rules differ by field. Top-level `output_tokens` is the sum of all executor iterations. Top-level `input_tokens` and `cache_read_input_tokens` reflect the first executor iteration only; subsequent executor iterations' inputs are not re-summed because they include prior output tokens. Use `usage.iterations` for a full per-iteration breakdown when building cost-tracking logic.

Advisor output is typically 400 to 700 text tokens, or 1,400 to 1,800 tokens total including thinking. The cost savings come from the advisor not generating your full final output; the executor does that at its lower rate.

The top-level `max_tokens` applies to executor output only. It does not bound advisor sub-inference tokens. The advisor's tokens also do not draw from any task budget applied to the executor.

## Advisor prompt caching

There are two independent caching layers.

### Executor-side caching

The `advisor_tool_result` block is cacheable like any other content block. A `cache_control` breakpoint placed after it on a subsequent turn will hit. The executor's prompt always contains the plaintext advice regardless of whether your client received `text` or `encrypted_content`, so caching behavior is identical for both result variants.

### Advisor-side caching

Set `caching` on the tool definition to enable prompt caching for the advisor's own transcript across calls within the same conversation:

```python
tools = [
    {
        "type": "advisor_20260301",
        "name": "advisor",
        "model": "claude-opus-4-7",
        "caching": {"type": "ephemeral", "ttl": "5m"},
    }
]
```

The advisor's prompt on the Nth call is the (N-1)th call's prompt with one more segment appended, so the prefix is stable across calls. With `caching` enabled, each advisor call writes a cache entry; the next call reads up to that point and pays only for the delta. You'll see `cache_read_input_tokens` become non-zero on the second and later `advisor_message` iterations.

**When to enable it:** The cache write costs more than the reads save when the advisor is called two or fewer times per conversation. Caching breaks even at roughly three advisor calls and improves from there. Enable it for long agent loops; keep it off for short tasks.

**Keep it consistent:** Set `caching` once and leave it for the whole conversation. Toggling it off and on mid-conversation causes cache misses.

<Warning>
  [`clear_thinking`](/docs/en/build-with-claude/context-editing) with a `keep`
  value other than `"all"` shifts the advisor's quoted transcript each turn,
  causing advisor-side cache misses. This is a cost degradation only; advice
  quality is unaffected. When extended thinking is enabled without explicit
  `clear_thinking` configuration, the API defaults to
  `keep: {type: "thinking_turns", value: 1}`, which triggers this behavior
  (the default on earlier Opus/Sonnet models and all Haiku models; on Opus
  4.5+ and Sonnet 4.6+ the default is to keep all turns). Set `keep: "all"`
  to preserve advisor cache stability.
</Warning>

## Combining with other tools

The advisor tool composes with other server-side and client-side tools. Add them all to the same `tools` array:

```python
tools = [
    {
        "type": "web_search_20250305",
        "name": "web_search",
        "max_uses": 5,
    },
    {
        "type": "advisor_20260301",
        "name": "advisor",
        "model": "claude-opus-4-7",
    },
    {
        "name": "run_bash",
        "description": "Run a bash command",
        "input_schema": {
            "type": "object",
            "properties": {"command": {"type": "string"}},
        },
    },
]
```

The executor can search the web, call the advisor, and use your custom tools in the same turn. The advisor's plan can inform which tools the executor reaches for next.

| Feature                                                          | Interaction                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Batch processing](/docs/en/build-with-claude/batch-processing)         | Supported. `usage.iterations` is reported per item.                                                                                                                                                                                                                                |
| [Token counting](/docs/en/build-with-claude/token-counting)      | Returns the executor's first-iteration input tokens only. For a rough advisor estimate, call `count_tokens` with `model` set to the advisor model and the same messages.                                                                                                           |
| [Context editing](/docs/en/build-with-claude/context-editing) | `clear_tool_uses` is not fully compatible with advisor tool blocks. With `clear_thinking`, see the earlier caching warning.                                                                                                    |
| `pause_turn`                                                     | A dangling advisor call ends the response with `stop_reason: "pause_turn"` and the `server_tool_use` block as the last content block. The advisor executes on resumption. See [Server tools](/docs/en/agents-and-tools/tool-use/server-tools#the-server-side-loop-and-pause-turn). |

## Best practices

### Prompting for coding and agent tasks

The advisor tool ships with a built-in description that nudges the executor to call it near the start of complex tasks and when it hits difficulty. For research tasks, no additional prompting is typically needed.

On coding and agent tasks, the advisor produces higher intelligence at similar cost when it reduces total tool calls and conversation length. Two timings drive this improvement:

1. An early first advisor call, after a few exploratory reads are in the transcript.
2. For difficult tasks, a final advisor call after file writes and test outputs are in the transcript.

If your agent exposes other planner-like tools (for example, a todo list tool), prompt the model to call the advisor before those tools so the advisor's plan funnels into them. The suggested system prompt below reinforces the early-call pattern; add your own funnel-in sentence pointing at whichever planner tools your agent exposes.

#### Suggested system prompt for coding tasks

For coding tasks where you want consistent advisor timing and around two to three calls per task, prepend the following blocks to your executor system prompt before any other sentences that mention the advisor. On internal coding evaluations this pattern produced the highest intelligence at near-Sonnet cost.

Timing guidance:

```text
You have access to an `advisor` tool backed by a stronger reviewer model. It takes NO parameters — when you call advisor(), your entire conversation history is automatically forwarded. They see the task, every tool call you've made, every result you've seen.

Call advisor BEFORE substantive work — before writing, before committing to an interpretation, before building on an assumption. If the task requires orientation first (finding files, fetching a source, seeing what's there), do that, then call advisor. Orientation is not substantive work. Writing, editing, and declaring an answer are.

Also call advisor:
- When you believe the task is complete. BEFORE this call, make your deliverable durable: write the file, save the result, commit the change. The advisor call takes time; if the session ends during it, a durable result persists and an unwritten one doesn't.
- When stuck — errors recurring, approach not converging, results that don't fit.
- When considering a change of approach.

On tasks longer than a few steps, call advisor at least once before committing to an approach and once before declaring done. On short reactive tasks where the next action is dictated by tool output you just read, you don't need to keep calling — the advisor adds most of its value on the first call, before the approach crystallizes.
```

How the executor should treat the advice (place directly after the timing block):

```text
Give the advice serious weight. If you follow a step and it fails empirically, or you have primary-source evidence that contradicts a specific claim (the file says X, the paper states Y), adapt. A passing self-test is not evidence the advice is wrong — it's evidence your test doesn't check what the advice is checking.

If you've already retrieved data pointing one way and the advisor points another: don't silently switch. Surface the conflict in one more advisor call — "I found X, you suggest Y, which constraint breaks the tie?" The advisor saw your evidence but may have underweighted it; a reconcile call is cheaper than committing to the wrong branch.
```

#### Trimming advisor output length

Advisor output is the advisor's largest cost driver, and `max_tokens` does not bound it. The advisor sees both your system prompt and your user messages as quoted context about the executor's task, so instructions that address the advisor directly are followed much more reliably than third-person descriptions. The most effective placement Anthropic tested is a line in the user message:

```text
(Advisor: please keep your guidance under 80 words — I need a focused starting point, not a comprehensive plan.)
```

This line can be prefixed programmatically by your agent framework before sending the request. The limit is a soft constraint; the advisor will occasionally exceed it, so ask for roughly 80 percent of your true ceiling.

<Note>
  In Anthropic's testing this line also increased how often the executor
  consults the advisor, but the net effect was still lower total cost
  (more consults, each shorter).
</Note>

Pair this approach with the timing guidance in [Suggested system prompt for coding tasks](#suggested-system-prompt-for-coding-tasks) for the strongest cost-versus-quality tradeoff.

### Pairing with effort settings

For coding tasks, pairing a Sonnet executor at medium [effort](/docs/en/build-with-claude/effort) with an Opus advisor achieves intelligence comparable to Sonnet at default effort, at lower cost. For maximum intelligence, keep the executor at default effort.

### Cost control

- For conversation-level budgets, count advisor calls client-side. When you reach your cap, remove the advisor tool from `tools` **and** strip all `advisor_tool_result` blocks from your message history to avoid a `400 invalid_request_error`.
- Enable `caching` only for conversations where you expect three or more advisor calls.

## Limitations

- **Advisor output does not stream.** Expect a pause in the stream while the sub-inference runs.
- **No built-in conversation-level cap on advisor calls.** Track and cap them client-side.
- **`max_tokens` applies to executor output only.** It does not bound advisor tokens.
- **[Priority Tier](/docs/en/api/service-tiers)** is honored for each model. Priority Tier on the executor model does not extend to the advisor; you need Priority Tier on the advisor model specifically.