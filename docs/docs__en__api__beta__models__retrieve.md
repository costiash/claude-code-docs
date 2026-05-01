## Retrieve

**get** `/v1/models/{model_id}`

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

### Path Parameters

- `model_id: string`

  Model identifier or alias.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 20 more`

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

### Returns

- `BetaModelInfo = object { id, capabilities, created_at, 4 more }`

  - `id: string`

    Unique model identifier.

  - `capabilities: BetaModelCapabilities`

    Model capability information.

    - `batch: BetaCapabilitySupport`

      Whether the model supports the Batch API.

      - `supported: boolean`

        Whether this capability is supported by the model.

    - `citations: BetaCapabilitySupport`

      Whether the model supports citation generation.

      - `supported: boolean`

        Whether this capability is supported by the model.

    - `code_execution: BetaCapabilitySupport`

      Whether the model supports code execution tools.

      - `supported: boolean`

        Whether this capability is supported by the model.

    - `context_management: BetaContextManagementCapability`

      Context management support and available strategies.

      - `clear_thinking_20251015: BetaCapabilitySupport`

        Indicates whether a capability is supported.

        - `supported: boolean`

          Whether this capability is supported by the model.

      - `clear_tool_uses_20250919: BetaCapabilitySupport`

        Indicates whether a capability is supported.

        - `supported: boolean`

          Whether this capability is supported by the model.

      - `compact_20260112: BetaCapabilitySupport`

        Indicates whether a capability is supported.

        - `supported: boolean`

          Whether this capability is supported by the model.

      - `supported: boolean`

        Whether this capability is supported by the model.

    - `effort: BetaEffortCapability`

      Effort (reasoning_effort) support and available levels.

      - `high: BetaCapabilitySupport`

        Whether the model supports high effort level.

        - `supported: boolean`

          Whether this capability is supported by the model.

      - `low: BetaCapabilitySupport`

        Whether the model supports low effort level.

        - `supported: boolean`

          Whether this capability is supported by the model.

      - `max: BetaCapabilitySupport`

        Whether the model supports max effort level.

        - `supported: boolean`

          Whether this capability is supported by the model.

      - `medium: BetaCapabilitySupport`

        Whether the model supports medium effort level.

        - `supported: boolean`

          Whether this capability is supported by the model.

      - `supported: boolean`

        Whether this capability is supported by the model.

      - `xhigh: BetaCapabilitySupport`

        Indicates whether a capability is supported.

        - `supported: boolean`

          Whether this capability is supported by the model.

    - `image_input: BetaCapabilitySupport`

      Whether the model accepts image content blocks.

      - `supported: boolean`

        Whether this capability is supported by the model.

    - `pdf_input: BetaCapabilitySupport`

      Whether the model accepts PDF content blocks.

      - `supported: boolean`

        Whether this capability is supported by the model.

    - `structured_outputs: BetaCapabilitySupport`

      Whether the model supports structured output / JSON mode / strict tool schemas.

      - `supported: boolean`

        Whether this capability is supported by the model.

    - `thinking: BetaThinkingCapability`

      Thinking capability and supported type configurations.

      - `supported: boolean`

        Whether this capability is supported by the model.

      - `types: BetaThinkingTypes`

        Supported thinking type configurations.

        - `adaptive: BetaCapabilitySupport`

          Whether the model supports thinking with type 'adaptive' (auto).

          - `supported: boolean`

            Whether this capability is supported by the model.

        - `enabled: BetaCapabilitySupport`

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

    - `"model"`

### Example

```http
curl https://api.anthropic.com/v1/models/$MODEL_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```
