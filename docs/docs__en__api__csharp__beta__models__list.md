## List Models

`ModelListPageResponse Beta.Models.List(ModelListParams?parameters, CancellationTokencancellationToken = default)`

**get** `/v1/models`

List available models.

The Models API response can be used to determine which models are available for use in the API. More recently released models are listed first.

### Parameters

- `ModelListParams parameters`

  - `string afterID`

    Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `string beforeID`

    Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `Long limit`

    Query param: Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

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

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"mid-conversation-system-2026-04-07"MidConversationSystem2026_04_07`

### Returns

- `class ModelListPageResponse:`

  - `required IReadOnlyList<BetaModelInfo> Data`

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

      - `required BetaCapabilitySupport CodeExecution`

        Whether the model supports code execution tools.

      - `required BetaContextManagementCapability ContextManagement`

        Context management support and available strategies.

        - `required BetaCapabilitySupport? ClearThinking20251015`

          Indicates whether a capability is supported.

        - `required BetaCapabilitySupport? ClearToolUses20250919`

          Indicates whether a capability is supported.

        - `required BetaCapabilitySupport? Compact20260112`

          Indicates whether a capability is supported.

        - `required Boolean Supported`

          Whether this capability is supported by the model.

      - `required BetaEffortCapability Effort`

        Effort (reasoning_effort) support and available levels.

        - `required BetaCapabilitySupport High`

          Whether the model supports high effort level.

        - `required BetaCapabilitySupport Low`

          Whether the model supports low effort level.

        - `required BetaCapabilitySupport Max`

          Whether the model supports max effort level.

        - `required BetaCapabilitySupport Medium`

          Whether the model supports medium effort level.

        - `required Boolean Supported`

          Whether this capability is supported by the model.

        - `required BetaCapabilitySupport? Xhigh`

          Indicates whether a capability is supported.

      - `required BetaCapabilitySupport ImageInput`

        Whether the model accepts image content blocks.

      - `required BetaCapabilitySupport PdfInput`

        Whether the model accepts PDF content blocks.

      - `required BetaCapabilitySupport StructuredOutputs`

        Whether the model supports structured output / JSON mode / strict tool schemas.

      - `required BetaThinkingCapability Thinking`

        Thinking capability and supported type configurations.

        - `required Boolean Supported`

          Whether this capability is supported by the model.

        - `required BetaThinkingTypes Types`

          Supported thinking type configurations.

          - `required BetaCapabilitySupport Adaptive`

            Whether the model supports thinking with type 'adaptive' (auto).

          - `required BetaCapabilitySupport Enabled`

            Whether the model supports thinking with type 'enabled'.

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

  - `required string? FirstID`

    First ID in the `data` list. Can be used as the `before_id` for the previous page.

  - `required Boolean HasMore`

    Indicates if there are more results in the requested page direction.

  - `required string? LastID`

    Last ID in the `data` list. Can be used as the `after_id` for the next page.

### Example

```csharp
ModelListParams parameters = new();

var page = await client.Beta.Models.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
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
