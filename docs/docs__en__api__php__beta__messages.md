# Messages

## Create a Message

`$client->beta->messages->create(int maxTokens, list<BetaMessageParam> messages, Model model, ?BetaCacheControlEphemeral cacheControl, ?Container container, ?BetaContextManagementConfig contextManagement, ?BetaDiagnosticsParam diagnostics, ?string inferenceGeo, ?list<BetaRequestMCPServerURLDefinition> mcpServers, ?BetaMetadata metadata, ?BetaOutputConfig outputConfig, ?BetaJSONOutputFormat outputFormat, ?ServiceTier serviceTier, ?Speed speed, ?list<string> stopSequences, ?System system, ?float temperature, ?BetaThinkingConfigParam thinking, ?BetaToolChoice toolChoice, ?list<BetaToolUnion> tools, ?int topK, ?float topP, ?string userProfileID, ?list<AnthropicBeta> betas): BetaMessage`

**post** `/v1/messages`

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://docs.claude.com/en/docs/initial-setup)

### Parameters

- `maxTokens: int`

  The maximum number of tokens to generate before stopping.

  Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

  Set to `0` to populate the [prompt cache](https://docs.claude.com/en/docs/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.

  Different models have different maximum values for this parameter.  See [models](https://docs.claude.com/en/docs/models-overview) for details.

- `messages: list<BetaMessageParam>`

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

  See [input examples](https://docs.claude.com/en/api/messages-examples).

  Note that if you want to include a [system prompt](https://docs.claude.com/en/docs/system-prompts), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.

  There is a limit of 100,000 messages in a single request.

- `model: Model`

  The model that will complete your prompt.

  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `cacheControl?:optional BetaCacheControlEphemeral`

  Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

- `container?:optional Container`

  Container identifier for reuse across requests.

- `contextManagement?:optional BetaContextManagementConfig`

  Context management configuration.

  This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

- `diagnostics?:optional BetaDiagnosticsParam`

  Request-level diagnostics. Currently carries the previous response
  id for prompt-cache divergence reporting.

- `inferenceGeo?:optional string`

  Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

- `mcpServers?:optional list<BetaRequestMCPServerURLDefinition>`

  MCP servers to be utilized in this request

- `metadata?:optional BetaMetadata`

  An object describing metadata about the request.

- `outputConfig?:optional BetaOutputConfig`

  Configuration options for the model's output, such as the output format.

- `outputFormat?:optional BetaJSONOutputFormat`

  Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

  A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

- `serviceTier?:optional ServiceTier`

  Determines whether to use priority capacity (if available) or standard capacity for this request.

  Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.

- `speed?:optional Speed`

  The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference.

- `stopSequences?:optional list<string>`

  Custom text sequences that will cause the model to stop generating.

  Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

  If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

- `stream?:optional bool`

  Whether to incrementally stream the response using server-sent events.

  See [streaming](https://docs.claude.com/en/api/messages-streaming) for details.

- `system?:optional System`

  System prompt.

  A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

- `temperature?:optional float`

  Amount of randomness injected into the response.

  Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

  Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

- `thinking?:optional BetaThinkingConfigParam`

  Configuration for enabling Claude's extended thinking.

  When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

  See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

- `toolChoice?:optional BetaToolChoice`

  How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

- `tools?:optional list<BetaToolUnion>`

  Definitions of tools that the model may use.

  If you include `tools` in your API request, the model may return `tool_use` content blocks that represent the model's use of those tools. You can then run those tools using the tool input generated by the model and then optionally return results back to the model using `tool_result` content blocks.

  There are two types of tools: **client tools** and **server tools**. The behavior described below applies to client tools. For [server tools](https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview#server-tools), see their individual documentation as each has its own behavior (e.g., the [web search tool](https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-search-tool)).

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

  See our [guide](https://docs.claude.com/en/docs/tool-use) for more details.

- `topK?:optional int`

  Only sample from the top K options for each subsequent token.

  Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

  Recommended for advanced use cases only.

- `topP?:optional float`

  Use nucleus sampling.

  In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

  Recommended for advanced use cases only.

- `userProfileID?:optional string`

  The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaMessage`

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `?BetaContainer container`

    Information about the container used in the request (for the code execution tool)

  - `list<BetaContentBlock> content`

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

  - `?BetaContextManagementResponse contextManagement`

    Context management response.

    Information about context management strategies applied during the request.

  - `?BetaDiagnostics diagnostics`

    Response envelope for request-level diagnostics. Present (possibly
    null) whenever the caller supplied `diagnostics` on the request.

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `"assistant" role`

    Conversational role of the generated message.

    This will always be `"assistant"`.

  - `?BetaRefusalStopDetails stopDetails`

    Structured information about a refusal.

  - `?BetaStopReason stopReason`

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

  - `BetaUsage usage`

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

$betaMessage = $client->beta->messages->create(
  maxTokens: 1024,
  messages: [['content' => 'Hello, world', 'role' => 'user']],
  model: 'claude-opus-4-6',
  cacheControl: ['type' => 'ephemeral', 'ttl' => '5m'],
  container: [
    'id' => 'id',
    'skills' => [
      ['skillID' => 'pdf', 'type' => 'anthropic', 'version' => 'latest']
    ],
  ],
  contextManagement: [
    'edits' => [
      [
        'type' => 'clear_tool_uses_20250919',
        'clearAtLeast' => ['type' => 'input_tokens', 'value' => 0],
        'clearToolInputs' => true,
        'excludeTools' => ['string'],
        'keep' => ['type' => 'tool_uses', 'value' => 0],
        'trigger' => ['type' => 'input_tokens', 'value' => 1],
      ],
    ],
  ],
  diagnostics: ['previousMessageID' => 'previous_message_id'],
  inferenceGeo: 'inference_geo',
  mcpServers: [
    [
      'name' => 'name',
      'type' => 'url',
      'url' => 'url',
      'authorizationToken' => 'authorization_token',
      'toolConfiguration' => ['allowedTools' => ['string'], 'enabled' => true],
    ],
  ],
  metadata: ['userID' => '13803d75-b4b5-4c3e-b2a2-6f21399b021b'],
  outputConfig: [
    'effort' => 'low',
    'format' => ['schema' => ['foo' => 'bar'], 'type' => 'json_schema'],
    'taskBudget' => ['total' => 1024, 'type' => 'tokens', 'remaining' => 0],
  ],
  outputFormat: ['schema' => ['foo' => 'bar'], 'type' => 'json_schema'],
  serviceTier: 'auto',
  speed: 'standard',
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
  userProfileID: 'user_profile_id',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaMessage);
```

#### Response

```json
{
  "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
  "container": {
    "id": "id",
    "expires_at": "2019-12-27T18:11:19.117Z",
    "skills": [
      {
        "skill_id": "pdf",
        "type": "anthropic",
        "version": "latest"
      }
    ]
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
  "context_management": {
    "applied_edits": [
      {
        "cleared_input_tokens": 0,
        "cleared_tool_uses": 0,
        "type": "clear_tool_uses_20250919"
      }
    ]
  },
  "diagnostics": {
    "cache_miss_reason": {
      "cache_missed_input_tokens": 0,
      "type": "model_changed"
    }
  },
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
    "iterations": [
      {
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 0
        },
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "output_tokens": 0,
        "type": "message"
      }
    ],
    "output_tokens": 503,
    "output_tokens_details": {
      "thinking_tokens": 0
    },
    "server_tool_use": {
      "web_fetch_requests": 2,
      "web_search_requests": 0
    },
    "service_tier": "standard",
    "speed": "standard"
  }
}
```

## Count tokens in a Message

`$client->beta->messages->countTokens(list<BetaMessageParam> messages, Model model, ?BetaCacheControlEphemeral cacheControl, ?BetaContextManagementConfig contextManagement, ?list<BetaRequestMCPServerURLDefinition> mcpServers, ?BetaOutputConfig outputConfig, ?BetaJSONOutputFormat outputFormat, ?Speed speed, ?System system, ?BetaThinkingConfigParam thinking, ?BetaToolChoice toolChoice, ?list<Tool> tools, ?list<AnthropicBeta> betas): BetaMessageTokensCount`

**post** `/v1/messages/count_tokens`

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://docs.claude.com/en/docs/build-with-claude/token-counting)

### Parameters

- `messages: list<BetaMessageParam>`

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

  See [input examples](https://docs.claude.com/en/api/messages-examples).

  Note that if you want to include a [system prompt](https://docs.claude.com/en/docs/system-prompts), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.

  There is a limit of 100,000 messages in a single request.

- `model: Model`

  The model that will complete your prompt.

  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `cacheControl?:optional BetaCacheControlEphemeral`

  Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

- `contextManagement?:optional BetaContextManagementConfig`

  Context management configuration.

  This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

- `mcpServers?:optional list<BetaRequestMCPServerURLDefinition>`

  MCP servers to be utilized in this request

- `outputConfig?:optional BetaOutputConfig`

  Configuration options for the model's output, such as the output format.

- `outputFormat?:optional BetaJSONOutputFormat`

  Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

  A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

- `speed?:optional Speed`

  The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference.

- `system?:optional System`

  System prompt.

  A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

- `thinking?:optional BetaThinkingConfigParam`

  Configuration for enabling Claude's extended thinking.

  When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

  See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

- `toolChoice?:optional BetaToolChoice`

  How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

- `tools?:optional list<Tool>`

  Definitions of tools that the model may use.

  If you include `tools` in your API request, the model may return `tool_use` content blocks that represent the model's use of those tools. You can then run those tools using the tool input generated by the model and then optionally return results back to the model using `tool_result` content blocks.

  There are two types of tools: **client tools** and **server tools**. The behavior described below applies to client tools. For [server tools](https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview#server-tools), see their individual documentation as each has its own behavior (e.g., the [web search tool](https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-search-tool)).

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

  See our [guide](https://docs.claude.com/en/docs/tool-use) for more details.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaMessageTokensCount`

  - `?BetaCountTokensContextManagementResponse contextManagement`

    Information about context management applied to the message.

  - `int inputTokens`

    The total number of tokens across the provided list of messages, system prompt, and tools.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaMessageTokensCount = $client->beta->messages->countTokens(
  messages: [['content' => 'Hello, world', 'role' => 'user']],
  model: 'claude-opus-4-6',
  cacheControl: ['type' => 'ephemeral', 'ttl' => '5m'],
  contextManagement: [
    'edits' => [
      [
        'type' => 'clear_tool_uses_20250919',
        'clearAtLeast' => ['type' => 'input_tokens', 'value' => 0],
        'clearToolInputs' => true,
        'excludeTools' => ['string'],
        'keep' => ['type' => 'tool_uses', 'value' => 0],
        'trigger' => ['type' => 'input_tokens', 'value' => 1],
      ],
    ],
  ],
  mcpServers: [
    [
      'name' => 'name',
      'type' => 'url',
      'url' => 'url',
      'authorizationToken' => 'authorization_token',
      'toolConfiguration' => ['allowedTools' => ['string'], 'enabled' => true],
    ],
  ],
  outputConfig: [
    'effort' => 'low',
    'format' => ['schema' => ['foo' => 'bar'], 'type' => 'json_schema'],
    'taskBudget' => ['total' => 1024, 'type' => 'tokens', 'remaining' => 0],
  ],
  outputFormat: ['schema' => ['foo' => 'bar'], 'type' => 'json_schema'],
  speed: 'standard',
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
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaMessageTokensCount);
```

#### Response

```json
{
  "context_management": {
    "original_input_tokens": 0
  },
  "input_tokens": 2095
}
```

## Domain Types

### Beta Advisor Message Iteration Usage

- `BetaAdvisorMessageIterationUsage`

  - `?BetaCacheCreation cacheCreation`

    Breakdown of cached tokens by TTL

  - `int cacheCreationInputTokens`

    The number of input tokens used to create the cache entry.

  - `int cacheReadInputTokens`

    The number of input tokens read from the cache.

  - `int inputTokens`

    The number of input tokens which were used.

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `int outputTokens`

    The number of output tokens which were used.

  - `"advisor_message" type`

    Usage for an advisor sub-inference iteration

### Beta Advisor Redacted Result Block

- `BetaAdvisorRedactedResultBlock`

  - `string encryptedContent`

    Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

  - `?string stopReason`

    The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

  - `"advisor_redacted_result" type`

### Beta Advisor Redacted Result Block Param

- `BetaAdvisorRedactedResultBlockParam`

  - `string encryptedContent`

    Opaque blob produced by a prior response; must be round-tripped verbatim.

  - `"advisor_redacted_result" type`

  - `?string stopReason`

### Beta Advisor Result Block

- `BetaAdvisorResultBlock`

  - `?string stopReason`

    The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

  - `string text`

  - `"advisor_result" type`

### Beta Advisor Result Block Param

- `BetaAdvisorResultBlockParam`

  - `string text`

  - `"advisor_result" type`

  - `?string stopReason`

### Beta Advisor Tool 20260301

- `BetaAdvisorTool20260301`

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `"advisor" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"advisor_20260301" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?BetaCacheControlEphemeral caching`

    Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int maxUses`

    Maximum number of times the tool can be used in the API request.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Advisor Tool Result Block

- `BetaAdvisorToolResultBlock`

  - `Content content`

  - `string toolUseID`

  - `"advisor_tool_result" type`

### Beta Advisor Tool Result Block Param

- `BetaAdvisorToolResultBlockParam`

  - `Content content`

  - `string toolUseID`

  - `"advisor_tool_result" type`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Beta Advisor Tool Result Error

- `BetaAdvisorToolResultError`

  - `ErrorCode errorCode`

  - `"advisor_tool_result_error" type`

### Beta Advisor Tool Result Error Param

- `BetaAdvisorToolResultErrorParam`

  - `ErrorCode errorCode`

  - `"advisor_tool_result_error" type`

### Beta All Thinking Turns

- `BetaAllThinkingTurns`

  - `"all" type`

### Beta Base64 Image Source

- `BetaBase64ImageSource`

  - `string data`

  - `MediaType mediaType`

  - `"base64" type`

### Beta Base64 PDF Source

- `BetaBase64PDFSource`

  - `string data`

  - `"application/pdf" mediaType`

  - `"base64" type`

### Beta Bash Code Execution Output Block

- `BetaBashCodeExecutionOutputBlock`

  - `string fileID`

  - `"bash_code_execution_output" type`

### Beta Bash Code Execution Output Block Param

- `BetaBashCodeExecutionOutputBlockParam`

  - `string fileID`

  - `"bash_code_execution_output" type`

### Beta Bash Code Execution Result Block

- `BetaBashCodeExecutionResultBlock`

  - `list<BetaBashCodeExecutionOutputBlock> content`

  - `int returnCode`

  - `string stderr`

  - `string stdout`

  - `"bash_code_execution_result" type`

### Beta Bash Code Execution Result Block Param

- `BetaBashCodeExecutionResultBlockParam`

  - `list<BetaBashCodeExecutionOutputBlockParam> content`

  - `int returnCode`

  - `string stderr`

  - `string stdout`

  - `"bash_code_execution_result" type`

### Beta Bash Code Execution Tool Result Block

- `BetaBashCodeExecutionToolResultBlock`

  - `Content content`

  - `string toolUseID`

  - `"bash_code_execution_tool_result" type`

### Beta Bash Code Execution Tool Result Block Param

- `BetaBashCodeExecutionToolResultBlockParam`

  - `Content content`

  - `string toolUseID`

  - `"bash_code_execution_tool_result" type`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Beta Bash Code Execution Tool Result Error

- `BetaBashCodeExecutionToolResultError`

  - `ErrorCode errorCode`

  - `"bash_code_execution_tool_result_error" type`

### Beta Bash Code Execution Tool Result Error Param

- `BetaBashCodeExecutionToolResultErrorParam`

  - `ErrorCode errorCode`

  - `"bash_code_execution_tool_result_error" type`

### Beta Cache Control Ephemeral

- `BetaCacheControlEphemeral`

  - `"ephemeral" type`

  - `?TTL ttl`

    The time-to-live for the cache control breakpoint.

    This may be one the following values:

    - `5m`: 5 minutes
    - `1h`: 1 hour

    Defaults to `5m`.

### Beta Cache Creation

- `BetaCacheCreation`

  - `int ephemeral1hInputTokens`

    The number of input tokens used to create the 1 hour cache entry.

  - `int ephemeral5mInputTokens`

    The number of input tokens used to create the 5 minute cache entry.

### Beta Cache Miss Messages Changed

- `BetaCacheMissMessagesChanged`

  - `int cacheMissedInputTokens`

    Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

  - `"messages_changed" type`

### Beta Cache Miss Model Changed

- `BetaCacheMissModelChanged`

  - `int cacheMissedInputTokens`

    Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

  - `"model_changed" type`

### Beta Cache Miss Previous Message Not Found

- `BetaCacheMissPreviousMessageNotFound`

  - `"previous_message_not_found" type`

### Beta Cache Miss System Changed

- `BetaCacheMissSystemChanged`

  - `int cacheMissedInputTokens`

    Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

  - `"system_changed" type`

### Beta Cache Miss Tools Changed

- `BetaCacheMissToolsChanged`

  - `int cacheMissedInputTokens`

    Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

  - `"tools_changed" type`

### Beta Cache Miss Unavailable

- `BetaCacheMissUnavailable`

  - `"unavailable" type`

### Beta Citation Char Location

- `BetaCitationCharLocation`

  - `string citedText`

  - `int documentIndex`

  - `?string documentTitle`

  - `int endCharIndex`

  - `?string fileID`

  - `int startCharIndex`

  - `"char_location" type`

### Beta Citation Char Location Param

- `BetaCitationCharLocationParam`

  - `string citedText`

  - `int documentIndex`

  - `?string documentTitle`

  - `int endCharIndex`

  - `int startCharIndex`

  - `"char_location" type`

### Beta Citation Config

- `BetaCitationConfig`

  - `bool enabled`

### Beta Citation Content Block Location

- `BetaCitationContentBlockLocation`

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

### Beta Citation Content Block Location Param

- `BetaCitationContentBlockLocationParam`

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

### Beta Citation Page Location

- `BetaCitationPageLocation`

  - `string citedText`

  - `int documentIndex`

  - `?string documentTitle`

  - `int endPageNumber`

  - `?string fileID`

  - `int startPageNumber`

  - `"page_location" type`

### Beta Citation Page Location Param

- `BetaCitationPageLocationParam`

  - `string citedText`

  - `int documentIndex`

  - `?string documentTitle`

  - `int endPageNumber`

  - `int startPageNumber`

  - `"page_location" type`

### Beta Citation Search Result Location

- `BetaCitationSearchResultLocation`

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

### Beta Citation Search Result Location Param

- `BetaCitationSearchResultLocationParam`

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

### Beta Citation Web Search Result Location Param

- `BetaCitationWebSearchResultLocationParam`

  - `string citedText`

  - `string encryptedIndex`

  - `?string title`

  - `"web_search_result_location" type`

  - `string url`

### Beta Citations Config Param

- `BetaCitationsConfigParam`

  - `?bool enabled`

### Beta Citations Delta

- `BetaCitationsDelta`

  - `Citation citation`

  - `"citations_delta" type`

### Beta Citations Web Search Result Location

- `BetaCitationsWebSearchResultLocation`

  - `string citedText`

  - `string encryptedIndex`

  - `?string title`

  - `"web_search_result_location" type`

  - `string url`

### Beta Clear Thinking 20251015 Edit

- `BetaClearThinking20251015Edit`

  - `"clear_thinking_20251015" type`

  - `?Keep keep`

    Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

### Beta Clear Thinking 20251015 Edit Response

- `BetaClearThinking20251015EditResponse`

  - `int clearedInputTokens`

    Number of input tokens cleared by this edit.

  - `int clearedThinkingTurns`

    Number of thinking turns that were cleared.

  - `"clear_thinking_20251015" type`

    The type of context management edit applied.

### Beta Clear Tool Uses 20250919 Edit

- `BetaClearToolUses20250919Edit`

  - `"clear_tool_uses_20250919" type`

  - `?BetaInputTokensClearAtLeast clearAtLeast`

    Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

  - `?ClearToolInputs clearToolInputs`

    Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

  - `?list<string> excludeTools`

    Tool names whose uses are preserved from clearing

  - `?BetaToolUsesKeep keep`

    Number of tool uses to retain in the conversation

  - `?Trigger trigger`

    Condition that triggers the context management strategy

### Beta Clear Tool Uses 20250919 Edit Response

- `BetaClearToolUses20250919EditResponse`

  - `int clearedInputTokens`

    Number of input tokens cleared by this edit.

  - `int clearedToolUses`

    Number of tool uses that were cleared.

  - `"clear_tool_uses_20250919" type`

    The type of context management edit applied.

### Beta Code Execution Output Block

- `BetaCodeExecutionOutputBlock`

  - `string fileID`

  - `"code_execution_output" type`

### Beta Code Execution Output Block Param

- `BetaCodeExecutionOutputBlockParam`

  - `string fileID`

  - `"code_execution_output" type`

### Beta Code Execution Result Block

- `BetaCodeExecutionResultBlock`

  - `list<BetaCodeExecutionOutputBlock> content`

  - `int returnCode`

  - `string stderr`

  - `string stdout`

  - `"code_execution_result" type`

### Beta Code Execution Result Block Param

- `BetaCodeExecutionResultBlockParam`

  - `list<BetaCodeExecutionOutputBlockParam> content`

  - `int returnCode`

  - `string stderr`

  - `string stdout`

  - `"code_execution_result" type`

### Beta Code Execution Tool 20250522

- `BetaCodeExecutionTool20250522`

  - `"code_execution" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"code_execution_20250522" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Code Execution Tool 20250825

- `BetaCodeExecutionTool20250825`

  - `"code_execution" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"code_execution_20250825" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Code Execution Tool 20260120

- `BetaCodeExecutionTool20260120`

  - `"code_execution" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"code_execution_20260120" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Code Execution Tool Result Block

- `BetaCodeExecutionToolResultBlock`

  - `BetaCodeExecutionToolResultBlockContent content`

    Code execution result with encrypted stdout for PFC + web_search results.

  - `string toolUseID`

  - `"code_execution_tool_result" type`

### Beta Code Execution Tool Result Block Content

- `BetaCodeExecutionToolResultBlockContent`

  - `BetaCodeExecutionToolResultError`

    - `BetaCodeExecutionToolResultErrorCode errorCode`

    - `"code_execution_tool_result_error" type`

  - `BetaCodeExecutionResultBlock`

    - `list<BetaCodeExecutionOutputBlock> content`

    - `int returnCode`

    - `string stderr`

    - `string stdout`

    - `"code_execution_result" type`

  - `BetaEncryptedCodeExecutionResultBlock`

    - `list<BetaCodeExecutionOutputBlock> content`

    - `string encryptedStdout`

    - `int returnCode`

    - `string stderr`

    - `"encrypted_code_execution_result" type`

### Beta Code Execution Tool Result Block Param

- `BetaCodeExecutionToolResultBlockParam`

  - `BetaCodeExecutionToolResultBlockParamContent content`

    Code execution result with encrypted stdout for PFC + web_search results.

  - `string toolUseID`

  - `"code_execution_tool_result" type`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Beta Code Execution Tool Result Block Param Content

- `BetaCodeExecutionToolResultBlockParamContent`

  - `BetaCodeExecutionToolResultErrorParam`

    - `BetaCodeExecutionToolResultErrorCode errorCode`

    - `"code_execution_tool_result_error" type`

  - `BetaCodeExecutionResultBlockParam`

    - `list<BetaCodeExecutionOutputBlockParam> content`

    - `int returnCode`

    - `string stderr`

    - `string stdout`

    - `"code_execution_result" type`

  - `BetaEncryptedCodeExecutionResultBlockParam`

    - `list<BetaCodeExecutionOutputBlockParam> content`

    - `string encryptedStdout`

    - `int returnCode`

    - `string stderr`

    - `"encrypted_code_execution_result" type`

### Beta Code Execution Tool Result Error

- `BetaCodeExecutionToolResultError`

  - `BetaCodeExecutionToolResultErrorCode errorCode`

  - `"code_execution_tool_result_error" type`

### Beta Code Execution Tool Result Error Code

- `BetaCodeExecutionToolResultErrorCode`

  - `"invalid_tool_input"`

  - `"unavailable"`

  - `"too_many_requests"`

  - `"execution_time_exceeded"`

### Beta Code Execution Tool Result Error Param

- `BetaCodeExecutionToolResultErrorParam`

  - `BetaCodeExecutionToolResultErrorCode errorCode`

  - `"code_execution_tool_result_error" type`

### Beta Compact 20260112 Edit

- `BetaCompact20260112Edit`

  - `"compact_20260112" type`

  - `?string instructions`

    Additional instructions for summarization.

  - `?bool pauseAfterCompaction`

    Whether to pause after compaction and return the compaction block to the user.

  - `?BetaInputTokensTrigger trigger`

    When to trigger compaction. Defaults to 150000 input tokens.

### Beta Compaction Block

- `BetaCompactionBlock`

  - `?string content`

    Summary of compacted content, or null if compaction failed

  - `?string encryptedContent`

    Opaque metadata from prior compaction, to be round-tripped verbatim

  - `"compaction" type`

### Beta Compaction Block Param

- `BetaCompactionBlockParam`

  - `"compaction" type`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?string content`

    Summary of previously compacted content, or null if compaction failed

  - `?string encryptedContent`

    Opaque metadata from prior compaction, to be round-tripped verbatim

### Beta Compaction Content Block Delta

- `BetaCompactionContentBlockDelta`

  - `?string content`

  - `?string encryptedContent`

    Opaque metadata from prior compaction, to be round-tripped verbatim

  - `"compaction_delta" type`

### Beta Compaction Iteration Usage

- `BetaCompactionIterationUsage`

  - `?BetaCacheCreation cacheCreation`

    Breakdown of cached tokens by TTL

  - `int cacheCreationInputTokens`

    The number of input tokens used to create the cache entry.

  - `int cacheReadInputTokens`

    The number of input tokens read from the cache.

  - `int inputTokens`

    The number of input tokens which were used.

  - `int outputTokens`

    The number of output tokens which were used.

  - `"compaction" type`

    Usage for a compaction iteration

### Beta Container

- `BetaContainer`

  - `string id`

    Identifier for the container used in this request

  - `\Datetime expiresAt`

    The time at which the container will expire.

  - `?list<BetaSkill> skills`

    Skills loaded in the container

### Beta Container Params

- `BetaContainerParams`

  - `?string id`

    Container id

  - `?list<BetaSkillParams> skills`

    List of skills to load in the container

### Beta Container Upload Block

- `BetaContainerUploadBlock`

  - `string fileID`

  - `"container_upload" type`

### Beta Container Upload Block Param

- `BetaContainerUploadBlockParam`

  - `string fileID`

  - `"container_upload" type`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Beta Content Block

- `BetaContentBlock`

  - `BetaTextBlock`

    - `?list<BetaTextCitation> citations`

      Citations supporting the text block.

      The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

    - `string text`

    - `"text" type`

  - `BetaThinkingBlock`

    - `string signature`

    - `string thinking`

    - `"thinking" type`

  - `BetaRedactedThinkingBlock`

    - `string data`

    - `"redacted_thinking" type`

  - `BetaToolUseBlock`

    - `string id`

    - `array<string,mixed> input`

    - `string name`

    - `"tool_use" type`

    - `?Caller caller`

      Tool invocation directly from the model.

  - `BetaServerToolUseBlock`

    - `string id`

    - `array<string,mixed> input`

    - `Name name`

    - `"server_tool_use" type`

    - `?Caller caller`

      Tool invocation directly from the model.

  - `BetaWebSearchToolResultBlock`

    - `BetaWebSearchToolResultBlockContent content`

    - `string toolUseID`

    - `"web_search_tool_result" type`

    - `?Caller caller`

      Tool invocation directly from the model.

  - `BetaWebFetchToolResultBlock`

    - `Content content`

    - `string toolUseID`

    - `"web_fetch_tool_result" type`

    - `?Caller caller`

      Tool invocation directly from the model.

  - `BetaAdvisorToolResultBlock`

    - `Content content`

    - `string toolUseID`

    - `"advisor_tool_result" type`

  - `BetaCodeExecutionToolResultBlock`

    - `BetaCodeExecutionToolResultBlockContent content`

      Code execution result with encrypted stdout for PFC + web_search results.

    - `string toolUseID`

    - `"code_execution_tool_result" type`

  - `BetaBashCodeExecutionToolResultBlock`

    - `Content content`

    - `string toolUseID`

    - `"bash_code_execution_tool_result" type`

  - `BetaTextEditorCodeExecutionToolResultBlock`

    - `Content content`

    - `string toolUseID`

    - `"text_editor_code_execution_tool_result" type`

  - `BetaToolSearchToolResultBlock`

    - `Content content`

    - `string toolUseID`

    - `"tool_search_tool_result" type`

  - `BetaMCPToolUseBlock`

    - `string id`

    - `array<string,mixed> input`

    - `string name`

      The name of the MCP tool

    - `string serverName`

      The name of the MCP server

    - `"mcp_tool_use" type`

  - `BetaMCPToolResultBlock`

    - `Content content`

    - `bool isError`

    - `string toolUseID`

    - `"mcp_tool_result" type`

  - `BetaContainerUploadBlock`

    - `string fileID`

    - `"container_upload" type`

  - `BetaCompactionBlock`

    - `?string content`

      Summary of compacted content, or null if compaction failed

    - `?string encryptedContent`

      Opaque metadata from prior compaction, to be round-tripped verbatim

    - `"compaction" type`

### Beta Content Block Param

- `BetaContentBlockParam`

  - `BetaTextBlockParam`

    - `string text`

    - `"text" type`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?list<BetaTextCitationParam> citations`

  - `BetaImageBlockParam`

    - `Source source`

    - `"image" type`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

  - `BetaRequestDocumentBlock`

    - `Source source`

    - `"document" type`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?BetaCitationsConfigParam citations`

    - `?string context`

    - `?string title`

  - `BetaSearchResultBlockParam`

    - `list<BetaTextBlockParam> content`

    - `string source`

    - `string title`

    - `"search_result" type`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?BetaCitationsConfigParam citations`

  - `BetaThinkingBlockParam`

    - `string signature`

    - `string thinking`

    - `"thinking" type`

  - `BetaRedactedThinkingBlockParam`

    - `string data`

    - `"redacted_thinking" type`

  - `BetaToolUseBlockParam`

    - `string id`

    - `array<string,mixed> input`

    - `string name`

    - `"tool_use" type`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?Caller caller`

      Tool invocation directly from the model.

  - `BetaToolResultBlockParam`

    - `string toolUseID`

    - `"tool_result" type`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?Content content`

    - `?bool isError`

  - `BetaServerToolUseBlockParam`

    - `string id`

    - `array<string,mixed> input`

    - `Name name`

    - `"server_tool_use" type`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?Caller caller`

      Tool invocation directly from the model.

  - `BetaWebSearchToolResultBlockParam`

    - `BetaWebSearchToolResultBlockParamContent content`

    - `string toolUseID`

    - `"web_search_tool_result" type`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?Caller caller`

      Tool invocation directly from the model.

  - `BetaWebFetchToolResultBlockParam`

    - `Content content`

    - `string toolUseID`

    - `"web_fetch_tool_result" type`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?Caller caller`

      Tool invocation directly from the model.

  - `BetaAdvisorToolResultBlockParam`

    - `Content content`

    - `string toolUseID`

    - `"advisor_tool_result" type`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

  - `BetaCodeExecutionToolResultBlockParam`

    - `BetaCodeExecutionToolResultBlockParamContent content`

      Code execution result with encrypted stdout for PFC + web_search results.

    - `string toolUseID`

    - `"code_execution_tool_result" type`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

  - `BetaBashCodeExecutionToolResultBlockParam`

    - `Content content`

    - `string toolUseID`

    - `"bash_code_execution_tool_result" type`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

  - `BetaTextEditorCodeExecutionToolResultBlockParam`

    - `Content content`

    - `string toolUseID`

    - `"text_editor_code_execution_tool_result" type`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

  - `BetaToolSearchToolResultBlockParam`

    - `Content content`

    - `string toolUseID`

    - `"tool_search_tool_result" type`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

  - `BetaMCPToolUseBlockParam`

    - `string id`

    - `array<string,mixed> input`

    - `string name`

    - `string serverName`

      The name of the MCP server

    - `"mcp_tool_use" type`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

  - `BetaRequestMCPToolResultBlockParam`

    - `string toolUseID`

    - `"mcp_tool_result" type`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?Content content`

    - `?bool isError`

  - `BetaContainerUploadBlockParam`

    - `string fileID`

    - `"container_upload" type`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

  - `BetaCompactionBlockParam`

    - `"compaction" type`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?string content`

      Summary of previously compacted content, or null if compaction failed

    - `?string encryptedContent`

      Opaque metadata from prior compaction, to be round-tripped verbatim

  - `BetaMidConversationSystemBlockParam`

    - `list<BetaTextBlockParam> content`

      System instruction text blocks.

    - `"mid_conv_system" type`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

### Beta Content Block Source

- `BetaContentBlockSource`

  - `Content content`

  - `"content" type`

### Beta Content Block Source Content

- `BetaContentBlockSourceContent`

  - `BetaTextBlockParam`

    - `string text`

    - `"text" type`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?list<BetaTextCitationParam> citations`

  - `BetaImageBlockParam`

    - `Source source`

    - `"image" type`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

### Beta Context Management Config

- `BetaContextManagementConfig`

  - `?list<Edit> edits`

    List of context management edits to apply

### Beta Context Management Response

- `BetaContextManagementResponse`

  - `list<AppliedEdit> appliedEdits`

    List of context management edits that were applied.

### Beta Count Tokens Context Management Response

- `BetaCountTokensContextManagementResponse`

  - `int originalInputTokens`

    The original token count before context management was applied

### Beta Diagnostics

- `BetaDiagnostics`

  - `?CacheMissReason cacheMissReason`

    Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

### Beta Diagnostics Param

- `BetaDiagnosticsParam`

  - `?string previousMessageID`

    The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.

### Beta Direct Caller

- `BetaDirectCaller`

  - `"direct" type`

### Beta Document Block

- `BetaDocumentBlock`

  - `?BetaCitationConfig citations`

    Citation configuration for the document

  - `Source source`

  - `?string title`

    The title of the document

  - `"document" type`

### Beta Encrypted Code Execution Result Block

- `BetaEncryptedCodeExecutionResultBlock`

  - `list<BetaCodeExecutionOutputBlock> content`

  - `string encryptedStdout`

  - `int returnCode`

  - `string stderr`

  - `"encrypted_code_execution_result" type`

### Beta Encrypted Code Execution Result Block Param

- `BetaEncryptedCodeExecutionResultBlockParam`

  - `list<BetaCodeExecutionOutputBlockParam> content`

  - `string encryptedStdout`

  - `int returnCode`

  - `string stderr`

  - `"encrypted_code_execution_result" type`

### Beta File Document Source

- `BetaFileDocumentSource`

  - `string fileID`

  - `"file" type`

### Beta File Image Source

- `BetaFileImageSource`

  - `string fileID`

  - `"file" type`

### Beta Image Block Param

- `BetaImageBlockParam`

  - `Source source`

  - `"image" type`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Beta Input JSON Delta

- `BetaInputJSONDelta`

  - `string partialJSON`

  - `"input_json_delta" type`

### Beta Input Tokens Clear At Least

- `BetaInputTokensClearAtLeast`

  - `"input_tokens" type`

  - `int value`

### Beta Input Tokens Trigger

- `BetaInputTokensTrigger`

  - `"input_tokens" type`

  - `int value`

### Beta Iterations Usage

- `list<BetaIterationsUsageItem>`

  - `BetaMessageIterationUsage`

    - `?BetaCacheCreation cacheCreation`

      Breakdown of cached tokens by TTL

    - `int cacheCreationInputTokens`

      The number of input tokens used to create the cache entry.

    - `int cacheReadInputTokens`

      The number of input tokens read from the cache.

    - `int inputTokens`

      The number of input tokens which were used.

    - `int outputTokens`

      The number of output tokens which were used.

    - `"message" type`

      Usage for a sampling iteration

  - `BetaCompactionIterationUsage`

    - `?BetaCacheCreation cacheCreation`

      Breakdown of cached tokens by TTL

    - `int cacheCreationInputTokens`

      The number of input tokens used to create the cache entry.

    - `int cacheReadInputTokens`

      The number of input tokens read from the cache.

    - `int inputTokens`

      The number of input tokens which were used.

    - `int outputTokens`

      The number of output tokens which were used.

    - `"compaction" type`

      Usage for a compaction iteration

  - `BetaAdvisorMessageIterationUsage`

    - `?BetaCacheCreation cacheCreation`

      Breakdown of cached tokens by TTL

    - `int cacheCreationInputTokens`

      The number of input tokens used to create the cache entry.

    - `int cacheReadInputTokens`

      The number of input tokens read from the cache.

    - `int inputTokens`

      The number of input tokens which were used.

    - `Model model`

      The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `int outputTokens`

      The number of output tokens which were used.

    - `"advisor_message" type`

      Usage for an advisor sub-inference iteration

### Beta JSON Output Format

- `BetaJSONOutputFormat`

  - `array<string,mixed> schema`

    The JSON schema of the format

  - `"json_schema" type`

### Beta MCP Tool Config

- `BetaMCPToolConfig`

  - `?bool deferLoading`

  - `?bool enabled`

### Beta MCP Tool Default Config

- `BetaMCPToolDefaultConfig`

  - `?bool deferLoading`

  - `?bool enabled`

### Beta MCP Tool Result Block

- `BetaMCPToolResultBlock`

  - `Content content`

  - `bool isError`

  - `string toolUseID`

  - `"mcp_tool_result" type`

### Beta MCP Tool Use Block

- `BetaMCPToolUseBlock`

  - `string id`

  - `array<string,mixed> input`

  - `string name`

    The name of the MCP tool

  - `string serverName`

    The name of the MCP server

  - `"mcp_tool_use" type`

### Beta MCP Tool Use Block Param

- `BetaMCPToolUseBlockParam`

  - `string id`

  - `array<string,mixed> input`

  - `string name`

  - `string serverName`

    The name of the MCP server

  - `"mcp_tool_use" type`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Beta MCP Toolset

- `BetaMCPToolset`

  - `string mcpServerName`

    Name of the MCP server to configure tools for

  - `"mcp_toolset" type`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?array<string,BetaMCPToolConfig> configs`

    Configuration overrides for specific tools, keyed by tool name

  - `?BetaMCPToolDefaultConfig defaultConfig`

    Default configuration applied to all tools from this server

### Beta Memory Tool 20250818

- `BetaMemoryTool20250818`

  - `"memory" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"memory_20250818" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Memory Tool 20250818 Command

- `BetaMemoryTool20250818Command`

  - `BetaMemoryTool20250818ViewCommand`

    - `"view" command`

      Command type identifier

    - `string path`

      Path to directory or file to view

    - `?list<int> viewRange`

      Optional line range for viewing specific lines

  - `BetaMemoryTool20250818CreateCommand`

    - `"create" command`

      Command type identifier

    - `string fileText`

      Content to write to the file

    - `string path`

      Path where the file should be created

  - `BetaMemoryTool20250818StrReplaceCommand`

    - `"str_replace" command`

      Command type identifier

    - `string newStr`

      Text to replace with

    - `string oldStr`

      Text to search for and replace

    - `string path`

      Path to the file where text should be replaced

  - `BetaMemoryTool20250818InsertCommand`

    - `"insert" command`

      Command type identifier

    - `int insertLine`

      Line number where text should be inserted

    - `string insertText`

      Text to insert at the specified line

    - `string path`

      Path to the file where text should be inserted

  - `BetaMemoryTool20250818DeleteCommand`

    - `"delete" command`

      Command type identifier

    - `string path`

      Path to the file or directory to delete

  - `BetaMemoryTool20250818RenameCommand`

    - `"rename" command`

      Command type identifier

    - `string newPath`

      New path for the file or directory

    - `string oldPath`

      Current path of the file or directory

### Beta Memory Tool 20250818 Create Command

- `BetaMemoryTool20250818CreateCommand`

  - `"create" command`

    Command type identifier

  - `string fileText`

    Content to write to the file

  - `string path`

    Path where the file should be created

### Beta Memory Tool 20250818 Delete Command

- `BetaMemoryTool20250818DeleteCommand`

  - `"delete" command`

    Command type identifier

  - `string path`

    Path to the file or directory to delete

### Beta Memory Tool 20250818 Insert Command

- `BetaMemoryTool20250818InsertCommand`

  - `"insert" command`

    Command type identifier

  - `int insertLine`

    Line number where text should be inserted

  - `string insertText`

    Text to insert at the specified line

  - `string path`

    Path to the file where text should be inserted

### Beta Memory Tool 20250818 Rename Command

- `BetaMemoryTool20250818RenameCommand`

  - `"rename" command`

    Command type identifier

  - `string newPath`

    New path for the file or directory

  - `string oldPath`

    Current path of the file or directory

### Beta Memory Tool 20250818 Str Replace Command

- `BetaMemoryTool20250818StrReplaceCommand`

  - `"str_replace" command`

    Command type identifier

  - `string newStr`

    Text to replace with

  - `string oldStr`

    Text to search for and replace

  - `string path`

    Path to the file where text should be replaced

### Beta Memory Tool 20250818 View Command

- `BetaMemoryTool20250818ViewCommand`

  - `"view" command`

    Command type identifier

  - `string path`

    Path to directory or file to view

  - `?list<int> viewRange`

    Optional line range for viewing specific lines

### Beta Message

- `BetaMessage`

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `?BetaContainer container`

    Information about the container used in the request (for the code execution tool)

  - `list<BetaContentBlock> content`

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

  - `?BetaContextManagementResponse contextManagement`

    Context management response.

    Information about context management strategies applied during the request.

  - `?BetaDiagnostics diagnostics`

    Response envelope for request-level diagnostics. Present (possibly
    null) whenever the caller supplied `diagnostics` on the request.

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `"assistant" role`

    Conversational role of the generated message.

    This will always be `"assistant"`.

  - `?BetaRefusalStopDetails stopDetails`

    Structured information about a refusal.

  - `?BetaStopReason stopReason`

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

  - `BetaUsage usage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

### Beta Message Delta Usage

- `BetaMessageDeltaUsage`

  - `?int cacheCreationInputTokens`

    The cumulative number of input tokens used to create the cache entry.

  - `?int cacheReadInputTokens`

    The cumulative number of input tokens read from the cache.

  - `?int inputTokens`

    The cumulative number of input tokens which were used.

  - `?list<BetaIterationsUsageItem> iterations`

    Per-iteration token usage breakdown.

    Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

    - Determine which iterations exceeded long context thresholds (>=200k tokens)
    - Calculate the true context window size from the last iteration
    - Understand token accumulation across server-side tool use loops

  - `int outputTokens`

    The cumulative number of output tokens which were used.

  - `?BetaOutputTokensDetails outputTokensDetails`

    Breakdown of output tokens by category.

    `output_tokens` remains the inclusive, authoritative total used for billing.
    This object provides a read-only decomposition for observability — for example,
    how many of the billed output tokens were spent on internal reasoning that may
    have been summarized before being returned to you.

  - `?BetaServerToolUsage serverToolUse`

    The number of server tool requests.

### Beta Message Iteration Usage

- `BetaMessageIterationUsage`

  - `?BetaCacheCreation cacheCreation`

    Breakdown of cached tokens by TTL

  - `int cacheCreationInputTokens`

    The number of input tokens used to create the cache entry.

  - `int cacheReadInputTokens`

    The number of input tokens read from the cache.

  - `int inputTokens`

    The number of input tokens which were used.

  - `int outputTokens`

    The number of output tokens which were used.

  - `"message" type`

    Usage for a sampling iteration

### Beta Message Param

- `BetaMessageParam`

  - `Content content`

  - `Role role`

### Beta Message Tokens Count

- `BetaMessageTokensCount`

  - `?BetaCountTokensContextManagementResponse contextManagement`

    Information about context management applied to the message.

  - `int inputTokens`

    The total number of tokens across the provided list of messages, system prompt, and tools.

### Beta Metadata

- `BetaMetadata`

  - `?string userID`

    An external identifier for the user who is associated with the request.

    This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

### Beta Mid Conversation System Block Param

- `BetaMidConversationSystemBlockParam`

  - `list<BetaTextBlockParam> content`

    System instruction text blocks.

  - `"mid_conv_system" type`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Beta Output Config

- `BetaOutputConfig`

  - `?Effort effort`

    All possible effort levels.

  - `?BetaJSONOutputFormat format`

    A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

  - `?BetaTokenTaskBudget taskBudget`

    User-configurable total token budget across contexts.

### Beta Output Tokens Details

- `BetaOutputTokensDetails`

  - `int thinkingTokens`

    Number of output tokens the model generated as internal reasoning, including
    the thinking-block delimiter tokens.

    Reflects the raw reasoning the model produced, not the (possibly shorter)
    summarized thinking text returned in the response body. Computed by
    re-tokenizing the raw reasoning text, so it may differ from the model's exact
    generation count by a small number of tokens. Always ≤ `output_tokens`;
    `output_tokens - thinking_tokens` approximates the non-reasoning output.

### Beta Plain Text Source

- `BetaPlainTextSource`

  - `string data`

  - `"text/plain" mediaType`

  - `"text" type`

### Beta Raw Content Block Delta

- `BetaRawContentBlockDelta`

  - `BetaTextDelta`

    - `string text`

    - `"text_delta" type`

  - `BetaInputJSONDelta`

    - `string partialJSON`

    - `"input_json_delta" type`

  - `BetaCitationsDelta`

    - `Citation citation`

    - `"citations_delta" type`

  - `BetaThinkingDelta`

    - `?int estimatedTokens`

      Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

    - `string thinking`

    - `"thinking_delta" type`

  - `BetaSignatureDelta`

    - `string signature`

    - `"signature_delta" type`

  - `BetaCompactionContentBlockDelta`

    - `?string content`

    - `?string encryptedContent`

      Opaque metadata from prior compaction, to be round-tripped verbatim

    - `"compaction_delta" type`

### Beta Raw Content Block Delta Event

- `BetaRawContentBlockDeltaEvent`

  - `BetaRawContentBlockDelta delta`

  - `int index`

  - `"content_block_delta" type`

### Beta Raw Content Block Start Event

- `BetaRawContentBlockStartEvent`

  - `ContentBlock contentBlock`

    Response model for a file uploaded to the container.

  - `int index`

  - `"content_block_start" type`

### Beta Raw Content Block Stop Event

- `BetaRawContentBlockStopEvent`

  - `int index`

  - `"content_block_stop" type`

### Beta Raw Message Delta Event

- `BetaRawMessageDeltaEvent`

  - `?BetaContextManagementResponse contextManagement`

    Information about context management strategies applied during the request

  - `Delta delta`

  - `"message_delta" type`

  - `BetaMessageDeltaUsage usage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

### Beta Raw Message Start Event

- `BetaRawMessageStartEvent`

  - `BetaMessage message`

  - `"message_start" type`

### Beta Raw Message Stop Event

- `BetaRawMessageStopEvent`

  - `"message_stop" type`

### Beta Raw Message Stream Event

- `BetaRawMessageStreamEvent`

  - `BetaRawMessageStartEvent`

    - `BetaMessage message`

    - `"message_start" type`

  - `BetaRawMessageDeltaEvent`

    - `?BetaContextManagementResponse contextManagement`

      Information about context management strategies applied during the request

    - `Delta delta`

    - `"message_delta" type`

    - `BetaMessageDeltaUsage usage`

      Billing and rate-limit usage.

      Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

      Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

      For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

      Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

  - `BetaRawMessageStopEvent`

    - `"message_stop" type`

  - `BetaRawContentBlockStartEvent`

    - `ContentBlock contentBlock`

      Response model for a file uploaded to the container.

    - `int index`

    - `"content_block_start" type`

  - `BetaRawContentBlockDeltaEvent`

    - `BetaRawContentBlockDelta delta`

    - `int index`

    - `"content_block_delta" type`

  - `BetaRawContentBlockStopEvent`

    - `int index`

    - `"content_block_stop" type`

### Beta Redacted Thinking Block

- `BetaRedactedThinkingBlock`

  - `string data`

  - `"redacted_thinking" type`

### Beta Redacted Thinking Block Param

- `BetaRedactedThinkingBlockParam`

  - `string data`

  - `"redacted_thinking" type`

### Beta Refusal Stop Details

- `BetaRefusalStopDetails`

  - `?Category category`

    The policy category that triggered the refusal.

    `null` when the refusal doesn't map to a named category.

  - `?string explanation`

    Human-readable explanation of the refusal.

    This text is not guaranteed to be stable. `null` when no explanation is available for the category.

  - `"refusal" type`

### Beta Request Document Block

- `BetaRequestDocumentBlock`

  - `Source source`

  - `"document" type`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?BetaCitationsConfigParam citations`

  - `?string context`

  - `?string title`

### Beta Request MCP Server Tool Configuration

- `BetaRequestMCPServerToolConfiguration`

  - `?list<string> allowedTools`

  - `?bool enabled`

### Beta Request MCP Server URL Definition

- `BetaRequestMCPServerURLDefinition`

  - `string name`

  - `"url" type`

  - `string url`

  - `?string authorizationToken`

  - `?BetaRequestMCPServerToolConfiguration toolConfiguration`

### Beta Request MCP Tool Result Block Param

- `BetaRequestMCPToolResultBlockParam`

  - `string toolUseID`

  - `"mcp_tool_result" type`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?Content content`

  - `?bool isError`

### Beta Search Result Block Param

- `BetaSearchResultBlockParam`

  - `list<BetaTextBlockParam> content`

  - `string source`

  - `string title`

  - `"search_result" type`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?BetaCitationsConfigParam citations`

### Beta Server Tool Caller

- `BetaServerToolCaller`

  - `string toolID`

  - `"code_execution_20250825" type`

### Beta Server Tool Caller 20260120

- `BetaServerToolCaller20260120`

  - `string toolID`

  - `"code_execution_20260120" type`

### Beta Server Tool Usage

- `BetaServerToolUsage`

  - `int webFetchRequests`

    The number of web fetch tool requests.

  - `int webSearchRequests`

    The number of web search tool requests.

### Beta Server Tool Use Block

- `BetaServerToolUseBlock`

  - `string id`

  - `array<string,mixed> input`

  - `Name name`

  - `"server_tool_use" type`

  - `?Caller caller`

    Tool invocation directly from the model.

### Beta Server Tool Use Block Param

- `BetaServerToolUseBlockParam`

  - `string id`

  - `array<string,mixed> input`

  - `Name name`

  - `"server_tool_use" type`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?Caller caller`

    Tool invocation directly from the model.

### Beta Signature Delta

- `BetaSignatureDelta`

  - `string signature`

  - `"signature_delta" type`

### Beta Skill

- `BetaSkill`

  - `string skillID`

    Skill ID

  - `Type type`

    Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

  - `string version`

    Skill version or 'latest' for most recent version

### Beta Skill Params

- `BetaSkillParams`

  - `string skillID`

    Skill ID

  - `Type type`

    Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

  - `?string version`

    Skill version or 'latest' for most recent version

### Beta Stop Reason

- `BetaStopReason`

  - `"end_turn"`

  - `"max_tokens"`

  - `"stop_sequence"`

  - `"tool_use"`

  - `"pause_turn"`

  - `"compaction"`

  - `"refusal"`

  - `"model_context_window_exceeded"`

### Beta Text Block

- `BetaTextBlock`

  - `?list<BetaTextCitation> citations`

    Citations supporting the text block.

    The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

  - `string text`

  - `"text" type`

### Beta Text Block Param

- `BetaTextBlockParam`

  - `string text`

  - `"text" type`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?list<BetaTextCitationParam> citations`

### Beta Text Citation

- `BetaTextCitation`

  - `BetaCitationCharLocation`

    - `string citedText`

    - `int documentIndex`

    - `?string documentTitle`

    - `int endCharIndex`

    - `?string fileID`

    - `int startCharIndex`

    - `"char_location" type`

  - `BetaCitationPageLocation`

    - `string citedText`

    - `int documentIndex`

    - `?string documentTitle`

    - `int endPageNumber`

    - `?string fileID`

    - `int startPageNumber`

    - `"page_location" type`

  - `BetaCitationContentBlockLocation`

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

  - `BetaCitationsWebSearchResultLocation`

    - `string citedText`

    - `string encryptedIndex`

    - `?string title`

    - `"web_search_result_location" type`

    - `string url`

  - `BetaCitationSearchResultLocation`

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

### Beta Text Citation Param

- `BetaTextCitationParam`

  - `BetaCitationCharLocationParam`

    - `string citedText`

    - `int documentIndex`

    - `?string documentTitle`

    - `int endCharIndex`

    - `int startCharIndex`

    - `"char_location" type`

  - `BetaCitationPageLocationParam`

    - `string citedText`

    - `int documentIndex`

    - `?string documentTitle`

    - `int endPageNumber`

    - `int startPageNumber`

    - `"page_location" type`

  - `BetaCitationContentBlockLocationParam`

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

  - `BetaCitationWebSearchResultLocationParam`

    - `string citedText`

    - `string encryptedIndex`

    - `?string title`

    - `"web_search_result_location" type`

    - `string url`

  - `BetaCitationSearchResultLocationParam`

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

### Beta Text Delta

- `BetaTextDelta`

  - `string text`

  - `"text_delta" type`

### Beta Text Editor Code Execution Create Result Block

- `BetaTextEditorCodeExecutionCreateResultBlock`

  - `bool isFileUpdate`

  - `"text_editor_code_execution_create_result" type`

### Beta Text Editor Code Execution Create Result Block Param

- `BetaTextEditorCodeExecutionCreateResultBlockParam`

  - `bool isFileUpdate`

  - `"text_editor_code_execution_create_result" type`

### Beta Text Editor Code Execution Str Replace Result Block

- `BetaTextEditorCodeExecutionStrReplaceResultBlock`

  - `?list<string> lines`

  - `?int newLines`

  - `?int newStart`

  - `?int oldLines`

  - `?int oldStart`

  - `"text_editor_code_execution_str_replace_result" type`

### Beta Text Editor Code Execution Str Replace Result Block Param

- `BetaTextEditorCodeExecutionStrReplaceResultBlockParam`

  - `"text_editor_code_execution_str_replace_result" type`

  - `?list<string> lines`

  - `?int newLines`

  - `?int newStart`

  - `?int oldLines`

  - `?int oldStart`

### Beta Text Editor Code Execution Tool Result Block

- `BetaTextEditorCodeExecutionToolResultBlock`

  - `Content content`

  - `string toolUseID`

  - `"text_editor_code_execution_tool_result" type`

### Beta Text Editor Code Execution Tool Result Block Param

- `BetaTextEditorCodeExecutionToolResultBlockParam`

  - `Content content`

  - `string toolUseID`

  - `"text_editor_code_execution_tool_result" type`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Beta Text Editor Code Execution Tool Result Error

- `BetaTextEditorCodeExecutionToolResultError`

  - `ErrorCode errorCode`

  - `?string errorMessage`

  - `"text_editor_code_execution_tool_result_error" type`

### Beta Text Editor Code Execution Tool Result Error Param

- `BetaTextEditorCodeExecutionToolResultErrorParam`

  - `ErrorCode errorCode`

  - `"text_editor_code_execution_tool_result_error" type`

  - `?string errorMessage`

### Beta Text Editor Code Execution View Result Block

- `BetaTextEditorCodeExecutionViewResultBlock`

  - `string content`

  - `FileType fileType`

  - `?int numLines`

  - `?int startLine`

  - `?int totalLines`

  - `"text_editor_code_execution_view_result" type`

### Beta Text Editor Code Execution View Result Block Param

- `BetaTextEditorCodeExecutionViewResultBlockParam`

  - `string content`

  - `FileType fileType`

  - `"text_editor_code_execution_view_result" type`

  - `?int numLines`

  - `?int startLine`

  - `?int totalLines`

### Beta Thinking Block

- `BetaThinkingBlock`

  - `string signature`

  - `string thinking`

  - `"thinking" type`

### Beta Thinking Block Param

- `BetaThinkingBlockParam`

  - `string signature`

  - `string thinking`

  - `"thinking" type`

### Beta Thinking Config Adaptive

- `BetaThinkingConfigAdaptive`

  - `"adaptive" type`

  - `?Display display`

    Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

### Beta Thinking Config Disabled

- `BetaThinkingConfigDisabled`

  - `"disabled" type`

### Beta Thinking Config Enabled

- `BetaThinkingConfigEnabled`

  - `int budgetTokens`

    Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

    Must be ≥1024 and less than `max_tokens`.

    See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

  - `"enabled" type`

  - `?Display display`

    Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

### Beta Thinking Config Param

- `BetaThinkingConfigParam`

  - `BetaThinkingConfigEnabled`

    - `int budgetTokens`

      Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

      Must be ≥1024 and less than `max_tokens`.

      See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

    - `"enabled" type`

    - `?Display display`

      Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

  - `BetaThinkingConfigDisabled`

    - `"disabled" type`

  - `BetaThinkingConfigAdaptive`

    - `"adaptive" type`

    - `?Display display`

      Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

### Beta Thinking Delta

- `BetaThinkingDelta`

  - `?int estimatedTokens`

    Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

  - `string thinking`

  - `"thinking_delta" type`

### Beta Thinking Turns

- `BetaThinkingTurns`

  - `"thinking_turns" type`

  - `int value`

### Beta Token Task Budget

- `BetaTokenTaskBudget`

  - `int total`

    Total token budget across all contexts in the session.

  - `"tokens" type`

    The budget type. Currently only 'tokens' is supported.

  - `?int remaining`

    Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.

### Beta Tool

- `BetaTool`

  - `InputSchema inputSchema`

    [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

    This defines the shape of the `input` that your tool accepts and that the model will produce.

  - `string name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

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

### Beta Tool Bash 20241022

- `BetaToolBash20241022`

  - `"bash" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"bash_20241022" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Bash 20250124

- `BetaToolBash20250124`

  - `"bash" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"bash_20250124" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Choice

- `BetaToolChoice`

  - `BetaToolChoiceAuto`

    - `"auto" type`

    - `?bool disableParallelToolUse`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output at most one tool use.

  - `BetaToolChoiceAny`

    - `"any" type`

    - `?bool disableParallelToolUse`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output exactly one tool use.

  - `BetaToolChoiceTool`

    - `string name`

      The name of the tool to use.

    - `"tool" type`

    - `?bool disableParallelToolUse`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output exactly one tool use.

  - `BetaToolChoiceNone`

    - `"none" type`

### Beta Tool Choice Any

- `BetaToolChoiceAny`

  - `"any" type`

  - `?bool disableParallelToolUse`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output exactly one tool use.

### Beta Tool Choice Auto

- `BetaToolChoiceAuto`

  - `"auto" type`

  - `?bool disableParallelToolUse`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output at most one tool use.

### Beta Tool Choice None

- `BetaToolChoiceNone`

  - `"none" type`

### Beta Tool Choice Tool

- `BetaToolChoiceTool`

  - `string name`

    The name of the tool to use.

  - `"tool" type`

  - `?bool disableParallelToolUse`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output exactly one tool use.

### Beta Tool Computer Use 20241022

- `BetaToolComputerUse20241022`

  - `int displayHeightPx`

    The height of the display in pixels.

  - `int displayWidthPx`

    The width of the display in pixels.

  - `"computer" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"computer_20241022" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int displayNumber`

    The X11 display number (e.g. 0, 1) for the display.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Computer Use 20250124

- `BetaToolComputerUse20250124`

  - `int displayHeightPx`

    The height of the display in pixels.

  - `int displayWidthPx`

    The width of the display in pixels.

  - `"computer" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"computer_20250124" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int displayNumber`

    The X11 display number (e.g. 0, 1) for the display.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Computer Use 20251124

- `BetaToolComputerUse20251124`

  - `int displayHeightPx`

    The height of the display in pixels.

  - `int displayWidthPx`

    The width of the display in pixels.

  - `"computer" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"computer_20251124" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int displayNumber`

    The X11 display number (e.g. 0, 1) for the display.

  - `?bool enableZoom`

    Whether to enable an action to take a zoomed-in screenshot of the screen.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Reference Block

- `BetaToolReferenceBlock`

  - `string toolName`

  - `"tool_reference" type`

### Beta Tool Reference Block Param

- `BetaToolReferenceBlockParam`

  - `string toolName`

  - `"tool_reference" type`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Beta Tool Result Block Param

- `BetaToolResultBlockParam`

  - `string toolUseID`

  - `"tool_result" type`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?Content content`

  - `?bool isError`

### Beta Tool Search Tool Bm25 20251119

- `BetaToolSearchToolBm25_20251119`

  - `"tool_search_tool_bm25" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `Type type`

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Search Tool Regex 20251119

- `BetaToolSearchToolRegex20251119`

  - `"tool_search_tool_regex" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `Type type`

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Search Tool Result Block

- `BetaToolSearchToolResultBlock`

  - `Content content`

  - `string toolUseID`

  - `"tool_search_tool_result" type`

### Beta Tool Search Tool Result Block Param

- `BetaToolSearchToolResultBlockParam`

  - `Content content`

  - `string toolUseID`

  - `"tool_search_tool_result" type`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Beta Tool Search Tool Result Error

- `BetaToolSearchToolResultError`

  - `ErrorCode errorCode`

  - `?string errorMessage`

  - `"tool_search_tool_result_error" type`

### Beta Tool Search Tool Result Error Param

- `BetaToolSearchToolResultErrorParam`

  - `ErrorCode errorCode`

  - `"tool_search_tool_result_error" type`

### Beta Tool Search Tool Search Result Block

- `BetaToolSearchToolSearchResultBlock`

  - `list<BetaToolReferenceBlock> toolReferences`

  - `"tool_search_tool_search_result" type`

### Beta Tool Search Tool Search Result Block Param

- `BetaToolSearchToolSearchResultBlockParam`

  - `list<BetaToolReferenceBlockParam> toolReferences`

  - `"tool_search_tool_search_result" type`

### Beta Tool Text Editor 20241022

- `BetaToolTextEditor20241022`

  - `"str_replace_editor" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"text_editor_20241022" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Text Editor 20250124

- `BetaToolTextEditor20250124`

  - `"str_replace_editor" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"text_editor_20250124" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Text Editor 20250429

- `BetaToolTextEditor20250429`

  - `"str_replace_based_edit_tool" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"text_editor_20250429" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Text Editor 20250728

- `BetaToolTextEditor20250728`

  - `"str_replace_based_edit_tool" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"text_editor_20250728" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?list<array<string,mixed>> inputExamples`

  - `?int maxCharacters`

    Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Union

- `BetaToolUnion`

  - `BetaTool`

    - `InputSchema inputSchema`

      [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

      This defines the shape of the `input` that your tool accepts and that the model will produce.

    - `string name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

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

  - `BetaToolBash20241022`

    - `"bash" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"bash_20241022" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `BetaToolBash20250124`

    - `"bash" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"bash_20250124" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `BetaCodeExecutionTool20250522`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"code_execution_20250522" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `BetaCodeExecutionTool20250825`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"code_execution_20250825" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `BetaCodeExecutionTool20260120`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"code_execution_20260120" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `BetaToolComputerUse20241022`

    - `int displayHeightPx`

      The height of the display in pixels.

    - `int displayWidthPx`

      The width of the display in pixels.

    - `"computer" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"computer_20241022" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int displayNumber`

      The X11 display number (e.g. 0, 1) for the display.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `BetaMemoryTool20250818`

    - `"memory" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"memory_20250818" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `BetaToolComputerUse20250124`

    - `int displayHeightPx`

      The height of the display in pixels.

    - `int displayWidthPx`

      The width of the display in pixels.

    - `"computer" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"computer_20250124" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int displayNumber`

      The X11 display number (e.g. 0, 1) for the display.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `BetaToolTextEditor20241022`

    - `"str_replace_editor" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"text_editor_20241022" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `BetaToolComputerUse20251124`

    - `int displayHeightPx`

      The height of the display in pixels.

    - `int displayWidthPx`

      The width of the display in pixels.

    - `"computer" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"computer_20251124" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int displayNumber`

      The X11 display number (e.g. 0, 1) for the display.

    - `?bool enableZoom`

      Whether to enable an action to take a zoomed-in screenshot of the screen.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `BetaToolTextEditor20250124`

    - `"str_replace_editor" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"text_editor_20250124" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `BetaToolTextEditor20250429`

    - `"str_replace_based_edit_tool" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"text_editor_20250429" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `BetaToolTextEditor20250728`

    - `"str_replace_based_edit_tool" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"text_editor_20250728" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?int maxCharacters`

      Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `BetaWebSearchTool20250305`

    - `"web_search" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"web_search_20250305" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `?list<string> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?BetaUserLocation userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `BetaWebFetchTool20250910`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"web_fetch_20250910" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      List of domains to allow fetching from

    - `?list<string> blockedDomains`

      List of domains to block fetching from

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?BetaCitationsConfigParam citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `BetaWebSearchTool20260209`

    - `"web_search" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"web_search_20260209" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `?list<string> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?BetaUserLocation userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `BetaWebFetchTool20260209`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"web_fetch_20260209" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      List of domains to allow fetching from

    - `?list<string> blockedDomains`

      List of domains to block fetching from

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?BetaCitationsConfigParam citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `BetaWebFetchTool20260309`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"web_fetch_20260309" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      List of domains to allow fetching from

    - `?list<string> blockedDomains`

      List of domains to block fetching from

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?BetaCitationsConfigParam citations`

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

  - `BetaAdvisorTool20260301`

    - `Model model`

      The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `"advisor" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"advisor_20260301" type`

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?BetaCacheControlEphemeral caching`

      Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `BetaToolSearchToolBm25_20251119`

    - `"tool_search_tool_bm25" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `Type type`

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `BetaToolSearchToolRegex20251119`

    - `"tool_search_tool_regex" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `Type type`

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `BetaMCPToolset`

    - `string mcpServerName`

      Name of the MCP server to configure tools for

    - `"mcp_toolset" type`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?array<string,BetaMCPToolConfig> configs`

      Configuration overrides for specific tools, keyed by tool name

    - `?BetaMCPToolDefaultConfig defaultConfig`

      Default configuration applied to all tools from this server

### Beta Tool Use Block

- `BetaToolUseBlock`

  - `string id`

  - `array<string,mixed> input`

  - `string name`

  - `"tool_use" type`

  - `?Caller caller`

    Tool invocation directly from the model.

### Beta Tool Use Block Param

- `BetaToolUseBlockParam`

  - `string id`

  - `array<string,mixed> input`

  - `string name`

  - `"tool_use" type`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?Caller caller`

    Tool invocation directly from the model.

### Beta Tool Uses Keep

- `BetaToolUsesKeep`

  - `"tool_uses" type`

  - `int value`

### Beta Tool Uses Trigger

- `BetaToolUsesTrigger`

  - `"tool_uses" type`

  - `int value`

### Beta URL Image Source

- `BetaURLImageSource`

  - `"url" type`

  - `string url`

### Beta URL PDF Source

- `BetaURLPDFSource`

  - `"url" type`

  - `string url`

### Beta Usage

- `BetaUsage`

  - `?BetaCacheCreation cacheCreation`

    Breakdown of cached tokens by TTL

  - `?int cacheCreationInputTokens`

    The number of input tokens used to create the cache entry.

  - `?int cacheReadInputTokens`

    The number of input tokens read from the cache.

  - `?string inferenceGeo`

    The geographic region where inference was performed for this request.

  - `int inputTokens`

    The number of input tokens which were used.

  - `?list<BetaIterationsUsageItem> iterations`

    Per-iteration token usage breakdown.

    Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

    - Determine which iterations exceeded long context thresholds (>=200k tokens)
    - Calculate the true context window size from the last iteration
    - Understand token accumulation across server-side tool use loops

  - `int outputTokens`

    The number of output tokens which were used.

  - `?BetaOutputTokensDetails outputTokensDetails`

    Breakdown of output tokens by category.

    `output_tokens` remains the inclusive, authoritative total used for billing.
    This object provides a read-only decomposition for observability — for example,
    how many of the billed output tokens were spent on internal reasoning that may
    have been summarized before being returned to you.

  - `?BetaServerToolUsage serverToolUse`

    The number of server tool requests.

  - `?ServiceTier serviceTier`

    If the request used the priority, standard, or batch tier.

  - `?Speed speed`

    The inference speed mode used for this request.

### Beta User Location

- `BetaUserLocation`

  - `"approximate" type`

  - `?string city`

    The city of the user.

  - `?string country`

    The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

  - `?string region`

    The region of the user.

  - `?string timezone`

    The [IANA timezone](https://nodatime.org/TimeZones) of the user.

### Beta Web Fetch Block

- `BetaWebFetchBlock`

  - `BetaDocumentBlock content`

  - `?string retrievedAt`

    ISO 8601 timestamp when the content was retrieved

  - `"web_fetch_result" type`

  - `string url`

    Fetched content URL

### Beta Web Fetch Block Param

- `BetaWebFetchBlockParam`

  - `BetaRequestDocumentBlock content`

  - `"web_fetch_result" type`

  - `string url`

    Fetched content URL

  - `?string retrievedAt`

    ISO 8601 timestamp when the content was retrieved

### Beta Web Fetch Tool 20250910

- `BetaWebFetchTool20250910`

  - `"web_fetch" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"web_fetch_20250910" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?list<string> allowedDomains`

    List of domains to allow fetching from

  - `?list<string> blockedDomains`

    List of domains to block fetching from

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?BetaCitationsConfigParam citations`

    Citations configuration for fetched documents. Citations are disabled by default.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int maxContentTokens`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

  - `?int maxUses`

    Maximum number of times the tool can be used in the API request.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Web Fetch Tool 20260209

- `BetaWebFetchTool20260209`

  - `"web_fetch" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"web_fetch_20260209" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?list<string> allowedDomains`

    List of domains to allow fetching from

  - `?list<string> blockedDomains`

    List of domains to block fetching from

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?BetaCitationsConfigParam citations`

    Citations configuration for fetched documents. Citations are disabled by default.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int maxContentTokens`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

  - `?int maxUses`

    Maximum number of times the tool can be used in the API request.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Web Fetch Tool 20260309

- `BetaWebFetchTool20260309`

  - `"web_fetch" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"web_fetch_20260309" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?list<string> allowedDomains`

    List of domains to allow fetching from

  - `?list<string> blockedDomains`

    List of domains to block fetching from

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?BetaCitationsConfigParam citations`

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

### Beta Web Fetch Tool Result Block

- `BetaWebFetchToolResultBlock`

  - `Content content`

  - `string toolUseID`

  - `"web_fetch_tool_result" type`

  - `?Caller caller`

    Tool invocation directly from the model.

### Beta Web Fetch Tool Result Block Param

- `BetaWebFetchToolResultBlockParam`

  - `Content content`

  - `string toolUseID`

  - `"web_fetch_tool_result" type`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?Caller caller`

    Tool invocation directly from the model.

### Beta Web Fetch Tool Result Error Block

- `BetaWebFetchToolResultErrorBlock`

  - `BetaWebFetchToolResultErrorCode errorCode`

  - `"web_fetch_tool_result_error" type`

### Beta Web Fetch Tool Result Error Block Param

- `BetaWebFetchToolResultErrorBlockParam`

  - `BetaWebFetchToolResultErrorCode errorCode`

  - `"web_fetch_tool_result_error" type`

### Beta Web Fetch Tool Result Error Code

- `BetaWebFetchToolResultErrorCode`

  - `"invalid_tool_input"`

  - `"url_too_long"`

  - `"url_not_allowed"`

  - `"url_not_in_prior_context"`

  - `"url_not_accessible"`

  - `"unsupported_content_type"`

  - `"too_many_requests"`

  - `"max_uses_exceeded"`

  - `"unavailable"`

### Beta Web Search Result Block

- `BetaWebSearchResultBlock`

  - `string encryptedContent`

  - `?string pageAge`

  - `string title`

  - `"web_search_result" type`

  - `string url`

### Beta Web Search Result Block Param

- `BetaWebSearchResultBlockParam`

  - `string encryptedContent`

  - `string title`

  - `"web_search_result" type`

  - `string url`

  - `?string pageAge`

### Beta Web Search Tool 20250305

- `BetaWebSearchTool20250305`

  - `"web_search" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"web_search_20250305" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?list<string> allowedDomains`

    If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

  - `?list<string> blockedDomains`

    If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int maxUses`

    Maximum number of times the tool can be used in the API request.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

  - `?BetaUserLocation userLocation`

    Parameters for the user's location. Used to provide more relevant search results.

### Beta Web Search Tool 20260209

- `BetaWebSearchTool20260209`

  - `"web_search" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"web_search_20260209" type`

  - `?list<AllowedCaller> allowedCallers`

  - `?list<string> allowedDomains`

    If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

  - `?list<string> blockedDomains`

    If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int maxUses`

    Maximum number of times the tool can be used in the API request.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

  - `?BetaUserLocation userLocation`

    Parameters for the user's location. Used to provide more relevant search results.

### Beta Web Search Tool Request Error

- `BetaWebSearchToolRequestError`

  - `BetaWebSearchToolResultErrorCode errorCode`

  - `"web_search_tool_result_error" type`

### Beta Web Search Tool Result Block

- `BetaWebSearchToolResultBlock`

  - `BetaWebSearchToolResultBlockContent content`

  - `string toolUseID`

  - `"web_search_tool_result" type`

  - `?Caller caller`

    Tool invocation directly from the model.

### Beta Web Search Tool Result Block Content

- `BetaWebSearchToolResultBlockContent`

  - `BetaWebSearchToolResultError`

    - `BetaWebSearchToolResultErrorCode errorCode`

    - `"web_search_tool_result_error" type`

  - `list<BetaWebSearchResultBlock>`

    - `string encryptedContent`

    - `?string pageAge`

    - `string title`

    - `"web_search_result" type`

    - `string url`

### Beta Web Search Tool Result Block Param

- `BetaWebSearchToolResultBlockParam`

  - `BetaWebSearchToolResultBlockParamContent content`

  - `string toolUseID`

  - `"web_search_tool_result" type`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?Caller caller`

    Tool invocation directly from the model.

### Beta Web Search Tool Result Block Param Content

- `BetaWebSearchToolResultBlockParamContent`

  - `list<BetaWebSearchResultBlockParam>`

    - `string encryptedContent`

    - `string title`

    - `"web_search_result" type`

    - `string url`

    - `?string pageAge`

  - `BetaWebSearchToolRequestError`

    - `BetaWebSearchToolResultErrorCode errorCode`

    - `"web_search_tool_result_error" type`

### Beta Web Search Tool Result Error

- `BetaWebSearchToolResultError`

  - `BetaWebSearchToolResultErrorCode errorCode`

  - `"web_search_tool_result_error" type`

### Beta Web Search Tool Result Error Code

- `BetaWebSearchToolResultErrorCode`

  - `"invalid_tool_input"`

  - `"unavailable"`

  - `"max_uses_exceeded"`

  - `"too_many_requests"`

  - `"query_too_long"`

  - `"request_too_large"`

# Batches

## Create a Message Batch

`$client->beta->messages->batches->create(list<Request> requests, ?list<AnthropicBeta> betas): MessageBatch`

**post** `/v1/messages/batches`

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `requests: list<Request>`

  List of requests for prompt completion. Each is an individual request to create a Message.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

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

$betaMessageBatch = $client->beta->messages->batches->create(
  requests: [
    [
      'customID' => 'my-custom-id-1',
      'params' => [
        'maxTokens' => 1024,
        'messages' => [['content' => 'Hello, world', 'role' => 'user']],
        'model' => 'claude-opus-4-6',
        'cacheControl' => ['type' => 'ephemeral', 'ttl' => '5m'],
        'container' => [
          'id' => 'id',
          'skills' => [
            ['skillID' => 'pdf', 'type' => 'anthropic', 'version' => 'latest']
          ],
        ],
        'contextManagement' => [
          'edits' => [
            [
              'type' => 'clear_tool_uses_20250919',
              'clearAtLeast' => ['type' => 'input_tokens', 'value' => 0],
              'clearToolInputs' => true,
              'excludeTools' => ['string'],
              'keep' => ['type' => 'tool_uses', 'value' => 0],
              'trigger' => ['type' => 'input_tokens', 'value' => 1],
            ],
          ],
        ],
        'diagnostics' => ['previousMessageID' => 'previous_message_id'],
        'inferenceGeo' => 'inference_geo',
        'mcpServers' => [
          [
            'name' => 'name',
            'type' => 'url',
            'url' => 'url',
            'authorizationToken' => 'authorization_token',
            'toolConfiguration' => [
              'allowedTools' => ['string'], 'enabled' => true
            ],
          ],
        ],
        'metadata' => ['userID' => '13803d75-b4b5-4c3e-b2a2-6f21399b021b'],
        'outputConfig' => [
          'effort' => 'low',
          'format' => ['schema' => ['foo' => 'bar'], 'type' => 'json_schema'],
          'taskBudget' => [
            'total' => 1024, 'type' => 'tokens', 'remaining' => 0
          ],
        ],
        'outputFormat' => [
          'schema' => ['foo' => 'bar'], 'type' => 'json_schema'
        ],
        'serviceTier' => 'auto',
        'speed' => 'standard',
        'stopSequences' => ['string'],
        'stream' => true,
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
        'userProfileID' => 'user_profile_id',
      ],
    ],
  ],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaMessageBatch);
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

`$client->beta->messages->batches->retrieve(string messageBatchID, ?list<AnthropicBeta> betas): MessageBatch`

**get** `/v1/messages/batches/{message_batch_id}`

This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `messageBatchID: string`

  ID of the Message Batch.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

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

$betaMessageBatch = $client->beta->messages->batches->retrieve(
  'message_batch_id', betas: ['message-batches-2024-09-24']
);

var_dump($betaMessageBatch);
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

`$client->beta->messages->batches->list(?string afterID, ?string beforeID, ?int limit, ?list<AnthropicBeta> betas): Page<MessageBatch>`

**get** `/v1/messages/batches`

List all Message Batches within a Workspace. Most recently created batches are returned first.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `afterID?:optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `beforeID?:optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `limit?:optional int`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

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

$page = $client->beta->messages->batches->list(
  afterID: 'after_id',
  beforeID: 'before_id',
  limit: 1,
  betas: ['message-batches-2024-09-24'],
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

`$client->beta->messages->batches->cancel(string messageBatchID, ?list<AnthropicBeta> betas): MessageBatch`

**post** `/v1/messages/batches/{message_batch_id}/cancel`

Batches may be canceled any time before processing ends. Once cancellation is initiated, the batch enters a `canceling` state, at which time the system may complete any in-progress, non-interruptible requests before finalizing cancellation.

The number of canceled requests is specified in `request_counts`. To determine which requests were canceled, check the individual results within the batch. Note that cancellation may not result in any canceled requests if they were non-interruptible.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `messageBatchID: string`

  ID of the Message Batch.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

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

$betaMessageBatch = $client->beta->messages->batches->cancel(
  'message_batch_id', betas: ['message-batches-2024-09-24']
);

var_dump($betaMessageBatch);
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

`$client->beta->messages->batches->delete(string messageBatchID, ?list<AnthropicBeta> betas): DeletedMessageBatch`

**delete** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `messageBatchID: string`

  ID of the Message Batch.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

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

$betaDeletedMessageBatch = $client->beta->messages->batches->delete(
  'message_batch_id', betas: ['message-batches-2024-09-24']
);

var_dump($betaDeletedMessageBatch);
```

#### Response

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```

## Retrieve Message Batch results

`$client->beta->messages->batches->results(string messageBatchID, ?list<AnthropicBeta> betas): MessageBatchIndividualResponse`

**get** `/v1/messages/batches/{message_batch_id}/results`

Streams the results of a Message Batch as a `.jsonl` file.

Each line in the file is a JSON object containing the result of a single request in the Message Batch. Results are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `messageBatchID: string`

  ID of the Message Batch.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

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

$betaMessageBatchIndividualResponse = $client
  ->beta
  ->messages
  ->batches
  ->resultsStream('message_batch_id', betas: ['message-batches-2024-09-24']);

var_dump($betaMessageBatchIndividualResponse);
```

## Domain Types

### Beta Deleted Message Batch

- `DeletedMessageBatch`

  - `string id`

    ID of the Message Batch.

  - `"message_batch_deleted" type`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

### Beta Message Batch

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

### Beta Message Batch Canceled Result

- `MessageBatchCanceledResult`

  - `"canceled" type`

### Beta Message Batch Errored Result

- `MessageBatchErroredResult`

  - `BetaErrorResponse error`

  - `"errored" type`

### Beta Message Batch Expired Result

- `MessageBatchExpiredResult`

  - `"expired" type`

### Beta Message Batch Individual Response

- `MessageBatchIndividualResponse`

  - `string customID`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `MessageBatchResult result`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

### Beta Message Batch Request Counts

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

### Beta Message Batch Result

- `MessageBatchResult`

  - `MessageBatchSucceededResult`

    - `BetaMessage message`

    - `"succeeded" type`

  - `MessageBatchErroredResult`

    - `BetaErrorResponse error`

    - `"errored" type`

  - `MessageBatchCanceledResult`

    - `"canceled" type`

  - `MessageBatchExpiredResult`

    - `"expired" type`

### Beta Message Batch Succeeded Result

- `MessageBatchSucceededResult`

  - `BetaMessage message`

  - `"succeeded" type`
