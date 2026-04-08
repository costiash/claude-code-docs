## Retrieve

`ModelInfo models().retrieve(ModelRetrieveParamsparams = ModelRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/models/{model_id}`

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

### Parameters

- `ModelRetrieveParams params`

  - `Optional<String> modelId`

    Model identifier or alias.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

### Returns

- `class ModelInfo:`

  - `String id`

    Unique model identifier.

  - `Optional<ModelCapabilities> capabilities`

    Model capability information.

    - `CapabilitySupport batch`

      Whether the model supports the Batch API.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `CapabilitySupport citations`

      Whether the model supports citation generation.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `CapabilitySupport codeExecution`

      Whether the model supports code execution tools.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `ContextManagementCapability contextManagement`

      Context management support and available strategies.

      - `Optional<CapabilitySupport> clearThinking20251015`

        Indicates whether a capability is supported.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `Optional<CapabilitySupport> clearToolUses20250919`

        Indicates whether a capability is supported.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `Optional<CapabilitySupport> compact20260112`

        Indicates whether a capability is supported.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `EffortCapability effort`

      Effort (reasoning_effort) support and available levels.

      - `CapabilitySupport high`

        Whether the model supports high effort level.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `CapabilitySupport low`

        Whether the model supports low effort level.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `CapabilitySupport max`

        Whether the model supports max effort level.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `CapabilitySupport medium`

        Whether the model supports medium effort level.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `CapabilitySupport imageInput`

      Whether the model accepts image content blocks.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `CapabilitySupport pdfInput`

      Whether the model accepts PDF content blocks.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `CapabilitySupport structuredOutputs`

      Whether the model supports structured output / JSON mode / strict tool schemas.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `ThinkingCapability thinking`

      Thinking capability and supported type configurations.

      - `boolean supported`

        Whether this capability is supported by the model.

      - `ThinkingTypes types`

        Supported thinking type configurations.

        - `CapabilitySupport adaptive`

          Whether the model supports thinking with type 'adaptive' (auto).

          - `boolean supported`

            Whether this capability is supported by the model.

        - `CapabilitySupport enabled`

          Whether the model supports thinking with type 'enabled'.

          - `boolean supported`

            Whether this capability is supported by the model.

  - `LocalDateTime createdAt`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

  - `String displayName`

    A human-readable name for the model.

  - `Optional<Long> maxInputTokens`

    Maximum input context window size in tokens for this model.

  - `Optional<Long> maxTokens`

    Maximum value for the `max_tokens` parameter when using this model.

  - `JsonValue; type "model"constant`

    Object type.

    For Models, this is always `"model"`.

    - `MODEL("model")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.models.ModelInfo;
import com.anthropic.models.models.ModelRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ModelInfo modelInfo = client.models().retrieve("model_id");
    }
}
```
