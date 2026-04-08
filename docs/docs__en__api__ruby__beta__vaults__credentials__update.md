## Update

`beta.vaults.credentials.update(credential_id, **kwargs) -> BetaManagedAgentsCredential`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update Credential

### Parameters

- `vault_id: String`

- `credential_id: String`

- `auth: BetaManagedAgentsMCPOAuthUpdateParams | BetaManagedAgentsStaticBearerUpdateParams`

  Updated authentication details for a credential.

  - `class BetaManagedAgentsMCPOAuthUpdateParams`

    Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

    - `type: :mcp_oauth`

      - `:mcp_oauth`

    - `access_token: String`

      Updated OAuth access token.

    - `expires_at: Time`

      A timestamp in RFC 3339 format

    - `refresh: BetaManagedAgentsMCPOAuthRefreshUpdateParams`

      Parameters for updating OAuth refresh token configuration.

      - `refresh_token: String`

        Updated OAuth refresh token.

      - `scope: String`

        Updated OAuth scope for the refresh request.

      - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthBasicUpdateParam | BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

        Updated HTTP Basic authentication parameters for the token endpoint.

        - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam`

          Updated HTTP Basic authentication parameters for the token endpoint.

          - `type: :client_secret_basic`

            - `:client_secret_basic`

          - `client_secret: String`

            Updated OAuth client secret.

        - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

          Updated POST body authentication parameters for the token endpoint.

          - `type: :client_secret_post`

            - `:client_secret_post`

          - `client_secret: String`

            Updated OAuth client secret.

  - `class BetaManagedAgentsStaticBearerUpdateParams`

    Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

    - `type: :static_bearer`

      - `:static_bearer`

    - `token: String`

      Updated static bearer token value.

- `display_name: String`

  Updated human-readable name for the credential. 1-255 characters.

- `metadata: Hash[Symbol, String]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 18 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

### Returns

- `class BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: String`

    Unique identifier for the credential.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse | BetaManagedAgentsStaticBearerAuthResponse`

    Authentication details for a credential.

    - `class BetaManagedAgentsMCPOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `mcp_server_url: String`

        URL of the MCP server this credential authenticates against.

      - `type: :mcp_oauth`

        - `:mcp_oauth`

      - `expires_at: Time`

        A timestamp in RFC 3339 format

      - `refresh: BetaManagedAgentsMCPOAuthRefreshResponse`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: String`

          OAuth client ID.

        - `token_endpoint: String`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse | BetaManagedAgentsTokenEndpointAuthBasicResponse | BetaManagedAgentsTokenEndpointAuthPostResponse`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `type: :none`

              - `:none`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: :client_secret_basic`

              - `:client_secret_basic`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `type: :client_secret_post`

              - `:client_secret_post`

        - `resource: String`

          OAuth resource indicator.

        - `scope: String`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: String`

        URL of the MCP server this credential authenticates against.

      - `type: :static_bearer`

        - `:static_bearer`

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata attached to the credential.

  - `type: :vault_credential`

    - `:vault_credential`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `vault_id: String`

    Identifier of the vault this credential belongs to.

  - `display_name: String`

    Human-readable name for the credential.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_credential = anthropic.beta.vaults.credentials.update(
  "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv"
)

puts(beta_managed_agents_credential)
```
