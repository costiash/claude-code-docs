# Credentials

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

## List Credentials

`beta.vaults.credentials.list(vault_id, **kwargs) -> PageCursor<BetaManagedAgentsCredential>`

**get** `/v1/vaults/{vault_id}/credentials`

List Credentials

### Parameters

- `vault_id: String`

- `include_archived: bool`

  Whether to include archived credentials in the results.

- `limit: Integer`

  Maximum number of credentials to return per page. Defaults to 20, maximum 100.

- `page: String`

  Opaque pagination token from a previous `list_credentials` response.

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

page = anthropic.beta.vaults.credentials.list("vlt_011CZkZDLs7fYzm1hXNPeRjv")

puts(page)
```

#### Response

```json
{
  "data": [
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Credential

`beta.vaults.credentials.retrieve(credential_id, **kwargs) -> BetaManagedAgentsCredential`

**get** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Get Credential

### Parameters

- `vault_id: String`

- `credential_id: String`

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

beta_managed_agents_credential = anthropic.beta.vaults.credentials.retrieve(
  "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv"
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

## Update Credential

`beta.vaults.credentials.update(credential_id, **kwargs) -> BetaManagedAgentsCredential`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update Credential

### Parameters

- `vault_id: String`

- `credential_id: String`

- `auth: BetaManagedAgentsMCPOAuthUpdateParams | BetaManagedAgentsStaticBearerUpdateParams | BetaManagedAgentsEnvironmentVariableUpdateParams`

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

  - `class BetaManagedAgentsEnvironmentVariableUpdateParams`

    Parameters for updating an environment variable credential. `secret_name` is immutable.

    - `type: :environment_variable`

      - `:environment_variable`

    - `injection_location: BetaManagedAgentsInjectionLocationUpdateParams`

      Updated injection location.

      - `body: bool`

        Substitute when the placeholder appears in the request body.

      - `header: bool`

        Substitute when the placeholder appears in a request header value.

    - `networking: BetaManagedAgentsCredentialNetworkingParams`

      Updated networking scope. Full replacement.

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

    - `secret_value: String`

      Updated secret value.

- `display_name: String`

  Updated human-readable name for the credential. 1-255 characters.

- `metadata: Hash[Symbol, String]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

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

beta_managed_agents_credential = anthropic.beta.vaults.credentials.update(
  "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv"
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

## Delete Credential

`beta.vaults.credentials.delete(credential_id, **kwargs) -> BetaManagedAgentsDeletedCredential`

**delete** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete Credential

### Parameters

- `vault_id: String`

- `credential_id: String`

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

- `class BetaManagedAgentsDeletedCredential`

  Confirmation of a deleted credential.

  - `id: String`

    Unique identifier of the deleted credential.

  - `type: :vault_credential_deleted`

    - `:vault_credential_deleted`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_deleted_credential = anthropic.beta.vaults.credentials.delete(
  "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv"
)

puts(beta_managed_agents_deleted_credential)
```

#### Response

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "type": "vault_credential_deleted"
}
```

## Archive Credential

`beta.vaults.credentials.archive(credential_id, **kwargs) -> BetaManagedAgentsCredential`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/archive`

Archive Credential

### Parameters

- `vault_id: String`

- `credential_id: String`

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

beta_managed_agents_credential = anthropic.beta.vaults.credentials.archive(
  "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv"
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

## Validate Credential

`beta.vaults.credentials.mcp_oauth_validate(credential_id, **kwargs) -> BetaManagedAgentsCredentialValidation`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate Credential

### Parameters

- `vault_id: String`

- `credential_id: String`

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

- `class BetaManagedAgentsCredentialValidation`

  Result of live-probing a credential against its configured MCP server.

  - `credential_id: String`

    Unique identifier of the credential that was validated.

  - `has_refresh_token: bool`

    Whether the credential has a refresh token configured.

  - `mcp_probe: BetaManagedAgentsMCPProbe`

    The failing step of an MCP validation probe.

    - `http_response: BetaManagedAgentsRefreshHTTPResponse`

      An HTTP response captured during a credential validation probe.

      - `body: String`

        Response body. May be truncated and has sensitive values scrubbed.

      - `body_truncated: bool`

        Whether `body` was truncated.

      - `content_type: String`

        Value of the `Content-Type` response header.

      - `status_code: Integer`

        HTTP status code.

    - `method_: String`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `refresh: BetaManagedAgentsRefreshObject`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `http_response: BetaManagedAgentsRefreshHTTPResponse`

      An HTTP response captured during a credential validation probe.

    - `status: :succeeded | :failed | :connect_error | :no_refresh_token`

      Outcome of a refresh-token exchange attempted during credential validation.

      - `:succeeded`

      - `:failed`

      - `:connect_error`

      - `:no_refresh_token`

  - `status: BetaManagedAgentsCredentialValidationStatus`

    Overall verdict of a credential validation probe.

    - `:valid`

    - `:invalid`

    - `:unknown`

  - `type: :vault_credential_validation`

    - `:vault_credential_validation`

  - `validated_at: Time`

    A timestamp in RFC 3339 format

  - `vault_id: String`

    Identifier of the vault containing the credential.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_credential_validation = anthropic.beta.vaults.credentials.mcp_oauth_validate(
  "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv"
)

puts(beta_managed_agents_credential_validation)
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

## Domain Types

### Beta Managed Agents Credential

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

### Beta Managed Agents Credential Networking Params

- `BetaManagedAgentsCredentialNetworkingParams = BetaManagedAgentsUnrestrictedCredentialNetworkingParams | BetaManagedAgentsLimitedCredentialNetworkingParams`

  Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

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

### Beta Managed Agents Credential Validation

- `class BetaManagedAgentsCredentialValidation`

  Result of live-probing a credential against its configured MCP server.

  - `credential_id: String`

    Unique identifier of the credential that was validated.

  - `has_refresh_token: bool`

    Whether the credential has a refresh token configured.

  - `mcp_probe: BetaManagedAgentsMCPProbe`

    The failing step of an MCP validation probe.

    - `http_response: BetaManagedAgentsRefreshHTTPResponse`

      An HTTP response captured during a credential validation probe.

      - `body: String`

        Response body. May be truncated and has sensitive values scrubbed.

      - `body_truncated: bool`

        Whether `body` was truncated.

      - `content_type: String`

        Value of the `Content-Type` response header.

      - `status_code: Integer`

        HTTP status code.

    - `method_: String`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `refresh: BetaManagedAgentsRefreshObject`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `http_response: BetaManagedAgentsRefreshHTTPResponse`

      An HTTP response captured during a credential validation probe.

    - `status: :succeeded | :failed | :connect_error | :no_refresh_token`

      Outcome of a refresh-token exchange attempted during credential validation.

      - `:succeeded`

      - `:failed`

      - `:connect_error`

      - `:no_refresh_token`

  - `status: BetaManagedAgentsCredentialValidationStatus`

    Overall verdict of a credential validation probe.

    - `:valid`

    - `:invalid`

    - `:unknown`

  - `type: :vault_credential_validation`

    - `:vault_credential_validation`

  - `validated_at: Time`

    A timestamp in RFC 3339 format

  - `vault_id: String`

    Identifier of the vault containing the credential.

### Beta Managed Agents Credential Validation Status

- `BetaManagedAgentsCredentialValidationStatus = :valid | :invalid | :unknown`

  Overall verdict of a credential validation probe.

  - `:valid`

  - `:invalid`

  - `:unknown`

### Beta Managed Agents Deleted Credential

- `class BetaManagedAgentsDeletedCredential`

  Confirmation of a deleted credential.

  - `id: String`

    Unique identifier of the deleted credential.

  - `type: :vault_credential_deleted`

    - `:vault_credential_deleted`

### Beta Managed Agents Environment Variable Auth Response

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

### Beta Managed Agents Environment Variable Create Params

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

### Beta Managed Agents Environment Variable Update Params

- `class BetaManagedAgentsEnvironmentVariableUpdateParams`

  Parameters for updating an environment variable credential. `secret_name` is immutable.

  - `type: :environment_variable`

    - `:environment_variable`

  - `injection_location: BetaManagedAgentsInjectionLocationUpdateParams`

    Updated injection location.

    - `body: bool`

      Substitute when the placeholder appears in the request body.

    - `header: bool`

      Substitute when the placeholder appears in a request header value.

  - `networking: BetaManagedAgentsCredentialNetworkingParams`

    Updated networking scope. Full replacement.

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

  - `secret_value: String`

    Updated secret value.

### Beta Managed Agents Injection Location Params

- `class BetaManagedAgentsInjectionLocationParams`

  Where in the outbound request the secret value may be substituted.

  - `body: bool`

    Substitute when the placeholder appears in the request body.

  - `header: bool`

    Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Injection Location Response

- `class BetaManagedAgentsInjectionLocationResponse`

  Where in the outbound request the secret value is substituted.

  - `body: bool`

    Whether the placeholder is substituted in the request body.

  - `header: bool`

    Whether the placeholder is substituted in request header values.

### Beta Managed Agents Injection Location Update Params

- `class BetaManagedAgentsInjectionLocationUpdateParams`

  Updated injection location.

  - `body: bool`

    Substitute when the placeholder appears in the request body.

  - `header: bool`

    Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Limited Credential Networking Params

- `class BetaManagedAgentsLimitedCredentialNetworkingParams`

  Substitute the secret only on requests to the listed hosts.

  - `allowed_hosts: Array[String]`

    Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

  - `type: :limited`

    - `:limited`

### Beta Managed Agents Limited Credential Networking Response

- `class BetaManagedAgentsLimitedCredentialNetworkingResponse`

  The secret is substituted only on requests to the listed hosts.

  - `allowed_hosts: Array[String]`

    Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

  - `type: :limited`

    - `:limited`

### Beta Managed Agents MCP OAuth Auth Response

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

### Beta Managed Agents MCP OAuth Create Params

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

### Beta Managed Agents MCP OAuth Refresh Params

- `class BetaManagedAgentsMCPOAuthRefreshParams`

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

### Beta Managed Agents MCP OAuth Refresh Response

- `class BetaManagedAgentsMCPOAuthRefreshResponse`

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

### Beta Managed Agents MCP OAuth Refresh Update Params

- `class BetaManagedAgentsMCPOAuthRefreshUpdateParams`

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

### Beta Managed Agents MCP OAuth Update Params

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

### Beta Managed Agents MCP Probe

- `class BetaManagedAgentsMCPProbe`

  The failing step of an MCP validation probe.

  - `http_response: BetaManagedAgentsRefreshHTTPResponse`

    An HTTP response captured during a credential validation probe.

    - `body: String`

      Response body. May be truncated and has sensitive values scrubbed.

    - `body_truncated: bool`

      Whether `body` was truncated.

    - `content_type: String`

      Value of the `Content-Type` response header.

    - `status_code: Integer`

      HTTP status code.

  - `method_: String`

    The MCP method that failed (for example `initialize` or `tools/list`).

### Beta Managed Agents Refresh HTTP Response

- `class BetaManagedAgentsRefreshHTTPResponse`

  An HTTP response captured during a credential validation probe.

  - `body: String`

    Response body. May be truncated and has sensitive values scrubbed.

  - `body_truncated: bool`

    Whether `body` was truncated.

  - `content_type: String`

    Value of the `Content-Type` response header.

  - `status_code: Integer`

    HTTP status code.

### Beta Managed Agents Refresh Object

- `class BetaManagedAgentsRefreshObject`

  Outcome of a refresh-token exchange attempted during credential validation.

  - `http_response: BetaManagedAgentsRefreshHTTPResponse`

    An HTTP response captured during a credential validation probe.

    - `body: String`

      Response body. May be truncated and has sensitive values scrubbed.

    - `body_truncated: bool`

      Whether `body` was truncated.

    - `content_type: String`

      Value of the `Content-Type` response header.

    - `status_code: Integer`

      HTTP status code.

  - `status: :succeeded | :failed | :connect_error | :no_refresh_token`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `:succeeded`

    - `:failed`

    - `:connect_error`

    - `:no_refresh_token`

### Beta Managed Agents Static Bearer Auth Response

- `class BetaManagedAgentsStaticBearerAuthResponse`

  Static bearer token credential details for an MCP server.

  - `mcp_server_url: String`

    URL of the MCP server this credential authenticates against.

  - `type: :static_bearer`

    - `:static_bearer`

### Beta Managed Agents Static Bearer Create Params

- `class BetaManagedAgentsStaticBearerCreateParams`

  Parameters for creating a static bearer token credential.

  - `token: String`

    Static bearer token value.

  - `mcp_server_url: String`

    URL of the MCP server this credential authenticates against.

  - `type: :static_bearer`

    - `:static_bearer`

### Beta Managed Agents Static Bearer Update Params

- `class BetaManagedAgentsStaticBearerUpdateParams`

  Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

  - `type: :static_bearer`

    - `:static_bearer`

  - `token: String`

    Updated static bearer token value.

### Beta Managed Agents Token Endpoint Auth Basic Param

- `class BetaManagedAgentsTokenEndpointAuthBasicParam`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `client_secret: String`

    OAuth client secret.

  - `type: :client_secret_basic`

    - `:client_secret_basic`

### Beta Managed Agents Token Endpoint Auth Basic Response

- `class BetaManagedAgentsTokenEndpointAuthBasicResponse`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `type: :client_secret_basic`

    - `:client_secret_basic`

### Beta Managed Agents Token Endpoint Auth Basic Update Param

- `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam`

  Updated HTTP Basic authentication parameters for the token endpoint.

  - `type: :client_secret_basic`

    - `:client_secret_basic`

  - `client_secret: String`

    Updated OAuth client secret.

### Beta Managed Agents Token Endpoint Auth None Param

- `class BetaManagedAgentsTokenEndpointAuthNoneParam`

  Token endpoint requires no client authentication.

  - `type: :none`

    - `:none`

### Beta Managed Agents Token Endpoint Auth None Response

- `class BetaManagedAgentsTokenEndpointAuthNoneResponse`

  Token endpoint requires no client authentication.

  - `type: :none`

    - `:none`

### Beta Managed Agents Token Endpoint Auth Post Param

- `class BetaManagedAgentsTokenEndpointAuthPostParam`

  Token endpoint uses POST body authentication with client credentials.

  - `client_secret: String`

    OAuth client secret.

  - `type: :client_secret_post`

    - `:client_secret_post`

### Beta Managed Agents Token Endpoint Auth Post Response

- `class BetaManagedAgentsTokenEndpointAuthPostResponse`

  Token endpoint uses POST body authentication with client credentials.

  - `type: :client_secret_post`

    - `:client_secret_post`

### Beta Managed Agents Token Endpoint Auth Post Update Param

- `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

  Updated POST body authentication parameters for the token endpoint.

  - `type: :client_secret_post`

    - `:client_secret_post`

  - `client_secret: String`

    Updated OAuth client secret.

### Beta Managed Agents Unrestricted Credential Networking Params

- `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams`

  Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

  - `type: :unrestricted`

    - `:unrestricted`

### Beta Managed Agents Unrestricted Credential Networking Response

- `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

  The secret is substituted on any host the session's Environment network policy permits egress to.

  - `type: :unrestricted`

    - `:unrestricted`
