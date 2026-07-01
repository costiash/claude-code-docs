## Update Credential

`client.Beta.Vaults.Credentials.Update(ctx, credentialID, params) (*BetaManagedAgentsCredential, error)`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update Credential

### Parameters

- `credentialID string`

- `params BetaVaultCredentialUpdateParams`

  - `VaultID param.Field[string]`

    Path param: Path parameter vault_id

  - `Auth param.Field[BetaVaultCredentialUpdateParamsAuthUnion]`

    Body param: Updated authentication details for a credential.

    - `type BetaManagedAgentsMCPOAuthUpdateParamsResp struct{…}`

      Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

      - `Type BetaManagedAgentsMCPOAuthUpdateParamsType`

        - `const BetaManagedAgentsMCPOAuthUpdateParamsTypeMCPOAuth BetaManagedAgentsMCPOAuthUpdateParamsType = "mcp_oauth"`

      - `AccessToken string`

        Updated OAuth access token.

      - `ExpiresAt Time`

        A timestamp in RFC 3339 format

      - `Refresh BetaManagedAgentsMCPOAuthRefreshUpdateParamsResp`

        Parameters for updating OAuth refresh token configuration.

        - `RefreshToken string`

          Updated OAuth refresh token.

        - `Scope string`

          Updated OAuth scope for the refresh request.

        - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshUpdateParamsTokenEndpointAuthUnionResp`

          Updated HTTP Basic authentication parameters for the token endpoint.

          - `type BetaManagedAgentsTokenEndpointAuthBasicUpdateParamResp struct{…}`

            Updated HTTP Basic authentication parameters for the token endpoint.

            - `Type BetaManagedAgentsTokenEndpointAuthBasicUpdateParamType`

              - `const BetaManagedAgentsTokenEndpointAuthBasicUpdateParamTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicUpdateParamType = "client_secret_basic"`

            - `ClientSecret string`

              Updated OAuth client secret.

          - `type BetaManagedAgentsTokenEndpointAuthPostUpdateParamResp struct{…}`

            Updated POST body authentication parameters for the token endpoint.

            - `Type BetaManagedAgentsTokenEndpointAuthPostUpdateParamType`

              - `const BetaManagedAgentsTokenEndpointAuthPostUpdateParamTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostUpdateParamType = "client_secret_post"`

            - `ClientSecret string`

              Updated OAuth client secret.

    - `type BetaManagedAgentsStaticBearerUpdateParamsResp struct{…}`

      Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

      - `Type BetaManagedAgentsStaticBearerUpdateParamsType`

        - `const BetaManagedAgentsStaticBearerUpdateParamsTypeStaticBearer BetaManagedAgentsStaticBearerUpdateParamsType = "static_bearer"`

      - `Token string`

        Updated static bearer token value.

    - `type BetaManagedAgentsEnvironmentVariableUpdateParamsResp struct{…}`

      Parameters for updating an environment variable credential. `secret_name` is immutable.

      - `Type BetaManagedAgentsEnvironmentVariableUpdateParamsType`

        - `const BetaManagedAgentsEnvironmentVariableUpdateParamsTypeEnvironmentVariable BetaManagedAgentsEnvironmentVariableUpdateParamsType = "environment_variable"`

      - `InjectionLocation BetaManagedAgentsInjectionLocationUpdateParamsResp`

        Updated injection location.

        - `Body bool`

          Substitute when the placeholder appears in the request body.

        - `Header bool`

          Substitute when the placeholder appears in a request header value.

      - `Networking BetaManagedAgentsCredentialNetworkingParamsUnionResp`

        Updated networking scope. Full replacement.

        - `type BetaManagedAgentsUnrestrictedCredentialNetworkingParamsResp struct{…}`

          Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

          - `Type BetaManagedAgentsUnrestrictedCredentialNetworkingParamsType`

            - `const BetaManagedAgentsUnrestrictedCredentialNetworkingParamsTypeUnrestricted BetaManagedAgentsUnrestrictedCredentialNetworkingParamsType = "unrestricted"`

        - `type BetaManagedAgentsLimitedCredentialNetworkingParamsResp struct{…}`

          Substitute the secret only on requests to the listed hosts.

          - `AllowedHosts []string`

            Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

          - `Type BetaManagedAgentsLimitedCredentialNetworkingParamsType`

            - `const BetaManagedAgentsLimitedCredentialNetworkingParamsTypeLimited BetaManagedAgentsLimitedCredentialNetworkingParamsType = "limited"`

      - `SecretValue string`

        Updated secret value.

  - `DisplayName param.Field[string]`

    Body param: Updated human-readable name for the credential. 1-255 characters.

  - `Metadata param.Field[map[string, string]]`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

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

    - `type BetaManagedAgentsEnvironmentVariableAuthResponse struct{…}`

      Environment variable credential details. The secret value is never returned.

      - `InjectionLocation BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `Body bool`

          Whether the placeholder is substituted in the request body.

        - `Header bool`

          Whether the placeholder is substituted in request header values.

      - `Networking BetaManagedAgentsEnvironmentVariableAuthResponseNetworkingUnion`

        Outbound hosts the secret value is substituted on.

        - `type BetaManagedAgentsUnrestrictedCredentialNetworkingResponse struct{…}`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `Type BetaManagedAgentsUnrestrictedCredentialNetworkingResponseType`

            - `const BetaManagedAgentsUnrestrictedCredentialNetworkingResponseTypeUnrestricted BetaManagedAgentsUnrestrictedCredentialNetworkingResponseType = "unrestricted"`

        - `type BetaManagedAgentsLimitedCredentialNetworkingResponse struct{…}`

          The secret is substituted only on requests to the listed hosts.

          - `AllowedHosts []string`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `Type BetaManagedAgentsLimitedCredentialNetworkingResponseType`

            - `const BetaManagedAgentsLimitedCredentialNetworkingResponseTypeLimited BetaManagedAgentsLimitedCredentialNetworkingResponseType = "limited"`

      - `SecretName string`

        Name of the environment variable.

      - `Type BetaManagedAgentsEnvironmentVariableAuthResponseType`

        - `const BetaManagedAgentsEnvironmentVariableAuthResponseTypeEnvironmentVariable BetaManagedAgentsEnvironmentVariableAuthResponseType = "environment_variable"`

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
  betaManagedAgentsCredential, err := client.Beta.Vaults.Credentials.Update(
    context.TODO(),
    "vcrd_011CZkZEMt8gZan2iYOQfSkw",
    anthropic.BetaVaultCredentialUpdateParams{
      VaultID: "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsCredential.ID)
}
```

#### Response

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```
