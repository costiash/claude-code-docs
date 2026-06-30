# Messages

## Create a Message

`$client->messages->create(int maxTokens, list<MessageParam> messages, Model model, ?CacheControlEphemeral cacheControl, ?string container, ?string inferenceGeo, ?Metadata metadata, ?OutputConfig outputConfig, ?ServiceTier serviceTier, ?list<string> stopSequences, ?System system, ?float temperature, ?ThinkingConfigParam thinking, ?ToolChoice toolChoice, ?list<ToolUnion> tools, ?int topK, ?float topP, ?string userProfileID): Message`

**post** `/v1/messages`

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://platform.claude.com/docs/en/get-started)

### Parameters

- `maxTokens: int`

  The maximum number of tokens to generate before stopping.

  Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

  Set to `0` to populate the [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.

  Different models have different maximum values for this parameter.  See [models](https://platform.claude.com/docs/en/about-claude/models/overview) for details.

- `messages: list<MessageParam>`

  Input messages.

  Our models are trained to operate on alternating `user` and `assistant` conversational turns. When creating a new `Message`, you specify the prior conversational turns with the `messages` parameter, and the model then generates the next `Message` in the conversation. Consecutive `user` or `assistant` turns in your request will be combined into a single turn.

  Each input message must be an object with a `role` and `content`. You can specify a single `user`-role message, or you can include multiple `user` and `assistant` messages.

  If the final message uses the `assistant` role, the response content will continue immediately from the content in that message. This can be used to constrain part of the model's response.

  Example with a single `user` message:

  ```json
  [{"role": "user", "content": "Hello, Claude"}]
  ```

  Example with multiple conversational turns:

  ```json
  [
    {"role": "user", "content": "Hello there."},
    {"role": "assistant", "content": "Hi, I'm Claude. How can I help you?"},
    {"role": "user", "content": "Can you explain LLMs in plain English?"},
  ]
  ```

  Example with a partially-filled response from Claude:

  ```json
  [
    {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
    {"role": "assistant", "content": "The best answer is ("},
  ]
  ```

  Each input message `content` may be either a single `string` or an array of content blocks, where each block has a specific `type`. Using a `string` for `content` is shorthand for an array of one content block of type `"text"`. The following input messages are equivalent:

  ```json
  {"role": "user", "content": "Hello, Claude"}
  ```

  ```json
  {"role": "user", "content": [{"type": "text", "text": "Hello, Claude"}]}
  ```

  See [input examples](https://platform.claude.com/docs/en/build-with-claude/working-with-messages).

  Note that if you want to include a [system prompt](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.

  There is a limit of 100,000 messages in a single request.

- `model: Model`

  The model that will complete your prompt.

  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `cacheControl?:optional CacheControlEphemeral`

  Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

- `container?:optional string`

  Container identifier for reuse across requests.

- `inferenceGeo?:optional string`

  Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

- `metadata?:optional Metadata`

  An object describing metadata about the request.

- `outputConfig?:optional OutputConfig`

  Configuration options for the model's output, such as the output format.

- `serviceTier?:optional ServiceTier`

  Determines whether to use priority capacity (if available) or standard capacity for this request.

  Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers) for details.

- `stopSequences?:optional list<string>`

  Custom text sequences that will cause the model to stop generating.

  Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

  If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

- `stream?:optional bool`

  Whether to incrementally stream the response using server-sent events.

  See [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) for details.

- `system?:optional System`

  System prompt.

  A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

- `temperature?:optional float`

  Amount of randomness injected into the response.

  Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

  Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

- `thinking?:optional ThinkingConfigParam`

  Configuration for enabling Claude's extended thinking.

  When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

  See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

- `toolChoice?:optional ToolChoice`

  How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

- `tools?:optional list<ToolUnion>`

  Definitions of tools that the model may use.

  If you include `tools` in your API request, the model may return `tool_use` content blocks that represent the model's use of those tools. You can then run those tools using the tool input generated by the model and then optionally return results back to the model using `tool_result` content blocks.

  There are two types of tools: **client tools** and **server tools**. The behavior described below applies to client tools. For [server tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools), see their individual documentation as each has its own behavior (e.g., the [web search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)).

  Each tool definition includes:

  * `name`: Name of the tool.
  * `description`: Optional, but strongly-recommended description of the tool.
  * `input_schema`: [JSON schema](https://json-schema.org/draft/2020-12) for the tool `input` shape that the model will produce in `tool_use` output content blocks.

  For example, if you defined `tools` as:

  ```json
  [
    {
      "name": "get_stock_price",
      "description": "Get the current stock price for a given ticker symbol.",
      "input_schema": {
        "type": "object",
        "properties": {
          "ticker": {
            "type": "string",
            "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
          }
        },
        "required": ["ticker"]
      }
    }
  ]
  ```

  And then asked the model "What's the S&P 500 at today?", the model might produce `tool_use` content blocks in the response like this:

  ```json
  [
    {
      "type": "tool_use",
      "id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
      "name": "get_stock_price",
      "input": { "ticker": "^GSPC" }
    }
  ]
  ```

  You might then run your `get_stock_price` tool with `{"ticker": "^GSPC"}` as an input, and return the following back to the model in a subsequent `user` message:

  ```json
  [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
      "content": "259.75 USD"
    }
  ]
  ```

  Tools can be used for workflows that include running client-side tools and functions, or more generally whenever you want the model to produce a particular JSON structure of output.

  See our [guide](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) for more details.

- `topK?:optional int`

  Only sample from the top K options for each subsequent token.

  Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

  Recommended for advanced use cases only.

- `topP?:optional float`

  Use nucleus sampling.

  In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

  Recommended for advanced use cases only.

- `userProfileID?:optional string`

  The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header.

### Returns

- `Message`

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `?Container container`

    Information about the container used in the request (for the code execution tool)

  - `list<ContentBlock> content`

    Content generated by the model.

    This is an array of content blocks, each of which has a `type` that determines its shape.

    Example:

    ```json
    [{"type": "text", "text": "Hi, I'm Claude."}]
    ```

    If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

    For example, if the input `messages` were:

    ```json
    [
      {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
      {"role": "assistant", "content": "The best answer is ("}
    ]
    ```

    Then the response `content` might be:

    ```json
    [{"type": "text", "text": "B)"}]
    ```

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `"assistant" role`

    Conversational role of the generated message.

    This will always be `"assistant"`.

  - `?RefusalStopDetails stopDetails`

    Structured information about a refusal.

  - `?StopReason stopReason`

    The reason that we stopped.

    This may be one the following values:

    * `"end_turn"`: the model reached a natural stopping point
    * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
    * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
    * `"tool_use"`: the model invoked one or more tools
    * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
    * `"refusal"`: when streaming classifiers intervene to handle potential policy violations

    In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

  - `?string stopSequence`

    Which custom stop sequence was generated, if any.

    This value will be a non-null string if one of your custom stop sequences was generated.

  - `"message" type`

    Object type.

    For Messages, this is always `"message"`.

  - `Usage usage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$message = $client->messages->create(
  maxTokens: 1024,
  messages: [['content' => 'Hello, world', 'role' => 'user']],
  model: 'claude-opus-4-6',
  cacheControl: ['type' => 'ephemeral', 'ttl' => '5m'],
  container: 'container',
  inferenceGeo: 'inference_geo',
  metadata: ['userID' => '13803d75-b4b5-4c3e-b2a2-6f21399b021b'],
  outputConfig: [
    'effort' => 'low',
    'format' => ['schema' => ['foo' => 'bar'], 'type' => 'json_schema'],
  ],
  serviceTier: 'auto',
  stopSequences: ['string'],
  system: [
    [
      'text' => 'Today\'s date is 2024-06-01.',
      'type' => 'text',
      'cacheControl' => ['type' => 'ephemeral', 'ttl' => '5m'],
      'citations' => [
        [
          'citedText' => 'cited_text',
          'documentIndex' => 0,
          'documentTitle' => 'x',
          'endCharIndex' => 0,
          'startCharIndex' => 0,
          'type' => 'char_location',
        ],
      ],
    ],
  ],
  temperature: 1,
  thinking: ['type' => 'adaptive', 'display' => 'summarized'],
  toolChoice: ['type' => 'auto', 'disableParallelToolUse' => true],
  tools: [
    [
      'inputSchema' => [
        'type' => 'object',
        'properties' => ['location' => 'bar', 'unit' => 'bar'],
        'required' => ['location'],
      ],
      'name' => 'name',
      'allowedCallers' => ['direct'],
      'cacheControl' => ['type' => 'ephemeral', 'ttl' => '5m'],
      'deferLoading' => true,
      'description' => 'Get the current weather in a given location',
      'eagerInputStreaming' => true,
      'inputExamples' => [['foo' => 'bar']],
      'strict' => true,
      'type' => 'custom',
    ],
  ],
  topK: 5,
  topP: 0.7,
  userProfileID: 'anthropic-user-profile-id',
);

var_dump($message);
```

#### Response

```json
{
  "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
  "container": {
    "id": "id",
    "expires_at": "2019-12-27T18:11:19.117Z"
  },
  "content": [
    {
      "citations": [
        {
          "cited_text": "cited_text",
          "document_index": 0,
          "document_title": "document_title",
          "end_char_index": 0,
          "file_id": "file_id",
          "start_char_index": 0,
          "type": "char_location"
        }
      ],
      "text": "Hi! My name is Claude.",
      "type": "text"
    }
  ],
  "model": "claude-opus-4-6",
  "role": "assistant",
  "stop_details": {
    "category": "cyber",
    "explanation": "explanation",
    "type": "refusal"
  },
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "type": "message",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_creation_input_tokens": 2051,
    "cache_read_input_tokens": 2051,
    "inference_geo": "inference_geo",
    "input_tokens": 2095,
    "output_tokens": 503,
    "output_tokens_details": {
      "thinking_tokens": 0
    },
    "server_tool_use": {
      "web_fetch_requests": 2,
      "web_search_requests": 0
    },
    "service_tier": "standard"
  }
}
```

## Count tokens in a Message

`$client->messages->countTokens(list<MessageParam> messages, Model model, ?CacheControlEphemeral cacheControl, ?OutputConfig outputConfig, ?System system, ?ThinkingConfigParam thinking, ?ToolChoice toolChoice, ?list<MessageCountTokensTool> tools, ?string userProfileID): MessageTokensCount`

**post** `/v1/messages/count_tokens`

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://platform.claude.com/docs/en/build-with-claude/token-counting)

### Parameters

- `messages: list<MessageParam>`

  Input messages.

  Our models are trained to operate on alternating `user` and `assistant` conversational turns. When creating a new `Message`, you specify the prior conversational turns with the `messages` parameter, and the model then generates the next `Message` in the conversation. Consecutive `user` or `assistant` turns in your request will be combined into a single turn.

  Each input message must be an object with a `role` and `content`. You can specify a single `user`-role message, or you can include multiple `user` and `assistant` messages.

  If the final message uses the `assistant` role, the response content will continue immediately from the content in that message. This can be used to constrain part of the model's response.

  Example with a single `user` message:

  ```json
  [{"role": "user", "content": "Hello, Claude"}]
  ```

  Example with multiple conversational turns:

  ```json
  [
    {"role": "user", "content": "Hello there."},
    {"role": "assistant", "content": "Hi, I'm Claude. How can I help you?"},
    {"role": "user", "content": "Can you explain LLMs in plain English?"},
  ]
  ```

  Example with a partially-filled response from Claude:

  ```json
  [
    {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
    {"role": "assistant", "content": "The best answer is ("},
  ]
  ```

  Each input message `content` may be either a single `string` or an array of content blocks, where each block has a specific `type`. Using a `string` for `content` is shorthand for an array of one content block of type `"text"`. The following input messages are equivalent:

  ```json
  {"role": "user", "content": "Hello, Claude"}
  ```

  ```json
  {"role": "user", "content": [{"type": "text", "text": "Hello, Claude"}]}
  ```

  See [input examples](https://platform.claude.com/docs/en/build-with-claude/working-with-messages).

  Note that if you want to include a [system prompt](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.

  There is a limit of 100,000 messages in a single request.

- `model: Model`

  The model that will complete your prompt.

  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `cacheControl?:optional CacheControlEphemeral`

  Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

- `outputConfig?:optional OutputConfig`

  Configuration options for the model's output, such as the output format.

- `system?:optional System`

  System prompt.

  A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

- `thinking?:optional ThinkingConfigParam`

  Configuration for enabling Claude's extended thinking.

  When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

  See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

- `toolChoice?:optional ToolChoice`

  How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

- `tools?:optional list<MessageCountTokensTool>`

  Definitions of tools that the model may use.

  If you include `tools` in your API request, the model may return `tool_use` content blocks that represent the model's use of those tools. You can then run those tools using the tool input generated by the model and then optionally return results back to the model using `tool_result` content blocks.

  There are two types of tools: **client tools** and **server tools**. The behavior described below applies to client tools. For [server tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools), see their individual documentation as each has its own behavior (e.g., the [web search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)).

  Each tool definition includes:

  * `name`: Name of the tool.
  * `description`: Optional, but strongly-recommended description of the tool.
  * `input_schema`: [JSON schema](https://json-schema.org/draft/2020-12) for the tool `input` shape that the model will produce in `tool_use` output content blocks.

  For example, if you defined `tools` as:

  ```json
  [
    {
      "name": "get_stock_price",
      "description": "Get the current stock price for a given ticker symbol.",
      "input_schema": {
        "type": "object",
        "properties": {
          "ticker": {
            "type": "string",
            "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
          }
        },
        "required": ["ticker"]
      }
    }
  ]
  ```

  And then asked the model "What's the S&P 500 at today?", the model might produce `tool_use` content blocks in the response like this:

  ```json
  [
    {
      "type": "tool_use",
      "id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
      "name": "get_stock_price",
      "input": { "ticker": "^GSPC" }
    }
  ]
  ```

  You might then run your `get_stock_price` tool with `{"ticker": "^GSPC"}` as an input, and return the following back to the model in a subsequent `user` message:

  ```json
  [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
      "content": "259.75 USD"
    }
  ]
  ```

  Tools can be used for workflows that include running client-side tools and functions, or more generally whenever you want the model to produce a particular JSON structure of output.

  See our [guide](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) for more details.

- `userProfileID?:optional string`

  The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header.

### Returns

- `MessageTokensCount`

  - `int inputTokens`

    The total number of tokens across the provided list of messages, system prompt, and tools.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$messageTokensCount = $client->messages->countTokens(
  messages: [['content' => 'Hello, world', 'role' => 'user']],
  model: 'claude-opus-4-6',
  cacheControl: ['type' => 'ephemeral', 'ttl' => '5m'],
  outputConfig: [
    'effort' => 'low',
    'format' => ['schema' => ['foo' => 'bar'], 'type' => 'json_schema'],
  ],
  system: [
    [
      'text' => 'Today\'s date is 2024-06-01.',
      'type' => 'text',
      'cacheControl' => ['type' => 'ephemeral', 'ttl' => '5m'],
      'citations' => [
        [
          'citedText' => 'cited_text',
          'documentIndex' => 0,
          'documentTitle' => 'x',
          'endCharIndex' => 0,
          'startCharIndex' => 0,
          'type' => 'char_location',
        ],
      ],
    ],
  ],
  thinking: ['type' => 'adaptive', 'display' => 'summarized'],
  toolChoice: ['type' => 'auto', 'disableParallelToolUse' => true],
  tools: [
    [
      'inputSchema' => [
        'type' => 'object',
        'properties' => ['location' => 'bar', 'unit' => 'bar'],
        'required' => ['location'],
      ],
      'name' => 'name',
      'allowedCallers' => ['direct'],
      'cacheControl' => ['type' => 'ephemeral', 'ttl' => '5m'],
      'deferLoading' => true,
      'description' => 'Get the current weather in a given location',
      'eagerInputStreaming' => true,
      'inputExamples' => [['foo' => 'bar']],
      'strict' => true,
      'type' => 'custom',
    ],
  ],
  userProfileID: 'anthropic-user-profile-id',
);

var_dump($messageTokensCount);
```

#### Response

```json
{
  "input_tokens": 2095
}
```

## Domain Types

### Base64 Image Source

- `Base64ImageSource`

  - `string data`

  - `MediaType mediaType`

  - `"base64" type`

### Base64 PDF Source

- `Base64PDFSource`

  - `string data`

  - `"application/pdf" mediaType`

  - `"base64" type`

### Bash Code Execution Output Block

- `BashCodeExecutionOutputBlock`

  - `string fileID`

  - `"bash_code_execution_output" type`

### Bash Code Execution Output Block Param

- `BashCodeExecutionOutputBlockParam`

  - `string fileID`

  - `"bash_code_execution_output" type`

### Bash Code Execution Result Block

- `BashCodeExecutionResultBlock`

  - `list<BashCodeExecutionOutputBlock> content`

  - `int returnCode`

  - `string stderr`

  - `string stdout`

  - `"bash_code_execution_result" type`

### Bash Code Execution Result Block Param

- `BashCodeExecutionResultBlockParam`

  - `list<BashCodeExecutionOutputBlockParam> content`

  - `int returnCode`

  - `string stderr`

  - `string stdout`

  - `"bash_code_execution_result" type`

### Bash Code Execution Tool Result Block

- `BashCodeExecutionToolResultBlock`

  - `Content content`

  - `string toolUseID`

  - `"bash_code_execution_tool_result" type`

### Bash Code Execution Tool Result Block Param

- `BashCodeExecutionToolResultBlockParam`

  - `Content content`

  - `string toolUseID`

  - `"bash_code_execution_tool_result" type`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Bash Code Execution Tool Result Error

- `BashCodeExecutionToolResultError`

  - `BashCodeExecutionToolResultErrorCode errorCode`

  - `"bash_code_execution_tool_result_error" type`

### Bash Code Execution Tool Result Error Code

- `BashCodeExecutionToolResultErrorCode`

  - `"invalid_tool_input"`

  - `"unavailable"`

  - `"too_many_requests"`

  - `"execution_time_exceeded"`

  - `"output_file_too_large"`

### Bash Code Execution Tool Result Error Param

- `BashCodeExecutionToolResultErrorParam`

  - `BashCodeExecutionToolResultErrorCode errorCode`

  - `"bash_code_execution_tool_result_error" type`

### Cache Control Ephemeral

- `CacheControlEphemeral`

  - `"ephemeral" type`

  - `?TTL ttl`

    The time-to-live for the cache control breakpoint.

    This may be one the following values:

    - `5m`: 5 minutes
    - `1h`: 1 hour

    Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

### Cache Creation

- `CacheCreation`

  - `int ephemeral1hInputTokens`

    The number of input tokens used to create the 1 hour cache entry.

  - `int ephemeral5mInputTokens`

    The number of input tokens used to create the 5 minute cache entry.

### Citation Char Location

- `CitationCharLocation`

  - `string citedText`

  - `int documentIndex`

  - `?string documentTitle`

  - `int endCharIndex`

  - `?string fileID`

  - `int startCharIndex`

  - `"char_location" type`

### Citation Char Location Param

- `CitationCharLocationParam`

  - `string citedText`

  - `int documentIndex`

  - `?string documentTitle`

  - `int endCharIndex`

  - `int startCharIndex`

  - `"char_location" type`

### Citation Content Block Location

- `CitationContentBlockLocation`

  - `string citedText`

    The full text of the cited block range, concatenated.

    Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

  - `int documentIndex`

  - `?string documentTitle`

  - `int endBlockIndex`

    Exclusive 0-based end index of the cited block range in the source's `content` array.

    Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

  - `?string fileID`

  - `int startBlockIndex`

    0-based index of the first cited block in the source's `content` array.

  - `"content_block_location" type`

### Citation Content Block Location Param

- `CitationContentBlockLocationParam`

  - `string citedText`

    The full text of the cited block range, concatenated.

    Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

  - `int documentIndex`

  - `?string documentTitle`

  - `int endBlockIndex`

    Exclusive 0-based end index of the cited block range in the source's `content` array.

    Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

  - `int startBlockIndex`

    0-based index of the first cited block in the source's `content` array.

  - `"content_block_location" type`

### Citation Page Location

- `CitationPageLocation`

  - `string citedText`

  - `int documentIndex`

  - `?string documentTitle`

  - `int endPageNumber`

  - `?string fileID`

  - `int startPageNumber`

  - `"page_location" type`

### Citation Page Location Param

- `CitationPageLocationParam`

  - `string citedText`

  - `int documentIndex`

  - `?string documentTitle`

  - `int endPageNumber`

  - `int startPageNumber`

  - `"page_location" type`

### Citation Search Result Location Param

- `CitationSearchResultLocationParam`

  - `string citedText`

    The full text of the cited block range, concatenated.

    Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

  - `int endBlockIndex`

    Exclusive 0-based end index of the cited block range in the source's `content` array.

    Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

  - `int searchResultIndex`

    0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

    Counted separately from `document_index`; server-side web search results are not included in this count.

  - `string source`

  - `int startBlockIndex`

    0-based index of the first cited block in the source's `content` array.

  - `?string title`

  - `"search_result_location" type`

### Citation Web Search Result Location Param

- `CitationWebSearchResultLocationParam`

  - `string citedText`

  - `string encryptedIndex`

  - `?string title`

  - `"web_search_result_location" type`

  - `string url`

### Citations Config

- `CitationsConfig`

  - `bool enabled`

### Citations Config Param

- `CitationsConfigParam`

  - `?bool enabled`

### Citations Delta

- `CitationsDelta`

  - `Citation citation`

  - `"citations_delta" type`

### Citations Search Result Location

- `CitationsSearchResultLocation`

  - `string citedText`

    The full text of the cited block range, concatenated.

    Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

  - `int endBlockIndex`

    Exclusive 0-based end index of the cited block range in the source's `content` array.

    Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

  - `int searchResultIndex`

    0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

    Counted separately from `document_index`; server-side web search results are not included in this count.

  - `string source`

  - `int startBlockIndex`

    0-based index of the first cited block in the source's `content` array.

  - `?string title`

  - `"search_result_location" type`

### Citations Web Search Result Location

- `CitationsWebSearchResultLocation`

  - `string citedText`

  - `string encryptedIndex`

  - `?string title`

  - `"web_search_result_location" type`

  - `string url`

### Code Execution Output Block

- `CodeExecutionOutputBlock`

  - `string fileID`

  - `"code_execution_output" type`

### Code Execution Output Block Param

- `CodeExecutionOutputBlockParam`

  - `string fileID`

  - `"code_execution_output" type`

### Code Execution Result Block

- `CodeExecutionResultBlock`

  - `list<CodeExecutionOutputBlock> content`

  - `int returnCode`

  - `string stderr`

  - `string stdout`

  - `"code_execution_result" type`

### Code Execution Result Block Param

- `CodeExecutionResultBlockParam`

  - `list<CodeExecutionOutputBlockParam> content`

  - `int returnCode`

  - `string stderr`

  - `string stdout`

  - `"code_execution_result" type`

### Code Execution Tool 20250522

- `CodeExecutionTool20250522`

  - `"code_execution" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"code_execution_20250522" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Code Execution Tool 20250825

- `CodeExecutionTool20250825`

  - `"code_execution" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"code_execution_20250825" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Code Execution Tool 20260120

- `CodeExecutionTool20260120`

  - `"code_execution" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"code_execution_20260120" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Code Execution Tool 20260521

- `CodeExecutionTool20260521`

  - `"code_execution" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"code_execution_20260521" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Code Execution Tool Result Block

- `CodeExecutionToolResultBlock`

  - `CodeExecutionToolResultBlockContent content`

    Code execution result with encrypted stdout for PFC + web_search results.

  - `string toolUseID`

  - `"code_execution_tool_result" type`

### Code Execution Tool Result Block Content

- `CodeExecutionToolResultBlockContent`

  - `CodeExecutionToolResultError`

    - `CodeExecutionToolResultErrorCode errorCode`

    - `"code_execution_tool_result_error" type`

  - `CodeExecutionResultBlock`

    - `list<CodeExecutionOutputBlock> content`

    - `int returnCode`

    - `string stderr`

    - `string stdout`

    - `"code_execution_result" type`

  - `EncryptedCodeExecutionResultBlock`

    - `list<CodeExecutionOutputBlock> content`

    - `string encryptedStdout`

    - `int returnCode`

    - `string stderr`

    - `"encrypted_code_execution_result" type`

### Code Execution Tool Result Block Param

- `CodeExecutionToolResultBlockParam`

  - `CodeExecutionToolResultBlockParamContent content`

    Code execution result with encrypted stdout for PFC + web_search results.

  - `string toolUseID`

  - `"code_execution_tool_result" type`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Code Execution Tool Result Block Param Content

- `CodeExecutionToolResultBlockParamContent`

  - `CodeExecutionToolResultErrorParam`

    - `CodeExecutionToolResultErrorCode errorCode`

    - `"code_execution_tool_result_error" type`

  - `CodeExecutionResultBlockParam`

    - `list<CodeExecutionOutputBlockParam> content`

    - `int returnCode`

    - `string stderr`

    - `string stdout`

    - `"code_execution_result" type`

  - `EncryptedCodeExecutionResultBlockParam`

    - `list<CodeExecutionOutputBlockParam> content`

    - `string encryptedStdout`

    - `int returnCode`

    - `string stderr`

    - `"encrypted_code_execution_result" type`

### Code Execution Tool Result Error

- `CodeExecutionToolResultError`

  - `CodeExecutionToolResultErrorCode errorCode`

  - `"code_execution_tool_result_error" type`

### Code Execution Tool Result Error Code

- `CodeExecutionToolResultErrorCode`

  - `"invalid_tool_input"`

  - `"unavailable"`

  - `"too_many_requests"`

  - `"execution_time_exceeded"`

### Code Execution Tool Result Error Param

- `CodeExecutionToolResultErrorParam`

  - `CodeExecutionToolResultErrorCode errorCode`

  - `"code_execution_tool_result_error" type`

### Container

- `Container`

  - `string id`

    Identifier for the container used in this request

  - `\Datetime expiresAt`

    The time at which the container will expire.

### Container Upload Block

- `ContainerUploadBlock`

  - `string fileID`

  - `"container_upload" type`

### Container Upload Block Param

- `ContainerUploadBlockParam`

  - `string fileID`

  - `"container_upload" type`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Content Block

- `ContentBlock`

  - `TextBlock`

    - `?list<TextCitation> citations`

      Citations supporting the text block.

      The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

    - `string text`

    - `"text" type`

  - `ThinkingBlock`

    - `string signature`

    - `string thinking`

    - `"thinking" type`

  - `RedactedThinkingBlock`

    - `string data`

    - `"redacted_thinking" type`

  - `ToolUseBlock`

    - `string id`

    - `Caller caller`

      Tool invocation directly from the model.

    - `array<string,mixed> input`

    - `string name`

    - `"tool_use" type`

  - `ServerToolUseBlock`

    - `string id`

    - `Caller caller`

      Tool invocation directly from the model.

    - `array<string,mixed> input`

    - `Name name`

    - `"server_tool_use" type`

  - `WebSearchToolResultBlock`

    - `Caller caller`

      Tool invocation directly from the model.

    - `WebSearchToolResultBlockContent content`

    - `string toolUseID`

    - `"web_search_tool_result" type`

  - `WebFetchToolResultBlock`

    - `Caller caller`

      Tool invocation directly from the model.

    - `Content content`

    - `string toolUseID`

    - `"web_fetch_tool_result" type`

  - `CodeExecutionToolResultBlock`

    - `CodeExecutionToolResultBlockContent content`

      Code execution result with encrypted stdout for PFC + web_search results.

    - `string toolUseID`

    - `"code_execution_tool_result" type`

  - `BashCodeExecutionToolResultBlock`

    - `Content content`

    - `string toolUseID`

    - `"bash_code_execution_tool_result" type`

  - `TextEditorCodeExecutionToolResultBlock`

    - `Content content`

    - `string toolUseID`

    - `"text_editor_code_execution_tool_result" type`

  - `ToolSearchToolResultBlock`

    - `Content content`

    - `string toolUseID`

    - `"tool_search_tool_result" type`

  - `ContainerUploadBlock`

    - `string fileID`

    - `"container_upload" type`

### Content Block Param

- `ContentBlockParam`

  - `TextBlockParam`

    - `string text`

    - `"text" type`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?list<TextCitationParam> citations`

  - `ImageBlockParam`

    - `Source source`

    - `"image" type`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

  - `DocumentBlockParam`

    - `Source source`

    - `"document" type`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?CitationsConfigParam citations`

    - `?string context`

    - `?string title`

  - `SearchResultBlockParam`

    - `list<TextBlockParam> content`

    - `string source`

    - `string title`

    - `"search_result" type`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?CitationsConfigParam citations`

  - `ThinkingBlockParam`

    - `string signature`

    - `string thinking`

    - `"thinking" type`

  - `RedactedThinkingBlockParam`

    - `string data`

    - `"redacted_thinking" type`

  - `ToolUseBlockParam`

    - `string id`

    - `array<string,mixed> input`

    - `string name`

    - `"tool_use" type`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?Caller caller`

      Tool invocation directly from the model.

  - `ToolResultBlockParam`

    - `string toolUseID`

    - `"tool_result" type`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?Content content`

    - `?bool isError`

  - `ServerToolUseBlockParam`

    - `string id`

    - `array<string,mixed> input`

    - `Name name`

    - `"server_tool_use" type`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?Caller caller`

      Tool invocation directly from the model.

  - `WebSearchToolResultBlockParam`

    - `WebSearchToolResultBlockParamContent content`

    - `string toolUseID`

    - `"web_search_tool_result" type`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?Caller caller`

      Tool invocation directly from the model.

  - `WebFetchToolResultBlockParam`

    - `Content content`

    - `string toolUseID`

    - `"web_fetch_tool_result" type`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?Caller caller`

      Tool invocation directly from the model.

  - `CodeExecutionToolResultBlockParam`

    - `CodeExecutionToolResultBlockParamContent content`

      Code execution result with encrypted stdout for PFC + web_search results.

    - `string toolUseID`

    - `"code_execution_tool_result" type`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

  - `BashCodeExecutionToolResultBlockParam`

    - `Content content`

    - `string toolUseID`

    - `"bash_code_execution_tool_result" type`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

  - `TextEditorCodeExecutionToolResultBlockParam`

    - `Content content`

    - `string toolUseID`

    - `"text_editor_code_execution_tool_result" type`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

  - `ToolSearchToolResultBlockParam`

    - `Content content`

    - `string toolUseID`

    - `"tool_search_tool_result" type`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

  - `ContainerUploadBlockParam`

    - `string fileID`

    - `"container_upload" type`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

  - `MidConversationSystemBlockParam`

    - `list<TextBlockParam> content`

      System instruction text blocks.

    - `"mid_conv_system" type`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

### Content Block Source

- `ContentBlockSource`

  - `Content content`

  - `"content" type`

### Content Block Source Content

- `ContentBlockSourceContent`

  - `TextBlockParam`

    - `string text`

    - `"text" type`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?list<TextCitationParam> citations`

  - `ImageBlockParam`

    - `Source source`

    - `"image" type`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

### Direct Caller

- `DirectCaller`

  - `"direct" type`

### Document Block

- `DocumentBlock`

  - `?CitationsConfig citations`

    Citation configuration for the document

  - `Source source`

  - `?string title`

    The title of the document

  - `"document" type`

### Document Block Param

- `DocumentBlockParam`

  - `Source source`

  - `"document" type`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?CitationsConfigParam citations`

  - `?string context`

  - `?string title`

### Encrypted Code Execution Result Block

- `EncryptedCodeExecutionResultBlock`

  - `list<CodeExecutionOutputBlock> content`

  - `string encryptedStdout`

  - `int returnCode`

  - `string stderr`

  - `"encrypted_code_execution_result" type`

### Encrypted Code Execution Result Block Param

- `EncryptedCodeExecutionResultBlockParam`

  - `list<CodeExecutionOutputBlockParam> content`

  - `string encryptedStdout`

  - `int returnCode`

  - `string stderr`

  - `"encrypted_code_execution_result" type`

### Image Block Param

- `ImageBlockParam`

  - `Source source`

  - `"image" type`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Input JSON Delta

- `InputJSONDelta`

  - `string partialJSON`

  - `"input_json_delta" type`

### JSON Output Format

- `JSONOutputFormat`

  - `array<string,mixed> schema`

    The JSON schema of the format

  - `"json_schema" type`

### Memory Tool 20250818

- `MemoryTool20250818`

  - `"memory" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"memory_20250818" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Message

- `Message`

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `?Container container`

    Information about the container used in the request (for the code execution tool)

  - `list<ContentBlock> content`

    Content generated by the model.

    This is an array of content blocks, each of which has a `type` that determines its shape.

    Example:

    ```json
    [{"type": "text", "text": "Hi, I'm Claude."}]
    ```

    If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

    For example, if the input `messages` were:

    ```json
    [
      {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
      {"role": "assistant", "content": "The best answer is ("}
    ]
    ```

    Then the response `content` might be:

    ```json
    [{"type": "text", "text": "B)"}]
    ```

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `"assistant" role`

    Conversational role of the generated message.

    This will always be `"assistant"`.

  - `?RefusalStopDetails stopDetails`

    Structured information about a refusal.

  - `?StopReason stopReason`

    The reason that we stopped.

    This may be one the following values:

    * `"end_turn"`: the model reached a natural stopping point
    * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
    * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
    * `"tool_use"`: the model invoked one or more tools
    * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
    * `"refusal"`: when streaming classifiers intervene to handle potential policy violations

    In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

  - `?string stopSequence`

    Which custom stop sequence was generated, if any.

    This value will be a non-null string if one of your custom stop sequences was generated.

  - `"message" type`

    Object type.

    For Messages, this is always `"message"`.

  - `Usage usage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

### Message Count Tokens Tool

- `MessageCountTokensTool`

  - `Tool`

    - `InputSchema inputSchema`

      [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

      This defines the shape of the `input` that your tool accepts and that the model will produce.

    - `string name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?string description`

      Description of what this tool does.

      Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

    - `?bool eagerInputStreaming`

      Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?Type type`

  - `ToolBash20250124`

    - `"bash" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"bash_20250124" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `CodeExecutionTool20250522`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"code_execution_20250522" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `CodeExecutionTool20250825`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"code_execution_20250825" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `CodeExecutionTool20260120`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"code_execution_20260120" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `CodeExecutionTool20260521`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"code_execution_20260521" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `MemoryTool20250818`

    - `"memory" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"memory_20250818" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `ToolTextEditor20250124`

    - `"str_replace_editor" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"text_editor_20250124" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `ToolTextEditor20250429`

    - `"str_replace_based_edit_tool" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"text_editor_20250429" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `ToolTextEditor20250728`

    - `"str_replace_based_edit_tool" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"text_editor_20250728" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?int maxCharacters`

      Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `WebSearchTool20250305`

    - `"web_search" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"web_search_20250305" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `?list<string> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?UserLocation userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `WebFetchTool20250910`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"web_fetch_20250910" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      List of domains to allow fetching from

    - `?list<string> blockedDomains`

      List of domains to block fetching from

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?CitationsConfigParam citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `WebSearchTool20260209`

    - `"web_search" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"web_search_20260209" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `?list<string> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?UserLocation userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `WebFetchTool20260209`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"web_fetch_20260209" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      List of domains to allow fetching from

    - `?list<string> blockedDomains`

      List of domains to block fetching from

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?CitationsConfigParam citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `WebFetchTool20260309`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"web_fetch_20260309" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      List of domains to allow fetching from

    - `?list<string> blockedDomains`

      List of domains to block fetching from

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?CitationsConfigParam citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?bool useCache`

      Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

  - `WebSearchTool20260318`

    - `"web_search" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"web_search_20260318" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `?list<string> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?ResponseInclusion responseInclusion`

      How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?UserLocation userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `WebFetchTool20260318`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"web_fetch_20260318" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      List of domains to allow fetching from

    - `?list<string> blockedDomains`

      List of domains to block fetching from

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?CitationsConfigParam citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?ResponseInclusion responseInclusion`

      How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?bool useCache`

      Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

  - `ToolSearchToolBm25_20251119`

    - `"tool_search_tool_bm25" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `Type type`

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `ToolSearchToolRegex20251119`

    - `"tool_search_tool_regex" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `Type type`

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

### Message Delta Usage

- `MessageDeltaUsage`

  - `?int cacheCreationInputTokens`

    The cumulative number of input tokens used to create the cache entry.

  - `?int cacheReadInputTokens`

    The cumulative number of input tokens read from the cache.

  - `?int inputTokens`

    The cumulative number of input tokens which were used.

  - `int outputTokens`

    The cumulative number of output tokens which were used.

  - `?OutputTokensDetails outputTokensDetails`

    Breakdown of output tokens by category.

    `output_tokens` remains the inclusive, authoritative total used for billing.
    This object provides a read-only decomposition for observability — for example,
    how many of the billed output tokens were spent on internal reasoning that may
    have been summarized before being returned to you.

  - `?ServerToolUsage serverToolUse`

    The number of server tool requests.

### Message Param

- `MessageParam`

  - `Content content`

  - `Role role`

### Message Tokens Count

- `MessageTokensCount`

  - `int inputTokens`

    The total number of tokens across the provided list of messages, system prompt, and tools.

### Metadata

- `Metadata`

  - `?string userID`

    An external identifier for the user who is associated with the request.

    This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

### Mid Conversation System Block Param

- `MidConversationSystemBlockParam`

  - `list<TextBlockParam> content`

    System instruction text blocks.

  - `"mid_conv_system" type`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Model

- `Model`

  - `"claude-fable-5"`

    Next generation of intelligence for the hardest knowledge work and coding problems

  - `"claude-mythos-5"`

    Most capable model for cybersecurity and biology research

  - `"claude-opus-4-8"`

    Frontier intelligence for long-running agents and coding

  - `"claude-opus-4-7"`

    Frontier intelligence for long-running agents and coding

  - `"claude-mythos-preview"`

    New class of intelligence, strongest in coding and cybersecurity

  - `"claude-opus-4-6"`

    Frontier intelligence for long-running agents and coding

  - `"claude-sonnet-4-6"`

    Best combination of speed and intelligence

  - `"claude-haiku-4-5"`

    Fastest model with near-frontier intelligence

  - `"claude-haiku-4-5-20251001"`

    Fastest model with near-frontier intelligence

  - `"claude-opus-4-5"`

    Premium model combining maximum intelligence with practical performance

  - `"claude-opus-4-5-20251101"`

    Premium model combining maximum intelligence with practical performance

  - `"claude-sonnet-4-5"`

    High-performance model for agents and coding

  - `"claude-sonnet-4-5-20250929"`

    High-performance model for agents and coding

  - `"claude-opus-4-1"`

    Exceptional model for specialized complex tasks

  - `"claude-opus-4-1-20250805"`

    Exceptional model for specialized complex tasks

### Output Config

- `OutputConfig`

  - `?Effort effort`

    All possible effort levels.

  - `?JSONOutputFormat format`

    A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

### Output Tokens Details

- `OutputTokensDetails`

  - `int thinkingTokens`

    Number of output tokens the model generated as internal reasoning, including
    the thinking-block delimiter tokens.

    Reflects the raw reasoning the model produced, not the (possibly shorter)
    summarized thinking text returned in the response body. Computed by
    re-tokenizing the raw reasoning text, so it may differ from the model's exact
    generation count by a small number of tokens. Always ≤ `output_tokens`;
    `output_tokens - thinking_tokens` approximates the non-reasoning output.

### Plain Text Source

- `PlainTextSource`

  - `string data`

  - `"text/plain" mediaType`

  - `"text" type`

### Raw Content Block Delta

- `RawContentBlockDelta`

  - `TextDelta`

    - `string text`

    - `"text_delta" type`

  - `InputJSONDelta`

    - `string partialJSON`

    - `"input_json_delta" type`

  - `CitationsDelta`

    - `Citation citation`

    - `"citations_delta" type`

  - `ThinkingDelta`

    - `string thinking`

    - `"thinking_delta" type`

  - `SignatureDelta`

    - `string signature`

    - `"signature_delta" type`

### Raw Content Block Delta Event

- `RawContentBlockDeltaEvent`

  - `RawContentBlockDelta delta`

  - `int index`

  - `"content_block_delta" type`

### Raw Content Block Start Event

- `RawContentBlockStartEvent`

  - `ContentBlock contentBlock`

    Response model for a file uploaded to the container.

  - `int index`

  - `"content_block_start" type`

### Raw Content Block Stop Event

- `RawContentBlockStopEvent`

  - `int index`

  - `"content_block_stop" type`

### Raw Message Delta Event

- `RawMessageDeltaEvent`

  - `Delta delta`

  - `"message_delta" type`

  - `MessageDeltaUsage usage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

### Raw Message Start Event

- `RawMessageStartEvent`

  - `Message message`

  - `"message_start" type`

### Raw Message Stop Event

- `RawMessageStopEvent`

  - `"message_stop" type`

### Raw Message Stream Event

- `RawMessageStreamEvent`

  - `RawMessageStartEvent`

    - `Message message`

    - `"message_start" type`

  - `RawMessageDeltaEvent`

    - `Delta delta`

    - `"message_delta" type`

    - `MessageDeltaUsage usage`

      Billing and rate-limit usage.

      Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

      Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

      For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

      Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

  - `RawMessageStopEvent`

    - `"message_stop" type`

  - `RawContentBlockStartEvent`

    - `ContentBlock contentBlock`

      Response model for a file uploaded to the container.

    - `int index`

    - `"content_block_start" type`

  - `RawContentBlockDeltaEvent`

    - `RawContentBlockDelta delta`

    - `int index`

    - `"content_block_delta" type`

  - `RawContentBlockStopEvent`

    - `int index`

    - `"content_block_stop" type`

### Redacted Thinking Block

- `RedactedThinkingBlock`

  - `string data`

  - `"redacted_thinking" type`

### Redacted Thinking Block Param

- `RedactedThinkingBlockParam`

  - `string data`

  - `"redacted_thinking" type`

### Refusal Stop Details

- `RefusalStopDetails`

  - `?Category category`

    The policy category that triggered a refusal.

  - `?string explanation`

    Human-readable explanation of the refusal.

    This text is not guaranteed to be stable. `null` when no explanation is available for the category.

  - `"refusal" type`

### Search Result Block Param

- `SearchResultBlockParam`

  - `list<TextBlockParam> content`

  - `string source`

  - `string title`

  - `"search_result" type`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?CitationsConfigParam citations`

### Server Tool Caller

- `ServerToolCaller`

  - `string toolID`

  - `"code_execution_20250825" type`

### Server Tool Caller 20260120

- `ServerToolCaller20260120`

  - `string toolID`

  - `"code_execution_20260120" type`

### Server Tool Usage

- `ServerToolUsage`

  - `int webFetchRequests`

    The number of web fetch tool requests.

  - `int webSearchRequests`

    The number of web search tool requests.

### Server Tool Use Block

- `ServerToolUseBlock`

  - `string id`

  - `Caller caller`

    Tool invocation directly from the model.

  - `array<string,mixed> input`

  - `Name name`

  - `"server_tool_use" type`

### Server Tool Use Block Param

- `ServerToolUseBlockParam`

  - `string id`

  - `array<string,mixed> input`

  - `Name name`

  - `"server_tool_use" type`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?Caller caller`

    Tool invocation directly from the model.

### Signature Delta

- `SignatureDelta`

  - `string signature`

  - `"signature_delta" type`

### Stop Reason

- `StopReason`

  - `"end_turn"`

  - `"max_tokens"`

  - `"stop_sequence"`

  - `"tool_use"`

  - `"pause_turn"`

  - `"refusal"`

### Text Block

- `TextBlock`

  - `?list<TextCitation> citations`

    Citations supporting the text block.

    The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

  - `string text`

  - `"text" type`

### Text Block Param

- `TextBlockParam`

  - `string text`

  - `"text" type`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?list<TextCitationParam> citations`

### Text Citation

- `TextCitation`

  - `CitationCharLocation`

    - `string citedText`

    - `int documentIndex`

    - `?string documentTitle`

    - `int endCharIndex`

    - `?string fileID`

    - `int startCharIndex`

    - `"char_location" type`

  - `CitationPageLocation`

    - `string citedText`

    - `int documentIndex`

    - `?string documentTitle`

    - `int endPageNumber`

    - `?string fileID`

    - `int startPageNumber`

    - `"page_location" type`

  - `CitationContentBlockLocation`

    - `string citedText`

      The full text of the cited block range, concatenated.

      Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

    - `int documentIndex`

    - `?string documentTitle`

    - `int endBlockIndex`

      Exclusive 0-based end index of the cited block range in the source's `content` array.

      Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

    - `?string fileID`

    - `int startBlockIndex`

      0-based index of the first cited block in the source's `content` array.

    - `"content_block_location" type`

  - `CitationsWebSearchResultLocation`

    - `string citedText`

    - `string encryptedIndex`

    - `?string title`

    - `"web_search_result_location" type`

    - `string url`

  - `CitationsSearchResultLocation`

    - `string citedText`

      The full text of the cited block range, concatenated.

      Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

    - `int endBlockIndex`

      Exclusive 0-based end index of the cited block range in the source's `content` array.

      Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

    - `int searchResultIndex`

      0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

      Counted separately from `document_index`; server-side web search results are not included in this count.

    - `string source`

    - `int startBlockIndex`

      0-based index of the first cited block in the source's `content` array.

    - `?string title`

    - `"search_result_location" type`

### Text Citation Param

- `TextCitationParam`

  - `CitationCharLocationParam`

    - `string citedText`

    - `int documentIndex`

    - `?string documentTitle`

    - `int endCharIndex`

    - `int startCharIndex`

    - `"char_location" type`

  - `CitationPageLocationParam`

    - `string citedText`

    - `int documentIndex`

    - `?string documentTitle`

    - `int endPageNumber`

    - `int startPageNumber`

    - `"page_location" type`

  - `CitationContentBlockLocationParam`

    - `string citedText`

      The full text of the cited block range, concatenated.

      Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

    - `int documentIndex`

    - `?string documentTitle`

    - `int endBlockIndex`

      Exclusive 0-based end index of the cited block range in the source's `content` array.

      Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

    - `int startBlockIndex`

      0-based index of the first cited block in the source's `content` array.

    - `"content_block_location" type`

  - `CitationWebSearchResultLocationParam`

    - `string citedText`

    - `string encryptedIndex`

    - `?string title`

    - `"web_search_result_location" type`

    - `string url`

  - `CitationSearchResultLocationParam`

    - `string citedText`

      The full text of the cited block range, concatenated.

      Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

    - `int endBlockIndex`

      Exclusive 0-based end index of the cited block range in the source's `content` array.

      Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

    - `int searchResultIndex`

      0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

      Counted separately from `document_index`; server-side web search results are not included in this count.

    - `string source`

    - `int startBlockIndex`

      0-based index of the first cited block in the source's `content` array.

    - `?string title`

    - `"search_result_location" type`

### Text Delta

- `TextDelta`

  - `string text`

  - `"text_delta" type`

### Text Editor Code Execution Create Result Block

- `TextEditorCodeExecutionCreateResultBlock`

  - `bool isFileUpdate`

  - `"text_editor_code_execution_create_result" type`

### Text Editor Code Execution Create Result Block Param

- `TextEditorCodeExecutionCreateResultBlockParam`

  - `bool isFileUpdate`

  - `"text_editor_code_execution_create_result" type`

### Text Editor Code Execution Str Replace Result Block

- `TextEditorCodeExecutionStrReplaceResultBlock`

  - `?list<string> lines`

  - `?int newLines`

  - `?int newStart`

  - `?int oldLines`

  - `?int oldStart`

  - `"text_editor_code_execution_str_replace_result" type`

### Text Editor Code Execution Str Replace Result Block Param

- `TextEditorCodeExecutionStrReplaceResultBlockParam`

  - `"text_editor_code_execution_str_replace_result" type`

  - `?list<string> lines`

  - `?int newLines`

  - `?int newStart`

  - `?int oldLines`

  - `?int oldStart`

### Text Editor Code Execution Tool Result Block

- `TextEditorCodeExecutionToolResultBlock`

  - `Content content`

  - `string toolUseID`

  - `"text_editor_code_execution_tool_result" type`

### Text Editor Code Execution Tool Result Block Param

- `TextEditorCodeExecutionToolResultBlockParam`

  - `Content content`

  - `string toolUseID`

  - `"text_editor_code_execution_tool_result" type`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Text Editor Code Execution Tool Result Error

- `TextEditorCodeExecutionToolResultError`

  - `TextEditorCodeExecutionToolResultErrorCode errorCode`

  - `?string errorMessage`

  - `"text_editor_code_execution_tool_result_error" type`

### Text Editor Code Execution Tool Result Error Code

- `TextEditorCodeExecutionToolResultErrorCode`

  - `"invalid_tool_input"`

  - `"unavailable"`

  - `"too_many_requests"`

  - `"execution_time_exceeded"`

  - `"file_not_found"`

### Text Editor Code Execution Tool Result Error Param

- `TextEditorCodeExecutionToolResultErrorParam`

  - `TextEditorCodeExecutionToolResultErrorCode errorCode`

  - `"text_editor_code_execution_tool_result_error" type`

  - `?string errorMessage`

### Text Editor Code Execution View Result Block

- `TextEditorCodeExecutionViewResultBlock`

  - `string content`

  - `FileType fileType`

  - `?int numLines`

  - `?int startLine`

  - `?int totalLines`

  - `"text_editor_code_execution_view_result" type`

### Text Editor Code Execution View Result Block Param

- `TextEditorCodeExecutionViewResultBlockParam`

  - `string content`

  - `FileType fileType`

  - `"text_editor_code_execution_view_result" type`

  - `?int numLines`

  - `?int startLine`

  - `?int totalLines`

### Thinking Block

- `ThinkingBlock`

  - `string signature`

  - `string thinking`

  - `"thinking" type`

### Thinking Block Param

- `ThinkingBlockParam`

  - `string signature`

  - `string thinking`

  - `"thinking" type`

### Thinking Config Adaptive

- `ThinkingConfigAdaptive`

  - `"adaptive" type`

  - `?Display display`

    Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

### Thinking Config Disabled

- `ThinkingConfigDisabled`

  - `"disabled" type`

### Thinking Config Enabled

- `ThinkingConfigEnabled`

  - `int budgetTokens`

    Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

    Must be ≥1024 and less than `max_tokens`.

    See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

  - `"enabled" type`

  - `?Display display`

    Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

### Thinking Config Param

- `ThinkingConfigParam`

  - `ThinkingConfigEnabled`

    - `int budgetTokens`

      Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

      Must be ≥1024 and less than `max_tokens`.

      See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

    - `"enabled" type`

    - `?Display display`

      Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

  - `ThinkingConfigDisabled`

    - `"disabled" type`

  - `ThinkingConfigAdaptive`

    - `"adaptive" type`

    - `?Display display`

      Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

### Thinking Delta

- `ThinkingDelta`

  - `string thinking`

  - `"thinking_delta" type`

### Tool

- `Tool`

  - `InputSchema inputSchema`

    [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

    This defines the shape of the `input` that your tool accepts and that the model will produce.

  - `string name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?string description`

    Description of what this tool does.

    Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

  - `?bool eagerInputStreaming`

    Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

  - `?Type type`

### Tool Bash 20250124

- `ToolBash20250124`

  - `"bash" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"bash_20250124" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Tool Choice

- `ToolChoice`

  - `ToolChoiceAuto`

    - `"auto" type`

    - `?bool disableParallelToolUse`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output at most one tool use.

  - `ToolChoiceAny`

    - `"any" type`

    - `?bool disableParallelToolUse`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output exactly one tool use.

  - `ToolChoiceTool`

    - `string name`

      The name of the tool to use.

    - `"tool" type`

    - `?bool disableParallelToolUse`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output exactly one tool use.

  - `ToolChoiceNone`

    - `"none" type`

### Tool Choice Any

- `ToolChoiceAny`

  - `"any" type`

  - `?bool disableParallelToolUse`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output exactly one tool use.

### Tool Choice Auto

- `ToolChoiceAuto`

  - `"auto" type`

  - `?bool disableParallelToolUse`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output at most one tool use.

### Tool Choice None

- `ToolChoiceNone`

  - `"none" type`

### Tool Choice Tool

- `ToolChoiceTool`

  - `string name`

    The name of the tool to use.

  - `"tool" type`

  - `?bool disableParallelToolUse`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output exactly one tool use.

### Tool Reference Block

- `ToolReferenceBlock`

  - `string toolName`

  - `"tool_reference" type`

### Tool Reference Block Param

- `ToolReferenceBlockParam`

  - `string toolName`

  - `"tool_reference" type`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Tool Result Block Param

- `ToolResultBlockParam`

  - `string toolUseID`

  - `"tool_result" type`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?Content content`

  - `?bool isError`

### Tool Search Tool Bm25 20251119

- `ToolSearchToolBm25_20251119`

  - `"tool_search_tool_bm25" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `Type type`

  - `?list<AllowedCaller> allowedCallers`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Tool Search Tool Regex 20251119

- `ToolSearchToolRegex20251119`

  - `"tool_search_tool_regex" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `Type type`

  - `?list<AllowedCaller> allowedCallers`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Tool Search Tool Result Block

- `ToolSearchToolResultBlock`

  - `Content content`

  - `string toolUseID`

  - `"tool_search_tool_result" type`

### Tool Search Tool Result Block Param

- `ToolSearchToolResultBlockParam`

  - `Content content`

  - `string toolUseID`

  - `"tool_search_tool_result" type`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Tool Search Tool Result Error

- `ToolSearchToolResultError`

  - `ToolSearchToolResultErrorCode errorCode`

  - `?string errorMessage`

  - `"tool_search_tool_result_error" type`

### Tool Search Tool Result Error Code

- `ToolSearchToolResultErrorCode`

  - `"invalid_tool_input"`

  - `"unavailable"`

  - `"too_many_requests"`

  - `"execution_time_exceeded"`

### Tool Search Tool Result Error Param

- `ToolSearchToolResultErrorParam`

  - `ToolSearchToolResultErrorCode errorCode`

  - `"tool_search_tool_result_error" type`

  - `?string errorMessage`

### Tool Search Tool Search Result Block

- `ToolSearchToolSearchResultBlock`

  - `list<ToolReferenceBlock> toolReferences`

  - `"tool_search_tool_search_result" type`

### Tool Search Tool Search Result Block Param

- `ToolSearchToolSearchResultBlockParam`

  - `list<ToolReferenceBlockParam> toolReferences`

  - `"tool_search_tool_search_result" type`

### Tool Text Editor 20250124

- `ToolTextEditor20250124`

  - `"str_replace_editor" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"text_editor_20250124" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Tool Text Editor 20250429

- `ToolTextEditor20250429`

  - `"str_replace_based_edit_tool" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"text_editor_20250429" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Tool Text Editor 20250728

- `ToolTextEditor20250728`

  - `"str_replace_based_edit_tool" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"text_editor_20250728" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?list<array<string,mixed>> inputExamples`

  - `?int maxCharacters`

    Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Tool Union

- `ToolUnion`

  - `Tool`

    - `InputSchema inputSchema`

      [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

      This defines the shape of the `input` that your tool accepts and that the model will produce.

    - `string name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?string description`

      Description of what this tool does.

      Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

    - `?bool eagerInputStreaming`

      Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?Type type`

  - `ToolBash20250124`

    - `"bash" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"bash_20250124" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `CodeExecutionTool20250522`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"code_execution_20250522" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `CodeExecutionTool20250825`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"code_execution_20250825" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `CodeExecutionTool20260120`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"code_execution_20260120" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `CodeExecutionTool20260521`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"code_execution_20260521" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `MemoryTool20250818`

    - `"memory" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"memory_20250818" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `ToolTextEditor20250124`

    - `"str_replace_editor" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"text_editor_20250124" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `ToolTextEditor20250429`

    - `"str_replace_based_edit_tool" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"text_editor_20250429" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `ToolTextEditor20250728`

    - `"str_replace_based_edit_tool" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"text_editor_20250728" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?int maxCharacters`

      Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `WebSearchTool20250305`

    - `"web_search" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"web_search_20250305" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `?list<string> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?UserLocation userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `WebFetchTool20250910`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"web_fetch_20250910" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      List of domains to allow fetching from

    - `?list<string> blockedDomains`

      List of domains to block fetching from

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?CitationsConfigParam citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `WebSearchTool20260209`

    - `"web_search" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"web_search_20260209" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `?list<string> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?UserLocation userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `WebFetchTool20260209`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"web_fetch_20260209" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      List of domains to allow fetching from

    - `?list<string> blockedDomains`

      List of domains to block fetching from

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?CitationsConfigParam citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `WebFetchTool20260309`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"web_fetch_20260309" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      List of domains to allow fetching from

    - `?list<string> blockedDomains`

      List of domains to block fetching from

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?CitationsConfigParam citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?bool useCache`

      Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

  - `WebSearchTool20260318`

    - `"web_search" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"web_search_20260318" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `?list<string> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?ResponseInclusion responseInclusion`

      How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?UserLocation userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `WebFetchTool20260318`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"web_fetch_20260318" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      List of domains to allow fetching from

    - `?list<string> blockedDomains`

      List of domains to block fetching from

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?CitationsConfigParam citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?ResponseInclusion responseInclusion`

      How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?bool useCache`

      Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

  - `ToolSearchToolBm25_20251119`

    - `"tool_search_tool_bm25" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `Type type`

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `ToolSearchToolRegex20251119`

    - `"tool_search_tool_regex" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `Type type`

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

### Tool Use Block

- `ToolUseBlock`

  - `string id`

  - `Caller caller`

    Tool invocation directly from the model.

  - `array<string,mixed> input`

  - `string name`

  - `"tool_use" type`

### Tool Use Block Param

- `ToolUseBlockParam`

  - `string id`

  - `array<string,mixed> input`

  - `string name`

  - `"tool_use" type`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?Caller caller`

    Tool invocation directly from the model.

### URL Image Source

- `URLImageSource`

  - `"url" type`

  - `string url`

### URL PDF Source

- `URLPDFSource`

  - `"url" type`

  - `string url`

### Usage

- `Usage`

  - `?CacheCreation cacheCreation`

    Breakdown of cached tokens by TTL

  - `?int cacheCreationInputTokens`

    The number of input tokens used to create the cache entry.

  - `?int cacheReadInputTokens`

    The number of input tokens read from the cache.

  - `?string inferenceGeo`

    The geographic region where inference was performed for this request.

  - `int inputTokens`

    The number of input tokens which were used.

  - `int outputTokens`

    The number of output tokens which were used.

  - `?OutputTokensDetails outputTokensDetails`

    Breakdown of output tokens by category.

    `output_tokens` remains the inclusive, authoritative total used for billing.
    This object provides a read-only decomposition for observability — for example,
    how many of the billed output tokens were spent on internal reasoning that may
    have been summarized before being returned to you.

  - `?ServerToolUsage serverToolUse`

    The number of server tool requests.

  - `?ServiceTier serviceTier`

    If the request used the priority, standard, or batch tier.

### User Location

- `UserLocation`

  - `"approximate" type`

  - `?string city`

    The city of the user.

  - `?string country`

    The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

  - `?string region`

    The region of the user.

  - `?string timezone`

    The [IANA timezone](https://nodatime.org/TimeZones) of the user.

### Web Fetch Block

- `WebFetchBlock`

  - `DocumentBlock content`

  - `?string retrievedAt`

    ISO 8601 timestamp when the content was retrieved

  - `"web_fetch_result" type`

  - `string url`

    Fetched content URL

### Web Fetch Block Param

- `WebFetchBlockParam`

  - `DocumentBlockParam content`

  - `"web_fetch_result" type`

  - `string url`

    Fetched content URL

  - `?string retrievedAt`

    ISO 8601 timestamp when the content was retrieved

### Web Fetch Tool 20250910

- `WebFetchTool20250910`

  - `"web_fetch" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"web_fetch_20250910" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?list<string> allowedDomains`

    List of domains to allow fetching from

  - `?list<string> blockedDomains`

    List of domains to block fetching from

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?CitationsConfigParam citations`

    Citations configuration for fetched documents. Citations are disabled by default.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int maxContentTokens`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

  - `?int maxUses`

    Maximum number of times the tool can be used in the API request.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Web Fetch Tool 20260209

- `WebFetchTool20260209`

  - `"web_fetch" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"web_fetch_20260209" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?list<string> allowedDomains`

    List of domains to allow fetching from

  - `?list<string> blockedDomains`

    List of domains to block fetching from

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?CitationsConfigParam citations`

    Citations configuration for fetched documents. Citations are disabled by default.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int maxContentTokens`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

  - `?int maxUses`

    Maximum number of times the tool can be used in the API request.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Web Fetch Tool 20260309

- `WebFetchTool20260309`

  - `"web_fetch" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"web_fetch_20260309" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?list<string> allowedDomains`

    List of domains to allow fetching from

  - `?list<string> blockedDomains`

    List of domains to block fetching from

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?CitationsConfigParam citations`

    Citations configuration for fetched documents. Citations are disabled by default.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int maxContentTokens`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

  - `?int maxUses`

    Maximum number of times the tool can be used in the API request.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

  - `?bool useCache`

    Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

### Web Fetch Tool 20260318

- `WebFetchTool20260318`

  - `"web_fetch" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"web_fetch_20260318" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?list<string> allowedDomains`

    List of domains to allow fetching from

  - `?list<string> blockedDomains`

    List of domains to block fetching from

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?CitationsConfigParam citations`

    Citations configuration for fetched documents. Citations are disabled by default.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int maxContentTokens`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

  - `?int maxUses`

    Maximum number of times the tool can be used in the API request.

  - `?ResponseInclusion responseInclusion`

    How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

  - `?bool useCache`

    Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

### Web Fetch Tool Result Block

- `WebFetchToolResultBlock`

  - `Caller caller`

    Tool invocation directly from the model.

  - `Content content`

  - `string toolUseID`

  - `"web_fetch_tool_result" type`

### Web Fetch Tool Result Block Param

- `WebFetchToolResultBlockParam`

  - `Content content`

  - `string toolUseID`

  - `"web_fetch_tool_result" type`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?Caller caller`

    Tool invocation directly from the model.

### Web Fetch Tool Result Error Block

- `WebFetchToolResultErrorBlock`

  - `WebFetchToolResultErrorCode errorCode`

  - `"web_fetch_tool_result_error" type`

### Web Fetch Tool Result Error Block Param

- `WebFetchToolResultErrorBlockParam`

  - `WebFetchToolResultErrorCode errorCode`

  - `"web_fetch_tool_result_error" type`

### Web Fetch Tool Result Error Code

- `WebFetchToolResultErrorCode`

  - `"invalid_tool_input"`

  - `"url_too_long"`

  - `"url_not_allowed"`

  - `"url_not_in_prior_context"`

  - `"url_not_accessible"`

  - `"unsupported_content_type"`

  - `"too_many_requests"`

  - `"max_uses_exceeded"`

  - `"unavailable"`

### Web Search Result Block

- `WebSearchResultBlock`

  - `string encryptedContent`

  - `?string pageAge`

  - `string title`

  - `"web_search_result" type`

  - `string url`

### Web Search Result Block Param

- `WebSearchResultBlockParam`

  - `string encryptedContent`

  - `string title`

  - `"web_search_result" type`

  - `string url`

  - `?string pageAge`

### Web Search Tool 20250305

- `WebSearchTool20250305`

  - `"web_search" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"web_search_20250305" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?list<string> allowedDomains`

    If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

  - `?list<string> blockedDomains`

    If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int maxUses`

    Maximum number of times the tool can be used in the API request.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

  - `?UserLocation userLocation`

    Parameters for the user's location. Used to provide more relevant search results.

### Web Search Tool 20260209

- `WebSearchTool20260209`

  - `"web_search" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"web_search_20260209" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?list<string> allowedDomains`

    If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

  - `?list<string> blockedDomains`

    If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int maxUses`

    Maximum number of times the tool can be used in the API request.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

  - `?UserLocation userLocation`

    Parameters for the user's location. Used to provide more relevant search results.

### Web Search Tool 20260318

- `WebSearchTool20260318`

  - `"web_search" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"web_search_20260318" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?list<string> allowedDomains`

    If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

  - `?list<string> blockedDomains`

    If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int maxUses`

    Maximum number of times the tool can be used in the API request.

  - `?ResponseInclusion responseInclusion`

    How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

  - `?UserLocation userLocation`

    Parameters for the user's location. Used to provide more relevant search results.

### Web Search Tool Request Error

- `WebSearchToolRequestError`

  - `WebSearchToolResultErrorCode errorCode`

  - `"web_search_tool_result_error" type`

### Web Search Tool Result Block

- `WebSearchToolResultBlock`

  - `Caller caller`

    Tool invocation directly from the model.

  - `WebSearchToolResultBlockContent content`

  - `string toolUseID`

  - `"web_search_tool_result" type`

### Web Search Tool Result Block Content

- `WebSearchToolResultBlockContent`

  - `WebSearchToolResultError`

    - `WebSearchToolResultErrorCode errorCode`

    - `"web_search_tool_result_error" type`

  - `list<WebSearchResultBlock>`

    - `string encryptedContent`

    - `?string pageAge`

    - `string title`

    - `"web_search_result" type`

    - `string url`

### Web Search Tool Result Block Param

- `WebSearchToolResultBlockParam`

  - `WebSearchToolResultBlockParamContent content`

  - `string toolUseID`

  - `"web_search_tool_result" type`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?Caller caller`

    Tool invocation directly from the model.

### Web Search Tool Result Block Param Content

- `WebSearchToolResultBlockParamContent`

  - `list<WebSearchResultBlockParam>`

    - `string encryptedContent`

    - `string title`

    - `"web_search_result" type`

    - `string url`

    - `?string pageAge`

  - `WebSearchToolRequestError`

    - `WebSearchToolResultErrorCode errorCode`

    - `"web_search_tool_result_error" type`

### Web Search Tool Result Error

- `WebSearchToolResultError`

  - `WebSearchToolResultErrorCode errorCode`

  - `"web_search_tool_result_error" type`

### Web Search Tool Result Error Code

- `WebSearchToolResultErrorCode`

  - `"invalid_tool_input"`

  - `"unavailable"`

  - `"max_uses_exceeded"`

  - `"too_many_requests"`

  - `"query_too_long"`

  - `"request_too_large"`

# Batches

## Create a Message Batch

`$client->messages->batches->create(list<Request> requests, ?string userProfileID): MessageBatch`

**post** `/v1/messages/batches`

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

### Parameters

- `requests: list<Request>`

  List of requests for prompt completion. Each is an individual request to create a Message.

- `userProfileID?:optional string`

  The user profile ID to attribute the requests in this batch to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header. Applies to every request in the batch; an individual request whose `user_profile_id` body field conflicts with this header is errored.

### Returns

- `MessageBatch`

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `?\Datetime archivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `?\Datetime cancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `?\Datetime endedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `\Datetime expiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `ProcessingStatus processingStatus`

    Processing status of the Message Batch.

  - `MessageBatchRequestCounts requestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

  - `?string resultsURL`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `"message_batch" type`

    Object type.

    For Message Batches, this is always `"message_batch"`.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$messageBatch = $client->messages->batches->create(
  requests: [
    [
      'customID' => 'my-custom-id-1',
      'params' => [
        'maxTokens' => 1024,
        'messages' => [['content' => 'Hello, world', 'role' => 'user']],
        'model' => 'claude-opus-4-6',
        'cacheControl' => ['type' => 'ephemeral', 'ttl' => '5m'],
        'container' => 'container',
        'inferenceGeo' => 'inference_geo',
        'metadata' => ['userID' => '13803d75-b4b5-4c3e-b2a2-6f21399b021b'],
        'outputConfig' => [
          'effort' => 'low',
          'format' => ['schema' => ['foo' => 'bar'], 'type' => 'json_schema'],
        ],
        'serviceTier' => 'auto',
        'stopSequences' => ['string'],
        'stream' => false,
        'system' => [
          [
            'text' => 'Today\'s date is 2024-06-01.',
            'type' => 'text',
            'cacheControl' => ['type' => 'ephemeral', 'ttl' => '5m'],
            'citations' => [
              [
                'citedText' => 'cited_text',
                'documentIndex' => 0,
                'documentTitle' => 'x',
                'endCharIndex' => 0,
                'startCharIndex' => 0,
                'type' => 'char_location',
              ],
            ],
          ],
        ],
        'temperature' => 1,
        'thinking' => ['type' => 'adaptive', 'display' => 'summarized'],
        'toolChoice' => ['type' => 'auto', 'disableParallelToolUse' => true],
        'tools' => [
          [
            'inputSchema' => [
              'type' => 'object',
              'properties' => ['location' => 'bar', 'unit' => 'bar'],
              'required' => ['location'],
            ],
            'name' => 'name',
            'allowedCallers' => ['direct'],
            'cacheControl' => ['type' => 'ephemeral', 'ttl' => '5m'],
            'deferLoading' => true,
            'description' => 'Get the current weather in a given location',
            'eagerInputStreaming' => true,
            'inputExamples' => [['foo' => 'bar']],
            'strict' => true,
            'type' => 'custom',
          ],
        ],
        'topK' => 5,
        'topP' => 0.7,
      ],
    ],
  ],
  userProfileID: 'anthropic-user-profile-id',
);

var_dump($messageBatch);
```

#### Response

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
}
```

## Retrieve a Message Batch

`$client->messages->batches->retrieve(string messageBatchID): MessageBatch`

**get** `/v1/messages/batches/{message_batch_id}`

This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

### Parameters

- `messageBatchID: string`

  ID of the Message Batch.

### Returns

- `MessageBatch`

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `?\Datetime archivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `?\Datetime cancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `?\Datetime endedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `\Datetime expiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `ProcessingStatus processingStatus`

    Processing status of the Message Batch.

  - `MessageBatchRequestCounts requestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

  - `?string resultsURL`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `"message_batch" type`

    Object type.

    For Message Batches, this is always `"message_batch"`.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$messageBatch = $client->messages->batches->retrieve('message_batch_id');

var_dump($messageBatch);
```

#### Response

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
}
```

## List Message Batches

`$client->messages->batches->list(?string afterID, ?string beforeID, ?int limit): Page<MessageBatch>`

**get** `/v1/messages/batches`

List all Message Batches within a Workspace. Most recently created batches are returned first.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

### Parameters

- `afterID?:optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `beforeID?:optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `limit?:optional int`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

### Returns

- `MessageBatch`

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `?\Datetime archivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `?\Datetime cancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `?\Datetime endedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `\Datetime expiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `ProcessingStatus processingStatus`

    Processing status of the Message Batch.

  - `MessageBatchRequestCounts requestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

  - `?string resultsURL`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `"message_batch" type`

    Object type.

    For Message Batches, this is always `"message_batch"`.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->messages->batches->list(
  afterID: 'after_id', beforeID: 'before_id', limit: 1
);

var_dump($page);
```

#### Response

```json
{
  "data": [
    {
      "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
      "archived_at": "2024-08-20T18:37:24.100435Z",
      "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
      "created_at": "2024-08-20T18:37:24.100435Z",
      "ended_at": "2024-08-20T18:37:24.100435Z",
      "expires_at": "2024-08-20T18:37:24.100435Z",
      "processing_status": "in_progress",
      "request_counts": {
        "canceled": 10,
        "errored": 30,
        "expired": 10,
        "processing": 100,
        "succeeded": 50
      },
      "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
      "type": "message_batch"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

## Cancel a Message Batch

`$client->messages->batches->cancel(string messageBatchID): MessageBatch`

**post** `/v1/messages/batches/{message_batch_id}/cancel`

Batches may be canceled any time before processing ends. Once cancellation is initiated, the batch enters a `canceling` state, at which time the system may complete any in-progress, non-interruptible requests before finalizing cancellation.

The number of canceled requests is specified in `request_counts`. To determine which requests were canceled, check the individual results within the batch. Note that cancellation may not result in any canceled requests if they were non-interruptible.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

### Parameters

- `messageBatchID: string`

  ID of the Message Batch.

### Returns

- `MessageBatch`

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `?\Datetime archivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `?\Datetime cancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `?\Datetime endedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `\Datetime expiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `ProcessingStatus processingStatus`

    Processing status of the Message Batch.

  - `MessageBatchRequestCounts requestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

  - `?string resultsURL`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `"message_batch" type`

    Object type.

    For Message Batches, this is always `"message_batch"`.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$messageBatch = $client->messages->batches->cancel('message_batch_id');

var_dump($messageBatch);
```

#### Response

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
}
```

## Delete a Message Batch

`$client->messages->batches->delete(string messageBatchID): DeletedMessageBatch`

**delete** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

### Parameters

- `messageBatchID: string`

  ID of the Message Batch.

### Returns

- `DeletedMessageBatch`

  - `string id`

    ID of the Message Batch.

  - `"message_batch_deleted" type`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$deletedMessageBatch = $client->messages->batches->delete('message_batch_id');

var_dump($deletedMessageBatch);
```

#### Response

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```

## Retrieve Message Batch results

`$client->messages->batches->results(string messageBatchID): MessageBatchIndividualResponse`

**get** `/v1/messages/batches/{message_batch_id}/results`

Streams the results of a Message Batch as a `.jsonl` file.

Each line in the file is a JSON object containing the result of a single request in the Message Batch. Results are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

### Parameters

- `messageBatchID: string`

  ID of the Message Batch.

### Returns

- `MessageBatchIndividualResponse`

  - `string customID`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `MessageBatchResult result`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$messageBatchIndividualResponse = $client->messages->batches->resultsStream(
  'message_batch_id'
);

var_dump($messageBatchIndividualResponse);
```

## Domain Types

### Deleted Message Batch

- `DeletedMessageBatch`

  - `string id`

    ID of the Message Batch.

  - `"message_batch_deleted" type`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

### Message Batch

- `MessageBatch`

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `?\Datetime archivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `?\Datetime cancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `?\Datetime endedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `\Datetime expiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `ProcessingStatus processingStatus`

    Processing status of the Message Batch.

  - `MessageBatchRequestCounts requestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

  - `?string resultsURL`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `"message_batch" type`

    Object type.

    For Message Batches, this is always `"message_batch"`.

### Message Batch Canceled Result

- `MessageBatchCanceledResult`

  - `"canceled" type`

### Message Batch Errored Result

- `MessageBatchErroredResult`

  - `ErrorResponse error`

  - `"errored" type`

### Message Batch Expired Result

- `MessageBatchExpiredResult`

  - `"expired" type`

### Message Batch Individual Response

- `MessageBatchIndividualResponse`

  - `string customID`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `MessageBatchResult result`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

### Message Batch Request Counts

- `MessageBatchRequestCounts`

  - `int canceled`

    Number of requests in the Message Batch that have been canceled.

    This is zero until processing of the entire Message Batch has ended.

  - `int errored`

    Number of requests in the Message Batch that encountered an error.

    This is zero until processing of the entire Message Batch has ended.

  - `int expired`

    Number of requests in the Message Batch that have expired.

    This is zero until processing of the entire Message Batch has ended.

  - `int processing`

    Number of requests in the Message Batch that are processing.

  - `int succeeded`

    Number of requests in the Message Batch that have completed successfully.

    This is zero until processing of the entire Message Batch has ended.

### Message Batch Result

- `MessageBatchResult`

  - `MessageBatchSucceededResult`

    - `Message message`

    - `"succeeded" type`

  - `MessageBatchErroredResult`

    - `ErrorResponse error`

    - `"errored" type`

  - `MessageBatchCanceledResult`

    - `"canceled" type`

  - `MessageBatchExpiredResult`

    - `"expired" type`

### Message Batch Succeeded Result

- `MessageBatchSucceededResult`

  - `Message message`

  - `"succeeded" type`
