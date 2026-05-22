# Models

## List Models

`$client->models->list(?string afterID, ?string beforeID, ?int limit, ?list<AnthropicBeta> betas): Page<ModelInfo>`

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

- `ModelInfo`

  - `string id`

    Unique model identifier.

  - `?ModelCapabilities capabilities`

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

$page = $client->models->list(
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

`$client->models->retrieve(string modelID, ?list<AnthropicBeta> betas): ModelInfo`

**get** `/v1/models/{model_id}`

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

### Parameters

- `modelID: string`

  Model identifier or alias.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ModelInfo`

  - `string id`

    Unique model identifier.

  - `?ModelCapabilities capabilities`

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

$modelInfo = $client->models->retrieve(
  'model_id', betas: ['message-batches-2024-09-24']
);

var_dump($modelInfo);
```

#### Response

```json
{
  "id": "claude-opus-4-6",
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

### Capability Support

- `CapabilitySupport`

  - `bool supported`

    Whether this capability is supported by the model.

### Context Management Capability

- `ContextManagementCapability`

  - `?CapabilitySupport clearThinking20251015`

    Indicates whether a capability is supported.

  - `?CapabilitySupport clearToolUses20250919`

    Indicates whether a capability is supported.

  - `?CapabilitySupport compact20260112`

    Indicates whether a capability is supported.

  - `bool supported`

    Whether this capability is supported by the model.

### Effort Capability

- `EffortCapability`

  - `CapabilitySupport high`

    Whether the model supports high effort level.

  - `CapabilitySupport low`

    Whether the model supports low effort level.

  - `CapabilitySupport max`

    Whether the model supports max effort level.

  - `CapabilitySupport medium`

    Whether the model supports medium effort level.

  - `bool supported`

    Whether this capability is supported by the model.

  - `?CapabilitySupport xhigh`

    Indicates whether a capability is supported.

### Model Capabilities

- `ModelCapabilities`

  - `CapabilitySupport batch`

    Whether the model supports the Batch API.

  - `CapabilitySupport citations`

    Whether the model supports citation generation.

  - `CapabilitySupport codeExecution`

    Whether the model supports code execution tools.

  - `ContextManagementCapability contextManagement`

    Context management support and available strategies.

  - `EffortCapability effort`

    Effort (reasoning_effort) support and available levels.

  - `CapabilitySupport imageInput`

    Whether the model accepts image content blocks.

  - `CapabilitySupport pdfInput`

    Whether the model accepts PDF content blocks.

  - `CapabilitySupport structuredOutputs`

    Whether the model supports structured output / JSON mode / strict tool schemas.

  - `ThinkingCapability thinking`

    Thinking capability and supported type configurations.

### Model Info

- `ModelInfo`

  - `string id`

    Unique model identifier.

  - `?ModelCapabilities capabilities`

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

### Thinking Capability

- `ThinkingCapability`

  - `bool supported`

    Whether this capability is supported by the model.

  - `ThinkingTypes types`

    Supported thinking type configurations.

### Thinking Types

- `ThinkingTypes`

  - `CapabilitySupport adaptive`

    Whether the model supports thinking with type 'adaptive' (auto).

  - `CapabilitySupport enabled`

    Whether the model supports thinking with type 'enabled'.
