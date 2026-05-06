## Create

`beta.vaults.credentials.create(strvault_id, CredentialCreateParams**kwargs)  -> BetaManagedAgentsCredential`

**post** `/v1/vaults/{vault_id}/credentials`

Create Credential

### Parameters

- `vault_id: str`

- `auth: Auth`

  Authentication details for creating a credential.

  - `class BetaManagedAgentsMCPOAuthCreateParams: …`

    Parameters for creating an MCP OAuth credential.

    - `access_token: str`

      OAuth access token.

    - `mcp_server_url: str`

      URL of the MCP server this credential authenticates against.

    - `type: Literal["mcp_oauth"]`

      - `"mcp_oauth"`

    - `expires_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `refresh: Optional[BetaManagedAgentsMCPOAuthRefreshParams]`

      OAuth refresh token parameters for creating a credential with refresh support.

      - `client_id: str`

        OAuth client ID.

      - `refresh_token: str`

        OAuth refresh token.

      - `token_endpoint: str`

        Token endpoint URL used to refresh the access token.

      - `token_endpoint_auth: TokenEndpointAuth`

        Token endpoint requires no client authentication.

        - `class BetaManagedAgentsTokenEndpointAuthNoneParam: …`

          Token endpoint requires no client authentication.

          - `type: Literal["none"]`

            - `"none"`

        - `class BetaManagedAgentsTokenEndpointAuthBasicParam: …`

          Token endpoint uses HTTP Basic authentication with client credentials.

          - `client_secret: str`

            OAuth client secret.

          - `type: Literal["client_secret_basic"]`

            - `"client_secret_basic"`

        - `class BetaManagedAgentsTokenEndpointAuthPostParam: …`

          Token endpoint uses POST body authentication with client credentials.

          - `client_secret: str`

            OAuth client secret.

          - `type: Literal["client_secret_post"]`

            - `"client_secret_post"`

      - `resource: Optional[str]`

        OAuth resource indicator.

      - `scope: Optional[str]`

        OAuth scope for the refresh request.

  - `class BetaManagedAgentsStaticBearerCreateParams: …`

    Parameters for creating a static bearer token credential.

    - `token: str`

      Static bearer token value.

    - `mcp_server_url: str`

      URL of the MCP server this credential authenticates against.

    - `type: Literal["static_bearer"]`

      - `"static_bearer"`

- `display_name: Optional[str]`

  Human-readable name for the credential. Up to 255 characters.

- `metadata: Optional[Dict[str, str]]`

  Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

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

- `class BetaManagedAgentsCredential: …`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: str`

    Unique identifier for the credential.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `auth: Auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMCPOAuthAuthResponse: …`

      OAuth credential details for an MCP server.

      - `mcp_server_url: str`

        URL of the MCP server this credential authenticates against.

      - `type: Literal["mcp_oauth"]`

        - `"mcp_oauth"`

      - `expires_at: Optional[datetime]`

        A timestamp in RFC 3339 format

      - `refresh: Optional[BetaManagedAgentsMCPOAuthRefreshResponse]`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: str`

          OAuth client ID.

        - `token_endpoint: str`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: TokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse: …`

            Token endpoint requires no client authentication.

            - `type: Literal["none"]`

              - `"none"`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse: …`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: Literal["client_secret_basic"]`

              - `"client_secret_basic"`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse: …`

            Token endpoint uses POST body authentication with client credentials.

            - `type: Literal["client_secret_post"]`

              - `"client_secret_post"`

        - `resource: Optional[str]`

          OAuth resource indicator.

        - `scope: Optional[str]`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse: …`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: str`

        URL of the MCP server this credential authenticates against.

      - `type: Literal["static_bearer"]`

        - `"static_bearer"`

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata attached to the credential.

  - `type: Literal["vault_credential"]`

    - `"vault_credential"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `vault_id: str`

    Identifier of the vault this credential belongs to.

  - `display_name: Optional[str]`

    Human-readable name for the credential.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_credential = client.beta.vaults.credentials.create(
    vault_id="vlt_011CZkZDLs7fYzm1hXNPeRjv",
    auth={
        "token": "bearer_exampletoken",
        "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
        "type": "static_bearer",
    },
)
print(beta_managed_agents_credential.id)
```
