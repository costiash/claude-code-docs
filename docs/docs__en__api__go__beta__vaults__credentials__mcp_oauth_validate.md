## Validate Credential

`client.Beta.Vaults.Credentials.MCPOAuthValidate(ctx, credentialID, params) (*BetaManagedAgentsCredentialValidation, error)`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate Credential

### Parameters

- `credentialID string`

- `params BetaVaultCredentialMCPOAuthValidateParams`

  - `VaultID param.Field[string]`

    Path param: Path parameter vault_id

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

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

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsCredentialValidation struct{…}`

  Result of live-probing a credential against its configured MCP server.

  - `CredentialID string`

    Unique identifier of the credential that was validated.

  - `HasRefreshToken bool`

    Whether the credential has a refresh token configured.

  - `MCPProbe BetaManagedAgentsMCPProbe`

    The failing step of an MCP validation probe.

    - `HTTPResponse BetaManagedAgentsRefreshHTTPResponse`

      An HTTP response captured during a credential validation probe.

      - `Body string`

        Response body. May be truncated and has sensitive values scrubbed.

      - `BodyTruncated bool`

        Whether `body` was truncated.

      - `ContentType string`

        Value of the `Content-Type` response header.

      - `StatusCode int64`

        HTTP status code.

    - `Method string`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `Refresh BetaManagedAgentsRefreshObject`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `HTTPResponse BetaManagedAgentsRefreshHTTPResponse`

      An HTTP response captured during a credential validation probe.

    - `Status BetaManagedAgentsRefreshObjectStatus`

      Outcome of a refresh-token exchange attempted during credential validation.

      - `const BetaManagedAgentsRefreshObjectStatusSucceeded BetaManagedAgentsRefreshObjectStatus = "succeeded"`

      - `const BetaManagedAgentsRefreshObjectStatusFailed BetaManagedAgentsRefreshObjectStatus = "failed"`

      - `const BetaManagedAgentsRefreshObjectStatusConnectError BetaManagedAgentsRefreshObjectStatus = "connect_error"`

      - `const BetaManagedAgentsRefreshObjectStatusNoRefreshToken BetaManagedAgentsRefreshObjectStatus = "no_refresh_token"`

  - `Status BetaManagedAgentsCredentialValidationStatus`

    Overall verdict of a credential validation probe.

    - `const BetaManagedAgentsCredentialValidationStatusValid BetaManagedAgentsCredentialValidationStatus = "valid"`

    - `const BetaManagedAgentsCredentialValidationStatusInvalid BetaManagedAgentsCredentialValidationStatus = "invalid"`

    - `const BetaManagedAgentsCredentialValidationStatusUnknown BetaManagedAgentsCredentialValidationStatus = "unknown"`

  - `Type BetaManagedAgentsCredentialValidationType`

    - `const BetaManagedAgentsCredentialValidationTypeVaultCredentialValidation BetaManagedAgentsCredentialValidationType = "vault_credential_validation"`

  - `ValidatedAt Time`

    A timestamp in RFC 3339 format

  - `VaultID string`

    Identifier of the vault containing the credential.

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
  betaManagedAgentsCredentialValidation, err := client.Beta.Vaults.Credentials.MCPOAuthValidate(
    context.TODO(),
    "vcrd_011CZkZEMt8gZan2iYOQfSkw",
    anthropic.BetaVaultCredentialMCPOAuthValidateParams{
      VaultID: "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsCredentialValidation.CredentialID)
}
```

#### Response

```json
{
  "credential_id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "has_refresh_token": true,
  "mcp_probe": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "method": "method"
  },
  "refresh": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "status": "succeeded"
  },
  "status": "valid",
  "type": "vault_credential_validation",
  "validated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv"
}
```
