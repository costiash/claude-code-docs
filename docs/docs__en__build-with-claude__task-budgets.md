# Task budgets

Give Claude an advisory token budget for the full agentic loop to help the model self-regulate on long agentic tasks with task budgets.

---

<Note>
This feature is eligible for [Zero Data Retention (ZDR)](/docs/en/build-with-claude/api-and-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.
</Note>

Task budgets let you tell Claude how many tokens it has for a full agentic loop, including thinking, tool calls, tool results, and output. The model sees a running countdown and uses it to prioritize work and finish gracefully as the budget is consumed.

<Note>
Task budgets are in public beta on [Claude Opus 4.7](/docs/en/about-claude/models/overview). Set the `task-budgets-2026-03-13` beta header to opt in.
</Note>

## When to use task budgets

Task budgets work best for agentic workflows where Claude makes multiple tool calls and decisions before finalizing its output to await the next human response. Use them when:

- You want Claude to self-regulate token spend on long-horizon tasks.
- You have a predictable per-task cost or latency ceiling to enforce.
- You want the model to finish gracefully (summarize findings, report progress) as it approaches the budget rather than cutting off mid-action.

Task budgets complement the [effort parameter](/docs/en/build-with-claude/effort): effort controls how thoroughly Claude reasons about each step, while task budgets cap the total work Claude can do across an agentic loop.

## Setting a task budget

Add `task_budget` to `output_config` and include the beta header:

<CodeGroup>
```bash Shell
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "anthropic-beta: task-budgets-2026-03-13" \
    --header "content-type: application/json" \
    --data '{
        "model": "claude-opus-4-7",
        "max_tokens": 128000,
        "messages": [{
            "role": "user",
            "content": "Review the codebase and propose a refactor plan."
        }],
        "output_config": {
            "effort": "high",
            "task_budget": {"type": "tokens", "total": 64000}
        }
    }'
```

```bash CLI
ant beta:messages create --beta task-budgets-2026-03-13 <<'YAML'
model: claude-opus-4-7
max_tokens: 128000
messages:
  - role: user
    content: Review the codebase and propose a refactor plan.
output_config:
  effort: high
  task_budget:
    type: tokens
    total: 64000
YAML
```

```python Python hidelines={1..2}
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=128000,
    output_config={
        "effort": "high",
        "task_budget": {"type": "tokens", "total": 64000},
    },
    messages=[
        {"role": "user", "content": "Review the codebase and propose a refactor plan."}
    ],
    betas=["task-budgets-2026-03-13"],
)
```

```typescript TypeScript hidelines={1..2}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const response = await client.beta.messages.create({
  model: "claude-opus-4-7",
  max_tokens: 128000,
  output_config: {
    effort: "high",
    task_budget: { type: "tokens", total: 64000 }
  },
  messages: [{ role: "user", content: "Review the codebase and propose a refactor plan." }],
  betas: ["task-budgets-2026-03-13"]
});
```

```go Go hidelines={1..10,-2..}
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	response, _ := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
		Model:     "claude-opus-4-7",
		MaxTokens: 128000,
		Betas:     []anthropic.AnthropicBeta{"task-budgets-2026-03-13"},
		Messages: []anthropic.BetaMessageParam{{
			Role: anthropic.BetaMessageParamRoleUser,
			Content: []anthropic.BetaContentBlockParamUnion{{
				OfText: &anthropic.BetaTextBlockParam{Text: "Review the codebase and propose a refactor plan."},
			}},
		}},
		OutputConfig: anthropic.BetaOutputConfigParam{
			Effort: anthropic.BetaOutputConfigEffortHigh,
			TaskBudget: anthropic.BetaTokenTaskBudgetParam{
				Total: 64000,
			},
		},
	})
	fmt.Println(response)
}
```

```java Java hidelines={1..7,9..11,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.BetaMessage;
import com.anthropic.models.beta.messages.BetaOutputConfig;
import com.anthropic.models.beta.messages.BetaTokenTaskBudget;
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;

public class Main {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCreateParams params = MessageCreateParams.builder()
            .model(Model.CLAUDE_OPUS_4_7)
            .maxTokens(128000L)
            .addUserMessage("Review the codebase and propose a refactor plan.")
            .outputConfig(BetaOutputConfig.builder()
                .effort(BetaOutputConfig.Effort.HIGH)
                .taskBudget(BetaTokenTaskBudget.builder().total(64000L).build())
                .build())
            .addBeta("task-budgets-2026-03-13")
            .build();

        BetaMessage response = client.beta().messages().create(params);
    }
}
```

```csharp C# hidelines={1..3}
using Anthropic;
using Anthropic.Models.Beta.Messages;
using Anthropic.Models.Messages;

var client = new AnthropicClient();

var response = await client.Beta.Messages.Create(new MessageCreateParams
{
    Model = "claude-opus-4-7",
    MaxTokens = 128000,
    Messages = [new() { Role = Role.User, Content = "Review the codebase and propose a refactor plan." }],
    OutputConfig = new BetaOutputConfig
    {
        Effort = Effort.High,
        TaskBudget = new BetaTokenTaskBudget { Total = 64000 },
    },
    Betas = ["task-budgets-2026-03-13"],
});
```

```php PHP hidelines={1..4}
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$response = $client->beta->messages->create(
    model: 'claude-opus-4-7',
    maxTokens: 128000,
    messages: [
        ['role' => 'user', 'content' => 'Review the codebase and propose a refactor plan.'],
    ],
    outputConfig: [
        'effort' => 'high',
        'taskBudget' => ['type' => 'tokens', 'total' => 64000],
    ],
    betas: ['task-budgets-2026-03-13'],
);
```

```ruby Ruby hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

response = client.beta.messages.create(
  model: "claude-opus-4-7",
  max_tokens: 128_000,
  messages: [
    { role: "user", content: "Review the codebase and propose a refactor plan." }
  ],
  output_config: {
    effort: :high,
    task_budget: { type: :tokens, total: 64_000 }
  },
  betas: ["task-budgets-2026-03-13"]
)

puts response
```
</CodeGroup>

The `task_budget` object has three fields:

- `type`: always `"tokens"`.
- `total`: the number of tokens Claude can spend across the agentic loop, including thinking, tool calls, tool results, and output.
- `remaining` (optional): the budget remainder carried over from a prior request. Defaults to `total` when omitted.

## How the budget countdown works

Claude sees a budget-countdown marker injected server-side throughout the conversation. The marker shows how many tokens remain in the current agentic loop and updates as the model generates thinking, tool calls, and output, and as it processes tool results. Claude uses this signal to pace itself and finish gracefully as the budget is consumed.

<Warning>
**The countdown reflects tokens Claude has processed in the current agentic loop, not tokens you resend between turns.** If your client sends the full conversation history on every follow-up request, your client-side token count may differ from the budget Claude is tracking. If you also decrement `remaining` while resending full history, the model sees an under-reported budget and the countdown drops faster than it should, causing Claude to wrap up earlier than the budget actually allows. Set a generous budget and let the model self-regulate against the countdown rather than trying to mirror it client-side.
</Warning>

### Worked example: budget counting across turns

The task budget counts what Claude **sees** (thinking, tool calls and results, and text), not what's in your request payload. In an agentic loop your client resends the full conversation on every request, so the payload grows turn over turn, but the budget only decrements by the tokens Claude sees this turn.

Consider a loop with `task_budget: {type: "tokens", total: 100000}` and a single `bash` tool.

**Turn 1.** You send the initial request:

```json
{
  "messages": [
    { "role": "user", "content": "Audit this repo for security issues and report findings." }
  ]
}
```

Claude thinks, then emits a tool call and stops with `stop_reason: "tool_use"`:

```json
{
  "role": "assistant",
  "content": [
    {
      "type": "thinking",
      "thinking": "I'll start by listing dependencies to look for known-vulnerable packages..."
    },
    {
      "type": "tool_use",
      "id": "toolu_01",
      "name": "bash",
      "input": { "command": "cat package.json && npm audit --json" }
    }
  ]
}
```

Suppose this assistant turn (thinking plus the tool call) totals 5,000 generated tokens. The countdown Claude saw during generation ended near `remaining` ≈ 95,000.

**Turn 2.** Your client executes the tool, then resends the full history with the tool result appended:

```json
{
  "messages": [
    { "role": "user", "content": "Audit this repo for security issues and report findings." },
    {
      "role": "assistant",
      "content": [
        { "type": "thinking", "thinking": "I'll start by listing dependencies..." },
        {
          "type": "tool_use",
          "id": "toolu_01",
          "name": "bash",
          "input": { "command": "cat package.json && npm audit --json" }
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01",
          "content": "<2,800 tokens of npm audit output>"
        }
      ]
    }
  ]
}
```

The resent turn-1 user and assistant messages are not counted again, but the 2,800-token tool result is new content Claude sees this turn and counts against the budget. Claude spends another 4,000 tokens on thinking and a second tool call (`grep -rn "eval(" src/`). The countdown ends near `remaining` ≈ 88,200.

**Turn 3.** Full history resent again with the second tool result (1,200 tokens of grep output) appended. Claude writes a 6,000-token final findings report and stops with `stop_reason: "end_turn"`. `remaining` ≈ 81,000.

Putting the three turns side by side makes the distinction between payload size and budget spend explicit:

| Turn | Request payload (approx. input tokens you sent) | Tokens counted against budget this turn | Budget `remaining` after |
|---|---|---|---|
| 1 | ~20 | 5,000 (thinking + `tool_use`) | ~95,000 |
| 2 | ~7,800 (turn 1 history + tool result) | 6,800 (2,800 tool result + 4,000 thinking and `tool_use`) | ~88,200 |
| 3 | ~13,000 (full history + second tool result) | 7,200 (1,200 tool result + 6,000 `text`) | ~81,000 |
| **Total** | **~20,820 sent across requests** | **19,000 counted against budget** | — |

Your client sent the turn-1 user message three times and the turn-1 assistant message twice, but each was counted once. The budget spent 19,000 of 100,000 tokens, even though the cumulative payload your client transmitted was larger and the prompt-cached input on turns 2 and 3 was larger still.

### Carrying a budget across compaction with `remaining`

If your agentic loop compacts or rewrites context between requests (for example, by summarizing earlier turns), the server has no memory of how much budget was spent before compaction. Pass `remaining` on the next request so the countdown continues from where you left off rather than resetting to `total`:

<CodeGroup>
```python Python
output_config = {
    "effort": "high",
    "task_budget": {
        "type": "tokens",
        "total": 128000,
        "remaining": 128000 - tokens_spent_so_far,
    },
}
```

```typescript TypeScript
const output_config = {
  effort: "high",
  task_budget: {
    type: "tokens",
    total: 128000,
    remaining: 128000 - tokensSpentSoFar
  }
};
```

```go Go
outputConfig := anthropic.BetaOutputConfigParam{
	Effort: anthropic.BetaOutputConfigEffortHigh,
	TaskBudget: anthropic.BetaTokenTaskBudgetParam{
		Total:     128000,
		Remaining: anthropic.Int(128000 - tokensSpentSoFar),
	},
}
```

```java Java
BetaOutputConfig outputConfig = BetaOutputConfig.builder()
    .effort(BetaOutputConfig.Effort.HIGH)
    .taskBudget(BetaTokenTaskBudget.builder()
        .total(128000L)
        .remaining(128000L - tokensSpentSoFar)
        .build())
    .build();
```

```csharp C#
var outputConfig = new BetaOutputConfig
{
    Effort = Effort.High,
    TaskBudget = new BetaTokenTaskBudget
    {
        Total = 128000,
        Remaining = 128000 - tokensSpentSoFar,
    },
};
```

```php PHP
$outputConfig = [
    'effort' => 'high',
    'taskBudget' => [
        'type' => 'tokens',
        'total' => 128000,
        'remaining' => 128000 - $tokensSpentSoFar,
    ],
];
```

```ruby Ruby
output_config = {
  effort: :high,
  task_budget: {
    type: :tokens,
    total: 128_000,
    remaining: 128_000 - tokens_spent_so_far
  }
}
```
</CodeGroup>

For loops that resend the full uncompacted history on every turn, omit `remaining` and let the server track the countdown.

## Task budgets are advisory, not enforced

Task budgets are a **soft hint, not a hard cap**. Claude may occasionally exceed the budget if it is in the middle of an action that would be more disruptive to interrupt than to finish. The enforced limit on total output tokens is still `max_tokens`, which truncates the response with `stop_reason: "max_tokens"` when reached.

For a hard cap on cost or latency, combine task budgets with a reasonable `max_tokens` value:

- Use `task_budget` to give Claude a target to pace against.
- Use `max_tokens` as the absolute ceiling that prevents runaway generation.

Because `task_budget` spans the full agentic loop (potentially many requests) while `max_tokens` caps each individual request, the two values are independent; one is not required to be at or below the other.

<Warning>
**A budget that is too small for the task can cause refusal-like behavior.** When Claude sees a budget that is clearly insufficient for the work being asked (for example, a 20,000-token budget for a multi-hour agentic coding task), it may decline to attempt the task at all, scope it down aggressively, or stop early with a partial result rather than start work it cannot finish. If you observe unexpected refusals or premature stops after setting a budget, raise the budget before debugging other parameters. Size budgets against your actual task-length distribution rather than a fixed default; see [Choosing a budget](#choosing-a-budget).
</Warning>

## Choosing a budget

The right budget depends on how much work your agentic loop currently does. Rather than guessing, measure your existing token usage first and then tune from there.

### Measure your current usage

Run a representative sample of tasks **without** `task_budget` set and record the total tokens Claude spends per task. For an agentic loop, sum `usage.output_tokens` plus thinking and tool-result tokens across every request in the loop:

<CodeGroup>
```python Python
def run_task_and_count_tokens(messages: list) -> int:
    """Runs an agentic loop to completion and returns total tokens spent."""
    total_spend = 0
    while True:
        response = client.beta.messages.create(
            model="claude-opus-4-7",
            max_tokens=128000,
            messages=messages,
            tools=tools,
            betas=["task-budgets-2026-03-13"],
        )
        # Count what Claude generated this turn (output covers text + thinking + tool calls).
        # Tool-result tokens also count against the budget; add the token count of the
        # tool_result blocks you append below if you want client-side tracking to match
        # the server-side countdown.
        total_spend += response.usage.output_tokens
        if response.stop_reason == "end_turn":
            return total_spend
        # Append the assistant turn and your tool results, then continue the loop.
        messages += [
            {"role": "assistant", "content": response.content},
            {"role": "user", "content": run_tools(response.content)},
        ]
```

```typescript TypeScript
async function runTaskAndCountTokens(
  messages: Anthropic.Beta.BetaMessageParam[]
): Promise<number> {
  let totalSpend = 0;
  while (true) {
    const response = await client.beta.messages.create({
      model: "claude-opus-4-7",
      max_tokens: 128000,
      messages,
      tools,
      betas: ["task-budgets-2026-03-13"]
    });
    // Count what Claude generated this turn (output covers text + tool calls;
    // add cache creation and thinking via the same usage object if you opt in).
    totalSpend += response.usage.output_tokens;
    if (response.stop_reason === "end_turn") {
      return totalSpend;
    }
    // Append the assistant turn and your tool results, then continue the loop.
    messages = [
      ...messages,
      { role: "assistant", content: response.content },
      { role: "user", content: runTools(response.content) }
    ];
  }
}
```
</CodeGroup>

Run this across a representative set of tasks and record the distribution. Start with the p99 of your per-task token spend to understand how providing the model with a task budget may modify the model's behavior, then test up or down as needed.

The minimum accepted `task_budget.total` is **20,000 tokens**; values below the minimum return a 400 error.

## Interaction with other parameters

- **`max_tokens`:** Orthogonal to task budgets. `max_tokens` is a hard per-request cap on generated tokens, while `task_budget` is an advisory cap across the full agentic loop (potentially spanning many requests). At `xhigh` or `max` effort, set `max_tokens` to at least 64k to give Claude room to think and act on each request.
- **[Effort](/docs/en/build-with-claude/effort):** Effort controls how deeply Claude reasons per step. Task budgets control how much total work Claude does across an agentic loop. The two are complementary: effort tunes depth, task budgets tune breadth.
- **[Adaptive thinking](/docs/en/build-with-claude/adaptive-thinking):** Task budgets include thinking tokens in the count, so adaptive thinking naturally scales down as the budget depletes.
- **[Prompt caching](/docs/en/build-with-claude/prompt-caching):** The budget-countdown marker is injected server-side per turn, so it does not match across requests. If your client decrements `task_budget.remaining` on each follow-up request, the changed value invalidates any cache prefix that contains it. To preserve caching, set the budget once on the initial request and let the model self-regulate against the server-side countdown rather than mutating the budget client-side.

## Feature support

| Model | Support |
|-------|---------|
| Claude Opus 4.7 | Public beta (set `task-budgets-2026-03-13` header) |
| Claude Opus 4.6 | Not supported |
| Claude Sonnet 4.6 | Not supported |
| Claude Haiku 4.5 | Not supported |

Task budgets are not supported on [Claude Code](https://docs.claude.com/en/docs/claude-code) or Cowork surfaces at launch. Use task budgets directly via the Messages API on Claude Opus 4.7.