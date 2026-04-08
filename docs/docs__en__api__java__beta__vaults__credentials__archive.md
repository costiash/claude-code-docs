## Archive

`BetaManagedAgentsCredential beta().vaults().credentials().archive(CredentialArchiveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/archive`

Archive Credential

### Parameters

- `CredentialArchiveParams params`

  - `String vaultId`

  - `Optional<String> credentialId`

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

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `String id`

    Unique identifier for the credential.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `MCP_OAUTH("mcp_oauth")`

      - `Optional<LocalDateTime> expiresAt`

        A timestamp in RFC 3339 format

      - `Optional<BetaManagedAgentsMcpOAuthRefreshResponse> refresh`

        OAuth refresh token configuration returned in credential responses.

        - `String clientId`

          OAuth client ID.

        - `String tokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth tokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

            Token endpoint requires no client authentication.

            - `Type type`

              - `NONE("none")`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type type`

              - `CLIENT_SECRET_BASIC("client_secret_basic")`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `Type type`

              - `CLIENT_SECRET_POST("client_secret_post")`

        - `Optional<String> resource`

          OAuth resource indicator.

        - `Optional<String> scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `STATIC_BEARER("static_bearer")`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

    - `VAULT_CREDENTIAL("vault_credential")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `String vaultId`

    Identifier of the vault this credential belongs to.

  - `Optional<String> displayName`

    Human-readable name for the credential.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsCredential;
import com.anthropic.models.beta.vaults.credentials.CredentialArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialArchiveParams params = CredentialArchiveParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .credentialId("vcrd_011CZkZEMt8gZan2iYOQfSkw")
            .build();
        BetaManagedAgentsCredential betaManagedAgentsCredential = client.beta().vaults().credentials().archive(params);
    }
}
```
