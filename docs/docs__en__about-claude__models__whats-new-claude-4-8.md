# What's new in Claude Opus 4.8

Overview of new features and behavior changes in Claude Opus 4.8.

---

Claude Opus 4.8 is built for complex agentic coding and enterprise work. It builds on Claude Opus 4.7. This page summarizes everything new at launch, including fast mode (research preview on the Claude API) and a lower 1,024-token minimum cacheable prompt length.

## New model

| Model           | API model ID    | Description                                    |
| --------------- | --------------- | ---------------------------------------------- |
| Claude Opus 4.8 | claude-opus-4-8 | For complex agentic coding and enterprise work |

Claude Opus 4.8 supports the [1M token context window](/docs/en/build-with-claude/context-windows) by default on the Claude API, Amazon Bedrock, Google Cloud, and Microsoft Foundry, 128k max output tokens, [adaptive thinking](/docs/en/build-with-claude/adaptive-thinking), and the same set of tools and platform features as Claude Opus 4.7.

For complete pricing and specs, see the [models overview](/docs/en/about-claude/models/overview).

## New features

### Mid-conversation system messages

Claude Opus 4.8 accepts `role: "system"` messages immediately after a user turn in the `messages` array (subject to [placement rules](/docs/en/build-with-claude/mid-conversation-system-messages#limitations)). This lets you append updated instructions later in a long-running conversation without restating the full system prompt. Updating instructions this way preserves [prompt cache](/docs/en/build-with-claude/prompt-caching) hits on the earlier turns and reduces input cost on agentic loops. No beta header is required. See [Mid-conversation system messages](/docs/en/build-with-claude/mid-conversation-system-messages) for usage details.

### Refusal stop details

The `stop_details` object on refusal responses (available since Claude Opus 4.7) is now publicly documented. When Claude declines to complete a request, this object describes the category of refusal, in addition to the existing `refusal` stop reason. Your application can use it to tell apart different classes of declined request and route the user to the right next step. No beta header is required. See [Refusals and fallback](/docs/en/build-with-claude/refusals-and-fallback#refusal-response) for the category list and [Stop reasons and fallback](/docs/en/build-with-claude/handling-stop-reasons) for handling guidance.

### Effort defaults

The [effort parameter](/docs/en/build-with-claude/effort) default on Claude Opus 4.8 is `high` on all surfaces, including the Claude API and Claude Code. If you set effort explicitly today, your setting is unchanged. See [Effort](/docs/en/build-with-claude/effort) for per-level guidance.

### Fast mode

[Fast mode](/docs/en/build-with-claude/fast-mode) is now available for Claude Opus 4.8 as a research preview on the Claude API. Set `speed: "fast"` with the `fast-mode-2026-02-01` beta header to get up to 2.5x higher output tokens per second from the same model at premium pricing. See [Fast mode](/docs/en/build-with-claude/fast-mode) for access, supported models, and pricing.

### Lower prompt cache minimum

The minimum cacheable prompt length on Claude Opus 4.8 is 1,024 tokens, down from 2,048 tokens on Claude Opus 4.7. Prompts that were too short to cache on Claude Opus 4.7 can now create cache entries with no code changes. See [Prompt caching](/docs/en/build-with-claude/prompt-caching#cache-limitations) for per-model minimums.

## API constraints inherited from Claude Opus 4.7

<Note>
  These constraints are unchanged from Claude Opus 4.7, so code that already runs on Claude Opus 4.7 needs no changes. They apply to the Messages API only. Claude Managed Agents are unaffected.
</Note>

### Sampling parameters not supported

Setting `temperature`, `top_p`, or `top_k` to a non-default value returns a 400 error on Claude Opus 4.8, same as on Claude Opus 4.7. Omit these parameters and use prompting to guide the model's behavior.

### Adaptive thinking is the only thinking mode

Like Claude Opus 4.7, Claude Opus 4.8 does not support extended thinking budgets. Setting `thinking: {type: "enabled", budget_tokens: N}` returns a 400 error.

The following diff updates a request written for Claude Opus 4.6 or earlier to run on Claude Opus 4.8. The removed lines (`-`) set the old model ID and the manual thinking budget that Claude Opus 4.8 rejects. The added lines (`+`) set the new model ID, switch to [adaptive thinking](/docs/en/build-with-claude/adaptive-thinking), and control thinking depth with the [effort parameter](/docs/en/build-with-claude/effort), passed in the top-level `output_config` field. The model determines when and how much to think on each turn. If you remove the `thinking` field entirely, requests run without thinking:

<CodeGroup>
  ```diff cURL
   curl https://api.anthropic.com/v1/messages \
        --header "x-api-key: $ANTHROPIC_API_KEY" \
        --header "anthropic-version: 2023-06-01" \
        --header "content-type: application/json" \
        --data \
   '{
  -    "model": "claude-opus-4-6",
  +    "model": "claude-opus-4-8",
       "max_tokens": 16000,
       "thinking": {
  -        "type": "enabled",
  -        "budget_tokens": 10000
  +        "type": "adaptive"
       },
  +    "output_config": {
  +        "effort": "high"
  +    },
       "messages": [
           {
               "role": "user",
               "content": "Explain why the sum of two even numbers is always even."
           }
       ]
   }'
  ```

  ```diff CLI
   ant messages create <<'YAML'
  -model: claude-opus-4-6
  +model: claude-opus-4-8
   max_tokens: 16000
   thinking:
  -  type: enabled
  -  budget_tokens: 10000
  +  type: adaptive
  +output_config:
  +  effort: high
   messages:
     - role: user
       content: Explain why the sum of two even numbers is always even.
   YAML
  ```

  ```diff Python
   import anthropic

   client = anthropic.Anthropic()

   response = client.messages.create(
  -    model="claude-opus-4-6",
  +    model="claude-opus-4-8",
       max_tokens=16000,
  -    thinking={"type": "enabled", "budget_tokens": 10000},
  +    thinking={"type": "adaptive"},
  +    output_config={"effort": "high"},
       messages=[
           {
               "role": "user",
               "content": "Explain why the sum of two even numbers is always even.",
           }
       ],
   )
  ```

  ```diff TypeScript
   import Anthropic from "@anthropic-ai/sdk";

   const client = new Anthropic();

   const response = await client.messages.create({
  -  model: "claude-opus-4-6",
  +  model: "claude-opus-4-8",
     max_tokens: 16000,
  -  thinking: { type: "enabled", budget_tokens: 10000 },
  +  thinking: { type: "adaptive" },
  +  output_config: { effort: "high" },
     messages: [
       {
         role: "user",
         content: "Explain why the sum of two even numbers is always even."
       }
     ]
   });
  ```

  ```diff C#
   using Anthropic;
   using Anthropic.Models.Messages;

   AnthropicClient client = new();

   var parameters = new MessageCreateParams
   {
  -    Model = "claude-opus-4-6",
  +    Model = Model.ClaudeOpus4_8,
       MaxTokens = 16000,
  -    Thinking = new ThinkingConfigEnabled(budgetTokens: 10000),
  +    Thinking = new ThinkingConfigAdaptive(),
  +    OutputConfig = new OutputConfig { Effort = Effort.High },
       Messages = [new() { Role = Role.User, Content = "Explain why the sum of two even numbers is always even." }]
   };

   var response = await client.Messages.Create(parameters);
   Console.WriteLine(response);
  ```

  ```diff Go
   package main

   import (
   	"context"
   	"fmt"
   	"log"

   	"github.com/anthropics/anthropic-sdk-go"
   )

   func main() {
   	client := anthropic.NewClient()

   	response, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
  -		Model:     "claude-opus-4-6",
  +		Model:     anthropic.ModelClaudeOpus4_8,
   		MaxTokens: 16000,
  -		Thinking:  anthropic.ThinkingConfigParamOfEnabled(10000),
  +		Thinking: anthropic.ThinkingConfigParamUnion{
  +			OfAdaptive: &anthropic.ThinkingConfigAdaptiveParam{},
  +		},
  +		OutputConfig: anthropic.OutputConfigParam{
  +			Effort: anthropic.OutputConfigEffortHigh,
  +		},
   		Messages: []anthropic.MessageParam{
   			anthropic.NewUserMessage(anthropic.NewTextBlock("Explain why the sum of two even numbers is always even.")),
   		},
   	})
   	if err != nil {
   		log.Fatal(err)
   	}
   	fmt.Println(response)
   }
  ```

  ```diff Java
   import com.anthropic.client.AnthropicClient;
   import com.anthropic.client.okhttp.AnthropicOkHttpClient;
   import com.anthropic.models.messages.Message;
   import com.anthropic.models.messages.MessageCreateParams;
  +import com.anthropic.models.messages.Model;
  +import com.anthropic.models.messages.OutputConfig;
  +import com.anthropic.models.messages.ThinkingConfigAdaptive;

   void main() {
       AnthropicClient client = AnthropicOkHttpClient.fromEnv();

       MessageCreateParams params = MessageCreateParams.builder()
  -        .model("claude-opus-4-6")
  +        .model(Model.CLAUDE_OPUS_4_8)
           .maxTokens(16000L)
  -        .enabledThinking(10000L)
  +        .thinking(ThinkingConfigAdaptive.builder().build())
  +        .outputConfig(OutputConfig.builder()
  +            .effort(OutputConfig.Effort.HIGH)
  +            .build())
           .addUserMessage("Explain why the sum of two even numbers is always even.")
           .build();

       Message response = client.messages().create(params);
       IO.println(response);
   }
  ```

  ```diff PHP
   <?php

   use Anthropic\Client;

   $client = new Client();

   $response = $client->messages->create(
       maxTokens: 16000,
       messages: [['role' => 'user', 'content' => 'Explain why the sum of two even numbers is always even.']],
  -    model: 'claude-opus-4-6',
  -    thinking: ['type' => 'enabled', 'budget_tokens' => 10000],
  +    model: 'claude-opus-4-8',
  +    thinking: ['type' => 'adaptive'],
  +    outputConfig: ['effort' => 'high'],
   );
  ```

  ```diff Ruby
   require "anthropic"

   client = Anthropic::Client.new

   response = client.messages.create(
  -  model: "claude-opus-4-6",
  +  model: "claude-opus-4-8",
     max_tokens: 16000,
  -  thinking: { type: "enabled", budget_tokens: 10000 },
  +  thinking: { type: "adaptive" },
  +  output_config: { effort: "high" },
     messages: [
       { role: "user", content: "Explain why the sum of two even numbers is always even." }
     ]
   )
  ```
</CodeGroup>

## Capability improvements

### Improvement areas

Compared with Claude Opus 4.7, Claude Opus 4.8 targets behavioral improvements in:

* **Long-horizon agentic coding**, including better long-context handling, fewer compactions, and better [compaction](/docs/en/build-with-claude/compaction) recovery.
* **Reasoning effort calibration**, with more reliable behavior at each effort level across a range of domains.
* **Tool triggering**, with fewer cases of skipping a tool call that the task required.

### Adaptive thinking

With [adaptive thinking](/docs/en/build-with-claude/adaptive-thinking) enabled, Claude Opus 4.8 triggers reasoning only when it determines the turn needs it. On simple lookups and short agentic steps it responds directly. On complex multistep problems it reasons before answering. This reduces wasted thinking tokens on bimodal workloads compared to Claude Opus 4.7 at the same effort level. As on Claude Opus 4.7, thinking is off unless you explicitly set `thinking: {type: "adaptive"}` in your request.

## Behavior changes

These are not API breaking changes but might require prompt updates. See [Migrating to Claude Opus 4.8](/docs/en/about-claude/models/migration-guide#migrating-from-claude-opus-47) for full guidance.

* **Fewer wasted thinking tokens** at the same effort level when adaptive thinking is enabled, because the model determines per turn whether to think.
* **Better tool triggering.** The model is less likely to skip a tool call the task required, an issue some users reported on Claude Opus 4.7.
* **Better compaction handling and long-context quality.** Long agentic traces stay on task with fewer derailments after compaction.
* **Effort levels recalibrated.** The token allocation behind each effort level changes compared to Claude Opus 4.7: `medium` allows somewhat more thinking, `high` somewhat less, and `xhigh` substantially more. If you tuned an effort level against Claude Opus 4.7, re-baseline cost and latency at that level before adjusting it.

## Migration guide

For step-by-step migration instructions and the full migration checklist, see [Migrating to Claude Opus 4.8](/docs/en/about-claude/models/migration-guide#migrating-from-claude-opus-47). If you are upgrading from Claude Opus 4.6 or earlier, also apply [Migrating to Claude Opus 4.8 from Claude Opus 4.6](/docs/en/about-claude/models/migration-guide#migrating-from-claude-opus-46). Those steps cover breaking changes that the upgrade from Claude Opus 4.7 alone does not. If you use Claude Code or the Agent SDK, the [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill) can apply these migration steps to your code base automatically.

## Next steps

<CardGroup cols={3}>
  <Card title="Migration guide" icon="arrow-right" href="/docs/en/about-claude/models/migration-guide#migrating-from-claude-opus-47">
    Guide for migrating to the latest Claude models from previous Claude versions.
  </Card>

  <Card title="Effort" icon="gauge" href="/docs/en/build-with-claude/effort">
    Control how many tokens Claude uses when responding with the effort parameter, trading off between response thoroughness and token efficiency.
  </Card>

  <Card title="Adaptive thinking" icon="brain" href="/docs/en/build-with-claude/adaptive-thinking">
    Let Claude dynamically determine when and how much to use extended thinking with adaptive thinking mode.
  </Card>

  <Card title="Prompt caching" icon="database" href="/docs/en/build-with-claude/prompt-caching">
    How mid-conversation system messages preserve cache hits.
  </Card>

  <Card title="Stop reasons and fallback" icon="code" href="/docs/en/build-with-claude/handling-stop-reasons">
    Learn what each stop\_reason value means and how to handle truncation, tool use, paused turns, and refusals in your application.
  </Card>

  <Card title="Fast mode (research preview)" icon="bolt" href="/docs/en/build-with-claude/fast-mode">
    Get up to 2.5x higher output tokens per second from Claude Opus models.
  </Card>
</CardGroup>
