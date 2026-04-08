## List

`client.Beta.Vaults.Credentials.List(ctx, vaultID, params) (*PageCursor[BetaManagedAgentsCredential], error)`

**get** `/v1/vaults/{vault_id}/credentials`

List Credentials

### Parameters

- `vaultID string`

- `params BetaVaultCredentialListParams`

  - `IncludeArchived param.Field[bool]`

    Query param: Whether to include archived credentials in the results.

  - `Limit param.Field[int64]`

    Query param: Maximum number of credentials to return per page. Defaults to 20, maximum 100.

  - `Page param.Field[string]`

    Query param: Opaque pagination token from a previous `list_credentials` response.

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

### Returns

- `type BetaManagedAgentsCredential struct{…}`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `ID string`

    Unique identifier for the credential.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `Auth BetaManagedAgentsCredentialAuthUnion`

    Authentication details for a credential.

    - `type BetaManagedAgentsMCPOAuthAuthResponse struct{…}`

      OAuth credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsMCPOAuthAuthResponseType`

        - `const BetaManagedAgentsMCPOAuthAuthResponseTypeMCPOAuth BetaManagedAgentsMCPOAuthAuthResponseType = "mcp_oauth"`

      - `ExpiresAt Time`

        A timestamp in RFC 3339 format

      - `Refresh BetaManagedAgentsMCPOAuthRefreshResponse`

        OAuth refresh token configuration returned in credential responses.

        - `ClientID string`

          OAuth client ID.

        - `TokenEndpoint string`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshResponseTokenEndpointAuthUnion`

          Token endpoint requires no client authentication.

          - `type BetaManagedAgentsTokenEndpointAuthNoneResponse struct{…}`

            Token endpoint requires no client authentication.

            - `Type BetaManagedAgentsTokenEndpointAuthNoneResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthNoneResponseTypeNone BetaManagedAgentsTokenEndpointAuthNoneResponseType = "none"`

          - `type BetaManagedAgentsTokenEndpointAuthBasicResponse struct{…}`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthBasicResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthBasicResponseTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicResponseType = "client_secret_basic"`

          - `type BetaManagedAgentsTokenEndpointAuthPostResponse struct{…}`

            Token endpoint uses POST body authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthPostResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthPostResponseTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostResponseType = "client_secret_post"`

        - `Resource string`

          OAuth resource indicator.

        - `Scope string`

          OAuth scope for the refresh request.

    - `type BetaManagedAgentsStaticBearerAuthResponse struct{…}`

      Static bearer token credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsStaticBearerAuthResponseType`

        - `const BetaManagedAgentsStaticBearerAuthResponseTypeStaticBearer BetaManagedAgentsStaticBearerAuthResponseType = "static_bearer"`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Metadata map[string, string]`

    Arbitrary key-value metadata attached to the credential.

  - `Type BetaManagedAgentsCredentialType`

    - `const BetaManagedAgentsCredentialTypeVaultCredential BetaManagedAgentsCredentialType = "vault_credential"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `VaultID string`

    Identifier of the vault this credential belongs to.

  - `DisplayName string`

    Human-readable name for the credential.

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
  page, err := client.Beta.Vaults.Credentials.List(
    context.TODO(),
    "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    anthropic.BetaVaultCredentialListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```
