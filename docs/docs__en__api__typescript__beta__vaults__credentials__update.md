## Update

`client.beta.vaults.credentials.update(stringcredentialID, CredentialUpdateParamsparams, RequestOptionsoptions?): BetaManagedAgentsCredential`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update Credential

### Parameters

- `credentialID: string`

- `params: CredentialUpdateParams`

  - `vault_id: string`

    Path param: Path parameter vault_id

  - `auth?: BetaManagedAgentsMCPOAuthUpdateParams | BetaManagedAgentsStaticBearerUpdateParams`

    Body param: Updated authentication details for a credential.

    - `BetaManagedAgentsMCPOAuthUpdateParams`

      Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

      - `type: "mcp_oauth"`

        - `"mcp_oauth"`

      - `access_token?: string | null`

        Updated OAuth access token.

      - `expires_at?: string | null`

        A timestamp in RFC 3339 format

      - `refresh?: BetaManagedAgentsMCPOAuthRefreshUpdateParams | null`

        Parameters for updating OAuth refresh token configuration.

        - `refresh_token?: string | null`

          Updated OAuth refresh token.

        - `scope?: string | null`

          Updated OAuth scope for the refresh request.

        - `token_endpoint_auth?: BetaManagedAgentsTokenEndpointAuthBasicUpdateParam | BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

          Updated HTTP Basic authentication parameters for the token endpoint.

          - `BetaManagedAgentsTokenEndpointAuthBasicUpdateParam`

            Updated HTTP Basic authentication parameters for the token endpoint.

            - `type: "client_secret_basic"`

              - `"client_secret_basic"`

            - `client_secret?: string | null`

              Updated OAuth client secret.

          - `BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

            Updated POST body authentication parameters for the token endpoint.

            - `type: "client_secret_post"`

              - `"client_secret_post"`

            - `client_secret?: string | null`

              Updated OAuth client secret.

    - `BetaManagedAgentsStaticBearerUpdateParams`

      Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

      - `type: "static_bearer"`

        - `"static_bearer"`

      - `token?: string | null`

        Updated static bearer token value.

  - `display_name?: string | null`

    Body param: Updated human-readable name for the credential. 1-255 characters.

  - `metadata?: Record<string, string | null> | null`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 20 more`

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

      - `"advisor-tool-2026-03-01"`

      - `"user-profiles-2026-03-24"`

### Returns

- `BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: string`

    Unique identifier for the credential.

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse | BetaManagedAgentsStaticBearerAuthResponse`

    Authentication details for a credential.

    - `BetaManagedAgentsMCPOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "mcp_oauth"`

        - `"mcp_oauth"`

      - `expires_at?: string | null`

        A timestamp in RFC 3339 format

      - `refresh?: BetaManagedAgentsMCPOAuthRefreshResponse | null`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: string`

          OAuth client ID.

        - `token_endpoint: string`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse | BetaManagedAgentsTokenEndpointAuthBasicResponse | BetaManagedAgentsTokenEndpointAuthPostResponse`

          Token endpoint requires no client authentication.

          - `BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `type: "none"`

              - `"none"`

          - `BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

              - `"client_secret_basic"`

          - `BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

              - `"client_secret_post"`

        - `resource?: string | null`

          OAuth resource indicator.

        - `scope?: string | null`

          OAuth scope for the refresh request.

    - `BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "static_bearer"`

        - `"static_bearer"`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata attached to the credential.

  - `type: "vault_credential"`

    - `"vault_credential"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_id: string`

    Identifier of the vault this credential belongs to.

  - `display_name?: string | null`

    Human-readable name for the credential.

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsCredential = await client.beta.vaults.credentials.update(
  'vcrd_011CZkZEMt8gZan2iYOQfSkw',
  { vault_id: 'vlt_011CZkZDLs7fYzm1hXNPeRjv' },
);

console.log(betaManagedAgentsCredential.id);
```
