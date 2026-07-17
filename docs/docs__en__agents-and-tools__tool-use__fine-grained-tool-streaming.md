# Fine-grained tool streaming

Stream tool inputs without server-side JSON buffering for latency-sensitive applications.

---

<Note>
  For how zero data retention (ZDR) applies to this feature, see [API and data retention](/docs/en/manage-claude/api-and-data-retention).
</Note>

Fine-grained tool streaming delivers a tool's input to your client as Claude generates it, without server-side buffering or JSON validation. Skipping the buffering step reduces the time to the first fragment of a large parameter, such as a document or a block of code, and the fragments arrive through the same [Streaming messages](/docs/en/build-with-claude/streaming) events as standard tool use.

<Warning>
  Because the API does not buffer or validate a tool's input before streaming it, you might receive partial or invalid JSON. A response that ends with the [stop reason](/docs/en/build-with-claude/handling-stop-reasons) `max_tokens` can also cut a parameter off midway. Accumulate the fragments, guard the parse, and see [Handling invalid JSON in tool responses](#handling-invalid-json-in-tool-responses) for how to return unparseable input to Claude.
</Warning>

## How to use fine-grained tool streaming

All models support fine-grained tool streaming on the Claude API, [Amazon Bedrock](/docs/en/build-with-claude/claude-in-amazon-bedrock), [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws), [Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai), and [Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry). To use it, set `eager_input_streaming` to `true` on any user-defined tool where you want fine-grained streaming enabled, and enable streaming on your request.

The `eager_input_streaming` field is optional. Setting it to `true` turns on fine-grained streaming for that tool, and omitting it gives you standard buffered streaming, in which the API buffers and validates each parameter value before streaming it back. The exception is a request that still sends the legacy `fine-grained-tool-streaming-2025-05-14` beta header, which turns fine-grained streaming on for tools that leave the field unset. The per-tool field replaces that header, and an explicit `false` keeps buffered streaming for a tool even when a request still sends it. See [Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference) for the field definition.

The following example turns on fine-grained streaming for a `make_file` tool and asks Claude for a long poem, so the tool input is large enough to watch it stream in:

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/messages \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -d '{
      "model": "claude-opus-4-8",
      "max_tokens": 65536,
      "tools": [
        {
          "name": "make_file",
          "description": "Write text to a file",
          "eager_input_streaming": true,
          "input_schema": {
            "type": "object",
            "properties": {
              "filename": {
                "type": "string",
                "description": "The filename to write text to"
              },
              "lines_of_text": {
                "type": "array",
                "description": "An array of lines of text to write to the file"
              }
            },
            "required": ["filename", "lines_of_text"]
          }
        }
      ],
      "messages": [
        {
          "role": "user",
          "content": "Can you write a long poem and make a file called poem.txt?"
        }
      ],
      "stream": true
    }'
  ```

  ```bash CLI
  ant messages create --stream --format jsonl <<'YAML' |
  model: claude-opus-4-8
  max_tokens: 65536
  tools:
    - name: make_file
      description: Write text to a file
      eager_input_streaming: true
      input_schema:
        type: object
        properties:
          filename:
            type: string
            description: The filename to write text to
          lines_of_text:
            type: array
            description: An array of lines of text to write to the file
        required:
          - filename
          - lines_of_text
  messages:
    - role: user
      content: Can you write a long poem and make a file called poem.txt?
  YAML
    jq -rj 'select(.delta.type == "input_json_delta") | .delta.partial_json'
  ```

  ```python Python
  client = anthropic.Anthropic()

  with client.messages.stream(
      max_tokens=65536,
      model="claude-opus-4-8",
      tools=[
          {
              "name": "make_file",
              "description": "Write text to a file",
              "eager_input_streaming": True,
              "input_schema": {
                  "type": "object",
                  "properties": {
                      "filename": {
                          "type": "string",
                          "description": "The filename to write text to",
                      },
                      "lines_of_text": {
                          "type": "array",
                          "description": "An array of lines of text to write to the file",
                      },
                  },
                  "required": ["filename", "lines_of_text"],
              },
          }
      ],
      messages=[
          {
              "role": "user",
              "content": "Can you write a long poem and make a file called poem.txt?",
          }
      ],
  ) as stream:
      for event in stream:
          if event.type == "input_json":
              print(event.partial_json, end="", flush=True)
      final_message = stream.get_final_message()

  print()
  for block in final_message.content:
      if block.type == "tool_use":
          print(f"Complete tool input: {block.input}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const stream = client.messages.stream({
    model: "claude-opus-4-8",
    max_tokens: 65536,
    tools: [
      {
        name: "make_file",
        description: "Write text to a file",
        eager_input_streaming: true,
        input_schema: {
          type: "object",
          properties: {
            filename: {
              type: "string",
              description: "The filename to write text to"
            },
            lines_of_text: {
              type: "array",
              description: "An array of lines of text to write to the file"
            }
          },
          required: ["filename", "lines_of_text"]
        }
      }
    ],
    messages: [
      {
        role: "user",
        content: "Can you write a long poem and make a file called poem.txt?"
      }
    ]
  });

  stream.on("inputJson", (partialJson) => {
    process.stdout.write(partialJson);
  });

  const message = await stream.finalMessage();
  console.log();
  for (const block of message.content) {
    if (block.type === "tool_use") {
      console.log("Complete tool input:", block.input);
    }
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  MessageCreateParams parameters = new()
  {
      Model = Model.ClaudeOpus4_8,
      MaxTokens = 65536,
      Tools =
      [
          new Tool
          {
              Name = "make_file",
              Description = "Write text to a file",
              EagerInputStreaming = true,
              InputSchema = new InputSchema
              {
                  Properties = new Dictionary<string, JsonElement>
                  {
                      ["filename"] = JsonSerializer.SerializeToElement(
                          new { type = "string", description = "The filename to write text to" }
                      ),
                      ["lines_of_text"] = JsonSerializer.SerializeToElement(
                          new { type = "array", description = "An array of lines of text to write to the file" }
                      ),
                  },
                  Required = ["filename", "lines_of_text"],
              },
          },
      ],
      Messages =
      [
          new()
          {
              Role = Role.User,
              Content = "Can you write a long poem and make a file called poem.txt?",
          },
      ],
  };

  // The C# example assembles the input itself: content block index -> accumulated JSON
  var toolInputs = new Dictionary<long, StringBuilder>();

  await foreach (var streamEvent in client.Messages.CreateStreaming(parameters))
  {
      if (
          streamEvent.TryPickContentBlockStart(out var start)
          && start.ContentBlock.TryPickToolUse(out _)
      )
      {
          toolInputs[start.Index] = new StringBuilder();
      }
      else if (
          streamEvent.TryPickContentBlockDelta(out var delta)
          && delta.Delta.TryPickInputJson(out var inputJson)
      )
      {
          Console.Write(inputJson.PartialJson);
          toolInputs[delta.Index].Append(inputJson.PartialJson);
      }
  }

  Console.WriteLine();
  foreach (var accumulatedInput in toolInputs.Values)
  {
      Console.WriteLine($"Complete tool input: {accumulatedInput}");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  makeFileTool := anthropic.ToolParam{
  	Name:                "make_file",
  	Description:         anthropic.String("Write text to a file"),
  	EagerInputStreaming: anthropic.Bool(true),
  	InputSchema: anthropic.ToolInputSchemaParam{
  		Properties: map[string]any{
  			"filename": map[string]any{
  				"type":        "string",
  				"description": "The filename to write text to",
  			},
  			"lines_of_text": map[string]any{
  				"type":        "array",
  				"description": "An array of lines of text to write to the file",
  			},
  		},
  		Required: []string{"filename", "lines_of_text"},
  	},
  }

  stream := client.Messages.NewStreaming(context.Background(), anthropic.MessageNewParams{
  	Model:     anthropic.ModelClaudeOpus4_8,
  	MaxTokens: 65536,
  	Tools:     []anthropic.ToolUnionParam{{OfTool: &makeFileTool}},
  	Messages: []anthropic.MessageParam{
  		anthropic.NewUserMessage(anthropic.NewTextBlock(
  			"Can you write a long poem and make a file called poem.txt?",
  		)),
  	},
  })

  message := anthropic.Message{}
  for stream.Next() {
  	event := stream.Current()
  	if err := message.Accumulate(event); err != nil {
  		panic(err)
  	}
  	if delta, ok := event.AsAny().(anthropic.ContentBlockDeltaEvent); ok {
  		if inputJSON, ok := delta.Delta.AsAny().(anthropic.InputJSONDelta); ok {
  			fmt.Print(inputJSON.PartialJSON)
  		}
  	}
  }
  if err := stream.Err(); err != nil {
  	panic(err)
  }

  fmt.Println()
  for _, block := range message.Content {
  	if toolUse, ok := block.AsAny().(anthropic.ToolUseBlock); ok {
  		fmt.Printf("Complete tool input: %s\n", toolUse.Input)
  	}
  }
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  Tool makeFileTool = Tool.builder()
      .name("make_file")
      .description("Write text to a file")
      .eagerInputStreaming(true)
      .inputSchema(Tool.InputSchema.builder()
          .properties(Tool.InputSchema.Properties.builder()
              .putAdditionalProperty("filename", JsonValue.from(Map.of(
                  "type", "string",
                  "description", "The filename to write text to")))
              .putAdditionalProperty("lines_of_text", JsonValue.from(Map.of(
                  "type", "array",
                  "description", "An array of lines of text to write to the file")))
              .build())
          .addRequired("filename")
          .addRequired("lines_of_text")
          .build())
      .build();

  MessageCreateParams params = MessageCreateParams.builder()
      .model(Model.CLAUDE_OPUS_4_8)
      .maxTokens(65536L)
      .addTool(makeFileTool)
      .addUserMessage("Can you write a long poem and make a file called poem.txt?")
      .build();

  MessageAccumulator accumulator = MessageAccumulator.create();

  try (StreamResponse<RawMessageStreamEvent> streamResponse =
          client.messages().createStreaming(params)) {
      streamResponse.stream().forEach(event -> {
          accumulator.accumulate(event);
          if (event.isContentBlockDelta()) {
              var delta = event.asContentBlockDelta().delta();
              if (delta.isInputJson()) {
                  IO.print(delta.asInputJson().partialJson());
              }
          }
      });
  }

  IO.println("");
  accumulator.message().content().forEach(block ->
      block.toolUse().ifPresent(toolUse ->
          IO.println("Complete tool input: " + toolUse._input())));
  ```

  ```php PHP
  use Anthropic\Client;
  use Anthropic\Messages\InputJSONDelta;
  use Anthropic\Messages\Model;
  use Anthropic\Messages\RawContentBlockDeltaEvent;
  use Anthropic\Messages\RawContentBlockStartEvent;
  use Anthropic\Messages\ToolUseBlock;

  $client = new Client();

  $stream = $client->messages->createStream(
      maxTokens: 65536,
      model: Model::CLAUDE_OPUS_4_8,
      tools: [
          [
              'name' => 'make_file',
              'description' => 'Write text to a file',
              'eager_input_streaming' => true,
              'input_schema' => [
                  'type' => 'object',
                  'properties' => [
                      'filename' => [
                          'type' => 'string',
                          'description' => 'The filename to write text to',
                      ],
                      'lines_of_text' => [
                          'type' => 'array',
                          'description' => 'An array of lines of text to write to the file',
                      ],
                  ],
                  'required' => ['filename', 'lines_of_text'],
              ],
          ],
      ],
      messages: [
          [
              'role' => 'user',
              'content' => 'Can you write a long poem and make a file called poem.txt?',
          ],
      ],
  );

  // The PHP example assembles the input itself: index => accumulated JSON string
  $toolInputs = [];

  foreach ($stream as $event) {
      if (
          $event instanceof RawContentBlockStartEvent
          && $event->contentBlock instanceof ToolUseBlock
      ) {
          $toolInputs[$event->index] = '';
      } elseif (
          $event instanceof RawContentBlockDeltaEvent
          && $event->delta instanceof InputJSONDelta
      ) {
          echo $event->delta->partialJSON;
          $toolInputs[$event->index] .= $event->delta->partialJSON;
      }
  }

  echo "\n";
  foreach ($toolInputs as $toolInput) {
      echo "Complete tool input: {$toolInput}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  stream = client.messages.stream(
    model: Anthropic::Models::Model::CLAUDE_OPUS_4_8,
    max_tokens: 65_536,
    tools: [
      {
        name: "make_file",
        description: "Write text to a file",
        eager_input_streaming: true,
        input_schema: {
          type: "object",
          properties: {
            filename: {
              type: "string",
              description: "The filename to write text to"
            },
            lines_of_text: {
              type: "array",
              description: "An array of lines of text to write to the file"
            }
          },
          required: ["filename", "lines_of_text"]
        }
      }
    ],
    messages: [
      {
        role: "user",
        content: "Can you write a long poem and make a file called poem.txt?"
      }
    ]
  )

  stream.each do |event|
    print event.partial_json if event.is_a?(Anthropic::Streaming::InputJsonEvent)
  end

  puts
  stream.accumulated_message.content.each do |block|
    puts "Complete tool input: #{block.input}" if block.type == :tool_use
  end
  ```
</CodeGroup>

Every tab turns on fine-grained streaming for the `make_file` tool. The SDK tabs print each input fragment the moment it arrives, then print the complete accumulated input once the stream ends. The cURL tab shows the raw event stream, and the CLI tab uses `jq` to print just the fragments. Because the printed fragments join into the full tool input, the poem fills your terminal as Claude writes it:

```text wrap
{"filename": "poem.txt", "lines_of_text": ["The Wanderer's Journey", "", "I.", "", "Beneath the vast and star-strewn sky,", "Where silver moonbeams softly lie,", ...
Complete tool input: {"filename": "poem.txt", "lines_of_text": ["The Wanderer's Journey", ...]}
```

Without `eager_input_streaming`, the API buffers and validates each parameter value before streaming it back, so nothing prints for a large parameter until Claude has finished generating it. With it, fragments start arriving as soon as Claude begins the parameter, and they are typically longer, with fewer mid-word breaks.

## Accumulating tool input deltas

The accumulation contract is the same as for standard tool-use streaming, so this section applies with and without `eager_input_streaming`. See [Input JSON delta](/docs/en/build-with-claude/streaming#input-json-delta) in Streaming messages for the event format. Fine-grained tool streaming changes what you can assume about the result: the server streams fragments without validating them, so the accumulated string might not be valid JSON.

When a `tool_use` content block streams, the initial `content_block_start` event contains `input: {}` (an empty object). This is a placeholder. The actual input arrives as a series of `input_json_delta` events, each carrying a `partial_json` string fragment. To assemble the full input, concatenate these fragments and parse the result when the block closes.

Where your SDK provides an accumulator helper (as the Python, TypeScript, Go, Java, and Ruby tabs in the previous example do), it handles this for you. The manual pattern is for SDKs without a helper, or when you want full control over how the input is assembled.

The accumulation contract:

1. On `content_block_start` with `type: "tool_use"`, initialize an empty string: `input_json = ""`
2. For each `content_block_delta` with `type: "input_json_delta"`, append: `input_json += event.delta.partial_json`
3. On `content_block_stop`, parse the accumulated string

Guard the parse, as the following SDK examples do. A response can also stop at `max_tokens` midway through a parameter. Check the [stop reason](/docs/en/build-with-claude/handling-stop-reasons) and decide whether to retry the request with a higher `max_tokens` or repair the partial input.

The type mismatch between the initial `input: {}` (object) and `partial_json` (string) is by design. The empty object marks the slot in the content array. The delta strings build the real value.

<CodeGroup>
  ```bash cURL
  # Accumulating per-block input deltas needs a programming language; the first
  # example's CLI tab shows the raw fragments with jq. See the SDK tabs.
  ```

  ```bash CLI
  # Accumulating per-block input deltas needs a programming language; the first
  # example's CLI tab shows the raw fragments with jq. See the SDK tabs.
  ```

  ```python Python
  client = anthropic.Anthropic()

  tool_inputs: dict[int, str] = {}  # index -> accumulated JSON string

  with client.messages.stream(
      model="claude-opus-4-8",
      max_tokens=1024,
      tools=[
          {
              "name": "get_weather",
              "description": "Get current weather for a city",
              "eager_input_streaming": True,
              "input_schema": {
                  "type": "object",
                  "properties": {"city": {"type": "string"}},
                  "required": ["city"],
              },
          }
      ],
      messages=[{"role": "user", "content": "Weather in Paris?"}],
  ) as stream:
      for event in stream:
          match event.type:
              case "content_block_start" if event.content_block.type == "tool_use":
                  tool_inputs[event.index] = ""
              case "content_block_delta" if event.delta.type == "input_json_delta":
                  tool_inputs[event.index] += event.delta.partial_json
              case "content_block_stop" if event.index in tool_inputs:
                  raw_input = tool_inputs[event.index]
                  try:
                      parsed = json.loads(raw_input)
                  except json.JSONDecodeError:
                      # The accumulated string is not guaranteed to be valid JSON.
                      # See "Handling invalid JSON in tool responses" on this page.
                      print(f"Invalid tool input: {raw_input}")
                  else:
                      print(f"Tool input: {parsed}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const toolInputs = new Map<number, string>();

  const stream = client.messages.stream({
    model: "claude-opus-4-8",
    max_tokens: 1024,
    tools: [
      {
        name: "get_weather",
        description: "Get current weather for a city",
        eager_input_streaming: true,
        input_schema: {
          type: "object",
          properties: { city: { type: "string" } },
          required: ["city"]
        }
      }
    ],
    messages: [{ role: "user", content: "Weather in Paris?" }]
  });

  for await (const event of stream) {
    if (event.type === "content_block_start" && event.content_block.type === "tool_use") {
      toolInputs.set(event.index, "");
    } else if (event.type === "content_block_delta" && event.delta.type === "input_json_delta") {
      toolInputs.set(
        event.index,
        (toolInputs.get(event.index) ?? "") + event.delta.partial_json
      );
    } else if (event.type === "content_block_stop" && toolInputs.has(event.index)) {
      const rawInput = toolInputs.get(event.index)!;
      try {
        console.log("Tool input:", JSON.parse(rawInput));
      } catch {
        // The accumulated string is not guaranteed to be valid JSON.
        // See "Handling invalid JSON in tool responses" on this page.
        console.log("Invalid tool input:", rawInput);
      }
    }
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  MessageCreateParams parameters = new()
  {
      Model = Model.ClaudeOpus4_8,
      MaxTokens = 1024,
      Tools =
      [
          new Tool
          {
              Name = "get_weather",
              Description = "Get current weather for a city",
              EagerInputStreaming = true,
              InputSchema = new InputSchema
              {
                  Properties = new Dictionary<string, JsonElement>
                  {
                      ["city"] = JsonSerializer.SerializeToElement(new { type = "string" }),
                  },
                  Required = ["city"],
              },
          },
      ],
      Messages = [new() { Role = Role.User, Content = "Weather in Paris?" }],
  };

  // Block index -> accumulated JSON fragments
  // This example accumulates the deltas manually to show the raw stream;
  // the SDK's MessageContentAggregator can also accumulate tool input automatically.
  var toolInputs = new Dictionary<long, StringBuilder>();

  await foreach (var streamEvent in client.Messages.CreateStreaming(parameters))
  {
      if (
          streamEvent.TryPickContentBlockStart(out var start)
          && start.ContentBlock.TryPickToolUse(out _)
      )
      {
          toolInputs[start.Index] = new StringBuilder();
      }
      else if (
          streamEvent.TryPickContentBlockDelta(out var delta)
          && delta.Delta.TryPickInputJson(out var inputJson)
      )
      {
          toolInputs[delta.Index].Append(inputJson.PartialJson);
      }
      else if (
          streamEvent.TryPickContentBlockStop(out var stop)
          && toolInputs.TryGetValue(stop.Index, out var accumulated)
      )
      {
          try
          {
              using var parsed = JsonDocument.Parse(accumulated.ToString());
              Console.WriteLine($"Tool input: {parsed.RootElement}");
          }
          catch (JsonException)
          {
              // The accumulated string is not guaranteed to be valid JSON.
              // See "Handling invalid JSON in tool responses" on this page.
              Console.WriteLine($"Invalid tool input: {accumulated}");
          }
      }
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  toolInputs := map[int64]string{} // content block index -> accumulated JSON

  stream := client.Messages.NewStreaming(context.Background(), anthropic.MessageNewParams{
  	Model:     anthropic.ModelClaudeOpus4_8,
  	MaxTokens: 1024,
  	Tools: []anthropic.ToolUnionParam{{
  		OfTool: &anthropic.ToolParam{
  			Name:                "get_weather",
  			Description:         anthropic.String("Get current weather for a city"),
  			EagerInputStreaming: anthropic.Bool(true),
  			InputSchema: anthropic.ToolInputSchemaParam{
  				Properties: map[string]any{
  					"city": map[string]any{"type": "string"},
  				},
  				Required: []string{"city"},
  			},
  		},
  	}},
  	Messages: []anthropic.MessageParam{
  		anthropic.NewUserMessage(anthropic.NewTextBlock("Weather in Paris?")),
  	},
  })

  for stream.Next() {
  	switch event := stream.Current().AsAny().(type) {
  	case anthropic.ContentBlockStartEvent:
  		if _, ok := event.ContentBlock.AsAny().(anthropic.ToolUseBlock); ok {
  			toolInputs[event.Index] = ""
  		}
  	case anthropic.ContentBlockDeltaEvent:
  		if delta, ok := event.Delta.AsAny().(anthropic.InputJSONDelta); ok {
  			toolInputs[event.Index] += delta.PartialJSON
  		}
  	case anthropic.ContentBlockStopEvent:
  		if accumulated, ok := toolInputs[event.Index]; ok {
  			var parsed map[string]any
  			if err := json.Unmarshal([]byte(accumulated), &parsed); err != nil {
  				// The accumulated string is not guaranteed to be valid JSON.
  				// See "Handling invalid JSON in tool responses" on this page.
  				fmt.Println("Invalid tool input:", accumulated)
  			} else {
  				fmt.Println("Tool input:", parsed)
  			}
  		}
  	}
  }
  if err := stream.Err(); err != nil {
  	panic(err)
  }
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();
  ObjectMapper objectMapper = new ObjectMapper();

  Tool weatherTool = Tool.builder()
          .name("get_weather")
          .description("Get current weather for a city")
          .eagerInputStreaming(true)
          .inputSchema(Tool.InputSchema.builder()
                  .properties(Tool.InputSchema.Properties.builder()
                          .putAdditionalProperty("city", JsonValue.from(Map.of("type", "string")))
                          .build())
                  .addRequired("city")
                  .build())
          .build();

  MessageCreateParams createParams = MessageCreateParams.builder()
          .model(Model.CLAUDE_OPUS_4_8)
          .maxTokens(1024)
          .addTool(weatherTool)
          .addUserMessage("Weather in Paris?")
          .build();

  // Content block index -> accumulated tool input JSON
  Map<Long, StringBuilder> toolInputs = new HashMap<>();

  try (StreamResponse<RawMessageStreamEvent> streamResponse = client.messages().createStreaming(createParams)) {
      var eventIterator = streamResponse.stream().iterator();
      while (eventIterator.hasNext()) {
          RawMessageStreamEvent event = eventIterator.next();
          if (event.isContentBlockStart()) {
              var blockStart = event.asContentBlockStart();
              if (blockStart.contentBlock().isToolUse()) {
                  toolInputs.put(blockStart.index(), new StringBuilder());
              }
          } else if (event.isContentBlockDelta()) {
              var blockDelta = event.asContentBlockDelta();
              if (blockDelta.delta().isInputJson() && toolInputs.containsKey(blockDelta.index())) {
                  toolInputs.get(blockDelta.index()).append(blockDelta.delta().asInputJson().partialJson());
              }
          } else if (event.isContentBlockStop()) {
              var blockStop = event.asContentBlockStop();
              if (toolInputs.containsKey(blockStop.index())) {
                  String accumulated = toolInputs.get(blockStop.index()).toString();
                  try {
                      IO.println("Tool input: " + objectMapper.readTree(accumulated));
                  } catch (JsonProcessingException e) {
                      // The accumulated string is not guaranteed to be valid JSON.
                      // See "Handling invalid JSON in tool responses" on this page.
                      IO.println("Invalid tool input: " + accumulated);
                  }
              }
          }
      }
  }
  ```

  ```php PHP
  use Anthropic\Client;
  use Anthropic\Messages\InputJSONDelta;
  use Anthropic\Messages\Model;
  use Anthropic\Messages\RawContentBlockDeltaEvent;
  use Anthropic\Messages\RawContentBlockStartEvent;
  use Anthropic\Messages\RawContentBlockStopEvent;
  use Anthropic\Messages\ToolUseBlock;

  $client = new Client();

  // The PHP SDK does not provide a stream accumulator for tool input;
  // the manual pattern shown here is the supported approach.
  $toolInputs = []; // index => accumulated JSON string

  $stream = $client->messages->createStream(
      maxTokens: 1024,
      model: Model::CLAUDE_OPUS_4_8,
      tools: [
          [
              'name' => 'get_weather',
              'description' => 'Get current weather for a city',
              'eager_input_streaming' => true,
              'input_schema' => [
                  'type' => 'object',
                  'properties' => ['city' => ['type' => 'string']],
                  'required' => ['city'],
              ],
          ],
      ],
      messages: [['role' => 'user', 'content' => 'Weather in Paris?']],
  );

  foreach ($stream as $event) {
      if (
          $event instanceof RawContentBlockStartEvent
          && $event->contentBlock instanceof ToolUseBlock
      ) {
          $toolInputs[$event->index] = '';
      } elseif (
          $event instanceof RawContentBlockDeltaEvent
          && $event->delta instanceof InputJSONDelta
      ) {
          $toolInputs[$event->index] .= $event->delta->partialJSON;
      } elseif (
          $event instanceof RawContentBlockStopEvent
          && isset($toolInputs[$event->index])
      ) {
          $accumulated = $toolInputs[$event->index];
          try {
              $parsed = json_decode($accumulated, associative: true, flags: JSON_THROW_ON_ERROR);
              echo "Tool input: " . json_encode($parsed) . "\n";
          } catch (JsonException $e) {
              // The accumulated string is not guaranteed to be valid JSON.
              // See "Handling invalid JSON in tool responses" on this page.
              echo "Invalid tool input: {$accumulated}\n";
          }
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  tool_inputs = {} # index -> accumulated JSON string

  stream = client.messages.stream_raw(
    model: Anthropic::Models::Model::CLAUDE_OPUS_4_8,
    max_tokens: 1024,
    tools: [
      {
        name: "get_weather",
        description: "Get current weather for a city",
        eager_input_streaming: true,
        input_schema: {
          type: "object",
          properties: {city: {type: "string"}},
          required: ["city"]
        }
      }
    ],
    messages: [{role: "user", content: "Weather in Paris?"}]
  )

  stream.each do |event|
    case event
    when Anthropic::Models::RawContentBlockStartEvent
      tool_inputs[event.index] = +"" if event.content_block.type == :tool_use
    when Anthropic::Models::RawContentBlockDeltaEvent
      if event.delta.is_a?(Anthropic::Models::InputJSONDelta)
        tool_inputs[event.index] << event.delta.partial_json
      end
    when Anthropic::Models::RawContentBlockStopEvent
      if tool_inputs.key?(event.index)
        accumulated = tool_inputs[event.index]
        begin
          parsed = JSON.parse(accumulated)
          puts "Tool input: #{parsed}"
        rescue JSON::ParserError
          # The accumulated string is not guaranteed to be valid JSON.
          # See "Handling invalid JSON in tool responses" on this page.
          puts "Invalid tool input: #{accumulated}"
        end
      end
    end
  end
  ```
</CodeGroup>

<Tip>
  Reacting to fragments and assembling them are separate concerns. The first example reacts to each fragment as it arrives and still hands assembly to the SDK in the tabs that use an accumulator helper. Use the manual pattern when you are not using an accumulator helper or when you want full control over assembly.
</Tip>

## Handling invalid JSON in tool responses

With fine-grained tool streaming, the accumulated input for a tool call might be invalid or incomplete JSON. When it is, you cannot run the tool, so report the failure back to Claude instead. The `content` of a tool result does not have to be JSON, but wrapping the raw string in a JSON object under a single key makes it unambiguous to Claude that you received invalid JSON, and preserves the original input for debugging:

```json
{
  "INVALID_JSON": "<the unparseable input you received>"
}
```

Return the wrapper, serialized to a string, as the `content` of a [tool result](/docs/en/agents-and-tools/tool-use/handle-tool-calls#handling-errors-with-is-error) content block with `is_error` set to `true`:

```json
{
  "type": "tool_result",
  "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
  "is_error": true,
  "content": "{\"INVALID_JSON\": \"<the unparseable input you received>\"}"
}
```

<Note>
  Build the wrapper with your JSON library rather than by concatenating strings, so quotes and other special characters in the invalid input are escaped correctly.
</Note>

## Next steps

<CardGroup cols={2}>
  <Card title="Context windows" icon="stack" href="/docs/en/build-with-claude/context-windows">
    Understand how the context window works, how extended thinking and tool use count toward it, and how to manage context as conversations grow.
  </Card>

  <Card title="Streaming messages" icon="lightning" href="/docs/en/build-with-claude/streaming">
    Stream Messages API responses incrementally with server-sent events, including text, tool use, and extended thinking deltas.
  </Card>

  <Card title="Handle tool calls" icon="arrows-left-right" href="/docs/en/agents-and-tools/tool-use/handle-tool-calls">
    Parse tool\_use blocks, format tool\_result responses, and handle errors with is\_error.
  </Card>

  <Card title="Tool reference" icon="book" href="/docs/en/agents-and-tools/tool-use/tool-reference">
    Directory of Anthropic-provided tools and reference for optional tool definition properties.
  </Card>
</CardGroup>
