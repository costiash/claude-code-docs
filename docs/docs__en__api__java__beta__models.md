# Models

## List

`ModelListPage beta().models().list(ModelListParamsparams = ModelListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/models`

List available models.

The Models API response can be used to determine which models are available for use in the API. More recently released models are listed first.

### Parameters

- `ModelListParams params`

  - `Optional<String> afterId`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `Optional<String> beforeId`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `Optional<Long> limit`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

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

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

### Returns

- `class BetaModelInfo:`

  - `String id`

    Unique model identifier.

  - `Optional<BetaModelCapabilities> capabilities`

    Model capability information.

    - `BetaCapabilitySupport batch`

      Whether the model supports the Batch API.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaCapabilitySupport citations`

      Whether the model supports citation generation.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaCapabilitySupport codeExecution`

      Whether the model supports code execution tools.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaContextManagementCapability contextManagement`

      Context management support and available strategies.

      - `Optional<BetaCapabilitySupport> clearThinking20251015`

        Indicates whether a capability is supported.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `Optional<BetaCapabilitySupport> clearToolUses20250919`

        Indicates whether a capability is supported.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `Optional<BetaCapabilitySupport> compact20260112`

        Indicates whether a capability is supported.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaEffortCapability effort`

      Effort (reasoning_effort) support and available levels.

      - `BetaCapabilitySupport high`

        Whether the model supports high effort level.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `BetaCapabilitySupport low`

        Whether the model supports low effort level.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `BetaCapabilitySupport max`

        Whether the model supports max effort level.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `BetaCapabilitySupport medium`

        Whether the model supports medium effort level.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `boolean supported`

        Whether this capability is supported by the model.

      - `Optional<BetaCapabilitySupport> xhigh`

        Indicates whether a capability is supported.

        - `boolean supported`

          Whether this capability is supported by the model.

    - `BetaCapabilitySupport imageInput`

      Whether the model accepts image content blocks.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaCapabilitySupport pdfInput`

      Whether the model accepts PDF content blocks.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaCapabilitySupport structuredOutputs`

      Whether the model supports structured output / JSON mode / strict tool schemas.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaThinkingCapability thinking`

      Thinking capability and supported type configurations.

      - `boolean supported`

        Whether this capability is supported by the model.

      - `BetaThinkingTypes types`

        Supported thinking type configurations.

        - `BetaCapabilitySupport adaptive`

          Whether the model supports thinking with type 'adaptive' (auto).

          - `boolean supported`

            Whether this capability is supported by the model.

        - `BetaCapabilitySupport enabled`

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
import com.anthropic.models.beta.models.ModelListPage;
import com.anthropic.models.beta.models.ModelListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ModelListPage page = client.beta().models().list();
    }
}
```

## Retrieve

`BetaModelInfo beta().models().retrieve(ModelRetrieveParamsparams = ModelRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

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

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

### Returns

- `class BetaModelInfo:`

  - `String id`

    Unique model identifier.

  - `Optional<BetaModelCapabilities> capabilities`

    Model capability information.

    - `BetaCapabilitySupport batch`

      Whether the model supports the Batch API.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaCapabilitySupport citations`

      Whether the model supports citation generation.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaCapabilitySupport codeExecution`

      Whether the model supports code execution tools.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaContextManagementCapability contextManagement`

      Context management support and available strategies.

      - `Optional<BetaCapabilitySupport> clearThinking20251015`

        Indicates whether a capability is supported.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `Optional<BetaCapabilitySupport> clearToolUses20250919`

        Indicates whether a capability is supported.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `Optional<BetaCapabilitySupport> compact20260112`

        Indicates whether a capability is supported.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaEffortCapability effort`

      Effort (reasoning_effort) support and available levels.

      - `BetaCapabilitySupport high`

        Whether the model supports high effort level.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `BetaCapabilitySupport low`

        Whether the model supports low effort level.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `BetaCapabilitySupport max`

        Whether the model supports max effort level.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `BetaCapabilitySupport medium`

        Whether the model supports medium effort level.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `boolean supported`

        Whether this capability is supported by the model.

      - `Optional<BetaCapabilitySupport> xhigh`

        Indicates whether a capability is supported.

        - `boolean supported`

          Whether this capability is supported by the model.

    - `BetaCapabilitySupport imageInput`

      Whether the model accepts image content blocks.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaCapabilitySupport pdfInput`

      Whether the model accepts PDF content blocks.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaCapabilitySupport structuredOutputs`

      Whether the model supports structured output / JSON mode / strict tool schemas.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaThinkingCapability thinking`

      Thinking capability and supported type configurations.

      - `boolean supported`

        Whether this capability is supported by the model.

      - `BetaThinkingTypes types`

        Supported thinking type configurations.

        - `BetaCapabilitySupport adaptive`

          Whether the model supports thinking with type 'adaptive' (auto).

          - `boolean supported`

            Whether this capability is supported by the model.

        - `BetaCapabilitySupport enabled`

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
import com.anthropic.models.beta.models.BetaModelInfo;
import com.anthropic.models.beta.models.ModelRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaModelInfo betaModelInfo = client.beta().models().retrieve("model_id");
    }
}
```

## Domain Types

### Beta Capability Support

- `class BetaCapabilitySupport:`

  Indicates whether a capability is supported.

  - `boolean supported`

    Whether this capability is supported by the model.

### Beta Context Management Capability

- `class BetaContextManagementCapability:`

  Context management capability details.

  - `Optional<BetaCapabilitySupport> clearThinking20251015`

    Indicates whether a capability is supported.

    - `boolean supported`

      Whether this capability is supported by the model.

  - `Optional<BetaCapabilitySupport> clearToolUses20250919`

    Indicates whether a capability is supported.

    - `boolean supported`

      Whether this capability is supported by the model.

  - `Optional<BetaCapabilitySupport> compact20260112`

    Indicates whether a capability is supported.

    - `boolean supported`

      Whether this capability is supported by the model.

  - `boolean supported`

    Whether this capability is supported by the model.

### Beta Effort Capability

- `class BetaEffortCapability:`

  Effort (reasoning_effort) capability details.

  - `BetaCapabilitySupport high`

    Whether the model supports high effort level.

    - `boolean supported`

      Whether this capability is supported by the model.

  - `BetaCapabilitySupport low`

    Whether the model supports low effort level.

    - `boolean supported`

      Whether this capability is supported by the model.

  - `BetaCapabilitySupport max`

    Whether the model supports max effort level.

    - `boolean supported`

      Whether this capability is supported by the model.

  - `BetaCapabilitySupport medium`

    Whether the model supports medium effort level.

    - `boolean supported`

      Whether this capability is supported by the model.

  - `boolean supported`

    Whether this capability is supported by the model.

  - `Optional<BetaCapabilitySupport> xhigh`

    Indicates whether a capability is supported.

    - `boolean supported`

      Whether this capability is supported by the model.

### Beta Model Capabilities

- `class BetaModelCapabilities:`

  Model capability information.

  - `BetaCapabilitySupport batch`

    Whether the model supports the Batch API.

    - `boolean supported`

      Whether this capability is supported by the model.

  - `BetaCapabilitySupport citations`

    Whether the model supports citation generation.

    - `boolean supported`

      Whether this capability is supported by the model.

  - `BetaCapabilitySupport codeExecution`

    Whether the model supports code execution tools.

    - `boolean supported`

      Whether this capability is supported by the model.

  - `BetaContextManagementCapability contextManagement`

    Context management support and available strategies.

    - `Optional<BetaCapabilitySupport> clearThinking20251015`

      Indicates whether a capability is supported.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `Optional<BetaCapabilitySupport> clearToolUses20250919`

      Indicates whether a capability is supported.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `Optional<BetaCapabilitySupport> compact20260112`

      Indicates whether a capability is supported.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `boolean supported`

      Whether this capability is supported by the model.

  - `BetaEffortCapability effort`

    Effort (reasoning_effort) support and available levels.

    - `BetaCapabilitySupport high`

      Whether the model supports high effort level.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaCapabilitySupport low`

      Whether the model supports low effort level.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaCapabilitySupport max`

      Whether the model supports max effort level.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaCapabilitySupport medium`

      Whether the model supports medium effort level.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `boolean supported`

      Whether this capability is supported by the model.

    - `Optional<BetaCapabilitySupport> xhigh`

      Indicates whether a capability is supported.

      - `boolean supported`

        Whether this capability is supported by the model.

  - `BetaCapabilitySupport imageInput`

    Whether the model accepts image content blocks.

    - `boolean supported`

      Whether this capability is supported by the model.

  - `BetaCapabilitySupport pdfInput`

    Whether the model accepts PDF content blocks.

    - `boolean supported`

      Whether this capability is supported by the model.

  - `BetaCapabilitySupport structuredOutputs`

    Whether the model supports structured output / JSON mode / strict tool schemas.

    - `boolean supported`

      Whether this capability is supported by the model.

  - `BetaThinkingCapability thinking`

    Thinking capability and supported type configurations.

    - `boolean supported`

      Whether this capability is supported by the model.

    - `BetaThinkingTypes types`

      Supported thinking type configurations.

      - `BetaCapabilitySupport adaptive`

        Whether the model supports thinking with type 'adaptive' (auto).

        - `boolean supported`

          Whether this capability is supported by the model.

      - `BetaCapabilitySupport enabled`

        Whether the model supports thinking with type 'enabled'.

        - `boolean supported`

          Whether this capability is supported by the model.

### Beta Model Info

- `class BetaModelInfo:`

  - `String id`

    Unique model identifier.

  - `Optional<BetaModelCapabilities> capabilities`

    Model capability information.

    - `BetaCapabilitySupport batch`

      Whether the model supports the Batch API.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaCapabilitySupport citations`

      Whether the model supports citation generation.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaCapabilitySupport codeExecution`

      Whether the model supports code execution tools.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaContextManagementCapability contextManagement`

      Context management support and available strategies.

      - `Optional<BetaCapabilitySupport> clearThinking20251015`

        Indicates whether a capability is supported.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `Optional<BetaCapabilitySupport> clearToolUses20250919`

        Indicates whether a capability is supported.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `Optional<BetaCapabilitySupport> compact20260112`

        Indicates whether a capability is supported.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaEffortCapability effort`

      Effort (reasoning_effort) support and available levels.

      - `BetaCapabilitySupport high`

        Whether the model supports high effort level.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `BetaCapabilitySupport low`

        Whether the model supports low effort level.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `BetaCapabilitySupport max`

        Whether the model supports max effort level.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `BetaCapabilitySupport medium`

        Whether the model supports medium effort level.

        - `boolean supported`

          Whether this capability is supported by the model.

      - `boolean supported`

        Whether this capability is supported by the model.

      - `Optional<BetaCapabilitySupport> xhigh`

        Indicates whether a capability is supported.

        - `boolean supported`

          Whether this capability is supported by the model.

    - `BetaCapabilitySupport imageInput`

      Whether the model accepts image content blocks.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaCapabilitySupport pdfInput`

      Whether the model accepts PDF content blocks.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaCapabilitySupport structuredOutputs`

      Whether the model supports structured output / JSON mode / strict tool schemas.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaThinkingCapability thinking`

      Thinking capability and supported type configurations.

      - `boolean supported`

        Whether this capability is supported by the model.

      - `BetaThinkingTypes types`

        Supported thinking type configurations.

        - `BetaCapabilitySupport adaptive`

          Whether the model supports thinking with type 'adaptive' (auto).

          - `boolean supported`

            Whether this capability is supported by the model.

        - `BetaCapabilitySupport enabled`

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

### Beta Thinking Capability

- `class BetaThinkingCapability:`

  Thinking capability details.

  - `boolean supported`

    Whether this capability is supported by the model.

  - `BetaThinkingTypes types`

    Supported thinking type configurations.

    - `BetaCapabilitySupport adaptive`

      Whether the model supports thinking with type 'adaptive' (auto).

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaCapabilitySupport enabled`

      Whether the model supports thinking with type 'enabled'.

      - `boolean supported`

        Whether this capability is supported by the model.

### Beta Thinking Types

- `class BetaThinkingTypes:`

  Supported thinking type configurations.

  - `BetaCapabilitySupport adaptive`

    Whether the model supports thinking with type 'adaptive' (auto).

    - `boolean supported`

      Whether this capability is supported by the model.

  - `BetaCapabilitySupport enabled`

    Whether the model supports thinking with type 'enabled'.

    - `boolean supported`

      Whether this capability is supported by the model.
