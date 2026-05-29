# Models

## List Models

`models.list(ModelListParams**kwargs)  -> SyncPage[ModelInfo]`

**get** `/v1/models`

List available models.

The Models API response can be used to determine which models are available for use in the API. More recently released models are listed first.

### Parameters

- `after_id: Optional[str]`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: Optional[str]`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `limit: Optional[int]`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 24 more]`

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

    - `"mid-conversation-system-2026-04-07"`

### Returns

- `class ModelInfo: …`

  - `id: str`

    Unique model identifier.

  - `capabilities: Optional[ModelCapabilities]`

    Model capability information.

    - `batch: CapabilitySupport`

      Whether the model supports the Batch API.

      - `supported: bool`

        Whether this capability is supported by the model.

    - `citations: CapabilitySupport`

      Whether the model supports citation generation.

    - `code_execution: CapabilitySupport`

      Whether the model supports code execution tools.

    - `context_management: ContextManagementCapability`

      Context management support and available strategies.

      - `clear_thinking_20251015: Optional[CapabilitySupport]`

        Indicates whether a capability is supported.

      - `clear_tool_uses_20250919: Optional[CapabilitySupport]`

        Indicates whether a capability is supported.

      - `compact_20260112: Optional[CapabilitySupport]`

        Indicates whether a capability is supported.

      - `supported: bool`

        Whether this capability is supported by the model.

    - `effort: EffortCapability`

      Effort (reasoning_effort) support and available levels.

      - `high: CapabilitySupport`

        Whether the model supports high effort level.

      - `low: CapabilitySupport`

        Whether the model supports low effort level.

      - `max: CapabilitySupport`

        Whether the model supports max effort level.

      - `medium: CapabilitySupport`

        Whether the model supports medium effort level.

      - `supported: bool`

        Whether this capability is supported by the model.

      - `xhigh: Optional[CapabilitySupport]`

        Indicates whether a capability is supported.

    - `image_input: CapabilitySupport`

      Whether the model accepts image content blocks.

    - `pdf_input: CapabilitySupport`

      Whether the model accepts PDF content blocks.

    - `structured_outputs: CapabilitySupport`

      Whether the model supports structured output / JSON mode / strict tool schemas.

    - `thinking: ThinkingCapability`

      Thinking capability and supported type configurations.

      - `supported: bool`

        Whether this capability is supported by the model.

      - `types: ThinkingTypes`

        Supported thinking type configurations.

        - `adaptive: CapabilitySupport`

          Whether the model supports thinking with type 'adaptive' (auto).

        - `enabled: CapabilitySupport`

          Whether the model supports thinking with type 'enabled'.

  - `created_at: datetime`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

  - `display_name: str`

    A human-readable name for the model.

  - `max_input_tokens: Optional[int]`

    Maximum input context window size in tokens for this model.

  - `max_tokens: Optional[int]`

    Maximum value for the `max_tokens` parameter when using this model.

  - `type: Literal["model"]`

    Object type.

    For Models, this is always `"model"`.

    - `"model"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.models.list()
page = page.data[0]
print(page.id)
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

`models.retrieve(strmodel_id, ModelRetrieveParams**kwargs)  -> ModelInfo`

**get** `/v1/models/{model_id}`

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

### Parameters

- `model_id: str`

  Model identifier or alias.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 24 more]`

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

    - `"mid-conversation-system-2026-04-07"`

### Returns

- `class ModelInfo: …`

  - `id: str`

    Unique model identifier.

  - `capabilities: Optional[ModelCapabilities]`

    Model capability information.

    - `batch: CapabilitySupport`

      Whether the model supports the Batch API.

      - `supported: bool`

        Whether this capability is supported by the model.

    - `citations: CapabilitySupport`

      Whether the model supports citation generation.

    - `code_execution: CapabilitySupport`

      Whether the model supports code execution tools.

    - `context_management: ContextManagementCapability`

      Context management support and available strategies.

      - `clear_thinking_20251015: Optional[CapabilitySupport]`

        Indicates whether a capability is supported.

      - `clear_tool_uses_20250919: Optional[CapabilitySupport]`

        Indicates whether a capability is supported.

      - `compact_20260112: Optional[CapabilitySupport]`

        Indicates whether a capability is supported.

      - `supported: bool`

        Whether this capability is supported by the model.

    - `effort: EffortCapability`

      Effort (reasoning_effort) support and available levels.

      - `high: CapabilitySupport`

        Whether the model supports high effort level.

      - `low: CapabilitySupport`

        Whether the model supports low effort level.

      - `max: CapabilitySupport`

        Whether the model supports max effort level.

      - `medium: CapabilitySupport`

        Whether the model supports medium effort level.

      - `supported: bool`

        Whether this capability is supported by the model.

      - `xhigh: Optional[CapabilitySupport]`

        Indicates whether a capability is supported.

    - `image_input: CapabilitySupport`

      Whether the model accepts image content blocks.

    - `pdf_input: CapabilitySupport`

      Whether the model accepts PDF content blocks.

    - `structured_outputs: CapabilitySupport`

      Whether the model supports structured output / JSON mode / strict tool schemas.

    - `thinking: ThinkingCapability`

      Thinking capability and supported type configurations.

      - `supported: bool`

        Whether this capability is supported by the model.

      - `types: ThinkingTypes`

        Supported thinking type configurations.

        - `adaptive: CapabilitySupport`

          Whether the model supports thinking with type 'adaptive' (auto).

        - `enabled: CapabilitySupport`

          Whether the model supports thinking with type 'enabled'.

  - `created_at: datetime`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

  - `display_name: str`

    A human-readable name for the model.

  - `max_input_tokens: Optional[int]`

    Maximum input context window size in tokens for this model.

  - `max_tokens: Optional[int]`

    Maximum value for the `max_tokens` parameter when using this model.

  - `type: Literal["model"]`

    Object type.

    For Models, this is always `"model"`.

    - `"model"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
model_info = client.models.retrieve(
    model_id="model_id",
)
print(model_info.id)
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

- `class CapabilitySupport: …`

  Indicates whether a capability is supported.

  - `supported: bool`

    Whether this capability is supported by the model.

### Context Management Capability

- `class ContextManagementCapability: …`

  Context management capability details.

  - `clear_thinking_20251015: Optional[CapabilitySupport]`

    Indicates whether a capability is supported.

    - `supported: bool`

      Whether this capability is supported by the model.

  - `clear_tool_uses_20250919: Optional[CapabilitySupport]`

    Indicates whether a capability is supported.

  - `compact_20260112: Optional[CapabilitySupport]`

    Indicates whether a capability is supported.

  - `supported: bool`

    Whether this capability is supported by the model.

### Effort Capability

- `class EffortCapability: …`

  Effort (reasoning_effort) capability details.

  - `high: CapabilitySupport`

    Whether the model supports high effort level.

    - `supported: bool`

      Whether this capability is supported by the model.

  - `low: CapabilitySupport`

    Whether the model supports low effort level.

  - `max: CapabilitySupport`

    Whether the model supports max effort level.

  - `medium: CapabilitySupport`

    Whether the model supports medium effort level.

  - `supported: bool`

    Whether this capability is supported by the model.

  - `xhigh: Optional[CapabilitySupport]`

    Indicates whether a capability is supported.

### Model Capabilities

- `class ModelCapabilities: …`

  Model capability information.

  - `batch: CapabilitySupport`

    Whether the model supports the Batch API.

    - `supported: bool`

      Whether this capability is supported by the model.

  - `citations: CapabilitySupport`

    Whether the model supports citation generation.

  - `code_execution: CapabilitySupport`

    Whether the model supports code execution tools.

  - `context_management: ContextManagementCapability`

    Context management support and available strategies.

    - `clear_thinking_20251015: Optional[CapabilitySupport]`

      Indicates whether a capability is supported.

    - `clear_tool_uses_20250919: Optional[CapabilitySupport]`

      Indicates whether a capability is supported.

    - `compact_20260112: Optional[CapabilitySupport]`

      Indicates whether a capability is supported.

    - `supported: bool`

      Whether this capability is supported by the model.

  - `effort: EffortCapability`

    Effort (reasoning_effort) support and available levels.

    - `high: CapabilitySupport`

      Whether the model supports high effort level.

    - `low: CapabilitySupport`

      Whether the model supports low effort level.

    - `max: CapabilitySupport`

      Whether the model supports max effort level.

    - `medium: CapabilitySupport`

      Whether the model supports medium effort level.

    - `supported: bool`

      Whether this capability is supported by the model.

    - `xhigh: Optional[CapabilitySupport]`

      Indicates whether a capability is supported.

  - `image_input: CapabilitySupport`

    Whether the model accepts image content blocks.

  - `pdf_input: CapabilitySupport`

    Whether the model accepts PDF content blocks.

  - `structured_outputs: CapabilitySupport`

    Whether the model supports structured output / JSON mode / strict tool schemas.

  - `thinking: ThinkingCapability`

    Thinking capability and supported type configurations.

    - `supported: bool`

      Whether this capability is supported by the model.

    - `types: ThinkingTypes`

      Supported thinking type configurations.

      - `adaptive: CapabilitySupport`

        Whether the model supports thinking with type 'adaptive' (auto).

      - `enabled: CapabilitySupport`

        Whether the model supports thinking with type 'enabled'.

### Model Info

- `class ModelInfo: …`

  - `id: str`

    Unique model identifier.

  - `capabilities: Optional[ModelCapabilities]`

    Model capability information.

    - `batch: CapabilitySupport`

      Whether the model supports the Batch API.

      - `supported: bool`

        Whether this capability is supported by the model.

    - `citations: CapabilitySupport`

      Whether the model supports citation generation.

    - `code_execution: CapabilitySupport`

      Whether the model supports code execution tools.

    - `context_management: ContextManagementCapability`

      Context management support and available strategies.

      - `clear_thinking_20251015: Optional[CapabilitySupport]`

        Indicates whether a capability is supported.

      - `clear_tool_uses_20250919: Optional[CapabilitySupport]`

        Indicates whether a capability is supported.

      - `compact_20260112: Optional[CapabilitySupport]`

        Indicates whether a capability is supported.

      - `supported: bool`

        Whether this capability is supported by the model.

    - `effort: EffortCapability`

      Effort (reasoning_effort) support and available levels.

      - `high: CapabilitySupport`

        Whether the model supports high effort level.

      - `low: CapabilitySupport`

        Whether the model supports low effort level.

      - `max: CapabilitySupport`

        Whether the model supports max effort level.

      - `medium: CapabilitySupport`

        Whether the model supports medium effort level.

      - `supported: bool`

        Whether this capability is supported by the model.

      - `xhigh: Optional[CapabilitySupport]`

        Indicates whether a capability is supported.

    - `image_input: CapabilitySupport`

      Whether the model accepts image content blocks.

    - `pdf_input: CapabilitySupport`

      Whether the model accepts PDF content blocks.

    - `structured_outputs: CapabilitySupport`

      Whether the model supports structured output / JSON mode / strict tool schemas.

    - `thinking: ThinkingCapability`

      Thinking capability and supported type configurations.

      - `supported: bool`

        Whether this capability is supported by the model.

      - `types: ThinkingTypes`

        Supported thinking type configurations.

        - `adaptive: CapabilitySupport`

          Whether the model supports thinking with type 'adaptive' (auto).

        - `enabled: CapabilitySupport`

          Whether the model supports thinking with type 'enabled'.

  - `created_at: datetime`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

  - `display_name: str`

    A human-readable name for the model.

  - `max_input_tokens: Optional[int]`

    Maximum input context window size in tokens for this model.

  - `max_tokens: Optional[int]`

    Maximum value for the `max_tokens` parameter when using this model.

  - `type: Literal["model"]`

    Object type.

    For Models, this is always `"model"`.

    - `"model"`

### Thinking Capability

- `class ThinkingCapability: …`

  Thinking capability details.

  - `supported: bool`

    Whether this capability is supported by the model.

  - `types: ThinkingTypes`

    Supported thinking type configurations.

    - `adaptive: CapabilitySupport`

      Whether the model supports thinking with type 'adaptive' (auto).

      - `supported: bool`

        Whether this capability is supported by the model.

    - `enabled: CapabilitySupport`

      Whether the model supports thinking with type 'enabled'.

### Thinking Types

- `class ThinkingTypes: …`

  Supported thinking type configurations.

  - `adaptive: CapabilitySupport`

    Whether the model supports thinking with type 'adaptive' (auto).

    - `supported: bool`

      Whether this capability is supported by the model.

  - `enabled: CapabilitySupport`

    Whether the model supports thinking with type 'enabled'.
