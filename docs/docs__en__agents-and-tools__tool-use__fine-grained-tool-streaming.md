# Fine-grained tool streaming

Stream tool inputs without server-side JSON buffering for latency-sensitive applications.

---

<Note>
This feature is eligible for [Zero Data Retention (ZDR)](/docs/en/build-with-claude/api-and-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.
</Note>

Fine-grained tool streaming is available on all models and all platforms. It enables [streaming](/docs/en/build-with-claude/streaming) of tool use parameter values without buffering or JSON validation, reducing the latency to begin receiving large parameters.

<Warning>
When using fine-grained tool streaming, you may potentially receive invalid or partial JSON inputs. Make sure to account for these edge cases in your code.
</Warning>

## How to use fine-grained tool streaming
Fine-grained tool streaming is supported on the Claude API, [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws), [Amazon Bedrock](/docs/en/build-with-claude/claude-in-amazon-bedrock), [Vertex AI](/docs/en/build-with-claude/claude-on-vertex-ai), and [Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry). To use it, set `eager_input_streaming` to `true` on any user-defined tool where you want fine-grained streaming enabled, and enable streaming on your request.

Here's an example of how to use fine-grained tool streaming with the API:

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
    jq 'select(.type == "message_delta") | .usage'
  ```

  ```python Python hidelines={1..2}
  import anthropic

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
      final_message = stream.get_final_message()

  print(f"Input tokens: {final_message.usage.input_tokens}")
  print(f"Output tokens: {final_message.usage.output_tokens}")
  ```

  ```typescript TypeScript hidelines={1..2}
  import Anthropic from "@anthropic-ai/sdk";

  const anthropic = new Anthropic();

  const stream = anthropic.messages.stream({
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

  const message = await stream.finalMessage();
  console.log(`Input tokens: ${message.usage.input_tokens}`);
  console.log(`Output tokens: ${message.usage.output_tokens}`);
  ```

  ```csharp C# hidelines={1..4}
  using System.Text.Json;
  using Anthropic;
  using Anthropic.Models.Messages;

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

  long inputTokens = 0;
  long outputTokens = 0;

  await foreach (var streamEvent in client.Messages.CreateStreaming(parameters))
  {
      switch (streamEvent.Value)
      {
          case RawMessageStartEvent startEvent:
              inputTokens = startEvent.Message.Usage.InputTokens;
              break;
          case RawMessageDeltaEvent deltaEvent:
              outputTokens = deltaEvent.Usage.OutputTokens;
              break;
      }
  }

  Console.WriteLine($"Input tokens: {inputTokens}");
  Console.WriteLine($"Output tokens: {outputTokens}");
  ```

  ```go Go hidelines={1..10,-1}
  package main

  import (
  	"context"
  	"fmt"

  	"github.com/anthropics/anthropic-sdk-go"
  )

  func main() {
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
  	}
  	if err := stream.Err(); err != nil {
  		panic(err)
  	}

  	fmt.Printf("Input tokens: %d\n", message.Usage.InputTokens)
  	fmt.Printf("Output tokens: %d\n", message.Usage.OutputTokens)
  }
  ```

  ```java Java hidelines={1..12,-1}
  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.core.JsonValue;
  import com.anthropic.core.http.StreamResponse;
  import com.anthropic.helpers.MessageAccumulator;
  import com.anthropic.models.messages.MessageCreateParams;
  import com.anthropic.models.messages.Model;
  import com.anthropic.models.messages.RawMessageStreamEvent;
  import com.anthropic.models.messages.Tool;
  import com.anthropic.models.messages.Usage;

  void main() {
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
          streamResponse.stream().forEach(accumulator::accumulate);
      }

      Usage usage = accumulator.message().usage();
      IO.println("Input tokens: " + usage.inputTokens());
      IO.println("Output tokens: " + usage.outputTokens());
  }
  ```

  ```php PHP hidelines={1..2}
  <?php

  use Anthropic\Client;
  use Anthropic\Messages\Model;
  use Anthropic\Messages\RawMessageDeltaEvent;
  use Anthropic\Messages\RawMessageStartEvent;

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

  $inputTokens = 0;
  $outputTokens = 0;

  foreach ($stream as $event) {
      if ($event instanceof RawMessageStartEvent) {
          $inputTokens = $event->message->usage->inputTokens;
      } elseif ($event instanceof RawMessageDeltaEvent) {
          $outputTokens = $event->usage->outputTokens;
      }
  }

  echo "Input tokens: {$inputTokens}\n";
  echo "Output tokens: {$outputTokens}\n";
  ```

  ```ruby Ruby hidelines={1..2}
  require "anthropic"

  anthropic = Anthropic::Client.new

  stream = anthropic.messages.stream(
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

  usage = stream.accumulated_message.usage
  puts "Input tokens: #{usage.input_tokens}"
  puts "Output tokens: #{usage.output_tokens}"
  ```

</CodeGroup>

In this example, fine-grained tool streaming enables Claude to stream the lines of a long poem into the tool call `make_file` without buffering to validate if the `lines_of_text` parameter is valid JSON. This means you can see the parameter stream as it arrives, without having to wait for the entire parameter to buffer and validate.

<Note>
With fine-grained tool streaming, tool input chunks start arriving sooner because the server skips JSON-validation buffering. Chunks are typically longer and contain fewer mid-token breaks as a side effect.
</Note>

<Warning>
Because fine-grained streaming sends parameters without buffering or JSON validation, there is no guarantee that the resulting stream will complete in a valid JSON string.
Particularly, if the [stop reason](/docs/en/build-with-claude/handling-stop-reasons) `max_tokens` is reached, the stream may end midway through a parameter and may be incomplete. You generally have to write specific support to handle when `max_tokens` is reached.
</Warning>

## Accumulating tool input deltas

When a `tool_use` content block streams, the initial `content_block_start` event contains `input: {}` (an empty object). This is a placeholder. The actual input arrives as a series of `input_json_delta` events, each carrying a `partial_json` string fragment. To assemble the full input, concatenate these fragments and parse the result when the block closes.

Where your SDK provides an accumulator helper (as used in the first example on this page), it handles this for you. The manual pattern is for SDKs without a helper, or when you need to react to partial input before the block closes.

The accumulation contract:

1. On `content_block_start` with `type: "tool_use"`, initialize an empty string: `input_json = ""`
2. For each `content_block_delta` with `type: "input_json_delta"`, append: `input_json += event.delta.partial_json`
3. On `content_block_stop`, parse the accumulated string: `json.loads(input_json)`

The type mismatch between the initial `input: {}` (object) and `partial_json` (string) is by design. The empty object marks the slot in the content array; the delta strings build the real value.

<CodeGroup>

  ```python Python hidelines={1..3}
  import json
  import anthropic

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
                  parsed = json.loads(tool_inputs[event.index])
                  print(f"Tool input: {parsed}")
  ```

  ```typescript TypeScript hidelines={1..2}
  import Anthropic from "@anthropic-ai/sdk";

  const anthropic = new Anthropic();

  const toolInputs = new Map<number, string>();

  const stream = anthropic.messages.stream({
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
      const parsed = JSON.parse(toolInputs.get(event.index)!);
      console.log("Tool input:", parsed);
    }
  }
  ```

  ```csharp C# hidelines={1..5}
  using System.Text;
  using System.Text.Json;
  using Anthropic;
  using Anthropic.Models.Messages;

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
  // The C# SDK does not currently provide a stream accumulator for tool input;
  // the manual pattern shown here is the supported approach.
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
          using var parsed = JsonDocument.Parse(accumulated.ToString());
          Console.WriteLine($"Tool input: {parsed.RootElement}");
      }
  }
  ```

  ```go Go hidelines={1..11,-1}
  package main

  import (
  	"context"
  	"encoding/json"
  	"fmt"

  	"github.com/anthropics/anthropic-sdk-go"
  )

  func main() {
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
  					panic(err)
  				}
  				fmt.Println("Tool input:", parsed)
  			}
  		}
  	}
  	if err := stream.Err(); err != nil {
  		panic(err)
  	}
  }
  ```

  ```java Java hidelines={1..11,-1}
  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.core.JsonValue;
  import com.anthropic.core.http.StreamResponse;
  import com.anthropic.models.messages.MessageCreateParams;
  import com.anthropic.models.messages.Model;
  import com.anthropic.models.messages.RawMessageStreamEvent;
  import com.anthropic.models.messages.Tool;
  import com.fasterxml.jackson.databind.ObjectMapper;

  void main() throws Exception {
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
                      var parsedInput = objectMapper.readTree(toolInputs.get(blockStop.index()).toString());
                      IO.println("Tool input: " + parsedInput);
                  }
              }
          }
      }
  }
  ```

  ```php PHP hidelines={1..2}
  <?php

  use Anthropic\Client;
  use Anthropic\Messages\InputJSONDelta;
  use Anthropic\Messages\Model;
  use Anthropic\Messages\RawContentBlockDeltaEvent;
  use Anthropic\Messages\RawContentBlockStartEvent;
  use Anthropic\Messages\RawContentBlockStopEvent;
  use Anthropic\Messages\ToolUseBlock;

  $client = new Client();

  // The PHP SDK does not currently provide a stream accumulator for tool input;
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
          $parsed = json_decode($toolInputs[$event->index], associative: true, flags: JSON_THROW_ON_ERROR);
          echo "Tool input: " . json_encode($parsed) . "\n";
      }
  }
  ```

  ```ruby Ruby hidelines={1..3}
  require "anthropic"
  require "json"

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
        parsed = JSON.parse(tool_inputs[event.index])
        puts "Tool input: #{parsed}"
      end
    end
  end
  ```

</CodeGroup>

<Tip>
Reach for the manual pattern when you need to react to partial input before the block closes (for example, rendering a progress indicator). Otherwise, prefer your SDK's accumulator helper where the first example on this page uses one.
</Tip>

## Handling invalid JSON in tool responses

When using fine-grained tool streaming, you may receive invalid or incomplete JSON from the model. If you need to pass this invalid JSON back to the model in an error response block, you may wrap it in a JSON object to ensure proper handling (with a reasonable key). For example:

```json
{
  "INVALID_JSON": "<your invalid json string>"
}
```

This approach helps the model understand that the content is invalid JSON while preserving the original malformed data for debugging purposes.

<Note>
When wrapping invalid JSON, make sure to properly escape any quotes or special characters in the invalid JSON string to maintain valid JSON structure in the wrapper object.
</Note>

## Next steps

<CardGroup cols={3}>
  <Card title="Streaming messages" href="/docs/en/build-with-claude/streaming">
    Full reference for server-sent events and stream event types.
  </Card>
  <Card title="Handle tool calls" href="/docs/en/agents-and-tools/tool-use/handle-tool-calls">
    Execute tools and return results in the required message format.
  </Card>
  <Card title="Tool reference" href="/docs/en/agents-and-tools/tool-use/tool-reference">
    Full directory of Anthropic-schema tools and their version strings.
  </Card>
</CardGroup>