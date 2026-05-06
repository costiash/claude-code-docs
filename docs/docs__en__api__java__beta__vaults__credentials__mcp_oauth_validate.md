## MCP OAuth Validate

`BetaManagedAgentsCredentialValidation beta().vaults().credentials().mcpOAuthValidate(CredentialMcpOAuthValidateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate Credential

### Parameters

- `CredentialMcpOAuthValidateParams params`

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

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

### Returns

- `class BetaManagedAgentsCredentialValidation:`

  Result of live-probing a credential against its configured MCP server.

  - `String credentialId`

    Unique identifier of the credential that was validated.

  - `boolean hasRefreshToken`

    Whether the credential has a refresh token configured.

  - `Optional<BetaManagedAgentsMcpProbe> mcpProbe`

    The failing step of an MCP validation probe.

    - `Optional<BetaManagedAgentsRefreshHttpResponse> httpResponse`

      An HTTP response captured during a credential validation probe.

      - `String body`

        Response body. May be truncated and has sensitive values scrubbed.

      - `boolean bodyTruncated`

        Whether `body` was truncated.

      - `String contentType`

        Value of the `Content-Type` response header.

      - `long statusCode`

        HTTP status code.

    - `String method`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `Optional<BetaManagedAgentsRefreshObject> refresh`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `Optional<BetaManagedAgentsRefreshHttpResponse> httpResponse`

      An HTTP response captured during a credential validation probe.

      - `String body`

        Response body. May be truncated and has sensitive values scrubbed.

      - `boolean bodyTruncated`

        Whether `body` was truncated.

      - `String contentType`

        Value of the `Content-Type` response header.

      - `long statusCode`

        HTTP status code.

    - `Status status`

      Outcome of a refresh-token exchange attempted during credential validation.

      - `SUCCEEDED("succeeded")`

      - `FAILED("failed")`

      - `CONNECT_ERROR("connect_error")`

      - `NO_REFRESH_TOKEN("no_refresh_token")`

  - `BetaManagedAgentsCredentialValidationStatus status`

    Overall verdict of a credential validation probe.

    - `VALID("valid")`

    - `INVALID("invalid")`

    - `UNKNOWN("unknown")`

  - `Type type`

    - `VAULT_CREDENTIAL_VALIDATION("vault_credential_validation")`

  - `LocalDateTime validatedAt`

    A timestamp in RFC 3339 format

  - `String vaultId`

    Identifier of the vault containing the credential.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsCredentialValidation;
import com.anthropic.models.beta.vaults.credentials.CredentialMcpOAuthValidateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialMcpOAuthValidateParams params = CredentialMcpOAuthValidateParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .credentialId("vcrd_011CZkZEMt8gZan2iYOQfSkw")
            .build();
        BetaManagedAgentsCredentialValidation betaManagedAgentsCredentialValidation = client.beta().vaults().credentials().mcpOAuthValidate(params);
    }
}
```
