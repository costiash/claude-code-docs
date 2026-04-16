# Fine-grained tool streaming

Stream tool inputs character-by-character for latency-sensitive applications.

---

<Note>
This feature is eligible for [Zero Data Retention (ZDR)](/docs/en/build-with-claude/api-and-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.
</Note>

Fine-grained tool streaming is generally available on all models and all platforms. It enables [streaming](/docs/en/build-with-claude/streaming) of tool use parameter values without buffering or JSON validation, reducing the latency to begin receiving large parameters.

<Warning>
When using fine-grained tool streaming, you may potentially receive invalid or partial JSON inputs. Make sure to account for these edge cases in your code.
</Warning>

## How to use fine-grained tool streaming
Fine-grained tool streaming is available on all models and all platforms (Claude API, Amazon Bedrock, Google Vertex AI, and Microsoft Foundry). To use it, set `eager_input_streaming` to `true` on any user-defined tool where you want fine-grained streaming enabled, and enable streaming on your request.

Here's an example of how to use fine-grained tool streaming with the API:

<CodeGroup>

  ```bash Shell
  curl https://api.anthropic.com/v1/messages \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -d '{
      "model": "claude-opus-4-7",
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
  ant messages create --stream \
    --transform usage <<'YAML'
  model: claude-opus-4-7
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
  ```

  ```python Python hidelines={1..2}
  import anthropic

  client = anthropic.Anthropic()

  with client.messages.stream(
      max_tokens=65536,
      model="claude-opus-4-7",
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
          pass
      final_message = stream.get_final_message()

  print(final_message.usage)
  ```

  ```typescript TypeScript hidelines={1..2}
  import Anthropic from "@anthropic-ai/sdk";

  const anthropic = new Anthropic();

  const stream = anthropic.messages.stream({
    model: "claude-opus-4-7",
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
  console.log(message.usage);
  ```
</CodeGroup>

In this example, fine-grained tool streaming enables Claude to stream the lines of a long poem into the tool call `make_file` without buffering to validate if the `lines_of_text` parameter is valid JSON. This means you can see the parameter stream as it arrives, without having to wait for the entire parameter to buffer and validate.

<Note>
With fine-grained tool streaming, tool use chunks start streaming faster, and are often longer and contain fewer word breaks. This is due to differences in chunking behavior.

Example:

Without fine-grained streaming (15s delay):
```text
Chunk 1: '{"'
Chunk 2: 'query": "Ty'
Chunk 3: 'peScri'
Chunk 4: 'pt 5.0 5.1 '
Chunk 5: '5.2 5'
Chunk 6: '.3'
Chunk 8: ' new f'
Chunk 9: 'eatur'
...
```

With fine-grained streaming (3s delay):
```text
Chunk 1: '{"query": "TypeScript 5.0 5.1 5.2 5.3'
Chunk 2: ' new features comparison'
```
</Note>

<Warning>
Because fine-grained streaming sends parameters without buffering or JSON validation, there is no guarantee that the resulting stream will complete in a valid JSON string.
Particularly, if the [stop reason](/docs/en/build-with-claude/handling-stop-reasons) `max_tokens` is reached, the stream may end midway through a parameter and may be incomplete. You generally have to write specific support to handle when `max_tokens` is reached.
</Warning>

## Accumulating tool input deltas

When a `tool_use` content block streams, the initial `content_block_start` event contains `input: {}` (an empty object). This is a placeholder. The actual input arrives as a series of `input_json_delta` events, each carrying a `partial_json` string fragment. Your code must concatenate these fragments and parse the result once the block closes.

The accumulation contract:

1. On `content_block_start` with `type: "tool_use"`, initialize an empty string: `input_json = ""`
2. For each `content_block_delta` with `type: "input_json_delta"`, append: `input_json += event.delta.partial_json`
3. On `content_block_stop`, parse the accumulated string: `json.loads(input_json)`

The type mismatch between the initial `input: {}` (object) and `partial_json` (string) is by design. The empty object marks the slot in the content array; the delta strings build the real value.

<CodeGroup>

```python Python
import json
import anthropic

client = anthropic.Anthropic()

tool_inputs = {}  # index -> accumulated JSON string

with client.messages.stream(
    model="claude-opus-4-7",
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
        if (
            event.type == "content_block_start"
            and event.content_block.type == "tool_use"
        ):
            tool_inputs[event.index] = ""
        elif (
            event.type == "content_block_delta"
            and event.delta.type == "input_json_delta"
        ):
            tool_inputs[event.index] += event.delta.partial_json
        elif event.type == "content_block_stop" and event.index in tool_inputs:
            parsed = json.loads(tool_inputs[event.index])
            print(f"Tool input: {parsed}")
```

```typescript TypeScript hidelines={1..4}
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic();

const toolInputs: Record<number, string> = {};

const stream = anthropic.messages.stream({
  model: "claude-opus-4-7",
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
    toolInputs[event.index] = "";
  } else if (event.type === "content_block_delta" && event.delta.type === "input_json_delta") {
    toolInputs[event.index] += event.delta.partial_json;
  } else if (event.type === "content_block_stop" && event.index in toolInputs) {
    const parsed = JSON.parse(toolInputs[event.index]);
    console.log("Tool input:", parsed);
  }
}
```

</CodeGroup>

<Tip>
The Python and TypeScript SDKs provide higher-level stream helpers (`stream.get_final_message()`, `stream.finalMessage()`) that perform this accumulation for you. Use the manual pattern above only when you need to react to partial input before the block closes, such as rendering a progress indicator or starting a downstream request early.
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