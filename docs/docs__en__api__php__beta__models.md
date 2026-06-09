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
