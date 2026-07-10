# Beta

## Domain Types

### Anthropic Beta

- `AnthropicBeta`

  - `"message-batches-2024-09-24"`

  - `"prompt-caching-2024-07-31"`

  - `"computer-use-2024-10-22"`

  - `"computer-use-2025-01-24"`

  - `"pdfs-2024-09-25"`

  - `"token-counting-2024-11-01"`

  - `"token-efficient-tools-2025-02-19"`

  - `"output-128k-2025-02-19"`

  - `"files-api-2025-04-14"`

  - `"mcp-client-2025-04-04"`

  - `"mcp-client-2025-11-20"`

  - `"dev-full-thinking-2025-05-14"`

  - `"interleaved-thinking-2025-05-14"`

  - `"code-execution-2025-05-22"`

  - `"extended-cache-ttl-2025-04-11"`

  - `"context-1m-2025-08-07"`

  - `"context-management-2025-06-27"`

  - `"model-context-window-exceeded-2025-08-26"`

  - `"skills-2025-10-02"`

  - `"fast-mode-2026-02-01"`

  - `"output-300k-2026-03-24"`

  - `"user-profiles-2026-03-24"`

  - `"advisor-tool-2026-03-01"`

  - `"managed-agents-2026-04-01"`

  - `"cache-diagnosis-2026-04-07"`

  - `"thinking-token-count-2026-05-13"`

  - `"server-side-fallback-2026-06-01"`

  - `"fallback-credit-2026-06-01"`

  - `"agent-memory-2026-07-22"`

### Beta API Error

- `BetaAPIError`

  - `string message`

  - `"api_error" type`

### Beta Authentication Error

- `BetaAuthenticationError`

  - `string message`

  - `"authentication_error" type`

### Beta Billing Error

- `BetaBillingError`

  - `string message`

  - `"billing_error" type`

### Beta Error

- `BetaError`

  - `BetaInvalidRequestError`

    - `string message`

    - `"invalid_request_error" type`

  - `BetaAuthenticationError`

    - `string message`

    - `"authentication_error" type`

  - `BetaBillingError`

    - `string message`

    - `"billing_error" type`

  - `BetaPermissionError`

    - `string message`

    - `"permission_error" type`

  - `BetaNotFoundError`

    - `string message`

    - `"not_found_error" type`

  - `BetaRateLimitError`

    - `string message`

    - `"rate_limit_error" type`

  - `BetaGatewayTimeoutError`

    - `string message`

    - `"timeout_error" type`

  - `BetaAPIError`

    - `string message`

    - `"api_error" type`

  - `BetaOverloadedError`

    - `string message`

    - `"overloaded_error" type`

### Beta Error Response

- `BetaErrorResponse`

  - `BetaError error`

  - `?string requestID`

  - `"error" type`

### Beta Gateway Timeout Error

- `BetaGatewayTimeoutError`

  - `string message`

  - `"timeout_error" type`

### Beta Invalid Request Error

- `BetaInvalidRequestError`

  - `string message`

  - `"invalid_request_error" type`

### Beta Not Found Error

- `BetaNotFoundError`

  - `string message`

  - `"not_found_error" type`

### Beta Overloaded Error

- `BetaOverloadedError`

  - `string message`

  - `"overloaded_error" type`

### Beta Permission Error

- `BetaPermissionError`

  - `string message`

  - `"permission_error" type`

### Beta Rate Limit Error

- `BetaRateLimitError`

  - `string message`

  - `"rate_limit_error" type`

# Models

## List Models

`$client->beta->models->list(?string afterID, ?string beforeID, ?int limit, ?list<AnthropicBeta> betas): Page<BetaModelInfo>`

**get** `/v1/models`

List available models.

The Models API response can be used to determine which models are available for use in the API. More recently released models are listed first.

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

- `BetaModelInfo`

  - `string id`

    Unique model identifier.

  - `?list<string> allowedFallbackModels`

    Model IDs this model accepts as `fallbacks[i].model` on the Messages API. An empty list means the `fallbacks` parameter is not supported for this model as primary.

  - `?BetaModelCapabilities capabilities`

    Model capability information.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

  - `string displayName`

    A human-readable name for the model.

  - `?int maxInputTokens`

    Maximum input context window size in tokens for this model.

  - `?int maxTokens`

    Maximum value for the `max_tokens` parameter when using this model.

  - `"model" type`

    Object type.

    For Models, this is always `"model"`.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->models->list(
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
      "id": "claude-opus-4-6",
      "allowed_fallback_models": [
        "string"
      ],
      "capabilities": {
        "batch": {
          "supported": true
        },
        "citations": {
          "supported": true
        },
        "code_execution": {
          "supported": true
        },
        "context_management": {
          "clear_thinking_20251015": {
            "supported": true
          },
          "clear_tool_uses_20250919": {
            "supported": true
          },
          "compact_20260112": {
            "supported": true
          },
          "supported": true
        },
        "effort": {
          "high": {
            "supported": true
          },
          "low": {
            "supported": true
          },
          "max": {
            "supported": true
          },
          "medium": {
            "supported": true
          },
          "supported": true,
          "xhigh": {
            "supported": true
          }
        },
        "image_input": {
          "supported": true
        },
        "pdf_input": {
          "supported": true
        },
        "structured_outputs": {
          "supported": true
        },
        "thinking": {
          "supported": true,
          "types": {
            "adaptive": {
              "supported": true
            },
            "enabled": {
              "supported": true
            }
          }
        }
      },
      "created_at": "2026-02-04T00:00:00Z",
      "display_name": "Claude Opus 4.6",
      "max_input_tokens": 0,
      "max_tokens": 0,
      "type": "model"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

## Get a Model

`$client->beta->models->retrieve(string modelID, ?list<AnthropicBeta> betas): BetaModelInfo`

**get** `/v1/models/{model_id}`

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

### Parameters

- `modelID: string`

  Model identifier or alias.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaModelInfo`

  - `string id`

    Unique model identifier.

  - `?list<string> allowedFallbackModels`

    Model IDs this model accepts as `fallbacks[i].model` on the Messages API. An empty list means the `fallbacks` parameter is not supported for this model as primary.

  - `?BetaModelCapabilities capabilities`

    Model capability information.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

  - `string displayName`

    A human-readable name for the model.

  - `?int maxInputTokens`

    Maximum input context window size in tokens for this model.

  - `?int maxTokens`

    Maximum value for the `max_tokens` parameter when using this model.

  - `"model" type`

    Object type.

    For Models, this is always `"model"`.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaModelInfo = $client->beta->models->retrieve(
  'model_id', betas: ['message-batches-2024-09-24']
);

var_dump($betaModelInfo);
```

#### Response

```json
{
  "id": "claude-opus-4-6",
  "allowed_fallback_models": [
    "string"
  ],
  "capabilities": {
    "batch": {
      "supported": true
    },
    "citations": {
      "supported": true
    },
    "code_execution": {
      "supported": true
    },
    "context_management": {
      "clear_thinking_20251015": {
        "supported": true
      },
      "clear_tool_uses_20250919": {
        "supported": true
      },
      "compact_20260112": {
        "supported": true
      },
      "supported": true
    },
    "effort": {
      "high": {
        "supported": true
      },
      "low": {
        "supported": true
      },
      "max": {
        "supported": true
      },
      "medium": {
        "supported": true
      },
      "supported": true,
      "xhigh": {
        "supported": true
      }
    },
    "image_input": {
      "supported": true
    },
    "pdf_input": {
      "supported": true
    },
    "structured_outputs": {
      "supported": true
    },
    "thinking": {
      "supported": true,
      "types": {
        "adaptive": {
          "supported": true
        },
        "enabled": {
          "supported": true
        }
      }
    }
  },
  "created_at": "2026-02-04T00:00:00Z",
  "display_name": "Claude Opus 4.6",
  "max_input_tokens": 0,
  "max_tokens": 0,
  "type": "model"
}
```

## Domain Types

### Beta Capability Support

- `BetaCapabilitySupport`

  - `bool supported`

    Whether this capability is supported by the model.

### Beta Context Management Capability

- `BetaContextManagementCapability`

  - `?BetaCapabilitySupport clearThinking20251015`

    Indicates whether a capability is supported.

  - `?BetaCapabilitySupport clearToolUses20250919`

    Indicates whether a capability is supported.

  - `?BetaCapabilitySupport compact20260112`

    Indicates whether a capability is supported.

  - `bool supported`

    Whether this capability is supported by the model.

### Beta Effort Capability

- `BetaEffortCapability`

  - `BetaCapabilitySupport high`

    Whether the model supports high effort level.

  - `BetaCapabilitySupport low`

    Whether the model supports low effort level.

  - `BetaCapabilitySupport max`

    Whether the model supports max effort level.

  - `BetaCapabilitySupport medium`

    Whether the model supports medium effort level.

  - `bool supported`

    Whether this capability is supported by the model.

  - `?BetaCapabilitySupport xhigh`

    Indicates whether a capability is supported.

### Beta Model Capabilities

- `BetaModelCapabilities`

  - `BetaCapabilitySupport batch`

    Whether the model supports the Batch API.

  - `BetaCapabilitySupport citations`

    Whether the model supports citation generation.

  - `BetaCapabilitySupport codeExecution`

    Whether the model supports code execution tools.

  - `BetaContextManagementCapability contextManagement`

    Context management support and available strategies.

  - `BetaEffortCapability effort`

    Effort (reasoning_effort) support and available levels.

  - `BetaCapabilitySupport imageInput`

    Whether the model accepts image content blocks.

  - `BetaCapabilitySupport pdfInput`

    Whether the model accepts PDF content blocks.

  - `BetaCapabilitySupport structuredOutputs`

    Whether the model supports structured output / JSON mode / strict tool schemas.

  - `BetaThinkingCapability thinking`

    Thinking capability and supported type configurations.

### Beta Model Info

- `BetaModelInfo`

  - `string id`

    Unique model identifier.

  - `?list<string> allowedFallbackModels`

    Model IDs this model accepts as `fallbacks[i].model` on the Messages API. An empty list means the `fallbacks` parameter is not supported for this model as primary.

  - `?BetaModelCapabilities capabilities`

    Model capability information.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

  - `string displayName`

    A human-readable name for the model.

  - `?int maxInputTokens`

    Maximum input context window size in tokens for this model.

  - `?int maxTokens`

    Maximum value for the `max_tokens` parameter when using this model.

  - `"model" type`

    Object type.

    For Models, this is always `"model"`.

### Beta Thinking Capability

- `BetaThinkingCapability`

  - `bool supported`

    Whether this capability is supported by the model.

  - `BetaThinkingTypes types`

    Supported thinking type configurations.

### Beta Thinking Types

- `BetaThinkingTypes`

  - `BetaCapabilitySupport adaptive`

    Whether the model supports thinking with type 'adaptive' (auto).

  - `BetaCapabilitySupport enabled`

    Whether the model supports thinking with type 'enabled'.

# Messages

## Create a Message

`$client->beta->messages->create(int maxTokens, list<BetaMessageParam> messages, Model model, ?BetaCacheControlEphemeral cacheControl, ?Container container, ?BetaContextManagementConfig contextManagement, ?BetaDiagnosticsParam diagnostics, ?string fallbackCreditToken, ?list<BetaFallbackParam> fallbacks, ?string inferenceGeo, ?list<BetaRequestMCPServerURLDefinition> mcpServers, ?BetaMetadata metadata, ?BetaOutputConfig outputConfig, ?BetaJSONOutputFormat outputFormat, ?ServiceTier serviceTier, ?Speed speed, ?list<string> stopSequences, ?System system, ?float temperature, ?BetaThinkingConfigParam thinking, ?BetaToolChoice toolChoice, ?list<BetaToolUnion> tools, ?int topK, ?float topP, ?list<AnthropicBeta> betas, ?string userProfileID): BetaMessage`

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

  See [input examples](https://platform.claude.com/docs/en/build-with-claude/working-with-messages).

  Note that if you want to include a [system prompt](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.

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

- `fallbackCreditToken?:optional string`

  The `fallback_credit_token` from a prior refusal's `stop_details`.

  When a preceding request was refused and returned a `fallback_credit_token`,
  pass that code here on the retry to have the retry's cache-creation tokens
  for the prefix that was warm on the refused model billed at the cache-read
  rate. Must be redeemed by the same organization and workspace, with the same
  request body (optionally extended by one appended `assistant` message whose
  content is the partial text — with any trailing whitespace stripped from
  the final text block — and paired server-tool blocks streamed before the
  refusal; the appended-assistant form is not available for requests with
  `output_format` set or forced `tool_choice`), on an eligible fallback
  model, on the same platform,
  and within 5 minutes of the refusal; a mismatch is a 400. A token minted
  mid-server-tool-loop whose partial content was continuable may only be
  redeemed with the appended-assistant form — if an exact-body retry is
  rejected with a 400 saying the token must be redeemed by continuing the
  partial response, retry with the appended-assistant form instead.

  When the appended-assistant form is used on a model that otherwise disallows
  assistant-turn prefill, this token also authorizes that one prefill.

- `fallbacks?:optional list<BetaFallbackParam>`

  Opt-in server-side retry on one or more substitute models when the requested model declines for policy reasons. Tried in order: if the first entry also declines, the second is tried, and so on.

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

  Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers) for details.

- `speed?:optional Speed`

  The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference.

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

- `thinking?:optional BetaThinkingConfigParam`

  Configuration for enabling Claude's extended thinking.

  When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

  See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

- `toolChoice?:optional BetaToolChoice`

  How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

- `tools?:optional list<BetaToolUnion>`

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

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `userProfileID?:optional string`

  The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header.

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
  fallbackCreditToken: 'x',
  fallbacks: [
    [
      'model' => 'claude-sonnet-5',
      'maxTokens' => 0,
      'outputConfig' => [
        'effort' => 'low',
        'format' => ['schema' => ['foo' => 'bar'], 'type' => 'json_schema'],
        'taskBudget' => ['total' => 1024, 'type' => 'tokens', 'remaining' => 0],
      ],
      'speed' => 'standard',
      'thinking' => [
        'budgetTokens' => 1024, 'type' => 'enabled', 'display' => 'summarized'
      ],
    ],
  ],
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
  betas: ['message-batches-2024-09-24'],
  userProfileID: 'anthropic-user-profile-id',
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
    "fallback_credit_token": "fallback_credit_token",
    "fallback_has_prefill_claim": true,
    "recommended_model": "recommended_model",
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
        "model": "claude-sonnet-5",
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

`$client->beta->messages->countTokens(list<BetaMessageParam> messages, Model model, ?BetaCacheControlEphemeral cacheControl, ?BetaContextManagementConfig contextManagement, ?list<BetaRequestMCPServerURLDefinition> mcpServers, ?BetaOutputConfig outputConfig, ?BetaJSONOutputFormat outputFormat, ?Speed speed, ?System system, ?BetaThinkingConfigParam thinking, ?BetaToolChoice toolChoice, ?list<Tool> tools, ?list<AnthropicBeta> betas, ?string userProfileID): BetaMessageTokensCount`

**post** `/v1/messages/count_tokens`

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://platform.claude.com/docs/en/build-with-claude/token-counting)

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

  See [input examples](https://platform.claude.com/docs/en/build-with-claude/working-with-messages).

  Note that if you want to include a [system prompt](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.

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

  A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

- `thinking?:optional BetaThinkingConfigParam`

  Configuration for enabling Claude's extended thinking.

  When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

  See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

- `toolChoice?:optional BetaToolChoice`

  How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

- `tools?:optional list<Tool>`

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

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `userProfileID?:optional string`

  The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header.

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
  userProfileID: 'anthropic-user-profile-id',
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

  - `?int maxTokens`

    Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor_result or advisor_redacted_result block carries stop_reason='max_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

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

    Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

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

### Beta Code Execution Tool 20260521

- `BetaCodeExecutionTool20260521`

  - `"code_execution" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"code_execution_20260521" type`

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

  - `BetaFallbackBlock`

    - `BetaFallbackInfo from`

      The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

    - `BetaFallbackInfo to`

      The fallback model producing the content that follows this block. Its `model` is always the canonical id.

    - `BetaFallbackRefusalTrigger trigger`

      What caused the `from` model to hand over at this hop.

    - `"fallback" type`

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

  - `BetaFallbackBlockParam`

    - `BetaFallbackInfoParam from`

      Identifies one hop of a fallback transition.

    - `BetaFallbackInfoParam to`

      Identifies one hop of a fallback transition.

    - `"fallback" type`

    - `?mixed trigger`

      The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.

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

### Beta Fallback Block

- `BetaFallbackBlock`

  - `BetaFallbackInfo from`

    The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

  - `BetaFallbackInfo to`

    The fallback model producing the content that follows this block. Its `model` is always the canonical id.

  - `BetaFallbackRefusalTrigger trigger`

    What caused the `from` model to hand over at this hop.

  - `"fallback" type`

### Beta Fallback Block Param

- `BetaFallbackBlockParam`

  - `BetaFallbackInfoParam from`

    Identifies one hop of a fallback transition.

  - `BetaFallbackInfoParam to`

    Identifies one hop of a fallback transition.

  - `"fallback" type`

  - `?mixed trigger`

    The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.

### Beta Fallback Info

- `BetaFallbackInfo`

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

### Beta Fallback Info Param

- `BetaFallbackInfoParam`

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

### Beta Fallback Message Iteration Usage

- `BetaFallbackMessageIterationUsage`

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

  - `"fallback_message" type`

    Usage for the fallback-model attempt that served the response

### Beta Fallback Param

- `BetaFallbackParam`

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `?int maxTokens`

  - `?BetaOutputConfig outputConfig`

  - `?Speed speed`

  - `?Thinking thinking`

### Beta Fallback Refusal Trigger

- `BetaFallbackRefusalTrigger`

  - `?Category category`

    The policy category that triggered a refusal.

  - `"refusal" type`

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

    - `Model model`

      The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

  - `BetaFallbackMessageIterationUsage`

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

    - `"fallback_message" type`

      Usage for the fallback-model attempt that served the response

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

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

    The policy category that triggered a refusal.

  - `?string explanation`

    Human-readable explanation of the refusal.

    This text is not guaranteed to be stable. `null` when no explanation is available for the category.

  - `?string fallbackCreditToken`

    Opaque code that refunds the cache-miss cost when retrying this refused
    request on the fallback model. Pass it as `fallback_credit_token` on the
    retry request. Expires 5 minutes after the refusal.

    The retry is sent either with the same request body (`system`, `messages`,
    `tools`, and other render-shaping fields), or with the same body plus one
    appended `assistant` message whose content is the partial text (with any
    trailing whitespace stripped from the final text block) and paired
    server-tool blocks from this refusal — which also authorizes that
    appended turn as an assistant-prefill continuation on models that otherwise
    disallow prefill. A token minted mid-server-tool-loop whose partial content
    was continuable may only be redeemed the second way — if a same-body retry
    is rejected with a 400 saying the token must be redeemed by continuing the
    partial response, retry the second way instead. Either way: same workspace,
    same platform; a mismatch is a 400. Resending a token for an already-warm
    prefix is permitted but yields no additional credit.

    `null` when the refused model isn't eligible for a fallback credit.

  - `?bool fallbackHasPrefillClaim`

    Whether the accompanying `fallback_credit_token` may be redeemed with the
    appended-assistant retry form. Only set when `fallback_credit_token` is
    present.

    `true`: retry by resending the same request body plus one appended
    `assistant` message whose content is this response's `content` with any
    trailing whitespace stripped from the final text block and unpaired
    `tool_use` blocks omitted (the same appended-turn shape described on
    `fallback_credit_token`), with the token attached. `false`: retry by
    resending the original request body unchanged, with the token attached —
    the appended-assistant form is not available for this refusal (no
    continuable partial content, or the request uses `output_format` or a
    `tool_choice` that forces tool use). One exception: when the request used
    `output_format` or a forced `tool_choice` and the refusal arrived after
    server tools (including MCP connector tools) had already executed, the
    token may not be redeemable by either retry form; if the exact-body retry
    is then rejected with a 400 saying the token must be redeemed by
    continuing the partial response, discard the token and retry without it.

    Advisory: if an appended-assistant retry is rejected with a 400 despite
    `true`, fall back to resending the original request body with the token.

  - `?string recommendedModel`

    The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

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

    See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

  - `"enabled" type`

  - `?Display display`

    Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

### Beta Thinking Config Param

- `BetaThinkingConfigParam`

  - `BetaThinkingConfigEnabled`

    - `int budgetTokens`

      Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

      Must be ≥1024 and less than `max_tokens`.

      See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

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

  - `?string errorMessage`

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

  - `BetaCodeExecutionTool20260521`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"code_execution_20260521" type`

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

  - `BetaWebSearchTool20260318`

    - `"web_search" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"web_search_20260318" type`

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

    - `?ResponseInclusion responseInclusion`

      How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?BetaUserLocation userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `BetaWebFetchTool20260318`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `"web_fetch_20260318" type`

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

    - `?ResponseInclusion responseInclusion`

      How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

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

    - `?int maxTokens`

      Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor_result or advisor_redacted_result block carries stop_reason='max_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

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

### Beta Web Fetch Tool 20260318

- `BetaWebFetchTool20260318`

  - `"web_fetch" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"web_fetch_20260318" type`

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

  - `?ResponseInclusion responseInclusion`

    How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

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

### Beta Web Search Tool 20260318

- `BetaWebSearchTool20260318`

  - `"web_search" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `"web_search_20260318" type`

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

  - `?ResponseInclusion responseInclusion`

    How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

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

`$client->beta->messages->batches->create(list<Request> requests, ?list<AnthropicBeta> betas, ?string userProfileID): MessageBatch`

**post** `/v1/messages/batches`

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

### Parameters

- `requests: list<Request>`

  List of requests for prompt completion. Each is an individual request to create a Message.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

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
        'fallbackCreditToken' => 'x',
        'fallbacks' => [
          [
            'model' => 'claude-sonnet-5',
            'maxTokens' => 0,
            'outputConfig' => [
              'effort' => 'low',
              'format' => [
                'schema' => ['foo' => 'bar'], 'type' => 'json_schema'
              ],
              'taskBudget' => [
                'total' => 1024, 'type' => 'tokens', 'remaining' => 0
              ],
            ],
            'speed' => 'standard',
            'thinking' => [
              'budgetTokens' => 1024,
              'type' => 'enabled',
              'display' => 'summarized',
            ],
          ],
        ],
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
  betas: ['message-batches-2024-09-24'],
  userProfileID: 'anthropic-user-profile-id',
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

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

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

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

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

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

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

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

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

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

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

# Agents

## Create Agent

`$client->beta->agents->create(Model model, string name, ?string description, ?list<BetaManagedAgentsURLMCPServerParams> mcpServers, ?array<string,string> metadata, ?BetaManagedAgentsMultiagentParams multiagent, ?list<BetaManagedAgentsSkillParams> skills, ?string system, ?list<Tool> tools, ?list<AnthropicBeta> betas): BetaManagedAgentsAgent`

**post** `/v1/agents`

Create Agent

### Parameters

- `model: Model`

  Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-4-6`, or a `model_config` object for additional configuration control

- `name: string`

  Human-readable name for the agent.

- `description?:optional string`

  Description of what the agent does.

- `mcpServers?:optional list<BetaManagedAgentsURLMCPServerParams>`

  MCP servers this agent connects to. Maximum 20. Names must be unique within the array. Every server must be referenced by an `mcp_toolset` in `tools`; unreferenced servers are rejected. See the [MCP connector guide](https://platform.claude.com/docs/en/managed-agents/mcp-connector).

- `metadata?:optional array<string,string>`

  Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `multiagent?:optional BetaManagedAgentsMultiagentParams`

  A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

- `skills?:optional list<BetaManagedAgentsSkillParams>`

  Skills available to the agent.

- `system?:optional string`

  System prompt for the agent.

- `tools?:optional list<Tool>`

  Tool configurations available to the agent. Maximum of 128 tools across all toolsets allowed.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsAgent`

  - `string id`

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?string description`

  - `list<BetaManagedAgentsMCPServerURLDefinition> mcpServers`

  - `array<string,string> metadata`

  - `BetaManagedAgentsModelConfig model`

    Model identifier and configuration.

  - `?BetaManagedAgentsMultiagent multiagent`

    Resolved coordinator topology with a concrete agent roster.

  - `string name`

  - `list<Skill> skills`

  - `?string system`

  - `list<Tool> tools`

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `int version`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsAgent = $client->beta->agents->create(
  model: 'claude-sonnet-4-6',
  name: 'My First Agent',
  description: 'A general-purpose starter agent.',
  mcpServers: [
    [
      'name' => 'example-mcp',
      'type' => 'url',
      'url' => 'https://example-server.modelcontextprotocol.io/sse',
    ],
  ],
  metadata: ['foo' => 'bar'],
  multiagent: [
    'agents' => ['agent_011CZkYqphY8vELVzwCUpqiQ', ['type' => 'self']],
    'type' => 'coordinator',
  ],
  skills: [['skillID' => 'xlsx', 'type' => 'anthropic', 'version' => '1']],
  system: 'You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user\'s task end to end.',
  tools: [
    [
      'type' => 'agent_toolset_20260401',
      'configs' => [
        [
          'name' => 'bash',
          'enabled' => true,
          'permissionPolicy' => ['type' => 'always_allow'],
        ],
      ],
      'defaultConfig' => [
        'enabled' => true, 'permissionPolicy' => ['type' => 'always_allow']
      ],
    ],
  ],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsAgent);
```

#### Response

```json
{
  "id": "agent_011CZkYpogX7uDKUyvBTophP",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "A general-purpose starter agent.",
  "mcp_servers": [
    {
      "name": "example-mcp",
      "type": "url",
      "url": "https://example-server.modelcontextprotocol.io/sse"
    }
  ],
  "metadata": {
    "foo": "bar"
  },
  "model": {
    "id": "claude-sonnet-4-6",
    "speed": "standard"
  },
  "multiagent": {
    "agents": [
      {
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
        "type": "agent",
        "version": 1
      }
    ],
    "type": "coordinator"
  },
  "name": "My First Agent",
  "skills": [
    {
      "skill_id": "xlsx",
      "type": "anthropic",
      "version": "1"
    },
    {
      "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
      "type": "custom",
      "version": "2"
    }
  ],
  "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
  "tools": [
    {
      "configs": [
        {
          "enabled": true,
          "name": "bash",
          "permission_policy": {
            "type": "always_allow"
          }
        }
      ],
      "default_config": {
        "enabled": true,
        "permission_policy": {
          "type": "always_ask"
        }
      },
      "type": "agent_toolset_20260401"
    }
  ],
  "type": "agent",
  "updated_at": "2026-03-15T10:00:00Z",
  "version": 1
}
```

## List Agents

`$client->beta->agents->list(?\Datetime createdAtGte, ?\Datetime createdAtLte, ?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<BetaManagedAgentsAgent>`

**get** `/v1/agents`

List Agents

### Parameters

- `createdAtGte?:optional \Datetime`

  Return agents created at or after this time (inclusive).

- `createdAtLte?:optional \Datetime`

  Return agents created at or before this time (inclusive).

- `includeArchived?:optional bool`

  Include archived agents in results. Defaults to false.

- `limit?:optional int`

  Maximum results per page. Default 20, maximum 100.

- `page?:optional string`

  Opaque pagination cursor from a previous response.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsAgent`

  - `string id`

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?string description`

  - `list<BetaManagedAgentsMCPServerURLDefinition> mcpServers`

  - `array<string,string> metadata`

  - `BetaManagedAgentsModelConfig model`

    Model identifier and configuration.

  - `?BetaManagedAgentsMultiagent multiagent`

    Resolved coordinator topology with a concrete agent roster.

  - `string name`

  - `list<Skill> skills`

  - `?string system`

  - `list<Tool> tools`

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `int version`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->agents->list(
  createdAtGte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  includeArchived: true,
  limit: 0,
  page: 'page',
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

#### Response

```json
{
  "data": [
    {
      "id": "agent_011CZkYpogX7uDKUyvBTophP",
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "description": "A general-purpose starter agent.",
      "mcp_servers": [
        {
          "name": "example-mcp",
          "type": "url",
          "url": "https://example-server.modelcontextprotocol.io/sse"
        }
      ],
      "metadata": {
        "foo": "bar"
      },
      "model": {
        "id": "claude-sonnet-4-6",
        "speed": "standard"
      },
      "multiagent": {
        "agents": [
          {
            "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
            "type": "agent",
            "version": 1
          }
        ],
        "type": "coordinator"
      },
      "name": "My First Agent",
      "skills": [
        {
          "skill_id": "xlsx",
          "type": "anthropic",
          "version": "1"
        },
        {
          "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
          "type": "custom",
          "version": "2"
        }
      ],
      "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
      "tools": [
        {
          "configs": [
            {
              "enabled": true,
              "name": "bash",
              "permission_policy": {
                "type": "always_allow"
              }
            }
          ],
          "default_config": {
            "enabled": true,
            "permission_policy": {
              "type": "always_ask"
            }
          },
          "type": "agent_toolset_20260401"
        }
      ],
      "type": "agent",
      "updated_at": "2026-03-15T10:00:00Z",
      "version": 1
    }
  ],
  "next_page": "next_page"
}
```

## Get Agent

`$client->beta->agents->retrieve(string agentID, ?int version, ?list<AnthropicBeta> betas): BetaManagedAgentsAgent`

**get** `/v1/agents/{agent_id}`

Get Agent

### Parameters

- `agentID: string`

- `version?:optional int`

  Agent version. Omit for the most recent version. Must be at least 1 if specified.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsAgent`

  - `string id`

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?string description`

  - `list<BetaManagedAgentsMCPServerURLDefinition> mcpServers`

  - `array<string,string> metadata`

  - `BetaManagedAgentsModelConfig model`

    Model identifier and configuration.

  - `?BetaManagedAgentsMultiagent multiagent`

    Resolved coordinator topology with a concrete agent roster.

  - `string name`

  - `list<Skill> skills`

  - `?string system`

  - `list<Tool> tools`

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `int version`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsAgent = $client->beta->agents->retrieve(
  'agent_011CZkYpogX7uDKUyvBTophP',
  version: 0,
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsAgent);
```

#### Response

```json
{
  "id": "agent_011CZkYpogX7uDKUyvBTophP",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "A general-purpose starter agent.",
  "mcp_servers": [
    {
      "name": "example-mcp",
      "type": "url",
      "url": "https://example-server.modelcontextprotocol.io/sse"
    }
  ],
  "metadata": {
    "foo": "bar"
  },
  "model": {
    "id": "claude-sonnet-4-6",
    "speed": "standard"
  },
  "multiagent": {
    "agents": [
      {
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
        "type": "agent",
        "version": 1
      }
    ],
    "type": "coordinator"
  },
  "name": "My First Agent",
  "skills": [
    {
      "skill_id": "xlsx",
      "type": "anthropic",
      "version": "1"
    },
    {
      "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
      "type": "custom",
      "version": "2"
    }
  ],
  "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
  "tools": [
    {
      "configs": [
        {
          "enabled": true,
          "name": "bash",
          "permission_policy": {
            "type": "always_allow"
          }
        }
      ],
      "default_config": {
        "enabled": true,
        "permission_policy": {
          "type": "always_ask"
        }
      },
      "type": "agent_toolset_20260401"
    }
  ],
  "type": "agent",
  "updated_at": "2026-03-15T10:00:00Z",
  "version": 1
}
```

## Update Agent

`$client->beta->agents->update(string agentID, int version, ?string description, ?list<BetaManagedAgentsURLMCPServerParams> mcpServers, ?array<string,string> metadata, ?Model model, ?BetaManagedAgentsMultiagentParams multiagent, ?string name, ?list<BetaManagedAgentsSkillParams> skills, ?string system, ?list<Tool> tools, ?list<AnthropicBeta> betas): BetaManagedAgentsAgent`

**post** `/v1/agents/{agent_id}`

Update Agent

### Parameters

- `agentID: string`

- `version: int`

  The agent's current version, used to prevent concurrent overwrites. Obtain this value from a create or retrieve response. The request fails if this does not match the server's current version.

- `description?:optional string`

  Description. Omit to preserve; send empty string or null to clear.

- `mcpServers?:optional list<BetaManagedAgentsURLMCPServerParams>`

  MCP servers. Full replacement. Omit to preserve; send empty array or `null` to clear. Names must be unique. Maximum 20. Every server must be referenced by an `mcp_toolset` in the agent's resulting `tools`; unreferenced servers are rejected. See the [MCP connector guide](https://platform.claude.com/docs/en/managed-agents/mcp-connector).

- `metadata?:optional array<string,string>`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `model?:optional Model`

  Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-4-6`, or a `model_config` object for additional configuration control. Omit to preserve. Cannot be cleared.

- `multiagent?:optional BetaManagedAgentsMultiagentParams`

  A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

- `name?:optional string`

  Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

- `skills?:optional list<BetaManagedAgentsSkillParams>`

  Skills. Full replacement. Omit to preserve; send empty array or null to clear.

- `system?:optional string`

  System prompt. Omit to preserve; send empty string or null to clear.

- `tools?:optional list<Tool>`

  Tool configurations available to the agent. Full replacement. Omit to preserve; send empty array or null to clear. Maximum of 128 tools across all toolsets allowed.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsAgent`

  - `string id`

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?string description`

  - `list<BetaManagedAgentsMCPServerURLDefinition> mcpServers`

  - `array<string,string> metadata`

  - `BetaManagedAgentsModelConfig model`

    Model identifier and configuration.

  - `?BetaManagedAgentsMultiagent multiagent`

    Resolved coordinator topology with a concrete agent roster.

  - `string name`

  - `list<Skill> skills`

  - `?string system`

  - `list<Tool> tools`

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `int version`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsAgent = $client->beta->agents->update(
  'agent_011CZkYpogX7uDKUyvBTophP',
  version: 1,
  description: 'description',
  mcpServers: [
    [
      'name' => 'example-mcp',
      'type' => 'url',
      'url' => 'https://example-server.modelcontextprotocol.io/sse',
    ],
  ],
  metadata: ['foo' => 'string'],
  model: ['id' => 'claude-opus-4-6', 'speed' => 'standard'],
  multiagent: [
    'agents' => ['agent_011CZkYqphY8vELVzwCUpqiQ', ['type' => 'self']],
    'type' => 'coordinator',
  ],
  name: 'name',
  skills: [['skillID' => 'xlsx', 'type' => 'anthropic', 'version' => '1']],
  system: 'You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user\'s task end to end.',
  tools: [
    [
      'type' => 'agent_toolset_20260401',
      'configs' => [
        [
          'name' => 'bash',
          'enabled' => true,
          'permissionPolicy' => ['type' => 'always_allow'],
        ],
      ],
      'defaultConfig' => [
        'enabled' => true, 'permissionPolicy' => ['type' => 'always_allow']
      ],
    ],
  ],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsAgent);
```

#### Response

```json
{
  "id": "agent_011CZkYpogX7uDKUyvBTophP",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "A general-purpose starter agent.",
  "mcp_servers": [
    {
      "name": "example-mcp",
      "type": "url",
      "url": "https://example-server.modelcontextprotocol.io/sse"
    }
  ],
  "metadata": {
    "foo": "bar"
  },
  "model": {
    "id": "claude-sonnet-4-6",
    "speed": "standard"
  },
  "multiagent": {
    "agents": [
      {
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
        "type": "agent",
        "version": 1
      }
    ],
    "type": "coordinator"
  },
  "name": "My First Agent",
  "skills": [
    {
      "skill_id": "xlsx",
      "type": "anthropic",
      "version": "1"
    },
    {
      "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
      "type": "custom",
      "version": "2"
    }
  ],
  "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
  "tools": [
    {
      "configs": [
        {
          "enabled": true,
          "name": "bash",
          "permission_policy": {
            "type": "always_allow"
          }
        }
      ],
      "default_config": {
        "enabled": true,
        "permission_policy": {
          "type": "always_ask"
        }
      },
      "type": "agent_toolset_20260401"
    }
  ],
  "type": "agent",
  "updated_at": "2026-03-15T10:00:00Z",
  "version": 1
}
```

## Archive Agent

`$client->beta->agents->archive(string agentID, ?list<AnthropicBeta> betas): BetaManagedAgentsAgent`

**post** `/v1/agents/{agent_id}/archive`

Archive Agent

### Parameters

- `agentID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsAgent`

  - `string id`

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?string description`

  - `list<BetaManagedAgentsMCPServerURLDefinition> mcpServers`

  - `array<string,string> metadata`

  - `BetaManagedAgentsModelConfig model`

    Model identifier and configuration.

  - `?BetaManagedAgentsMultiagent multiagent`

    Resolved coordinator topology with a concrete agent roster.

  - `string name`

  - `list<Skill> skills`

  - `?string system`

  - `list<Tool> tools`

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `int version`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsAgent = $client->beta->agents->archive(
  'agent_011CZkYpogX7uDKUyvBTophP', betas: ['message-batches-2024-09-24']
);

var_dump($betaManagedAgentsAgent);
```

#### Response

```json
{
  "id": "agent_011CZkYpogX7uDKUyvBTophP",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "A general-purpose starter agent.",
  "mcp_servers": [
    {
      "name": "example-mcp",
      "type": "url",
      "url": "https://example-server.modelcontextprotocol.io/sse"
    }
  ],
  "metadata": {
    "foo": "bar"
  },
  "model": {
    "id": "claude-sonnet-4-6",
    "speed": "standard"
  },
  "multiagent": {
    "agents": [
      {
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
        "type": "agent",
        "version": 1
      }
    ],
    "type": "coordinator"
  },
  "name": "My First Agent",
  "skills": [
    {
      "skill_id": "xlsx",
      "type": "anthropic",
      "version": "1"
    },
    {
      "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
      "type": "custom",
      "version": "2"
    }
  ],
  "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
  "tools": [
    {
      "configs": [
        {
          "enabled": true,
          "name": "bash",
          "permission_policy": {
            "type": "always_allow"
          }
        }
      ],
      "default_config": {
        "enabled": true,
        "permission_policy": {
          "type": "always_ask"
        }
      },
      "type": "agent_toolset_20260401"
    }
  ],
  "type": "agent",
  "updated_at": "2026-03-15T10:00:00Z",
  "version": 1
}
```

## Domain Types

### Beta Managed Agents Agent

- `BetaManagedAgentsAgent`

  - `string id`

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?string description`

  - `list<BetaManagedAgentsMCPServerURLDefinition> mcpServers`

  - `array<string,string> metadata`

  - `BetaManagedAgentsModelConfig model`

    Model identifier and configuration.

  - `?BetaManagedAgentsMultiagent multiagent`

    Resolved coordinator topology with a concrete agent roster.

  - `string name`

  - `list<Skill> skills`

  - `?string system`

  - `list<Tool> tools`

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `int version`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Beta Managed Agents Agent Reference

- `BetaManagedAgentsAgentReference`

  - `string id`

  - `Type type`

  - `int version`

### Beta Managed Agents Agent Tool Config

- `BetaManagedAgentsAgentToolConfig`

  - `bool enabled`

  - `Name name`

    Built-in agent tool identifier.

  - `PermissionPolicy permissionPolicy`

    Permission policy for tool execution.

### Beta Managed Agents Agent Tool Config Params

- `BetaManagedAgentsAgentToolConfigParams`

  - `Name name`

    Built-in agent tool identifier.

  - `?bool enabled`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `?PermissionPolicy permissionPolicy`

    Permission policy for tool execution.

### Beta Managed Agents Agent Toolset Default Config

- `BetaManagedAgentsAgentToolsetDefaultConfig`

  - `bool enabled`

  - `PermissionPolicy permissionPolicy`

    Permission policy for tool execution.

### Beta Managed Agents Agent Toolset Default Config Params

- `BetaManagedAgentsAgentToolsetDefaultConfigParams`

  - `?bool enabled`

    Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

  - `?PermissionPolicy permissionPolicy`

    Permission policy for tool execution.

### Beta Managed Agents Agent Toolset20260401

- `BetaManagedAgentsAgentToolset20260401`

  - `list<BetaManagedAgentsAgentToolConfig> configs`

  - `BetaManagedAgentsAgentToolsetDefaultConfig defaultConfig`

    Resolved default configuration for agent tools.

  - `Type type`

### Beta Managed Agents Agent Toolset20260401 Bash Input

- `BetaManagedAgentsAgentToolset20260401BashInput`

  - `?string command`

    Shell command to execute. Omit only when `restart` is true.

  - `?bool restart`

    When true, restart the persistent bash session instead of
    running a command. Subsequent calls without `restart` will
    run against the fresh session.

  - `?int timeoutMs`

    Per-call timeout in milliseconds. Defaults to the
    runner-wide tool timeout when omitted or zero.

### Beta Managed Agents Agent Toolset20260401 Edit Input

- `BetaManagedAgentsAgentToolset20260401EditInput`

  - `string filePath`

    Path of the file to edit.

  - `string newString`

    Replacement text.

  - `string oldString`

    Substring to find and replace.

  - `?bool replaceAll`

    When true, replace every occurrence of `old_string`
    instead of requiring a unique match.

### Beta Managed Agents Agent Toolset20260401 Glob Input

- `BetaManagedAgentsAgentToolset20260401GlobInput`

  - `string pattern`

    Doublestar glob pattern (e.g. `**/*.go`). Absolute patterns
    are only permitted when the runner is configured to allow
    them.

  - `?string path`

    Optional directory root to search under. Defaults to the
    runner's working directory.

### Beta Managed Agents Agent Toolset20260401 Grep Input

- `BetaManagedAgentsAgentToolset20260401GrepInput`

  - `string pattern`

    Regular expression to search for.

  - `?string path`

    Optional directory root to search under. Defaults to the
    runner's working directory.

### Beta Managed Agents Agent Toolset20260401 Params

- `BetaManagedAgentsAgentToolset20260401Params`

  - `Type type`

  - `?list<BetaManagedAgentsAgentToolConfigParams> configs`

    Per-tool configuration overrides.

  - `?BetaManagedAgentsAgentToolsetDefaultConfigParams defaultConfig`

    Default configuration for all tools in a toolset.

### Beta Managed Agents Agent Toolset20260401 Read Input

- `BetaManagedAgentsAgentToolset20260401ReadInput`

  - `string filePath`

    Path of the file to read.

  - `?list<int> viewRange`

    Optional `[start_line, end_line]` 1-indexed inclusive
    range. When omitted the entire file is returned.
    `end_line` of 0 or negative means "to end of file".

### Beta Managed Agents Agent Toolset20260401 Write Input

- `BetaManagedAgentsAgentToolset20260401WriteInput`

  - `string content`

    Full file contents to write.

  - `string filePath`

    Path of the file to write.

### Beta Managed Agents Always Allow Policy

- `BetaManagedAgentsAlwaysAllowPolicy`

  - `Type type`

### Beta Managed Agents Always Ask Policy

- `BetaManagedAgentsAlwaysAskPolicy`

  - `Type type`

### Beta Managed Agents Anthropic Skill

- `BetaManagedAgentsAnthropicSkill`

  - `string skillID`

  - `Type type`

  - `string version`

### Beta Managed Agents Anthropic Skill Params

- `BetaManagedAgentsAnthropicSkillParams`

  - `string skillID`

    Identifier of the Anthropic skill (e.g., "xlsx").

  - `Type type`

  - `?string version`

    Version to pin. Defaults to latest if omitted.

### Beta Managed Agents Custom Skill

- `BetaManagedAgentsCustomSkill`

  - `string skillID`

  - `Type type`

  - `string version`

### Beta Managed Agents Custom Skill Params

- `BetaManagedAgentsCustomSkillParams`

  - `string skillID`

    Tagged ID of the custom skill (e.g., "skill_01XJ5...").

  - `Type type`

  - `?string version`

    Version to pin. Defaults to latest if omitted.

### Beta Managed Agents Custom Tool

- `BetaManagedAgentsCustomTool`

  - `string description`

  - `BetaManagedAgentsCustomToolInputSchema inputSchema`

    JSON Schema for custom tool input parameters.

  - `string name`

  - `Type type`

### Beta Managed Agents Custom Tool Input Schema

- `BetaManagedAgentsCustomToolInputSchema`

  - `"object" type`

  - `?array<string,mixed> properties`

  - `?list<string> required`

### Beta Managed Agents Custom Tool Params

- `BetaManagedAgentsCustomToolParams`

  - `string description`

    Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-4096 characters.

  - `BetaManagedAgentsCustomToolInputSchema inputSchema`

    JSON Schema for custom tool input parameters.

  - `string name`

    Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

  - `Type type`

### Beta Managed Agents MCP Server URL Definition

- `BetaManagedAgentsMCPServerURLDefinition`

  - `string name`

  - `Type type`

  - `string url`

### Beta Managed Agents MCP Tool Config

- `BetaManagedAgentsMCPToolConfig`

  - `bool enabled`

  - `string name`

  - `PermissionPolicy permissionPolicy`

    Permission policy for tool execution.

### Beta Managed Agents MCP Tool Config Params

- `BetaManagedAgentsMCPToolConfigParams`

  - `string name`

    Name of the MCP tool to configure. 1-128 characters.

  - `?bool enabled`

    Whether this tool is enabled. Overrides the `default_config` setting.

  - `?PermissionPolicy permissionPolicy`

    Permission policy for tool execution.

### Beta Managed Agents MCP Toolset

- `BetaManagedAgentsMCPToolset`

  - `list<BetaManagedAgentsMCPToolConfig> configs`

  - `BetaManagedAgentsMCPToolsetDefaultConfig defaultConfig`

    Resolved default configuration for all tools from an MCP server.

  - `string mcpServerName`

  - `Type type`

### Beta Managed Agents MCP Toolset Default Config

- `BetaManagedAgentsMCPToolsetDefaultConfig`

  - `bool enabled`

  - `PermissionPolicy permissionPolicy`

    Permission policy for tool execution.

### Beta Managed Agents MCP Toolset Default Config Params

- `BetaManagedAgentsMCPToolsetDefaultConfigParams`

  - `?bool enabled`

    Whether tools are enabled by default. Defaults to true if not specified.

  - `?PermissionPolicy permissionPolicy`

    Permission policy for tool execution.

### Beta Managed Agents MCP Toolset Params

- `BetaManagedAgentsMCPToolsetParams`

  - `string mcpServerName`

    Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

  - `Type type`

  - `?list<BetaManagedAgentsMCPToolConfigParams> configs`

    Per-tool configuration overrides.

  - `?BetaManagedAgentsMCPToolsetDefaultConfigParams defaultConfig`

    Default configuration for all tools from an MCP server.

### Beta Managed Agents Model

- `BetaManagedAgentsModel`

  - `"claude-sonnet-5"`

    High-performance model for coding and agents

  - `"claude-fable-5"`

    Next generation of intelligence for the hardest knowledge work and coding problems

  - `"claude-opus-4-8"`

    Frontier intelligence for long-running agents and coding

  - `"claude-opus-4-7"`

    Frontier intelligence for long-running agents and coding

  - `"claude-opus-4-6"`

    Most intelligent model for building agents and coding

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

### Beta Managed Agents Model Config

- `BetaManagedAgentsModelConfig`

  - `BetaManagedAgentsModel id`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `?Speed speed`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

### Beta Managed Agents Model Config Params

- `BetaManagedAgentsModelConfigParams`

  - `BetaManagedAgentsModel id`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `?Speed speed`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

### Beta Managed Agents Multiagent Coordinator

- `BetaManagedAgentsMultiagentCoordinator`

  - `list<BetaManagedAgentsAgentReference> agents`

    Agents the coordinator may spawn as session threads, each resolved to a specific version.

  - `Type type`

### Beta Managed Agents Multiagent Coordinator Params

- `BetaManagedAgentsMultiagentCoordinatorParams`

  - `list<BetaManagedAgentsMultiagentRosterEntryParams> agents`

    Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

  - `Type type`

### Beta Managed Agents Multiagent Self Params

- `BetaManagedAgentsMultiagentSelfParams`

  - `Type type`

### Beta Managed Agents Session Thread Agent

- `BetaManagedAgentsSessionThreadAgent`

  - `string id`

  - `?string description`

  - `list<BetaManagedAgentsMCPServerURLDefinition> mcpServers`

  - `BetaManagedAgentsModelConfig model`

    Model identifier and configuration.

  - `string name`

  - `list<Skill> skills`

  - `?string system`

  - `list<Tool> tools`

  - `Type type`

  - `int version`

### Beta Managed Agents Skill Params

- `BetaManagedAgentsSkillParams`

  - `BetaManagedAgentsAnthropicSkillParams`

    - `string skillID`

      Identifier of the Anthropic skill (e.g., "xlsx").

    - `Type type`

    - `?string version`

      Version to pin. Defaults to latest if omitted.

  - `BetaManagedAgentsCustomSkillParams`

    - `string skillID`

      Tagged ID of the custom skill (e.g., "skill_01XJ5...").

    - `Type type`

    - `?string version`

      Version to pin. Defaults to latest if omitted.

### Beta Managed Agents URL MCP Server Params

- `BetaManagedAgentsURLMCPServerParams`

  - `string name`

    Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

  - `Type type`

  - `string url`

    Endpoint URL for the MCP server.

# Versions

## List Agent Versions

`$client->beta->agents->versions->list(string agentID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<BetaManagedAgentsAgent>`

**get** `/v1/agents/{agent_id}/versions`

List Agent Versions

### Parameters

- `agentID: string`

- `limit?:optional int`

  Maximum results per page. Default 20, maximum 100.

- `page?:optional string`

  Opaque pagination cursor.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsAgent`

  - `string id`

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?string description`

  - `list<BetaManagedAgentsMCPServerURLDefinition> mcpServers`

  - `array<string,string> metadata`

  - `BetaManagedAgentsModelConfig model`

    Model identifier and configuration.

  - `?BetaManagedAgentsMultiagent multiagent`

    Resolved coordinator topology with a concrete agent roster.

  - `string name`

  - `list<Skill> skills`

  - `?string system`

  - `list<Tool> tools`

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `int version`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->agents->versions->list(
  'agent_011CZkYpogX7uDKUyvBTophP',
  limit: 0,
  page: 'page',
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

#### Response

```json
{
  "data": [
    {
      "id": "agent_011CZkYpogX7uDKUyvBTophP",
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "description": "A general-purpose starter agent.",
      "mcp_servers": [
        {
          "name": "example-mcp",
          "type": "url",
          "url": "https://example-server.modelcontextprotocol.io/sse"
        }
      ],
      "metadata": {
        "foo": "bar"
      },
      "model": {
        "id": "claude-sonnet-4-6",
        "speed": "standard"
      },
      "multiagent": {
        "agents": [
          {
            "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
            "type": "agent",
            "version": 1
          }
        ],
        "type": "coordinator"
      },
      "name": "My First Agent",
      "skills": [
        {
          "skill_id": "xlsx",
          "type": "anthropic",
          "version": "1"
        },
        {
          "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
          "type": "custom",
          "version": "2"
        }
      ],
      "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
      "tools": [
        {
          "configs": [
            {
              "enabled": true,
              "name": "bash",
              "permission_policy": {
                "type": "always_allow"
              }
            }
          ],
          "default_config": {
            "enabled": true,
            "permission_policy": {
              "type": "always_ask"
            }
          },
          "type": "agent_toolset_20260401"
        }
      ],
      "type": "agent",
      "updated_at": "2026-03-15T10:00:00Z",
      "version": 1
    }
  ],
  "next_page": "next_page"
}
```

# Environments

## Create Environment

`$client->beta->environments->create(string name, ?Config config, ?string description, ?array<string,string> metadata, ?Scope scope, ?list<AnthropicBeta> betas): BetaEnvironment`

**post** `/v1/environments`

Create a new environment with the specified configuration.

### Parameters

- `name: string`

  Human-readable name for the environment

- `config?:optional Config`

  Environment configuration

- `description?:optional string`

  Optional description of the environment

- `metadata?:optional array<string,string>`

  User-provided metadata key-value pairs

- `scope?:optional Scope`

  The visibility scope for this environment. 'organization' makes the environment visible to all accounts. 'account' restricts visibility to the owning account only. Only applicable for self-hosted environments. If not specified, defaults based on organization type.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaEnvironment`

  - `string id`

    Environment identifier (e.g., 'env_...')

  - `?string archivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config config`

    Environment configuration (either Anthropic Cloud or self-hosted)

  - `string createdAt`

    RFC 3339 timestamp when environment was created

  - `string description`

    User-provided description for the environment

  - `array<string,string> metadata`

    User-provided metadata key-value pairs

  - `string name`

    Human-readable name for the environment

  - `"environment" type`

    The type of object (always 'environment')

  - `string updatedAt`

    RFC 3339 timestamp when environment was last updated

  - `?Scope scope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaEnvironment = $client->beta->environments->create(
  name: 'python-data-analysis',
  config: [
    'type' => 'cloud',
    'networking' => [
      'type' => 'limited',
      'allowMCPServers' => true,
      'allowPackageManagers' => true,
      'allowedHosts' => ['api.example.com'],
    ],
    'packages' => [
      'apt' => ['string'],
      'cargo' => ['string'],
      'gem' => ['string'],
      'go' => ['string'],
      'npm' => ['string'],
      'pip' => ['pandas', 'numpy'],
      'type' => 'packages',
    ],
  ],
  description: 'Python environment with data-analysis packages.',
  metadata: ['foo' => 'string'],
  scope: 'organization',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaEnvironment);
```

#### Response

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```

## List Environments

`$client->beta->environments->list(?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<BetaEnvironment>`

**get** `/v1/environments`

List environments with pagination support.

### Parameters

- `includeArchived?:optional bool`

  Include archived environments in the response

- `limit?:optional int`

  Maximum number of environments to return

- `page?:optional string`

  Opaque cursor from previous response for pagination. Pass the `next_page` value from the previous response.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaEnvironment`

  - `string id`

    Environment identifier (e.g., 'env_...')

  - `?string archivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config config`

    Environment configuration (either Anthropic Cloud or self-hosted)

  - `string createdAt`

    RFC 3339 timestamp when environment was created

  - `string description`

    User-provided description for the environment

  - `array<string,string> metadata`

    User-provided metadata key-value pairs

  - `string name`

    Human-readable name for the environment

  - `"environment" type`

    The type of object (always 'environment')

  - `string updatedAt`

    RFC 3339 timestamp when environment was last updated

  - `?Scope scope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->environments->list(
  includeArchived: true,
  limit: 1,
  page: 'page',
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

#### Response

```json
{
  "data": [
    {
      "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
      "archived_at": null,
      "config": {
        "networking": {
          "allow_mcp_servers": false,
          "allow_package_managers": true,
          "allowed_hosts": [
            "api.example.com"
          ],
          "type": "limited"
        },
        "packages": {
          "apt": [
            "string"
          ],
          "cargo": [
            "string"
          ],
          "gem": [
            "string"
          ],
          "go": [
            "string"
          ],
          "npm": [
            "string"
          ],
          "pip": [
            "pandas",
            "numpy"
          ],
          "type": "packages"
        },
        "type": "cloud"
      },
      "created_at": "2026-03-15T10:00:00Z",
      "description": "Python environment with data-analysis packages.",
      "metadata": {},
      "name": "python-data-analysis",
      "type": "environment",
      "updated_at": "2026-03-15T10:00:00Z",
      "scope": "organization"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Environment

`$client->beta->environments->retrieve(string environmentID, ?list<AnthropicBeta> betas): BetaEnvironment`

**get** `/v1/environments/{environment_id}`

Retrieve a specific environment by ID.

### Parameters

- `environmentID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaEnvironment`

  - `string id`

    Environment identifier (e.g., 'env_...')

  - `?string archivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config config`

    Environment configuration (either Anthropic Cloud or self-hosted)

  - `string createdAt`

    RFC 3339 timestamp when environment was created

  - `string description`

    User-provided description for the environment

  - `array<string,string> metadata`

    User-provided metadata key-value pairs

  - `string name`

    Human-readable name for the environment

  - `"environment" type`

    The type of object (always 'environment')

  - `string updatedAt`

    RFC 3339 timestamp when environment was last updated

  - `?Scope scope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaEnvironment = $client->beta->environments->retrieve(
  'env_011CZkZ9X2dpNyB7HsEFoRfW', betas: ['message-batches-2024-09-24']
);

var_dump($betaEnvironment);
```

#### Response

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```

## Update Environment

`$client->beta->environments->update(string environmentID, ?Config config, ?string description, ?array<string,string> metadata, ?string name, ?Scope scope, ?list<AnthropicBeta> betas): BetaEnvironment`

**post** `/v1/environments/{environment_id}`

Update an existing environment's configuration.

### Parameters

- `environmentID: string`

- `config?:optional Config`

  Updated environment configuration

- `description?:optional string`

  Updated description of the environment

- `metadata?:optional array<string,string>`

  User-provided metadata key-value pairs. Set a value to null or empty string to delete the key.

- `name?:optional string`

  Updated name for the environment

- `scope?:optional Scope`

  The visibility scope for this environment. 'organization' makes the environment visible to all accounts. 'account' restricts visibility to the owning account only.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaEnvironment`

  - `string id`

    Environment identifier (e.g., 'env_...')

  - `?string archivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config config`

    Environment configuration (either Anthropic Cloud or self-hosted)

  - `string createdAt`

    RFC 3339 timestamp when environment was created

  - `string description`

    User-provided description for the environment

  - `array<string,string> metadata`

    User-provided metadata key-value pairs

  - `string name`

    Human-readable name for the environment

  - `"environment" type`

    The type of object (always 'environment')

  - `string updatedAt`

    RFC 3339 timestamp when environment was last updated

  - `?Scope scope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaEnvironment = $client->beta->environments->update(
  'env_011CZkZ9X2dpNyB7HsEFoRfW',
  config: [
    'type' => 'cloud',
    'networking' => [
      'type' => 'limited',
      'allowMCPServers' => true,
      'allowPackageManagers' => true,
      'allowedHosts' => ['api.example.com'],
    ],
    'packages' => [
      'apt' => ['string'],
      'cargo' => ['string'],
      'gem' => ['string'],
      'go' => ['string'],
      'npm' => ['string'],
      'pip' => ['pandas', 'numpy'],
      'type' => 'packages',
    ],
  ],
  description: 'Python environment with data-analysis packages.',
  metadata: ['foo' => 'string'],
  name: 'x',
  scope: 'organization',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaEnvironment);
```

#### Response

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```

## Delete Environment

`$client->beta->environments->delete(string environmentID, ?list<AnthropicBeta> betas): BetaEnvironmentDeleteResponse`

**delete** `/v1/environments/{environment_id}`

Delete an environment by ID. Returns a confirmation of the deletion.

### Parameters

- `environmentID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaEnvironmentDeleteResponse`

  - `string id`

    Environment identifier

  - `"environment_deleted" type`

    The type of response

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaEnvironmentDeleteResponse = $client->beta->environments->delete(
  'env_011CZkZ9X2dpNyB7HsEFoRfW', betas: ['message-batches-2024-09-24']
);

var_dump($betaEnvironmentDeleteResponse);
```

#### Response

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "type": "environment_deleted"
}
```

## Archive Environment

`$client->beta->environments->archive(string environmentID, ?list<AnthropicBeta> betas): BetaEnvironment`

**post** `/v1/environments/{environment_id}/archive`

Archive an environment by ID. Archived environments cannot be used to create new sessions.

### Parameters

- `environmentID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaEnvironment`

  - `string id`

    Environment identifier (e.g., 'env_...')

  - `?string archivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config config`

    Environment configuration (either Anthropic Cloud or self-hosted)

  - `string createdAt`

    RFC 3339 timestamp when environment was created

  - `string description`

    User-provided description for the environment

  - `array<string,string> metadata`

    User-provided metadata key-value pairs

  - `string name`

    Human-readable name for the environment

  - `"environment" type`

    The type of object (always 'environment')

  - `string updatedAt`

    RFC 3339 timestamp when environment was last updated

  - `?Scope scope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaEnvironment = $client->beta->environments->archive(
  'env_011CZkZ9X2dpNyB7HsEFoRfW', betas: ['message-batches-2024-09-24']
);

var_dump($betaEnvironment);
```

#### Response

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```

## Domain Types

### Beta Cloud Config

- `BetaCloudConfig`

  - `Networking networking`

    Network configuration policy.

  - `BetaPackages packages`

    Package manager configuration.

  - `"cloud" type`

    Environment type

### Beta Cloud Config Params

- `BetaCloudConfigParams`

  - `"cloud" type`

    Environment type

  - `?Networking networking`

    Network configuration policy. Omit on update to preserve the existing value.

  - `?BetaPackagesParams packages`

    Specify packages (and optionally their versions) available in this environment.

    When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

### Beta Environment

- `BetaEnvironment`

  - `string id`

    Environment identifier (e.g., 'env_...')

  - `?string archivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config config`

    Environment configuration (either Anthropic Cloud or self-hosted)

  - `string createdAt`

    RFC 3339 timestamp when environment was created

  - `string description`

    User-provided description for the environment

  - `array<string,string> metadata`

    User-provided metadata key-value pairs

  - `string name`

    Human-readable name for the environment

  - `"environment" type`

    The type of object (always 'environment')

  - `string updatedAt`

    RFC 3339 timestamp when environment was last updated

  - `?Scope scope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

### Beta Environment Delete Response

- `BetaEnvironmentDeleteResponse`

  - `string id`

    Environment identifier

  - `"environment_deleted" type`

    The type of response

### Beta Limited Network

- `BetaLimitedNetwork`

  - `bool allowMCPServers`

    Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

  - `bool allowPackageManagers`

    Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

  - `list<string> allowedHosts`

    Specifies domains the container can reach.

  - `"limited" type`

    Network policy type

### Beta Limited Network Params

- `BetaLimitedNetworkParams`

  - `"limited" type`

    Network policy type

  - `?bool allowMCPServers`

    Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

  - `?bool allowPackageManagers`

    Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

  - `?list<string> allowedHosts`

    Specifies domains the container can reach.

### Beta Packages

- `BetaPackages`

  - `list<string> apt`

    Ubuntu/Debian packages to install

  - `list<string> cargo`

    Rust packages to install

  - `list<string> gem`

    Ruby packages to install

  - `list<string> go`

    Go packages to install

  - `list<string> npm`

    Node.js packages to install

  - `list<string> pip`

    Python packages to install

  - `?Type type`

    Package configuration type

### Beta Packages Params

- `BetaPackagesParams`

  - `?list<string> apt`

    Ubuntu/Debian packages to install

  - `?list<string> cargo`

    Rust packages to install

  - `?list<string> gem`

    Ruby packages to install

  - `?list<string> go`

    Go packages to install

  - `?list<string> npm`

    Node.js packages to install

  - `?list<string> pip`

    Python packages to install

  - `?Type type`

    Package configuration type

### Beta Self Hosted Config

- `BetaSelfHostedConfig`

  - `"self_hosted" type`

    Environment type

### Beta Self Hosted Config Params

- `BetaSelfHostedConfigParams`

  - `"self_hosted" type`

    Environment type

### Beta Unrestricted Network

- `BetaUnrestrictedNetwork`

  - `"unrestricted" type`

    Network policy type

# Work

## Get Work Item

`$client->beta->environments->work->retrieve(string workID, string environmentID, ?list<AnthropicBeta> betas): SelfHostedWork`

**get** `/v1/environments/{environment_id}/work/{work_id}`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Retrieve detailed information about a specific work item.

### Parameters

- `environmentID: string`

- `workID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `SelfHostedWork`

  - `string id`

    Work identifier (e.g., 'work_...')

  - `?string acknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `string createdAt`

    RFC 3339 timestamp when work was created

  - `SessionWorkData data`

    The actual work to be performed

  - `string environmentID`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `?string latestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `array<string,string> metadata`

    User-provided metadata key-value pairs associated with this work item

  - `?string startedAt`

    RFC 3339 timestamp when work execution started

  - `State state`

    Current state of the work item

  - `?string stopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `?string stoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `"work" type`

    The type of object (always 'work')

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaSelfHostedWork = $client->beta->environments->work->retrieve(
  'work_id',
  environmentID: 'env_011CZkZ9X2dpNyB7HsEFoRfW',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaSelfHostedWork);
```

#### Response

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

## Poll for Work

`$client->beta->environments->work->poll(string environmentID, ?int blockMs, ?int reclaimOlderThanMs, ?list<AnthropicBeta> betas, ?string anthropicWorkerID): SelfHostedWork`

**get** `/v1/environments/{environment_id}/work/poll`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Long poll for work items in the queue.

### Parameters

- `environmentID: string`

- `blockMs?:optional int`

  How long to wait for work to arrive before returning. Must be 1-999 in milliseconds. Defaults to non-blocking (returns immediately if no work is available).

- `reclaimOlderThanMs?:optional int`

  Reclaim unacknowledged work items older than this many milliseconds. If omitted, uses the default (5000ms).

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `anthropicWorkerID?:optional string`

  Unique identifier for the specific worker polling, used to track aggregated environment-level work metrics in Console

### Returns

- `SelfHostedWork`

  - `string id`

    Work identifier (e.g., 'work_...')

  - `?string acknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `string createdAt`

    RFC 3339 timestamp when work was created

  - `SessionWorkData data`

    The actual work to be performed

  - `string environmentID`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `?string latestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `array<string,string> metadata`

    User-provided metadata key-value pairs associated with this work item

  - `?string startedAt`

    RFC 3339 timestamp when work execution started

  - `State state`

    Current state of the work item

  - `?string stopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `?string stoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `"work" type`

    The type of object (always 'work')

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaSelfHostedWork = $client->beta->environments->work->poll(
  'env_011CZkZ9X2dpNyB7HsEFoRfW',
  blockMs: 1,
  reclaimOlderThanMs: 1,
  betas: ['message-batches-2024-09-24'],
  anthropicWorkerID: 'Anthropic-Worker-ID',
);

var_dump($betaSelfHostedWork);
```

#### Response

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

## Acknowledge Work

`$client->beta->environments->work->ack(string workID, string environmentID, ?list<AnthropicBeta> betas): SelfHostedWork`

**post** `/v1/environments/{environment_id}/work/{work_id}/ack`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Acknowledge receipt of a work item, transitioning it from 'queued' to 'starting' and removing it from the queue.

### Parameters

- `environmentID: string`

- `workID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `SelfHostedWork`

  - `string id`

    Work identifier (e.g., 'work_...')

  - `?string acknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `string createdAt`

    RFC 3339 timestamp when work was created

  - `SessionWorkData data`

    The actual work to be performed

  - `string environmentID`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `?string latestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `array<string,string> metadata`

    User-provided metadata key-value pairs associated with this work item

  - `?string startedAt`

    RFC 3339 timestamp when work execution started

  - `State state`

    Current state of the work item

  - `?string stopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `?string stoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `"work" type`

    The type of object (always 'work')

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaSelfHostedWork = $client->beta->environments->work->ack(
  'work_id',
  environmentID: 'env_011CZkZ9X2dpNyB7HsEFoRfW',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaSelfHostedWork);
```

#### Response

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

## Record Heartbeat

`$client->beta->environments->work->heartbeat(string workID, string environmentID, ?int desiredTTLSeconds, ?string expectedLastHeartbeat, ?list<AnthropicBeta> betas): SelfHostedWorkHeartbeatResponse`

**post** `/v1/environments/{environment_id}/work/{work_id}/heartbeat`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Record a heartbeat for a work item to maintain the lease.

### Parameters

- `environmentID: string`

- `workID: string`

- `desiredTTLSeconds?:optional int`

  Desired TTL in seconds

- `expectedLastHeartbeat?:optional string`

  Expected last_heartbeat for conditional update (optimistic concurrency). Use literal 'NO_HEARTBEAT' to claim an unclaimed lease (first heartbeat). For subsequent heartbeats, echo the server's previous last_heartbeat value exactly. Returns 412 Precondition Failed if the actual value doesn't match.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `SelfHostedWorkHeartbeatResponse`

  - `string lastHeartbeat`

    RFC 3339 timestamp of the actual heartbeat from DB

  - `bool leaseExtended`

    Whether the heartbeat succeeded in extending the lease

  - `State state`

    Current state of the work item (active/stopping/stopped)

  - `int ttlSeconds`

    Effective TTL applied to the lease

  - `"work_heartbeat" type`

    The type of response

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaSelfHostedWorkHeartbeatResponse = $client
  ->beta
  ->environments
  ->work
  ->heartbeat(
  'work_id',
  environmentID: 'env_011CZkZ9X2dpNyB7HsEFoRfW',
  desiredTTLSeconds: 0,
  expectedLastHeartbeat: 'expected_last_heartbeat',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaSelfHostedWorkHeartbeatResponse);
```

#### Response

```json
{
  "last_heartbeat": "last_heartbeat",
  "lease_extended": true,
  "state": "queued",
  "ttl_seconds": 0,
  "type": "work_heartbeat"
}
```

## Stop Work

`$client->beta->environments->work->stop(string workID, string environmentID, ?bool force, ?list<AnthropicBeta> betas): SelfHostedWork`

**post** `/v1/environments/{environment_id}/work/{work_id}/stop`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Stop a work item, initiating graceful or forced shutdown.

### Parameters

- `environmentID: string`

- `workID: string`

- `force?:optional bool`

  If true, immediately stop work without graceful shutdown

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `SelfHostedWork`

  - `string id`

    Work identifier (e.g., 'work_...')

  - `?string acknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `string createdAt`

    RFC 3339 timestamp when work was created

  - `SessionWorkData data`

    The actual work to be performed

  - `string environmentID`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `?string latestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `array<string,string> metadata`

    User-provided metadata key-value pairs associated with this work item

  - `?string startedAt`

    RFC 3339 timestamp when work execution started

  - `State state`

    Current state of the work item

  - `?string stopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `?string stoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `"work" type`

    The type of object (always 'work')

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaSelfHostedWork = $client->beta->environments->work->stop(
  'work_id',
  environmentID: 'env_011CZkZ9X2dpNyB7HsEFoRfW',
  force: true,
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaSelfHostedWork);
```

#### Response

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

## List Work Items

`$client->beta->environments->work->list(string environmentID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<SelfHostedWork>`

**get** `/v1/environments/{environment_id}/work`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

List work items in an environment.

### Parameters

- `environmentID: string`

- `limit?:optional int`

  Maximum number of work items to return

- `page?:optional string`

  Opaque cursor from previous response for pagination

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `SelfHostedWork`

  - `string id`

    Work identifier (e.g., 'work_...')

  - `?string acknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `string createdAt`

    RFC 3339 timestamp when work was created

  - `SessionWorkData data`

    The actual work to be performed

  - `string environmentID`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `?string latestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `array<string,string> metadata`

    User-provided metadata key-value pairs associated with this work item

  - `?string startedAt`

    RFC 3339 timestamp when work execution started

  - `State state`

    Current state of the work item

  - `?string stopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `?string stoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `"work" type`

    The type of object (always 'work')

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->environments->work->list(
  'env_011CZkZ9X2dpNyB7HsEFoRfW',
  limit: 1,
  page: 'page',
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "acknowledged_at": "acknowledged_at",
      "created_at": "created_at",
      "data": {
        "id": "id",
        "type": "session"
      },
      "environment_id": "environment_id",
      "latest_heartbeat_at": "latest_heartbeat_at",
      "metadata": {
        "foo": "string"
      },
      "started_at": "started_at",
      "state": "queued",
      "stop_requested_at": "stop_requested_at",
      "stopped_at": "stopped_at",
      "type": "work"
    }
  ],
  "next_page": "next_page"
}
```

## Update Work Item

`$client->beta->environments->work->update(string workID, string environmentID, array<string,string> metadata, ?list<AnthropicBeta> betas): SelfHostedWork`

**post** `/v1/environments/{environment_id}/work/{work_id}`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Update work item metadata with merge semantics.

### Parameters

- `environmentID: string`

- `workID: string`

- `metadata: array<string,string>`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `SelfHostedWork`

  - `string id`

    Work identifier (e.g., 'work_...')

  - `?string acknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `string createdAt`

    RFC 3339 timestamp when work was created

  - `SessionWorkData data`

    The actual work to be performed

  - `string environmentID`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `?string latestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `array<string,string> metadata`

    User-provided metadata key-value pairs associated with this work item

  - `?string startedAt`

    RFC 3339 timestamp when work execution started

  - `State state`

    Current state of the work item

  - `?string stopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `?string stoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `"work" type`

    The type of object (always 'work')

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaSelfHostedWork = $client->beta->environments->work->update(
  'work_id',
  environmentID: 'env_011CZkZ9X2dpNyB7HsEFoRfW',
  metadata: ['foo' => 'string'],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaSelfHostedWork);
```

#### Response

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

## Get Queue Statistics

`$client->beta->environments->work->stats(string environmentID, ?list<AnthropicBeta> betas): SelfHostedWorkQueueStats`

**get** `/v1/environments/{environment_id}/work/stats`

Get statistics about the work queue for an environment.

### Parameters

- `environmentID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `SelfHostedWorkQueueStats`

  - `int depth`

    Number of work items waiting to be picked up (lag from consumer group)

  - `?string oldestQueuedAt`

    RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

  - `int pending`

    Number of work items being processed (polled but not acknowledged)

  - `"work_queue_stats" type`

    The type of object

  - `?int workersPolling`

    Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaSelfHostedWorkQueueStats = $client->beta->environments->work->stats(
  'env_011CZkZ9X2dpNyB7HsEFoRfW', betas: ['message-batches-2024-09-24']
);

var_dump($betaSelfHostedWorkQueueStats);
```

#### Response

```json
{
  "depth": 0,
  "oldest_queued_at": "oldest_queued_at",
  "pending": 0,
  "type": "work_queue_stats",
  "workers_polling": 0
}
```

## Domain Types

### Beta Self Hosted Work

- `SelfHostedWork`

  - `string id`

    Work identifier (e.g., 'work_...')

  - `?string acknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `string createdAt`

    RFC 3339 timestamp when work was created

  - `SessionWorkData data`

    The actual work to be performed

  - `string environmentID`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `?string latestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `array<string,string> metadata`

    User-provided metadata key-value pairs associated with this work item

  - `?string startedAt`

    RFC 3339 timestamp when work execution started

  - `State state`

    Current state of the work item

  - `?string stopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `?string stoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `"work" type`

    The type of object (always 'work')

### Beta Self Hosted Work Heartbeat Response

- `SelfHostedWorkHeartbeatResponse`

  - `string lastHeartbeat`

    RFC 3339 timestamp of the actual heartbeat from DB

  - `bool leaseExtended`

    Whether the heartbeat succeeded in extending the lease

  - `State state`

    Current state of the work item (active/stopping/stopped)

  - `int ttlSeconds`

    Effective TTL applied to the lease

  - `"work_heartbeat" type`

    The type of response

### Beta Self Hosted Work List Response

- `SelfHostedWorkListResponse`

  - `list<SelfHostedWork> data`

    List of work items

  - `?string nextPage`

    Opaque cursor for fetching the next page of results

### Beta Self Hosted Work Queue Stats

- `SelfHostedWorkQueueStats`

  - `int depth`

    Number of work items waiting to be picked up (lag from consumer group)

  - `?string oldestQueuedAt`

    RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

  - `int pending`

    Number of work items being processed (polled but not acknowledged)

  - `"work_queue_stats" type`

    The type of object

  - `?int workersPolling`

    Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.

### Beta Self Hosted Work Stop Request

- `SelfHostedWorkStopRequest`

  - `?bool force`

    If true, immediately stop work without graceful shutdown

### Beta Self Hosted Work Update Request

- `SelfHostedWorkUpdateRequest`

  - `array<string,string> metadata`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

### Beta Session Work Data

- `SessionWorkData`

  - `string id`

    Session identifier (e.g., 'session_...')

  - `"session" type`

    Type of work data

# Sessions

## Create Session

`$client->beta->sessions->create(Agent agent, string environmentID, ?array<string,string> metadata, ?list<Resource> resources, ?string title, ?list<string> vaultIDs, ?list<AnthropicBeta> betas): BetaManagedAgentsSession`

**post** `/v1/sessions`

Create Session

### Parameters

- `agent: Agent`

  Agent identifier. Accepts the `agent` ID string, which pins the latest version for the session, or an `agent` object with both id and version specified.

- `environmentID: string`

  ID of the `environment` defining the container configuration for this session.

- `metadata?:optional array<string,string>`

  Arbitrary key-value metadata attached to the session. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `resources?:optional list<Resource>`

  Resources (e.g. repositories, files) to mount into the session's container.

- `title?:optional string`

  Human-readable session title.

- `vaultIDs?:optional list<string>`

  Vault IDs for stored credentials the agent can use during the session.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsSession`

  - `string id`

  - `BetaManagedAgentsSessionAgent agent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string environmentID`

  - `array<string,string> metadata`

  - `list<BetaManagedAgentsOutcomeEvaluationResource> outcomeEvaluations`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

  - `list<ManagedAgentsSessionResource> resources`

  - `BetaManagedAgentsSessionStats stats`

    Timing statistics for a session.

  - `Status status`

    SessionStatus enum

  - `?string title`

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `BetaManagedAgentsSessionUsage usage`

    Cumulative token usage for a session across all turns.

  - `list<string> vaultIDs`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `?string deploymentID`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsSession = $client->beta->sessions->create(
  agent: 'agent_011CZkYpogX7uDKUyvBTophP',
  environmentID: 'env_011CZkZ9X2dpNyB7HsEFoRfW',
  metadata: ['foo' => 'string'],
  resources: [
    [
      'fileID' => 'file_011CNha8iCJcU1wXNR6q4V8w',
      'type' => 'file',
      'mountPath' => '/uploads/receipt.pdf',
    ],
  ],
  title: 'Order #1234 inquiry',
  vaultIDs: ['string'],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsSession);
```

#### Response

```json
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "description": "A general-purpose starter agent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-sonnet-4-6",
      "speed": "standard"
    },
    "multiagent": {
      "agents": [
        {
          "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
          "description": "A focused research subagent.",
          "mcp_servers": [
            {
              "name": "example-mcp",
              "type": "url",
              "url": "https://example-server.modelcontextprotocol.io/sse"
            }
          ],
          "model": {
            "id": "claude-sonnet-4-6",
            "speed": "standard"
          },
          "name": "Researcher",
          "skills": [
            {
              "skill_id": "xlsx",
              "type": "anthropic",
              "version": "1"
            }
          ],
          "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
          "tools": [
            {
              "configs": [
                {
                  "enabled": true,
                  "name": "bash",
                  "permission_policy": {
                    "type": "always_allow"
                  }
                }
              ],
              "default_config": {
                "enabled": true,
                "permission_policy": {
                  "type": "always_ask"
                }
              },
              "type": "agent_toolset_20260401"
            }
          ],
          "type": "agent",
          "version": 1
        }
      ],
      "type": "coordinator"
    },
    "name": "My First Agent",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      },
      {
        "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
        "type": "custom",
        "version": "2"
      }
    ],
    "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            }
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "metadata": {},
  "outcome_evaluations": [
    {
      "completed_at": "2026-03-15T10:02:31Z",
      "description": "Produce a 2-page summary as summary.md",
      "explanation": "All five sections present with inline citations.",
      "iteration": 0,
      "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
      "result": "satisfied",
      "type": "outcome_evaluation"
    }
  ],
  "resources": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0
  },
  "status": "idle",
  "title": "Order #1234 inquiry",
  "type": "session",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  },
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "deployment_id": "deployment_id"
}
```

## List Sessions

`$client->beta->sessions->list(?string agentID, ?int agentVersion, ?\Datetime createdAtGt, ?\Datetime createdAtGte, ?\Datetime createdAtLt, ?\Datetime createdAtLte, ?string deploymentID, ?bool includeArchived, ?int limit, ?string memoryStoreID, ?Order order, ?string page, ?list<Status> statuses, ?list<AnthropicBeta> betas): BidirectionalPageCursor<BetaManagedAgentsSession>`

**get** `/v1/sessions`

List Sessions

### Parameters

- `agentID?:optional string`

  Filter sessions created with this agent ID.

- `agentVersion?:optional int`

  Filter by agent version. Only applies when agent_id is also set.

- `createdAtGt?:optional \Datetime`

  Return sessions created after this time (exclusive).

- `createdAtGte?:optional \Datetime`

  Return sessions created at or after this time (inclusive).

- `createdAtLt?:optional \Datetime`

  Return sessions created before this time (exclusive).

- `createdAtLte?:optional \Datetime`

  Return sessions created at or before this time (inclusive).

- `deploymentID?:optional string`

  Filter sessions created by this deployment ID.

- `includeArchived?:optional bool`

  When true, includes archived sessions. Default: false (exclude archived).

- `limit?:optional int`

  Maximum number of results to return.

- `memoryStoreID?:optional string`

  Filter sessions whose resources contain a memory_store with this memory store ID.

- `order?:optional Order`

  Sort direction for results, ordered by created_at. Defaults to desc (newest first).

- `page?:optional string`

  Opaque pagination cursor from a previous response.

- `statuses?:optional list<Status>`

  Filter by session status. Repeat the parameter to match any of multiple statuses.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsSession`

  - `string id`

  - `BetaManagedAgentsSessionAgent agent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string environmentID`

  - `array<string,string> metadata`

  - `list<BetaManagedAgentsOutcomeEvaluationResource> outcomeEvaluations`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

  - `list<ManagedAgentsSessionResource> resources`

  - `BetaManagedAgentsSessionStats stats`

    Timing statistics for a session.

  - `Status status`

    SessionStatus enum

  - `?string title`

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `BetaManagedAgentsSessionUsage usage`

    Cumulative token usage for a session across all turns.

  - `list<string> vaultIDs`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `?string deploymentID`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->sessions->list(
  agentID: 'agent_id',
  agentVersion: 0,
  createdAtGt: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtGte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLt: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  deploymentID: 'deployment_id',
  includeArchived: true,
  limit: 0,
  memoryStoreID: 'memory_store_id',
  order: 'asc',
  page: 'page',
  statuses: ['rescheduling'],
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

#### Response

```json
{
  "data": [
    {
      "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
      "agent": {
        "id": "agent_011CZkYpogX7uDKUyvBTophP",
        "description": "A general-purpose starter agent.",
        "mcp_servers": [
          {
            "name": "example-mcp",
            "type": "url",
            "url": "https://example-server.modelcontextprotocol.io/sse"
          }
        ],
        "model": {
          "id": "claude-sonnet-4-6",
          "speed": "standard"
        },
        "multiagent": {
          "agents": [
            {
              "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
              "description": "A focused research subagent.",
              "mcp_servers": [
                {
                  "name": "example-mcp",
                  "type": "url",
                  "url": "https://example-server.modelcontextprotocol.io/sse"
                }
              ],
              "model": {
                "id": "claude-sonnet-4-6",
                "speed": "standard"
              },
              "name": "Researcher",
              "skills": [
                {
                  "skill_id": "xlsx",
                  "type": "anthropic",
                  "version": "1"
                }
              ],
              "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
              "tools": [
                {
                  "configs": [
                    {
                      "enabled": true,
                      "name": "bash",
                      "permission_policy": {
                        "type": "always_allow"
                      }
                    }
                  ],
                  "default_config": {
                    "enabled": true,
                    "permission_policy": {
                      "type": "always_ask"
                    }
                  },
                  "type": "agent_toolset_20260401"
                }
              ],
              "type": "agent",
              "version": 1
            }
          ],
          "type": "coordinator"
        },
        "name": "My First Agent",
        "skills": [
          {
            "skill_id": "xlsx",
            "type": "anthropic",
            "version": "1"
          },
          {
            "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
            "type": "custom",
            "version": "2"
          }
        ],
        "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
        "tools": [
          {
            "configs": [
              {
                "enabled": true,
                "name": "bash",
                "permission_policy": {
                  "type": "always_allow"
                }
              }
            ],
            "default_config": {
              "enabled": true,
              "permission_policy": {
                "type": "always_ask"
              }
            },
            "type": "agent_toolset_20260401"
          }
        ],
        "type": "agent",
        "version": 1
      },
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
      "metadata": {},
      "outcome_evaluations": [
        {
          "completed_at": "2026-03-15T10:02:31Z",
          "description": "Produce a 2-page summary as summary.md",
          "explanation": "All five sections present with inline citations.",
          "iteration": 0,
          "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
          "result": "satisfied",
          "type": "outcome_evaluation"
        }
      ],
      "resources": [
        {
          "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
          "created_at": "2026-03-15T10:00:00Z",
          "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
          "mount_path": "/uploads/receipt.pdf",
          "type": "file",
          "updated_at": "2026-03-15T10:00:00Z"
        },
        {
          "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
          "created_at": "2026-03-15T10:00:00Z",
          "mount_path": "/workspace/example-repo",
          "type": "github_repository",
          "updated_at": "2026-03-15T10:00:00Z",
          "url": "https://github.com/example-org/example-repo",
          "checkout": {
            "name": "main",
            "type": "branch"
          }
        }
      ],
      "stats": {
        "active_seconds": 0,
        "duration_seconds": 0
      },
      "status": "idle",
      "title": "Order #1234 inquiry",
      "type": "session",
      "updated_at": "2026-03-15T10:00:00Z",
      "usage": {
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 0
        },
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "output_tokens": 0
      },
      "vault_ids": [
        "vlt_011CZkZDLs7fYzm1hXNPeRjv"
      ],
      "deployment_id": "deployment_id"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo=",
  "prev_page": "page_MjAyNS0wNS0xM1QwMDowMDowMFo="
}
```

## Get Session

`$client->beta->sessions->retrieve(string sessionID, ?list<AnthropicBeta> betas): BetaManagedAgentsSession`

**get** `/v1/sessions/{session_id}`

Get Session

### Parameters

- `sessionID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsSession`

  - `string id`

  - `BetaManagedAgentsSessionAgent agent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string environmentID`

  - `array<string,string> metadata`

  - `list<BetaManagedAgentsOutcomeEvaluationResource> outcomeEvaluations`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

  - `list<ManagedAgentsSessionResource> resources`

  - `BetaManagedAgentsSessionStats stats`

    Timing statistics for a session.

  - `Status status`

    SessionStatus enum

  - `?string title`

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `BetaManagedAgentsSessionUsage usage`

    Cumulative token usage for a session across all turns.

  - `list<string> vaultIDs`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `?string deploymentID`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsSession = $client->beta->sessions->retrieve(
  'sesn_011CZkZAtmR3yMPDzynEDxu7', betas: ['message-batches-2024-09-24']
);

var_dump($betaManagedAgentsSession);
```

#### Response

```json
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "description": "A general-purpose starter agent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-sonnet-4-6",
      "speed": "standard"
    },
    "multiagent": {
      "agents": [
        {
          "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
          "description": "A focused research subagent.",
          "mcp_servers": [
            {
              "name": "example-mcp",
              "type": "url",
              "url": "https://example-server.modelcontextprotocol.io/sse"
            }
          ],
          "model": {
            "id": "claude-sonnet-4-6",
            "speed": "standard"
          },
          "name": "Researcher",
          "skills": [
            {
              "skill_id": "xlsx",
              "type": "anthropic",
              "version": "1"
            }
          ],
          "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
          "tools": [
            {
              "configs": [
                {
                  "enabled": true,
                  "name": "bash",
                  "permission_policy": {
                    "type": "always_allow"
                  }
                }
              ],
              "default_config": {
                "enabled": true,
                "permission_policy": {
                  "type": "always_ask"
                }
              },
              "type": "agent_toolset_20260401"
            }
          ],
          "type": "agent",
          "version": 1
        }
      ],
      "type": "coordinator"
    },
    "name": "My First Agent",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      },
      {
        "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
        "type": "custom",
        "version": "2"
      }
    ],
    "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            }
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "metadata": {},
  "outcome_evaluations": [
    {
      "completed_at": "2026-03-15T10:02:31Z",
      "description": "Produce a 2-page summary as summary.md",
      "explanation": "All five sections present with inline citations.",
      "iteration": 0,
      "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
      "result": "satisfied",
      "type": "outcome_evaluation"
    }
  ],
  "resources": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0
  },
  "status": "idle",
  "title": "Order #1234 inquiry",
  "type": "session",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  },
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "deployment_id": "deployment_id"
}
```

## Update Session

`$client->beta->sessions->update(string sessionID, ?BetaManagedAgentsSessionAgentUpdate agent, ?array<string,string> metadata, ?string title, ?list<string> vaultIDs, ?list<AnthropicBeta> betas): BetaManagedAgentsSession`

**post** `/v1/sessions/{session_id}`

Update Session

### Parameters

- `sessionID: string`

- `agent?:optional BetaManagedAgentsSessionAgentUpdate`

  Mid-session agent configuration update. Only `tools` and `mcp_servers` are updatable. Full replacement: the provided array becomes the new value. To preserve existing entries, GET the session, modify the array, and POST it back.

- `metadata?:optional array<string,string>`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve.

- `title?:optional string`

  Human-readable session title.

- `vaultIDs?:optional list<string>`

  Vault IDs (`vlt_*`) to attach to the session. Not yet supported; requests setting this field are rejected. Reserved for future use.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsSession`

  - `string id`

  - `BetaManagedAgentsSessionAgent agent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string environmentID`

  - `array<string,string> metadata`

  - `list<BetaManagedAgentsOutcomeEvaluationResource> outcomeEvaluations`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

  - `list<ManagedAgentsSessionResource> resources`

  - `BetaManagedAgentsSessionStats stats`

    Timing statistics for a session.

  - `Status status`

    SessionStatus enum

  - `?string title`

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `BetaManagedAgentsSessionUsage usage`

    Cumulative token usage for a session across all turns.

  - `list<string> vaultIDs`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `?string deploymentID`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsSession = $client->beta->sessions->update(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  agent: [
    'mcpServers' => [
      [
        'name' => 'example-mcp',
        'type' => 'url',
        'url' => 'https://example-server.modelcontextprotocol.io/sse',
      ],
    ],
    'tools' => [
      [
        'type' => 'agent_toolset_20260401',
        'configs' => [
          [
            'name' => 'bash',
            'enabled' => true,
            'permissionPolicy' => ['type' => 'always_allow'],
          ],
        ],
        'defaultConfig' => [
          'enabled' => true, 'permissionPolicy' => ['type' => 'always_allow']
        ],
      ],
    ],
  ],
  metadata: ['foo' => 'string'],
  title: 'Order #1234 inquiry',
  vaultIDs: ['string'],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsSession);
```

#### Response

```json
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "description": "A general-purpose starter agent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-sonnet-4-6",
      "speed": "standard"
    },
    "multiagent": {
      "agents": [
        {
          "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
          "description": "A focused research subagent.",
          "mcp_servers": [
            {
              "name": "example-mcp",
              "type": "url",
              "url": "https://example-server.modelcontextprotocol.io/sse"
            }
          ],
          "model": {
            "id": "claude-sonnet-4-6",
            "speed": "standard"
          },
          "name": "Researcher",
          "skills": [
            {
              "skill_id": "xlsx",
              "type": "anthropic",
              "version": "1"
            }
          ],
          "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
          "tools": [
            {
              "configs": [
                {
                  "enabled": true,
                  "name": "bash",
                  "permission_policy": {
                    "type": "always_allow"
                  }
                }
              ],
              "default_config": {
                "enabled": true,
                "permission_policy": {
                  "type": "always_ask"
                }
              },
              "type": "agent_toolset_20260401"
            }
          ],
          "type": "agent",
          "version": 1
        }
      ],
      "type": "coordinator"
    },
    "name": "My First Agent",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      },
      {
        "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
        "type": "custom",
        "version": "2"
      }
    ],
    "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            }
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "metadata": {},
  "outcome_evaluations": [
    {
      "completed_at": "2026-03-15T10:02:31Z",
      "description": "Produce a 2-page summary as summary.md",
      "explanation": "All five sections present with inline citations.",
      "iteration": 0,
      "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
      "result": "satisfied",
      "type": "outcome_evaluation"
    }
  ],
  "resources": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0
  },
  "status": "idle",
  "title": "Order #1234 inquiry",
  "type": "session",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  },
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "deployment_id": "deployment_id"
}
```

## Delete Session

`$client->beta->sessions->delete(string sessionID, ?list<AnthropicBeta> betas): BetaManagedAgentsDeletedSession`

**delete** `/v1/sessions/{session_id}`

Delete Session

### Parameters

- `sessionID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsDeletedSession`

  - `string id`

  - `Type type`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeletedSession = $client->beta->sessions->delete(
  'sesn_011CZkZAtmR3yMPDzynEDxu7', betas: ['message-batches-2024-09-24']
);

var_dump($betaManagedAgentsDeletedSession);
```

#### Response

```json
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "type": "session_deleted"
}
```

## Archive Session

`$client->beta->sessions->archive(string sessionID, ?list<AnthropicBeta> betas): BetaManagedAgentsSession`

**post** `/v1/sessions/{session_id}/archive`

Archive Session

### Parameters

- `sessionID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsSession`

  - `string id`

  - `BetaManagedAgentsSessionAgent agent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string environmentID`

  - `array<string,string> metadata`

  - `list<BetaManagedAgentsOutcomeEvaluationResource> outcomeEvaluations`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

  - `list<ManagedAgentsSessionResource> resources`

  - `BetaManagedAgentsSessionStats stats`

    Timing statistics for a session.

  - `Status status`

    SessionStatus enum

  - `?string title`

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `BetaManagedAgentsSessionUsage usage`

    Cumulative token usage for a session across all turns.

  - `list<string> vaultIDs`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `?string deploymentID`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsSession = $client->beta->sessions->archive(
  'sesn_011CZkZAtmR3yMPDzynEDxu7', betas: ['message-batches-2024-09-24']
);

var_dump($betaManagedAgentsSession);
```

#### Response

```json
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "description": "A general-purpose starter agent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-sonnet-4-6",
      "speed": "standard"
    },
    "multiagent": {
      "agents": [
        {
          "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
          "description": "A focused research subagent.",
          "mcp_servers": [
            {
              "name": "example-mcp",
              "type": "url",
              "url": "https://example-server.modelcontextprotocol.io/sse"
            }
          ],
          "model": {
            "id": "claude-sonnet-4-6",
            "speed": "standard"
          },
          "name": "Researcher",
          "skills": [
            {
              "skill_id": "xlsx",
              "type": "anthropic",
              "version": "1"
            }
          ],
          "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
          "tools": [
            {
              "configs": [
                {
                  "enabled": true,
                  "name": "bash",
                  "permission_policy": {
                    "type": "always_allow"
                  }
                }
              ],
              "default_config": {
                "enabled": true,
                "permission_policy": {
                  "type": "always_ask"
                }
              },
              "type": "agent_toolset_20260401"
            }
          ],
          "type": "agent",
          "version": 1
        }
      ],
      "type": "coordinator"
    },
    "name": "My First Agent",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      },
      {
        "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
        "type": "custom",
        "version": "2"
      }
    ],
    "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            }
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "metadata": {},
  "outcome_evaluations": [
    {
      "completed_at": "2026-03-15T10:02:31Z",
      "description": "Produce a 2-page summary as summary.md",
      "explanation": "All five sections present with inline citations.",
      "iteration": 0,
      "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
      "result": "satisfied",
      "type": "outcome_evaluation"
    }
  ],
  "resources": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0
  },
  "status": "idle",
  "title": "Order #1234 inquiry",
  "type": "session",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  },
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "deployment_id": "deployment_id"
}
```

## Domain Types

### Beta Managed Agents Agent Message Preview

- `BetaManagedAgentsAgentMessagePreview`

  - `string id`

    The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

  - `Type type`

### Beta Managed Agents Agent Params

- `BetaManagedAgentsAgentParams`

  - `string id`

    The `agent` ID.

  - `Type type`

  - `?int version`

    The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

### Beta Managed Agents Agent Thinking Preview

- `BetaManagedAgentsAgentThinkingPreview`

  - `string id`

    The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

  - `Type type`

### Beta Managed Agents Agent With Overrides Params

- `BetaManagedAgentsAgentWithOverridesParams`

  - `string id`

    The `agent` ID.

  - `Type type`

  - `?list<BetaManagedAgentsURLMCPServerParams> mcpServers`

    Replacement MCP server list. Full replacement: the provided array becomes the MCP servers. Send an empty array to clear; omit to preserve the agent's servers.

  - `?Model model`

    Replacement model. Accepts the model string, e.g. `claude-opus-4-6`, or a `model_config` object. Omit to use the agent's model.

  - `?list<BetaManagedAgentsSkillParams> skills`

    Replacement skill list. Full replacement: the provided array becomes the skills. Send an empty array to clear; omit to preserve the agent's skills.

  - `?string system`

    Replacement system prompt. Up to 100,000 characters. Set to null to clear the agent's system prompt; omit to preserve it.

  - `?list<Tool> tools`

    Replacement tool list. Full replacement: the provided array becomes the tool configuration. Send an empty array to clear; omit to preserve the agent's tools.

  - `?int version`

    The specific `agent` version to use. Omit to use the latest version.

### Beta Managed Agents Branch Checkout

- `BetaManagedAgentsBranchCheckout`

  - `string name`

    Branch name to check out.

  - `Type type`

### Beta Managed Agents Cache Creation Usage

- `BetaManagedAgentsCacheCreationUsage`

  - `?int ephemeral1hInputTokens`

    Tokens used to create 1-hour ephemeral cache entries.

  - `?int ephemeral5mInputTokens`

    Tokens used to create 5-minute ephemeral cache entries.

### Beta Managed Agents Commit Checkout

- `BetaManagedAgentsCommitCheckout`

  - `string sha`

    Full commit SHA to check out.

  - `Type type`

### Beta Managed Agents Deleted Session

- `BetaManagedAgentsDeletedSession`

  - `string id`

  - `Type type`

### Beta Managed Agents Delta Content

- `BetaManagedAgentsDeltaContent`

  - `ManagedAgentsTextBlock content`

    Regular text content.

  - `Type type`

  - `?int index`

    Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

### Beta Managed Agents Delta Event

- `BetaManagedAgentsDeltaEvent`

  - `BetaManagedAgentsDeltaContent delta`

    One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

  - `string eventID`

    The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

  - `Type type`

### Beta Managed Agents Delta Type

- `BetaManagedAgentsDeltaType`

  - `"agent.message"`

  - `"agent.thinking"`

### Beta Managed Agents File Resource Params

- `BetaManagedAgentsFileResourceParams`

  - `string fileID`

    ID of a previously uploaded file.

  - `Type type`

  - `?string mountPath`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

### Beta Managed Agents GitHub Repository Resource Params

- `BetaManagedAgentsGitHubRepositoryResourceParams`

  - `string authorizationToken`

    GitHub authorization token used to clone the repository.

  - `Type type`

  - `string url`

    Github URL of the repository

  - `?Checkout checkout`

    Branch or commit to check out. Defaults to the repository's default branch.

  - `?string mountPath`

    Mount path in the container. Defaults to `/workspace/<repo-name>`.

### Beta Managed Agents Memory Store Resource Param

- `BetaManagedAgentsMemoryStoreResourceParam`

  - `string memoryStoreID`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `Type type`

  - `?Access access`

    Access mode for an attached memory store.

  - `?string instructions`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Multiagent

- `BetaManagedAgentsMultiagent`

  - `list<BetaManagedAgentsAgentReference> agents`

    Agents the coordinator may spawn as session threads, each resolved to a specific version.

  - `Type type`

### Beta Managed Agents Multiagent Params

- `BetaManagedAgentsMultiagentParams`

  - `list<BetaManagedAgentsMultiagentRosterEntryParams> agents`

    Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

  - `Type type`

### Beta Managed Agents Multiagent Roster Entry Params

- `BetaManagedAgentsMultiagentRosterEntryParams`

  - `string`

  - `BetaManagedAgentsAgentParams`

    - `string id`

      The `agent` ID.

    - `Type type`

    - `?int version`

      The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

  - `BetaManagedAgentsMultiagentSelfParams`

    - `Type type`

### Beta Managed Agents Outcome Evaluation Resource

- `BetaManagedAgentsOutcomeEvaluationResource`

  - `?\Datetime completedAt`

    A timestamp in RFC 3339 format

  - `string description`

    What the agent should produce.

  - `?string explanation`

    Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

  - `int iteration`

    0-indexed revision cycle the outcome is currently on.

  - `string outcomeID`

    Server-generated outc_ ID for this outcome.

  - `string result`

    Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

  - `Type type`

### Beta Managed Agents Session

- `BetaManagedAgentsSession`

  - `string id`

  - `BetaManagedAgentsSessionAgent agent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string environmentID`

  - `array<string,string> metadata`

  - `list<BetaManagedAgentsOutcomeEvaluationResource> outcomeEvaluations`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

  - `list<ManagedAgentsSessionResource> resources`

  - `BetaManagedAgentsSessionStats stats`

    Timing statistics for a session.

  - `Status status`

    SessionStatus enum

  - `?string title`

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `BetaManagedAgentsSessionUsage usage`

    Cumulative token usage for a session across all turns.

  - `list<string> vaultIDs`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `?string deploymentID`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Beta Managed Agents Session Agent

- `BetaManagedAgentsSessionAgent`

  - `string id`

  - `?string description`

  - `list<BetaManagedAgentsMCPServerURLDefinition> mcpServers`

  - `BetaManagedAgentsModelConfig model`

    Model identifier and configuration.

  - `?BetaManagedAgentsSessionMultiagentCoordinator multiagent`

    Resolved coordinator topology with full agent definitions for each roster member.

  - `string name`

  - `list<Skill> skills`

  - `?string system`

  - `list<Tool> tools`

  - `Type type`

  - `int version`

### Beta Managed Agents Session Agent Update

- `BetaManagedAgentsSessionAgentUpdate`

  - `?list<BetaManagedAgentsURLMCPServerParams> mcpServers`

    Replacement MCP server list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

  - `?list<Tool> tools`

    Replacement tool list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

### Beta Managed Agents Session Multiagent Coordinator

- `BetaManagedAgentsSessionMultiagentCoordinator`

  - `list<BetaManagedAgentsSessionThreadAgent> agents`

    Full `agent` definitions the coordinator may spawn as session threads.

  - `Type type`

### Beta Managed Agents Session Stats

- `BetaManagedAgentsSessionStats`

  - `?float activeSeconds`

    Cumulative time in seconds the session spent in running status. Excludes idle time.

  - `?float durationSeconds`

    Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

### Beta Managed Agents Session Updated Event

- `BetaManagedAgentsSessionUpdatedEvent`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

  - `?BetaManagedAgentsSessionAgent agent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

  - `?array<string,string> metadata`

    The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

  - `?string title`

    The session's new title. Present only when the update changed it.

### Beta Managed Agents Session Usage

- `BetaManagedAgentsSessionUsage`

  - `?BetaManagedAgentsCacheCreationUsage cacheCreation`

    Prompt-cache creation token usage broken down by cache lifetime.

  - `?int cacheReadInputTokens`

    Total tokens read from prompt cache.

  - `?int inputTokens`

    Total input tokens consumed across all turns.

  - `?int outputTokens`

    Total output tokens generated across all turns.

### Beta Managed Agents Start Event

- `BetaManagedAgentsStartEvent`

  - `BetaManagedAgentsStartEventPreview event`

    The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

  - `Type type`

### Beta Managed Agents Start Event Preview

- `BetaManagedAgentsStartEventPreview`

  - `BetaManagedAgentsAgentMessagePreview`

    - `string id`

      The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

    - `Type type`

  - `BetaManagedAgentsAgentThinkingPreview`

    - `string id`

      The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

    - `Type type`

### Beta Managed Agents System Content Block

- `BetaManagedAgentsSystemContentBlock`

  - `string text`

    The text content.

  - `Type type`

### Beta Managed Agents System Message Event

- `BetaManagedAgentsSystemMessageEvent`

  - `string id`

    Unique identifier for this event.

  - `list<BetaManagedAgentsSystemContentBlock> content`

    System content blocks. Text-only.

  - `Type type`

  - `?\Datetime processedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Tool Result Event

- `BetaManagedAgentsUserToolResultEvent`

  - `string id`

    Unique identifier for this event.

  - `string toolUseID`

    The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `Type type`

  - `?list<Content> content`

    The result content returned by the tool.

  - `?bool isError`

    Whether the tool execution resulted in an error.

  - `?\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `?string sessionThreadID`

    Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

# Events

## List Events

`$client->beta->sessions->events->list(string sessionID, ?\Datetime createdAtGt, ?\Datetime createdAtGte, ?\Datetime createdAtLt, ?\Datetime createdAtLte, ?int limit, ?Order order, ?string page, ?list<string> types, ?list<AnthropicBeta> betas): PageCursor<ManagedAgentsSessionEvent>`

**get** `/v1/sessions/{session_id}/events`

List Events

### Parameters

- `sessionID: string`

- `createdAtGt?:optional \Datetime`

  Return events created after this time (exclusive).

- `createdAtGte?:optional \Datetime`

  Return events created at or after this time (inclusive).

- `createdAtLt?:optional \Datetime`

  Return events created before this time (exclusive).

- `createdAtLte?:optional \Datetime`

  Return events created at or before this time (inclusive).

- `limit?:optional int`

  Query parameter for limit

- `order?:optional Order`

  Sort direction for results, ordered by created_at. Defaults to asc (chronological).

- `page?:optional string`

  Opaque pagination cursor from a previous response's next_page.

- `types?:optional list<string>`

  Filter by event type. Values match the `type` field on returned events (for example, `user.message` or `agent.tool_use`). Omit to return all event types.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsSessionEvent`

  - `ManagedAgentsUserMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of content blocks comprising the user message.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `ManagedAgentsUserInterruptEvent`

    - `string id`

      Unique identifier for this event.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `ManagedAgentsUserToolConfirmationEvent`

    - `string id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

    - `string toolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?string denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `ManagedAgentsUserCustomToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string customToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `ManagedAgentsAgentCustomToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the custom tool being called.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `ManagedAgentsAgentMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<ManagedAgentsTextBlock> content`

      Array of text blocks comprising the agent response.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsAgentThinkingEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsAgentMCPToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string mcpServerName`

      Name of the MCP server providing the tool.

    - `string name`

      Name of the MCP tool being used.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `ManagedAgentsAgentMCPToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string mcpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `ManagedAgentsAgentToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the agent tool being used.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `ManagedAgentsAgentToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `ManagedAgentsAgentThreadMessageReceivedEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `string fromSessionThreadID`

      Public `sthr_` ID of the thread that sent the message.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?string fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `ManagedAgentsAgentThreadMessageSentEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string toSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type type`

    - `?string toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `ManagedAgentsAgentThreadContextCompactedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionErrorEvent`

    - `string id`

      Unique identifier for this event.

    - `Error error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusRescheduledEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusRunningEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusIdleEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

    - `Type type`

  - `ManagedAgentsSessionStatusTerminatedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionThreadCreatedEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the callable agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public `sthr_` ID of the newly created thread.

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationStartEvent`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationEndEvent`

    - `string id`

      Unique identifier for this event.

    - `string explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type type`

    - `ManagedAgentsSpanModelUsage usage`

      Token usage for a single model request.

  - `ManagedAgentsSpanModelRequestStartEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanModelRequestEndEvent`

    - `string id`

      Unique identifier for this event.

    - `?bool isError`

      Whether the model request resulted in an error.

    - `string modelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `ManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsUserDefineOutcomeEvent`

    - `string id`

      Unique identifier for this event.

    - `string description`

      What the agent should produce. Copied from the input event.

    - `?int maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `string outcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

    - `Type type`

  - `ManagedAgentsSessionDeletedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionThreadStatusRunningEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that started running.

    - `Type type`

  - `ManagedAgentsSessionThreadStatusIdleEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

    - `Type type`

  - `ManagedAgentsSessionThreadStatusTerminatedEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that terminated.

    - `Type type`

  - `BetaManagedAgentsUserToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `ManagedAgentsSessionThreadStatusRescheduledEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that is retrying.

    - `Type type`

  - `BetaManagedAgentsSessionUpdatedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?BetaManagedAgentsSessionAgent agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `?array<string,string> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `?string title`

      The session's new title. Present only when the update changed it.

  - `BetaManagedAgentsSystemMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->sessions->events->list(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  createdAtGt: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtGte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLt: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  limit: 0,
  order: 'asc',
  page: 'page',
  types: ['string'],
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

#### Response

```json
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sevt_011CZkZHPq1jCdq5lbRTjiVnz",
      "content": [
        {
          "text": "Let me look up order #1234 for you.",
          "type": "text"
        }
      ],
      "processed_at": "2026-03-15T10:00:00Z",
      "type": "agent.message"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Send Events

`$client->beta->sessions->events->send(string sessionID, list<ManagedAgentsEventParams> events, ?list<AnthropicBeta> betas): ManagedAgentsSendSessionEvents`

**post** `/v1/sessions/{session_id}/events`

Send Events

### Parameters

- `sessionID: string`

- `events: list<ManagedAgentsEventParams>`

  Events to send to the `session`.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsSendSessionEvents`

  - `?list<Data> data`

    Sent events

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsSendSessionEvents = $client->beta->sessions->events->send(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  events: [
    [
      'content' => [['text' => 'Where is my order #1234?', 'type' => 'text']],
      'type' => 'user.message',
    ],
  ],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsSendSessionEvents);
```

#### Response

```json
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    }
  ]
}
```

## Stream Events

`$client->beta->sessions->events->stream(string sessionID, ?list<BetaManagedAgentsDeltaType> eventDeltas, ?list<AnthropicBeta> betas): ManagedAgentsStreamSessionEvents`

**get** `/v1/sessions/{session_id}/events/stream`

Stream Events

### Parameters

- `sessionID: string`

- `eventDeltas?:optional list<BetaManagedAgentsDeltaType>`

  When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsStreamSessionEvents`

  - `ManagedAgentsUserMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of content blocks comprising the user message.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `ManagedAgentsUserInterruptEvent`

    - `string id`

      Unique identifier for this event.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `ManagedAgentsUserToolConfirmationEvent`

    - `string id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

    - `string toolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?string denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `ManagedAgentsUserCustomToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string customToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `ManagedAgentsAgentCustomToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the custom tool being called.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `ManagedAgentsAgentMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<ManagedAgentsTextBlock> content`

      Array of text blocks comprising the agent response.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsAgentThinkingEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsAgentMCPToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string mcpServerName`

      Name of the MCP server providing the tool.

    - `string name`

      Name of the MCP tool being used.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `ManagedAgentsAgentMCPToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string mcpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `ManagedAgentsAgentToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the agent tool being used.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `ManagedAgentsAgentToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `ManagedAgentsAgentThreadMessageReceivedEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `string fromSessionThreadID`

      Public `sthr_` ID of the thread that sent the message.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?string fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `ManagedAgentsAgentThreadMessageSentEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string toSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type type`

    - `?string toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `ManagedAgentsAgentThreadContextCompactedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionErrorEvent`

    - `string id`

      Unique identifier for this event.

    - `Error error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusRescheduledEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusRunningEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusIdleEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

    - `Type type`

  - `ManagedAgentsSessionStatusTerminatedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionThreadCreatedEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the callable agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public `sthr_` ID of the newly created thread.

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationStartEvent`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationEndEvent`

    - `string id`

      Unique identifier for this event.

    - `string explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type type`

    - `ManagedAgentsSpanModelUsage usage`

      Token usage for a single model request.

  - `ManagedAgentsSpanModelRequestStartEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanModelRequestEndEvent`

    - `string id`

      Unique identifier for this event.

    - `?bool isError`

      Whether the model request resulted in an error.

    - `string modelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `ManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsUserDefineOutcomeEvent`

    - `string id`

      Unique identifier for this event.

    - `string description`

      What the agent should produce. Copied from the input event.

    - `?int maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `string outcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

    - `Type type`

  - `ManagedAgentsSessionDeletedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionThreadStatusRunningEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that started running.

    - `Type type`

  - `ManagedAgentsSessionThreadStatusIdleEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

    - `Type type`

  - `ManagedAgentsSessionThreadStatusTerminatedEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that terminated.

    - `Type type`

  - `BetaManagedAgentsUserToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `ManagedAgentsSessionThreadStatusRescheduledEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that is retrying.

    - `Type type`

  - `BetaManagedAgentsSessionUpdatedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?BetaManagedAgentsSessionAgent agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `?array<string,string> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `?string title`

      The session's new title. Present only when the update changed it.

  - `BetaManagedAgentsStartEvent`

    - `BetaManagedAgentsStartEventPreview event`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

    - `Type type`

  - `BetaManagedAgentsDeltaEvent`

    - `BetaManagedAgentsDeltaContent delta`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

    - `string eventID`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `Type type`

  - `BetaManagedAgentsSystemMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsStreamSessionEvents = $client
  ->beta
  ->sessions
  ->events
  ->streamStream(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  eventDeltas: [BetaManagedAgentsDeltaType::AGENT_MESSAGE],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsStreamSessionEvents);
```

#### Response

```json
{
  "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
  "content": [
    {
      "text": "Where is my order #1234?",
      "type": "text"
    }
  ],
  "type": "user.message",
  "processed_at": "2026-03-15T10:00:00Z"
}
```

## Domain Types

### Beta Managed Agents Agent Custom Tool Use Event

- `ManagedAgentsAgentCustomToolUseEvent`

  - `string id`

    Unique identifier for this event.

  - `array<string,mixed> input`

    Input parameters for the tool call.

  - `string name`

    Name of the custom tool being called.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

  - `?string sessionThreadID`

    When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

### Beta Managed Agents Agent MCP Tool Result Event

- `ManagedAgentsAgentMCPToolResultEvent`

  - `string id`

    Unique identifier for this event.

  - `string mcpToolUseID`

    The id of the `agent.mcp_tool_use` event this result corresponds to.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

  - `?list<Content> content`

    The result content returned by the tool.

  - `?bool isError`

    Whether the tool execution resulted in an error.

### Beta Managed Agents Agent MCP Tool Use Event

- `ManagedAgentsAgentMCPToolUseEvent`

  - `string id`

    Unique identifier for this event.

  - `array<string,mixed> input`

    Input parameters for the tool call.

  - `string mcpServerName`

    Name of the MCP server providing the tool.

  - `string name`

    Name of the MCP tool being used.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

  - `?EvaluatedPermission evaluatedPermission`

    AgentEvaluatedPermission enum

  - `?string sessionThreadID`

    When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

### Beta Managed Agents Agent Message Event

- `ManagedAgentsAgentMessageEvent`

  - `string id`

    Unique identifier for this event.

  - `list<ManagedAgentsTextBlock> content`

    Array of text blocks comprising the agent response.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

### Beta Managed Agents Agent Thinking Event

- `ManagedAgentsAgentThinkingEvent`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

### Beta Managed Agents Agent Thread Context Compacted Event

- `ManagedAgentsAgentThreadContextCompactedEvent`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

### Beta Managed Agents Agent Thread Message Received Event

- `ManagedAgentsAgentThreadMessageReceivedEvent`

  - `string id`

    Unique identifier for this event.

  - `list<Content> content`

    Message content blocks.

  - `string fromSessionThreadID`

    Public `sthr_` ID of the thread that sent the message.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

  - `?string fromAgentName`

    Name of the callable agent this message came from. Absent when received from the primary agent.

### Beta Managed Agents Agent Thread Message Sent Event

- `ManagedAgentsAgentThreadMessageSentEvent`

  - `string id`

    Unique identifier for this event.

  - `list<Content> content`

    Message content blocks.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `string toSessionThreadID`

    Public `sthr_` ID of the thread the message was sent to.

  - `Type type`

  - `?string toAgentName`

    Name of the callable agent this message was sent to. Absent when sent to the primary agent.

### Beta Managed Agents Agent Tool Result Event

- `ManagedAgentsAgentToolResultEvent`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `string toolUseID`

    The id of the `agent.tool_use` event this result corresponds to.

  - `Type type`

  - `?list<Content> content`

    The result content returned by the tool.

  - `?bool isError`

    Whether the tool execution resulted in an error.

### Beta Managed Agents Agent Tool Use Event

- `ManagedAgentsAgentToolUseEvent`

  - `string id`

    Unique identifier for this event.

  - `array<string,mixed> input`

    Input parameters for the tool call.

  - `string name`

    Name of the agent tool being used.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

  - `?EvaluatedPermission evaluatedPermission`

    AgentEvaluatedPermission enum

  - `?string sessionThreadID`

    When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

### Beta Managed Agents Base64 Document Source

- `ManagedAgentsBase64DocumentSource`

  - `string data`

    Base64-encoded document data.

  - `string mediaType`

    MIME type of the document (e.g., "application/pdf").

  - `Type type`

### Beta Managed Agents Base64 Image Source

- `ManagedAgentsBase64ImageSource`

  - `string data`

    Base64-encoded image data.

  - `string mediaType`

    MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

  - `Type type`

### Beta Managed Agents Billing Error

- `ManagedAgentsBillingError`

  - `string message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

  - `Type type`

### Beta Managed Agents Credential Host Unreachable Error

- `ManagedAgentsCredentialHostUnreachableError`

  - `string credentialID`

    ID of the affected credential.

  - `string message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

  - `Type type`

  - `string vaultID`

    ID of the vault containing the affected credential.

### Beta Managed Agents Document Block

- `ManagedAgentsDocumentBlock`

  - `Source source`

    Union type for document source variants.

  - `Type type`

  - `?string context`

    Additional context about the document for the model.

  - `?string title`

    The title of the document.

### Beta Managed Agents Event Params

- `ManagedAgentsEventParams`

  - `ManagedAgentsUserMessageEventParams`

    - `list<Content> content`

      Array of content blocks for the user message.

    - `Type type`

  - `ManagedAgentsUserInterruptEventParams`

    - `Type type`

    - `?string sessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `ManagedAgentsUserToolConfirmationEventParams`

    - `Result result`

      UserToolConfirmationResult enum

    - `string toolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?string denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

  - `ManagedAgentsUserCustomToolResultEventParams`

    - `string customToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `ManagedAgentsUserDefineOutcomeEventParams`

    - `string description`

      What the agent should produce. This is the task specification.

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

    - `Type type`

    - `?int maxIterations`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `ManagedAgentsUserToolResultEventParams`

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `ManagedAgentsSystemMessageEventParams`

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks to append. Text-only.

    - `Type type`

### Beta Managed Agents File Document Source

- `ManagedAgentsFileDocumentSource`

  - `string fileID`

    ID of a previously uploaded file.

  - `Type type`

### Beta Managed Agents File Image Source

- `ManagedAgentsFileImageSource`

  - `string fileID`

    ID of a previously uploaded file.

  - `Type type`

### Beta Managed Agents File Rubric

- `ManagedAgentsFileRubric`

  - `string fileID`

    ID of the rubric file.

  - `Type type`

### Beta Managed Agents File Rubric Params

- `ManagedAgentsFileRubricParams`

  - `string fileID`

    ID of the rubric file.

  - `Type type`

### Beta Managed Agents Image Block

- `ManagedAgentsImageBlock`

  - `Source source`

    Union type for image source variants.

  - `Type type`

### Beta Managed Agents MCP Authentication Failed Error

- `ManagedAgentsMCPAuthenticationFailedError`

  - `string mcpServerName`

    Name of the MCP server that failed authentication.

  - `string message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

  - `Type type`

### Beta Managed Agents MCP Connection Failed Error

- `ManagedAgentsMCPConnectionFailedError`

  - `string mcpServerName`

    Name of the MCP server that failed to connect.

  - `string message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

  - `Type type`

### Beta Managed Agents Model Overloaded Error

- `ManagedAgentsModelOverloadedError`

  - `string message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

  - `Type type`

### Beta Managed Agents Model Rate Limited Error

- `ManagedAgentsModelRateLimitedError`

  - `string message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

  - `Type type`

### Beta Managed Agents Model Request Failed Error

- `ManagedAgentsModelRequestFailedError`

  - `string message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

  - `Type type`

### Beta Managed Agents Plain Text Document Source

- `ManagedAgentsPlainTextDocumentSource`

  - `string data`

    The plain text content.

  - `MediaType mediaType`

    MIME type of the text content. Must be "text/plain".

  - `Type type`

### Beta Managed Agents Retry Status Exhausted

- `ManagedAgentsRetryStatusExhausted`

  - `Type type`

### Beta Managed Agents Retry Status Retrying

- `ManagedAgentsRetryStatusRetrying`

  - `Type type`

### Beta Managed Agents Retry Status Terminal

- `ManagedAgentsRetryStatusTerminal`

  - `Type type`

### Beta Managed Agents Search Result Block

- `ManagedAgentsSearchResultBlock`

  - `ManagedAgentsSearchResultCitations citations`

    Citation settings for a search result.

  - `list<ManagedAgentsSearchResultContent> content`

    Array of text content blocks from the search result.

  - `string source`

    The URL source of the search result.

  - `string title`

    The title of the search result.

  - `Type type`

### Beta Managed Agents Search Result Citations

- `ManagedAgentsSearchResultCitations`

  - `bool enabled`

    Whether citations are enabled for this search result.

### Beta Managed Agents Search Result Content

- `ManagedAgentsSearchResultContent`

  - `string text`

    The text content.

  - `Type type`

### Beta Managed Agents Send Session Events

- `ManagedAgentsSendSessionEvents`

  - `?list<Data> data`

    Sent events

### Beta Managed Agents Session Deleted Event

- `ManagedAgentsSessionDeletedEvent`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

### Beta Managed Agents Session End Turn

- `ManagedAgentsSessionEndTurn`

  - `Type type`

### Beta Managed Agents Session Error Event

- `ManagedAgentsSessionErrorEvent`

  - `string id`

    Unique identifier for this event.

  - `Error error`

    An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

### Beta Managed Agents Session Event

- `ManagedAgentsSessionEvent`

  - `ManagedAgentsUserMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of content blocks comprising the user message.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `ManagedAgentsUserInterruptEvent`

    - `string id`

      Unique identifier for this event.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `ManagedAgentsUserToolConfirmationEvent`

    - `string id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

    - `string toolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?string denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `ManagedAgentsUserCustomToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string customToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `ManagedAgentsAgentCustomToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the custom tool being called.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `ManagedAgentsAgentMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<ManagedAgentsTextBlock> content`

      Array of text blocks comprising the agent response.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsAgentThinkingEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsAgentMCPToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string mcpServerName`

      Name of the MCP server providing the tool.

    - `string name`

      Name of the MCP tool being used.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `ManagedAgentsAgentMCPToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string mcpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `ManagedAgentsAgentToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the agent tool being used.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `ManagedAgentsAgentToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `ManagedAgentsAgentThreadMessageReceivedEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `string fromSessionThreadID`

      Public `sthr_` ID of the thread that sent the message.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?string fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `ManagedAgentsAgentThreadMessageSentEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string toSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type type`

    - `?string toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `ManagedAgentsAgentThreadContextCompactedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionErrorEvent`

    - `string id`

      Unique identifier for this event.

    - `Error error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusRescheduledEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusRunningEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusIdleEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

    - `Type type`

  - `ManagedAgentsSessionStatusTerminatedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionThreadCreatedEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the callable agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public `sthr_` ID of the newly created thread.

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationStartEvent`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationEndEvent`

    - `string id`

      Unique identifier for this event.

    - `string explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type type`

    - `ManagedAgentsSpanModelUsage usage`

      Token usage for a single model request.

  - `ManagedAgentsSpanModelRequestStartEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanModelRequestEndEvent`

    - `string id`

      Unique identifier for this event.

    - `?bool isError`

      Whether the model request resulted in an error.

    - `string modelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `ManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsUserDefineOutcomeEvent`

    - `string id`

      Unique identifier for this event.

    - `string description`

      What the agent should produce. Copied from the input event.

    - `?int maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `string outcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

    - `Type type`

  - `ManagedAgentsSessionDeletedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionThreadStatusRunningEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that started running.

    - `Type type`

  - `ManagedAgentsSessionThreadStatusIdleEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

    - `Type type`

  - `ManagedAgentsSessionThreadStatusTerminatedEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that terminated.

    - `Type type`

  - `BetaManagedAgentsUserToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `ManagedAgentsSessionThreadStatusRescheduledEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that is retrying.

    - `Type type`

  - `BetaManagedAgentsSessionUpdatedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?BetaManagedAgentsSessionAgent agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `?array<string,string> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `?string title`

      The session's new title. Present only when the update changed it.

  - `BetaManagedAgentsSystemMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

### Beta Managed Agents Session Requires Action

- `ManagedAgentsSessionRequiresAction`

  - `list<string> eventIDs`

    The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

  - `Type type`

### Beta Managed Agents Session Retries Exhausted

- `ManagedAgentsSessionRetriesExhausted`

  - `Type type`

### Beta Managed Agents Session Status Idle Event

- `ManagedAgentsSessionStatusIdleEvent`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `StopReason stopReason`

    The agent completed its turn naturally and is ready for the next user message.

  - `Type type`

### Beta Managed Agents Session Status Rescheduled Event

- `ManagedAgentsSessionStatusRescheduledEvent`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

### Beta Managed Agents Session Status Running Event

- `ManagedAgentsSessionStatusRunningEvent`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

### Beta Managed Agents Session Status Terminated Event

- `ManagedAgentsSessionStatusTerminatedEvent`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

### Beta Managed Agents Session Thread Created Event

- `ManagedAgentsSessionThreadCreatedEvent`

  - `string id`

    Unique identifier for this event.

  - `string agentName`

    Name of the callable agent the thread runs.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `string sessionThreadID`

    Public `sthr_` ID of the newly created thread.

  - `Type type`

### Beta Managed Agents Session Thread Status Idle Event

- `ManagedAgentsSessionThreadStatusIdleEvent`

  - `string id`

    Unique identifier for this event.

  - `string agentName`

    Name of the agent the thread runs.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `string sessionThreadID`

    Public sthr_ ID of the thread that went idle.

  - `StopReason stopReason`

    The agent completed its turn naturally and is ready for the next user message.

  - `Type type`

### Beta Managed Agents Session Thread Status Rescheduled Event

- `ManagedAgentsSessionThreadStatusRescheduledEvent`

  - `string id`

    Unique identifier for this event.

  - `string agentName`

    Name of the agent the thread runs.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `string sessionThreadID`

    Public sthr_ ID of the thread that is retrying.

  - `Type type`

### Beta Managed Agents Session Thread Status Running Event

- `ManagedAgentsSessionThreadStatusRunningEvent`

  - `string id`

    Unique identifier for this event.

  - `string agentName`

    Name of the agent the thread runs.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `string sessionThreadID`

    Public sthr_ ID of the thread that started running.

  - `Type type`

### Beta Managed Agents Session Thread Status Terminated Event

- `ManagedAgentsSessionThreadStatusTerminatedEvent`

  - `string id`

    Unique identifier for this event.

  - `string agentName`

    Name of the agent the thread runs.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `string sessionThreadID`

    Public sthr_ ID of the thread that terminated.

  - `Type type`

### Beta Managed Agents Span Model Request End Event

- `ManagedAgentsSpanModelRequestEndEvent`

  - `string id`

    Unique identifier for this event.

  - `?bool isError`

    Whether the model request resulted in an error.

  - `string modelRequestStartID`

    The id of the corresponding `span.model_request_start` event.

  - `ManagedAgentsSpanModelUsage modelUsage`

    Token usage for a single model request.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

### Beta Managed Agents Span Model Request Start Event

- `ManagedAgentsSpanModelRequestStartEvent`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

### Beta Managed Agents Span Model Usage

- `ManagedAgentsSpanModelUsage`

  - `int cacheCreationInputTokens`

    Tokens used to create prompt cache in this request.

  - `int cacheReadInputTokens`

    Tokens read from prompt cache in this request.

  - `int inputTokens`

    Input tokens consumed by this request.

  - `int outputTokens`

    Output tokens generated by this request.

  - `?Speed speed`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

### Beta Managed Agents Span Outcome Evaluation End Event

- `ManagedAgentsSpanOutcomeEvaluationEndEvent`

  - `string id`

    Unique identifier for this event.

  - `string explanation`

    Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

  - `int iteration`

    0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

  - `string outcomeEvaluationStartID`

    The id of the corresponding `span.outcome_evaluation_start` event.

  - `string outcomeID`

    The `outc_` ID of the outcome being evaluated.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `string result`

    Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

  - `Type type`

  - `ManagedAgentsSpanModelUsage usage`

    Token usage for a single model request.

### Beta Managed Agents Span Outcome Evaluation Ongoing Event

- `ManagedAgentsSpanOutcomeEvaluationOngoingEvent`

  - `string id`

    Unique identifier for this event.

  - `int iteration`

    0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

  - `string outcomeID`

    The `outc_` ID of the outcome being evaluated.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

### Beta Managed Agents Span Outcome Evaluation Start Event

- `ManagedAgentsSpanOutcomeEvaluationStartEvent`

  - `string id`

    Unique identifier for this event.

  - `int iteration`

    0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

  - `string outcomeID`

    The `outc_` ID of the outcome being evaluated.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

### Beta Managed Agents Stream Session Events

- `ManagedAgentsStreamSessionEvents`

  - `ManagedAgentsUserMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of content blocks comprising the user message.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `ManagedAgentsUserInterruptEvent`

    - `string id`

      Unique identifier for this event.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `ManagedAgentsUserToolConfirmationEvent`

    - `string id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

    - `string toolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?string denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `ManagedAgentsUserCustomToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string customToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `ManagedAgentsAgentCustomToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the custom tool being called.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `ManagedAgentsAgentMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<ManagedAgentsTextBlock> content`

      Array of text blocks comprising the agent response.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsAgentThinkingEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsAgentMCPToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string mcpServerName`

      Name of the MCP server providing the tool.

    - `string name`

      Name of the MCP tool being used.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `ManagedAgentsAgentMCPToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string mcpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `ManagedAgentsAgentToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the agent tool being used.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `ManagedAgentsAgentToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `ManagedAgentsAgentThreadMessageReceivedEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `string fromSessionThreadID`

      Public `sthr_` ID of the thread that sent the message.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?string fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `ManagedAgentsAgentThreadMessageSentEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string toSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type type`

    - `?string toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `ManagedAgentsAgentThreadContextCompactedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionErrorEvent`

    - `string id`

      Unique identifier for this event.

    - `Error error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusRescheduledEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusRunningEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusIdleEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

    - `Type type`

  - `ManagedAgentsSessionStatusTerminatedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionThreadCreatedEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the callable agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public `sthr_` ID of the newly created thread.

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationStartEvent`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationEndEvent`

    - `string id`

      Unique identifier for this event.

    - `string explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type type`

    - `ManagedAgentsSpanModelUsage usage`

      Token usage for a single model request.

  - `ManagedAgentsSpanModelRequestStartEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanModelRequestEndEvent`

    - `string id`

      Unique identifier for this event.

    - `?bool isError`

      Whether the model request resulted in an error.

    - `string modelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `ManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsUserDefineOutcomeEvent`

    - `string id`

      Unique identifier for this event.

    - `string description`

      What the agent should produce. Copied from the input event.

    - `?int maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `string outcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

    - `Type type`

  - `ManagedAgentsSessionDeletedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionThreadStatusRunningEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that started running.

    - `Type type`

  - `ManagedAgentsSessionThreadStatusIdleEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

    - `Type type`

  - `ManagedAgentsSessionThreadStatusTerminatedEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that terminated.

    - `Type type`

  - `BetaManagedAgentsUserToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `ManagedAgentsSessionThreadStatusRescheduledEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that is retrying.

    - `Type type`

  - `BetaManagedAgentsSessionUpdatedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?BetaManagedAgentsSessionAgent agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `?array<string,string> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `?string title`

      The session's new title. Present only when the update changed it.

  - `BetaManagedAgentsStartEvent`

    - `BetaManagedAgentsStartEventPreview event`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

    - `Type type`

  - `BetaManagedAgentsDeltaEvent`

    - `BetaManagedAgentsDeltaContent delta`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

    - `string eventID`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `Type type`

  - `BetaManagedAgentsSystemMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

### Beta Managed Agents System Message Event Params

- `ManagedAgentsSystemMessageEventParams`

  - `list<BetaManagedAgentsSystemContentBlock> content`

    System content blocks to append. Text-only.

  - `Type type`

### Beta Managed Agents Text Block

- `ManagedAgentsTextBlock`

  - `string text`

    The text content.

  - `Type type`

### Beta Managed Agents Text Rubric

- `ManagedAgentsTextRubric`

  - `string content`

    Rubric content. Plain text or markdown — the grader treats it as freeform text.

  - `Type type`

### Beta Managed Agents Text Rubric Params

- `ManagedAgentsTextRubricParams`

  - `string content`

    Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

  - `Type type`

### Beta Managed Agents Unknown Error

- `ManagedAgentsUnknownError`

  - `string message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

  - `Type type`

### Beta Managed Agents URL Document Source

- `ManagedAgentsURLDocumentSource`

  - `Type type`

  - `string url`

    URL of the document to fetch.

### Beta Managed Agents URL Image Source

- `ManagedAgentsURLImageSource`

  - `Type type`

  - `string url`

    URL of the image to fetch.

### Beta Managed Agents User Custom Tool Result Event

- `ManagedAgentsUserCustomToolResultEvent`

  - `string id`

    Unique identifier for this event.

  - `string customToolUseID`

    The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `Type type`

  - `?list<Content> content`

    The result content returned by the tool.

  - `?bool isError`

    Whether the tool execution resulted in an error.

  - `?\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `?string sessionThreadID`

    Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

### Beta Managed Agents User Custom Tool Result Event Params

- `ManagedAgentsUserCustomToolResultEventParams`

  - `string customToolUseID`

    The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `Type type`

  - `?list<Content> content`

    The result content returned by the tool.

  - `?bool isError`

    Whether the tool execution resulted in an error.

### Beta Managed Agents User Define Outcome Event

- `ManagedAgentsUserDefineOutcomeEvent`

  - `string id`

    Unique identifier for this event.

  - `string description`

    What the agent should produce. Copied from the input event.

  - `?int maxIterations`

    Evaluate-then-revise cycles before giving up. Default 3, max 20.

  - `string outcomeID`

    Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `Rubric rubric`

    Rubric for grading the quality of an outcome.

  - `Type type`

### Beta Managed Agents User Define Outcome Event Params

- `ManagedAgentsUserDefineOutcomeEventParams`

  - `string description`

    What the agent should produce. This is the task specification.

  - `Rubric rubric`

    Rubric for grading the quality of an outcome.

  - `Type type`

  - `?int maxIterations`

    Eval→revision cycles before giving up. Default 3, max 20.

### Beta Managed Agents User Interrupt Event

- `ManagedAgentsUserInterruptEvent`

  - `string id`

    Unique identifier for this event.

  - `Type type`

  - `?\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `?string sessionThreadID`

    If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

### Beta Managed Agents User Interrupt Event Params

- `ManagedAgentsUserInterruptEventParams`

  - `Type type`

  - `?string sessionThreadID`

    If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

### Beta Managed Agents User Message Event

- `ManagedAgentsUserMessageEvent`

  - `string id`

    Unique identifier for this event.

  - `list<Content> content`

    Array of content blocks comprising the user message.

  - `Type type`

  - `?\Datetime processedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Message Event Params

- `ManagedAgentsUserMessageEventParams`

  - `list<Content> content`

    Array of content blocks for the user message.

  - `Type type`

### Beta Managed Agents User Tool Confirmation Event

- `ManagedAgentsUserToolConfirmationEvent`

  - `string id`

    Unique identifier for this event.

  - `Result result`

    UserToolConfirmationResult enum

  - `string toolUseID`

    The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `Type type`

  - `?string denyMessage`

    Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

  - `?\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `?string sessionThreadID`

    When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

### Beta Managed Agents User Tool Confirmation Event Params

- `ManagedAgentsUserToolConfirmationEventParams`

  - `Result result`

    UserToolConfirmationResult enum

  - `string toolUseID`

    The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `Type type`

  - `?string denyMessage`

    Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

### Beta Managed Agents User Tool Result Event Params

- `ManagedAgentsUserToolResultEventParams`

  - `string toolUseID`

    The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `Type type`

  - `?list<Content> content`

    The result content returned by the tool.

  - `?bool isError`

    Whether the tool execution resulted in an error.

# Resources

## Add Session Resource

`$client->beta->sessions->resources->add(string sessionID, string fileID, Type type, ?string mountPath, ?list<AnthropicBeta> betas): ManagedAgentsFileResource`

**post** `/v1/sessions/{session_id}/resources`

Add Session Resource

### Parameters

- `sessionID: string`

- `fileID: string`

  ID of a previously uploaded file.

- `type: Type`

- `mountPath?:optional string`

  Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsFileResource`

  - `string id`

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string fileID`

  - `string mountPath`

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsFileResource = $client->beta->sessions->resources->add(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  fileID: 'file_011CNha8iCJcU1wXNR6q4V8w',
  type: 'file',
  mountPath: '/uploads/receipt.pdf',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsFileResource);
```

#### Response

```json
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "created_at": "2026-03-15T10:00:00Z",
  "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "mount_path": "/uploads/receipt.pdf",
  "type": "file",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## List Session Resources

`$client->beta->sessions->resources->list(string sessionID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<ManagedAgentsSessionResource>`

**get** `/v1/sessions/{session_id}/resources`

List Session Resources

### Parameters

- `sessionID: string`

- `limit?:optional int`

  Maximum number of resources to return per page (max 1000). If omitted, returns all resources.

- `page?:optional string`

  Opaque cursor from a previous response's next_page field.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsSessionResource`

  - `ManagedAgentsGitHubRepositoryResource`

    - `string id`

    - `\Datetime createdAt`

      A timestamp in RFC 3339 format

    - `string mountPath`

    - `Type type`

    - `\Datetime updatedAt`

      A timestamp in RFC 3339 format

    - `string url`

    - `?Checkout checkout`

  - `ManagedAgentsFileResource`

    - `string id`

    - `\Datetime createdAt`

      A timestamp in RFC 3339 format

    - `string fileID`

    - `string mountPath`

    - `Type type`

    - `\Datetime updatedAt`

      A timestamp in RFC 3339 format

  - `ManagedAgentsMemoryStoreResource`

    - `string memoryStoreID`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `Type type`

    - `?Access access`

      Access mode for an attached memory store.

    - `?string description`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `?string instructions`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `?string mountPath`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `?string name`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->sessions->resources->list(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  limit: 0,
  page: 'page',
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

#### Response

```json
{
  "data": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Session Resource

`$client->beta->sessions->resources->retrieve(string resourceID, string sessionID, ?list<AnthropicBeta> betas): ResourceGetResponse`

**get** `/v1/sessions/{session_id}/resources/{resource_id}`

Get Session Resource

### Parameters

- `sessionID: string`

- `resourceID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ResourceGetResponse`

  - `ManagedAgentsGitHubRepositoryResource`

    - `string id`

    - `\Datetime createdAt`

      A timestamp in RFC 3339 format

    - `string mountPath`

    - `Type type`

    - `\Datetime updatedAt`

      A timestamp in RFC 3339 format

    - `string url`

    - `?Checkout checkout`

  - `ManagedAgentsFileResource`

    - `string id`

    - `\Datetime createdAt`

      A timestamp in RFC 3339 format

    - `string fileID`

    - `string mountPath`

    - `Type type`

    - `\Datetime updatedAt`

      A timestamp in RFC 3339 format

  - `ManagedAgentsMemoryStoreResource`

    - `string memoryStoreID`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `Type type`

    - `?Access access`

      Access mode for an attached memory store.

    - `?string description`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `?string instructions`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `?string mountPath`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `?string name`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$resource = $client->beta->sessions->resources->retrieve(
  'sesrsc_011CZkZBJq5dWxk9fVLNcPht',
  sessionID: 'sesn_011CZkZAtmR3yMPDzynEDxu7',
  betas: ['message-batches-2024-09-24'],
);

var_dump($resource);
```

#### Response

```json
{
  "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
  "created_at": "2026-03-15T10:00:00Z",
  "mount_path": "/workspace/example-repo",
  "type": "github_repository",
  "updated_at": "2026-03-15T10:00:00Z",
  "url": "https://github.com/example-org/example-repo",
  "checkout": {
    "name": "main",
    "type": "branch"
  }
}
```

## Update Session Resource

`$client->beta->sessions->resources->update(string resourceID, string sessionID, string authorizationToken, ?list<AnthropicBeta> betas): ResourceUpdateResponse`

**post** `/v1/sessions/{session_id}/resources/{resource_id}`

Update Session Resource

### Parameters

- `sessionID: string`

- `resourceID: string`

- `authorizationToken: string`

  New authorization token for the resource. Currently only `github_repository` resources support token rotation.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ResourceUpdateResponse`

  - `ManagedAgentsGitHubRepositoryResource`

    - `string id`

    - `\Datetime createdAt`

      A timestamp in RFC 3339 format

    - `string mountPath`

    - `Type type`

    - `\Datetime updatedAt`

      A timestamp in RFC 3339 format

    - `string url`

    - `?Checkout checkout`

  - `ManagedAgentsFileResource`

    - `string id`

    - `\Datetime createdAt`

      A timestamp in RFC 3339 format

    - `string fileID`

    - `string mountPath`

    - `Type type`

    - `\Datetime updatedAt`

      A timestamp in RFC 3339 format

  - `ManagedAgentsMemoryStoreResource`

    - `string memoryStoreID`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `Type type`

    - `?Access access`

      Access mode for an attached memory store.

    - `?string description`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `?string instructions`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `?string mountPath`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `?string name`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$resource = $client->beta->sessions->resources->update(
  'sesrsc_011CZkZBJq5dWxk9fVLNcPht',
  sessionID: 'sesn_011CZkZAtmR3yMPDzynEDxu7',
  authorizationToken: 'ghp_exampletoken',
  betas: ['message-batches-2024-09-24'],
);

var_dump($resource);
```

#### Response

```json
{
  "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
  "created_at": "2026-03-15T10:00:00Z",
  "mount_path": "/workspace/example-repo",
  "type": "github_repository",
  "updated_at": "2026-03-15T10:00:00Z",
  "url": "https://github.com/example-org/example-repo",
  "checkout": {
    "name": "main",
    "type": "branch"
  }
}
```

## Delete Session Resource

`$client->beta->sessions->resources->delete(string resourceID, string sessionID, ?list<AnthropicBeta> betas): ManagedAgentsDeleteSessionResource`

**delete** `/v1/sessions/{session_id}/resources/{resource_id}`

Delete Session Resource

### Parameters

- `sessionID: string`

- `resourceID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsDeleteSessionResource`

  - `string id`

  - `Type type`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeleteSessionResource = $client
  ->beta
  ->sessions
  ->resources
  ->delete(
  'sesrsc_011CZkZBJq5dWxk9fVLNcPht',
  sessionID: 'sesn_011CZkZAtmR3yMPDzynEDxu7',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsDeleteSessionResource);
```

#### Response

```json
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "type": "session_resource_deleted"
}
```

## Domain Types

### Beta Managed Agents Delete Session Resource

- `ManagedAgentsDeleteSessionResource`

  - `string id`

  - `Type type`

### Beta Managed Agents File Resource

- `ManagedAgentsFileResource`

  - `string id`

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string fileID`

  - `string mountPath`

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents GitHub Repository Resource

- `ManagedAgentsGitHubRepositoryResource`

  - `string id`

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string mountPath`

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `string url`

  - `?Checkout checkout`

### Beta Managed Agents Memory Store Resource

- `ManagedAgentsMemoryStoreResource`

  - `string memoryStoreID`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `Type type`

  - `?Access access`

    Access mode for an attached memory store.

  - `?string description`

    Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

  - `?string instructions`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `?string mountPath`

    Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

  - `?string name`

    Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

### Beta Managed Agents Session Resource

- `ManagedAgentsSessionResource`

  - `ManagedAgentsGitHubRepositoryResource`

    - `string id`

    - `\Datetime createdAt`

      A timestamp in RFC 3339 format

    - `string mountPath`

    - `Type type`

    - `\Datetime updatedAt`

      A timestamp in RFC 3339 format

    - `string url`

    - `?Checkout checkout`

  - `ManagedAgentsFileResource`

    - `string id`

    - `\Datetime createdAt`

      A timestamp in RFC 3339 format

    - `string fileID`

    - `string mountPath`

    - `Type type`

    - `\Datetime updatedAt`

      A timestamp in RFC 3339 format

  - `ManagedAgentsMemoryStoreResource`

    - `string memoryStoreID`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `Type type`

    - `?Access access`

      Access mode for an attached memory store.

    - `?string description`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `?string instructions`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `?string mountPath`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `?string name`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

# Threads

## List Session Threads

`$client->beta->sessions->threads->list(string sessionID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<ManagedAgentsSessionThread>`

**get** `/v1/sessions/{session_id}/threads`

List Session Threads

### Parameters

- `sessionID: string`

- `limit?:optional int`

  Maximum results per page. Defaults to 1000.

- `page?:optional string`

  Opaque pagination cursor from a previous response's next_page. Forward-only.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsSessionThread`

  - `string id`

    Unique identifier for this thread.

  - `BetaManagedAgentsSessionThreadAgent agent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?string parentThreadID`

    Parent thread that spawned this thread. Null for the primary thread.

  - `string sessionID`

    The session this thread belongs to.

  - `?ManagedAgentsSessionThreadStats stats`

    Timing statistics for a session thread.

  - `ManagedAgentsSessionThreadStatus status`

    SessionThreadStatus enum

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `?ManagedAgentsSessionThreadUsage usage`

    Cumulative token usage for a session thread across all turns.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->sessions->threads->list(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  limit: 0,
  page: 'page',
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

#### Response

```json
{
  "data": [
    {
      "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
      "agent": {
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
        "description": "A focused research subagent.",
        "mcp_servers": [
          {
            "name": "example-mcp",
            "type": "url",
            "url": "https://example-server.modelcontextprotocol.io/sse"
          }
        ],
        "model": {
          "id": "claude-sonnet-4-6",
          "speed": "standard"
        },
        "name": "Researcher",
        "skills": [
          {
            "skill_id": "xlsx",
            "type": "anthropic",
            "version": "1"
          }
        ],
        "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
        "tools": [
          {
            "configs": [
              {
                "enabled": true,
                "name": "bash",
                "permission_policy": {
                  "type": "always_allow"
                }
              }
            ],
            "default_config": {
              "enabled": true,
              "permission_policy": {
                "type": "always_ask"
              }
            },
            "type": "agent_toolset_20260401"
          }
        ],
        "type": "agent",
        "version": 1
      },
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "parent_thread_id": null,
      "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
      "stats": {
        "active_seconds": 0,
        "duration_seconds": 0,
        "startup_seconds": 0
      },
      "status": "idle",
      "type": "session_thread",
      "updated_at": "2026-03-15T10:00:00Z",
      "usage": {
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 0
        },
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "output_tokens": 0
      }
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Session Thread

`$client->beta->sessions->threads->retrieve(string threadID, string sessionID, ?list<AnthropicBeta> betas): ManagedAgentsSessionThread`

**get** `/v1/sessions/{session_id}/threads/{thread_id}`

Get Session Thread

### Parameters

- `sessionID: string`

- `threadID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsSessionThread`

  - `string id`

    Unique identifier for this thread.

  - `BetaManagedAgentsSessionThreadAgent agent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?string parentThreadID`

    Parent thread that spawned this thread. Null for the primary thread.

  - `string sessionID`

    The session this thread belongs to.

  - `?ManagedAgentsSessionThreadStats stats`

    Timing statistics for a session thread.

  - `ManagedAgentsSessionThreadStatus status`

    SessionThreadStatus enum

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `?ManagedAgentsSessionThreadUsage usage`

    Cumulative token usage for a session thread across all turns.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsSessionThread = $client->beta->sessions->threads->retrieve(
  'sthr_011CZkZVWa6oIjw0rgXZpnBt',
  sessionID: 'sesn_011CZkZAtmR3yMPDzynEDxu7',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsSessionThread);
```

#### Response

```json
{
  "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "description": "A focused research subagent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-sonnet-4-6",
      "speed": "standard"
    },
    "name": "Researcher",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      }
    ],
    "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            }
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "parent_thread_id": null,
  "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0,
    "startup_seconds": 0
  },
  "status": "idle",
  "type": "session_thread",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

## Archive Session Thread

`$client->beta->sessions->threads->archive(string threadID, string sessionID, ?list<AnthropicBeta> betas): ManagedAgentsSessionThread`

**post** `/v1/sessions/{session_id}/threads/{thread_id}/archive`

Archive Session Thread

### Parameters

- `sessionID: string`

- `threadID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsSessionThread`

  - `string id`

    Unique identifier for this thread.

  - `BetaManagedAgentsSessionThreadAgent agent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?string parentThreadID`

    Parent thread that spawned this thread. Null for the primary thread.

  - `string sessionID`

    The session this thread belongs to.

  - `?ManagedAgentsSessionThreadStats stats`

    Timing statistics for a session thread.

  - `ManagedAgentsSessionThreadStatus status`

    SessionThreadStatus enum

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `?ManagedAgentsSessionThreadUsage usage`

    Cumulative token usage for a session thread across all turns.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsSessionThread = $client->beta->sessions->threads->archive(
  'sthr_011CZkZVWa6oIjw0rgXZpnBt',
  sessionID: 'sesn_011CZkZAtmR3yMPDzynEDxu7',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsSessionThread);
```

#### Response

```json
{
  "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "description": "A focused research subagent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-sonnet-4-6",
      "speed": "standard"
    },
    "name": "Researcher",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      }
    ],
    "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            }
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "parent_thread_id": null,
  "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0,
    "startup_seconds": 0
  },
  "status": "idle",
  "type": "session_thread",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

## Domain Types

### Beta Managed Agents Session Thread

- `ManagedAgentsSessionThread`

  - `string id`

    Unique identifier for this thread.

  - `BetaManagedAgentsSessionThreadAgent agent`

    Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?string parentThreadID`

    Parent thread that spawned this thread. Null for the primary thread.

  - `string sessionID`

    The session this thread belongs to.

  - `?ManagedAgentsSessionThreadStats stats`

    Timing statistics for a session thread.

  - `ManagedAgentsSessionThreadStatus status`

    SessionThreadStatus enum

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `?ManagedAgentsSessionThreadUsage usage`

    Cumulative token usage for a session thread across all turns.

### Beta Managed Agents Session Thread Stats

- `ManagedAgentsSessionThreadStats`

  - `?float activeSeconds`

    Cumulative time in seconds the thread spent actively running. Excludes idle time.

  - `?float durationSeconds`

    Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

  - `?float startupSeconds`

    Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

### Beta Managed Agents Session Thread Status

- `ManagedAgentsSessionThreadStatus`

  - `"running"`

  - `"idle"`

  - `"rescheduling"`

  - `"terminated"`

### Beta Managed Agents Session Thread Usage

- `ManagedAgentsSessionThreadUsage`

  - `?BetaManagedAgentsCacheCreationUsage cacheCreation`

    Prompt-cache creation token usage broken down by cache lifetime.

  - `?int cacheReadInputTokens`

    Total tokens read from prompt cache.

  - `?int inputTokens`

    Total input tokens consumed across all turns.

  - `?int outputTokens`

    Total output tokens generated across all turns.

### Beta Managed Agents Stream Session Thread Events

- `ManagedAgentsStreamSessionThreadEvents`

  - `ManagedAgentsUserMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of content blocks comprising the user message.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `ManagedAgentsUserInterruptEvent`

    - `string id`

      Unique identifier for this event.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `ManagedAgentsUserToolConfirmationEvent`

    - `string id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

    - `string toolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?string denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `ManagedAgentsUserCustomToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string customToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `ManagedAgentsAgentCustomToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the custom tool being called.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `ManagedAgentsAgentMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<ManagedAgentsTextBlock> content`

      Array of text blocks comprising the agent response.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsAgentThinkingEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsAgentMCPToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string mcpServerName`

      Name of the MCP server providing the tool.

    - `string name`

      Name of the MCP tool being used.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `ManagedAgentsAgentMCPToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string mcpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `ManagedAgentsAgentToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the agent tool being used.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `ManagedAgentsAgentToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `ManagedAgentsAgentThreadMessageReceivedEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `string fromSessionThreadID`

      Public `sthr_` ID of the thread that sent the message.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?string fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `ManagedAgentsAgentThreadMessageSentEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string toSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type type`

    - `?string toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `ManagedAgentsAgentThreadContextCompactedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionErrorEvent`

    - `string id`

      Unique identifier for this event.

    - `Error error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusRescheduledEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusRunningEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusIdleEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

    - `Type type`

  - `ManagedAgentsSessionStatusTerminatedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionThreadCreatedEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the callable agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public `sthr_` ID of the newly created thread.

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationStartEvent`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationEndEvent`

    - `string id`

      Unique identifier for this event.

    - `string explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type type`

    - `ManagedAgentsSpanModelUsage usage`

      Token usage for a single model request.

  - `ManagedAgentsSpanModelRequestStartEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanModelRequestEndEvent`

    - `string id`

      Unique identifier for this event.

    - `?bool isError`

      Whether the model request resulted in an error.

    - `string modelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `ManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsUserDefineOutcomeEvent`

    - `string id`

      Unique identifier for this event.

    - `string description`

      What the agent should produce. Copied from the input event.

    - `?int maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `string outcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

    - `Type type`

  - `ManagedAgentsSessionDeletedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionThreadStatusRunningEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that started running.

    - `Type type`

  - `ManagedAgentsSessionThreadStatusIdleEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

    - `Type type`

  - `ManagedAgentsSessionThreadStatusTerminatedEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that terminated.

    - `Type type`

  - `BetaManagedAgentsUserToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `ManagedAgentsSessionThreadStatusRescheduledEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that is retrying.

    - `Type type`

  - `BetaManagedAgentsSessionUpdatedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?BetaManagedAgentsSessionAgent agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `?array<string,string> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `?string title`

      The session's new title. Present only when the update changed it.

  - `BetaManagedAgentsStartEvent`

    - `BetaManagedAgentsStartEventPreview event`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

    - `Type type`

  - `BetaManagedAgentsDeltaEvent`

    - `BetaManagedAgentsDeltaContent delta`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

    - `string eventID`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `Type type`

  - `BetaManagedAgentsSystemMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

# Events

## List Session Thread Events

`$client->beta->sessions->threads->events->list(string threadID, string sessionID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<ManagedAgentsSessionEvent>`

**get** `/v1/sessions/{session_id}/threads/{thread_id}/events`

List Session Thread Events

### Parameters

- `sessionID: string`

- `threadID: string`

- `limit?:optional int`

  Query parameter for limit

- `page?:optional string`

  Query parameter for page

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsSessionEvent`

  - `ManagedAgentsUserMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of content blocks comprising the user message.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `ManagedAgentsUserInterruptEvent`

    - `string id`

      Unique identifier for this event.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `ManagedAgentsUserToolConfirmationEvent`

    - `string id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

    - `string toolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?string denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `ManagedAgentsUserCustomToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string customToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `ManagedAgentsAgentCustomToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the custom tool being called.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `ManagedAgentsAgentMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<ManagedAgentsTextBlock> content`

      Array of text blocks comprising the agent response.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsAgentThinkingEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsAgentMCPToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string mcpServerName`

      Name of the MCP server providing the tool.

    - `string name`

      Name of the MCP tool being used.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `ManagedAgentsAgentMCPToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string mcpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `ManagedAgentsAgentToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the agent tool being used.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `ManagedAgentsAgentToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `ManagedAgentsAgentThreadMessageReceivedEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `string fromSessionThreadID`

      Public `sthr_` ID of the thread that sent the message.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?string fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `ManagedAgentsAgentThreadMessageSentEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string toSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type type`

    - `?string toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `ManagedAgentsAgentThreadContextCompactedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionErrorEvent`

    - `string id`

      Unique identifier for this event.

    - `Error error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusRescheduledEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusRunningEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusIdleEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

    - `Type type`

  - `ManagedAgentsSessionStatusTerminatedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionThreadCreatedEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the callable agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public `sthr_` ID of the newly created thread.

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationStartEvent`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationEndEvent`

    - `string id`

      Unique identifier for this event.

    - `string explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type type`

    - `ManagedAgentsSpanModelUsage usage`

      Token usage for a single model request.

  - `ManagedAgentsSpanModelRequestStartEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanModelRequestEndEvent`

    - `string id`

      Unique identifier for this event.

    - `?bool isError`

      Whether the model request resulted in an error.

    - `string modelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `ManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsUserDefineOutcomeEvent`

    - `string id`

      Unique identifier for this event.

    - `string description`

      What the agent should produce. Copied from the input event.

    - `?int maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `string outcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

    - `Type type`

  - `ManagedAgentsSessionDeletedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionThreadStatusRunningEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that started running.

    - `Type type`

  - `ManagedAgentsSessionThreadStatusIdleEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

    - `Type type`

  - `ManagedAgentsSessionThreadStatusTerminatedEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that terminated.

    - `Type type`

  - `BetaManagedAgentsUserToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `ManagedAgentsSessionThreadStatusRescheduledEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that is retrying.

    - `Type type`

  - `BetaManagedAgentsSessionUpdatedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?BetaManagedAgentsSessionAgent agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `?array<string,string> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `?string title`

      The session's new title. Present only when the update changed it.

  - `BetaManagedAgentsSystemMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->sessions->threads->events->list(
  'sthr_011CZkZVWa6oIjw0rgXZpnBt',
  sessionID: 'sesn_011CZkZAtmR3yMPDzynEDxu7',
  limit: 0,
  page: 'page',
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

#### Response

```json
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "next_page"
}
```

## Stream Session Thread Events

`$client->beta->sessions->threads->events->stream(string threadID, string sessionID, ?list<AnthropicBeta> betas): ManagedAgentsStreamSessionThreadEvents`

**get** `/v1/sessions/{session_id}/threads/{thread_id}/stream`

Stream Session Thread Events

### Parameters

- `sessionID: string`

- `threadID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsStreamSessionThreadEvents`

  - `ManagedAgentsUserMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of content blocks comprising the user message.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `ManagedAgentsUserInterruptEvent`

    - `string id`

      Unique identifier for this event.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `ManagedAgentsUserToolConfirmationEvent`

    - `string id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

    - `string toolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?string denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `ManagedAgentsUserCustomToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string customToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `ManagedAgentsAgentCustomToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the custom tool being called.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `ManagedAgentsAgentMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<ManagedAgentsTextBlock> content`

      Array of text blocks comprising the agent response.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsAgentThinkingEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsAgentMCPToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string mcpServerName`

      Name of the MCP server providing the tool.

    - `string name`

      Name of the MCP tool being used.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `ManagedAgentsAgentMCPToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string mcpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `ManagedAgentsAgentToolUseEvent`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the agent tool being used.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `ManagedAgentsAgentToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `ManagedAgentsAgentThreadMessageReceivedEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `string fromSessionThreadID`

      Public `sthr_` ID of the thread that sent the message.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?string fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `ManagedAgentsAgentThreadMessageSentEvent`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string toSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type type`

    - `?string toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `ManagedAgentsAgentThreadContextCompactedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionErrorEvent`

    - `string id`

      Unique identifier for this event.

    - `Error error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusRescheduledEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusRunningEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionStatusIdleEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

    - `Type type`

  - `ManagedAgentsSessionStatusTerminatedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionThreadCreatedEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the callable agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public `sthr_` ID of the newly created thread.

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationStartEvent`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationEndEvent`

    - `string id`

      Unique identifier for this event.

    - `string explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type type`

    - `ManagedAgentsSpanModelUsage usage`

      Token usage for a single model request.

  - `ManagedAgentsSpanModelRequestStartEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanModelRequestEndEvent`

    - `string id`

      Unique identifier for this event.

    - `?bool isError`

      Whether the model request resulted in an error.

    - `string modelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `ManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsUserDefineOutcomeEvent`

    - `string id`

      Unique identifier for this event.

    - `string description`

      What the agent should produce. Copied from the input event.

    - `?int maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `string outcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

    - `Type type`

  - `ManagedAgentsSessionDeletedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `ManagedAgentsSessionThreadStatusRunningEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that started running.

    - `Type type`

  - `ManagedAgentsSessionThreadStatusIdleEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

    - `Type type`

  - `ManagedAgentsSessionThreadStatusTerminatedEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that terminated.

    - `Type type`

  - `BetaManagedAgentsUserToolResultEvent`

    - `string id`

      Unique identifier for this event.

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `ManagedAgentsSessionThreadStatusRescheduledEvent`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that is retrying.

    - `Type type`

  - `BetaManagedAgentsSessionUpdatedEvent`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

    - `?BetaManagedAgentsSessionAgent agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `?array<string,string> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `?string title`

      The session's new title. Present only when the update changed it.

  - `BetaManagedAgentsStartEvent`

    - `BetaManagedAgentsStartEventPreview event`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

    - `Type type`

  - `BetaManagedAgentsDeltaEvent`

    - `BetaManagedAgentsDeltaContent delta`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

    - `string eventID`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `Type type`

  - `BetaManagedAgentsSystemMessageEvent`

    - `string id`

      Unique identifier for this event.

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

    - `Type type`

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsStreamSessionThreadEvents = $client
  ->beta
  ->sessions
  ->threads
  ->events
  ->streamStream(
  'sthr_011CZkZVWa6oIjw0rgXZpnBt',
  sessionID: 'sesn_011CZkZAtmR3yMPDzynEDxu7',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsStreamSessionThreadEvents);
```

#### Response

```json
{
  "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
  "content": [
    {
      "text": "Where is my order #1234?",
      "type": "text"
    }
  ],
  "type": "user.message",
  "processed_at": "2026-03-15T10:00:00Z"
}
```

# Deployments

## Create Deployment

`$client->beta->deployments->create(Agent agent, string environmentID, list<BetaManagedAgentsDeploymentInitialEventParams> initialEvents, string name, ?string description, ?array<string,string> metadata, ?list<Resource> resources, ?BetaManagedAgentsScheduleParams schedule, ?list<string> vaultIDs, ?list<AnthropicBeta> betas): BetaManagedAgentsDeployment`

**post** `/v1/deployments`

Create Deployment

### Parameters

- `agent: Agent`

  Agent to deploy. Accepts the `agent` ID string, which pins the latest version, or an `agent` object with both id and version specified. The agent must exist and not be archived.

- `environmentID: string`

  ID of the `environment` defining the container configuration for sessions created from this deployment.

- `initialEvents: list<BetaManagedAgentsDeploymentInitialEventParams>`

  Events to send to each session immediately after creation. At least 1, maximum 50.

- `name: string`

  Human-readable name for the deployment.

- `description?:optional string`

  Description of what the deployment does.

- `metadata?:optional array<string,string>`

  Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `resources?:optional list<Resource>`

  Resources (e.g. repositories, files) to mount into each session's container. Maximum 500.

- `schedule?:optional BetaManagedAgentsScheduleParams`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

- `vaultIDs?:optional list<string>`

  Vault IDs for stored credentials the agent can use during sessions created from this deployment. Maximum 50.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsDeployment`

  - `string id`

    Unique identifier for this deployment.

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?string description`

    Description of what the deployment does.

  - `string environmentID`

    ID of the `environment` where sessions run.

  - `list<BetaManagedAgentsDeploymentInitialEvent> initialEvents`

    Events sent to each session immediately after creation.

  - `array<string,string> metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `string name`

    Human-readable name.

  - `?BetaManagedAgentsDeploymentPausedReason pausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

  - `list<BetaManagedAgentsSessionResourceConfig> resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

  - `?BetaManagedAgentsSchedule schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

  - `BetaManagedAgentsDeploymentStatus status`

    Lifecycle status of a deployment.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `list<string> vaultIDs`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeployment = $client->beta->deployments->create(
  agent: 'string',
  environmentID: 'x',
  initialEvents: [
    [
      'content' => [['text' => 'Where is my order #1234?', 'type' => 'text']],
      'type' => 'user.message',
    ],
  ],
  name: 'x',
  description: 'description',
  metadata: ['foo' => 'string'],
  resources: [
    [
      'fileID' => 'file_011CNha8iCJcU1wXNR6q4V8w',
      'type' => 'file',
      'mountPath' => '/uploads/receipt.pdf',
    ],
  ],
  schedule: [
    'expression' => '0 9 * * 1-5',
    'timezone' => 'America/Los_Angeles',
    'type' => 'cron',
  ],
  vaultIDs: ['string'],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsDeployment);
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

## List Deployments

`$client->beta->deployments->list(?string agentID, ?\Datetime createdAtGte, ?\Datetime createdAtLte, ?bool includeArchived, ?int limit, ?string page, ?BetaManagedAgentsDeploymentStatus status, ?list<AnthropicBeta> betas): PageCursor<BetaManagedAgentsDeployment>`

**get** `/v1/deployments`

List Deployments

### Parameters

- `agentID?:optional string`

  Filter by agent ID.

- `createdAtGte?:optional \Datetime`

  Return deployments created at or after this time (inclusive).

- `createdAtLte?:optional \Datetime`

  Return deployments created at or before this time (inclusive).

- `includeArchived?:optional bool`

  When true, includes archived deployments. Default: false (exclude archived).

- `limit?:optional int`

  Maximum results per page. Default 20, maximum 100.

- `page?:optional string`

  Opaque pagination cursor.

- `status?:optional BetaManagedAgentsDeploymentStatus`

  Filter by status: active or paused. Omit for both. To include archived deployments, use include_archived instead; the two cannot be combined.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsDeployment`

  - `string id`

    Unique identifier for this deployment.

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?string description`

    Description of what the deployment does.

  - `string environmentID`

    ID of the `environment` where sessions run.

  - `list<BetaManagedAgentsDeploymentInitialEvent> initialEvents`

    Events sent to each session immediately after creation.

  - `array<string,string> metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `string name`

    Human-readable name.

  - `?BetaManagedAgentsDeploymentPausedReason pausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

  - `list<BetaManagedAgentsSessionResourceConfig> resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

  - `?BetaManagedAgentsSchedule schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

  - `BetaManagedAgentsDeploymentStatus status`

    Lifecycle status of a deployment.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `list<string> vaultIDs`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->deployments->list(
  agentID: 'agent_id',
  createdAtGte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  includeArchived: true,
  limit: 0,
  page: 'page',
  status: BetaManagedAgentsDeploymentStatus::ACTIVE,
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

#### Response

```json
{
  "data": [
    {
      "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
      "agent": {
        "id": "agent_011CZkYpogX7uDKUyvBTophP",
        "type": "agent",
        "version": 1
      },
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "description": "Compiles yesterday's orders into a report every weekday morning.",
      "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
      "initial_events": [
        {
          "content": [
            {
              "text": "Compile yesterday's orders into report.md.",
              "type": "text"
            }
          ],
          "type": "user.message"
        }
      ],
      "metadata": {},
      "name": "Daily order report",
      "paused_reason": {
        "type": "manual"
      },
      "resources": [
        {
          "type": "github_repository",
          "url": "url",
          "checkout": {
            "name": "main",
            "type": "branch"
          },
          "mount_path": "mount_path"
        }
      ],
      "schedule": {
        "expression": "0 9 * * 1-5",
        "timezone": "America/Los_Angeles",
        "type": "cron",
        "last_run_at": "2026-03-16T16:00:09Z",
        "upcoming_runs_at": [
          "2026-03-17T16:00:00Z",
          "2026-03-18T16:00:00Z"
        ]
      },
      "status": "active",
      "type": "deployment",
      "updated_at": "2026-03-15T10:00:00Z",
      "vault_ids": [
        "vlt_011CZkZDLs7fYzm1hXNPeRjv"
      ]
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Deployment

`$client->beta->deployments->retrieve(string deploymentID, ?list<AnthropicBeta> betas): BetaManagedAgentsDeployment`

**get** `/v1/deployments/{deployment_id}`

Get Deployment

### Parameters

- `deploymentID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsDeployment`

  - `string id`

    Unique identifier for this deployment.

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?string description`

    Description of what the deployment does.

  - `string environmentID`

    ID of the `environment` where sessions run.

  - `list<BetaManagedAgentsDeploymentInitialEvent> initialEvents`

    Events sent to each session immediately after creation.

  - `array<string,string> metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `string name`

    Human-readable name.

  - `?BetaManagedAgentsDeploymentPausedReason pausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

  - `list<BetaManagedAgentsSessionResourceConfig> resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

  - `?BetaManagedAgentsSchedule schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

  - `BetaManagedAgentsDeploymentStatus status`

    Lifecycle status of a deployment.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `list<string> vaultIDs`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeployment = $client->beta->deployments->retrieve(
  'depl_011CZkZcDH3vPqd7xnEfwTai', betas: ['message-batches-2024-09-24']
);

var_dump($betaManagedAgentsDeployment);
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

## Update Deployment

`$client->beta->deployments->update(string deploymentID, ?Agent agent, ?string description, ?string environmentID, ?list<BetaManagedAgentsDeploymentInitialEventParams> initialEvents, ?array<string,string> metadata, ?string name, ?list<Resource> resources, ?BetaManagedAgentsScheduleParams schedule, ?list<string> vaultIDs, ?list<AnthropicBeta> betas): BetaManagedAgentsDeployment`

**post** `/v1/deployments/{deployment_id}`

Update Deployment

### Parameters

- `deploymentID: string`

- `agent?:optional Agent`

  Agent to deploy. Accepts the `agent` ID string, which re-pins to the latest version, or an `agent` object with both id and version specified. Omit to preserve. Cannot be cleared.

- `description?:optional string`

  Description. Omit to preserve; send empty string or null to clear.

- `environmentID?:optional string`

  ID of the `environment` where sessions run. Omit to preserve. Cannot be cleared.

- `initialEvents?:optional list<BetaManagedAgentsDeploymentInitialEventParams>`

  Initial events. Full replacement. Omit to preserve. Cannot be cleared. At least 1, maximum 50.

- `metadata?:optional array<string,string>`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `name?:optional string`

  Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

- `resources?:optional list<Resource>`

  Session resources. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 500.

- `schedule?:optional BetaManagedAgentsScheduleParams`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

- `vaultIDs?:optional list<string>`

  Vault IDs. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 50.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsDeployment`

  - `string id`

    Unique identifier for this deployment.

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?string description`

    Description of what the deployment does.

  - `string environmentID`

    ID of the `environment` where sessions run.

  - `list<BetaManagedAgentsDeploymentInitialEvent> initialEvents`

    Events sent to each session immediately after creation.

  - `array<string,string> metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `string name`

    Human-readable name.

  - `?BetaManagedAgentsDeploymentPausedReason pausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

  - `list<BetaManagedAgentsSessionResourceConfig> resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

  - `?BetaManagedAgentsSchedule schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

  - `BetaManagedAgentsDeploymentStatus status`

    Lifecycle status of a deployment.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `list<string> vaultIDs`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeployment = $client->beta->deployments->update(
  'depl_011CZkZcDH3vPqd7xnEfwTai',
  agent: 'string',
  description: 'description',
  environmentID: 'environment_id',
  initialEvents: [
    [
      'content' => [['text' => 'Where is my order #1234?', 'type' => 'text']],
      'type' => 'user.message',
    ],
  ],
  metadata: ['foo' => 'string'],
  name: 'name',
  resources: [
    [
      'fileID' => 'file_011CNha8iCJcU1wXNR6q4V8w',
      'type' => 'file',
      'mountPath' => '/uploads/receipt.pdf',
    ],
  ],
  schedule: [
    'expression' => '0 9 * * 1-5',
    'timezone' => 'America/Los_Angeles',
    'type' => 'cron',
  ],
  vaultIDs: ['string'],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsDeployment);
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

## Archive Deployment

`$client->beta->deployments->archive(string deploymentID, ?list<AnthropicBeta> betas): BetaManagedAgentsDeployment`

**post** `/v1/deployments/{deployment_id}/archive`

Archive Deployment

### Parameters

- `deploymentID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsDeployment`

  - `string id`

    Unique identifier for this deployment.

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?string description`

    Description of what the deployment does.

  - `string environmentID`

    ID of the `environment` where sessions run.

  - `list<BetaManagedAgentsDeploymentInitialEvent> initialEvents`

    Events sent to each session immediately after creation.

  - `array<string,string> metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `string name`

    Human-readable name.

  - `?BetaManagedAgentsDeploymentPausedReason pausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

  - `list<BetaManagedAgentsSessionResourceConfig> resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

  - `?BetaManagedAgentsSchedule schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

  - `BetaManagedAgentsDeploymentStatus status`

    Lifecycle status of a deployment.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `list<string> vaultIDs`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeployment = $client->beta->deployments->archive(
  'depl_011CZkZcDH3vPqd7xnEfwTai', betas: ['message-batches-2024-09-24']
);

var_dump($betaManagedAgentsDeployment);
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

## Run Deployment Now

`$client->beta->deployments->run(string deploymentID, ?list<AnthropicBeta> betas): BetaManagedAgentsDeploymentRun`

**post** `/v1/deployments/{deployment_id}/run`

Run Deployment Now

### Parameters

- `deploymentID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsDeploymentRun`

  - `string id`

    Unique identifier for this run (`drun_...`).

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string deploymentID`

    ID of the deployment that produced this run.

  - `?Error error`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

  - `?string sessionID`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `BetaManagedAgentsTriggerContext triggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

  - `Type type`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeploymentRun = $client->beta->deployments->run(
  'depl_011CZkZcDH3vPqd7xnEfwTai', betas: ['message-batches-2024-09-24']
);

var_dump($betaManagedAgentsDeploymentRun);
```

#### Response

```json
{
  "id": "id",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "type": "agent",
    "version": 1
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "deployment_id": "deployment_id",
  "error": {
    "message": "message",
    "type": "environment_archived_error"
  },
  "session_id": "session_id",
  "trigger_context": {
    "scheduled_at": "2019-12-27T18:11:19.117Z",
    "type": "schedule"
  },
  "type": "deployment_run"
}
```

## Pause Deployment

`$client->beta->deployments->pause(string deploymentID, ?list<AnthropicBeta> betas): BetaManagedAgentsDeployment`

**post** `/v1/deployments/{deployment_id}/pause`

Pause Deployment

### Parameters

- `deploymentID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsDeployment`

  - `string id`

    Unique identifier for this deployment.

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?string description`

    Description of what the deployment does.

  - `string environmentID`

    ID of the `environment` where sessions run.

  - `list<BetaManagedAgentsDeploymentInitialEvent> initialEvents`

    Events sent to each session immediately after creation.

  - `array<string,string> metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `string name`

    Human-readable name.

  - `?BetaManagedAgentsDeploymentPausedReason pausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

  - `list<BetaManagedAgentsSessionResourceConfig> resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

  - `?BetaManagedAgentsSchedule schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

  - `BetaManagedAgentsDeploymentStatus status`

    Lifecycle status of a deployment.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `list<string> vaultIDs`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeployment = $client->beta->deployments->pause(
  'depl_011CZkZcDH3vPqd7xnEfwTai', betas: ['message-batches-2024-09-24']
);

var_dump($betaManagedAgentsDeployment);
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

## Unpause Deployment

`$client->beta->deployments->unpause(string deploymentID, ?list<AnthropicBeta> betas): BetaManagedAgentsDeployment`

**post** `/v1/deployments/{deployment_id}/unpause`

Unpause Deployment

### Parameters

- `deploymentID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsDeployment`

  - `string id`

    Unique identifier for this deployment.

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?string description`

    Description of what the deployment does.

  - `string environmentID`

    ID of the `environment` where sessions run.

  - `list<BetaManagedAgentsDeploymentInitialEvent> initialEvents`

    Events sent to each session immediately after creation.

  - `array<string,string> metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `string name`

    Human-readable name.

  - `?BetaManagedAgentsDeploymentPausedReason pausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

  - `list<BetaManagedAgentsSessionResourceConfig> resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

  - `?BetaManagedAgentsSchedule schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

  - `BetaManagedAgentsDeploymentStatus status`

    Lifecycle status of a deployment.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `list<string> vaultIDs`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeployment = $client->beta->deployments->unpause(
  'depl_011CZkZcDH3vPqd7xnEfwTai', betas: ['message-batches-2024-09-24']
);

var_dump($betaManagedAgentsDeployment);
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

## Domain Types

### Beta Managed Agents Agent Archived Deployment Paused Reason Error

- `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Cron Schedule

- `BetaManagedAgentsCronSchedule`

  - `string expression`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `string timezone`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

  - `Type type`

  - `?\Datetime lastRunAt`

    A timestamp in RFC 3339 format

  - `?list<\Datetime> upcomingRunsAt`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Cron Schedule Params

- `BetaManagedAgentsCronScheduleParams`

  - `string expression`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `string timezone`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `Type type`

### Beta Managed Agents Deployment

- `BetaManagedAgentsDeployment`

  - `string id`

    Unique identifier for this deployment.

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?string description`

    Description of what the deployment does.

  - `string environmentID`

    ID of the `environment` where sessions run.

  - `list<BetaManagedAgentsDeploymentInitialEvent> initialEvents`

    Events sent to each session immediately after creation.

  - `array<string,string> metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `string name`

    Human-readable name.

  - `?BetaManagedAgentsDeploymentPausedReason pausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

  - `list<BetaManagedAgentsSessionResourceConfig> resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

  - `?BetaManagedAgentsSchedule schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

  - `BetaManagedAgentsDeploymentStatus status`

    Lifecycle status of a deployment.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `list<string> vaultIDs`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Beta Managed Agents Deployment Initial Event

- `BetaManagedAgentsDeploymentInitialEvent`

  - `BetaManagedAgentsDeploymentUserMessageEvent`

    - `list<Content> content`

      Array of content blocks for the user message.

    - `Type type`

  - `BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

    - `string description`

      What the agent should produce. This is the task specification.

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

    - `Type type`

    - `?int maxIterations`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `BetaManagedAgentsDeploymentSystemMessageEvent`

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks to append. Text-only.

    - `Type type`

### Beta Managed Agents Deployment Initial Event Params

- `BetaManagedAgentsDeploymentInitialEventParams`

  - `ManagedAgentsUserMessageEventParams`

    - `list<Content> content`

      Array of content blocks for the user message.

    - `Type type`

  - `ManagedAgentsUserDefineOutcomeEventParams`

    - `string description`

      What the agent should produce. This is the task specification.

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

    - `Type type`

    - `?int maxIterations`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `ManagedAgentsSystemMessageEventParams`

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks to append. Text-only.

    - `Type type`

### Beta Managed Agents Deployment Paused Reason

- `BetaManagedAgentsDeploymentPausedReason`

  - `BetaManagedAgentsManualDeploymentPausedReason`

    - `Type type`

  - `BetaManagedAgentsErrorDeploymentPausedReason`

    - `BetaManagedAgentsDeploymentPausedReasonError error`

      The error that triggered an auto-pause. Matches the failed run's `error.type`.

    - `Type type`

### Beta Managed Agents Deployment Paused Reason Error

- `BetaManagedAgentsDeploymentPausedReasonError`

  - `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

    - `Type type`

  - `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

    - `Type type`

  - `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

    - `Type type`

  - `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

    - `Type type`

  - `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

    - `Type type`

  - `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

    - `Type type`

  - `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

    - `Type type`

  - `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

    - `Type type`

  - `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

    - `Type type`

  - `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

    - `Type type`

  - `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

    - `Type type`

  - `BetaManagedAgentsUnknownDeploymentPausedReasonError`

    - `Type type`

  - `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

    - `Type type`

  - `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

    - `Type type`

### Beta Managed Agents Deployment Status

- `BetaManagedAgentsDeploymentStatus`

  - `"active"`

  - `"paused"`

### Beta Managed Agents Deployment System Message Event

- `BetaManagedAgentsDeploymentSystemMessageEvent`

  - `list<BetaManagedAgentsSystemContentBlock> content`

    System content blocks to append. Text-only.

  - `Type type`

### Beta Managed Agents Deployment User Define Outcome Event

- `BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

  - `string description`

    What the agent should produce. This is the task specification.

  - `Rubric rubric`

    Rubric for grading the quality of an outcome.

  - `Type type`

  - `?int maxIterations`

    Eval→revision cycles before giving up. Default 3, max 20.

### Beta Managed Agents Deployment User Message Event

- `BetaManagedAgentsDeploymentUserMessageEvent`

  - `list<Content> content`

    Array of content blocks for the user message.

  - `Type type`

### Beta Managed Agents Environment Archived Deployment Paused Reason Error

- `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Environment Not Found Deployment Paused Reason Error

- `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Error Deployment Paused Reason

- `BetaManagedAgentsErrorDeploymentPausedReason`

  - `BetaManagedAgentsDeploymentPausedReasonError error`

    The error that triggered an auto-pause. Matches the failed run's `error.type`.

  - `Type type`

### Beta Managed Agents File Not Found Deployment Paused Reason Error

- `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents File Resource Config

- `BetaManagedAgentsFileResourceConfig`

  - `string fileID`

    ID of a previously uploaded file.

  - `Type type`

  - `?string mountPath`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

### Beta Managed Agents GitHub Repository Resource Config

- `BetaManagedAgentsGitHubRepositoryResourceConfig`

  - `Type type`

  - `string url`

    Github URL of the repository

  - `?Checkout checkout`

    Branch or commit to check out. Defaults to the repository's default branch.

  - `?string mountPath`

    Mount path in the container. Defaults to `/workspace/<repo-name>`.

### Beta Managed Agents Manual Deployment Paused Reason

- `BetaManagedAgentsManualDeploymentPausedReason`

  - `Type type`

### Beta Managed Agents MCP Egress Blocked Deployment Paused Reason Error

- `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Memory Store Archived Deployment Paused Reason Error

- `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Memory Store Resource Config

- `BetaManagedAgentsMemoryStoreResourceConfig`

  - `string memoryStoreID`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `Type type`

  - `?Access access`

    Access mode for an attached memory store.

  - `?string instructions`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Organization Disabled Deployment Paused Reason Error

- `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Schedule

- `BetaManagedAgentsSchedule`

  - `string expression`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `string timezone`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

  - `Type type`

  - `?\Datetime lastRunAt`

    A timestamp in RFC 3339 format

  - `?list<\Datetime> upcomingRunsAt`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Schedule Params

- `BetaManagedAgentsScheduleParams`

  - `string expression`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `string timezone`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `Type type`

### Beta Managed Agents Self Hosted Resources Unsupported Deployment Paused Reason Error

- `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Session Resource Config

- `BetaManagedAgentsSessionResourceConfig`

  - `BetaManagedAgentsGitHubRepositoryResourceConfig`

    - `Type type`

    - `string url`

      Github URL of the repository

    - `?Checkout checkout`

      Branch or commit to check out. Defaults to the repository's default branch.

    - `?string mountPath`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

  - `BetaManagedAgentsFileResourceConfig`

    - `string fileID`

      ID of a previously uploaded file.

    - `Type type`

    - `?string mountPath`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  - `BetaManagedAgentsMemoryStoreResourceConfig`

    - `string memoryStoreID`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `Type type`

    - `?Access access`

      Access mode for an attached memory store.

    - `?string instructions`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Session Resource Not Found Deployment Paused Reason Error

- `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Skill Not Found Deployment Paused Reason Error

- `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Unknown Deployment Paused Reason Error

- `BetaManagedAgentsUnknownDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Vault Archived Deployment Paused Reason Error

- `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Vault Not Found Deployment Paused Reason Error

- `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Workspace Archived Deployment Paused Reason Error

- `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

  - `Type type`

# Deployment Runs

## List Deployment Runs

`$client->beta->deploymentRuns->list(?\Datetime createdAtGt, ?\Datetime createdAtGte, ?\Datetime createdAtLt, ?\Datetime createdAtLte, ?string deploymentID, ?bool hasError, ?int limit, ?string page, ?BetaManagedAgentsTriggerType triggerType, ?list<AnthropicBeta> betas): PageCursor<BetaManagedAgentsDeploymentRun>`

**get** `/v1/deployment_runs`

List Deployment Runs

### Parameters

- `createdAtGt?:optional \Datetime`

  Return runs created strictly after this time (exclusive).

- `createdAtGte?:optional \Datetime`

  Return runs created at or after this time (inclusive).

- `createdAtLt?:optional \Datetime`

  Return runs created strictly before this time (exclusive).

- `createdAtLte?:optional \Datetime`

  Return runs created at or before this time (inclusive).

- `deploymentID?:optional string`

  Filter to a specific deployment. Omit to list across all deployments in the workspace. Filtering by a non-existent deployment_id returns 200 with empty data.

- `hasError?:optional bool`

  Filter: true for runs with non-null error, false for runs with non-null session_id. Omit for all.

- `limit?:optional int`

  Maximum results per page. Default 20, maximum 1000.

- `page?:optional string`

  Opaque pagination cursor. Pass next_page from the previous response. Invalid or expired cursors return 400.

- `triggerType?:optional BetaManagedAgentsTriggerType`

  Filter runs by what triggered them. Omit to return all runs.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsDeploymentRun`

  - `string id`

    Unique identifier for this run (`drun_...`).

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string deploymentID`

    ID of the deployment that produced this run.

  - `?Error error`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

  - `?string sessionID`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `BetaManagedAgentsTriggerContext triggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

  - `Type type`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->deploymentRuns->list(
  createdAtGt: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtGte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLt: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  deploymentID: 'deployment_id',
  hasError: true,
  limit: 0,
  page: 'page',
  triggerType: BetaManagedAgentsTriggerType::SCHEDULE,
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "agent": {
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
        "type": "agent",
        "version": 1
      },
      "created_at": "2019-12-27T18:11:19.117Z",
      "deployment_id": "deployment_id",
      "error": {
        "message": "message",
        "type": "environment_archived_error"
      },
      "session_id": "session_id",
      "trigger_context": {
        "scheduled_at": "2019-12-27T18:11:19.117Z",
        "type": "schedule"
      },
      "type": "deployment_run"
    }
  ],
  "next_page": "next_page"
}
```

## Get Deployment Run

`$client->beta->deploymentRuns->retrieve(string deploymentRunID, ?list<AnthropicBeta> betas): BetaManagedAgentsDeploymentRun`

**get** `/v1/deployment_runs/{deployment_run_id}`

Get Deployment Run

### Parameters

- `deploymentRunID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsDeploymentRun`

  - `string id`

    Unique identifier for this run (`drun_...`).

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string deploymentID`

    ID of the deployment that produced this run.

  - `?Error error`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

  - `?string sessionID`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `BetaManagedAgentsTriggerContext triggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

  - `Type type`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeploymentRun = $client->beta->deploymentRuns->retrieve(
  'deployment_run_id', betas: ['message-batches-2024-09-24']
);

var_dump($betaManagedAgentsDeploymentRun);
```

#### Response

```json
{
  "id": "id",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "type": "agent",
    "version": 1
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "deployment_id": "deployment_id",
  "error": {
    "message": "message",
    "type": "environment_archived_error"
  },
  "session_id": "session_id",
  "trigger_context": {
    "scheduled_at": "2019-12-27T18:11:19.117Z",
    "type": "schedule"
  },
  "type": "deployment_run"
}
```

## Domain Types

### Beta Managed Agents Agent Archived Run Error

- `BetaManagedAgentsAgentArchivedRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Deployment Run

- `BetaManagedAgentsDeploymentRun`

  - `string id`

    Unique identifier for this run (`drun_...`).

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string deploymentID`

    ID of the deployment that produced this run.

  - `?Error error`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

  - `?string sessionID`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `BetaManagedAgentsTriggerContext triggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

  - `Type type`

### Beta Managed Agents Environment Archived Run Error

- `BetaManagedAgentsEnvironmentArchivedRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Environment Not Found Run Error

- `BetaManagedAgentsEnvironmentNotFoundRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents File Not Found Run Error

- `BetaManagedAgentsFileNotFoundRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Manual Trigger Context

- `BetaManagedAgentsManualTriggerContext`

  - `Type type`

### Beta Managed Agents MCP Egress Blocked Run Error

- `BetaManagedAgentsMCPEgressBlockedRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Memory Store Archived Run Error

- `BetaManagedAgentsMemoryStoreArchivedRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Organization Disabled Run Error

- `BetaManagedAgentsOrganizationDisabledRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Schedule Trigger Context

- `BetaManagedAgentsScheduleTriggerContext`

  - `\Datetime scheduledAt`

    A timestamp in RFC 3339 format

  - `Type type`

### Beta Managed Agents Self Hosted Resources Unsupported Run Error

- `BetaManagedAgentsSelfHostedResourcesUnsupportedRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Session Creation Rejected Run Error

- `BetaManagedAgentsSessionCreationRejectedRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Session Rate Limited Run Error

- `BetaManagedAgentsSessionRateLimitedRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Session Resource Not Found Run Error

- `BetaManagedAgentsSessionResourceNotFoundRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Skill Not Found Run Error

- `BetaManagedAgentsSkillNotFoundRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Trigger Context

- `BetaManagedAgentsTriggerContext`

  - `BetaManagedAgentsScheduleTriggerContext`

    - `\Datetime scheduledAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `BetaManagedAgentsManualTriggerContext`

    - `Type type`

### Beta Managed Agents Trigger Type

- `BetaManagedAgentsTriggerType`

  - `"schedule"`

  - `"manual"`

### Beta Managed Agents Unknown Run Error

- `BetaManagedAgentsUnknownRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Vault Archived Run Error

- `BetaManagedAgentsVaultArchivedRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Vault Not Found Run Error

- `BetaManagedAgentsVaultNotFoundRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Workspace Archived Run Error

- `BetaManagedAgentsWorkspaceArchivedRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

# Vaults

## Create Vault

`$client->beta->vaults->create(string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas): BetaManagedAgentsVault`

**post** `/v1/vaults`

Create Vault

### Parameters

- `displayName: string`

  Human-readable name for the vault. 1-255 characters.

- `metadata?:optional array<string,string>`

  Arbitrary key-value metadata to attach to the vault. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsVault`

  - `string id`

    Unique identifier for the vault.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string displayName`

    Human-readable name for the vault.

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsVault = $client->beta->vaults->create(
  displayName: 'Example vault',
  metadata: ['environment' => 'production'],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsVault);
```

#### Response

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## List Vaults

`$client->beta->vaults->list(?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<BetaManagedAgentsVault>`

**get** `/v1/vaults`

List Vaults

### Parameters

- `includeArchived?:optional bool`

  Whether to include archived vaults in the results.

- `limit?:optional int`

  Maximum number of vaults to return per page. Defaults to 20, maximum 100.

- `page?:optional string`

  Opaque pagination token from a previous `list_vaults` response.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsVault`

  - `string id`

    Unique identifier for the vault.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string displayName`

    Human-readable name for the vault.

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->vaults->list(
  includeArchived: true,
  limit: 0,
  page: 'page',
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

#### Response

```json
{
  "data": [
    {
      "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "display_name": "Example vault",
      "metadata": {
        "environment": "production"
      },
      "type": "vault",
      "updated_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Vault

`$client->beta->vaults->retrieve(string vaultID, ?list<AnthropicBeta> betas): BetaManagedAgentsVault`

**get** `/v1/vaults/{vault_id}`

Get Vault

### Parameters

- `vaultID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsVault`

  - `string id`

    Unique identifier for the vault.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string displayName`

    Human-readable name for the vault.

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsVault = $client->beta->vaults->retrieve(
  'vlt_011CZkZDLs7fYzm1hXNPeRjv', betas: ['message-batches-2024-09-24']
);

var_dump($betaManagedAgentsVault);
```

#### Response

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## Update Vault

`$client->beta->vaults->update(string vaultID, ?string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas): BetaManagedAgentsVault`

**post** `/v1/vaults/{vault_id}`

Update Vault

### Parameters

- `vaultID: string`

- `displayName?:optional string`

  Updated human-readable name for the vault. 1-255 characters.

- `metadata?:optional array<string,string>`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsVault`

  - `string id`

    Unique identifier for the vault.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string displayName`

    Human-readable name for the vault.

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsVault = $client->beta->vaults->update(
  'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  displayName: 'Example vault',
  metadata: ['environment' => 'production'],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsVault);
```

#### Response

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## Delete Vault

`$client->beta->vaults->delete(string vaultID, ?list<AnthropicBeta> betas): BetaManagedAgentsDeletedVault`

**delete** `/v1/vaults/{vault_id}`

Delete Vault

### Parameters

- `vaultID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsDeletedVault`

  - `string id`

    Unique identifier of the deleted vault.

  - `Type type`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeletedVault = $client->beta->vaults->delete(
  'vlt_011CZkZDLs7fYzm1hXNPeRjv', betas: ['message-batches-2024-09-24']
);

var_dump($betaManagedAgentsDeletedVault);
```

#### Response

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "type": "vault_deleted"
}
```

## Archive Vault

`$client->beta->vaults->archive(string vaultID, ?list<AnthropicBeta> betas): BetaManagedAgentsVault`

**post** `/v1/vaults/{vault_id}/archive`

Archive Vault

### Parameters

- `vaultID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsVault`

  - `string id`

    Unique identifier for the vault.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string displayName`

    Human-readable name for the vault.

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsVault = $client->beta->vaults->archive(
  'vlt_011CZkZDLs7fYzm1hXNPeRjv', betas: ['message-batches-2024-09-24']
);

var_dump($betaManagedAgentsVault);
```

#### Response

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## Domain Types

### Beta Managed Agents Deleted Vault

- `BetaManagedAgentsDeletedVault`

  - `string id`

    Unique identifier of the deleted vault.

  - `Type type`

### Beta Managed Agents Vault

- `BetaManagedAgentsVault`

  - `string id`

    Unique identifier for the vault.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string displayName`

    Human-readable name for the vault.

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

# Credentials

## Create Credential

`$client->beta->vaults->credentials->create(string vaultID, Auth auth, ?string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas): ManagedAgentsCredential`

**post** `/v1/vaults/{vault_id}/credentials`

Create Credential

### Parameters

- `vaultID: string`

- `auth: Auth`

  Authentication details for creating a credential.

- `displayName?:optional string`

  Human-readable name for the credential. Up to 255 characters.

- `metadata?:optional array<string,string>`

  Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsCredential`

  - `string id`

    Unique identifier for the credential.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `string vaultID`

    Identifier of the vault this credential belongs to.

  - `?string displayName`

    Human-readable name for the credential.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsCredential = $client->beta->vaults->credentials->create(
  'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  auth: [
    'token' => 'bearer_exampletoken',
    'mcpServerURL' => 'https://example-server.modelcontextprotocol.io/sse',
    'type' => 'static_bearer',
  ],
  displayName: 'Example credential',
  metadata: ['environment' => 'production'],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsCredential);
```

#### Response

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

## List Credentials

`$client->beta->vaults->credentials->list(string vaultID, ?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<ManagedAgentsCredential>`

**get** `/v1/vaults/{vault_id}/credentials`

List Credentials

### Parameters

- `vaultID: string`

- `includeArchived?:optional bool`

  Whether to include archived credentials in the results.

- `limit?:optional int`

  Maximum number of credentials to return per page. Defaults to 20, maximum 100.

- `page?:optional string`

  Opaque pagination token from a previous `list_credentials` response.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsCredential`

  - `string id`

    Unique identifier for the credential.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `string vaultID`

    Identifier of the vault this credential belongs to.

  - `?string displayName`

    Human-readable name for the credential.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->vaults->credentials->list(
  'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  includeArchived: true,
  limit: 0,
  page: 'page',
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

#### Response

```json
{
  "data": [
    {
      "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
      "archived_at": null,
      "auth": {
        "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
        "type": "static_bearer"
      },
      "created_at": "2026-03-15T10:00:00Z",
      "metadata": {
        "environment": "production"
      },
      "type": "vault_credential",
      "updated_at": "2026-03-15T10:00:00Z",
      "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
      "display_name": "Example credential"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Credential

`$client->beta->vaults->credentials->retrieve(string credentialID, string vaultID, ?list<AnthropicBeta> betas): ManagedAgentsCredential`

**get** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Get Credential

### Parameters

- `vaultID: string`

- `credentialID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsCredential`

  - `string id`

    Unique identifier for the credential.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `string vaultID`

    Identifier of the vault this credential belongs to.

  - `?string displayName`

    Human-readable name for the credential.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsCredential = $client->beta->vaults->credentials->retrieve(
  'vcrd_011CZkZEMt8gZan2iYOQfSkw',
  vaultID: 'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsCredential);
```

#### Response

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

## Update Credential

`$client->beta->vaults->credentials->update(string credentialID, string vaultID, ?Auth auth, ?string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas): ManagedAgentsCredential`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update Credential

### Parameters

- `vaultID: string`

- `credentialID: string`

- `auth?:optional Auth`

  Updated authentication details for a credential.

- `displayName?:optional string`

  Updated human-readable name for the credential. 1-255 characters.

- `metadata?:optional array<string,string>`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsCredential`

  - `string id`

    Unique identifier for the credential.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `string vaultID`

    Identifier of the vault this credential belongs to.

  - `?string displayName`

    Human-readable name for the credential.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsCredential = $client->beta->vaults->credentials->update(
  'vcrd_011CZkZEMt8gZan2iYOQfSkw',
  vaultID: 'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  auth: [
    'type' => 'mcp_oauth',
    'accessToken' => 'x',
    'expiresAt' => new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
    'refresh' => [
      'refreshToken' => 'x',
      'scope' => 'scope',
      'tokenEndpointAuth' => [
        'type' => 'client_secret_basic', 'clientSecret' => 'x'
      ],
    ],
  ],
  displayName: 'Example credential',
  metadata: ['environment' => 'production'],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsCredential);
```

#### Response

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

## Delete Credential

`$client->beta->vaults->credentials->delete(string credentialID, string vaultID, ?list<AnthropicBeta> betas): ManagedAgentsDeletedCredential`

**delete** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete Credential

### Parameters

- `vaultID: string`

- `credentialID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsDeletedCredential`

  - `string id`

    Unique identifier of the deleted credential.

  - `Type type`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeletedCredential = $client
  ->beta
  ->vaults
  ->credentials
  ->delete(
  'vcrd_011CZkZEMt8gZan2iYOQfSkw',
  vaultID: 'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsDeletedCredential);
```

#### Response

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "type": "vault_credential_deleted"
}
```

## Archive Credential

`$client->beta->vaults->credentials->archive(string credentialID, string vaultID, ?list<AnthropicBeta> betas): ManagedAgentsCredential`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/archive`

Archive Credential

### Parameters

- `vaultID: string`

- `credentialID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsCredential`

  - `string id`

    Unique identifier for the credential.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `string vaultID`

    Identifier of the vault this credential belongs to.

  - `?string displayName`

    Human-readable name for the credential.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsCredential = $client->beta->vaults->credentials->archive(
  'vcrd_011CZkZEMt8gZan2iYOQfSkw',
  vaultID: 'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsCredential);
```

#### Response

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

## Validate Credential

`$client->beta->vaults->credentials->mcpOAuthValidate(string credentialID, string vaultID, ?list<AnthropicBeta> betas): ManagedAgentsCredentialValidation`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate Credential

### Parameters

- `vaultID: string`

- `credentialID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsCredentialValidation`

  - `string credentialID`

    Unique identifier of the credential that was validated.

  - `bool hasRefreshToken`

    Whether the credential has a refresh token configured.

  - `?ManagedAgentsMCPProbe mcpProbe`

    The failing step of an MCP validation probe.

  - `?ManagedAgentsRefreshObject refresh`

    Outcome of a refresh-token exchange attempted during credential validation.

  - `ManagedAgentsCredentialValidationStatus status`

    Overall verdict of a credential validation probe.

  - `Type type`

  - `\Datetime validatedAt`

    A timestamp in RFC 3339 format

  - `string vaultID`

    Identifier of the vault containing the credential.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsCredentialValidation = $client
  ->beta
  ->vaults
  ->credentials
  ->mcpOAuthValidate(
  'vcrd_011CZkZEMt8gZan2iYOQfSkw',
  vaultID: 'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsCredentialValidation);
```

#### Response

```json
{
  "credential_id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "has_refresh_token": true,
  "mcp_probe": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "method": "method"
  },
  "refresh": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "status": "succeeded"
  },
  "status": "valid",
  "type": "vault_credential_validation",
  "validated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv"
}
```

## Domain Types

### Beta Managed Agents Credential

- `ManagedAgentsCredential`

  - `string id`

    Unique identifier for the credential.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `string vaultID`

    Identifier of the vault this credential belongs to.

  - `?string displayName`

    Human-readable name for the credential.

### Beta Managed Agents Credential Networking Params

- `ManagedAgentsCredentialNetworkingParams`

  - `ManagedAgentsUnrestrictedCredentialNetworkingParams`

    - `Type type`

  - `ManagedAgentsLimitedCredentialNetworkingParams`

    - `list<string> allowedHosts`

      Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

    - `Type type`

### Beta Managed Agents Credential Validation

- `ManagedAgentsCredentialValidation`

  - `string credentialID`

    Unique identifier of the credential that was validated.

  - `bool hasRefreshToken`

    Whether the credential has a refresh token configured.

  - `?ManagedAgentsMCPProbe mcpProbe`

    The failing step of an MCP validation probe.

  - `?ManagedAgentsRefreshObject refresh`

    Outcome of a refresh-token exchange attempted during credential validation.

  - `ManagedAgentsCredentialValidationStatus status`

    Overall verdict of a credential validation probe.

  - `Type type`

  - `\Datetime validatedAt`

    A timestamp in RFC 3339 format

  - `string vaultID`

    Identifier of the vault containing the credential.

### Beta Managed Agents Credential Validation Status

- `ManagedAgentsCredentialValidationStatus`

  - `"valid"`

  - `"invalid"`

  - `"unknown"`

### Beta Managed Agents Deleted Credential

- `ManagedAgentsDeletedCredential`

  - `string id`

    Unique identifier of the deleted credential.

  - `Type type`

### Beta Managed Agents Environment Variable Auth Response

- `ManagedAgentsEnvironmentVariableAuthResponse`

  - `ManagedAgentsInjectionLocationResponse injectionLocation`

    Where in the outbound request the secret value is substituted.

  - `Networking networking`

    Outbound hosts the secret value is substituted on.

  - `string secretName`

    Name of the environment variable.

  - `Type type`

### Beta Managed Agents Environment Variable Create Params

- `ManagedAgentsEnvironmentVariableCreateParams`

  - `ManagedAgentsCredentialNetworkingParams networking`

    Outbound hosts the secret value is substituted on.

  - `string secretName`

    Name of the environment variable. Immutable after create.

  - `string secretValue`

    Secret value. Write-only; never returned in responses.

  - `Type type`

  - `?ManagedAgentsInjectionLocationParams injectionLocation`

    Where in the outbound request the secret value may be substituted.

### Beta Managed Agents Environment Variable Update Params

- `ManagedAgentsEnvironmentVariableUpdateParams`

  - `Type type`

  - `?ManagedAgentsInjectionLocationUpdateParams injectionLocation`

    Updated injection location.

  - `?ManagedAgentsCredentialNetworkingParams networking`

    Updated networking scope. Full replacement.

  - `?string secretValue`

    Updated secret value.

### Beta Managed Agents Injection Location Params

- `ManagedAgentsInjectionLocationParams`

  - `?bool body`

    Substitute when the placeholder appears in the request body.

  - `?bool header`

    Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Injection Location Response

- `ManagedAgentsInjectionLocationResponse`

  - `bool body`

    Whether the placeholder is substituted in the request body.

  - `bool header`

    Whether the placeholder is substituted in request header values.

### Beta Managed Agents Injection Location Update Params

- `ManagedAgentsInjectionLocationUpdateParams`

  - `?bool body`

    Substitute when the placeholder appears in the request body.

  - `?bool header`

    Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Limited Credential Networking Params

- `ManagedAgentsLimitedCredentialNetworkingParams`

  - `list<string> allowedHosts`

    Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

  - `Type type`

### Beta Managed Agents Limited Credential Networking Response

- `ManagedAgentsLimitedCredentialNetworkingResponse`

  - `list<string> allowedHosts`

    Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

  - `Type type`

### Beta Managed Agents MCP OAuth Auth Response

- `ManagedAgentsMCPOAuthAuthResponse`

  - `string mcpServerURL`

    URL of the MCP server this credential authenticates against.

  - `Type type`

  - `?\Datetime expiresAt`

    A timestamp in RFC 3339 format

  - `?ManagedAgentsMCPOAuthRefreshResponse refresh`

    OAuth refresh token configuration returned in credential responses.

### Beta Managed Agents MCP OAuth Create Params

- `ManagedAgentsMCPOAuthCreateParams`

  - `string accessToken`

    OAuth access token.

  - `string mcpServerURL`

    URL of the MCP server this credential authenticates against.

  - `Type type`

  - `?\Datetime expiresAt`

    A timestamp in RFC 3339 format

  - `?ManagedAgentsMCPOAuthRefreshParams refresh`

    OAuth refresh token parameters for creating a credential with refresh support.

### Beta Managed Agents MCP OAuth Refresh Params

- `ManagedAgentsMCPOAuthRefreshParams`

  - `string clientID`

    OAuth client ID.

  - `string refreshToken`

    OAuth refresh token.

  - `string tokenEndpoint`

    Token endpoint URL used to refresh the access token.

  - `TokenEndpointAuth tokenEndpointAuth`

    Token endpoint requires no client authentication.

  - `?string resource`

    OAuth resource indicator.

  - `?string scope`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Response

- `ManagedAgentsMCPOAuthRefreshResponse`

  - `string clientID`

    OAuth client ID.

  - `string tokenEndpoint`

    Token endpoint URL used to refresh the access token.

  - `TokenEndpointAuth tokenEndpointAuth`

    Token endpoint requires no client authentication.

  - `?string resource`

    OAuth resource indicator.

  - `?string scope`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Update Params

- `ManagedAgentsMCPOAuthRefreshUpdateParams`

  - `?string refreshToken`

    Updated OAuth refresh token.

  - `?string scope`

    Updated OAuth scope for the refresh request.

  - `?TokenEndpointAuth tokenEndpointAuth`

    Updated HTTP Basic authentication parameters for the token endpoint.

### Beta Managed Agents MCP OAuth Update Params

- `ManagedAgentsMCPOAuthUpdateParams`

  - `Type type`

  - `?string accessToken`

    Updated OAuth access token.

  - `?\Datetime expiresAt`

    A timestamp in RFC 3339 format

  - `?ManagedAgentsMCPOAuthRefreshUpdateParams refresh`

    Parameters for updating OAuth refresh token configuration.

### Beta Managed Agents MCP Probe

- `ManagedAgentsMCPProbe`

  - `?ManagedAgentsRefreshHTTPResponse httpResponse`

    An HTTP response captured during a credential validation probe.

  - `string method`

    The MCP method that failed (for example `initialize` or `tools/list`).

### Beta Managed Agents Refresh HTTP Response

- `ManagedAgentsRefreshHTTPResponse`

  - `string body`

    Response body. May be truncated and has sensitive values scrubbed.

  - `bool bodyTruncated`

    Whether `body` was truncated.

  - `string contentType`

    Value of the `Content-Type` response header.

  - `int statusCode`

    HTTP status code.

### Beta Managed Agents Refresh Object

- `ManagedAgentsRefreshObject`

  - `?ManagedAgentsRefreshHTTPResponse httpResponse`

    An HTTP response captured during a credential validation probe.

  - `Status status`

    Outcome of a refresh-token exchange attempted during credential validation.

### Beta Managed Agents Static Bearer Auth Response

- `ManagedAgentsStaticBearerAuthResponse`

  - `string mcpServerURL`

    URL of the MCP server this credential authenticates against.

  - `Type type`

### Beta Managed Agents Static Bearer Create Params

- `ManagedAgentsStaticBearerCreateParams`

  - `string token`

    Static bearer token value.

  - `string mcpServerURL`

    URL of the MCP server this credential authenticates against.

  - `Type type`

### Beta Managed Agents Static Bearer Update Params

- `ManagedAgentsStaticBearerUpdateParams`

  - `Type type`

  - `?string token`

    Updated static bearer token value.

### Beta Managed Agents Token Endpoint Auth Basic Param

- `ManagedAgentsTokenEndpointAuthBasicParam`

  - `string clientSecret`

    OAuth client secret.

  - `Type type`

### Beta Managed Agents Token Endpoint Auth Basic Response

- `ManagedAgentsTokenEndpointAuthBasicResponse`

  - `Type type`

### Beta Managed Agents Token Endpoint Auth Basic Update Param

- `ManagedAgentsTokenEndpointAuthBasicUpdateParam`

  - `Type type`

  - `?string clientSecret`

    Updated OAuth client secret.

### Beta Managed Agents Token Endpoint Auth None Param

- `ManagedAgentsTokenEndpointAuthNoneParam`

  - `Type type`

### Beta Managed Agents Token Endpoint Auth None Response

- `ManagedAgentsTokenEndpointAuthNoneResponse`

  - `Type type`

### Beta Managed Agents Token Endpoint Auth Post Param

- `ManagedAgentsTokenEndpointAuthPostParam`

  - `string clientSecret`

    OAuth client secret.

  - `Type type`

### Beta Managed Agents Token Endpoint Auth Post Response

- `ManagedAgentsTokenEndpointAuthPostResponse`

  - `Type type`

### Beta Managed Agents Token Endpoint Auth Post Update Param

- `ManagedAgentsTokenEndpointAuthPostUpdateParam`

  - `Type type`

  - `?string clientSecret`

    Updated OAuth client secret.

### Beta Managed Agents Unrestricted Credential Networking Params

- `ManagedAgentsUnrestrictedCredentialNetworkingParams`

  - `Type type`

### Beta Managed Agents Unrestricted Credential Networking Response

- `ManagedAgentsUnrestrictedCredentialNetworkingResponse`

  - `Type type`

# Memory Stores

## Create a memory store

`$client->beta->memoryStores->create(string name, ?string description, ?array<string,string> metadata, ?list<AnthropicBeta> betas): BetaManagedAgentsMemoryStore`

**post** `/v1/memory_stores`

Create a memory store

### Parameters

- `name: string`

  Human-readable name for the store. Required; 1–255 characters; no control characters. The mount-path slug under `/mnt/memory/` is derived from this name (lowercased, non-alphanumeric runs collapsed to a hyphen). Names need not be unique within a workspace.

- `description?:optional string`

  Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent.

- `metadata?:optional array<string,string>`

  Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Not visible to the agent.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsMemoryStore`

  - `string id`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `?string description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `?array<string,string> metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsMemoryStore = $client->beta->memoryStores->create(
  name: 'x',
  description: 'description',
  metadata: ['foo' => 'string'],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsMemoryStore);
```

#### Response

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "name": "name",
  "type": "memory_store",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "metadata": {
    "foo": "string"
  }
}
```

## List memory stores

`$client->beta->memoryStores->list(?\Datetime createdAtGte, ?\Datetime createdAtLte, ?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<BetaManagedAgentsMemoryStore>`

**get** `/v1/memory_stores`

List memory stores

### Parameters

- `createdAtGte?:optional \Datetime`

  Return only stores whose `created_at` is at or after this time (inclusive). Sent on the wire as `created_at[gte]`.

- `createdAtLte?:optional \Datetime`

  Return only stores whose `created_at` is at or before this time (inclusive). Sent on the wire as `created_at[lte]`.

- `includeArchived?:optional bool`

  When `true`, archived stores are included in the results. Defaults to `false` (archived stores are excluded).

- `limit?:optional int`

  Maximum number of stores to return per page. Must be between 1 and 100. Defaults to 20 when omitted.

- `page?:optional string`

  Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsMemoryStore`

  - `string id`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `?string description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `?array<string,string> metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->memoryStores->list(
  createdAtGte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  includeArchived: true,
  limit: 0,
  page: 'page',
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "name": "name",
      "type": "memory_store",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "description": "description",
      "metadata": {
        "foo": "string"
      }
    }
  ],
  "next_page": "next_page"
}
```

## Retrieve a memory store

`$client->beta->memoryStores->retrieve(string memoryStoreID, ?list<AnthropicBeta> betas): BetaManagedAgentsMemoryStore`

**get** `/v1/memory_stores/{memory_store_id}`

Retrieve a memory store

### Parameters

- `memoryStoreID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsMemoryStore`

  - `string id`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `?string description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `?array<string,string> metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsMemoryStore = $client->beta->memoryStores->retrieve(
  'memory_store_id', betas: ['message-batches-2024-09-24']
);

var_dump($betaManagedAgentsMemoryStore);
```

#### Response

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "name": "name",
  "type": "memory_store",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "metadata": {
    "foo": "string"
  }
}
```

## Update a memory store

`$client->beta->memoryStores->update(string memoryStoreID, ?string description, ?array<string,string> metadata, ?string name, ?list<AnthropicBeta> betas): BetaManagedAgentsMemoryStore`

**post** `/v1/memory_stores/{memory_store_id}`

Update a memory store

### Parameters

- `memoryStoreID: string`

- `description?:optional string`

  New description for the store, up to 1024 characters. Pass an empty string to clear it.

- `metadata?:optional array<string,string>`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `name?:optional string`

  New human-readable name for the store. 1–255 characters; no control characters. Renaming changes the slug used for the store's `mount_path` in sessions created after the update.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsMemoryStore`

  - `string id`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `?string description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `?array<string,string> metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsMemoryStore = $client->beta->memoryStores->update(
  'memory_store_id',
  description: 'description',
  metadata: ['foo' => 'string'],
  name: 'x',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsMemoryStore);
```

#### Response

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "name": "name",
  "type": "memory_store",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "metadata": {
    "foo": "string"
  }
}
```

## Delete a memory store

`$client->beta->memoryStores->delete(string memoryStoreID, ?list<AnthropicBeta> betas): BetaManagedAgentsDeletedMemoryStore`

**delete** `/v1/memory_stores/{memory_store_id}`

Delete a memory store

### Parameters

- `memoryStoreID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsDeletedMemoryStore`

  - `string id`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

  - `Type type`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeletedMemoryStore = $client->beta->memoryStores->delete(
  'memory_store_id', betas: ['message-batches-2024-09-24']
);

var_dump($betaManagedAgentsDeletedMemoryStore);
```

#### Response

```json
{
  "id": "id",
  "type": "memory_store_deleted"
}
```

## Archive a memory store

`$client->beta->memoryStores->archive(string memoryStoreID, ?list<AnthropicBeta> betas): BetaManagedAgentsMemoryStore`

**post** `/v1/memory_stores/{memory_store_id}/archive`

Archive a memory store

### Parameters

- `memoryStoreID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsMemoryStore`

  - `string id`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `?string description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `?array<string,string> metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsMemoryStore = $client->beta->memoryStores->archive(
  'memory_store_id', betas: ['message-batches-2024-09-24']
);

var_dump($betaManagedAgentsMemoryStore);
```

#### Response

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "name": "name",
  "type": "memory_store",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "metadata": {
    "foo": "string"
  }
}
```

## Domain Types

### Beta Managed Agents Deleted Memory Store

- `BetaManagedAgentsDeletedMemoryStore`

  - `string id`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

  - `Type type`

### Beta Managed Agents Memory Store

- `BetaManagedAgentsMemoryStore`

  - `string id`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `?string description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `?array<string,string> metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

# Memories

## Create a memory

`$client->beta->memoryStores->memories->create(string memoryStoreID, ?string content, string path, ?ManagedAgentsMemoryView view, ?list<AnthropicBeta> betas): ManagedAgentsMemory`

**post** `/v1/memory_stores/{memory_store_id}/memories`

Create a memory

### Parameters

- `memoryStoreID: string`

- `content: string`

  UTF-8 text content for the new memory. Maximum 100 kB (102,400 bytes). Required; pass `""` explicitly to create an empty memory.

- `path: string`

  Hierarchical path for the new memory, e.g. `/projects/foo/notes.md`. Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive.

- `view?:optional ManagedAgentsMemoryView`

  Query parameter for view

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsMemory`

  - `string id`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `string contentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `int contentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string memoryStoreID`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `string memoryVersionID`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `string path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `?string content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsMemory = $client->beta->memoryStores->memories->create(
  'memory_store_id',
  content: 'content',
  path: 'xx',
  view: ManagedAgentsMemoryView::BASIC,
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsMemory);
```

#### Response

```json
{
  "id": "id",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_store_id": "memory_store_id",
  "memory_version_id": "memory_version_id",
  "path": "path",
  "type": "memory",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "content": "content"
}
```

## List memories

`$client->beta->memoryStores->memories->list(string memoryStoreID, ?int depth, ?int limit, ?string page, ?string pathPrefix, ?ManagedAgentsMemoryView view, ?list<AnthropicBeta> betas): PageCursor<ManagedAgentsMemoryListItem>`

**get** `/v1/memory_stores/{memory_store_id}/memories`

List memories

### Parameters

- `memoryStoreID: string`

- `depth?:optional int`

  `0` (or omitted) returns all descendants below `path_prefix` (recursive). `1` returns immediate children only; deeper entries roll up as `memory_prefix` items. `depth=1` behaves like `ls`; omitting `depth` behaves like `find`.

- `limit?:optional int`

  Maximum number of items to return per page. Must be between 1 and 100. Defaults to 20 when omitted. Capped at 20 when `view=full`. Both `memory` and `memory_prefix` items count toward the limit.

- `page?:optional string`

  Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

- `pathPrefix?:optional string`

  Optional path prefix filter. Must end with `/` (segment-aligned), e.g., `/notes/`. This value appears in request URLs. Do not include secrets or personally identifiable information.

- `view?:optional ManagedAgentsMemoryView`

  Which projection of each `memory` to return. Defaults to `basic` (content omitted). `full` populates `content` on each item and caps `limit` at 20; use this as the bulk-read path for export and sync.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsMemoryListItem`

  - `ManagedAgentsMemory`

    - `string id`

      Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

    - `string contentSha256`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `int contentSizeBytes`

      Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    - `\Datetime createdAt`

      A timestamp in RFC 3339 format

    - `string memoryStoreID`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `string memoryVersionID`

      ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

    - `string path`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `Type type`

    - `\Datetime updatedAt`

      A timestamp in RFC 3339 format

    - `?string content`

      The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

  - `ManagedAgentsMemoryPrefix`

    - `string path`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

    - `Type type`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->memoryStores->memories->list(
  'memory_store_id',
  depth: 0,
  limit: 0,
  page: 'page',
  pathPrefix: 'path_prefix',
  view: ManagedAgentsMemoryView::BASIC,
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "content_sha256": "content_sha256",
      "content_size_bytes": 0,
      "created_at": "2019-12-27T18:11:19.117Z",
      "memory_store_id": "memory_store_id",
      "memory_version_id": "memory_version_id",
      "path": "path",
      "type": "memory",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "content": "content"
    }
  ],
  "next_page": "next_page"
}
```

## Retrieve a memory

`$client->beta->memoryStores->memories->retrieve(string memoryID, string memoryStoreID, ?ManagedAgentsMemoryView view, ?list<AnthropicBeta> betas): ManagedAgentsMemory`

**get** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Retrieve a memory

### Parameters

- `memoryStoreID: string`

- `memoryID: string`

- `view?:optional ManagedAgentsMemoryView`

  Query parameter for view

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsMemory`

  - `string id`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `string contentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `int contentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string memoryStoreID`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `string memoryVersionID`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `string path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `?string content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsMemory = $client->beta->memoryStores->memories->retrieve(
  'memory_id',
  memoryStoreID: 'memory_store_id',
  view: ManagedAgentsMemoryView::BASIC,
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsMemory);
```

#### Response

```json
{
  "id": "id",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_store_id": "memory_store_id",
  "memory_version_id": "memory_version_id",
  "path": "path",
  "type": "memory",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "content": "content"
}
```

## Update a memory

`$client->beta->memoryStores->memories->update(string memoryID, string memoryStoreID, ?ManagedAgentsMemoryView view, ?string content, ?string path, ?ManagedAgentsPrecondition precondition, ?list<AnthropicBeta> betas): ManagedAgentsMemory`

**post** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Update a memory

### Parameters

- `memoryStoreID: string`

- `memoryID: string`

- `view?:optional ManagedAgentsMemoryView`

  Query parameter for view

- `content?:optional string`

  New UTF-8 text content for the memory. Maximum 100 kB (102,400 bytes). Omit to leave the content unchanged (e.g., for a rename-only update).

- `path?:optional string`

  New path for the memory (a rename). Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive. The memory's `id` is preserved across renames. Omit to leave the path unchanged.

- `precondition?:optional ManagedAgentsPrecondition`

  Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsMemory`

  - `string id`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `string contentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `int contentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string memoryStoreID`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `string memoryVersionID`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `string path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `?string content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsMemory = $client->beta->memoryStores->memories->update(
  'memory_id',
  memoryStoreID: 'memory_store_id',
  view: ManagedAgentsMemoryView::BASIC,
  content: 'content',
  path: 'xx',
  precondition: [
    'type' => 'content_sha256', 'contentSha256' => 'content_sha256'
  ],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsMemory);
```

#### Response

```json
{
  "id": "id",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_store_id": "memory_store_id",
  "memory_version_id": "memory_version_id",
  "path": "path",
  "type": "memory",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "content": "content"
}
```

## Delete a memory

`$client->beta->memoryStores->memories->delete(string memoryID, string memoryStoreID, ?string expectedContentSha256, ?list<AnthropicBeta> betas): ManagedAgentsDeletedMemory`

**delete** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Delete a memory

### Parameters

- `memoryStoreID: string`

- `memoryID: string`

- `expectedContentSha256?:optional string`

  Query parameter for expected_content_sha256

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsDeletedMemory`

  - `string id`

    ID of the deleted memory (a `mem_...` value).

  - `Type type`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeletedMemory = $client->beta->memoryStores->memories->delete(
  'memory_id',
  memoryStoreID: 'memory_store_id',
  expectedContentSha256: 'expected_content_sha256',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsDeletedMemory);
```

#### Response

```json
{
  "id": "id",
  "type": "memory_deleted"
}
```

## Domain Types

### Beta Managed Agents Conflict Error

- `ManagedAgentsConflictError`

  - `Type type`

  - `?string message`

### Beta Managed Agents Content Sha256 Precondition

- `ManagedAgentsContentSha256Precondition`

  - `Type type`

  - `?string contentSha256`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

### Beta Managed Agents Deleted Memory

- `ManagedAgentsDeletedMemory`

  - `string id`

    ID of the deleted memory (a `mem_...` value).

  - `Type type`

### Beta Managed Agents Error

- `ManagedAgentsError`

  - `BetaInvalidRequestError`

    - `string message`

    - `"invalid_request_error" type`

  - `BetaAuthenticationError`

    - `string message`

    - `"authentication_error" type`

  - `BetaBillingError`

    - `string message`

    - `"billing_error" type`

  - `BetaPermissionError`

    - `string message`

    - `"permission_error" type`

  - `BetaNotFoundError`

    - `string message`

    - `"not_found_error" type`

  - `BetaRateLimitError`

    - `string message`

    - `"rate_limit_error" type`

  - `BetaGatewayTimeoutError`

    - `string message`

    - `"timeout_error" type`

  - `BetaAPIError`

    - `string message`

    - `"api_error" type`

  - `BetaOverloadedError`

    - `string message`

    - `"overloaded_error" type`

  - `ManagedAgentsMemoryPreconditionFailedError`

    - `Type type`

    - `?string message`

  - `ManagedAgentsMemoryPathConflictError`

    - `Type type`

    - `?string conflictingMemoryID`

    - `?string conflictingPath`

    - `?string message`

  - `ManagedAgentsConflictError`

    - `Type type`

    - `?string message`

### Beta Managed Agents Memory

- `ManagedAgentsMemory`

  - `string id`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `string contentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `int contentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string memoryStoreID`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `string memoryVersionID`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `string path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `?string content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Beta Managed Agents Memory List Item

- `ManagedAgentsMemoryListItem`

  - `ManagedAgentsMemory`

    - `string id`

      Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

    - `string contentSha256`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `int contentSizeBytes`

      Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    - `\Datetime createdAt`

      A timestamp in RFC 3339 format

    - `string memoryStoreID`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `string memoryVersionID`

      ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

    - `string path`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `Type type`

    - `\Datetime updatedAt`

      A timestamp in RFC 3339 format

    - `?string content`

      The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

  - `ManagedAgentsMemoryPrefix`

    - `string path`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

    - `Type type`

### Beta Managed Agents Memory Path Conflict Error

- `ManagedAgentsMemoryPathConflictError`

  - `Type type`

  - `?string conflictingMemoryID`

  - `?string conflictingPath`

  - `?string message`

### Beta Managed Agents Memory Precondition Failed Error

- `ManagedAgentsMemoryPreconditionFailedError`

  - `Type type`

  - `?string message`

### Beta Managed Agents Memory Prefix

- `ManagedAgentsMemoryPrefix`

  - `string path`

    The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

  - `Type type`

### Beta Managed Agents Memory View

- `ManagedAgentsMemoryView`

  - `"basic"`

  - `"full"`

### Beta Managed Agents Precondition

- `ManagedAgentsPrecondition`

  - `Type type`

  - `?string contentSha256`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

# Memory Versions

## List memory versions

`$client->beta->memoryStores->memoryVersions->list(string memoryStoreID, ?string apiKeyID, ?\Datetime createdAtGte, ?\Datetime createdAtLte, ?int limit, ?string memoryID, ?ManagedAgentsMemoryVersionOperation operation, ?string page, ?string sessionID, ?ManagedAgentsMemoryView view, ?list<AnthropicBeta> betas): PageCursor<ManagedAgentsMemoryVersion>`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions`

List memory versions

### Parameters

- `memoryStoreID: string`

- `apiKeyID?:optional string`

  Query parameter for api_key_id

- `createdAtGte?:optional \Datetime`

  Return versions created at or after this time (inclusive).

- `createdAtLte?:optional \Datetime`

  Return versions created at or before this time (inclusive).

- `limit?:optional int`

  Query parameter for limit

- `memoryID?:optional string`

  Query parameter for memory_id

- `operation?:optional ManagedAgentsMemoryVersionOperation`

  Query parameter for operation

- `page?:optional string`

  Query parameter for page

- `sessionID?:optional string`

  Query parameter for session_id

- `view?:optional ManagedAgentsMemoryView`

  Query parameter for view

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsMemoryVersion`

  - `string id`

    Unique identifier for this version (a `memver_...` value).

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string memoryID`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `string memoryStoreID`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `ManagedAgentsMemoryVersionOperation operation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

  - `Type type`

  - `?string content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `?string contentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `?int contentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `?ManagedAgentsActor createdBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

  - `?string path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `?\Datetime redactedAt`

    A timestamp in RFC 3339 format

  - `?ManagedAgentsActor redactedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->memoryStores->memoryVersions->list(
  'memory_store_id',
  apiKeyID: 'api_key_id',
  createdAtGte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  limit: 0,
  memoryID: 'memory_id',
  operation: ManagedAgentsMemoryVersionOperation::CREATED,
  page: 'page',
  sessionID: 'session_id',
  view: ManagedAgentsMemoryView::BASIC,
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "memory_id": "memory_id",
      "memory_store_id": "memory_store_id",
      "operation": "created",
      "type": "memory_version",
      "content": "content",
      "content_sha256": "content_sha256",
      "content_size_bytes": 0,
      "created_by": {
        "session_id": "x",
        "type": "session_actor"
      },
      "path": "path",
      "redacted_at": "2019-12-27T18:11:19.117Z",
      "redacted_by": {
        "session_id": "x",
        "type": "session_actor"
      }
    }
  ],
  "next_page": "next_page"
}
```

## Retrieve a memory version

`$client->beta->memoryStores->memoryVersions->retrieve(string memoryVersionID, string memoryStoreID, ?ManagedAgentsMemoryView view, ?list<AnthropicBeta> betas): ManagedAgentsMemoryVersion`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

Retrieve a memory version

### Parameters

- `memoryStoreID: string`

- `memoryVersionID: string`

- `view?:optional ManagedAgentsMemoryView`

  Query parameter for view

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsMemoryVersion`

  - `string id`

    Unique identifier for this version (a `memver_...` value).

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string memoryID`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `string memoryStoreID`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `ManagedAgentsMemoryVersionOperation operation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

  - `Type type`

  - `?string content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `?string contentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `?int contentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `?ManagedAgentsActor createdBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

  - `?string path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `?\Datetime redactedAt`

    A timestamp in RFC 3339 format

  - `?ManagedAgentsActor redactedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsMemoryVersion = $client
  ->beta
  ->memoryStores
  ->memoryVersions
  ->retrieve(
  'memory_version_id',
  memoryStoreID: 'memory_store_id',
  view: ManagedAgentsMemoryView::BASIC,
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsMemoryVersion);
```

#### Response

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_id": "memory_id",
  "memory_store_id": "memory_store_id",
  "operation": "created",
  "type": "memory_version",
  "content": "content",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_by": {
    "session_id": "x",
    "type": "session_actor"
  },
  "path": "path",
  "redacted_at": "2019-12-27T18:11:19.117Z",
  "redacted_by": {
    "session_id": "x",
    "type": "session_actor"
  }
}
```

## Redact a memory version

`$client->beta->memoryStores->memoryVersions->redact(string memoryVersionID, string memoryStoreID, ?list<AnthropicBeta> betas): ManagedAgentsMemoryVersion`

**post** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

Redact a memory version

### Parameters

- `memoryStoreID: string`

- `memoryVersionID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsMemoryVersion`

  - `string id`

    Unique identifier for this version (a `memver_...` value).

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string memoryID`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `string memoryStoreID`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `ManagedAgentsMemoryVersionOperation operation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

  - `Type type`

  - `?string content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `?string contentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `?int contentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `?ManagedAgentsActor createdBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

  - `?string path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `?\Datetime redactedAt`

    A timestamp in RFC 3339 format

  - `?ManagedAgentsActor redactedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsMemoryVersion = $client
  ->beta
  ->memoryStores
  ->memoryVersions
  ->redact(
  'memory_version_id',
  memoryStoreID: 'memory_store_id',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsMemoryVersion);
```

#### Response

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_id": "memory_id",
  "memory_store_id": "memory_store_id",
  "operation": "created",
  "type": "memory_version",
  "content": "content",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_by": {
    "session_id": "x",
    "type": "session_actor"
  },
  "path": "path",
  "redacted_at": "2019-12-27T18:11:19.117Z",
  "redacted_by": {
    "session_id": "x",
    "type": "session_actor"
  }
}
```

## Domain Types

### Beta Managed Agents Actor

- `ManagedAgentsActor`

  - `ManagedAgentsSessionActor`

    - `string sessionID`

      ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

    - `Type type`

  - `ManagedAgentsAPIActor`

    - `string apiKeyID`

      ID of the API key that performed the write. This identifies the key, not the secret.

    - `Type type`

  - `ManagedAgentsUserActor`

    - `Type type`

    - `string userID`

      ID of the user who performed the write (a `user_...` value).

### Beta Managed Agents API Actor

- `ManagedAgentsAPIActor`

  - `string apiKeyID`

    ID of the API key that performed the write. This identifies the key, not the secret.

  - `Type type`

### Beta Managed Agents Memory Version

- `ManagedAgentsMemoryVersion`

  - `string id`

    Unique identifier for this version (a `memver_...` value).

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string memoryID`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `string memoryStoreID`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `ManagedAgentsMemoryVersionOperation operation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

  - `Type type`

  - `?string content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `?string contentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `?int contentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `?ManagedAgentsActor createdBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

  - `?string path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `?\Datetime redactedAt`

    A timestamp in RFC 3339 format

  - `?ManagedAgentsActor redactedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Beta Managed Agents Memory Version Operation

- `ManagedAgentsMemoryVersionOperation`

  - `"created"`

  - `"modified"`

  - `"deleted"`

### Beta Managed Agents Session Actor

- `ManagedAgentsSessionActor`

  - `string sessionID`

    ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

  - `Type type`

### Beta Managed Agents User Actor

- `ManagedAgentsUserActor`

  - `Type type`

  - `string userID`

    ID of the user who performed the write (a `user_...` value).

# Files

## Upload File

`$client->beta->files->upload(string file, ?list<AnthropicBeta> betas): FileMetadata`

**post** `/v1/files`

Upload File

### Parameters

- `file: string`

  The file to upload

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `FileMetadata`

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing when the file was created.

  - `string filename`

    Original filename of the uploaded file.

  - `string mimeType`

    MIME type of the file.

  - `int sizeBytes`

    Size of the file in bytes.

  - `"file" type`

    Object type.

    For files, this is always `"file"`.

  - `?bool downloadable`

    Whether the file can be downloaded.

  - `?BetaFileScope scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$fileMetadata = $client->beta->files->upload(
  file: FileParam::fromString('Example data', filename: uniqid('file-upload-', true)),
  betas: ['message-batches-2024-09-24'],
);

var_dump($fileMetadata);
```

#### Response

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "created_at": "2025-04-15T18:37:24.100435Z",
  "filename": "document.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 102400,
  "type": "file",
  "downloadable": false,
  "scope": {
    "id": "id",
    "type": "session"
  }
}
```

## List Files

`$client->beta->files->list(?string afterID, ?string beforeID, ?int limit, ?string scopeID, ?list<AnthropicBeta> betas): Page<FileMetadata>`

**get** `/v1/files`

List Files

### Parameters

- `afterID?:optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `beforeID?:optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `limit?:optional int`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

- `scopeID?:optional string`

  Filter by scope ID. Only returns files associated with the specified scope (e.g., a session ID).

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `FileMetadata`

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing when the file was created.

  - `string filename`

    Original filename of the uploaded file.

  - `string mimeType`

    MIME type of the file.

  - `int sizeBytes`

    Size of the file in bytes.

  - `"file" type`

    Object type.

    For files, this is always `"file"`.

  - `?bool downloadable`

    Whether the file can be downloaded.

  - `?BetaFileScope scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->files->list(
  afterID: 'after_id',
  beforeID: 'before_id',
  limit: 1,
  scopeID: 'scope_id',
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

#### Response

```json
{
  "data": [
    {
      "id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "created_at": "2025-04-15T18:37:24.100435Z",
      "filename": "document.pdf",
      "mime_type": "application/pdf",
      "size_bytes": 102400,
      "type": "file",
      "downloadable": false,
      "scope": {
        "id": "id",
        "type": "session"
      }
    }
  ],
  "first_id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "has_more": true,
  "last_id": "file_013Zva2CMHLNnXjNJJKqJ2EF"
}
```

## Download File

`$client->beta->files->download(string fileID, ?list<AnthropicBeta> betas): download`

**get** `/v1/files/{file_id}/content`

Download File

### Parameters

- `fileID: string`

  ID of the File.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `mixed`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$response = $client->beta->files->download(
  'file_id', betas: ['message-batches-2024-09-24']
);

var_dump($response);
```

## Get File Metadata

`$client->beta->files->retrieveMetadata(string fileID, ?list<AnthropicBeta> betas): FileMetadata`

**get** `/v1/files/{file_id}`

Get File Metadata

### Parameters

- `fileID: string`

  ID of the File.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `FileMetadata`

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing when the file was created.

  - `string filename`

    Original filename of the uploaded file.

  - `string mimeType`

    MIME type of the file.

  - `int sizeBytes`

    Size of the file in bytes.

  - `"file" type`

    Object type.

    For files, this is always `"file"`.

  - `?bool downloadable`

    Whether the file can be downloaded.

  - `?BetaFileScope scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$fileMetadata = $client->beta->files->retrieveMetadata(
  'file_id', betas: ['message-batches-2024-09-24']
);

var_dump($fileMetadata);
```

#### Response

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "created_at": "2025-04-15T18:37:24.100435Z",
  "filename": "document.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 102400,
  "type": "file",
  "downloadable": false,
  "scope": {
    "id": "id",
    "type": "session"
  }
}
```

## Delete File

`$client->beta->files->delete(string fileID, ?list<AnthropicBeta> betas): DeletedFile`

**delete** `/v1/files/{file_id}`

Delete File

### Parameters

- `fileID: string`

  ID of the File.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `DeletedFile`

  - `string id`

    ID of the deleted file.

  - `?Type type`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$deletedFile = $client->beta->files->delete(
  'file_id', betas: ['message-batches-2024-09-24']
);

var_dump($deletedFile);
```

#### Response

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "type": "file_deleted"
}
```

## Domain Types

### Beta File Scope

- `BetaFileScope`

  - `string id`

    The ID of the scoping resource (e.g., the session ID).

  - `"session" type`

    The type of scope (e.g., `"session"`).

### Deleted File

- `DeletedFile`

  - `string id`

    ID of the deleted file.

  - `?Type type`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

### File Metadata

- `FileMetadata`

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing when the file was created.

  - `string filename`

    Original filename of the uploaded file.

  - `string mimeType`

    MIME type of the file.

  - `int sizeBytes`

    Size of the file in bytes.

  - `"file" type`

    Object type.

    For files, this is always `"file"`.

  - `?bool downloadable`

    Whether the file can be downloaded.

  - `?BetaFileScope scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

# Skills

## Create Skill

`$client->beta->skills->create(list<string> files, ?string displayTitle, ?list<AnthropicBeta> betas): SkillNewResponse`

**post** `/v1/skills`

Create Skill

### Parameters

- `files: list<string>`

  Files to upload for the skill.

  All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

- `displayTitle?:optional string`

  Display title for the skill.

  This is a human-readable label that is not included in the prompt sent to the model.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `SkillNewResponse`

  - `string id`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `string createdAt`

    ISO 8601 timestamp of when the skill was created.

  - `?string displayTitle`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `?string latestVersion`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `string source`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `string type`

    Object type.

    For Skills, this is always `"skill"`.

  - `string updatedAt`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$skill = $client->beta->skills->create(
  files: [
    FileParam::fromString('Example data', filename: uniqid('file-upload-', true)),
  ],
  displayTitle: 'display_title',
  betas: ['message-batches-2024-09-24'],
);

var_dump($skill);
```

#### Response

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_title": "My Custom Skill",
  "latest_version": "1759178010641129",
  "source": "custom",
  "type": "type",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

## List Skills

`$client->beta->skills->list(?int limit, ?string page, ?string source, ?list<AnthropicBeta> betas): PageCursor<SkillListResponse>`

**get** `/v1/skills`

List Skills

### Parameters

- `limit?:optional int`

  Number of results to return per page.

  Maximum value is 100. Defaults to 20.

- `page?:optional string`

  Pagination token for fetching a specific page of results.

  Pass the value from a previous response's `next_page` field to get the next page of results.

- `source?:optional string`

  Filter skills by source.

  If provided, only skills from the specified source will be returned:

  * `"custom"`: only return user-created skills
  * `"anthropic"`: only return Anthropic-created skills

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `SkillListResponse`

  - `string id`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `string createdAt`

    ISO 8601 timestamp of when the skill was created.

  - `?string displayTitle`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `?string latestVersion`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `string source`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `string type`

    Object type.

    For Skills, this is always `"skill"`.

  - `string updatedAt`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->skills->list(
  limit: 0,
  page: 'page',
  source: 'source',
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

#### Response

```json
{
  "data": [
    {
      "id": "skill_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_title": "My Custom Skill",
      "latest_version": "1759178010641129",
      "source": "custom",
      "type": "type",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Skill

`$client->beta->skills->retrieve(string skillID, ?list<AnthropicBeta> betas): SkillGetResponse`

**get** `/v1/skills/{skill_id}`

Get Skill

### Parameters

- `skillID: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `SkillGetResponse`

  - `string id`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `string createdAt`

    ISO 8601 timestamp of when the skill was created.

  - `?string displayTitle`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `?string latestVersion`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `string source`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `string type`

    Object type.

    For Skills, this is always `"skill"`.

  - `string updatedAt`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$skill = $client->beta->skills->retrieve(
  'skill_id', betas: ['message-batches-2024-09-24']
);

var_dump($skill);
```

#### Response

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_title": "My Custom Skill",
  "latest_version": "1759178010641129",
  "source": "custom",
  "type": "type",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

## Delete Skill

`$client->beta->skills->delete(string skillID, ?list<AnthropicBeta> betas): SkillDeleteResponse`

**delete** `/v1/skills/{skill_id}`

Delete Skill

### Parameters

- `skillID: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `SkillDeleteResponse`

  - `string id`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `string type`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$skill = $client->beta->skills->delete(
  'skill_id', betas: ['message-batches-2024-09-24']
);

var_dump($skill);
```

#### Response

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type"
}
```

# Versions

## Create Skill Version

`$client->beta->skills->versions->create(string skillID, list<string> files, ?list<AnthropicBeta> betas): VersionNewResponse`

**post** `/v1/skills/{skill_id}/versions`

Create Skill Version

### Parameters

- `skillID: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `files: list<string>`

  Files to upload for the skill.

  All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `VersionNewResponse`

  - `string id`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `string createdAt`

    ISO 8601 timestamp of when the skill version was created.

  - `string description`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `string directory`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `string name`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `string skillID`

    Identifier for the skill that this version belongs to.

  - `string type`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `string version`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$version = $client->beta->skills->versions->create(
  'skill_id',
  files: [
    FileParam::fromString('Example data', filename: uniqid('file-upload-', true)),
  ],
  betas: ['message-batches-2024-09-24'],
);

var_dump($version);
```

#### Response

```json
{
  "id": "skillver_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "description": "A custom skill for doing something useful",
  "directory": "my-skill",
  "name": "my-skill",
  "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type",
  "version": "1759178010641129"
}
```

## List Skill Versions

`$client->beta->skills->versions->list(string skillID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<VersionListResponse>`

**get** `/v1/skills/{skill_id}/versions`

List Skill Versions

### Parameters

- `skillID: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `limit?:optional int`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

- `page?:optional string`

  Optionally set to the `next_page` token from the previous response.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `VersionListResponse`

  - `string id`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `string createdAt`

    ISO 8601 timestamp of when the skill version was created.

  - `string description`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `string directory`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `string name`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `string skillID`

    Identifier for the skill that this version belongs to.

  - `string type`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `string version`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->skills->versions->list(
  'skill_id', limit: 0, page: 'page', betas: ['message-batches-2024-09-24']
);

var_dump($page);
```

#### Response

```json
{
  "data": [
    {
      "id": "skillver_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "description": "A custom skill for doing something useful",
      "directory": "my-skill",
      "name": "my-skill",
      "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
      "type": "type",
      "version": "1759178010641129"
    }
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Download Skill Version Content

`$client->beta->skills->versions->download(string version, string skillID, ?list<AnthropicBeta> betas): download`

**get** `/v1/skills/{skill_id}/versions/{version}/content`

Download a skill version's content as a zip archive.

### Parameters

- `skillID: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `version: string`

  Version identifier for the skill.

  Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `mixed`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$response = $client->beta->skills->versions->download(
  'version', skillID: 'skill_id', betas: ['message-batches-2024-09-24']
);

var_dump($response);
```

## Get Skill Version

`$client->beta->skills->versions->retrieve(string version, string skillID, ?list<AnthropicBeta> betas): VersionGetResponse`

**get** `/v1/skills/{skill_id}/versions/{version}`

Get Skill Version

### Parameters

- `skillID: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `version: string`

  Version identifier for the skill.

  Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `VersionGetResponse`

  - `string id`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `string createdAt`

    ISO 8601 timestamp of when the skill version was created.

  - `string description`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `string directory`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `string name`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `string skillID`

    Identifier for the skill that this version belongs to.

  - `string type`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `string version`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$version = $client->beta->skills->versions->retrieve(
  'version', skillID: 'skill_id', betas: ['message-batches-2024-09-24']
);

var_dump($version);
```

#### Response

```json
{
  "id": "skillver_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "description": "A custom skill for doing something useful",
  "directory": "my-skill",
  "name": "my-skill",
  "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type",
  "version": "1759178010641129"
}
```

## Delete Skill Version

`$client->beta->skills->versions->delete(string version, string skillID, ?list<AnthropicBeta> betas): VersionDeleteResponse`

**delete** `/v1/skills/{skill_id}/versions/{version}`

Delete Skill Version

### Parameters

- `skillID: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `version: string`

  Version identifier for the skill.

  Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `VersionDeleteResponse`

  - `string id`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `string type`

    Deleted object type.

    For Skill Versions, this is always `"skill_version_deleted"`.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$version = $client->beta->skills->versions->delete(
  'version', skillID: 'skill_id', betas: ['message-batches-2024-09-24']
);

var_dump($version);
```

#### Response

```json
{
  "id": "1759178010641129",
  "type": "type"
}
```

# User Profiles

## Create User Profile

`$client->beta->userProfiles->create(?string externalID, ?array<string,string> metadata, ?string name, ?Relationship relationship, ?list<AnthropicBeta> betas): BetaUserProfile`

**post** `/v1/user_profiles`

Create User Profile

### Parameters

- `externalID?:optional string`

  Platform's own identifier for this user. Not enforced unique. Maximum 255 characters.

- `metadata?:optional array<string,string>`

  Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

- `name?:optional string`

  Display name of the entity this profile represents. Required when relationship is `resold` (the resold-to company's name); optional otherwise. Maximum 255 characters.

- `relationship?:optional Relationship`

  How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaUserProfile`

  - `string id`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `array<string,string> metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `Relationship relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

  - `array<string,BetaUserProfileTrustGrant> trustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

  - `Type type`

    Object type. Always `user_profile`.

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `?string externalID`

    Platform's own identifier for this user. Not enforced unique.

  - `?string name`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaUserProfile = $client->beta->userProfiles->create(
  externalID: 'user_12345',
  metadata: [],
  name: 'x',
  relationship: 'external',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaUserProfile);
```

#### Response

```json
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {},
  "relationship": "external",
  "trust_grants": {
    "cyber": {
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "external_id": "user_12345",
  "name": "Example User"
}
```

## List User Profiles

`$client->beta->userProfiles->list(?int limit, ?Order order, ?string page, ?list<AnthropicBeta> betas): PageCursor<BetaUserProfile>`

**get** `/v1/user_profiles`

List User Profiles

### Parameters

- `limit?:optional int`

  Query parameter for limit

- `order?:optional Order`

  Query parameter for order

- `page?:optional string`

  Query parameter for page

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaUserProfile`

  - `string id`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `array<string,string> metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `Relationship relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

  - `array<string,BetaUserProfileTrustGrant> trustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

  - `Type type`

    Object type. Always `user_profile`.

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `?string externalID`

    Platform's own identifier for this user. Not enforced unique.

  - `?string name`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->userProfiles->list(
  limit: 0, order: 'asc', page: 'page', betas: ['message-batches-2024-09-24']
);

var_dump($page);
```

#### Response

```json
{
  "data": [
    {
      "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
      "created_at": "2026-03-15T10:00:00Z",
      "metadata": {},
      "relationship": "external",
      "trust_grants": {
        "cyber": {
          "status": "active"
        }
      },
      "type": "user_profile",
      "updated_at": "2026-03-15T10:00:00Z",
      "external_id": "user_12345",
      "name": "Example User"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get User Profile

`$client->beta->userProfiles->retrieve(string userProfileID, ?list<AnthropicBeta> betas): BetaUserProfile`

**get** `/v1/user_profiles/{user_profile_id}`

Get User Profile

### Parameters

- `userProfileID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaUserProfile`

  - `string id`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `array<string,string> metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `Relationship relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

  - `array<string,BetaUserProfileTrustGrant> trustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

  - `Type type`

    Object type. Always `user_profile`.

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `?string externalID`

    Platform's own identifier for this user. Not enforced unique.

  - `?string name`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaUserProfile = $client->beta->userProfiles->retrieve(
  'uprof_011CZkZCu8hGbp5mYRQgUmz9', betas: ['message-batches-2024-09-24']
);

var_dump($betaUserProfile);
```

#### Response

```json
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {},
  "relationship": "external",
  "trust_grants": {
    "cyber": {
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "external_id": "user_12345",
  "name": "Example User"
}
```

## Update User Profile

`$client->beta->userProfiles->update(string userProfileID, ?string externalID, ?array<string,string> metadata, ?string name, ?Relationship relationship, ?list<AnthropicBeta> betas): BetaUserProfile`

**post** `/v1/user_profiles/{user_profile_id}`

Update User Profile

### Parameters

- `userProfileID: string`

- `externalID?:optional string`

  If present, replaces the stored external_id. Omit to leave unchanged. Maximum 255 characters.

- `metadata?:optional array<string,string>`

  Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

- `name?:optional string`

  If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

- `relationship?:optional Relationship`

  How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaUserProfile`

  - `string id`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `array<string,string> metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `Relationship relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

  - `array<string,BetaUserProfileTrustGrant> trustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

  - `Type type`

    Object type. Always `user_profile`.

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `?string externalID`

    Platform's own identifier for this user. Not enforced unique.

  - `?string name`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaUserProfile = $client->beta->userProfiles->update(
  'uprof_011CZkZCu8hGbp5mYRQgUmz9',
  externalID: 'user_12345',
  metadata: ['foo' => 'string'],
  name: 'x',
  relationship: 'external',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaUserProfile);
```

#### Response

```json
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {},
  "relationship": "external",
  "trust_grants": {
    "cyber": {
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "external_id": "user_12345",
  "name": "Example User"
}
```

## Create Enrollment URL

`$client->beta->userProfiles->createEnrollmentURL(string userProfileID, ?list<AnthropicBeta> betas): BetaUserProfileEnrollmentURL`

**post** `/v1/user_profiles/{user_profile_id}/enrollment_url`

Create Enrollment URL

### Parameters

- `userProfileID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaUserProfileEnrollmentURL`

  - `\Datetime expiresAt`

    A timestamp in RFC 3339 format

  - `Type type`

    Object type. Always `enrollment_url`.

  - `string url`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaUserProfileEnrollmentURL = $client
  ->beta
  ->userProfiles
  ->createEnrollmentURL(
  'uprof_011CZkZCu8hGbp5mYRQgUmz9', betas: ['message-batches-2024-09-24']
);

var_dump($betaUserProfileEnrollmentURL);
```

#### Response

```json
{
  "expires_at": "2026-03-15T10:15:00Z",
  "type": "enrollment_url",
  "url": "https://platform.claude.com/user-profiles/enrollment/M3J0bGJxZ2ppMnptbnB1"
}
```

## Domain Types

### Beta User Profile

- `BetaUserProfile`

  - `string id`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `array<string,string> metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `Relationship relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

  - `array<string,BetaUserProfileTrustGrant> trustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

  - `Type type`

    Object type. Always `user_profile`.

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `?string externalID`

    Platform's own identifier for this user. Not enforced unique.

  - `?string name`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

### Beta User Profile Enrollment URL

- `BetaUserProfileEnrollmentURL`

  - `\Datetime expiresAt`

    A timestamp in RFC 3339 format

  - `Type type`

    Object type. Always `enrollment_url`.

  - `string url`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Beta User Profile Trust Grant

- `BetaUserProfileTrustGrant`

  - `Status status`

    Status of the trust grant.

# Tunnels

# Certificates

# Webhooks

## Domain Types

### Beta Webhook Agent Archived Event Data

- `BetaWebhookAgentArchivedEventData`

  - `string id`

    ID of the agent that triggered the event.

  - `string organizationID`

  - `"agent.archived" type`

  - `string workspaceID`

### Beta Webhook Agent Created Event Data

- `BetaWebhookAgentCreatedEventData`

  - `string id`

    ID of the agent that triggered the event.

  - `string organizationID`

  - `"agent.created" type`

  - `string workspaceID`

### Beta Webhook Agent Deleted Event Data

- `BetaWebhookAgentDeletedEventData`

  - `string id`

    ID of the agent that triggered the event.

  - `string organizationID`

  - `"agent.deleted" type`

  - `string workspaceID`

### Beta Webhook Agent Updated Event Data

- `BetaWebhookAgentUpdatedEventData`

  - `string id`

    ID of the agent that triggered the event.

  - `string organizationID`

  - `"agent.updated" type`

  - `string workspaceID`

### Beta Webhook Deployment Archived Event Data

- `BetaWebhookDeploymentArchivedEventData`

  - `string id`

    ID of the deployment that triggered the event.

  - `string organizationID`

  - `"deployment.archived" type`

  - `string workspaceID`

### Beta Webhook Deployment Created Event Data

- `BetaWebhookDeploymentCreatedEventData`

  - `string id`

    ID of the deployment that triggered the event.

  - `string organizationID`

  - `"deployment.created" type`

  - `string workspaceID`

### Beta Webhook Deployment Deleted Event Data

- `BetaWebhookDeploymentDeletedEventData`

  - `string id`

    ID of the deployment that triggered the event.

  - `string organizationID`

  - `"deployment.deleted" type`

  - `string workspaceID`

### Beta Webhook Deployment Paused Event Data

- `BetaWebhookDeploymentPausedEventData`

  - `string id`

    ID of the deployment that triggered the event.

  - `string organizationID`

  - `"deployment.paused" type`

  - `string workspaceID`

### Beta Webhook Deployment Run Failed Event Data

- `BetaWebhookDeploymentRunFailedEventData`

  - `string id`

    ID of the deployment run that triggered the event.

  - `string organizationID`

  - `"deployment_run.failed" type`

  - `string workspaceID`

### Beta Webhook Deployment Run Started Event Data

- `BetaWebhookDeploymentRunStartedEventData`

  - `string id`

    ID of the deployment run that triggered the event.

  - `string organizationID`

  - `"deployment_run.started" type`

  - `string workspaceID`

### Beta Webhook Deployment Run Succeeded Event Data

- `BetaWebhookDeploymentRunSucceededEventData`

  - `string id`

    ID of the deployment run that triggered the event.

  - `string organizationID`

  - `"deployment_run.succeeded" type`

  - `string workspaceID`

### Beta Webhook Deployment Unpaused Event Data

- `BetaWebhookDeploymentUnpausedEventData`

  - `string id`

    ID of the deployment that triggered the event.

  - `string organizationID`

  - `"deployment.unpaused" type`

  - `string workspaceID`

### Beta Webhook Deployment Updated Event Data

- `BetaWebhookDeploymentUpdatedEventData`

  - `string id`

    ID of the deployment that triggered the event.

  - `string organizationID`

  - `"deployment.updated" type`

  - `string workspaceID`

### Beta Webhook Event

- `BetaWebhookEvent`

  - `string id`

    Unique event identifier for idempotency.

  - `\Datetime createdAt`

    RFC 3339 timestamp when the event occurred.

  - `BetaWebhookEventData data`

  - `"event" type`

    Object type. Always `event` for webhook payloads.

### Beta Webhook Event Data

- `BetaWebhookEventData`

  - `BetaWebhookSessionCreatedEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `"session.created" type`

    - `string workspaceID`

  - `BetaWebhookSessionPendingEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `"session.pending" type`

    - `string workspaceID`

  - `BetaWebhookSessionRunningEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `"session.running" type`

    - `string workspaceID`

  - `BetaWebhookSessionIdledEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `"session.idled" type`

    - `string workspaceID`

  - `BetaWebhookSessionRequiresActionEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `"session.requires_action" type`

    - `string workspaceID`

  - `BetaWebhookSessionArchivedEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `"session.archived" type`

    - `string workspaceID`

  - `BetaWebhookSessionDeletedEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `"session.deleted" type`

    - `string workspaceID`

  - `BetaWebhookSessionStatusRescheduledEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `"session.status_rescheduled" type`

    - `string workspaceID`

  - `BetaWebhookSessionStatusRunStartedEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `"session.status_run_started" type`

    - `string workspaceID`

  - `BetaWebhookSessionStatusIdledEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `"session.status_idled" type`

    - `string workspaceID`

  - `BetaWebhookSessionStatusTerminatedEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `"session.status_terminated" type`

    - `string workspaceID`

  - `BetaWebhookSessionThreadCreatedEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string sessionThreadID`

      ID of the session thread this event refers to.

    - `"session.thread_created" type`

    - `string workspaceID`

  - `BetaWebhookSessionThreadIdledEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string sessionThreadID`

      ID of the session thread this event refers to.

    - `"session.thread_idled" type`

    - `string workspaceID`

  - `BetaWebhookSessionThreadTerminatedEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string sessionThreadID`

      ID of the session thread this event refers to.

    - `"session.thread_terminated" type`

    - `string workspaceID`

  - `BetaWebhookSessionOutcomeEvaluationEndedEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `"session.outcome_evaluation_ended" type`

    - `string workspaceID`

  - `BetaWebhookVaultCreatedEventData`

    - `string id`

      ID of the vault that triggered the event.

    - `string organizationID`

    - `"vault.created" type`

    - `string workspaceID`

  - `BetaWebhookVaultArchivedEventData`

    - `string id`

      ID of the vault that triggered the event.

    - `string organizationID`

    - `"vault.archived" type`

    - `string workspaceID`

  - `BetaWebhookVaultDeletedEventData`

    - `string id`

      ID of the vault that triggered the event.

    - `string organizationID`

    - `"vault.deleted" type`

    - `string workspaceID`

  - `BetaWebhookVaultCredentialCreatedEventData`

    - `string id`

      ID of the vault credential that triggered the event.

    - `string organizationID`

    - `"vault_credential.created" type`

    - `string vaultID`

      ID of the vault that owns this credential.

    - `string workspaceID`

  - `BetaWebhookVaultCredentialArchivedEventData`

    - `string id`

      ID of the vault credential that triggered the event.

    - `string organizationID`

    - `"vault_credential.archived" type`

    - `string vaultID`

      ID of the vault that owns this credential.

    - `string workspaceID`

  - `BetaWebhookVaultCredentialDeletedEventData`

    - `string id`

      ID of the vault credential that triggered the event.

    - `string organizationID`

    - `"vault_credential.deleted" type`

    - `string vaultID`

      ID of the vault that owns this credential.

    - `string workspaceID`

  - `BetaWebhookVaultCredentialRefreshFailedEventData`

    - `string id`

      ID of the vault credential that triggered the event.

    - `string organizationID`

    - `"vault_credential.refresh_failed" type`

    - `string vaultID`

      ID of the vault that owns this credential.

    - `string workspaceID`

  - `BetaWebhookSessionUpdatedEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `"session.updated" type`

    - `string workspaceID`

  - `BetaWebhookAgentCreatedEventData`

    - `string id`

      ID of the agent that triggered the event.

    - `string organizationID`

    - `"agent.created" type`

    - `string workspaceID`

  - `BetaWebhookAgentArchivedEventData`

    - `string id`

      ID of the agent that triggered the event.

    - `string organizationID`

    - `"agent.archived" type`

    - `string workspaceID`

  - `BetaWebhookAgentDeletedEventData`

    - `string id`

      ID of the agent that triggered the event.

    - `string organizationID`

    - `"agent.deleted" type`

    - `string workspaceID`

  - `BetaWebhookDeploymentPausedEventData`

    - `string id`

      ID of the deployment that triggered the event.

    - `string organizationID`

    - `"deployment.paused" type`

    - `string workspaceID`

  - `BetaWebhookDeploymentRunFailedEventData`

    - `string id`

      ID of the deployment run that triggered the event.

    - `string organizationID`

    - `"deployment_run.failed" type`

    - `string workspaceID`

  - `BetaWebhookDeploymentCreatedEventData`

    - `string id`

      ID of the deployment that triggered the event.

    - `string organizationID`

    - `"deployment.created" type`

    - `string workspaceID`

  - `BetaWebhookDeploymentUpdatedEventData`

    - `string id`

      ID of the deployment that triggered the event.

    - `string organizationID`

    - `"deployment.updated" type`

    - `string workspaceID`

  - `BetaWebhookDeploymentUnpausedEventData`

    - `string id`

      ID of the deployment that triggered the event.

    - `string organizationID`

    - `"deployment.unpaused" type`

    - `string workspaceID`

  - `BetaWebhookAgentUpdatedEventData`

    - `string id`

      ID of the agent that triggered the event.

    - `string organizationID`

    - `"agent.updated" type`

    - `string workspaceID`

  - `BetaWebhookDeploymentArchivedEventData`

    - `string id`

      ID of the deployment that triggered the event.

    - `string organizationID`

    - `"deployment.archived" type`

    - `string workspaceID`

  - `BetaWebhookDeploymentRunStartedEventData`

    - `string id`

      ID of the deployment run that triggered the event.

    - `string organizationID`

    - `"deployment_run.started" type`

    - `string workspaceID`

  - `BetaWebhookDeploymentDeletedEventData`

    - `string id`

      ID of the deployment that triggered the event.

    - `string organizationID`

    - `"deployment.deleted" type`

    - `string workspaceID`

  - `BetaWebhookDeploymentRunSucceededEventData`

    - `string id`

      ID of the deployment run that triggered the event.

    - `string organizationID`

    - `"deployment_run.succeeded" type`

    - `string workspaceID`

### Beta Webhook Session Archived Event Data

- `BetaWebhookSessionArchivedEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `"session.archived" type`

  - `string workspaceID`

### Beta Webhook Session Created Event Data

- `BetaWebhookSessionCreatedEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `"session.created" type`

  - `string workspaceID`

### Beta Webhook Session Deleted Event Data

- `BetaWebhookSessionDeletedEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `"session.deleted" type`

  - `string workspaceID`

### Beta Webhook Session Idled Event Data

- `BetaWebhookSessionIdledEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `"session.idled" type`

  - `string workspaceID`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `BetaWebhookSessionOutcomeEvaluationEndedEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `"session.outcome_evaluation_ended" type`

  - `string workspaceID`

### Beta Webhook Session Pending Event Data

- `BetaWebhookSessionPendingEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `"session.pending" type`

  - `string workspaceID`

### Beta Webhook Session Requires Action Event Data

- `BetaWebhookSessionRequiresActionEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `"session.requires_action" type`

  - `string workspaceID`

### Beta Webhook Session Running Event Data

- `BetaWebhookSessionRunningEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `"session.running" type`

  - `string workspaceID`

### Beta Webhook Session Status Idled Event Data

- `BetaWebhookSessionStatusIdledEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `"session.status_idled" type`

  - `string workspaceID`

### Beta Webhook Session Status Rescheduled Event Data

- `BetaWebhookSessionStatusRescheduledEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `"session.status_rescheduled" type`

  - `string workspaceID`

### Beta Webhook Session Status Run Started Event Data

- `BetaWebhookSessionStatusRunStartedEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `"session.status_run_started" type`

  - `string workspaceID`

### Beta Webhook Session Status Terminated Event Data

- `BetaWebhookSessionStatusTerminatedEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `"session.status_terminated" type`

  - `string workspaceID`

### Beta Webhook Session Thread Created Event Data

- `BetaWebhookSessionThreadCreatedEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string sessionThreadID`

    ID of the session thread this event refers to.

  - `"session.thread_created" type`

  - `string workspaceID`

### Beta Webhook Session Thread Idled Event Data

- `BetaWebhookSessionThreadIdledEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string sessionThreadID`

    ID of the session thread this event refers to.

  - `"session.thread_idled" type`

  - `string workspaceID`

### Beta Webhook Session Thread Terminated Event Data

- `BetaWebhookSessionThreadTerminatedEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string sessionThreadID`

    ID of the session thread this event refers to.

  - `"session.thread_terminated" type`

  - `string workspaceID`

### Beta Webhook Session Updated Event Data

- `BetaWebhookSessionUpdatedEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `"session.updated" type`

  - `string workspaceID`

### Beta Webhook Vault Archived Event Data

- `BetaWebhookVaultArchivedEventData`

  - `string id`

    ID of the vault that triggered the event.

  - `string organizationID`

  - `"vault.archived" type`

  - `string workspaceID`

### Beta Webhook Vault Created Event Data

- `BetaWebhookVaultCreatedEventData`

  - `string id`

    ID of the vault that triggered the event.

  - `string organizationID`

  - `"vault.created" type`

  - `string workspaceID`

### Beta Webhook Vault Credential Archived Event Data

- `BetaWebhookVaultCredentialArchivedEventData`

  - `string id`

    ID of the vault credential that triggered the event.

  - `string organizationID`

  - `"vault_credential.archived" type`

  - `string vaultID`

    ID of the vault that owns this credential.

  - `string workspaceID`

### Beta Webhook Vault Credential Created Event Data

- `BetaWebhookVaultCredentialCreatedEventData`

  - `string id`

    ID of the vault credential that triggered the event.

  - `string organizationID`

  - `"vault_credential.created" type`

  - `string vaultID`

    ID of the vault that owns this credential.

  - `string workspaceID`

### Beta Webhook Vault Credential Deleted Event Data

- `BetaWebhookVaultCredentialDeletedEventData`

  - `string id`

    ID of the vault credential that triggered the event.

  - `string organizationID`

  - `"vault_credential.deleted" type`

  - `string vaultID`

    ID of the vault that owns this credential.

  - `string workspaceID`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `BetaWebhookVaultCredentialRefreshFailedEventData`

  - `string id`

    ID of the vault credential that triggered the event.

  - `string organizationID`

  - `"vault_credential.refresh_failed" type`

  - `string vaultID`

    ID of the vault that owns this credential.

  - `string workspaceID`

### Beta Webhook Vault Deleted Event Data

- `BetaWebhookVaultDeletedEventData`

  - `string id`

    ID of the vault that triggered the event.

  - `string organizationID`

  - `"vault.deleted" type`

  - `string workspaceID`

### Unwrap Webhook Event

- `UnwrapWebhookEvent`

  - `string id`

    Unique event identifier for idempotency.

  - `\Datetime createdAt`

    RFC 3339 timestamp when the event occurred.

  - `BetaWebhookEventData data`

  - `"event" type`

    Object type. Always `event` for webhook payloads.
