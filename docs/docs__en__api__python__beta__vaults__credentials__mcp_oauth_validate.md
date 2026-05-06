## MCP OAuth Validate

`beta.vaults.credentials.mcp_oauth_validate(strcredential_id, CredentialMCPOAuthValidateParams**kwargs)  -> BetaManagedAgentsCredentialValidation`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate Credential

### Parameters

- `vault_id: str`

- `credential_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 21 more]`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

### Returns

- `class BetaManagedAgentsCredentialValidation: …`

  Result of live-probing a credential against its configured MCP server.

  - `credential_id: str`

    Unique identifier of the credential that was validated.

  - `has_refresh_token: bool`

    Whether the credential has a refresh token configured.

  - `mcp_probe: Optional[BetaManagedAgentsMCPProbe]`

    The failing step of an MCP validation probe.

    - `http_response: Optional[BetaManagedAgentsRefreshHTTPResponse]`

      An HTTP response captured during a credential validation probe.

      - `body: str`

        Response body. May be truncated and has sensitive values scrubbed.

      - `body_truncated: bool`

        Whether `body` was truncated.

      - `content_type: str`

        Value of the `Content-Type` response header.

      - `status_code: int`

        HTTP status code.

    - `method: str`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `refresh: Optional[BetaManagedAgentsRefreshObject]`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `http_response: Optional[BetaManagedAgentsRefreshHTTPResponse]`

      An HTTP response captured during a credential validation probe.

      - `body: str`

        Response body. May be truncated and has sensitive values scrubbed.

      - `body_truncated: bool`

        Whether `body` was truncated.

      - `content_type: str`

        Value of the `Content-Type` response header.

      - `status_code: int`

        HTTP status code.

    - `status: Literal["succeeded", "failed", "connect_error", "no_refresh_token"]`

      Outcome of a refresh-token exchange attempted during credential validation.

      - `"succeeded"`

      - `"failed"`

      - `"connect_error"`

      - `"no_refresh_token"`

  - `status: BetaManagedAgentsCredentialValidationStatus`

    Overall verdict of a credential validation probe.

    - `"valid"`

    - `"invalid"`

    - `"unknown"`

  - `type: Literal["vault_credential_validation"]`

    - `"vault_credential_validation"`

  - `validated_at: datetime`

    A timestamp in RFC 3339 format

  - `vault_id: str`

    Identifier of the vault containing the credential.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_credential_validation = client.beta.vaults.credentials.mcp_oauth_validate(
    credential_id="vcrd_011CZkZEMt8gZan2iYOQfSkw",
    vault_id="vlt_011CZkZDLs7fYzm1hXNPeRjv",
)
print(beta_managed_agents_credential_validation.credential_id)
```
