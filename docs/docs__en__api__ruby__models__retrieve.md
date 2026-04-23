## Retrieve

`models.retrieve(model_id, **kwargs) -> ModelInfo`

**get** `/v1/models/{model_id}`

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

### Parameters

- `model_id: String`

  Model identifier or alias.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 19 more`

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

    - `:"advisor-tool-2026-03-01"`

### Returns

- `class ModelInfo`

  - `id: String`

    Unique model identifier.

  - `capabilities: ModelCapabilities`

    Model capability information.

    - `batch: CapabilitySupport`

      Whether the model supports the Batch API.

      - `supported: bool`

        Whether this capability is supported by the model.

    - `citations: CapabilitySupport`

      Whether the model supports citation generation.

      - `supported: bool`

        Whether this capability is supported by the model.

    - `code_execution: CapabilitySupport`

      Whether the model supports code execution tools.

      - `supported: bool`

        Whether this capability is supported by the model.

    - `context_management: ContextManagementCapability`

      Context management support and available strategies.

      - `clear_thinking_20251015: CapabilitySupport`

        Indicates whether a capability is supported.

        - `supported: bool`

          Whether this capability is supported by the model.

      - `clear_tool_uses_20250919: CapabilitySupport`

        Indicates whether a capability is supported.

        - `supported: bool`

          Whether this capability is supported by the model.

      - `compact_20260112: CapabilitySupport`

        Indicates whether a capability is supported.

        - `supported: bool`

          Whether this capability is supported by the model.

      - `supported: bool`

        Whether this capability is supported by the model.

    - `effort: EffortCapability`

      Effort (reasoning_effort) support and available levels.

      - `high: CapabilitySupport`

        Whether the model supports high effort level.

        - `supported: bool`

          Whether this capability is supported by the model.

      - `low: CapabilitySupport`

        Whether the model supports low effort level.

        - `supported: bool`

          Whether this capability is supported by the model.

      - `max: CapabilitySupport`

        Whether the model supports max effort level.

        - `supported: bool`

          Whether this capability is supported by the model.

      - `medium: CapabilitySupport`

        Whether the model supports medium effort level.

        - `supported: bool`

          Whether this capability is supported by the model.

      - `supported: bool`

        Whether this capability is supported by the model.

    - `image_input: CapabilitySupport`

      Whether the model accepts image content blocks.

      - `supported: bool`

        Whether this capability is supported by the model.

    - `pdf_input: CapabilitySupport`

      Whether the model accepts PDF content blocks.

      - `supported: bool`

        Whether this capability is supported by the model.

    - `structured_outputs: CapabilitySupport`

      Whether the model supports structured output / JSON mode / strict tool schemas.

      - `supported: bool`

        Whether this capability is supported by the model.

    - `thinking: ThinkingCapability`

      Thinking capability and supported type configurations.

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

          - `supported: bool`

            Whether this capability is supported by the model.

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

model_info = anthropic.models.retrieve("model_id")

puts(model_info)
```
