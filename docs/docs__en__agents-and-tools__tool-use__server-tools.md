# Server tools

Work with Anthropic-executed tools: server_tool_use blocks, pause_turn continuation, and domain filtering.

---

This page covers the shared mechanics of server-executed tools: the `server_tool_use` block, `pause_turn` continuation, ZDR considerations, and domain filtering. For individual tools, see the [tool reference](/docs/en/agents-and-tools/tool-use/tool-reference).

## The server_tool_use block

The `server_tool_use` block appears in Claude's response when a server-executed tool runs. Its `id` field uses the `srvtoolu_` prefix to distinguish it from client tool calls:

```json
{
  "type": "server_tool_use",
  "id": "srvtoolu_01A2B3C4D5E6F7G8H9",
  "name": "web_search",
  "input": { "query": "latest quantum computing breakthroughs" }
}
```

The API executes the tool internally. You see the call and its result in the response, but you don't handle execution. Unlike client `tool_use` blocks, you don't need to respond with a `tool_result`. The result block appears immediately after the `server_tool_use` block in the same assistant turn.

## The server-side loop and pause_turn

When using server tools like web search, the API may return a `pause_turn` stop reason, indicating that the API has paused a long-running turn.

Here's how to handle the `pause_turn` stop reason:

<CodeGroup>
```python Python hidelines={1..4}
import anthropic

client = anthropic.Anthropic()

# Initial request with web search
response = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Search for comprehensive information about quantum computing breakthroughs in 2025",
        }
    ],
    tools=[{"type": "web_search_20250305", "name": "web_search", "max_uses": 10}],
)

# Check if the response has pause_turn stop reason
if response.stop_reason == "pause_turn":
    # Continue the conversation with the paused content
    messages = [
        {
            "role": "user",
            "content": "Search for comprehensive information about quantum computing breakthroughs in 2025",
        },
        {"role": "assistant", "content": response.content},
    ]

    # Send the continuation request
    continuation = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=1024,
        messages=messages,
        tools=[{"type": "web_search_20250305", "name": "web_search", "max_uses": 10}],
    )

    print(continuation)
else:
    print(response)
```

```typescript TypeScript hidelines={1..4}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

async function main() {
  // Initial request with web search
  const response = await client.messages.create({
    model: "claude-opus-4-7",
    max_tokens: 1024,
    messages: [
      {
        role: "user",
        content:
          "Search for comprehensive information about quantum computing breakthroughs in 2025"
      }
    ],
    tools: [
      {
        type: "web_search_20250305",
        name: "web_search",
        max_uses: 10
      }
    ]
  });

  // Check if the response has pause_turn stop reason
  if (response.stop_reason === "pause_turn") {
    // Continue the conversation with the paused content
    const messages: Anthropic.MessageParam[] = [
      {
        role: "user",
        content:
          "Search for comprehensive information about quantum computing breakthroughs in 2025"
      },
      { role: "assistant", content: response.content }
    ];

    // Send the continuation request
    const continuation = await client.messages.create({
      model: "claude-opus-4-7",
      max_tokens: 1024,
      messages: messages,
      tools: [
        {
          type: "web_search_20250305",
          name: "web_search",
          max_uses: 10
        }
      ]
    });

    console.log(continuation);
  } else {
    console.log(response);
  }
}

main().catch(console.error);
```

```csharp C#
using Anthropic;
using Anthropic.Models.Messages;
using System;
using System.Linq;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        AnthropicClient client = new();

        var parameters = new MessageCreateParams
        {
            Model = "claude-opus-4-7",
            MaxTokens = 1024,
            Messages = [
                new() {
                    Role = Role.User,
                    Content = "Search for comprehensive information about quantum computing breakthroughs in 2025"
                }
            ],
            Tools = [new ToolUnion(new WebSearchTool20250305() { MaxUses = 10 })]
        };

        var response = await client.Messages.Create(parameters);

        if (response.StopReason == "pause_turn")
        {
            var continuationParams = new MessageCreateParams
            {
                Model = "claude-opus-4-7",
                MaxTokens = 1024,
                Messages = [
                    new() {
                        Role = Role.User,
                        Content = "Search for comprehensive information about quantum computing breakthroughs in 2025"
                    },
                    new() {
                        Role = Role.Assistant,
                        Content = response.Content.Select(block => new ContentBlockParam(block.Json)).ToList()
                    }
                ],
                Tools = [new ToolUnion(new WebSearchTool20250305() { MaxUses = 10 })]
            };

            var continuation = await client.Messages.Create(continuationParams);
            Console.WriteLine(continuation);
        }
        else
        {
            Console.WriteLine(response);
        }
    }
}
```

```go Go hidelines={1..13,-1}
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	webSearchTool := []anthropic.ToolUnionParam{
		{OfWebSearchTool20250305: &anthropic.WebSearchTool20250305Param{
			MaxUses: anthropic.Int(10),
		}},
	}

	response, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
		Model:     anthropic.ModelClaudeOpus4_7,
		MaxTokens: 1024,
		Messages: []anthropic.MessageParam{
			anthropic.NewUserMessage(anthropic.NewTextBlock("Search for comprehensive information about quantum computing breakthroughs in 2025")),
		},
		Tools: webSearchTool,
	})
	if err != nil {
		log.Fatal(err)
	}

	if response.StopReason == "pause_turn" {
		// Convert response content to param types for the assistant message
		var contentParams []anthropic.ContentBlockParamUnion
		for _, block := range response.Content {
			contentParams = append(contentParams, block.ToParam())
		}

		continuation, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
			Model:     anthropic.ModelClaudeOpus4_7,
			MaxTokens: 1024,
			Messages: []anthropic.MessageParam{
				anthropic.NewUserMessage(anthropic.NewTextBlock("Search for comprehensive information about quantum computing breakthroughs in 2025")),
				anthropic.NewAssistantMessage(contentParams...),
			},
			Tools: webSearchTool,
		})
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(continuation)
	} else {
		fmt.Println(response)
	}
}
```

```java Java hidelines={1..4,7..8,-1..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.StopReason;
import com.anthropic.models.messages.WebSearchTool20250305;

void main() {
    AnthropicClient client = AnthropicOkHttpClient.fromEnv();

    MessageCreateParams params = MessageCreateParams.builder()
        .model("claude-opus-4-7")
        .maxTokens(1024L)
        .addUserMessage("Search for comprehensive information about quantum computing breakthroughs in 2025")
        .addTool(WebSearchTool20250305.builder()
            .maxUses(10L)
            .build())
        .build();

    Message response = client.messages().create(params);

    if (response.stopReason().isPresent()
            && response.stopReason().get().equals(StopReason.PAUSE_TURN)) {
        MessageCreateParams continuationParams = MessageCreateParams.builder()
            .model("claude-opus-4-7")
            .maxTokens(1024L)
            .addUserMessage("Search for comprehensive information about quantum computing breakthroughs in 2025")
            .addMessage(response)
            .addTool(WebSearchTool20250305.builder()
                .maxUses(10L)
                .build())
            .build();

        Message continuation = client.messages().create(continuationParams);
        IO.println(continuation);
    } else {
        IO.println(response);
    }
}
```

```php PHP hidelines={1..6}
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$response = $client->messages->create(
    maxTokens: 1024,
    messages: [
        [
            'role' => 'user',
            'content' => 'Search for comprehensive information about quantum computing breakthroughs in 2025'
        ]
    ],
    model: 'claude-opus-4-7',
    tools: [
        [
            'type' => 'web_search_20250305',
            'name' => 'web_search',
            'max_uses' => 10
        ]
    ],
);

if ($response->stopReason === 'pause_turn') {
    $messages = [
        [
            'role' => 'user',
            'content' => 'Search for comprehensive information about quantum computing breakthroughs in 2025'
        ],
        [
            'role' => 'assistant',
            'content' => $response->content
        ]
    ];

    $continuation = $client->messages->create(
        maxTokens: 1024,
        messages: $messages,
        model: 'claude-opus-4-7',
        tools: [
            [
                'type' => 'web_search_20250305',
                'name' => 'web_search',
                'max_uses' => 10
            ]
        ],
    );

    echo $continuation;
} else {
    echo $response;
}
```

```ruby Ruby
require "anthropic"

client = Anthropic::Client.new

response = client.messages.create(
  model: "claude-opus-4-7",
  max_tokens: 1024,
  messages: [
    {
      role: "user",
      content:
        "Search for comprehensive information about quantum computing breakthroughs in 2025"
    }
  ],
  tools: [
    {
      type: "web_search_20250305",
      name: "web_search",
      max_uses: 10
    }
  ]
)

if response.stop_reason == :pause_turn
  messages = [
    {
      role: "user",
      content: "Search for comprehensive information about quantum computing breakthroughs in 2025"
    },
    {
      role: "assistant",
      content: response.content
    }
  ]

  continuation = client.messages.create(
    model: "claude-opus-4-7",
    max_tokens: 1024,
    messages: messages,
    tools: [
      {
        type: "web_search_20250305",
        name: "web_search",
        max_uses: 10
      }
    ]
  )

  puts continuation
else
  puts response
end
```
</CodeGroup>

When handling `pause_turn`:
- **Continue the conversation:** Pass the paused response back as-is in a subsequent request to let Claude continue its turn
- **Modify if needed:** You can optionally modify the content before continuing if you want to interrupt or redirect the conversation
- **Preserve tool state:** Include the same tools in the continuation request to maintain functionality

## ZDR and allowed_callers

The basic versions of web search (`web_search_20250305`) and web fetch (`web_fetch_20250910`) are eligible for [Zero Data Retention (ZDR)](/docs/en/build-with-claude/zero-data-retention).

The `_20260209` versions with dynamic filtering are **not** ZDR-eligible by default because dynamic filtering relies on code execution internally.

To use a `_20260209` server tool with ZDR, disable dynamic filtering by setting `"allowed_callers": ["direct"]` on the tool:

```json
{
  "type": "web_search_20260209",
  "name": "web_search",
  "allowed_callers": ["direct"]
}
```

This restricts the tool to direct invocation only, bypassing the internal code execution step.

<Note>
While the web fetch tool itself is ZDR-eligible, website publishers may retain any parameters passed to the URL if Claude fetches content from their site.
</Note>

## Domain filtering

Server tools that access the web accept `allowed_domains` and `blocked_domains` parameters to control which domains Claude can reach.

When using domain filters:

- Domains should not include the HTTP/HTTPS scheme (use `example.com` instead of `https://example.com`)
- Subdomains are automatically included (`example.com` covers `docs.example.com`)
- Specific subdomains restrict results to only that subdomain (`docs.example.com` returns only results from that subdomain, not from `example.com` or `api.example.com`)
- Subpaths are supported and match anything after the path (`example.com/blog` matches `example.com/blog/post-1`)
- You can use either `allowed_domains` or `blocked_domains`, but not both in the same request

**Wildcard support:**

- Only one wildcard (`*`) is allowed per domain entry, and it must appear after the domain part (in the path)
- Valid: `example.com/*`, `example.com/*/articles`
- Invalid: `*.example.com`, `ex*.com`, `example.com/*/news/*`

Invalid domain formats return an `invalid_tool_input` tool error.

<Note>
Request-level domain restrictions must be compatible with organization-level domain restrictions configured in the Console. Request-level domains can only further restrict domains, not override or expand beyond the organization-level list. If your request includes domains that conflict with organization settings, the API returns a validation error.
</Note>

<Warning>
Be aware that Unicode characters in domain names can create security vulnerabilities through homograph attacks, where visually similar characters from different scripts can bypass domain filters. For example, `аmazon.com` (using Cyrillic 'а') may appear identical to `amazon.com` but represents a different domain.

When configuring domain allow/block lists:
- Use ASCII-only domain names when possible
- Consider that URL parsers may handle Unicode normalization differently
- Test your domain filters with potential homograph variations
- Regularly audit your domain configurations for suspicious Unicode characters
</Warning>

## Dynamic filtering with code execution

The `_20260209` versions of web search and web fetch use code execution internally to apply dynamic filters against search results.

<Warning>
Including a standalone `code_execution` tool alongside `_20260209` versions of web tools creates two execution environments, which can confuse the model. Use one or the other, or pin both to the same version.
</Warning>

## Streaming server-tool events

Server-tool events stream as part of the normal SSE flow. The `server_tool_use` block and its result arrive as `content_block_start` and `content_block_delta` events, the same way text and client tool calls stream.

See [Streaming](/docs/en/build-with-claude/streaming) for the full event reference. Individual tool pages document tool-specific event names where they differ.

## Batch requests

All server tools support batch processing. See [Batch processing](/docs/en/build-with-claude/batch-processing).

## Next steps

<CardGroup cols={2}>
  <Card title="Web search" icon="magnifying-glass" href="/docs/en/agents-and-tools/tool-use/web-search-tool">
    Search the web and cite results.
  </Card>
  <Card title="Web fetch" icon="globe" href="/docs/en/agents-and-tools/tool-use/web-fetch-tool">
    Retrieve content from specific URLs.
  </Card>
  <Card title="Code execution" icon="terminal" href="/docs/en/agents-and-tools/tool-use/code-execution-tool">
    Run Python in a sandboxed container.
  </Card>
  <Card title="Tool search" icon="list-magnifying-glass" href="/docs/en/agents-and-tools/tool-use/tool-search-tool">
    Discover and load tools on demand.
  </Card>
</CardGroup>