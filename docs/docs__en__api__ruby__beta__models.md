# Models

## List Models

`beta.models.list(**kwargs) -> Page<BetaModelInfo>`

**get** `/v1/models`

List available models.

The Models API response can be used to determine which models are available for use in the API. More recently released models are listed first.

### Parameters

- `after_id: String`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: String`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `limit: Integer`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 24 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"mid-conversation-system-2026-04-07"`

### Returns

- `class BetaModelInfo`

  - `id: String`

    Unique model identifier.

  - `capabilities: BetaModelCapabilities`

    Model capability information.

    - `batch: BetaCapabilitySupport`

      Whether the model supports the Batch API.

      - `supported: bool`

        Whether this capability is supported by the model.

    - `citations: BetaCapabilitySupport`

      Whether the model supports citation generation.

    - `code_execution: BetaCapabilitySupport`

      Whether the model supports code execution tools.

    - `context_management: BetaContextManagementCapability`

      Context management support and available strategies.

      - `clear_thinking_20251015: BetaCapabilitySupport`

        Indicates whether a capability is supported.

      - `clear_tool_uses_20250919: BetaCapabilitySupport`

        Indicates whether a capability is supported.

      - `compact_20260112: BetaCapabilitySupport`

        Indicates whether a capability is supported.

      - `supported: bool`

        Whether this capability is supported by the model.

    - `effort: BetaEffortCapability`

      Effort (reasoning_effort) support and available levels.

      - `high: BetaCapabilitySupport`

        Whether the model supports high effort level.

      - `low: BetaCapabilitySupport`

        Whether the model supports low effort level.

      - `max: BetaCapabilitySupport`

        Whether the model supports max effort level.

      - `medium: BetaCapabilitySupport`

        Whether the model supports medium effort level.

      - `supported: bool`

        Whether this capability is supported by the model.

      - `xhigh: BetaCapabilitySupport`

        Indicates whether a capability is supported.

    - `image_input: BetaCapabilitySupport`

      Whether the model accepts image content blocks.

    - `pdf_input: BetaCapabilitySupport`

      Whether the model accepts PDF content blocks.

    - `structured_outputs: BetaCapabilitySupport`

      Whether the model supports structured output / JSON mode / strict tool schemas.

    - `thinking: BetaThinkingCapability`

      Thinking capability and supported type configurations.

      - `supported: bool`

        Whether this capability is supported by the model.

      - `types: BetaThinkingTypes`

        Supported thinking type configurations.

        - `adaptive: BetaCapabilitySupport`

          Whether the model supports thinking with type 'adaptive' (auto).

        - `enabled: BetaCapabilitySupport`

          Whether the model supports thinking with type 'enabled'.

  - `created_at: Time`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

  - `display_name: String`

    A human-readable name for the model.

  - `max_input_tokens: Integer`

    Maximum input context window size in tokens for this model.

  - `max_tokens: Integer`

    Maximum value for the `max_tokens` parameter when using this model.

  - `type: :model`

    Object type.

    For Models, this is always `"model"`.

    - `:model`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.models.list

puts(page)
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

`beta.models.retrieve(model_id, **kwargs) -> BetaModelInfo`

**get** `/v1/models/{model_id}`

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

### Parameters

- `model_id: String`

  Model identifier or alias.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 24 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"mid-conversation-system-2026-04-07"`

### Returns

- `class BetaModelInfo`

  - `id: String`

    Unique model identifier.

  - `capabilities: BetaModelCapabilities`

    Model capability information.

    - `batch: BetaCapabilitySupport`

      Whether the model supports the Batch API.

      - `supported: bool`

        Whether this capability is supported by the model.

    - `citations: BetaCapabilitySupport`

      Whether the model supports citation generation.

    - `code_execution: BetaCapabilitySupport`

      Whether the model supports code execution tools.

    - `context_management: BetaContextManagementCapability`

      Context management support and available strategies.

      - `clear_thinking_20251015: BetaCapabilitySupport`

        Indicates whether a capability is supported.

      - `clear_tool_uses_20250919: BetaCapabilitySupport`

        Indicates whether a capability is supported.

      - `compact_20260112: BetaCapabilitySupport`

        Indicates whether a capability is supported.

      - `supported: bool`

        Whether this capability is supported by the model.

    - `effort: BetaEffortCapability`

      Effort (reasoning_effort) support and available levels.

      - `high: BetaCapabilitySupport`

        Whether the model supports high effort level.

      - `low: BetaCapabilitySupport`

        Whether the model supports low effort level.

      - `max: BetaCapabilitySupport`

        Whether the model supports max effort level.

      - `medium: BetaCapabilitySupport`

        Whether the model supports medium effort level.

      - `supported: bool`

        Whether this capability is supported by the model.

      - `xhigh: BetaCapabilitySupport`

        Indicates whether a capability is supported.

    - `image_input: BetaCapabilitySupport`

      Whether the model accepts image content blocks.

    - `pdf_input: BetaCapabilitySupport`

      Whether the model accepts PDF content blocks.

    - `structured_outputs: BetaCapabilitySupport`

      Whether the model supports structured output / JSON mode / strict tool schemas.

    - `thinking: BetaThinkingCapability`

      Thinking capability and supported type configurations.

      - `supported: bool`

        Whether this capability is supported by the model.

      - `types: BetaThinkingTypes`

        Supported thinking type configurations.

        - `adaptive: BetaCapabilitySupport`

          Whether the model supports thinking with type 'adaptive' (auto).

        - `enabled: BetaCapabilitySupport`

          Whether the model supports thinking with type 'enabled'.

  - `created_at: Time`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

  - `display_name: String`

    A human-readable name for the model.

  - `max_input_tokens: Integer`

    Maximum input context window size in tokens for this model.

  - `max_tokens: Integer`

    Maximum value for the `max_tokens` parameter when using this model.

  - `type: :model`

    Object type.

    For Models, this is always `"model"`.

    - `:model`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_model_info = anthropic.beta.models.retrieve("model_id")

puts(beta_model_info)
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

### Beta Capability Support

- `class BetaCapabilitySupport`

  Indicates whether a capability is supported.

  - `supported: bool`

    Whether this capability is supported by the model.

### Beta Context Management Capability

- `class BetaContextManagementCapability`

  Context management capability details.

  - `clear_thinking_20251015: BetaCapabilitySupport`

    Indicates whether a capability is supported.

    - `supported: bool`

      Whether this capability is supported by the model.

  - `clear_tool_uses_20250919: BetaCapabilitySupport`

    Indicates whether a capability is supported.

  - `compact_20260112: BetaCapabilitySupport`

    Indicates whether a capability is supported.

  - `supported: bool`

    Whether this capability is supported by the model.

### Beta Effort Capability

- `class BetaEffortCapability`

  Effort (reasoning_effort) capability details.

  - `high: BetaCapabilitySupport`

    Whether the model supports high effort level.

    - `supported: bool`

      Whether this capability is supported by the model.

  - `low: BetaCapabilitySupport`

    Whether the model supports low effort level.

  - `max: BetaCapabilitySupport`

    Whether the model supports max effort level.

  - `medium: BetaCapabilitySupport`

    Whether the model supports medium effort level.

  - `supported: bool`

    Whether this capability is supported by the model.

  - `xhigh: BetaCapabilitySupport`

    Indicates whether a capability is supported.

### Beta Model Capabilities

- `class BetaModelCapabilities`

  Model capability information.

  - `batch: BetaCapabilitySupport`

    Whether the model supports the Batch API.

    - `supported: bool`

      Whether this capability is supported by the model.

  - `citations: BetaCapabilitySupport`

    Whether the model supports citation generation.

  - `code_execution: BetaCapabilitySupport`

    Whether the model supports code execution tools.

  - `context_management: BetaContextManagementCapability`

    Context management support and available strategies.

    - `clear_thinking_20251015: BetaCapabilitySupport`

      Indicates whether a capability is supported.

    - `clear_tool_uses_20250919: BetaCapabilitySupport`

      Indicates whether a capability is supported.

    - `compact_20260112: BetaCapabilitySupport`

      Indicates whether a capability is supported.

    - `supported: bool`

      Whether this capability is supported by the model.

  - `effort: BetaEffortCapability`

    Effort (reasoning_effort) support and available levels.

    - `high: BetaCapabilitySupport`

      Whether the model supports high effort level.

    - `low: BetaCapabilitySupport`

      Whether the model supports low effort level.

    - `max: BetaCapabilitySupport`

      Whether the model supports max effort level.

    - `medium: BetaCapabilitySupport`

      Whether the model supports medium effort level.

    - `supported: bool`

      Whether this capability is supported by the model.

    - `xhigh: BetaCapabilitySupport`

      Indicates whether a capability is supported.

  - `image_input: BetaCapabilitySupport`

    Whether the model accepts image content blocks.

  - `pdf_input: BetaCapabilitySupport`

    Whether the model accepts PDF content blocks.

  - `structured_outputs: BetaCapabilitySupport`

    Whether the model supports structured output / JSON mode / strict tool schemas.

  - `thinking: BetaThinkingCapability`

    Thinking capability and supported type configurations.

    - `supported: bool`

      Whether this capability is supported by the model.

    - `types: BetaThinkingTypes`

      Supported thinking type configurations.

      - `adaptive: BetaCapabilitySupport`

        Whether the model supports thinking with type 'adaptive' (auto).

      - `enabled: BetaCapabilitySupport`

        Whether the model supports thinking with type 'enabled'.

### Beta Model Info

- `class BetaModelInfo`

  - `id: String`

    Unique model identifier.

  - `capabilities: BetaModelCapabilities`

    Model capability information.

    - `batch: BetaCapabilitySupport`

      Whether the model supports the Batch API.

      - `supported: bool`

        Whether this capability is supported by the model.

    - `citations: BetaCapabilitySupport`

      Whether the model supports citation generation.

    - `code_execution: BetaCapabilitySupport`

      Whether the model supports code execution tools.

    - `context_management: BetaContextManagementCapability`

      Context management support and available strategies.

      - `clear_thinking_20251015: BetaCapabilitySupport`

        Indicates whether a capability is supported.

      - `clear_tool_uses_20250919: BetaCapabilitySupport`

        Indicates whether a capability is supported.

      - `compact_20260112: BetaCapabilitySupport`

        Indicates whether a capability is supported.

      - `supported: bool`

        Whether this capability is supported by the model.

    - `effort: BetaEffortCapability`

      Effort (reasoning_effort) support and available levels.

      - `high: BetaCapabilitySupport`

        Whether the model supports high effort level.

      - `low: BetaCapabilitySupport`

        Whether the model supports low effort level.

      - `max: BetaCapabilitySupport`

        Whether the model supports max effort level.

      - `medium: BetaCapabilitySupport`

        Whether the model supports medium effort level.

      - `supported: bool`

        Whether this capability is supported by the model.

      - `xhigh: BetaCapabilitySupport`

        Indicates whether a capability is supported.

    - `image_input: BetaCapabilitySupport`

      Whether the model accepts image content blocks.

    - `pdf_input: BetaCapabilitySupport`

      Whether the model accepts PDF content blocks.

    - `structured_outputs: BetaCapabilitySupport`

      Whether the model supports structured output / JSON mode / strict tool schemas.

    - `thinking: BetaThinkingCapability`

      Thinking capability and supported type configurations.

      - `supported: bool`

        Whether this capability is supported by the model.

      - `types: BetaThinkingTypes`

        Supported thinking type configurations.

        - `adaptive: BetaCapabilitySupport`

          Whether the model supports thinking with type 'adaptive' (auto).

        - `enabled: BetaCapabilitySupport`

          Whether the model supports thinking with type 'enabled'.

  - `created_at: Time`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

  - `display_name: String`

    A human-readable name for the model.

  - `max_input_tokens: Integer`

    Maximum input context window size in tokens for this model.

  - `max_tokens: Integer`

    Maximum value for the `max_tokens` parameter when using this model.

  - `type: :model`

    Object type.

    For Models, this is always `"model"`.

    - `:model`

### Beta Thinking Capability

- `class BetaThinkingCapability`

  Thinking capability details.

  - `supported: bool`

    Whether this capability is supported by the model.

  - `types: BetaThinkingTypes`

    Supported thinking type configurations.

    - `adaptive: BetaCapabilitySupport`

      Whether the model supports thinking with type 'adaptive' (auto).

      - `supported: bool`

        Whether this capability is supported by the model.

    - `enabled: BetaCapabilitySupport`

      Whether the model supports thinking with type 'enabled'.

### Beta Thinking Types

- `class BetaThinkingTypes`

  Supported thinking type configurations.

  - `adaptive: BetaCapabilitySupport`

    Whether the model supports thinking with type 'adaptive' (auto).

    - `supported: bool`

      Whether this capability is supported by the model.

  - `enabled: BetaCapabilitySupport`

    Whether the model supports thinking with type 'enabled'.
