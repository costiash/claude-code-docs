# Models

## List

`$ ant models list`

**get** `/v1/models`

List available models.

The Models API response can be used to determine which models are available for use in the API. More recently released models are listed first.

### Parameters

- `--after-id: optional string`

  Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `--before-id: optional string`

  Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `--limit: optional number`

  Query param: Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `ListResponse_ModelInfo_: object { data, first_id, has_more, last_id }`

  - `data: array of ModelInfo`

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

      - `effort: object { high, low, max, 3 more }`

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

        - `xhigh: object { supported }`

          Indicates whether a capability is supported.

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

  - `first_id: string`

    First ID in the `data` list. Can be used as the `before_id` for the previous page.

  - `has_more: boolean`

    Indicates if there are more results in the requested page direction.

  - `last_id: string`

    Last ID in the `data` list. Can be used as the `after_id` for the next page.

### Example

```cli
ant models list \
  --api-key my-anthropic-api-key
```

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

    - `effort: object { high, low, max, 3 more }`

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

      - `xhigh: object { supported }`

        Indicates whether a capability is supported.

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

## Domain Types

### Capability Support

- `capability_support: object { supported }`

  Indicates whether a capability is supported.

  - `supported: boolean`

    Whether this capability is supported by the model.

### Context Management Capability

- `context_management_capability: object { clear_thinking_20251015, clear_tool_uses_20250919, compact_20260112, supported }`

  Context management capability details.

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

### Effort Capability

- `effort_capability: object { high, low, max, 3 more }`

  Effort (reasoning_effort) capability details.

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

  - `xhigh: object { supported }`

    Indicates whether a capability is supported.

    - `supported: boolean`

      Whether this capability is supported by the model.

### Model Capabilities

- `model_capabilities: object { batch, citations, code_execution, 6 more }`

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

  - `effort: object { high, low, max, 3 more }`

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

    - `xhigh: object { supported }`

      Indicates whether a capability is supported.

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

### Model Info

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

    - `effort: object { high, low, max, 3 more }`

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

      - `xhigh: object { supported }`

        Indicates whether a capability is supported.

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

### Thinking Capability

- `thinking_capability: object { supported, types }`

  Thinking capability details.

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

### Thinking Types

- `thinking_types: object { adaptive, enabled }`

  Supported thinking type configurations.

  - `adaptive: object { supported }`

    Whether the model supports thinking with type 'adaptive' (auto).

    - `supported: boolean`

      Whether this capability is supported by the model.

  - `enabled: object { supported }`

    Whether the model supports thinking with type 'enabled'.

    - `supported: boolean`

      Whether this capability is supported by the model.
