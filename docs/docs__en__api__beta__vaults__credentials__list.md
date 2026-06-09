## List Credentials

**get** `/v1/vaults/{vault_id}/credentials`

List Credentials

### Path Parameters

- `vault_id: string`

### Query Parameters

- `include_archived: optional boolean`

  Whether to include archived credentials in the results.

- `limit: optional number`

  Maximum number of credentials to return per page. Defaults to 20, maximum 100.

- `page: optional string`

  Opaque pagination token from a previous `list_credentials` response.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more`

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

    - `"cache-diagnosis-2026-04-07"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

### Returns

- `data: optional array of BetaManagedAgentsCredential`

  List of credentials.

  - `id: string`

    Unique identifier for the credential.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse or BetaManagedAgentsStaticBearerAuthResponse or BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication details for a credential.

    - `BetaManagedAgentsMCPOAuthAuthResponse object { mcp_server_url, type, expires_at, refresh }`

      OAuth credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "mcp_oauth"`

        - `"mcp_oauth"`

      - `expires_at: optional string`

        A timestamp in RFC 3339 format

      - `refresh: optional BetaManagedAgentsMCPOAuthRefreshResponse`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: string`

          OAuth client ID.

        - `token_endpoint: string`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse or BetaManagedAgentsTokenEndpointAuthBasicResponse or BetaManagedAgentsTokenEndpointAuthPostResponse`

          Token endpoint requires no client authentication.

          - `BetaManagedAgentsTokenEndpointAuthNoneResponse object { type }`

            Token endpoint requires no client authentication.

            - `type: "none"`

              - `"none"`

          - `BetaManagedAgentsTokenEndpointAuthBasicResponse object { type }`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

              - `"client_secret_basic"`

          - `BetaManagedAgentsTokenEndpointAuthPostResponse object { type }`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

              - `"client_secret_post"`

        - `resource: optional string`

          OAuth resource indicator.

        - `scope: optional string`

          OAuth scope for the refresh request.

    - `BetaManagedAgentsStaticBearerAuthResponse object { mcp_server_url, type }`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "static_bearer"`

        - `"static_bearer"`

    - `BetaManagedAgentsEnvironmentVariableAuthResponse object { networking, secret_name, type }`

      Environment variable credential details. The secret value is never returned.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse or BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `BetaManagedAgentsUnrestrictedCredentialNetworkingResponse object { type }`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: "unrestricted"`

            - `"unrestricted"`

        - `BetaManagedAgentsLimitedCredentialNetworkingResponse object { allowed_hosts, type }`

          The secret is substituted only on requests to the listed hosts.

          - `allowed_hosts: array of string`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `type: "limited"`

            - `"limited"`

      - `secret_name: string`

        Name of the environment variable.

      - `type: "environment_variable"`

        - `"environment_variable"`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the credential.

  - `type: "vault_credential"`

    - `"vault_credential"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_id: string`

    Identifier of the vault this credential belongs to.

  - `display_name: optional string`

    Human-readable name for the credential.

- `next_page: optional string`

  Pagination token for the next page, or null if no more results.

### Example

```http
curl https://api.anthropic.com/v1/vaults/$VAULT_ID/credentials \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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
