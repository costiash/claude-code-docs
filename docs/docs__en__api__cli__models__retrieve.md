## Retrieve

`$ ant models retrieve`

**get** `/v1/models/{model_id}`

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

### Parameters

- `--model-id: string`

  Model identifier or alias.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `model_info: object { id, capabilities, created_at, 4 more }`

  - `id: string`

    Unique model identifier.

  - `capabilities: object { batch, citations, code_execution, 6 more }`

    Model capability information.

    - `batch: object { supported }`

      Whether the model supports the Batch API.

      - `supported: boolean`

        Whether this capability is supported by the model.

    - `citations: object { supported }`

      Whether the model supports citation generation.

      - `supported: boolean`

        Whether this capability is supported by the model.

    - `code_execution: object { supported }`

      Whether the model supports code execution tools.

      - `supported: boolean`

        Whether this capability is supported by the model.

    - `context_management: object { clear_thinking_20251015, clear_tool_uses_20250919, compact_20260112, supported }`

      Context management support and available strategies.

      - `clear_thinking_20251015: object { supported }`

        Indicates whether a capability is supported.

        - `supported: boolean`

          Whether this capability is supported by the model.

      - `clear_tool_uses_20250919: object { supported }`

        Indicates whether a capability is supported.

        - `supported: boolean`

          Whether this capability is supported by the model.

      - `compact_20260112: object { supported }`

        Indicates whether a capability is supported.

        - `supported: boolean`

          Whether this capability is supported by the model.

      - `supported: boolean`

        Whether this capability is supported by the model.

    - `effort: object { high, low, max, 2 more }`

      Effort (reasoning_effort) support and available levels.

      - `high: object { supported }`

        Whether the model supports high effort level.

        - `supported: boolean`

          Whether this capability is supported by the model.

      - `low: object { supported }`

        Whether the model supports low effort level.

        - `supported: boolean`

          Whether this capability is supported by the model.

      - `max: object { supported }`

        Whether the model supports max effort level.

        - `supported: boolean`

          Whether this capability is supported by the model.

      - `medium: object { supported }`

        Whether the model supports medium effort level.

        - `supported: boolean`

          Whether this capability is supported by the model.

      - `supported: boolean`

        Whether this capability is supported by the model.

    - `image_input: object { supported }`

      Whether the model accepts image content blocks.

      - `supported: boolean`

        Whether this capability is supported by the model.

    - `pdf_input: object { supported }`

      Whether the model accepts PDF content blocks.

      - `supported: boolean`

        Whether this capability is supported by the model.

    - `structured_outputs: object { supported }`

      Whether the model supports structured output / JSON mode / strict tool schemas.

      - `supported: boolean`

        Whether this capability is supported by the model.

    - `thinking: object { supported, types }`

      Thinking capability and supported type configurations.

      - `supported: boolean`

        Whether this capability is supported by the model.

      - `types: object { adaptive, enabled }`

        Supported thinking type configurations.

        - `adaptive: object { supported }`

          Whether the model supports thinking with type 'adaptive' (auto).

          - `supported: boolean`

            Whether this capability is supported by the model.

        - `enabled: object { supported }`

          Whether the model supports thinking with type 'enabled'.

          - `supported: boolean`

            Whether this capability is supported by the model.

  - `created_at: string`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

  - `display_name: string`

    A human-readable name for the model.

  - `max_input_tokens: number`

    Maximum input context window size in tokens for this model.

  - `max_tokens: number`

    Maximum value for the `max_tokens` parameter when using this model.

  - `type: "model"`

    Object type.

    For Models, this is always `"model"`.

### Example

```cli
ant models retrieve \
  --api-key my-anthropic-api-key \
  --model-id model_id
```
