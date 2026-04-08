## Retrieve

`BetaModelInfo Beta.Models.Retrieve(ModelRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/models/{model_id}`

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

### Parameters

- `ModelRetrieveParams parameters`

  - `required string modelID`

    Model identifier or alias.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

### Returns

- `class BetaModelInfo:`

  - `required string ID`

    Unique model identifier.

  - `required BetaModelCapabilities? Capabilities`

    Model capability information.

    - `required BetaCapabilitySupport Batch`

      Whether the model supports the Batch API.

      - `required Boolean Supported`

        Whether this capability is supported by the model.

    - `required BetaCapabilitySupport Citations`

      Whether the model supports citation generation.

      - `required Boolean Supported`

        Whether this capability is supported by the model.

    - `required BetaCapabilitySupport CodeExecution`

      Whether the model supports code execution tools.

      - `required Boolean Supported`

        Whether this capability is supported by the model.

    - `required BetaContextManagementCapability ContextManagement`

      Context management support and available strategies.

      - `required BetaCapabilitySupport? ClearThinking20251015`

        Indicates whether a capability is supported.

        - `required Boolean Supported`

          Whether this capability is supported by the model.

      - `required BetaCapabilitySupport? ClearToolUses20250919`

        Indicates whether a capability is supported.

        - `required Boolean Supported`

          Whether this capability is supported by the model.

      - `required BetaCapabilitySupport? Compact20260112`

        Indicates whether a capability is supported.

        - `required Boolean Supported`

          Whether this capability is supported by the model.

      - `required Boolean Supported`

        Whether this capability is supported by the model.

    - `required BetaEffortCapability Effort`

      Effort (reasoning_effort) support and available levels.

      - `required BetaCapabilitySupport High`

        Whether the model supports high effort level.

        - `required Boolean Supported`

          Whether this capability is supported by the model.

      - `required BetaCapabilitySupport Low`

        Whether the model supports low effort level.

        - `required Boolean Supported`

          Whether this capability is supported by the model.

      - `required BetaCapabilitySupport Max`

        Whether the model supports max effort level.

        - `required Boolean Supported`

          Whether this capability is supported by the model.

      - `required BetaCapabilitySupport Medium`

        Whether the model supports medium effort level.

        - `required Boolean Supported`

          Whether this capability is supported by the model.

      - `required Boolean Supported`

        Whether this capability is supported by the model.

    - `required BetaCapabilitySupport ImageInput`

      Whether the model accepts image content blocks.

      - `required Boolean Supported`

        Whether this capability is supported by the model.

    - `required BetaCapabilitySupport PdfInput`

      Whether the model accepts PDF content blocks.

      - `required Boolean Supported`

        Whether this capability is supported by the model.

    - `required BetaCapabilitySupport StructuredOutputs`

      Whether the model supports structured output / JSON mode / strict tool schemas.

      - `required Boolean Supported`

        Whether this capability is supported by the model.

    - `required BetaThinkingCapability Thinking`

      Thinking capability and supported type configurations.

      - `required Boolean Supported`

        Whether this capability is supported by the model.

      - `required BetaThinkingTypes Types`

        Supported thinking type configurations.

        - `required BetaCapabilitySupport Adaptive`

          Whether the model supports thinking with type 'adaptive' (auto).

          - `required Boolean Supported`

            Whether this capability is supported by the model.

        - `required BetaCapabilitySupport Enabled`

          Whether the model supports thinking with type 'enabled'.

          - `required Boolean Supported`

            Whether this capability is supported by the model.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

  - `required string DisplayName`

    A human-readable name for the model.

  - `required Long? MaxInputTokens`

    Maximum input context window size in tokens for this model.

  - `required Long? MaxTokens`

    Maximum value for the `max_tokens` parameter when using this model.

  - `JsonElement Type "model"constant`

    Object type.

    For Models, this is always `"model"`.

### Example

```csharp
ModelRetrieveParams parameters = new() { ModelID = "model_id" };

var betaModelInfo = await client.Beta.Models.Retrieve(parameters);

Console.WriteLine(betaModelInfo);
```
