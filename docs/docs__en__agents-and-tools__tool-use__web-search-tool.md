# Web search tool

Give Claude access to current web content with cited sources, optional dynamic filtering, and domain controls.

---

<Note>
  For how zero data retention (ZDR) applies to this feature, see [API and data retention](/docs/en/manage-claude/api-and-data-retention).
</Note>

The web search tool gives Claude direct access to real-time web content, allowing it to answer questions with up-to-date information beyond its knowledge cutoff. The response includes citations for sources drawn from search results.

With `web_search_20260209` and later versions, Claude can write and run code that filters the search results before they reach the context window (**dynamic filtering**), keeping only relevant information. Dynamic filtering is available with Claude Fable 5, Claude Opus 4.8, Claude Mythos 5, [Claude Mythos Preview](https://anthropic.com/glasswing), Claude Opus 4.7, Claude Opus 4.6, Claude Sonnet 5, and Claude Sonnet 4.6.

Three versions of the web search tool are available:

* `web_search_20250305`: basic web search
* `web_search_20260209`: adds [dynamic filtering](#dynamic-filtering)
* `web_search_20260318`: adds [response inclusion](#response-inclusion) control for agentic workflows

The examples on this page use `web_search_20250305` for basic search and `web_search_20260318` for dynamic filtering.

<Note>
  For [Claude Mythos Preview](https://anthropic.com/glasswing), web search is supported on the Claude API, Google Cloud, and Microsoft Foundry. Web search is not available for Mythos Preview on Amazon Bedrock or [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws).
</Note>

For web search's Zero Data Retention eligibility and the related `allowed_callers` configuration, see [Server tools](/docs/en/agents-and-tools/tool-use/server-tools#zdr-and-allowed-callers).

For model support, see the [Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference).

## How web search works

When you add the web search tool to your API request:

1. Claude determines when to search based on the prompt.
2. The API runs the searches and provides Claude with the results. This process can repeat multiple times throughout a single request.
3. At the end of its turn, Claude provides a final response with cited sources.

### When Claude searches

Claude searches when the request depends on information that is current, changing, or outside its training data:

* Recent events, news, or announcements
* Current prices, rates, scores, or statistics
* Information about specific organizations, people, or products that might have changed
* Explicit requests to search or look something up

Claude answers directly without searching when the request draws on stable knowledge:

* Established facts, math, science fundamentals, or coding concepts
* Creative writing or brainstorming
* Analysis of content already provided in the conversation
* Conversational turns and greetings

Triggering is steerable through your system prompt: you can encourage Claude to search more readily or to prefer answering directly. For a hard constraint, use `max_uses` to cap the number of searches for each request.

### Dynamic filtering

With basic web search, every search result is loaded into Claude's context window, and much of that content can be irrelevant to the request. With `web_search_20260209` or later, Claude instead writes and runs code that filters the results first, so only relevant content reaches the context window. This reduces token use on search-heavy requests.

Dynamic filtering runs web search from inside [code execution](/docs/en/agents-and-tools/tool-use/code-execution-tool): on `web_search_20260209` and later, the tool's `allowed_callers` field defaults to `["code_execution_20260120"]`, and when dynamic filtering runs, the API provisions the code execution it needs for the request automatically. You don't need to add the code execution tool to `tools` yourself. There are no additional charges for code execution calls made this way beyond the standard token costs.

To call web search directly, without dynamic filtering, set `allowed_callers: ["direct"]`. Models that don't support programmatic tool calling require this setting. Without it, the API returns a 400 error that tells you to set it.

<Note>
  The web search tool (with and without dynamic filtering) is available on the Claude API, [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws), and [Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry). On Microsoft Foundry, web search requires a [Hosted on Anthropic deployment](/docs/en/build-with-claude/claude-in-microsoft-foundry#additional-features-not-supported-when-hosted-on-azure). On Google Cloud, only the basic web search tool (without dynamic filtering) is available. Web search is not available on Amazon Bedrock.
</Note>

The following examples use `web_search_20260318`:

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-opus-4-8",
      "max_tokens": 4096,
      "messages": [
        {
          "role": "user",
          "content": "Search for the current prices of AAPL and GOOGL, then calculate which has a better P/E ratio."
        }
      ],
      "tools": [{
        "type": "web_search_20260318",
        "name": "web_search"
      }]
    }'
  ```

  ```bash CLI
  ant messages create <<'YAML'
  model: claude-opus-4-8
  max_tokens: 4096
  messages:
    - role: user
      content: >-
        Search for the current prices of AAPL and GOOGL, then calculate
        which has a better P/E ratio.
  tools:
    - type: web_search_20260318
      name: web_search
  YAML
  ```

  ```python Python
  client = anthropic.Anthropic()

  response = client.messages.create(
      model="claude-opus-4-8",
      max_tokens=4096,
      messages=[
          {
              "role": "user",
              "content": "Search for the current prices of AAPL and GOOGL, then calculate which has a better P/E ratio.",
          }
      ],
      tools=[{"type": "web_search_20260318", "name": "web_search"}],
  )
  print(response)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const response = await client.messages.create({
    model: "claude-opus-4-8",
    max_tokens: 4096,
    messages: [
      {
        role: "user",
        content:
          "Search for the current prices of AAPL and GOOGL, then calculate which has a better P/E ratio."
      }
    ],
    tools: [{ type: "web_search_20260318", name: "web_search" }]
  });

  console.log(response);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var parameters = new MessageCreateParams
  {
      Model = Model.ClaudeOpus4_8,
      MaxTokens = 4096,
      Messages = [new() { Role = Role.User, Content = "Search for the current prices of AAPL and GOOGL, then calculate which has a better P/E ratio." }],
      Tools = [new ToolUnion(new WebSearchTool20260318())]
  };

  var message = await client.Messages.Create(parameters);
  Console.WriteLine(message);
  ```

  ```go Go
  client := anthropic.NewClient()

  response, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
  	Model:     anthropic.ModelClaudeOpus4_8,
  	MaxTokens: 4096,
  	Messages: []anthropic.MessageParam{
  		anthropic.NewUserMessage(anthropic.NewTextBlock("Search for the current prices of AAPL and GOOGL, then calculate which has a better P/E ratio.")),
  	},
  	Tools: []anthropic.ToolUnionParam{
  		{OfWebSearchTool20260318: &anthropic.WebSearchTool20260318Param{}},
  	},
  })
  if err != nil {
  	log.Fatal(err)
  }
  fmt.Println(response)
  ```

  ```java Java
  import com.anthropic.models.messages.WebSearchTool20260318;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      MessageCreateParams params = MessageCreateParams.builder()
          .model(Model.CLAUDE_OPUS_4_8)
          .maxTokens(4096L)
          .addUserMessage("Search for the current prices of AAPL and GOOGL, then calculate which has a better P/E ratio.")
          .addTool(WebSearchTool20260318.builder().build())
          .build();

      Message response = client.messages().create(params);
      IO.println(response);
  }
  ```

  ```php PHP
  $client = new Client();

  $message = $client->messages->create(
      maxTokens: 4096,
      messages: [
          ['role' => 'user', 'content' => 'Search for the current prices of AAPL and GOOGL, then calculate which has a better P/E ratio.'],
      ],
      model: 'claude-opus-4-8',
      tools: [
          [
              'type' => 'web_search_20260318',
              'name' => 'web_search',
          ],
      ],
  );

  echo $message;
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  message = client.messages.create(
    model: "claude-opus-4-8",
    max_tokens: 4096,
    messages: [
      { role: "user", content: "Search for the current prices of AAPL and GOOGL, then calculate which has a better P/E ratio." }
    ],
    tools: [{
      type: "web_search_20260318",
      name: "web_search"
    }]
  )
  puts message
  ```
</CodeGroup>

## How to use web search

<Note>
  Web search is enabled for your organization unless an administrator has disabled it in the [Claude Console](/settings/privacy), where they can also restrict which domains it searches. If it's disabled, a request that includes the tool fails with a 400 `invalid_request_error` that says web search is not enabled, rather than an [error code](#errors) inside a search result.
</Note>

Provide the web search tool in your API request:

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-opus-4-8",
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

  ```bash CLI
  ant messages create \
    --model claude-opus-4-8 \
    --max-tokens 1024 \
    --message '{role: user, content: What is the weather in NYC?}' \
    --tool '{type: web_search_20250305, name: web_search, max_uses: 5}'
  ```

  ```python Python
  client = anthropic.Anthropic()

  response = client.messages.create(
      model="claude-opus-4-8",
      max_tokens=1024,
      messages=[{"role": "user", "content": "What's the weather in NYC?"}],
      tools=[{"type": "web_search_20250305", "name": "web_search", "max_uses": 5}],
  )
  print(response)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const response = await client.messages.create({
    model: "claude-opus-4-8",
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
  ```

  ```csharp C#
  AnthropicClient client = new();

  var parameters = new MessageCreateParams
  {
      Model = Model.ClaudeOpus4_8,
      MaxTokens = 1024,
      Messages = [new() { Role = Role.User, Content = "What's the weather in NYC?" }],
      Tools = [new ToolUnion(new WebSearchTool20250305() { MaxUses = 5 })]
  };

  var message = await client.Messages.Create(parameters);
  Console.WriteLine(message);
  ```

  ```go Go
  client := anthropic.NewClient()

  response, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
  	Model:     anthropic.ModelClaudeOpus4_8,
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
  ```

  ```java Java
  import com.anthropic.models.messages.WebSearchTool20250305;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      MessageCreateParams params = MessageCreateParams.builder()
          .model(Model.CLAUDE_OPUS_4_8)
          .maxTokens(1024L)
          .addUserMessage("What's the weather in NYC?")
          .addTool(WebSearchTool20250305.builder()
              .maxUses(5L)
              .build())
          .build();

      Message response = client.messages().create(params);
      IO.println(response);
  }
  ```

  ```php PHP
  $client = new Client();

  $message = $client->messages->create(
      maxTokens: 1024,
      messages: [
          ['role' => 'user', 'content' => "What's the weather in NYC?"],
      ],
      model: 'claude-opus-4-8',
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

  ```ruby Ruby
  client = Anthropic::Client.new

  message = client.messages.create(
    model: "claude-opus-4-8",
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

## Tool definition

The web search tool supports the following parameters:

```json JSON
{
  "type": "web_search_20250305",
  "name": "web_search",

  // Optional: Limit the number of searches per request
  "max_uses": 5,

  // Optional: Only include results from these domains.
  // Use allowed_domains or blocked_domains, not both.
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

All web search tool versions accept `allowed_callers`, which controls whether Claude calls web search directly or from code execution through [dynamic filtering](#dynamic-filtering). On `web_search_20260209` and later it defaults to `["code_execution_20260120"]` instead of `["direct"]`. See [Server tools](/docs/en/agents-and-tools/tool-use/server-tools#zdr-and-allowed-callers) for how to configure it. `web_search_20260318` and later also accept [`response_inclusion`](#response-inclusion).

### Max uses

The `max_uses` parameter limits the number of searches performed. If Claude attempts more searches than allowed, the `web_search_tool_result` is an error with the `max_uses_exceeded` error code.

Simple factual queries typically use 1–3 searches; comparative or multientity research can use 10 or more. For guidance on choosing a value, see [Server tools](/docs/en/agents-and-tools/tool-use/server-tools).

### Domain filtering

Provide `allowed_domains` or `blocked_domains`, not both. If a request includes both, the API returns a 400 error. Entries are bare domains with an optional path, for example `example.com` or `example.com/blog`, without a scheme.

For the full domain filtering rules, see [Domain filtering](/docs/en/agents-and-tools/tool-use/server-tools#domain-filtering) in the Server tools guide.

### Localization

The `user_location` parameter allows you to localize search results based on a user's location. Provide at least one of `city`, `region`, `country`, or `timezone`.

* `type`: The type of location (must be `approximate`)
* `city`: The city name
* `region`: The region or state
* `country`: The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. The API rejects unsupported country codes with a 400 error.
* `timezone`: The [IANA timezone ID](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

### Response inclusion

<Note>
  Requires `web_search_20260318` or later.
</Note>

The `response_inclusion` parameter controls how search result blocks appear in the API response when the result was consumed by a completed [code execution](/docs/en/agents-and-tools/tool-use/code-execution-tool) call in the same turn. Set `"response_inclusion": "excluded"` to drop those nested `server_tool_use` and result block pairs entirely from the response, reducing output token costs for agentic workflows that don't need to echo raw search content back to the client. The default is `"full"`. Results from direct calls, or from code execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

```json JSON
{
  "tools": [
    {
      "type": "web_search_20260318",
      "name": "web_search",
      "response_inclusion": "excluded"
    }
  ]
}
```

## Response

Here's an example response structure:

```json Output
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

This example shows a direct search. When a search runs through [dynamic filtering](#dynamic-filtering), the response also contains the [code execution tool's](/docs/en/agents-and-tools/tool-use/code-execution-tool) result blocks, and each nested `server_tool_use` and `web_search_tool_result` pair carries a `caller` field identifying the code execution call that made it.

### Search results

Search results include:

* `url`: The URL of the source page
* `title`: The title of the source page
* `page_age`: When the site was last updated
* `encrypted_content`: Encrypted content that you must pass back in multi-turn conversations

To continue a conversation that contains search results, send the assistant's content blocks back exactly as you received them, including each result's `encrypted_content`. The API decrypts that content on later turns to restore the search results in Claude's context. If `encrypted_content` is missing or modified, the request fails with a 400 validation error.

### Citations

Citations are always enabled for web search, and each `web_search_result_location` includes:

* `url`: The URL of the cited source
* `title`: The title of the cited source
* `encrypted_index`: A reference that must be passed back for multi-turn conversations
* `cited_text`: Up to 150 characters of the cited content

The web search citation fields `cited_text`, `title`, and `url` do not count toward input or output token usage.

<Note>
  When displaying API outputs directly to end users, citations must be included to the original source. If you are making modifications to API outputs, including by reprocessing or combining them with your own material before displaying them to end users, display citations as appropriate based on consultation with your legal team.
</Note>

### Errors

When the web search tool encounters an error (such as hitting rate limits), the Claude API still returns a 200 (success) response. The error is represented within the response body using the following structure:

```json Output
{
  "type": "web_search_tool_result",
  "tool_use_id": "srvtoolu_a93jad",
  "content": {
    "type": "web_search_tool_result_error",
    "error_code": "max_uses_exceeded"
  }
}
```

On an error, `content` is a single error object rather than a list of result blocks. A search that succeeds but matches no results returns an empty `content` list, not an error.

These are the possible error codes:

* `too_many_requests`: Rate limit exceeded
* `invalid_tool_input`: Invalid search query parameter
* `max_uses_exceeded`: Maximum web search tool uses exceeded
* `query_too_long`: Query exceeds maximum length
* `request_too_large`: The search request is too large, typically because of a long domain filter list
* `unavailable`: An internal error occurred

### `pause_turn` stop reason

The API can pause a long-running search turn and return `stop_reason: "pause_turn"`. To continue, send the paused assistant message back unchanged in a new request.

If Claude calls web search and one of your client tools in the same group of parallel tool calls, the API returns `stop_reason: "tool_use"` instead and does not run the search yet. To continue, return the client tool results, and the API runs the search in the next request. See [Mixing server tools and client tools in one turn](/docs/en/agents-and-tools/tool-use/server-tools#mixing-server-tools-and-client-tools-in-one-turn).

For the server-side loop and `pause_turn` handling, see [The server-side loop and pause\_turn](/docs/en/agents-and-tools/tool-use/server-tools#the-server-side-loop-and-pause-turn) in the Server tools guide.

## Prompt caching

For caching tool definitions across turns, see [Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching).

## Streaming

With streaming enabled, you'll receive search events as part of the stream. There will be a pause while the search runs:

```sse Output
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

To protect shared capacity, the Batches API throttles web search requests per organization, so large batches with many searches might take longer to complete. You can see your organization's web search rate limit on the [Limits](/settings/limits) page in the Claude Console. To request a higher limit, contact sales from that page.

## Usage and pricing

Web search usage is charged in addition to token usage:

```json
{
  "usage": {
    "input_tokens": 105,
    "output_tokens": 6039,
    "cache_read_input_tokens": 7123,
    "cache_creation_input_tokens": 7345,
    "server_tool_use": {
      "web_search_requests": 1
    }
  }
}
```

Web search is available on the Claude API for **$10 per 1,000 searches**, plus standard token costs for search-generated content. Web search results retrieved throughout a conversation are counted as input tokens, in search iterations executed during a single turn and in subsequent conversation turns.

Each web search counts as one use, regardless of the number of results returned. If an error occurs during web search, the web search will not be billed.

## Next steps

<CardGroup cols={3}>
  <Card title="Web fetch tool" icon="link" href="/docs/en/agents-and-tools/tool-use/web-fetch-tool">
    Fetch and read content from specific URLs to augment Claude's context with live web content.
  </Card>

  <Card title="Server tools" icon="tool" href="/docs/en/agents-and-tools/tool-use/server-tools">
    Work with Anthropic-executed tools: server\_tool\_use blocks, pause\_turn continuation, and domain filtering.
  </Card>

  <Card title="Tool reference" icon="book" href="/docs/en/agents-and-tools/tool-use/tool-reference">
    Directory of Anthropic-provided tools and reference for optional tool definition properties.
  </Card>
</CardGroup>
