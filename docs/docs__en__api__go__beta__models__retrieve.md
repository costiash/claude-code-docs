## Get a Model

`client.Beta.Models.Get(ctx, modelID, query) (*BetaModelInfo, error)`

**get** `/v1/models/{model_id}`

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

### Parameters

- `modelID string`

  Model identifier or alias.

- `query BetaModelGetParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

### Returns

- `type BetaModelInfo struct{…}`

  - `ID string`

    Unique model identifier.

  - `Capabilities BetaModelCapabilities`

    Model capability information.

    - `Batch BetaCapabilitySupport`

      Whether the model supports the Batch API.

      - `Supported bool`

        Whether this capability is supported by the model.

    - `Citations BetaCapabilitySupport`

      Whether the model supports citation generation.

    - `CodeExecution BetaCapabilitySupport`

      Whether the model supports code execution tools.

    - `ContextManagement BetaContextManagementCapability`

      Context management support and available strategies.

      - `ClearThinking20251015 BetaCapabilitySupport`

        Indicates whether a capability is supported.

      - `ClearToolUses20250919 BetaCapabilitySupport`

        Indicates whether a capability is supported.

      - `Compact20260112 BetaCapabilitySupport`

        Indicates whether a capability is supported.

      - `Supported bool`

        Whether this capability is supported by the model.

    - `Effort BetaEffortCapability`

      Effort (reasoning_effort) support and available levels.

      - `High BetaCapabilitySupport`

        Whether the model supports high effort level.

      - `Low BetaCapabilitySupport`

        Whether the model supports low effort level.

      - `Max BetaCapabilitySupport`

        Whether the model supports max effort level.

      - `Medium BetaCapabilitySupport`

        Whether the model supports medium effort level.

      - `Supported bool`

        Whether this capability is supported by the model.

      - `Xhigh BetaCapabilitySupport`

        Indicates whether a capability is supported.

    - `ImageInput BetaCapabilitySupport`

      Whether the model accepts image content blocks.

    - `PDFInput BetaCapabilitySupport`

      Whether the model accepts PDF content blocks.

    - `StructuredOutputs BetaCapabilitySupport`

      Whether the model supports structured output / JSON mode / strict tool schemas.

    - `Thinking BetaThinkingCapability`

      Thinking capability and supported type configurations.

      - `Supported bool`

        Whether this capability is supported by the model.

      - `Types BetaThinkingTypes`

        Supported thinking type configurations.

        - `Adaptive BetaCapabilitySupport`

          Whether the model supports thinking with type 'adaptive' (auto).

        - `Enabled BetaCapabilitySupport`

          Whether the model supports thinking with type 'enabled'.

  - `CreatedAt Time`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

  - `DisplayName string`

    A human-readable name for the model.

  - `MaxInputTokens int64`

    Maximum input context window size in tokens for this model.

  - `MaxTokens int64`

    Maximum value for the `max_tokens` parameter when using this model.

  - `Type Model`

    Object type.

    For Models, this is always `"model"`.

    - `const ModelModel Model = "model"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaModelInfo, err := client.Beta.Models.Get(
    context.TODO(),
    "model_id",
    anthropic.BetaModelGetParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaModelInfo.ID)
}
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
