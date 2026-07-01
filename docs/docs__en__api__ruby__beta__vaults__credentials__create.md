## Create Credential

`beta.vaults.credentials.create(vault_id, **kwargs) -> BetaManagedAgentsCredential`

**post** `/v1/vaults/{vault_id}/credentials`

Create Credential

### Parameters

- `vault_id: String`

- `auth: BetaManagedAgentsMCPOAuthCreateParams | BetaManagedAgentsStaticBearerCreateParams | BetaManagedAgentsEnvironmentVariableCreateParams`

  Authentication details for creating a credential.

  - `class BetaManagedAgentsMCPOAuthCreateParams`

    Parameters for creating an MCP OAuth credential.

    - `access_token: String`

      OAuth access token.

    - `mcp_server_url: String`

      URL of the MCP server this credential authenticates against.

    - `type: :mcp_oauth`

      - `:mcp_oauth`

    - `expires_at: Time`

      A timestamp in RFC 3339 format

    - `refresh: BetaManagedAgentsMCPOAuthRefreshParams`

      OAuth refresh token parameters for creating a credential with refresh support.

      - `client_id: String`

        OAuth client ID.

      - `refresh_token: String`

        OAuth refresh token.

      - `token_endpoint: String`

        Token endpoint URL used to refresh the access token.

      - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneParam | BetaManagedAgentsTokenEndpointAuthBasicParam | BetaManagedAgentsTokenEndpointAuthPostParam`

        Token endpoint requires no client authentication.

        - `class BetaManagedAgentsTokenEndpointAuthNoneParam`

          Token endpoint requires no client authentication.

          - `type: :none`

            - `:none`

        - `class BetaManagedAgentsTokenEndpointAuthBasicParam`

          Token endpoint uses HTTP Basic authentication with client credentials.

          - `client_secret: String`

            OAuth client secret.

          - `type: :client_secret_basic`

            - `:client_secret_basic`

        - `class BetaManagedAgentsTokenEndpointAuthPostParam`

          Token endpoint uses POST body authentication with client credentials.

          - `client_secret: String`

            OAuth client secret.

          - `type: :client_secret_post`

            - `:client_secret_post`

      - `resource: String`

        OAuth resource indicator.

      - `scope: String`

        OAuth scope for the refresh request.

  - `class BetaManagedAgentsStaticBearerCreateParams`

    Parameters for creating a static bearer token credential.

    - `token: String`

      Static bearer token value.

    - `mcp_server_url: String`

      URL of the MCP server this credential authenticates against.

    - `type: :static_bearer`

      - `:static_bearer`

  - `class BetaManagedAgentsEnvironmentVariableCreateParams`

    Parameters for creating an environment variable credential.

    - `networking: BetaManagedAgentsCredentialNetworkingParams`

      Outbound hosts the secret value is substituted on.

      - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams`

        Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

        - `type: :unrestricted`

          - `:unrestricted`

      - `class BetaManagedAgentsLimitedCredentialNetworkingParams`

        Substitute the secret only on requests to the listed hosts.

        - `allowed_hosts: Array[String]`

          Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

        - `type: :limited`

          - `:limited`

    - `secret_name: String`

      Name of the environment variable. Immutable after create.

    - `secret_value: String`

      Secret value. Write-only; never returned in responses.

    - `type: :environment_variable`

      - `:environment_variable`

    - `injection_location: BetaManagedAgentsInjectionLocationParams`

      Where in the outbound request the secret value may be substituted.

      - `body: bool`

        Substitute when the placeholder appears in the request body.

      - `header: bool`

        Substitute when the placeholder appears in a request header value.

- `display_name: String`

  Human-readable name for the credential. Up to 255 characters.

- `metadata: Hash[Symbol, String]`

  Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 25 more`

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

    - `:"user-profiles-2026-03-24"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"fallback-credit-2026-06-01"`

### Returns

- `class BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: String`

    Unique identifier for the credential.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse | BetaManagedAgentsStaticBearerAuthResponse | BetaManagedAgentsEnvironmentVariableAuthResponse`

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

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse`

      Environment variable credential details. The secret value is never returned.

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: bool`

          Whether the placeholder is substituted in the request body.

        - `header: bool`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse | BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: :unrestricted`

            - `:unrestricted`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse`

          The secret is substituted only on requests to the listed hosts.

          - `allowed_hosts: Array[String]`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `type: :limited`

            - `:limited`

      - `secret_name: String`

        Name of the environment variable.

      - `type: :environment_variable`

        - `:environment_variable`

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

beta_managed_agents_credential = anthropic.beta.vaults.credentials.create(
  "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  auth: {
    token: "bearer_exampletoken",
    mcp_server_url: "https://example-server.modelcontextprotocol.io/sse",
    type: :static_bearer
  }
)

puts(beta_managed_agents_credential)
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
