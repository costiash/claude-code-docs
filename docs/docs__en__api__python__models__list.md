## List

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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 21 more]`

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

      - `supported: bool`

        Whether this capability is supported by the model.

    - `code_execution: CapabilitySupport`

      Whether the model supports code execution tools.

      - `supported: bool`

        Whether this capability is supported by the model.

    - `context_management: ContextManagementCapability`

      Context management support and available strategies.

      - `clear_thinking_20251015: Optional[CapabilitySupport]`

        Indicates whether a capability is supported.

        - `supported: bool`

          Whether this capability is supported by the model.

      - `clear_tool_uses_20250919: Optional[CapabilitySupport]`

        Indicates whether a capability is supported.

        - `supported: bool`

          Whether this capability is supported by the model.

      - `compact_20260112: Optional[CapabilitySupport]`

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

      - `xhigh: Optional[CapabilitySupport]`

        Indicates whether a capability is supported.

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
