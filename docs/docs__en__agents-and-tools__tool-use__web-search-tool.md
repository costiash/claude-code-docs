# Web search tool

---

The web search tool gives Claude direct access to real-time web content, allowing it to answer questions with up-to-date information beyond its knowledge cutoff. Claude automatically cites sources from search results as part of its answer.

The latest web search tool version (`web_search_20260209`) supports **dynamic filtering** with Claude Opus 4.6 and Sonnet 4.6. Claude can write and execute code to filter search results before they reach the context window, keeping only relevant information and discarding the rest. This leads to more accurate responses while reducing token consumption. The previous tool version (`web_search_20250305`) remains available without dynamic filtering.

<Note>
The basic web search tool (`web_search_20250305`) is eligible for [Zero Data Retention (ZDR)](/docs/en/build-with-claude/zero-data-retention).

The `web_search_20260209` version with dynamic filtering is **not** ZDR-eligible by default because dynamic filtering relies on code execution internally.

To use `web_search_20260209` with ZDR, disable dynamic filtering by setting `"allowed_callers": ["direct"]` on the tool:

```json
{
  "type": "web_search_20260209",
  "name": "web_search",
  "allowed_callers": ["direct"]
}
```

This restricts the tool to direct invocation only, bypassing the internal code execution step.
</Note>

## Supported models

Web search is available on:

- Claude Opus 4.6 (`claude-opus-4-6`)
- Claude Opus 4.5 (`claude-opus-4-5-20251101`)
- Claude Opus 4.1 (`claude-opus-4-1-20250805`)
- Claude Opus 4 (`claude-opus-4-20250514`)
- Claude Sonnet 4.6 (`claude-sonnet-4-6`)
- Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`)
- Claude Sonnet 4 (`claude-sonnet-4-20250514`)
- Claude Sonnet 3.7 ([deprecated](/docs/en/about-claude/model-deprecations)) (`claude-3-7-sonnet-20250219`)
- Claude Haiku 4.5 (`claude-haiku-4-5-20251001`)
- Claude Haiku 3.5 ([deprecated](/docs/en/about-claude/model-deprecations)) (`claude-3-5-haiku-latest`)

## How web search works

When you add the web search tool to your API request:

1. Claude decides when to search based on the prompt.
2. The API executes the searches and provides Claude with the results. This process may repeat multiple times throughout a single request.
3. At the end of its turn, Claude provides a final response with cited sources.

### Dynamic filtering with Opus 4.6 and Sonnet 4.6

Web search is a token-intensive task. With basic web search, Claude needs to pull search results into context, fetch full HTML from multiple websites, and reason over all of it before arriving at an answer. Often, much of this content is irrelevant, which can degrade response quality.

With the `web_search_20260209` tool version, Claude can write and execute code to post-process query results. Instead of reasoning over full HTML files, Claude dynamically filters search results before loading them into context, keeping only what's relevant and discarding the rest.

Dynamic filtering is particularly effective for:
- Searching through technical documentation
- Literature review and citation verification
- Technical research
- Response grounding and verification

<Note>
Dynamic filtering requires the [code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool) to be enabled. The improved web search tool is available on the Claude API and Microsoft Azure. On Google Vertex AI, the basic web search tool (without dynamic filtering) is available.
</Note>

To enable dynamic filtering, use the `web_search_20260209` tool version:

<CodeGroup>
```bash Shell
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "content-type: application/json" \
    --data '{
        "model": "claude-opus-4-6",
        "max_tokens": 4096,
        "messages": [
            {
                "role": "user",
                "content": "Search for the current prices of AAPL and GOOGL, then calculate which has a better P/E ratio."
            }
        ],
        "tools": [{
            "type": "web_search_20260209",
            "name": "web_search"
        }]
    }'
```

```python Python hidelines={1..2}
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    messages=[
        {
            "role": "user",
            "content": "Search for the current prices of AAPL and GOOGL, then calculate which has a better P/E ratio.",
        }
    ],
    tools=[{"type": "web_search_20260209", "name": "web_search"}],
)
print(response)
```

```typescript TypeScript nocheck hidelines={1..5,-3..-1}
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic();

async function main() {
  const response = await anthropic.messages.create({
    model: "claude-opus-4-6",
    max_tokens: 4096,
    messages: [
      {
        role: "user",
        content:
          "Search for the current prices of AAPL and GOOGL, then calculate which has a better P/E ratio."
      }
    ],
    tools: [{ type: "web_search_20260209", name: "web_search" }]
  });

  console.log(response);
}

main().catch(console.error);
```

```csharp C#
using System;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Messages;

class Program
{
    static async Task Main(string[] args)
    {
        AnthropicClient client = new();

        var parameters = new MessageCreateParams
        {
            Model = Model.ClaudeOpus4_6,
            MaxTokens = 4096,
            Messages = [new() { Role = Role.User, Content = "Search for the current prices of AAPL and GOOGL, then calculate which has a better P/E ratio." }],
            Tools = [new ToolUnion(new WebSearchTool20260209())]
        };

        var message = await client.Messages.Create(parameters);
        Console.WriteLine(message);
    }
}
```

```go Go hidelines={1..11,-1}
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
		Model:     anthropic.ModelClaudeOpus4_6,
		MaxTokens: 4096,
		Messages: []anthropic.MessageParam{
			anthropic.NewUserMessage(anthropic.NewTextBlock("Search for the current prices of AAPL and GOOGL, then calculate which has a better P/E ratio.")),
		},
		Tools: []anthropic.ToolUnionParam{
			{OfWebSearchTool20260209: &anthropic.WebSearchTool20260209Param{}},
		},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(response)
}
```

```java Java hidelines={1..5,7..9,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;
import com.anthropic.models.messages.WebSearchTool20260209;

public class WebSearchExample {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCreateParams params = MessageCreateParams.builder()
            .model(Model.CLAUDE_OPUS_4_6)
            .maxTokens(4096L)
            .addUserMessage("Search for the current prices of AAPL and GOOGL, then calculate which has a better P/E ratio.")
            .addTool(WebSearchTool20260209.builder().build())
            .build();

        Message response = client.messages().create(params);
        System.out.println(response);
    }
}
```

```php PHP hidelines={1..4}
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$message = $client->messages->create(
    maxTokens: 4096,
    messages: [
        ['role' => 'user', 'content' => 'Search for the current prices of AAPL and GOOGL, then calculate which has a better P/E ratio.'],
    ],
    model: 'claude-opus-4-6',
    tools: [
        [
            'type' => 'web_search_20260209',
            'name' => 'web_search',
        ],
    ],
);

echo $message;
```

```ruby Ruby hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

message = client.messages.create(
  model: "claude-opus-4-6",
  max_tokens: 4096,
  messages: [
    { role: "user", content: "Search for the current prices of AAPL and GOOGL, then calculate which has a better P/E ratio." }
  ],
  tools: [{
    type: "web_search_20260209",
    name: "web_search"
  }]
)
puts message
```
</CodeGroup>

## How to use web search

<Note>
Your organization's administrator must enable web search in the [Claude Console](/settings/privacy).
</Note>

Provide the web search tool in your API request:

<CodeGroup>
```bash Shell
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "content-type: application/json" \
    --data '{
        "model": "claude-opus-4-6",
        "max_tokens": 1024,
        "messages": [
            {
                "role": "user",
                "content": "What is the weather in NYC?"
            }
        ],
        "tools": [{
            "type": "web_search_20250305",
            "name": "web_search",
            "max_uses": 5
        }]
    }'
```

```python Python hidelines={1..2}
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "What's the weather in NYC?"}],
    tools=[{"type": "web_search_20250305", "name": "web_search", "max_uses": 5}],
)
print(response)
```

```typescript TypeScript hidelines={1..5,-3..-1}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

async function main() {
  const response = await client.messages.create({
    model: "claude-opus-4-6",
    max_tokens: 1024,
    messages: [
      {
        role: "user",
        content: "What's the weather in NYC?"
      }
    ],
    tools: [
      {
        type: "web_search_20250305",
        name: "web_search",
        max_uses: 5
      }
    ]
  });

  console.log(response);
}

main().catch(console.error);
```

```csharp C#
using System;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Messages;

class Program
{
    static async Task Main(string[] args)
    {
        AnthropicClient client = new();

        var parameters = new MessageCreateParams
        {
            Model = Model.ClaudeOpus4_6,
            MaxTokens = 1024,
            Messages = [new() { Role = Role.User, Content = "What's the weather in NYC?" }],
            Tools = [new ToolUnion(new WebSearchTool20250305() { MaxUses = 5 })]
        };

        var message = await client.Messages.Create(parameters);
        Console.WriteLine(message);
    }
}
```

```go Go hidelines={1..11,-1}
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
		Model:     anthropic.ModelClaudeOpus4_6,
		MaxTokens: 1024,
		Messages: []anthropic.MessageParam{
			anthropic.NewUserMessage(anthropic.NewTextBlock("What's the weather in NYC?")),
		},
		Tools: []anthropic.ToolUnionParam{
			{OfWebSearchTool20250305: &anthropic.WebSearchTool20250305Param{
				MaxUses: anthropic.Int(5),
			}},
		},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(response)
}
```

```java Java hidelines={1..5,7..9,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;
import com.anthropic.models.messages.WebSearchTool20250305;

public class WebSearchExample {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCreateParams params = MessageCreateParams.builder()
            .model(Model.CLAUDE_OPUS_4_6)
            .maxTokens(1024L)
            .addUserMessage("What's the weather in NYC?")
            .addTool(WebSearchTool20250305.builder()
                .maxUses(5L)
                .build())
            .build();

        Message response = client.messages().create(params);
        System.out.println(response);
    }
}
```

```php PHP hidelines={1..4}
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$message = $client->messages->create(
    maxTokens: 1024,
    messages: [
        ['role' => 'user', 'content' => "What's the weather in NYC?"],
    ],
    model: 'claude-opus-4-6',
    tools: [
        [
            'type' => 'web_search_20250305',
            'name' => 'web_search',
            'max_uses' => 5,
        ],
    ],
);

echo $message;
```

```ruby Ruby hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

message = client.messages.create(
  model: "claude-opus-4-6",
  max_tokens: 1024,
  messages: [
    { role: "user", content: "What's the weather in NYC?" }
  ],
  tools: [{
    type: "web_search_20250305",
    name: "web_search",
    max_uses: 5
  }]
)
puts message
```
</CodeGroup>

### Tool definition

The web search tool supports the following parameters:

```json JSON
{
  "type": "web_search_20250305",
  "name": "web_search",

  // Optional: Limit the number of searches per request
  "max_uses": 5,

  // Optional: Only include results from these domains
  "allowed_domains": ["example.com", "trusteddomain.org"],

  // Optional: Never include results from these domains
  "blocked_domains": ["untrustedsource.com"],

  // Optional: Localize search results
  "user_location": {
    "type": "approximate",
    "city": "San Francisco",
    "region": "California",
    "country": "US",
    "timezone": "America/Los_Angeles"
  }
}
```

#### Max uses

The `max_uses` parameter limits the number of searches performed. If Claude attempts more searches than allowed, the `web_search_tool_result` is an error with the `max_uses_exceeded` error code.

#### Domain filtering

When using domain filters:

- Domains should not include the HTTP/HTTPS scheme (use `example.com` instead of `https://example.com`)
- Subdomains are automatically included (`example.com` covers `docs.example.com`)
- Specific subdomains restrict results to only that subdomain (`docs.example.com` returns only results from that subdomain, not from `example.com` or `api.example.com`)
- Subpaths are supported and match anything after the path (`example.com/blog` matches `example.com/blog/post-1`)
- You can use either `allowed_domains` or `blocked_domains`, but not both in the same request.

**Wildcard support:**

- Only one wildcard (`*`) is allowed per domain entry, and it must appear after the domain part (in the path)
- Valid: `example.com/*`, `example.com/*/articles`
- Invalid: `*.example.com`, `ex*.com`, `example.com/*/news/*`

Invalid domain formats return an `invalid_tool_input` tool error.

<Note>
Request-level domain restrictions must be compatible with organization-level domain restrictions configured in the Console. Request-level domains can only further restrict domains, not override or expand beyond the organization-level list. If your request includes domains that conflict with organization settings, the API returns a validation error.
</Note>

#### Localization

The `user_location` parameter allows you to localize search results based on a user's location.

- `type`: The type of location (must be `approximate`)
- `city`: The city name
- `region`: The region or state
- `country`: The country
- `timezone`: The [IANA timezone ID](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

### Response

Here's an example response structure:

```json
{
  "role": "assistant",
  "content": [
    // 1. Claude's decision to search
    {
      "type": "text",
      "text": "I'll search for when Claude Shannon was born."
    },
    // 2. The search query used
    {
      "type": "server_tool_use",
      "id": "srvtoolu_01WYG3ziw53XMcoyKL4XcZmE",
      "name": "web_search",
      "input": {
        "query": "claude shannon birth date"
      }
    },
    // 3. Search results
    {
      "type": "web_search_tool_result",
      "tool_use_id": "srvtoolu_01WYG3ziw53XMcoyKL4XcZmE",
      "content": [
        {
          "type": "web_search_result",
          "url": "https://en.wikipedia.org/wiki/Claude_Shannon",
          "title": "Claude Shannon - Wikipedia",
          "encrypted_content": "EqgfCioIARgBIiQ3YTAwMjY1Mi1mZjM5LTQ1NGUtODgxNC1kNjNjNTk1ZWI3Y...",
          "page_age": "April 30, 2025"
        }
      ]
    },
    {
      "text": "Based on the search results, ",
      "type": "text"
    },
    // 4. Claude's response with citations
    {
      "text": "Claude Shannon was born on April 30, 1916, in Petoskey, Michigan",
      "type": "text",
      "citations": [
        {
          "type": "web_search_result_location",
          "url": "https://en.wikipedia.org/wiki/Claude_Shannon",
          "title": "Claude Shannon - Wikipedia",
          "encrypted_index": "Eo8BCioIAhgBIiQyYjQ0OWJmZi1lNm..",
          "cited_text": "Claude Elwood Shannon (April 30, 1916 – February 24, 2001) was an American mathematician, electrical engineer, computer scientist, cryptographer and i..."
        }
      ]
    }
  ],
  "id": "msg_a930390d3a",
  "usage": {
    "input_tokens": 6039,
    "output_tokens": 931,
    "server_tool_use": {
      "web_search_requests": 1
    }
  },
  "stop_reason": "end_turn"
}
```

#### Search results

Search results include:

- `url`: The URL of the source page
- `title`: The title of the source page
- `page_age`: When the site was last updated
- `encrypted_content`: Encrypted content that must be passed back in multi-turn conversations for citations

#### Citations

Citations are always enabled for web search, and each `web_search_result_location` includes:

- `url`: The URL of the cited source
- `title`: The title of the cited source
- `encrypted_index`: A reference that must be passed back for multi-turn conversations.
- `cited_text`: Up to 150 characters of the cited content

The web search citation fields `cited_text`, `title`, and `url` do not count towards input or output token usage.

<Note>
  When displaying API outputs directly to end users, citations must be included to the original source. If you are making modifications to API outputs, including by reprocessing and/or combining them with your own material before displaying them to end users, display citations as appropriate based on consultation with your legal team.
</Note>

#### Errors

When the web search tool encounters an error (such as hitting rate limits), the Claude API still returns a 200 (success) response. The error is represented within the response body using the following structure:

```json
{
  "type": "web_search_tool_result",
  "tool_use_id": "servertoolu_a93jad",
  "content": {
    "type": "web_search_tool_result_error",
    "error_code": "max_uses_exceeded"
  }
}
```

These are the possible error codes:

- `too_many_requests`: Rate limit exceeded
- `invalid_input`: Invalid search query parameter
- `max_uses_exceeded`: Maximum web search tool uses exceeded
- `query_too_long`: Query exceeds maximum length
- `unavailable`: An internal error occurred

#### `pause_turn` stop reason

The response may include a `pause_turn` stop reason, which indicates that the API paused a long-running turn. You may provide the response back as-is in a subsequent request to let Claude continue its turn, or modify the content if you wish to interrupt the conversation.

## Prompt caching

Web search works with [prompt caching](/docs/en/build-with-claude/prompt-caching). To enable prompt caching, add at least one `cache_control` breakpoint in your request. The system will automatically cache up until the last `web_search_tool_result` block when executing the tool.

For multi-turn conversations, set a `cache_control` breakpoint on or after the last `web_search_tool_result` block to reuse cached content.

For example, to use prompt caching with web search for a multi-turn conversation:

<CodeGroup>
```python Python hidelines={1..2}
import anthropic

client = anthropic.Anthropic()

# First request with web search and cache breakpoint
messages = [
    {"role": "user", "content": "What's the current weather in San Francisco today?"}
]

response1 = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=messages,
    tools=[
        {
            "type": "web_search_20250305",
            "name": "web_search",
            "user_location": {
                "type": "approximate",
                "city": "San Francisco",
                "region": "California",
                "country": "US",
                "timezone": "America/Los_Angeles",
            },
        }
    ],
)

# Add Claude's response to the conversation
messages.append({"role": "assistant", "content": response1.content})

# Second request with cache breakpoint after the search results
messages.append(
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Should I expect rain later this week?",
                "cache_control": {"type": "ephemeral"},
            }
        ],
    }
)

response2 = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=messages,
    tools=[
        {
            "type": "web_search_20250305",
            "name": "web_search",
            "user_location": {
                "type": "approximate",
                "city": "San Francisco",
                "region": "California",
                "country": "US",
                "timezone": "America/Los_Angeles",
            },
        }
    ],
)
# The second response will benefit from cached search results
# while still being able to perform new searches if needed
print(f"Cache read tokens: {response2.usage.cache_read_input_tokens or 0}")
```

```typescript TypeScript hidelines={1..5,-3..-1}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

async function main() {
  const messages: Anthropic.MessageParam[] = [
    { role: "user", content: "What's the current weather in San Francisco today?" }
  ];

  const response1 = await client.messages.create({
    model: "claude-opus-4-6",
    max_tokens: 1024,
    messages: messages,
    tools: [
      {
        type: "web_search_20250305",
        name: "web_search",
        user_location: {
          type: "approximate",
          city: "San Francisco",
          region: "California",
          country: "US",
          timezone: "America/Los_Angeles"
        }
      }
    ]
  });

  messages.push({ role: "assistant", content: response1.content });

  messages.push({
    role: "user",
    content: [
      {
        type: "text",
        text: "Should I expect rain later this week?",
        cache_control: { type: "ephemeral" }
      }
    ]
  });

  const response2 = await client.messages.create({
    model: "claude-opus-4-6",
    max_tokens: 1024,
    messages: messages,
    tools: [
      {
        type: "web_search_20250305",
        name: "web_search",
        user_location: {
          type: "approximate",
          city: "San Francisco",
          region: "California",
          country: "US",
          timezone: "America/Los_Angeles"
        }
      }
    ]
  });

  console.log(`Cache read tokens: ${response2.usage.cache_read_input_tokens || 0}`);
}

main().catch(console.error);
```

```csharp C# nocheck
using System.Collections.Generic;
using Anthropic;
using Anthropic.Models.Messages;

AnthropicClient client = new();

var webSearchTool = new ToolUnion(new WebSearchTool20250305()
{
    UserLocation = new UserLocation()
    {
        Type = "approximate",
        City = "San Francisco",
        Region = "California",
        Country = "US",
        Timezone = "America/Los_Angeles",
    },
});

var parameters1 = new MessageCreateParams
{
    Model = Model.ClaudeOpus4_6,
    MaxTokens = 1024,
    Messages = [new() { Role = Role.User, Content = "What's the current weather in San Francisco today?" }],
    Tools = [webSearchTool]
};

var response1 = await client.Messages.Create(parameters1);

var parameters2 = new MessageCreateParams
{
    Model = Model.ClaudeOpus4_6,
    MaxTokens = 1024,
    Messages = [
        new() { Role = Role.User, Content = "What's the current weather in San Francisco today?" },
        new() { Role = Role.Assistant, Content = response1.Content },
        new()
        {
            Role = Role.User,
            Content = new MessageParamContent(new List<ContentBlockParam>
            {
                new ContentBlockParam(new TextBlockParam("Should I expect rain later this week?")
                {
                    CacheControl = new CacheControlEphemeral(),
                }),
            }),
        },
    ],
    Tools = [webSearchTool]
};

var response2 = await client.Messages.Create(parameters2);

Console.WriteLine($"Cache read tokens: {response2.Usage.CacheReadInputTokens ?? 0}");
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

	webSearchTool := anthropic.ToolUnionParam{
		OfWebSearchTool20250305: &anthropic.WebSearchTool20250305Param{
			UserLocation: anthropic.WebSearchTool20250305UserLocationParam{
				City:     anthropic.String("San Francisco"),
				Region:   anthropic.String("California"),
				Country:  anthropic.String("US"),
				Timezone: anthropic.String("America/Los_Angeles"),
			},
		},
	}

	messages := []anthropic.MessageParam{
		anthropic.NewUserMessage(anthropic.NewTextBlock("What's the current weather in San Francisco today?")),
	}

	response1, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
		Model:     anthropic.ModelClaudeOpus4_6,
		MaxTokens: 1024,
		Messages:  messages,
		Tools:     []anthropic.ToolUnionParam{webSearchTool},
	})
	if err != nil {
		log.Fatal(err)
	}

	// Convert assistant response to a message param
	messages = append(messages, response1.ToParam())

	// Second request with cache breakpoint after the search results
	followUp := anthropic.NewTextBlock("Should I expect rain later this week?")
	followUp.OfText.CacheControl = anthropic.NewCacheControlEphemeralParam()
	messages = append(messages, anthropic.NewUserMessage(followUp))

	response2, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
		Model:     anthropic.ModelClaudeOpus4_6,
		MaxTokens: 1024,
		Messages:  messages,
		Tools:     []anthropic.ToolUnionParam{webSearchTool},
	})
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("Cache read tokens: %d\n", response2.Usage.CacheReadInputTokens)
}
```

```java Java hidelines={1..2,4..9,12..16,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.CacheControlEphemeral;
import com.anthropic.models.messages.ContentBlockParam;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.MessageParam;
import com.anthropic.models.messages.Model;
import com.anthropic.models.messages.TextBlockParam;
import com.anthropic.models.messages.UserLocation;
import com.anthropic.models.messages.WebSearchTool20250305;
import java.util.ArrayList;
import java.util.List;

public class WebSearchWithCache {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        WebSearchTool20250305 webSearchTool = WebSearchTool20250305.builder()
            .userLocation(UserLocation.builder()
                .city("San Francisco")
                .region("California")
                .country("US")
                .timezone("America/Los_Angeles")
                .build())
            .build();

        List<MessageParam> messages = new ArrayList<>();
        messages.add(MessageParam.builder()
            .role(MessageParam.Role.USER)
            .content("What's the current weather in San Francisco today?")
            .build());

        Message response1 = client.messages().create(
            MessageCreateParams.builder()
                .model(Model.CLAUDE_OPUS_4_6)
                .maxTokens(1024L)
                .messages(messages)
                .addTool(webSearchTool)
                .build());

        messages.add(response1.toParam());

        messages.add(MessageParam.builder()
            .role(MessageParam.Role.USER)
            .contentOfBlockParams(List.of(
                ContentBlockParam.ofText(
                    TextBlockParam.builder()
                        .text("Should I expect rain later this week?")
                        .cacheControl(CacheControlEphemeral.builder().build())
                        .build())
            ))
            .build());

        Message response2 = client.messages().create(
            MessageCreateParams.builder()
                .model(Model.CLAUDE_OPUS_4_6)
                .maxTokens(1024L)
                .messages(messages)
                .addTool(webSearchTool)
                .build());

        System.out.println("Cache read tokens: " +
            response2.usage().cacheReadInputTokens().orElse(0L));
    }
}
```

```php PHP hidelines={1..4} nocheck
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$messages = [
    ['role' => 'user', 'content' => "What's the current weather in San Francisco today?"]
];

$response1 = $client->messages->create(
    maxTokens: 1024,
    messages: $messages,
    model: 'claude-opus-4-6',
    tools: [
        [
            'type' => 'web_search_20250305',
            'name' => 'web_search',
            'user_location' => [
                'type' => 'approximate',
                'city' => 'San Francisco',
                'region' => 'California',
                'country' => 'US',
                'timezone' => 'America/Los_Angeles',
            ],
        ],
    ],
);

$messages[] = ['role' => 'assistant', 'content' => $response1->content];

$messages[] = [
    'role' => 'user',
    'content' => [[
        'type' => 'text',
        'text' => 'Should I expect rain later this week?',
        'cache_control' => ['type' => 'ephemeral'],
    ]],
];

$response2 = $client->messages->create(
    maxTokens: 1024,
    messages: $messages,
    model: 'claude-opus-4-6',
    tools: [
        [
            'type' => 'web_search_20250305',
            'name' => 'web_search',
            'user_location' => [
                'type' => 'approximate',
                'city' => 'San Francisco',
                'region' => 'California',
                'country' => 'US',
                'timezone' => 'America/Los_Angeles',
            ],
        ],
    ],
);

echo "Cache read tokens: " . ($response2->usage->cacheReadInputTokens ?? 0) . "\n";
```

```ruby Ruby hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

messages = [
  { role: "user", content: "What's the current weather in San Francisco today?" }
]

response1 = client.messages.create(
  model: "claude-opus-4-6",
  max_tokens: 1024,
  messages: messages,
  tools: [
    {
      type: "web_search_20250305",
      name: "web_search",
      user_location: {
        type: "approximate",
        city: "San Francisco",
        region: "California",
        country: "US",
        timezone: "America/Los_Angeles"
      }
    }
  ]
)

messages << { role: "assistant", content: response1.content }

messages << {
  role: "user",
  content: [
    {
      type: "text",
      text: "Should I expect rain later this week?",
      cache_control: { type: "ephemeral" }
    }
  ]
}

response2 = client.messages.create(
  model: "claude-opus-4-6",
  max_tokens: 1024,
  messages: messages,
  tools: [
    {
      type: "web_search_20250305",
      name: "web_search",
      user_location: {
        type: "approximate",
        city: "San Francisco",
        region: "California",
        country: "US",
        timezone: "America/Los_Angeles"
      }
    }
  ]
)

puts "Cache read tokens: #{response2.usage.cache_read_input_tokens || 0}"
```

</CodeGroup>

## Streaming

With streaming enabled, you'll receive search events as part of the stream. There will be a pause while the search executes:

```sse
event: message_start
data: {"type": "message_start", "message": {"id": "msg_abc123", "type": "message"}}

event: content_block_start
data: {"type": "content_block_start", "index": 0, "content_block": {"type": "text", "text": ""}}

// Claude's decision to search

event: content_block_start
data: {"type": "content_block_start", "index": 1, "content_block": {"type": "server_tool_use", "id": "srvtoolu_xyz789", "name": "web_search"}}

// Search query streamed
event: content_block_delta
data: {"type": "content_block_delta", "index": 1, "delta": {"type": "input_json_delta", "partial_json": "{\"query\":\"latest quantum computing breakthroughs 2025\"}"}}

// Pause while search executes

// Search results streamed
event: content_block_start
data: {"type": "content_block_start", "index": 2, "content_block": {"type": "web_search_tool_result", "tool_use_id": "srvtoolu_xyz789", "content": [{"type": "web_search_result", "title": "Quantum Computing Breakthroughs in 2025", "url": "https://example.com"}]}}

// Claude's response with citations (omitted in this example)
```

## Batch requests

You can include the web search tool in the [Messages Batches API](/docs/en/build-with-claude/batch-processing). Web search tool calls through the Messages Batches API are priced the same as those in regular Messages API requests.

## Usage and pricing

Web search usage is charged in addition to token usage:

```json
"usage": {
  "input_tokens": 105,
  "output_tokens": 6039,
  "cache_read_input_tokens": 7123,
  "cache_creation_input_tokens": 7345,
  "server_tool_use": {
    "web_search_requests": 1
  }
}
```

Web search is available on the Claude API for **$10 per 1,000 searches**, plus standard token costs for search-generated content. Web search results retrieved throughout a conversation are counted as input tokens, in search iterations executed during a single turn and in subsequent conversation turns.

Each web search counts as one use, regardless of the number of results returned. If an error occurs during web search, the web search will not be billed.