## Get a Model

`beta.models.retrieve(strmodel_id, ModelRetrieveParams**kwargs)  -> BetaModelInfo`

**get** `/v1/models/{model_id}`

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

### Parameters

- `model_id: str`

  Model identifier or alias.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 23 more]`

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

### Returns

- `class BetaModelInfo: …`

  - `id: str`

    Unique model identifier.

  - `capabilities: Optional[BetaModelCapabilities]`

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

      - `clear_thinking_20251015: Optional[BetaCapabilitySupport]`

        Indicates whether a capability is supported.

      - `clear_tool_uses_20250919: Optional[BetaCapabilitySupport]`

        Indicates whether a capability is supported.

      - `compact_20260112: Optional[BetaCapabilitySupport]`

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

      - `xhigh: Optional[BetaCapabilitySupport]`

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
beta_model_info = client.beta.models.retrieve(
    model_id="model_id",
)
print(beta_model_info.id)
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
