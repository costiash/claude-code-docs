# Compaction

Server-side context compaction for managing long conversations that approach context window limits.

---

<Tip>
Server-side compaction is the recommended strategy for managing context in long-running conversations and agentic workflows. It handles context management automatically with minimal integration work.
</Tip>

Compaction extends the effective context length for long-running conversations and tasks by automatically summarizing older context when approaching the context window limit. This isn't just about staying under a token cap. As conversations get longer, models struggle to maintain focus across the full history. Compaction keeps the active context focused and performant by replacing stale content with concise summaries.

<Tip>
For a deeper look at why long contexts degrade and how compaction helps, see
[Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
</Tip>

This is ideal for:

- Chat-based, multi-turn conversations where you want users to use one chat for a long period of time
- Task-oriented prompts that require a lot of follow-up work (often tool use) that may exceed the context window

<Note>
Compaction is in beta. Include the [beta header](/docs/en/api/beta-headers) `compact-2026-01-12` in your API requests to use this feature.
</Note>

<Note>
Compaction is eligible for [Zero Data Retention (ZDR)](/docs/en/build-with-claude/zero-data-retention) arrangements.
</Note>

## Supported models

Compaction is supported on the following models:

- Claude Opus 4.6 (`claude-opus-4-6`)
- Claude Sonnet 4.6 (`claude-sonnet-4-6`)

## How compaction works

When compaction is enabled, Claude automatically summarizes your conversation when it approaches the configured token threshold. The API:

1. Detects when input tokens exceed your specified trigger threshold.
2. Generates a summary of the current conversation.
3. Creates a `compaction` block containing the summary.
4. Continues the response with the compacted context.

On subsequent requests, append the response to your messages. The API automatically drops all message blocks prior to the `compaction` block, continuing the conversation from the summary.

![Flow diagram showing the compaction process: when input tokens exceed the trigger threshold, Claude generates a summary in a compaction block and continues the response with the compacted context](/docs/images/compaction-flow.svg)

## Basic usage

Enable compaction by adding the `compact_20260112` strategy to `context_management.edits` in your Messages API request.

<CodeGroup>
```bash Shell
curl https://api.anthropic.com/v1/messages \
     --header "x-api-key: $ANTHROPIC_API_KEY" \
     --header "anthropic-version: 2023-06-01" \
     --header "anthropic-beta: compact-2026-01-12" \
     --header "content-type: application/json" \
     --data \
'{
    "model": "claude-opus-4-6",
    "max_tokens": 4096,
    "messages": [
        {
            "role": "user",
            "content": "Help me build a website"
        }
    ],
    "context_management": {
        "edits": [
            {
                "type": "compact_20260112"
            }
        ]
    }
}'
```

```python Python
import anthropic

client = anthropic.Anthropic()

messages = [{"role": "user", "content": "Help me build a website"}]

response = client.beta.messages.create(
    betas=["compact-2026-01-12"],
    model="claude-opus-4-6",
    max_tokens=4096,
    messages=messages,
    context_management={"edits": [{"type": "compact_20260112"}]},
)

# Append the response (including any compaction block) to continue the conversation
messages.append({"role": "assistant", "content": response.content})
```

```typescript TypeScript hidelines={1..4}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const messages: Anthropic.Beta.Messages.BetaMessageParam[] = [
  { role: "user", content: "Help me build a website" }
];

const response = await client.beta.messages.create({
  betas: ["compact-2026-01-12"],
  model: "claude-opus-4-6",
  max_tokens: 4096,
  messages,
  context_management: {
    edits: [
      {
        type: "compact_20260112"
      }
    ]
  }
} as unknown as Anthropic.Beta.Messages.MessageCreateParamsNonStreaming);

// Append the response (including any compaction block) to continue the conversation
messages.push({
  role: "assistant",
  content: response.content as unknown as Anthropic.Beta.Messages.BetaContentBlockParam[]
});
```

```csharp C# nocheck
using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Beta.Messages;

class Program
{
    static async Task Main(string[] args)
    {
        AnthropicClient client = new();

        var messages = new List<BetaMessageParam>
        {
            new() { Role = Role.User, Content = "Help me build a website" }
        };

        var parameters = new MessageCreateParams
        {
            Betas = new[] { "compact-2026-01-12" },
            Model = "claude-opus-4-6",
            MaxTokens = 4096,
            Messages = messages,
            ContextManagement = new BetaContextManagementConfig
            {
                Edits = [new BetaCompact20260112Edit()]
            }
        };

        var response = await client.Beta.Messages.Create(parameters);

        // Append the response (including any compaction block) to continue the conversation
        messages.Add(new BetaMessageParam { Role = Role.Assistant, Content = response.Content });

        Console.WriteLine(response);
    }
}
```
```go Go hidelines={1..13,-3..-1}
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	messages := []anthropic.BetaMessageParam{
		anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Help me build a website")),
	}

	response, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
		Model:     anthropic.ModelClaudeOpus4_6,
		MaxTokens: 4096,
		Messages:  messages,
		ContextManagement: anthropic.BetaContextManagementConfigParam{
			Edits: []anthropic.BetaContextManagementConfigEditUnionParam{
				{OfCompact20260112: &anthropic.BetaCompact20260112EditParam{}},
			},
		},
		Betas: []anthropic.AnthropicBeta{"compact-2026-01-12"},
	})
	if err != nil {
		log.Fatal(err)
	}

	// Append the response (including any compaction block) to continue the conversation
	messages = append(messages, response.ToParam())

	fmt.Println(response)
}
```

```java Java nocheck hidelines={1..9,-1}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.beta.messages.BetaMessage;
import com.anthropic.models.beta.messages.BetaContextManagementConfig;
import com.anthropic.models.beta.messages.BetaCompact20260112Edit;

public class CompactionExample {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCreateParams params = MessageCreateParams.builder()
            .addBeta("compact-2026-01-12")
            .model("claude-opus-4-6")
            .maxTokens(4096L)
            .addUserMessage("Help me build a website")
            .contextManagement(BetaContextManagementConfig.builder()
                .addEdit(BetaCompact20260112Edit.builder().build())
                .build())
            .build();

        BetaMessage response = client.beta().messages().create(params);

        // Append the response (including any compaction block) to continue the conversation
        // by including it in the next request's messages
        System.out.println(response);
    }
}
```

```php PHP
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$messages = [
    ['role' => 'user', 'content' => 'Help me build a website']
];

$response = $client->beta->messages->create(
    maxTokens: 4096,
    messages: $messages,
    model: 'claude-opus-4-6',
    betas: ['compact-2026-01-12'],
    contextManagement: [
        'edits' => [
            ['type' => 'compact_20260112']
        ]
    ]
);

// Append the response (including any compaction block) to continue the conversation
$messages[] = ['role' => 'assistant', 'content' => $response->content];

echo $response->content[0]->text;
```

```ruby Ruby
require "anthropic"

client = Anthropic::Client.new

messages = [
  { role: "user", content: "Help me build a website" }
]

response = client.beta.messages.create(
  betas: ["compact-2026-01-12"],
  model: "claude-opus-4-6",
  max_tokens: 4096,
  messages: messages,
  context_management: {
    edits: [{ type: "compact_20260112" }]
  }
)

# Append the response (including any compaction block) to continue the conversation
messages << { role: "assistant", content: response.content }

puts response
```
</CodeGroup>

## Parameters

| Parameter | Type | Default | Description |
|:----------|:-----|:--------|:------------|
| `type` | string | Required | Must be `"compact_20260112"` |
| `trigger` | object | 150,000 tokens | When to trigger compaction. Must be at least 50,000 tokens. |
| `pause_after_compaction` | boolean | `false` | Whether to pause after generating the compaction summary |
| `instructions` | string | `null` | Custom summarization prompt. Completely replaces the default prompt when provided. |

### Trigger configuration

Configure when compaction triggers using the `trigger` parameter:

<CodeGroup>
```python Python hidelines={1..4}
import anthropic

client = anthropic.Anthropic()
messages = [{"role": "user", "content": "Hello, Claude"}]
response = client.beta.messages.create(
    betas=["compact-2026-01-12"],
    model="claude-opus-4-6",
    max_tokens=4096,
    messages=messages,
    context_management={
        "edits": [
            {
                "type": "compact_20260112",
                "trigger": {"type": "input_tokens", "value": 150000},
            }
        ]
    },
)
```

```typescript TypeScript hidelines={1..3}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();
const messages: Anthropic.Beta.Messages.BetaMessageParam[] = [];

const response = await client.beta.messages.create({
  betas: ["compact-2026-01-12"],
  model: "claude-opus-4-6",
  max_tokens: 4096,
  messages,
  context_management: {
    edits: [
      {
        type: "compact_20260112",
        trigger: {
          type: "input_tokens",
          value: 150000
        }
      }
    ]
  }
} as unknown as Anthropic.Beta.Messages.MessageCreateParamsNonStreaming);
```

```csharp C# nocheck
using System;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Beta.Messages;

class Program
{
    static async Task Main(string[] args)
    {
        AnthropicClient client = new();

        var parameters = new MessageCreateParams
        {
            Model = "claude-opus-4-6",
            MaxTokens = 4096,
            Betas = new[] { "compact-2026-01-12" },
            Messages = messages,
            ContextManagement = new BetaContextManagementConfig
            {
                Edits = [new BetaCompact20260112Edit
                {
                    Trigger = new BetaInputTokensTrigger(150000)
                }]
            }
        };

        var message = await client.Beta.Messages.Create(parameters);
        Console.WriteLine(message);
    }
}
```
```go Go hidelines={1..14,-5..-1}
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()
	messages := []anthropic.BetaMessageParam{anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Hello, Claude"))}

	response, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
		Model:     anthropic.ModelClaudeOpus4_6,
		MaxTokens: 4096,
		Messages:  messages,
		ContextManagement: anthropic.BetaContextManagementConfigParam{
			Edits: []anthropic.BetaContextManagementConfigEditUnionParam{
				{OfCompact20260112: &anthropic.BetaCompact20260112EditParam{
					Trigger: anthropic.BetaInputTokensTriggerParam{Value: 150000},
				}},
			},
		},
		Betas: []anthropic.AnthropicBeta{"compact-2026-01-12"},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(response)
}
```

```java Java nocheck hidelines={1..11,-1}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.beta.messages.BetaMessage;
import com.anthropic.models.beta.messages.BetaContextManagementConfig;
import com.anthropic.models.beta.messages.BetaCompact20260112Edit;
import com.anthropic.models.beta.messages.BetaInputTokensTrigger;

public class CompactionExample {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCreateParams params = MessageCreateParams.builder()
            .model("claude-opus-4-6")
            .maxTokens(4096L)
            .addBeta("compact-2026-01-12")
            .addUserMessage("Hello, Claude")
            .contextManagement(BetaContextManagementConfig.builder()
                .addEdit(BetaCompact20260112Edit.builder()
                    .trigger(BetaInputTokensTrigger.builder()
                        .value(150000L)
                        .build())
                    .build())
                .build())
            .build();

        BetaMessage response = client.beta().messages().create(params);
        System.out.println(response);
    }
}
```

```php PHP hidelines={1..5}
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));
$messages = [['role' => 'user', 'content' => 'Hello, Claude']];

$message = $client->beta->messages->create(
    maxTokens: 4096,
    messages: $messages,
    model: 'claude-opus-4-6',
    betas: ['compact-2026-01-12'],
    contextManagement: [
        'edits' => [
            [
                'type' => 'compact_20260112',
                'trigger' => [
                    'type' => 'input_tokens',
                    'value' => 150000
                ]
            ]
        ]
    ]
);

echo $message;
```

```ruby Ruby hidelines={4}
require "anthropic"

client = Anthropic::Client.new
messages = [{ role: "user", content: "Hello, Claude" }]

response = client.beta.messages.create(
  betas: ["compact-2026-01-12"],
  model: "claude-opus-4-6",
  max_tokens: 4096,
  messages: messages,
  context_management: {
    edits: [
      {
        type: "compact_20260112",
        trigger: {
          type: "input_tokens",
          value: 150000
        }
      }
    ]
  }
)
puts response
```
</CodeGroup>

### Custom summarization instructions

By default, compaction uses the following summarization prompt:

```text
You have written a partial transcript for the initial task above. Please write a summary of the transcript. The purpose of this summary is to provide continuity so you can continue to make progress towards solving the task in a future context, where the raw history above may not be accessible and will be replaced with this summary. Write down anything that would be helpful, including the state, next steps, learnings etc. You must wrap your summary in a <summary></summary> block.
```

You can provide custom instructions via the `instructions` parameter to replace this prompt entirely. Custom instructions don't supplement the default; they completely replace it:

<CodeGroup>
```python Python hidelines={1..4}
import anthropic

client = anthropic.Anthropic()
messages = [{"role": "user", "content": "Hello, Claude"}]
response = client.beta.messages.create(
    betas=["compact-2026-01-12"],
    model="claude-opus-4-6",
    max_tokens=4096,
    messages=messages,
    context_management={
        "edits": [
            {
                "type": "compact_20260112",
                "instructions": "Focus on preserving code snippets, variable names, and technical decisions.",
            }
        ]
    },
)
```

```typescript TypeScript nocheck hidelines={1..3}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();
const messages: Anthropic.Beta.Messages.BetaMessageParam[] = [];

const response = await client.beta.messages.create({
  betas: ["compact-2026-01-12"],
  model: "claude-opus-4-6",
  max_tokens: 4096,
  messages,
  context_management: {
    edits: [
      {
        type: "compact_20260112",
        instructions:
          "Focus on preserving code snippets, variable names, and technical decisions."
      }
    ]
  }
} as unknown as Anthropic.Beta.Messages.MessageCreateParamsNonStreaming);
```

```csharp C# nocheck
using System;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Beta.Messages;

class Program
{
    static async Task Main(string[] args)
    {
        AnthropicClient client = new();

        var parameters = new MessageCreateParams
        {
            Betas = new[] { "compact-2026-01-12" },
            Model = "claude-opus-4-6",
            MaxTokens = 4096,
            Messages = new[]
            {
                new BetaMessageParam { Role = Role.User, Content = "Help me build a Python web scraper" },
                new BetaMessageParam { Role = Role.Assistant, Content = "I'll help you build a web scraper..." },
                new BetaMessageParam { Role = Role.User, Content = "Add support for JavaScript-rendered pages" }
            },
            ContextManagement = new BetaContextManagementConfig
            {
                Edits = [new BetaCompact20260112Edit
                {
                    Instructions = "Focus on preserving code snippets, variable names, and technical decisions."
                }]
            }
        };

        var message = await client.Beta.Messages.Create(parameters);
        Console.WriteLine(message);
    }
}
```
```go Go hidelines={1..13,-5..-1}
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
		Model:     anthropic.ModelClaudeOpus4_6,
		MaxTokens: 4096,
		Messages: []anthropic.BetaMessageParam{
			anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Help me build a Python web scraper")),
			{Role: anthropic.BetaMessageParamRoleAssistant, Content: []anthropic.BetaContentBlockParamUnion{anthropic.NewBetaTextBlock("I'll help you build a web scraper...")}},
			anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Add support for JavaScript-rendered pages")),
		},
		ContextManagement: anthropic.BetaContextManagementConfigParam{
			Edits: []anthropic.BetaContextManagementConfigEditUnionParam{
				{OfCompact20260112: &anthropic.BetaCompact20260112EditParam{
					Instructions: anthropic.String("Focus on preserving code snippets, variable names, and technical decisions."),
				}},
			},
		},
		Betas: []anthropic.AnthropicBeta{"compact-2026-01-12"},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(response)
}
```

```java Java nocheck hidelines={1..11,-1}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.beta.messages.BetaMessage;
import com.anthropic.models.beta.messages.BetaContextManagementConfig;
import com.anthropic.models.beta.messages.BetaCompact20260112Edit;

public class CompactionExample {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCreateParams params = MessageCreateParams.builder()
            .addBeta("compact-2026-01-12")
            .model("claude-opus-4-6")
            .maxTokens(4096L)
            .addUserMessage("Help me build a Python web scraper")
            .addAssistantMessage("I'll help you build a web scraper...")
            .addUserMessage("Add support for JavaScript-rendered pages")
            .contextManagement(BetaContextManagementConfig.builder()
                .addEdit(BetaCompact20260112Edit.builder()
                    .instructions("Focus on preserving code snippets, variable names, and technical decisions.")
                    .build())
                .build())
            .build();

        BetaMessage response = client.beta().messages().create(params);
        System.out.println(response);
    }
}
```

```php PHP hidelines={1..5}
<?php
use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$response = $client->beta->messages->create(
    maxTokens: 4096,
    messages: [
        ['role' => 'user', 'content' => 'Help me build a Python web scraper'],
        ['role' => 'assistant', 'content' => "I'll help you build a web scraper..."],
        ['role' => 'user', 'content' => 'Add support for JavaScript-rendered pages']
    ],
    model: 'claude-opus-4-6',
    betas: ['compact-2026-01-12'],
    contextManagement: [
        'edits' => [
            [
                'type' => 'compact_20260112',
                'instructions' => 'Focus on preserving code snippets, variable names, and technical decisions.'
            ]
        ]
    ]
);

echo $response->content[0]->text;
```

```ruby Ruby
require "anthropic"

client = Anthropic::Client.new

response = client.beta.messages.create(
  betas: ["compact-2026-01-12"],
  model: "claude-opus-4-6",
  max_tokens: 4096,
  messages: [
    { role: "user", content: "Help me build a Python web scraper" },
    { role: "assistant", content: "I'll help you build a web scraper..." },
    { role: "user", content: "Add support for JavaScript-rendered pages" }
  ],
  context_management: {
    edits: [
      {
        type: "compact_20260112",
        instructions:
          "Focus on preserving code snippets, variable names, and technical decisions."
      }
    ]
  }
)

puts response
```
</CodeGroup>

### Pausing after compaction

Use `pause_after_compaction` to pause the API after generating the compaction summary. This allows you to add additional content blocks (such as preserving recent messages or specific instruction-oriented messages) before the API continues with the response.

When enabled, the API returns a message with the `compaction` stop reason after generating the compaction block:

<CodeGroup>
```python Python hidelines={1..4}
import anthropic

client = anthropic.Anthropic()
messages = [{"role": "user", "content": "Hello, Claude"}]
response = client.beta.messages.create(
    betas=["compact-2026-01-12"],
    model="claude-opus-4-6",
    max_tokens=4096,
    messages=messages,
    context_management={
        "edits": [{"type": "compact_20260112", "pause_after_compaction": True}]
    },
)

# Check if compaction triggered a pause
if response.stop_reason == "compaction":
    # Response contains only the compaction block
    messages.append({"role": "assistant", "content": response.content})

    # Continue the request
    response = client.beta.messages.create(
        betas=["compact-2026-01-12"],
        model="claude-opus-4-6",
        max_tokens=4096,
        messages=messages,
        context_management={"edits": [{"type": "compact_20260112"}]},
    )
```

```typescript TypeScript hidelines={1..3}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();
const messages: Anthropic.Beta.Messages.BetaMessageParam[] = [];

let response = await client.beta.messages.create({
  betas: ["compact-2026-01-12"],
  model: "claude-opus-4-6",
  max_tokens: 4096,
  messages,
  context_management: {
    edits: [
      {
        type: "compact_20260112",
        pause_after_compaction: true
      }
    ]
  }
} as unknown as Anthropic.Beta.Messages.MessageCreateParamsNonStreaming);

// Check if compaction triggered a pause
if ((response.stop_reason as string) === "compaction") {
  // Response contains only the compaction block
  messages.push({
    role: "assistant",
    content: response.content as unknown as Anthropic.Beta.Messages.BetaContentBlockParam[]
  });

  // Continue the request
  response = await client.beta.messages.create({
    betas: ["compact-2026-01-12"],
    model: "claude-opus-4-6",
    max_tokens: 4096,
    messages,
    context_management: {
      edits: [{ type: "compact_20260112" }]
    }
  } as unknown as Anthropic.Beta.Messages.MessageCreateParamsNonStreaming);
}
```

```csharp C# nocheck
using Anthropic;
using Anthropic.Models.Beta.Messages;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        var client = new AnthropicClient();
        var messages = new List<BetaMessageParam>();

        var parameters = new MessageCreateParams
        {
            Model = "claude-opus-4-6",
            MaxTokens = 4096,
            Betas = new[] { "compact-2026-01-12" },
            Messages = messages,
            ContextManagement = new BetaContextManagementConfig
            {
                Edits = [new BetaCompact20260112Edit
                {
                    PauseAfterCompaction = true
                }]
            }
        };

        var response = await client.Beta.Messages.Create(parameters);

        if (response.StopReason == "compaction")
        {
            messages.Add(new BetaMessageParam
            {
                Role = Role.Assistant,
                Content = response.Content
            });

            parameters = new MessageCreateParams
            {
                Model = "claude-opus-4-6",
                MaxTokens = 4096,
                Betas = new[] { "compact-2026-01-12" },
                Messages = messages,
                ContextManagement = new BetaContextManagementConfig
                {
                    Edits = [new BetaCompact20260112Edit()]
                }
            };

            response = await client.Beta.Messages.Create(parameters);
        }

        Console.WriteLine(response);
    }
}
```
```go Go hidelines={1..12,-3..-1}
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()
	messages := []anthropic.BetaMessageParam{anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Hello, Claude"))}

	compactEdit := anthropic.BetaContextManagementConfigParam{
		Edits: []anthropic.BetaContextManagementConfigEditUnionParam{
			{OfCompact20260112: &anthropic.BetaCompact20260112EditParam{
				PauseAfterCompaction: anthropic.Bool(true),
			}},
		},
	}

	response, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
		Model:             anthropic.ModelClaudeOpus4_6,
		MaxTokens:         4096,
		Messages:          messages,
		ContextManagement: compactEdit,
		Betas:             []anthropic.AnthropicBeta{"compact-2026-01-12"},
	})
	if err != nil {
		log.Fatal(err)
	}

	if response.StopReason == "compaction" {
		messages = append(messages, response.ToParam())

		response, err = client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
			Model:     anthropic.ModelClaudeOpus4_6,
			MaxTokens: 4096,
			Messages:  messages,
			ContextManagement: anthropic.BetaContextManagementConfigParam{
				Edits: []anthropic.BetaContextManagementConfigEditUnionParam{
					{OfCompact20260112: &anthropic.BetaCompact20260112EditParam{}},
				},
			},
			Betas: []anthropic.AnthropicBeta{"compact-2026-01-12"},
		})
		if err != nil {
			log.Fatal(err)
		}
	}

	fmt.Println(response)
}
```

```java Java nocheck hidelines={1..12,-1}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.beta.messages.BetaMessage;
import com.anthropic.models.beta.messages.BetaContextManagementConfig;
import com.anthropic.models.beta.messages.BetaCompact20260112Edit;
import com.anthropic.models.beta.messages.BetaStopReason;

public class CompactionPauseExample {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCreateParams params = MessageCreateParams.builder()
            .model("claude-opus-4-6")
            .maxTokens(4096L)
            .addBeta("compact-2026-01-12")
            .addUserMessage("Help me build a website")
            .contextManagement(BetaContextManagementConfig.builder()
                .addEdit(BetaCompact20260112Edit.builder()
                    .pauseAfterCompaction(true)
                    .build())
                .build())
            .build();

        BetaMessage response = client.beta().messages().create(params);

        // Check if compaction triggered a pause
        if (response.stopReason().isPresent()
                && response.stopReason().get().equals(BetaStopReason.COMPACTION)) {
            // Append the compaction block and continue the request
            // by building a new request with the compacted context
            MessageCreateParams continueParams = MessageCreateParams.builder()
                .model("claude-opus-4-6")
                .maxTokens(4096L)
                .addBeta("compact-2026-01-12")
                .addUserMessage("Help me build a website")
                .addMessage(response)
                .contextManagement(BetaContextManagementConfig.builder()
                    .addEdit(BetaCompact20260112Edit.builder().build())
                    .build())
                .build();

            response = client.beta().messages().create(continueParams);
        }

        System.out.println(response);
    }
}
```

```php PHP hidelines={1..5}
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));
$messages = [];

$response = $client->beta->messages->create(
    maxTokens: 4096,
    messages: $messages,
    model: 'claude-opus-4-6',
    betas: ['compact-2026-01-12'],
    contextManagement: [
        'edits' => [
            [
                'type' => 'compact_20260112',
                'pause_after_compaction' => true
            ]
        ]
    ]
);

if ($response->stopReason === 'compaction') {
    $messages[] = [
        'role' => 'assistant',
        'content' => $response->content
    ];

    $response = $client->beta->messages->create(
        maxTokens: 4096,
        messages: $messages,
        model: 'claude-opus-4-6',
        betas: ['compact-2026-01-12'],
        contextManagement: [
            'edits' => [
                ['type' => 'compact_20260112']
            ]
        ]
    );
}

echo $response;
```

```ruby Ruby
require "anthropic"

client = Anthropic::Client.new
messages = []

response = client.beta.messages.create(
  betas: ["compact-2026-01-12"],
  model: "claude-opus-4-6",
  max_tokens: 4096,
  messages: messages,
  context_management: {
    edits: [
      {
        type: "compact_20260112",
        pause_after_compaction: true
      }
    ]
  }
)

if response.stop_reason == :compaction
  messages << { role: "assistant", content: response.content }

  response = client.beta.messages.create(
    betas: ["compact-2026-01-12"],
    model: "claude-opus-4-6",
    max_tokens: 4096,
    messages: messages,
    context_management: {
      edits: [{ type: "compact_20260112" }]
    }
  )
end

puts response
```
</CodeGroup>

#### Enforcing a total token budget

When a model works on long tasks with many tool-use iterations, total token consumption can grow significantly. You can combine `pause_after_compaction` with a compaction counter to estimate cumulative usage and gracefully wrap up the task once a budget is reached:

```python Python hidelines={1..4}
import anthropic

client = anthropic.Anthropic()
messages = [{"role": "user", "content": "Hello, Claude"}]
TRIGGER_THRESHOLD = 100_000
TOTAL_TOKEN_BUDGET = 3_000_000
n_compactions = 0

response = client.beta.messages.create(
    betas=["compact-2026-01-12"],
    model="claude-opus-4-6",
    max_tokens=4096,
    messages=messages,
    context_management={
        "edits": [
            {
                "type": "compact_20260112",
                "trigger": {"type": "input_tokens", "value": TRIGGER_THRESHOLD},
                "pause_after_compaction": True,
            }
        ]
    },
)

if response.stop_reason == "compaction":
    n_compactions += 1
    messages.append({"role": "assistant", "content": response.content})

    # Estimate total tokens consumed; prompt wrap-up if over budget
    if n_compactions * TRIGGER_THRESHOLD >= TOTAL_TOKEN_BUDGET:
        messages.append(
            {
                "role": "user",
                "content": "Please wrap up your current work and summarize the final state.",
            }
        )
```

## Working with compaction blocks

When compaction is triggered, the API returns a `compaction` block at the start of the assistant response.

A long-running conversation may result in multiple compactions. The last compaction block reflects the final state of the prompt, replacing content prior to it with the generated summary.

```json
{
  "content": [
    {
      "type": "compaction",
      "content": "Summary of the conversation: The user requested help building a web scraper..."
    },
    {
      "type": "text",
      "text": "Based on our conversation so far..."
    }
  ]
}
```

### Passing compaction blocks back

You must pass the `compaction` block back to the API on subsequent requests to continue the conversation with the shortened prompt. The simplest approach is to append the entire response content to your messages:

<CodeGroup>
```python Python hidelines={1..4}
import anthropic

client = anthropic.Anthropic()
messages = [{"role": "user", "content": "Hello, Claude"}]
response = client.beta.messages.create(
    betas=["compact-2026-01-12"],
    model="claude-opus-4-6",
    max_tokens=4096,
    messages=messages,
    context_management={"edits": [{"type": "compact_20260112"}]},
)
# After receiving a response with a compaction block
messages.append({"role": "assistant", "content": response.content})

# Continue the conversation
messages.append({"role": "user", "content": "Now add error handling"})

response = client.beta.messages.create(
    betas=["compact-2026-01-12"],
    model="claude-opus-4-6",
    max_tokens=4096,
    messages=messages,
    context_management={"edits": [{"type": "compact_20260112"}]},
)
```

```typescript TypeScript hidelines={1..3}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();
const messages: Anthropic.Beta.Messages.BetaMessageParam[] = [];

// Assume we already have a response from a previous request
const response = await client.beta.messages.create({
  betas: ["compact-2026-01-12"],
  model: "claude-opus-4-6",
  max_tokens: 4096,
  messages,
  context_management: {
    edits: [{ type: "compact_20260112" }]
  }
} as unknown as Anthropic.Beta.Messages.MessageCreateParamsNonStreaming);

// After receiving a response with a compaction block
messages.push({
  role: "assistant",
  content: response.content as unknown as Anthropic.Beta.Messages.BetaContentBlockParam[]
});

// Continue the conversation
messages.push({ role: "user", content: "Now add error handling" });

const nextResponse = await client.beta.messages.create({
  betas: ["compact-2026-01-12"],
  model: "claude-opus-4-6",
  max_tokens: 4096,
  messages,
  context_management: {
    edits: [{ type: "compact_20260112" }]
  }
} as unknown as Anthropic.Beta.Messages.MessageCreateParamsNonStreaming);
```

```csharp C# nocheck
using Anthropic;
using Anthropic.Models.Beta.Messages;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        AnthropicClient client = new();

        var messages = new List<BetaMessageParam>
        {
            new() { Role = Role.User, Content = "Help me build a web scraper" }
        };

        var response = await client.Beta.Messages.Create(new MessageCreateParams
        {
            Betas = ["compact-2026-01-12"],
            Model = "claude-opus-4-6",
            MaxTokens = 4096,
            Messages = messages,
            ContextManagement = new BetaContextManagementConfig
            {
                Edits = [new BetaCompact20260112Edit()]
            }
        });

        messages.Add(new BetaMessageParam { Role = Role.Assistant, Content = response.Content });

        messages.Add(new BetaMessageParam { Role = Role.User, Content = "Now add error handling" });

        var nextResponse = await client.Beta.Messages.Create(new MessageCreateParams
        {
            Betas = ["compact-2026-01-12"],
            Model = "claude-opus-4-6",
            MaxTokens = 4096,
            Messages = messages,
            ContextManagement = new BetaContextManagementConfig
            {
                Edits = [new BetaCompact20260112Edit()]
            }
        });

        Console.WriteLine(nextResponse);
    }
}
```
```go Go hidelines={1..13,-6..-1}
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	messages := []anthropic.BetaMessageParam{
		anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Help me build a web scraper")),
	}

	compactEdit := anthropic.BetaContextManagementConfigParam{
		Edits: []anthropic.BetaContextManagementConfigEditUnionParam{
			{OfCompact20260112: &anthropic.BetaCompact20260112EditParam{}},
		},
	}

	response, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
		Model:             anthropic.ModelClaudeOpus4_6,
		MaxTokens:         4096,
		Messages:          messages,
		ContextManagement: compactEdit,
		Betas:             []anthropic.AnthropicBeta{"compact-2026-01-12"},
	})
	if err != nil {
		log.Fatal(err)
	}

	messages = append(messages, response.ToParam())

	messages = append(messages, anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Now add error handling")))

	nextResponse, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
		Model:             anthropic.ModelClaudeOpus4_6,
		MaxTokens:         4096,
		Messages:          messages,
		ContextManagement: compactEdit,
		Betas:             []anthropic.AnthropicBeta{"compact-2026-01-12"},
	})
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(nextResponse)
}
```

```java Java nocheck
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.beta.messages.BetaMessage;
import com.anthropic.models.beta.messages.BetaContextManagementConfig;
import com.anthropic.models.beta.messages.BetaCompact20260112Edit;

public class CompactionExample {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        // First request
        BetaMessage response = client.beta().messages().create(
            MessageCreateParams.builder()
                .addBeta("compact-2026-01-12")
                .model("claude-opus-4-6")
                .maxTokens(4096L)
                .addUserMessage("Help me build a web scraper")
                .contextManagement(BetaContextManagementConfig.builder()
                    .addEdit(BetaCompact20260112Edit.builder().build())
                    .build())
                .build());

        // After receiving a response with a compaction block, append the full
        // content (including compaction blocks) and continue the conversation
        BetaMessage nextResponse = client.beta().messages().create(
            MessageCreateParams.builder()
                .addBeta("compact-2026-01-12")
                .model("claude-opus-4-6")
                .maxTokens(4096L)
                .addUserMessage("Help me build a web scraper")
                .addMessage(response)
                .addUserMessage("Now add error handling")
                .contextManagement(BetaContextManagementConfig.builder()
                    .addEdit(BetaCompact20260112Edit.builder().build())
                    .build())
                .build());

        System.out.println(nextResponse);
    }
}
```

```php PHP hidelines={1..6}
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$messages = [
    ['role' => 'user', 'content' => 'Help me build a web scraper']
];

$response = $client->beta->messages->create(
    maxTokens: 4096,
    messages: $messages,
    model: 'claude-opus-4-6',
    betas: ['compact-2026-01-12'],
    contextManagement: [
        'edits' => [['type' => 'compact_20260112']]
    ]
);

$messages[] = ['role' => 'assistant', 'content' => $response->content];

$messages[] = ['role' => 'user', 'content' => 'Now add error handling'];

$nextResponse = $client->beta->messages->create(
    maxTokens: 4096,
    messages: $messages,
    model: 'claude-opus-4-6',
    betas: ['compact-2026-01-12'],
    contextManagement: [
        'edits' => [['type' => 'compact_20260112']]
    ]
);

echo $nextResponse->content[0]->text;
```

```ruby Ruby
require "anthropic"

client = Anthropic::Client.new

messages = [
  { role: "user", content: "Help me build a web scraper" }
]

response = client.beta.messages.create(
  betas: ["compact-2026-01-12"],
  model: "claude-opus-4-6",
  max_tokens: 4096,
  messages: messages,
  context_management: {
    edits: [{ type: "compact_20260112" }]
  }
)

messages << { role: "assistant", content: response.content }

messages << { role: "user", content: "Now add error handling" }

next_response = client.beta.messages.create(
  betas: ["compact-2026-01-12"],
  model: "claude-opus-4-6",
  max_tokens: 4096,
  messages: messages,
  context_management: {
    edits: [{ type: "compact_20260112" }]
  }
)

puts next_response.content
```
</CodeGroup>

When the API receives a `compaction` block, all content blocks before it are ignored. You can either:

- Keep the original messages in your list and let the API handle removing the compacted content
- Manually drop the compacted messages and only include the compaction block onwards

### Streaming

When streaming responses with compaction enabled, you'll receive a `content_block_start` event when compaction begins. The compaction block streams differently from text blocks. You'll receive a `content_block_start` event, followed by a single `content_block_delta` with the complete summary content (no intermediate streaming), and then a `content_block_stop` event.

<CodeGroup>
```python Python hidelines={1..4}
import anthropic

client = anthropic.Anthropic()
messages = [{"role": "user", "content": "Hello, Claude"}]

with client.beta.messages.stream(
    betas=["compact-2026-01-12"],
    model="claude-opus-4-6",
    max_tokens=4096,
    messages=messages,
    context_management={"edits": [{"type": "compact_20260112"}]},
) as stream:
    for event in stream:
        if event.type == "content_block_start":
            if event.content_block.type == "compaction":
                print("Compaction started...")
            elif event.content_block.type == "text":
                print("Text response started...")

        elif event.type == "content_block_delta":
            if event.delta.type == "compaction_delta":
                print(f"Compaction complete: {len(event.delta.content)} chars")
            elif event.delta.type == "text_delta":
                print(event.delta.text, end="", flush=True)

    # Get the final accumulated message
    message = stream.get_final_message()
    messages.append({"role": "assistant", "content": message.content})
```

```typescript TypeScript nocheck hidelines={1..3}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();
const messages: Anthropic.Beta.Messages.BetaMessageParam[] = [];

const stream = await client.beta.messages.stream({
  betas: ["compact-2026-01-12"],
  model: "claude-opus-4-6",
  max_tokens: 4096,
  messages,
  context_management: {
    edits: [{ type: "compact_20260112" }]
  }
} as unknown as Anthropic.Beta.Messages.BetaMessageStreamParams);

for await (const event of stream) {
  if (event.type === "content_block_start") {
    if ((event.content_block as { type: string }).type === "compaction") {
      console.log("Compaction started...");
    } else if (event.content_block.type === "text") {
      console.log("Text response started...");
    }
  } else if (event.type === "content_block_delta") {
    if ((event.delta as { type: string }).type === "compaction_delta") {
      console.log(
        `Compaction complete: ${(event.delta as unknown as { content: string }).content.length} chars`
      );
    } else if (event.delta.type === "text_delta") {
      process.stdout.write(event.delta.text);
    }
  }
}

// Get the final accumulated message
const message = await stream.finalMessage();
messages.push({
  role: "assistant",
  content: message.content as unknown as Anthropic.Beta.Messages.BetaContentBlockParam[]
});
```

```csharp C# nocheck
using System;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Beta.Messages;

class Program
{
    static async Task Main(string[] args)
    {
        var client = new AnthropicClient();

        var parameters = new MessageCreateParams
        {
            Betas = ["compact-2026-01-12"],
            Model = "claude-opus-4-6",
            MaxTokens = 4096,
            Messages = messages,
            ContextManagement = new BetaContextManagementConfig
            {
                Edits = [new BetaCompact20260112Edit()]
            }
        };

        await foreach (var streamEvent in client.Beta.Messages.CreateStreaming(parameters))
        {
            if (streamEvent.Type == "content_block_start")
            {
                if (streamEvent.ContentBlock?.Type == "compaction")
                {
                    Console.WriteLine("Compaction started...");
                }
                else if (streamEvent.ContentBlock?.Type == "text")
                {
                    Console.WriteLine("Text response started...");
                }
            }
            else if (streamEvent.Type == "content_block_delta")
            {
                if (streamEvent.Delta?.Type == "compaction_delta")
                {
                    Console.WriteLine($"Compaction complete: {streamEvent.Delta.Content.Length} chars");
                }
                else if (streamEvent.Delta?.Type == "text_delta")
                {
                    Console.Write(streamEvent.Delta.Text);
                }
            }
        }
    }
}
```
```go Go hidelines={1..14,-1}
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()
	messages := []anthropic.BetaMessageParam{anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Hello, Claude"))}

	stream := client.Beta.Messages.NewStreaming(context.TODO(), anthropic.BetaMessageNewParams{
		Model:     anthropic.ModelClaudeOpus4_6,
		MaxTokens: 4096,
		Messages:  messages,
		ContextManagement: anthropic.BetaContextManagementConfigParam{
			Edits: []anthropic.BetaContextManagementConfigEditUnionParam{
				{OfCompact20260112: &anthropic.BetaCompact20260112EditParam{}},
			},
		},
		Betas: []anthropic.AnthropicBeta{"compact-2026-01-12"},
	})

	for stream.Next() {
		event := stream.Current()
		switch eventVariant := event.AsAny().(type) {
		case anthropic.BetaRawContentBlockStartEvent:
			switch eventVariant.ContentBlock.AsAny().(type) {
			case anthropic.BetaCompactionBlock:
				fmt.Println("Compaction started...")
			case anthropic.BetaTextBlock:
				fmt.Println("Text response started...")
			}
		case anthropic.BetaRawContentBlockDeltaEvent:
			switch deltaVariant := eventVariant.Delta.AsAny().(type) {
			case anthropic.BetaCompactionContentBlockDelta:
				fmt.Printf("Compaction complete: %d chars\n", len(deltaVariant.Content))
			case anthropic.BetaTextDelta:
				fmt.Print(deltaVariant.Text)
			}
		}
	}
	if err := stream.Err(); err != nil {
		log.Fatal(err)
	}
}
```

```java Java nocheck hidelines={1..10,-1}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.beta.messages.BetaContextManagementConfig;
import com.anthropic.models.beta.messages.BetaCompact20260112Edit;

public class CompactionStreamingExample {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCreateParams params = MessageCreateParams.builder()
            .model("claude-opus-4-6")
            .maxTokens(4096L)
            .addBeta("compact-2026-01-12")
            .addUserMessage("Hello, Claude")
            .contextManagement(BetaContextManagementConfig.builder()
                .addEdit(BetaCompact20260112Edit.builder().build())
                .build())
            .build();

        try (var streamResponse = client.beta().messages().createStreaming(params)) {
            streamResponse.stream().forEach(event -> {
                event.contentBlockStart().ifPresent(startEvent -> {
                    startEvent.contentBlock().compaction().ifPresent(c ->
                        System.out.println("Compaction started...")
                    );
                    startEvent.contentBlock().text().ifPresent(t ->
                        System.out.println("Text response started...")
                    );
                });

                event.contentBlockDelta().ifPresent(deltaEvent -> {
                    deltaEvent.delta().compaction().ifPresent(cd ->
                        System.out.println("Compaction complete: " + cd.content().length() + " chars")
                    );
                    deltaEvent.delta().text().ifPresent(td ->
                        System.out.print(td.text())
                    );
                });
            });
        }
    }
}
```

```php PHP hidelines={1..5}
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));
$messages = [['role' => 'user', 'content' => 'Hello, Claude']];

$stream = $client->beta->messages->createStream(
    maxTokens: 4096,
    messages: $messages,
    model: 'claude-opus-4-6',
    betas: ['compact-2026-01-12'],
    contextManagement: [
        'edits' => [
            ['type' => 'compact_20260112']
        ]
    ]
);

foreach ($stream as $event) {
    if ($event->type === 'content_block_start') {
        if ($event->contentBlock->type === 'compaction') {
            echo "Compaction started...\n";
        } elseif ($event->contentBlock->type === 'text') {
            echo "Text response started...\n";
        }
    } elseif ($event->type === 'content_block_delta') {
        if ($event->delta->type === 'compaction_delta') {
            echo "Compaction complete: " . strlen($event->delta->content) . " chars\n";
        } elseif ($event->delta->type === 'text_delta') {
            echo $event->delta->text;
        }
    }
}
```

```ruby Ruby hidelines={4}
require "anthropic"

client = Anthropic::Client.new
messages = [{ role: "user", content: "Hello, Claude" }]

stream = client.beta.messages.stream(
  betas: ["compact-2026-01-12"],
  model: "claude-opus-4-6",
  max_tokens: 4096,
  messages: messages,
  context_management: {
    edits: [{ type: "compact_20260112" }]
  }
)

stream.each do |event|
  case event.type
  when :content_block_start
    if event.content_block.type == :compaction
      puts "Compaction started..."
    elsif event.content_block.type == :text
      puts "Text response started..."
    end
  when :content_block_delta
    if event.delta.type == :compaction_delta
      puts "Compaction complete: #{event.delta.content.length} chars"
    elsif event.delta.type == :text_delta
      print event.delta.text
    end
  end
end
```
</CodeGroup>

### Prompt caching

Compaction works well with [prompt caching](/docs/en/build-with-claude/prompt-caching). You can add a `cache_control` breakpoint on compaction blocks to cache the summarized content. The original compacted content is ignored.

```json
{
  "role": "assistant",
  "content": [
    {
      "type": "compaction",
      "content": "[summary text]",
      "cache_control": { "type": "ephemeral" }
    },
    {
      "type": "text",
      "text": "Based on our conversation..."
    }
  ]
}
```

#### Maximizing cache hits with system prompts

When compaction occurs, the summary becomes new content that needs to be written to the cache. Without additional cache breakpoints, this would also invalidate any cached system prompt, requiring it to be re-cached along with the compaction summary.

To maximize cache hit rates, add a `cache_control` breakpoint at the end of your system prompt. This keeps the system prompt cached separately from the conversation, so when compaction occurs:

- The system prompt cache remains valid and is read from cache
- Only the compaction summary needs to be written as a new cache entry

<CodeGroup>
```python Python hidelines={1..4}
import anthropic

client = anthropic.Anthropic()
messages = [{"role": "user", "content": "Hello, Claude"}]
response = client.beta.messages.create(
    betas=["compact-2026-01-12"],
    model="claude-opus-4-6",
    max_tokens=4096,
    system=[
        {
            "type": "text",
            "text": "You are a helpful coding assistant...",
            "cache_control": {
                "type": "ephemeral"
            },  # Cache the system prompt separately
        }
    ],
    messages=messages,
    context_management={"edits": [{"type": "compact_20260112"}]},
)
```

```typescript TypeScript hidelines={1..3}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();
const messages: Anthropic.Beta.Messages.BetaMessageParam[] = [];

const response = await client.beta.messages.create({
  betas: ["compact-2026-01-12"],
  model: "claude-opus-4-6",
  max_tokens: 4096,
  system: [
    {
      type: "text",
      text: "You are a helpful coding assistant...",
      cache_control: { type: "ephemeral" } // Cache the system prompt separately
    }
  ],
  messages,
  context_management: {
    edits: [{ type: "compact_20260112" }]
  }
} as unknown as Anthropic.Beta.Messages.MessageCreateParamsNonStreaming);
```

```csharp C# nocheck
using System;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Beta.Messages;

class Program
{
    static async Task Main(string[] args)
    {
        var client = new AnthropicClient();

        var parameters = new MessageCreateParams
        {
            Betas = new[] { "compact-2026-01-12" },
            Model = "claude-opus-4-6",
            MaxTokens = 4096,
            System = new[]
            {
                new BetaTextBlockParam
                {
                    Type = "text",
                    Text = "You are a helpful coding assistant...",
                    CacheControl = new BetaCacheControlEphemeral()
                }
            },
            Messages = Array.Empty<BetaMessageParam>(),
            ContextManagement = new BetaContextManagementConfig
            {
                Edits = [new BetaCompact20260112Edit()]
            }
        };

        var response = await client.Beta.Messages.Create(parameters);
        Console.WriteLine(response);
    }
}
```
```go Go hidelines={1..13,-5..-1}
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
		Model:     anthropic.ModelClaudeOpus4_6,
		MaxTokens: 4096,
		System: []anthropic.BetaTextBlockParam{
			{
				Text:         "You are a helpful coding assistant...",
				CacheControl: anthropic.NewBetaCacheControlEphemeralParam(),
			},
		},
		Messages: []anthropic.BetaMessageParam{anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Hello, Claude"))},
		ContextManagement: anthropic.BetaContextManagementConfigParam{
			Edits: []anthropic.BetaContextManagementConfigEditUnionParam{
				{OfCompact20260112: &anthropic.BetaCompact20260112EditParam{}},
			},
		},
		Betas: []anthropic.AnthropicBeta{"compact-2026-01-12"},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(response)
}
```

```java Java nocheck hidelines={1..14,-1}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.beta.messages.BetaMessage;
import com.anthropic.models.beta.messages.BetaTextBlockParam;
import com.anthropic.models.beta.messages.BetaContextManagementConfig;
import com.anthropic.models.beta.messages.BetaCompact20260112Edit;
import com.anthropic.models.beta.messages.BetaCacheControlEphemeral;
import java.util.List;

public class CompactionExample {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCreateParams params = MessageCreateParams.builder()
            .model("claude-opus-4-6")
            .maxTokens(4096L)
            .addBeta("compact-2026-01-12")
            .systemOfBetaTextBlockParams(List.of(
                BetaTextBlockParam.builder()
                    .text("You are a helpful coding assistant...")
                    .cacheControl(BetaCacheControlEphemeral.builder().build())
                    .build()
            ))
            .addUserMessage("Hello, Claude")
            .contextManagement(BetaContextManagementConfig.builder()
                .addEdit(BetaCompact20260112Edit.builder().build())
                .build())
            .build();

        BetaMessage response = client.beta().messages().create(params);
        System.out.println(response);
    }
}
```

```php PHP hidelines={1..5}
<?php
use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$response = $client->beta->messages->create(
    maxTokens: 4096,
    messages: [['role' => 'user', 'content' => 'Hello, Claude']],
    model: 'claude-opus-4-6',
    betas: ['compact-2026-01-12'],
    system: [
        [
            'type' => 'text',
            'text' => 'You are a helpful coding assistant...',
            'cache_control' => [
                'type' => 'ephemeral'
            ]
        ]
    ],
    contextManagement: [
        'edits' => [
            ['type' => 'compact_20260112']
        ]
    ]
);

echo $response->content[0]->text;
```

```ruby Ruby
require "anthropic"

client = Anthropic::Client.new

response = client.beta.messages.create(
  betas: ["compact-2026-01-12"],
  model: "claude-opus-4-6",
  max_tokens: 4096,
  system: [
    {
      type: "text",
      text: "You are a helpful coding assistant...",
      cache_control: {
        type: "ephemeral"
      }
    }
  ],
  messages: [],
  context_management: {
    edits: [{ type: "compact_20260112" }]
  }
)
puts response
```
</CodeGroup>

This approach is particularly beneficial for long system prompts, as they remain cached even across multiple compaction events throughout a conversation.

## Understanding usage

Compaction requires an additional sampling step, which contributes to rate limits and billing. The API returns detailed usage information in the response:

```json
{
  "usage": {
    "input_tokens": 45000,
    "output_tokens": 1234,
    "iterations": [
      {
        "type": "compaction",
        "input_tokens": 180000,
        "output_tokens": 3500
      },
      {
        "type": "message",
        "input_tokens": 23000,
        "output_tokens": 1000
      }
    ]
  }
}
```

The `iterations` array shows usage for each sampling iteration. When compaction occurs, you'll see a `compaction` iteration followed by the main `message` iteration. The final iteration's token counts reflect the effective context size after compaction.

<Note>
The top-level `input_tokens` and `output_tokens` do not include compaction iteration usage. They reflect the sum of all non-compaction iterations. To calculate total tokens consumed and billed for a request, sum across all entries in the `usage.iterations` array.

If you previously relied on `usage.input_tokens` and `usage.output_tokens` for cost tracking or auditing, you'll need to update your tracking logic to aggregate across `usage.iterations` when compaction is enabled. The `iterations` array is only populated when a new compaction is triggered during the request. Re-applying a previous `compaction` block incurs no additional compaction cost, and the top-level usage fields remain accurate in that case.
</Note>

## Combining with other features

### Server tools

When using server tools (like web search), the compaction trigger is checked at the start of each sampling iteration. Compaction may occur multiple times within a single request depending on your trigger threshold and the amount of output generated.

### Token counting

The token counting endpoint (`/v1/messages/count_tokens`) applies existing `compaction` blocks in your prompt but does not trigger new compactions. Use it to check your effective token count after previous compactions:

<CodeGroup>
```python Python hidelines={1..4}
import anthropic

client = anthropic.Anthropic()
messages = [{"role": "user", "content": "Hello, Claude"}]
count_response = client.beta.messages.count_tokens(
    betas=["compact-2026-01-12"],
    model="claude-opus-4-6",
    messages=messages,
    context_management={"edits": [{"type": "compact_20260112"}]},
)

print(f"Current tokens: {count_response.input_tokens}")
print(f"Original tokens: {count_response.context_management.original_input_tokens}")
```

```typescript TypeScript hidelines={1..3}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();
const messages: Anthropic.Beta.Messages.BetaMessageParam[] = [
  { role: "user", content: "Summarize the key points of our conversation so far." }
];

const countResponse = await client.beta.messages.countTokens({
  betas: ["compact-2026-01-12"],
  model: "claude-opus-4-6",
  messages,
  context_management: {
    edits: [{ type: "compact_20260112" }]
  }
} as unknown as Anthropic.Beta.Messages.MessageCountTokensParams);

console.log(`Current tokens: ${countResponse.input_tokens}`);
console.log(`Original tokens: ${countResponse.context_management!.original_input_tokens}`);
```

```csharp C# nocheck
using System;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Beta.Messages;

class Program
{
    static async Task Main(string[] args)
    {
        AnthropicClient client = new();

        var countParams = new MessageCountTokensParams
        {
            Model = "claude-opus-4-6",
            Messages = messages,
            ContextManagement = new BetaContextManagementConfig
            {
                Edits = [new BetaCompact20260112Edit()]
            },
            Betas = ["compact-2026-01-12"]
        };

        var countResponse = await client.Beta.Messages.CountTokens(countParams);
        Console.WriteLine($"Current tokens: {countResponse.InputTokens}");
        Console.WriteLine($"Original tokens: {countResponse.ContextManagement.OriginalInputTokens}");
    }
}
```
```go Go hidelines={1..14,-7..-5,-1}
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()
	messages := []anthropic.BetaMessageParam{anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Hello, Claude"))}

	countResponse, err := client.Beta.Messages.CountTokens(context.TODO(), anthropic.BetaMessageCountTokensParams{
		Model:    anthropic.ModelClaudeOpus4_6,
		Messages: messages,
		ContextManagement: anthropic.BetaContextManagementConfigParam{
			Edits: []anthropic.BetaContextManagementConfigEditUnionParam{
				{OfCompact20260112: &anthropic.BetaCompact20260112EditParam{}},
			},
		},
		Betas: []anthropic.AnthropicBeta{"compact-2026-01-12"},
	})
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("Current tokens: %d\n", countResponse.InputTokens)
	fmt.Printf("Original tokens: %d\n", countResponse.ContextManagement.OriginalInputTokens)
}
```

```java Java nocheck hidelines={1..11,-1}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.BetaMessageTokensCount;
import com.anthropic.models.beta.messages.MessageCountTokensParams;
import com.anthropic.models.beta.messages.BetaContextManagementConfig;
import com.anthropic.models.beta.messages.BetaCompact20260112Edit;

public class Main {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCountTokensParams params = MessageCountTokensParams.builder()
            .model("claude-opus-4-6")
            .addUserMessage("Hello, Claude")
            .contextManagement(BetaContextManagementConfig.builder()
                .addEdit(BetaCompact20260112Edit.builder().build())
                .build())
            .addBeta("compact-2026-01-12")
            .build();

        BetaMessageTokensCount countResponse = client.beta().messages().countTokens(params);
        System.out.println("Current tokens: " + countResponse.inputTokens());
        System.out.println("Original tokens: " + countResponse.contextManagement().get().originalInputTokens());
    }
}
```

```php PHP hidelines={1..5}
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));
$messages = [['role' => 'user', 'content' => 'Hello, Claude']];

$countResponse = $client->beta->messages->countTokens(
    messages: $messages,
    model: 'claude-opus-4-6',
    betas: ['compact-2026-01-12'],
    contextManagement: [
        'edits' => [
            ['type' => 'compact_20260112']
        ]
    ]
);

echo "Current tokens: " . $countResponse->inputTokens . "\n";
echo "Original tokens: " . $countResponse->contextManagement->originalInputTokens . "\n";
```

```ruby Ruby hidelines={4}
require "anthropic"

client = Anthropic::Client.new
messages = [{ role: "user", content: "Hello, Claude" }]

count_response = client.beta.messages.count_tokens(
  betas: ["compact-2026-01-12"],
  model: "claude-opus-4-6",
  messages: messages,
  context_management: {
    edits: [{ type: "compact_20260112" }]
  }
)

puts "Current tokens: #{count_response.input_tokens}"
puts "Original tokens: #{count_response.context_management.original_input_tokens}"
```
</CodeGroup>

## Examples

Here's a complete example of a long-running conversation with compaction:

<CodeGroup>
```python Python
import anthropic

client = anthropic.Anthropic()

messages: list[dict] = []


def chat(user_message: str) -> str:
    messages.append({"role": "user", "content": user_message})

    response = client.beta.messages.create(
        betas=["compact-2026-01-12"],
        model="claude-opus-4-6",
        max_tokens=4096,
        messages=messages,
        context_management={
            "edits": [
                {
                    "type": "compact_20260112",
                    "trigger": {"type": "input_tokens", "value": 100000},
                }
            ]
        },
    )

    # Append response (compaction blocks are automatically included)
    messages.append({"role": "assistant", "content": response.content})

    # Return the text content
    return next(block.text for block in response.content if block.type == "text")


# Run a long conversation
print(chat("Help me build a Python web scraper"))
print(chat("Add support for JavaScript-rendered pages"))
print(chat("Now add rate limiting and error handling"))
# ... continue as long as needed
```

```typescript TypeScript hidelines={1..4}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const messages: Anthropic.Beta.BetaMessageParam[] = [];

async function chat(userMessage: string): Promise<string> {
  messages.push({ role: "user", content: userMessage });

  const response = await client.beta.messages.create({
    betas: ["compact-2026-01-12"],
    model: "claude-opus-4-6",
    max_tokens: 4096,
    messages,
    context_management: {
      edits: [
        {
          type: "compact_20260112",
          trigger: { type: "input_tokens", value: 100000 }
        }
      ]
    }
  });

  // Append response (compaction blocks are automatically included)
  messages.push({ role: "assistant", content: response.content });

  // Return the text content
  const textBlock = response.content.find((block) => block.type === "text");
  return textBlock?.text ?? "";
}

// Run a long conversation
console.log(await chat("Help me build a Python web scraper"));
console.log(await chat("Add support for JavaScript-rendered pages"));
console.log(await chat("Now add rate limiting and error handling"));
// ... continue as long as needed
```

```csharp C# nocheck
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Beta.Messages;

public class Program
{
    static async Task Main(string[] args)
    {
        AnthropicClient client = new();
        List<BetaMessageParam> messages = new();

        Console.WriteLine(await Chat(client, messages, "Help me build a Python web scraper"));
        Console.WriteLine(await Chat(client, messages, "Add support for JavaScript-rendered pages"));
        Console.WriteLine(await Chat(client, messages, "Now add rate limiting and error handling"));
    }

    static async Task<string> Chat(AnthropicClient client, List<BetaMessageParam> messages, string userMessage)
    {
        messages.Add(new() { Role = Role.User, Content = userMessage });

        var parameters = new MessageCreateParams
        {
            Betas = new[] { "compact-2026-01-12" },
            Model = "claude-opus-4-6",
            MaxTokens = 4096,
            Messages = messages,
            ContextManagement = new BetaContextManagementConfig
            {
                Edits = [new BetaCompact20260112Edit
                {
                    Trigger = new BetaInputTokensTrigger(100000)
                }]
            }
        };

        var response = await client.Beta.Messages.Create(parameters);

        messages.Add(new() { Role = Role.Assistant, Content = response.Content });

        return response.Content.FirstOrDefault(block => block.Type == "text")?.Text ?? "";
    }
}
```
```go Go
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/anthropics/anthropic-sdk-go"
)

var (
	client   = anthropic.NewClient()
	messages []anthropic.BetaMessageParam
)

func chat(userMessage string) string {
	messages = append(messages, anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock(userMessage)))

	response, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
		Model:     anthropic.ModelClaudeOpus4_6,
		MaxTokens: 4096,
		Messages:  messages,
		ContextManagement: anthropic.BetaContextManagementConfigParam{
			Edits: []anthropic.BetaContextManagementConfigEditUnionParam{
				{OfCompact20260112: &anthropic.BetaCompact20260112EditParam{
					Trigger: anthropic.BetaInputTokensTriggerParam{Value: 100000},
				}},
			},
		},
		Betas: []anthropic.AnthropicBeta{"compact-2026-01-12"},
	})
	if err != nil {
		log.Fatal(err)
	}

	messages = append(messages, response.ToParam())

	for _, block := range response.Content {
		if variant, ok := block.AsAny().(anthropic.BetaTextBlock); ok {
			return variant.Text
		}
	}
	return ""
}

func main() {
	fmt.Println(chat("Help me build a Python web scraper"))
	fmt.Println(chat("Add support for JavaScript-rendered pages"))
	fmt.Println(chat("Now add rate limiting and error handling"))
}
```

```java Java nocheck hidelines={1..12,-1}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.beta.messages.BetaMessage;
import com.anthropic.models.beta.messages.BetaMessageParam;
import com.anthropic.models.beta.messages.BetaContextManagementConfig;
import com.anthropic.models.beta.messages.BetaCompact20260112Edit;
import com.anthropic.models.beta.messages.BetaInputTokensTrigger;
import java.util.ArrayList;
import java.util.List;

public class CompactionExample {
    private static final AnthropicClient client = AnthropicOkHttpClient.fromEnv();
    private static final List<BetaMessageParam> messages = new ArrayList<>();

    public static void main(String[] args) {
        System.out.println(chat("Help me build a Python web scraper"));
        System.out.println(chat("Add support for JavaScript-rendered pages"));
        System.out.println(chat("Now add rate limiting and error handling"));
    }

    private static String chat(String userMessage) {
        messages.add(BetaMessageParam.builder()
            .role(BetaMessageParam.Role.USER)
            .content(userMessage)
            .build());

        MessageCreateParams params = MessageCreateParams.builder()
            .addBeta("compact-2026-01-12")
            .model("claude-opus-4-6")
            .maxTokens(4096L)
            .messages(messages)
            .contextManagement(BetaContextManagementConfig.builder()
                .addEdit(BetaCompact20260112Edit.builder()
                    .trigger(BetaInputTokensTrigger.builder()
                        .value(100000L)
                        .build())
                    .build())
                .build())
            .build();

        BetaMessage response = client.beta().messages().create(params);

        // Append response (compaction blocks are automatically included)
        messages.add(response.toParam());

        return response.content().stream()
            .filter(block -> block.text().isPresent())
            .map(block -> block.text().get().text())
            .findFirst()
            .orElse("");
    }
}
```

```php PHP hidelines={1..4}
<?php
use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));
$messages = [];

function chat($client, &$messages, $userMessage) {
    $messages[] = ['role' => 'user', 'content' => $userMessage];

    $response = $client->beta->messages->create(
        maxTokens: 4096,
        messages: $messages,
        model: 'claude-opus-4-6',
        betas: ['compact-2026-01-12'],
        contextManagement: [
            'edits' => [
                [
                    'type' => 'compact_20260112',
                    'trigger' => ['type' => 'input_tokens', 'value' => 100000]
                ]
            ]
        ]
    );

    $messages[] = ['role' => 'assistant', 'content' => $response->content];

    foreach ($response->content as $block) {
        if ($block->type === 'text') {
            return $block->text;
        }
    }
    return '';
}

echo chat($client, $messages, "Help me build a Python web scraper") . "\n";
echo chat($client, $messages, "Add support for JavaScript-rendered pages") . "\n";
echo chat($client, $messages, "Now add rate limiting and error handling") . "\n";
```

```ruby Ruby
require "anthropic"

client = Anthropic::Client.new
messages = []

def chat(client, messages, user_message)
  messages << { role: "user", content: user_message }

  response = client.beta.messages.create(
    betas: ["compact-2026-01-12"],
    model: "claude-opus-4-6",
    max_tokens: 4096,
    messages: messages,
    context_management: {
      edits: [
        {
          type: "compact_20260112",
          trigger: { type: "input_tokens", value: 100000 }
        }
      ]
    }
  )

  messages << { role: "assistant", content: response.content }

  response.content.find { |block| block.type == :text }&.text || ""
end

puts chat(client, messages, "Help me build a Python web scraper")
puts chat(client, messages, "Add support for JavaScript-rendered pages")
puts chat(client, messages, "Now add rate limiting and error handling")
```
</CodeGroup>

Here's an example that uses `pause_after_compaction` to preserve the last two messages (one user + one assistant turn) verbatim instead of summarizing them:

<CodeGroup>
```python Python
import anthropic
from typing import Any

client = anthropic.Anthropic()

messages: list[dict[str, Any]] = []


def chat(user_message: str) -> str:
    messages.append({"role": "user", "content": user_message})

    response = client.beta.messages.create(
        betas=["compact-2026-01-12"],
        model="claude-opus-4-6",
        max_tokens=4096,
        messages=messages,
        context_management={
            "edits": [
                {
                    "type": "compact_20260112",
                    "trigger": {"type": "input_tokens", "value": 100000},
                    "pause_after_compaction": True,
                }
            ]
        },
    )

    # Check if compaction occurred and paused
    if response.stop_reason == "compaction":
        # Get the compaction block from the response
        compaction_block = response.content[0]

        # Preserve the last 2 messages (1 user + 1 assistant turn)
        # by including them after the compaction block
        preserved_messages = messages[-2:] if len(messages) >= 2 else messages

        # Build new message list: compaction + preserved messages
        new_assistant_content = [compaction_block]
        messages_after_compaction = [
            {"role": "assistant", "content": new_assistant_content}
        ] + preserved_messages

        # Continue the request with the compacted context + preserved messages
        response = client.beta.messages.create(
            betas=["compact-2026-01-12"],
            model="claude-opus-4-6",
            max_tokens=4096,
            messages=messages_after_compaction,
            context_management={"edits": [{"type": "compact_20260112"}]},
        )

        # Update our message list to reflect the compaction
        messages.clear()
        messages.extend(messages_after_compaction)

    # Append the final response
    messages.append({"role": "assistant", "content": response.content})

    # Return the text content
    return next(block.text for block in response.content if block.type == "text")


# Run a long conversation
print(chat("Help me build a Python web scraper"))
print(chat("Add support for JavaScript-rendered pages"))
print(chat("Now add rate limiting and error handling"))
# ... continue as long as needed
```

```typescript TypeScript hidelines={1..4}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

let messages: Anthropic.Beta.BetaMessageParam[] = [];

async function chat(userMessage: string): Promise<string> {
  messages.push({ role: "user", content: userMessage });

  let response = await client.beta.messages.create({
    betas: ["compact-2026-01-12"],
    model: "claude-opus-4-6",
    max_tokens: 4096,
    messages,
    context_management: {
      edits: [
        {
          type: "compact_20260112",
          trigger: { type: "input_tokens", value: 100000 },
          pause_after_compaction: true
        }
      ]
    }
  });

  // Check if compaction occurred and paused
  if (response.stop_reason === "compaction") {
    // Get the compaction block from the response
    const compactionBlock = response.content[0];

    // Preserve the last 2 messages (1 user + 1 assistant turn)
    // by including them after the compaction block
    const preservedMessages = messages.length >= 2 ? messages.slice(-2) : [...messages];

    // Build new message list: compaction + preserved messages
    const messagesAfterCompaction: Anthropic.Beta.BetaMessageParam[] = [
      { role: "assistant", content: [compactionBlock] },
      ...preservedMessages
    ];

    // Continue the request with the compacted context + preserved messages
    response = await client.beta.messages.create({
      betas: ["compact-2026-01-12"],
      model: "claude-opus-4-6",
      max_tokens: 4096,
      messages: messagesAfterCompaction,
      context_management: {
        edits: [{ type: "compact_20260112" }]
      }
    });

    // Update our message list to reflect the compaction
    messages = messagesAfterCompaction;
  }

  // Append the final response
  messages.push({ role: "assistant", content: response.content });

  // Return the text content
  const textBlock = response.content.find((block) => block.type === "text");
  return textBlock?.text ?? "";
}

// Run a long conversation
console.log(await chat("Help me build a Python web scraper"));
console.log(await chat("Add support for JavaScript-rendered pages"));
console.log(await chat("Now add rate limiting and error handling"));
// ... continue as long as needed
```

```csharp C# nocheck
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Beta.Messages;

public class CompactionExample
{
    private static AnthropicClient client = new();
    private static List<BetaMessageParam> messages = new();

    static async Task<string> Chat(string userMessage)
    {
        messages.Add(new() { Role = Role.User, Content = userMessage });

        var response = await client.Beta.Messages.Create(new MessageCreateParams
        {
            Betas = new[] { "compact-2026-01-12" },
            Model = "claude-opus-4-6",
            MaxTokens = 4096,
            Messages = messages,
            ContextManagement = new BetaContextManagementConfig
            {
                Edits = [new BetaCompact20260112Edit
                {
                    Trigger = new BetaInputTokensTrigger(100000),
                    PauseAfterCompaction = true
                }]
            }
        });

        if (response.StopReason == "compaction")
        {
            var compactionBlock = response.Content[0];

            var preserved = messages.Count >= 2
                ? messages.Skip(messages.Count - 2).ToList()
                : new List<BetaMessageParam>(messages);

            var messagesAfterCompaction = new List<BetaMessageParam>
            {
                new() { Role = Role.Assistant, Content = new[] { compactionBlock } }
            };
            messagesAfterCompaction.AddRange(preserved);

            response = await client.Beta.Messages.Create(new MessageCreateParams
            {
                Betas = new[] { "compact-2026-01-12" },
                Model = "claude-opus-4-6",
                MaxTokens = 4096,
                Messages = messagesAfterCompaction,
                ContextManagement = new BetaContextManagementConfig
                {
                    Edits = [new BetaCompact20260112Edit()]
                }
            });

            messages = messagesAfterCompaction;
        }

        messages.Add(new() { Role = Role.Assistant, Content = response.Content });

        return response.Content.FirstOrDefault(block => block.Type == "text")?.Text ?? "";
    }

    static async Task Main()
    {
        Console.WriteLine(await Chat("Help me build a Python web scraper"));
        Console.WriteLine(await Chat("Add support for JavaScript-rendered pages"));
        Console.WriteLine(await Chat("Now add rate limiting and error handling"));
    }
}
```
```go Go
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/anthropics/anthropic-sdk-go"
)

var (
	client   = anthropic.NewClient()
	messages []anthropic.BetaMessageParam
)

func chat(userMessage string) string {
	messages = append(messages, anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock(userMessage)))

	compactEdit := anthropic.BetaContextManagementConfigParam{
		Edits: []anthropic.BetaContextManagementConfigEditUnionParam{
			{OfCompact20260112: &anthropic.BetaCompact20260112EditParam{
				Trigger:              anthropic.BetaInputTokensTriggerParam{Value: 100000},
				PauseAfterCompaction: anthropic.Bool(true),
			}},
		},
	}

	response, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
		Model:             anthropic.ModelClaudeOpus4_6,
		MaxTokens:         4096,
		Messages:          messages,
		ContextManagement: compactEdit,
		Betas:             []anthropic.AnthropicBeta{"compact-2026-01-12"},
	})
	if err != nil {
		log.Fatal(err)
	}

	if response.StopReason == "compaction" {
		compactionParam := response.Content[0].ToParam()

		var preserved []anthropic.BetaMessageParam
		if len(messages) >= 2 {
			preserved = messages[len(messages)-2:]
		} else {
			preserved = messages
		}

		messagesAfterCompaction := []anthropic.BetaMessageParam{
			{Role: anthropic.BetaMessageParamRoleAssistant, Content: []anthropic.BetaContentBlockParamUnion{compactionParam}},
		}
		messagesAfterCompaction = append(messagesAfterCompaction, preserved...)

		response, err = client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
			Model:     anthropic.ModelClaudeOpus4_6,
			MaxTokens: 4096,
			Messages:  messagesAfterCompaction,
			ContextManagement: anthropic.BetaContextManagementConfigParam{
				Edits: []anthropic.BetaContextManagementConfigEditUnionParam{
					{OfCompact20260112: &anthropic.BetaCompact20260112EditParam{}},
				},
			},
			Betas: []anthropic.AnthropicBeta{"compact-2026-01-12"},
		})
		if err != nil {
			log.Fatal(err)
		}

		messages = messagesAfterCompaction
	}

	messages = append(messages, response.ToParam())

	for _, block := range response.Content {
		if textBlock, ok := block.AsAny().(anthropic.BetaTextBlock); ok {
			return textBlock.Text
		}
	}
	return ""
}

func main() {
	fmt.Println(chat("Help me build a Python web scraper"))
	fmt.Println(chat("Add support for JavaScript-rendered pages"))
	fmt.Println(chat("Now add rate limiting and error handling"))
}
```

```java Java nocheck hidelines={1..12,-1}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.beta.messages.BetaMessage;
import com.anthropic.models.beta.messages.BetaMessageParam;
import com.anthropic.models.beta.messages.BetaContextManagementConfig;
import com.anthropic.models.beta.messages.BetaCompact20260112Edit;
import com.anthropic.models.beta.messages.BetaInputTokensTrigger;
import com.anthropic.models.beta.messages.BetaStopReason;
import java.util.ArrayList;
import java.util.List;

public class CompactionExample {
    private static final AnthropicClient client = AnthropicOkHttpClient.fromEnv();
    private static final List<BetaMessageParam> messages = new ArrayList<>();

    public static String chat(String userMessage) {
        messages.add(BetaMessageParam.builder()
            .role(BetaMessageParam.Role.USER)
            .content(userMessage)
            .build());

        MessageCreateParams params = MessageCreateParams.builder()
            .addBeta("compact-2026-01-12")
            .model("claude-opus-4-6")
            .maxTokens(4096L)
            .messages(messages)
            .contextManagement(BetaContextManagementConfig.builder()
                .addEdit(BetaCompact20260112Edit.builder()
                    .trigger(BetaInputTokensTrigger.builder()
                        .value(100000L)
                        .build())
                    .pauseAfterCompaction(true)
                    .build())
                .build())
            .build();

        BetaMessage response = client.beta().messages().create(params);

        // Check if compaction occurred and paused
        if (response.stopReason().isPresent()
                && response.stopReason().get().equals(BetaStopReason.COMPACTION)) {
            // Preserve the last 2 messages (1 user + 1 assistant turn)
            List<BetaMessageParam> preservedMessages = messages.size() >= 2
                ? new ArrayList<>(messages.subList(messages.size() - 2, messages.size()))
                : new ArrayList<>(messages);

            // Build new message list: compaction + preserved messages
            List<BetaMessageParam> messagesAfterCompaction = new ArrayList<>();
            messagesAfterCompaction.add(response.toParam());
            messagesAfterCompaction.addAll(preservedMessages);

            // Continue the request with the compacted context + preserved messages
            MessageCreateParams continueParams = MessageCreateParams.builder()
                .addBeta("compact-2026-01-12")
                .model("claude-opus-4-6")
                .maxTokens(4096L)
                .messages(messagesAfterCompaction)
                .contextManagement(BetaContextManagementConfig.builder()
                    .addEdit(BetaCompact20260112Edit.builder().build())
                    .build())
                .build();

            response = client.beta().messages().create(continueParams);

            // Update our message list to reflect the compaction
            messages.clear();
            messages.addAll(messagesAfterCompaction);
        }

        // Append the final response
        messages.add(response.toParam());

        return response.content().stream()
            .filter(block -> block.text().isPresent())
            .map(block -> block.text().get().text())
            .findFirst()
            .orElse("");
    }

    public static void main(String[] args) {
        System.out.println(chat("Help me build a Python web scraper"));
        System.out.println(chat("Add support for JavaScript-rendered pages"));
        System.out.println(chat("Now add rate limiting and error handling"));
    }
}
```

```php PHP hidelines={1..5}
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));
$messages = [];

function chat($client, &$messages, $userMessage) {
    $messages[] = ['role' => 'user', 'content' => $userMessage];

    $response = $client->beta->messages->create(
        maxTokens: 4096,
        messages: $messages,
        model: 'claude-opus-4-6',
        betas: ['compact-2026-01-12'],
        contextManagement: [
            'edits' => [
                [
                    'type' => 'compact_20260112',
                    'trigger' => ['type' => 'input_tokens', 'value' => 100000],
                    'pause_after_compaction' => true
                ]
            ]
        ]
    );

    if ($response->stopReason === 'compaction') {
        $compactionBlock = $response->content[0];

        $preserved = count($messages) >= 2
            ? array_slice($messages, -2)
            : $messages;

        $messagesAfterCompaction = array_merge(
            [['role' => 'assistant', 'content' => [$compactionBlock]]],
            $preserved
        );

        $response = $client->beta->messages->create(
            maxTokens: 4096,
            messages: $messagesAfterCompaction,
            model: 'claude-opus-4-6',
            betas: ['compact-2026-01-12'],
            contextManagement: [
                'edits' => [['type' => 'compact_20260112']]
            ]
        );

        $messages = $messagesAfterCompaction;
    }

    $messages[] = ['role' => 'assistant', 'content' => $response->content];

    foreach ($response->content as $block) {
        if ($block->type === 'text') {
            return $block->text;
        }
    }
    return '';
}

echo chat($client, $messages, "Help me build a Python web scraper") . "\n";
echo chat($client, $messages, "Add support for JavaScript-rendered pages") . "\n";
echo chat($client, $messages, "Now add rate limiting and error handling") . "\n";
```

```ruby Ruby
require "anthropic"

client = Anthropic::Client.new
messages = []

def chat(client, messages, user_message)
  messages << { role: "user", content: user_message }

  response = client.beta.messages.create(
    betas: ["compact-2026-01-12"],
    model: "claude-opus-4-6",
    max_tokens: 4096,
    messages: messages,
    context_management: {
      edits: [
        {
          type: "compact_20260112",
          trigger: { type: "input_tokens", value: 100000 },
          pause_after_compaction: true
        }
      ]
    }
  )

  if response.stop_reason == :compaction
    compaction_block = response.content[0]

    preserved = messages.length >= 2 ? messages[-2..-1] : messages.dup

    messages_after_compaction = [
      { role: "assistant", content: [compaction_block] }
    ] + preserved

    response = client.beta.messages.create(
      betas: ["compact-2026-01-12"],
      model: "claude-opus-4-6",
      max_tokens: 4096,
      messages: messages_after_compaction,
      context_management: {
        edits: [{ type: "compact_20260112" }]
      }
    )

    messages.clear
    messages.concat(messages_after_compaction)
  end

  messages << { role: "assistant", content: response.content }

  response.content.find { |block| block.type == :text }&.text || ""
end

puts chat(client, messages, "Help me build a Python web scraper")
puts chat(client, messages, "Add support for JavaScript-rendered pages")
puts chat(client, messages, "Now add rate limiting and error handling")
```
</CodeGroup>

## Current limitations

- **Same model for summarization:** The model specified in your request is used for summarization. There is no option to use a different (for example, cheaper) model for the summary.

## Next steps

<CardGroup>
  <Card title="Compaction cookbook" icon="book" href="https://platform.claude.com/cookbook">
    Explore practical examples and implementations in the cookbook.
  </Card>
  <Card title="Context windows" icon="arrows-maximize" href="/docs/en/build-with-claude/context-windows">
    Learn about context window sizes and management strategies.
  </Card>
  <Card title="Context editing" icon="pen" href="/docs/en/build-with-claude/context-editing">
    Explore other strategies for managing conversation context like tool result clearing and thinking block clearing.
  </Card>
</CardGroup>