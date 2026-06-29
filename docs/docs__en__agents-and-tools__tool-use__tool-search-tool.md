# Tool search tool

Scale to hundreds or thousands of tools by letting Claude search your tool catalog and load only the tools it needs.

---

The tool search tool lets Claude work with hundreds or thousands of tools by discovering and loading them on demand. Instead of loading all tool definitions into the context window up front, Claude searches your tool catalog (including tool names, descriptions, argument names, and argument descriptions) and loads only the tools it needs.

Loading every tool definition up front causes two problems as a tool library grows:

* **Context bloat:** A typical multi-server setup (GitHub, Slack, Sentry, Grafana, and Splunk) can consume \~55k tokens in definitions before Claude does any work. Tool search typically reduces this by over 85 percent, loading only the 3–5 tools Claude needs for a given request.
* **Tool selection accuracy:** Claude's ability to pick the right tool degrades once you exceed 30–50 available tools. Because tool search loads only a focused set of relevant tools on demand, selection accuracy stays high even across thousands of tools.

Tool search is generally available on the Claude API. For supported models, see [Model compatibility](#model-compatibility).

<Tip>
  For background on the scaling challenges that tool search solves, see [Advanced tool use](https://www.anthropic.com/engineering/advanced-tool-use). Tool search's on-demand loading is also an instance of the broader just-in-time retrieval principle described in [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
</Tip>

Tool search runs as a server-side tool, but you can also implement your own client-side tool search. See [Custom tool search implementation](#custom-tool-search-implementation) for details.

<Note>
  Share feedback on this feature through the [feedback form](https://forms.gle/MhcGFFwLxuwnWTkYA).
</Note>

<Note>
  This feature is eligible for [Zero Data Retention (ZDR)](/docs/en/build-with-claude/api-and-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.
</Note>

<Warning>
  On Amazon Bedrock, server-side tool search is available only through the [InvokeModel API](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_InvokeModel_AnthropicClaude_section.html), not the Converse API.
</Warning>

<Note>
  On [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws), server-side tool search works identically to the Claude API. Claude Platform on AWS uses the Anthropic Messages API directly, so there is no InvokeModel or Converse distinction.
</Note>

## Model compatibility

Both tool search variants are available on the following models:

| Model                                          | Tool versions                                                       |
| ---------------------------------------------- | ------------------------------------------------------------------- |
| Claude Fable 5 (claude-fable-5)                | `tool_search_tool_regex_20251119`, `tool_search_tool_bm25_20251119` |
| Claude Mythos 5 (claude-mythos-5)              | `tool_search_tool_regex_20251119`, `tool_search_tool_bm25_20251119` |
| Claude Opus 4.8 (claude-opus-4-8)              | `tool_search_tool_regex_20251119`, `tool_search_tool_bm25_20251119` |
| Claude Opus 4.7 (claude-opus-4-7)              | `tool_search_tool_regex_20251119`, `tool_search_tool_bm25_20251119` |
| Claude Opus 4.6 (claude-opus-4-6)              | `tool_search_tool_regex_20251119`, `tool_search_tool_bm25_20251119` |
| Claude Sonnet 4.6 (claude-sonnet-4-6)          | `tool_search_tool_regex_20251119`, `tool_search_tool_bm25_20251119` |
| Claude Opus 4.5 (claude-opus-4-5-20251101)     | `tool_search_tool_regex_20251119`, `tool_search_tool_bm25_20251119` |
| Claude Sonnet 4.5 (claude-sonnet-4-5-20250929) | `tool_search_tool_regex_20251119`, `tool_search_tool_bm25_20251119` |
| Claude Haiku 4.5 (claude-haiku-4-5-20251001)   | `tool_search_tool_regex_20251119`, `tool_search_tool_bm25_20251119` |

Claude Opus 4.1 and earlier models don't support the tool search tool.

## How tool search works

There are two tool search variants:

* **Regex** (`tool_search_tool_regex_20251119`): Claude constructs regex patterns to search for tools.
* **BM25** (`tool_search_tool_bm25_20251119`): Claude uses natural language queries to search for tools.

When you enable the tool search tool:

1. You include a tool search tool (for example, `tool_search_tool_regex_20251119` or `tool_search_tool_bm25_20251119`) in your `tools` list.
2. You provide every tool definition in the `tools` array and set `defer_loading: true` on the tools that shouldn't load up front. At least one tool, normally the tool search tool itself, must stay non-deferred.
3. Initially, Claude's context contains only the tool search tool and any non-deferred tools.
4. When Claude needs additional tools, it searches using a tool search tool.
5. The API runs the search and returns the matching tools as `tool_reference` blocks (up to 5 by default).
6. The API automatically expands these references into full tool definitions.
7. Claude selects from the discovered tools and calls them.

## Quick start

The following example includes the tool search tool and two deferred tools:

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/messages \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "content-type: application/json" \
      --data '{
          "model": "claude-opus-4-8",
          "max_tokens": 2048,
          "messages": [
              {
                  "role": "user",
                  "content": "What is the weather in San Francisco?"
              }
          ],
          "tools": [
              {
                  "type": "tool_search_tool_regex_20251119",
                  "name": "tool_search_tool_regex"
              },
              {
                  "name": "get_weather",
                  "description": "Get the weather at a specific location",
                  "input_schema": {
                      "type": "object",
                      "properties": {
                          "location": {"type": "string"},
                          "unit": {
                              "type": "string",
                              "enum": ["celsius", "fahrenheit"]
                          }
                      },
                      "required": ["location"]
                  },
                  "defer_loading": true
              },
              {
                  "name": "search_files",
                  "description": "Search through files in the workspace",
                  "input_schema": {
                      "type": "object",
                      "properties": {
                          "query": {"type": "string"},
                          "file_types": {
                              "type": "array",
                              "items": {"type": "string"}
                          }
                      },
                      "required": ["query"]
                  },
                  "defer_loading": true
              }
          ]
      }'
  ```

  ```bash CLI
  ant messages create <<'YAML'
  model: claude-opus-4-8
  max_tokens: 2048
  messages:
    - role: user
      content: What is the weather in San Francisco?
  tools:
    - type: tool_search_tool_regex_20251119
      name: tool_search_tool_regex
    - name: get_weather
      description: Get the weather at a specific location
      input_schema:
        type: object
        properties:
          location:
            type: string
          unit:
            type: string
            enum: [celsius, fahrenheit]
        required: [location]
      defer_loading: true
    - name: search_files
      description: Search through files in the workspace
      input_schema:
        type: object
        properties:
          query:
            type: string
          file_types:
            type: array
            items:
              type: string
        required: [query]
      defer_loading: true
  YAML
  ```

  ```python Python
  client = anthropic.Anthropic()

  response = client.messages.create(
      model="claude-opus-4-8",
      max_tokens=2048,
      messages=[{"role": "user", "content": "What is the weather in San Francisco?"}],
      tools=[
          {"type": "tool_search_tool_regex_20251119", "name": "tool_search_tool_regex"},
          {
              "name": "get_weather",
              "description": "Get the weather at a specific location",
              "input_schema": {
                  "type": "object",
                  "properties": {
                      "location": {"type": "string"},
                      "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                  },
                  "required": ["location"],
              },
              "defer_loading": True,
          },
          {
              "name": "search_files",
              "description": "Search through files in the workspace",
              "input_schema": {
                  "type": "object",
                  "properties": {
                      "query": {"type": "string"},
                      "file_types": {"type": "array", "items": {"type": "string"}},
                  },
                  "required": ["query"],
              },
              "defer_loading": True,
          },
      ],
  )

  print(response)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const response = await client.messages.create({
    model: "claude-opus-4-8",
    max_tokens: 2048,
    messages: [
      {
        role: "user",
        content: "What is the weather in San Francisco?"
      }
    ],
    tools: [
      {
        type: "tool_search_tool_regex_20251119",
        name: "tool_search_tool_regex"
      },
      {
        name: "get_weather",
        description: "Get the weather at a specific location",
        input_schema: {
          type: "object" as const,
          properties: {
            location: { type: "string" },
            unit: {
              type: "string",
              enum: ["celsius", "fahrenheit"]
            }
          },
          required: ["location"]
        },
        defer_loading: true
      },
      {
        name: "search_files",
        description: "Search through files in the workspace",
        input_schema: {
          type: "object" as const,
          properties: {
            query: { type: "string" },
            file_types: {
              type: "array",
              items: { type: "string" }
            }
          },
          required: ["query"]
        },
        defer_loading: true
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
      MaxTokens = 2048,
      Messages = [
          new() {
              Role = Role.User,
              Content = "What is the weather in San Francisco?"
          }
      ],
      Tools = [
          new ToolUnion(new ToolSearchToolRegex20251119
          {
              Type = ToolSearchToolRegex20251119Type.ToolSearchToolRegex20251119
          }),
          new ToolUnion(new Tool()
          {
              Name = "get_weather",
              Description = "Get the weather at a specific location",
              InputSchema = new InputSchema()
              {
                  Properties = new Dictionary<string, JsonElement>
                  {
                      ["location"] = JsonSerializer.SerializeToElement(new { type = "string" }),
                      ["unit"] = JsonSerializer.SerializeToElement(new { type = "string", @enum = new[] { "celsius", "fahrenheit" } }),
                  },
                  Required = ["location"],
              },
              DeferLoading = true,
          }),
          new ToolUnion(new Tool()
          {
              Name = "search_files",
              Description = "Search through files in the workspace",
              InputSchema = new InputSchema()
              {
                  Properties = new Dictionary<string, JsonElement>
                  {
                      ["query"] = JsonSerializer.SerializeToElement(new { type = "string" }),
                      ["file_types"] = JsonSerializer.SerializeToElement(new { type = "array", items = new { type = "string" } }),
                  },
                  Required = ["query"],
              },
              DeferLoading = true,
          }),
      ]
  };

  var message = await client.Messages.Create(parameters);
  Console.WriteLine(message);
  ```

  ```go Go
  client := anthropic.NewClient()

  response, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
  	Model:     anthropic.ModelClaudeOpus4_8,
  	MaxTokens: 2048,
  	Messages: []anthropic.MessageParam{
  		anthropic.NewUserMessage(anthropic.NewTextBlock("What is the weather in San Francisco?")),
  	},
  	Tools: []anthropic.ToolUnionParam{
  		{OfToolSearchToolRegex20251119: &anthropic.ToolSearchToolRegex20251119Param{
  			Type: anthropic.ToolSearchToolRegex20251119TypeToolSearchToolRegex20251119,
  		}},
  		{OfTool: &anthropic.ToolParam{
  			Name:        "get_weather",
  			Description: anthropic.String("Get the weather at a specific location"),
  			InputSchema: anthropic.ToolInputSchemaParam{
  				Properties: map[string]any{
  					"location": map[string]any{"type": "string"},
  					"unit": map[string]any{
  						"type": "string",
  						"enum": []string{"celsius", "fahrenheit"},
  					},
  				},
  				Required: []string{"location"},
  			},
  			DeferLoading: anthropic.Bool(true),
  		}},
  		{OfTool: &anthropic.ToolParam{
  			Name:        "search_files",
  			Description: anthropic.String("Search through files in the workspace"),
  			InputSchema: anthropic.ToolInputSchemaParam{
  				Properties: map[string]any{
  					"query":      map[string]any{"type": "string"},
  					"file_types": map[string]any{"type": "array", "items": map[string]any{"type": "string"}},
  				},
  				Required: []string{"query"},
  			},
  			DeferLoading: anthropic.Bool(true),
  		}},
  	},
  })
  if err != nil {
  	log.Fatal(err)
  }
  fmt.Println(response)
  ```

  ```java Java
  import com.anthropic.models.messages.ToolSearchToolRegex20251119;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      InputSchema weatherSchema = InputSchema.builder()
          .properties(JsonValue.from(Map.of(
              "location", Map.of("type", "string"),
              "unit", Map.of(
                  "type", "string",
                  "enum", List.of("celsius", "fahrenheit")
              )
          )))
          .putAdditionalProperty("required", JsonValue.from(List.of("location")))
          .build();

      InputSchema searchSchema = InputSchema.builder()
          .properties(JsonValue.from(Map.of(
              "query", Map.of("type", "string"),
              "file_types", Map.of(
                  "type", "array",
                  "items", Map.of("type", "string")
              )
          )))
          .putAdditionalProperty("required", JsonValue.from(List.of("query")))
          .build();

      MessageCreateParams params = MessageCreateParams.builder()
          .model(Model.CLAUDE_OPUS_4_8)
          .maxTokens(2048L)
          .addUserMessage("What is the weather in San Francisco?")
          .addTool(ToolSearchToolRegex20251119.builder()
              .type(ToolSearchToolRegex20251119.Type.TOOL_SEARCH_TOOL_REGEX_20251119)
              .build())
          .addTool(Tool.builder()
              .name("get_weather")
              .description("Get the weather at a specific location")
              .inputSchema(weatherSchema)
              .deferLoading(true)
              .build())
          .addTool(Tool.builder()
              .name("search_files")
              .description("Search through files in the workspace")
              .inputSchema(searchSchema)
              .deferLoading(true)
              .build())
          .build();

      Message response = client.messages().create(params);
      IO.println(response);
  }
  ```

  ```php PHP
  $client = new Client();

  $message = $client->messages->create(
      maxTokens: 2048,
      messages: [
          ['role' => 'user', 'content' => 'What is the weather in San Francisco?'],
      ],
      model: 'claude-opus-4-8',
      tools: [
          [
              'type' => 'tool_search_tool_regex_20251119',
              'name' => 'tool_search_tool_regex',
          ],
          [
              'name' => 'get_weather',
              'description' => 'Get the weather at a specific location',
              'input_schema' => [
                  'type' => 'object',
                  'properties' => [
                      'location' => ['type' => 'string'],
                      'unit' => [
                          'type' => 'string',
                          'enum' => ['celsius', 'fahrenheit'],
                      ],
                  ],
                  'required' => ['location'],
              ],
              'defer_loading' => true,
          ],
          [
              'name' => 'search_files',
              'description' => 'Search through files in the workspace',
              'input_schema' => [
                  'type' => 'object',
                  'properties' => [
                      'query' => ['type' => 'string'],
                      'file_types' => [
                          'type' => 'array',
                          'items' => ['type' => 'string'],
                      ],
                  ],
                  'required' => ['query'],
              ],
              'defer_loading' => true,
          ],
      ],
  );

  echo $message;
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  message = client.messages.create(
    model: "claude-opus-4-8",
    max_tokens: 2048,
    messages: [
      { role: "user", content: "What is the weather in San Francisco?" }
    ],
    tools: [
      {
        type: "tool_search_tool_regex_20251119",
        name: "tool_search_tool_regex"
      },
      {
        name: "get_weather",
        description: "Get the weather at a specific location",
        input_schema: {
          type: "object",
          properties: {
            location: { type: "string" },
            unit: {
              type: "string",
              enum: ["celsius", "fahrenheit"]
            }
          },
          required: ["location"]
        },
        defer_loading: true
      },
      {
        name: "search_files",
        description: "Search through files in the workspace",
        input_schema: {
          type: "object",
          properties: {
            query: { type: "string" },
            file_types: {
              type: "array",
              items: { type: "string" }
            }
          },
          required: ["query"]
        },
        defer_loading: true
      }
    ]
  )

  puts message
  ```
</CodeGroup>

Claude searches the catalog, discovers `get_weather`, and calls it. The response ends with `stop_reason: "tool_use"`. Execute the discovered tool and return a `tool_result` as in [Handle tool calls](/docs/en/agents-and-tools/tool-use/handle-tool-calls). [Response format](#response-format) shows the blocks you get back and what to send next.

## Tool definition

The tool search tool has two variants:

```json JSON
{
  "type": "tool_search_tool_regex_20251119",
  "name": "tool_search_tool_regex"
}
```

```json JSON
{
  "type": "tool_search_tool_bm25_20251119",
  "name": "tool_search_tool_bm25"
}
```

<Warning>
  **Regex variant query format: Python regex, not natural language**

  With `tool_search_tool_regex_20251119`, Claude writes Python `re.search()` patterns, not natural language queries. Matching is case-insensitive. Common patterns include the following:

  * `"weather"`: matches tool names and descriptions containing "weather"
  * `"get_.*_data"`: matches tools such as `get_user_data` and `get_weather_data`
  * `"database.*query|query.*database"`: matches either word order

  Maximum pattern length: 200 characters
</Warning>

<Note>
  **BM25 variant query format: natural language**

  With `tool_search_tool_bm25_20251119`, Claude searches with natural language queries. Maximum query length: 500 characters.
</Note>

### Deferred tool loading

Mark tools for on-demand loading by adding `defer_loading: true`:

```json JSON
{
  "name": "get_weather",
  "description": "Get current weather for a location",
  "input_schema": {
    "type": "object",
    "properties": {
      "location": { "type": "string" },
      "unit": { "type": "string", "enum": ["celsius", "fahrenheit"] }
    },
    "required": ["location"]
  },
  "defer_loading": true
}
```

`defer_loading` controls what enters the context window, not what you send in the request:

* You still send every tool's full definition in the `tools` array on every request, including the deferred ones. The API needs them server-side to run the search and expand `tool_reference` blocks.
* Tools without `defer_loading` load into context immediately.
* Tools with `defer_loading: true` load only when Claude discovers them through search.
* Never set `defer_loading: true` on the tool search tool itself.
* Keep your 3–5 most frequently used tools non-deferred so Claude can call them without searching first.

Both tool search variants (`regex` and `bm25`) search tool names, descriptions, argument names, and argument descriptions.

Internally, the API excludes deferred tools from the system-prompt prefix. When Claude discovers a deferred tool through tool search, the API appends a `tool_reference` block inline in the conversation, then expands it into the full tool definition before passing it to Claude. The prefix is untouched, so prompt caching is preserved. The grammar for [strict mode](/docs/en/agents-and-tools/tool-use/strict-tool-use) (the rules that constrain tool-call output to match your schemas) builds from the full toolset, so `defer_loading` and strict mode compose without grammar recompilation.

## Response format

When Claude uses the tool search tool, the response includes the following block types:

```json JSON
{
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "I'll search for tools to help with the weather information."
    },
    {
      "type": "server_tool_use",
      "id": "srvtoolu_01ABC123",
      "name": "tool_search_tool_regex",
      "input": {
        "pattern": "weather"
      }
    },
    {
      "type": "tool_search_tool_result",
      "tool_use_id": "srvtoolu_01ABC123",
      "content": {
        "type": "tool_search_tool_search_result",
        "tool_references": [{ "type": "tool_reference", "tool_name": "get_weather" }]
      }
    },
    {
      "type": "text",
      "text": "I found a weather tool. Let me get the weather for San Francisco."
    },
    {
      "type": "tool_use",
      "id": "toolu_01XYZ789",
      "name": "get_weather",
      "input": { "location": "San Francisco", "unit": "fahrenheit" }
    }
  ],
  "stop_reason": "tool_use"
}
```

### Understanding the response

* **`server_tool_use`:** Claude's call to the tool search tool. The search runs on Anthropic's servers. Never return a `tool_result` for its `srvtoolu_...` ID.
* **`tool_search_tool_result`:** the search results, in a nested `tool_search_tool_search_result` object. Keep it in the message history as is.
* **`tool_references`:** an array of `tool_reference` objects pointing to discovered tools. The API expands these for Claude. You never expand them yourself.
* **`tool_use`:** Claude's call to a discovered tool. Execute it and return a `tool_result` exactly as in standard tool use.

The API automatically expands `tool_reference` blocks into full tool definitions before showing them to Claude. You don't need to handle this expansion yourself, as long as you provide all matching tool definitions in the `tools` parameter.

### Continuing the conversation

On the next request, pass the assistant's content back unchanged, including the `server_tool_use` and `tool_search_tool_result` blocks. Add your `tool_result` for the discovered tool in a user message, and send the same `tools` array: the search tool plus every deferred definition. Don't return a `tool_result` for the `srvtoolu_...` ID: the API rejects the request. The API expands `tool_reference` blocks throughout the conversation history, so Claude can reuse discovered tools in later turns without re-searching. A search that matches nothing returns a `tool_search_tool_search_result` with an empty `tool_references` array, not an error.

## MCP integration

If your tools come from MCP servers through the [MCP connector](/docs/en/agents-and-tools/mcp-connector), you don't set `defer_loading` on individual tool definitions. Instead, set it once on the `mcp_toolset` entry's `default_config` for the whole server, or per tool in its `configs`. See [MCP toolset configuration](/docs/en/agents-and-tools/mcp-connector#mcp-toolset-configuration).

## Custom tool search implementation

You can implement your own tool search logic (for example, using embeddings or semantic search) by returning `tool_reference` blocks from a custom tool. When Claude calls your custom search tool, return a standard `tool_result` with `tool_reference` blocks in the content array:

```json JSON
{
  "type": "tool_result",
  "tool_use_id": "toolu_your_tool_id",
  "content": [{ "type": "tool_reference", "tool_name": "discovered_tool_name" }]
}
```

Every tool referenced must have a corresponding tool definition in the top-level `tools` parameter, normally with `defer_loading: true`. This lets you use search methods the built-in variants don't provide, such as embedding-based retrieval, and the API expands the returned `tool_reference` blocks the same way.

<Note>
  The `tool_search_tool_result` format shown in the [Response format](#response-format) section is the server-side format used internally by Anthropic's built-in tool search. For custom client-side implementations, always use the standard `tool_result` format with `tool_reference` content blocks as shown in the preceding example.
</Note>

For a complete example using embeddings, see the [tool search with embeddings](https://platform.claude.com/cookbook/tool-use-tool-search-with-embeddings) recipe.

## Error handling

<Note>
  [Tool use examples](/docs/en/agents-and-tools/tool-use/define-tools#providing-tool-use-examples) work with tool search: when Claude discovers a deferred tool, the API expands its `input_examples` along with its definition.
</Note>

### HTTP errors (400 status)

These errors prevent the API from processing the request:

**All tools deferred:**

```json
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "At least one tool must have defer_loading=false. All tools cannot be deferred."
  }
}
```

**Missing tool definition:**

```json
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "Tool reference 'unknown_tool' not found in available tools"
  }
}
```

### Tool result errors (200 status)

When a tool search operation fails during execution, the API returns a 200 response with the error in the body:

```json JSON
{
  "type": "tool_search_tool_result",
  "tool_use_id": "srvtoolu_01ABC123",
  "content": {
    "type": "tool_search_tool_result_error",
    "error_code": "invalid_tool_input",
    "error_message": "Invalid regular expression pattern: missing ) at position 1"
  }
}
```

The `error_code` field has four possible values:

* `invalid_tool_input`: the search input was invalid, for example a malformed regex pattern or a pattern over the 200-character limit
* `unavailable`: the search couldn't run, for example because it timed out or the service was unavailable
* `too_many_requests`: rate limit exceeded for tool search operations
* `execution_time_exceeded`: the search exceeded its execution time limit

### Common mistakes

<Accordion title="400 error: all tools are deferred">
  **Cause:** You set `defer_loading: true` on every tool, including the tool search tool.

  **Fix:** Remove `defer_loading` from the tool search tool:

  ```json
  {
    "type": "tool_search_tool_regex_20251119",
    "name": "tool_search_tool_regex"
  }
  ```
</Accordion>

<Accordion title="400 error: missing tool definition">
  **Cause:** A `tool_reference` points to a tool not in your `tools` array.

  **Fix:** Ensure every tool that could be discovered has a complete definition:

  ```json
  {
    "name": "my_tool",
    "description": "Full description here",
    "input_schema": {
      "type": "object"
    },
    "defer_loading": true
  }
  ```
</Accordion>

<Accordion title="Claude doesn't find expected tools">
  **Cause:** The regex pattern doesn't match the tool's name, description, argument names, or argument descriptions.

  **Debugging steps:**

  1. Check tool name, description, argument names, and argument descriptions. Claude searches all of these fields.
  2. Test your pattern: `import re; re.search(r"your_pattern", "tool_name", re.IGNORECASE)`.
  3. Matching is case-insensitive, so casing differences aren't the problem.
  4. Claude uses broad patterns such as `".*weather.*"`, not exact matches.

  **Tip:** Add common keywords to tool descriptions to improve discoverability.
</Accordion>

## Prompt caching

For how `defer_loading` preserves prompt caching, see [Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching).

A tool with `defer_loading: true` can't also carry `cache_control`: the API returns a 400. Put the cache breakpoint on a non-deferred tool.

## Streaming

With streaming enabled, you'll receive tool search events as part of the stream:

```sse
event: content_block_start
data: {"type": "content_block_start", "index": 1, "content_block": {"type": "server_tool_use", "id": "srvtoolu_xyz789", "name": "tool_search_tool_regex"}}

// Search pattern streamed
event: content_block_delta
data: {"type": "content_block_delta", "index": 1, "delta": {"type": "input_json_delta", "partial_json": "{\"pattern\":\"weather\"}"}}

// Pause while search executes

// Search results streamed
event: content_block_start
data: {"type": "content_block_start", "index": 2, "content_block": {"type": "tool_search_tool_result", "tool_use_id": "srvtoolu_xyz789", "content": {"type": "tool_search_tool_search_result", "tool_references": [{"type": "tool_reference", "tool_name": "get_weather"}]}}}

// Claude continues with discovered tools
```

## Batch requests

You can include the tool search tool in the [Messages Batches API](/docs/en/build-with-claude/batch-processing).

## Limits and best practices

### Limits

* **Maximum deferred tools:** 10,000 tools with `defer_loading: true` per request
* **Search results:** each search returns up to 5 matching tools by default
* **Pattern and query length:** maximum 200 characters for regex patterns and 500 characters for BM25 queries
* **Model support:** see [Model compatibility](#model-compatibility)

### When to use tool search

Use tool search when any of the following apply:

* You have 10 or more tools available.
* Your tool definitions consume more than 10k tokens.
* Tool selection accuracy drops as your toolset grows.
* You aggregate multiple MCP servers (200+ tools).
* Your tool library grows over time.

Standard tool calling, without tool search, is a better fit when you have fewer than 10 tools, every tool is used in every request, or your tool definitions are small (less than 100 tokens total).

### Optimization tips

* Keep your 3–5 most frequently used tools non-deferred.
* Write clear, descriptive tool names and descriptions.
* Use consistent namespacing in tool names: prefix by service or resource (for example, `github_`, `slack_`) so one search matches the whole group.
* Use keywords in descriptions that match how users describe tasks.
* Add a system prompt section describing available tool categories: "You can search for tools to interact with Slack, GitHub, and Jira."
* Monitor which tools Claude discovers to refine your descriptions.

## Usage

Tool search isn't metered as a separate server tool. The response's `usage.server_tool_use` object has no tool search field, and the tool definitions that search loads into context count as input tokens like any other tool definition.

## Next steps

<CardGroup cols={2}>
  <Card title="Memory tool" icon="brain" href="/docs/en/agents-and-tools/tool-use/memory-tool">
    Let Claude store and retrieve information across conversations by implementing the memory tool's file operations in your application.
  </Card>

  <Card title="Tool reference" icon="book" href="/docs/en/agents-and-tools/tool-use/tool-reference">
    Directory of Anthropic-provided tools and reference for optional tool definition properties.
  </Card>

  <Card title="MCP connector" icon="link" href="/docs/en/agents-and-tools/mcp-connector">
    Configure MCP toolsets with deferred loading.
  </Card>

  <Card title="Tool use with prompt caching" icon="bolt" href="/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching">
    Cache tool definitions across turns and understand what invalidates your cache.
  </Card>

  <Card title="Define tools" icon="hammer" href="/docs/en/agents-and-tools/tool-use/define-tools">
    Specify tool schemas, write effective descriptions, and control when Claude calls your tools.
  </Card>
</CardGroup>
