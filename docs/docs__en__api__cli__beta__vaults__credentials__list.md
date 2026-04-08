## List

`$ ant beta:vaults:credentials list`

**get** `/v1/vaults/{vault_id}/credentials`

List Credentials

### Parameters

- `--vault-id: string`

  Path param: Path parameter vault_id

- `--include-archived: optional boolean`

  Query param: Whether to include archived credentials in the results.

- `--limit: optional number`

  Query param: Maximum number of credentials to return per page. Defaults to 20, maximum 100.

- `--page: optional string`

  Query param: Opaque pagination token from a previous `list_credentials` response.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsListCredentialsResponse: object { data, next_page }`

  Response containing a paginated list of credentials.

  - `data: optional array of BetaManagedAgentsCredential`

    List of credentials.

    - `id: string`

      Unique identifier for the credential.

    - `archived_at: string`

      A timestamp in RFC 3339 format

    - `auth: BetaManagedAgentsMCPOAuthAuthResponse or BetaManagedAgentsStaticBearerAuthResponse`

      Authentication details for a credential.

      - `beta_managed_agents_mcp_oauth_auth_response: object { mcp_server_url, type, expires_at, refresh }`

        OAuth credential details for an MCP server.

        - `mcp_server_url: string`

          URL of the MCP server this credential authenticates against.

        - `type: "mcp_oauth"`

          - `"mcp_oauth"`

        - `expires_at: optional string`

          A timestamp in RFC 3339 format

        - `refresh: optional object { client_id, token_endpoint, token_endpoint_auth, 2 more }`

          OAuth refresh token configuration returned in credential responses.

          - `client_id: string`

            OAuth client ID.

          - `token_endpoint: string`

            Token endpoint URL used to refresh the access token.

          - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse or BetaManagedAgentsTokenEndpointAuthBasicResponse or BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint requires no client authentication.

            - `beta_managed_agents_token_endpoint_auth_none_response: object { type }`

              Token endpoint requires no client authentication.

              - `type: "none"`

                - `"none"`

            - `beta_managed_agents_token_endpoint_auth_basic_response: object { type }`

              Token endpoint uses HTTP Basic authentication with client credentials.

              - `type: "client_secret_basic"`

                - `"client_secret_basic"`

            - `beta_managed_agents_token_endpoint_auth_post_response: object { type }`

              Token endpoint uses POST body authentication with client credentials.

              - `type: "client_secret_post"`

                - `"client_secret_post"`

          - `resource: optional string`

            OAuth resource indicator.

          - `scope: optional string`

            OAuth scope for the refresh request.

      - `beta_managed_agents_static_bearer_auth_response: object { mcp_server_url, type }`

        Static bearer token credential details for an MCP server.

        - `mcp_server_url: string`

          URL of the MCP server this credential authenticates against.

        - `type: "static_bearer"`

          - `"static_bearer"`

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

```cli
ant beta:vaults:credentials list \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv
```
