# Vaults

## Create

**post** `/v1/vaults`

Create Vault

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 21 more`

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

### Body Parameters

- `display_name: string`

  Human-readable name for the vault. 1-255 characters.

- `metadata: optional map[string]`

  Arbitrary key-value metadata to attach to the vault. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

### Returns

- `BetaManagedAgentsVault = object { id, archived_at, created_at, 4 more }`

  A vault that stores credentials for use by agents during sessions.

  - `id: string`

    Unique identifier for the vault.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the vault.

  - `type: "vault"`

    - `"vault"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

### Example

```http
curl https://api.anthropic.com/v1/vaults \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "display_name": "Example vault",
          "metadata": {
            "environment": "production"
          }
        }'
```

## List

**get** `/v1/vaults`

List Vaults

### Query Parameters

- `include_archived: optional boolean`

  Whether to include archived vaults in the results.

- `limit: optional number`

  Maximum number of vaults to return per page. Defaults to 20, maximum 100.

- `page: optional string`

  Opaque pagination token from a previous `list_vaults` response.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 21 more`

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

- `data: optional array of BetaManagedAgentsVault`

  List of vaults.

  - `id: string`

    Unique identifier for the vault.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the vault.

  - `type: "vault"`

    - `"vault"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

- `next_page: optional string`

  Pagination token for the next page, or null if no more results.

### Example

```http
curl https://api.anthropic.com/v1/vaults \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Retrieve

**get** `/v1/vaults/{vault_id}`

Get Vault

### Path Parameters

- `vault_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 21 more`

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

- `BetaManagedAgentsVault = object { id, archived_at, created_at, 4 more }`

  A vault that stores credentials for use by agents during sessions.

  - `id: string`

    Unique identifier for the vault.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the vault.

  - `type: "vault"`

    - `"vault"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

### Example

```http
curl https://api.anthropic.com/v1/vaults/$VAULT_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Update

**post** `/v1/vaults/{vault_id}`

Update Vault

### Path Parameters

- `vault_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 21 more`

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

### Body Parameters

- `display_name: optional string`

  Updated human-readable name for the vault. 1-255 characters.

- `metadata: optional map[string]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

### Returns

- `BetaManagedAgentsVault = object { id, archived_at, created_at, 4 more }`

  A vault that stores credentials for use by agents during sessions.

  - `id: string`

    Unique identifier for the vault.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the vault.

  - `type: "vault"`

    - `"vault"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

### Example

```http
curl https://api.anthropic.com/v1/vaults/$VAULT_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "display_name": "Example vault",
          "metadata": {
            "environment": "production"
          }
        }'
```

## Delete

**delete** `/v1/vaults/{vault_id}`

Delete Vault

### Path Parameters

- `vault_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 21 more`

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

- `BetaManagedAgentsDeletedVault = object { id, type }`

  Confirmation of a deleted vault.

  - `id: string`

    Unique identifier of the deleted vault.

  - `type: "vault_deleted"`

    - `"vault_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/vaults/$VAULT_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Archive

**post** `/v1/vaults/{vault_id}/archive`

Archive Vault

### Path Parameters

- `vault_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 21 more`

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

- `BetaManagedAgentsVault = object { id, archived_at, created_at, 4 more }`

  A vault that stores credentials for use by agents during sessions.

  - `id: string`

    Unique identifier for the vault.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the vault.

  - `type: "vault"`

    - `"vault"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

### Example

```http
curl https://api.anthropic.com/v1/vaults/$VAULT_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Domain Types

### Beta Managed Agents Deleted Vault

- `BetaManagedAgentsDeletedVault = object { id, type }`

  Confirmation of a deleted vault.

  - `id: string`

    Unique identifier of the deleted vault.

  - `type: "vault_deleted"`

    - `"vault_deleted"`

### Beta Managed Agents Vault

- `BetaManagedAgentsVault = object { id, archived_at, created_at, 4 more }`

  A vault that stores credentials for use by agents during sessions.

  - `id: string`

    Unique identifier for the vault.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the vault.

  - `type: "vault"`

    - `"vault"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

# Credentials

## Create

**post** `/v1/vaults/{vault_id}/credentials`

Create Credential

### Path Parameters

- `vault_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 21 more`

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

### Body Parameters

- `auth: BetaManagedAgentsMCPOAuthCreateParams or BetaManagedAgentsStaticBearerCreateParams`

  Authentication details for creating a credential.

  - `BetaManagedAgentsMCPOAuthCreateParams = object { access_token, mcp_server_url, type, 2 more }`

    Parameters for creating an MCP OAuth credential.

    - `access_token: string`

      OAuth access token.

    - `mcp_server_url: string`

      URL of the MCP server this credential authenticates against.

    - `type: "mcp_oauth"`

      - `"mcp_oauth"`

    - `expires_at: optional string`

      A timestamp in RFC 3339 format

    - `refresh: optional BetaManagedAgentsMCPOAuthRefreshParams`

      OAuth refresh token parameters for creating a credential with refresh support.

      - `client_id: string`

        OAuth client ID.

      - `refresh_token: string`

        OAuth refresh token.

      - `token_endpoint: string`

        Token endpoint URL used to refresh the access token.

      - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneParam or BetaManagedAgentsTokenEndpointAuthBasicParam or BetaManagedAgentsTokenEndpointAuthPostParam`

        Token endpoint requires no client authentication.

        - `BetaManagedAgentsTokenEndpointAuthNoneParam = object { type }`

          Token endpoint requires no client authentication.

          - `type: "none"`

            - `"none"`

        - `BetaManagedAgentsTokenEndpointAuthBasicParam = object { client_secret, type }`

          Token endpoint uses HTTP Basic authentication with client credentials.

          - `client_secret: string`

            OAuth client secret.

          - `type: "client_secret_basic"`

            - `"client_secret_basic"`

        - `BetaManagedAgentsTokenEndpointAuthPostParam = object { client_secret, type }`

          Token endpoint uses POST body authentication with client credentials.

          - `client_secret: string`

            OAuth client secret.

          - `type: "client_secret_post"`

            - `"client_secret_post"`

      - `resource: optional string`

        OAuth resource indicator.

      - `scope: optional string`

        OAuth scope for the refresh request.

  - `BetaManagedAgentsStaticBearerCreateParams = object { token, mcp_server_url, type }`

    Parameters for creating a static bearer token credential.

    - `token: string`

      Static bearer token value.

    - `mcp_server_url: string`

      URL of the MCP server this credential authenticates against.

    - `type: "static_bearer"`

      - `"static_bearer"`

- `display_name: optional string`

  Human-readable name for the credential. Up to 255 characters.

- `metadata: optional map[string]`

  Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

### Returns

- `BetaManagedAgentsCredential = object { id, archived_at, auth, 6 more }`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: string`

    Unique identifier for the credential.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse or BetaManagedAgentsStaticBearerAuthResponse`

    Authentication details for a credential.

    - `BetaManagedAgentsMCPOAuthAuthResponse = object { mcp_server_url, type, expires_at, refresh }`

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

          - `BetaManagedAgentsTokenEndpointAuthNoneResponse = object { type }`

            Token endpoint requires no client authentication.

            - `type: "none"`

              - `"none"`

          - `BetaManagedAgentsTokenEndpointAuthBasicResponse = object { type }`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

              - `"client_secret_basic"`

          - `BetaManagedAgentsTokenEndpointAuthPostResponse = object { type }`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

              - `"client_secret_post"`

        - `resource: optional string`

          OAuth resource indicator.

        - `scope: optional string`

          OAuth scope for the refresh request.

    - `BetaManagedAgentsStaticBearerAuthResponse = object { mcp_server_url, type }`

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

### Example

```http
curl https://api.anthropic.com/v1/vaults/$VAULT_ID/credentials \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "auth": {
            "token": "bearer_exampletoken",
            "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
            "type": "static_bearer"
          },
          "display_name": "Example credential",
          "metadata": {
            "environment": "production"
          }
        }'
```

## List

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

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 21 more`

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

- `data: optional array of BetaManagedAgentsCredential`

  List of credentials.

  - `id: string`

    Unique identifier for the credential.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse or BetaManagedAgentsStaticBearerAuthResponse`

    Authentication details for a credential.

    - `BetaManagedAgentsMCPOAuthAuthResponse = object { mcp_server_url, type, expires_at, refresh }`

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

          - `BetaManagedAgentsTokenEndpointAuthNoneResponse = object { type }`

            Token endpoint requires no client authentication.

            - `type: "none"`

              - `"none"`

          - `BetaManagedAgentsTokenEndpointAuthBasicResponse = object { type }`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

              - `"client_secret_basic"`

          - `BetaManagedAgentsTokenEndpointAuthPostResponse = object { type }`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

              - `"client_secret_post"`

        - `resource: optional string`

          OAuth resource indicator.

        - `scope: optional string`

          OAuth scope for the refresh request.

    - `BetaManagedAgentsStaticBearerAuthResponse = object { mcp_server_url, type }`

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

```http
curl https://api.anthropic.com/v1/vaults/$VAULT_ID/credentials \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Retrieve

**get** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Get Credential

### Path Parameters

- `vault_id: string`

- `credential_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 21 more`

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

- `BetaManagedAgentsCredential = object { id, archived_at, auth, 6 more }`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: string`

    Unique identifier for the credential.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse or BetaManagedAgentsStaticBearerAuthResponse`

    Authentication details for a credential.

    - `BetaManagedAgentsMCPOAuthAuthResponse = object { mcp_server_url, type, expires_at, refresh }`

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

          - `BetaManagedAgentsTokenEndpointAuthNoneResponse = object { type }`

            Token endpoint requires no client authentication.

            - `type: "none"`

              - `"none"`

          - `BetaManagedAgentsTokenEndpointAuthBasicResponse = object { type }`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

              - `"client_secret_basic"`

          - `BetaManagedAgentsTokenEndpointAuthPostResponse = object { type }`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

              - `"client_secret_post"`

        - `resource: optional string`

          OAuth resource indicator.

        - `scope: optional string`

          OAuth scope for the refresh request.

    - `BetaManagedAgentsStaticBearerAuthResponse = object { mcp_server_url, type }`

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

### Example

```http
curl https://api.anthropic.com/v1/vaults/$VAULT_ID/credentials/$CREDENTIAL_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Update

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update Credential

### Path Parameters

- `vault_id: string`

- `credential_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 21 more`

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

### Body Parameters

- `auth: optional BetaManagedAgentsMCPOAuthUpdateParams or BetaManagedAgentsStaticBearerUpdateParams`

  Updated authentication details for a credential.

  - `BetaManagedAgentsMCPOAuthUpdateParams = object { type, access_token, expires_at, refresh }`

    Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

    - `type: "mcp_oauth"`

      - `"mcp_oauth"`

    - `access_token: optional string`

      Updated OAuth access token.

    - `expires_at: optional string`

      A timestamp in RFC 3339 format

    - `refresh: optional BetaManagedAgentsMCPOAuthRefreshUpdateParams`

      Parameters for updating OAuth refresh token configuration.

      - `refresh_token: optional string`

        Updated OAuth refresh token.

      - `scope: optional string`

        Updated OAuth scope for the refresh request.

      - `token_endpoint_auth: optional BetaManagedAgentsTokenEndpointAuthBasicUpdateParam or BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

        Updated HTTP Basic authentication parameters for the token endpoint.

        - `BetaManagedAgentsTokenEndpointAuthBasicUpdateParam = object { type, client_secret }`

          Updated HTTP Basic authentication parameters for the token endpoint.

          - `type: "client_secret_basic"`

            - `"client_secret_basic"`

          - `client_secret: optional string`

            Updated OAuth client secret.

        - `BetaManagedAgentsTokenEndpointAuthPostUpdateParam = object { type, client_secret }`

          Updated POST body authentication parameters for the token endpoint.

          - `type: "client_secret_post"`

            - `"client_secret_post"`

          - `client_secret: optional string`

            Updated OAuth client secret.

  - `BetaManagedAgentsStaticBearerUpdateParams = object { type, token }`

    Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

    - `type: "static_bearer"`

      - `"static_bearer"`

    - `token: optional string`

      Updated static bearer token value.

- `display_name: optional string`

  Updated human-readable name for the credential. 1-255 characters.

- `metadata: optional map[string]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

### Returns

- `BetaManagedAgentsCredential = object { id, archived_at, auth, 6 more }`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: string`

    Unique identifier for the credential.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse or BetaManagedAgentsStaticBearerAuthResponse`

    Authentication details for a credential.

    - `BetaManagedAgentsMCPOAuthAuthResponse = object { mcp_server_url, type, expires_at, refresh }`

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

          - `BetaManagedAgentsTokenEndpointAuthNoneResponse = object { type }`

            Token endpoint requires no client authentication.

            - `type: "none"`

              - `"none"`

          - `BetaManagedAgentsTokenEndpointAuthBasicResponse = object { type }`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

              - `"client_secret_basic"`

          - `BetaManagedAgentsTokenEndpointAuthPostResponse = object { type }`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

              - `"client_secret_post"`

        - `resource: optional string`

          OAuth resource indicator.

        - `scope: optional string`

          OAuth scope for the refresh request.

    - `BetaManagedAgentsStaticBearerAuthResponse = object { mcp_server_url, type }`

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

### Example

```http
curl https://api.anthropic.com/v1/vaults/$VAULT_ID/credentials/$CREDENTIAL_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "display_name": "Example credential",
          "metadata": {
            "environment": "production"
          }
        }'
```

## Delete

**delete** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete Credential

### Path Parameters

- `vault_id: string`

- `credential_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 21 more`

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

- `BetaManagedAgentsDeletedCredential = object { id, type }`

  Confirmation of a deleted credential.

  - `id: string`

    Unique identifier of the deleted credential.

  - `type: "vault_credential_deleted"`

    - `"vault_credential_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/vaults/$VAULT_ID/credentials/$CREDENTIAL_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Archive

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/archive`

Archive Credential

### Path Parameters

- `vault_id: string`

- `credential_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 21 more`

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

- `BetaManagedAgentsCredential = object { id, archived_at, auth, 6 more }`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: string`

    Unique identifier for the credential.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse or BetaManagedAgentsStaticBearerAuthResponse`

    Authentication details for a credential.

    - `BetaManagedAgentsMCPOAuthAuthResponse = object { mcp_server_url, type, expires_at, refresh }`

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

          - `BetaManagedAgentsTokenEndpointAuthNoneResponse = object { type }`

            Token endpoint requires no client authentication.

            - `type: "none"`

              - `"none"`

          - `BetaManagedAgentsTokenEndpointAuthBasicResponse = object { type }`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

              - `"client_secret_basic"`

          - `BetaManagedAgentsTokenEndpointAuthPostResponse = object { type }`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

              - `"client_secret_post"`

        - `resource: optional string`

          OAuth resource indicator.

        - `scope: optional string`

          OAuth scope for the refresh request.

    - `BetaManagedAgentsStaticBearerAuthResponse = object { mcp_server_url, type }`

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

### Example

```http
curl https://api.anthropic.com/v1/vaults/$VAULT_ID/credentials/$CREDENTIAL_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## MCP OAuth Validate

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate Credential

### Path Parameters

- `vault_id: string`

- `credential_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 21 more`

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

- `BetaManagedAgentsCredentialValidation = object { credential_id, has_refresh_token, mcp_probe, 5 more }`

  Result of live-probing a credential against its configured MCP server.

  - `credential_id: string`

    Unique identifier of the credential that was validated.

  - `has_refresh_token: boolean`

    Whether the credential has a refresh token configured.

  - `mcp_probe: BetaManagedAgentsMCPProbe`

    The failing step of an MCP validation probe.

    - `http_response: BetaManagedAgentsRefreshHTTPResponse`

      An HTTP response captured during a credential validation probe.

      - `body: string`

        Response body. May be truncated and has sensitive values scrubbed.

      - `body_truncated: boolean`

        Whether `body` was truncated.

      - `content_type: string`

        Value of the `Content-Type` response header.

      - `status_code: number`

        HTTP status code.

    - `method: string`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `refresh: BetaManagedAgentsRefreshObject`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `http_response: BetaManagedAgentsRefreshHTTPResponse`

      An HTTP response captured during a credential validation probe.

      - `body: string`

        Response body. May be truncated and has sensitive values scrubbed.

      - `body_truncated: boolean`

        Whether `body` was truncated.

      - `content_type: string`

        Value of the `Content-Type` response header.

      - `status_code: number`

        HTTP status code.

    - `status: "succeeded" or "failed" or "connect_error" or "no_refresh_token"`

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

  - `type: "vault_credential_validation"`

    - `"vault_credential_validation"`

  - `validated_at: string`

    A timestamp in RFC 3339 format

  - `vault_id: string`

    Identifier of the vault containing the credential.

### Example

```http
curl https://api.anthropic.com/v1/vaults/$VAULT_ID/credentials/$CREDENTIAL_ID/mcp_oauth_validate \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Domain Types

### Beta Managed Agents Credential

- `BetaManagedAgentsCredential = object { id, archived_at, auth, 6 more }`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: string`

    Unique identifier for the credential.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse or BetaManagedAgentsStaticBearerAuthResponse`

    Authentication details for a credential.

    - `BetaManagedAgentsMCPOAuthAuthResponse = object { mcp_server_url, type, expires_at, refresh }`

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

          - `BetaManagedAgentsTokenEndpointAuthNoneResponse = object { type }`

            Token endpoint requires no client authentication.

            - `type: "none"`

              - `"none"`

          - `BetaManagedAgentsTokenEndpointAuthBasicResponse = object { type }`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

              - `"client_secret_basic"`

          - `BetaManagedAgentsTokenEndpointAuthPostResponse = object { type }`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

              - `"client_secret_post"`

        - `resource: optional string`

          OAuth resource indicator.

        - `scope: optional string`

          OAuth scope for the refresh request.

    - `BetaManagedAgentsStaticBearerAuthResponse = object { mcp_server_url, type }`

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

### Beta Managed Agents Credential Validation

- `BetaManagedAgentsCredentialValidation = object { credential_id, has_refresh_token, mcp_probe, 5 more }`

  Result of live-probing a credential against its configured MCP server.

  - `credential_id: string`

    Unique identifier of the credential that was validated.

  - `has_refresh_token: boolean`

    Whether the credential has a refresh token configured.

  - `mcp_probe: BetaManagedAgentsMCPProbe`

    The failing step of an MCP validation probe.

    - `http_response: BetaManagedAgentsRefreshHTTPResponse`

      An HTTP response captured during a credential validation probe.

      - `body: string`

        Response body. May be truncated and has sensitive values scrubbed.

      - `body_truncated: boolean`

        Whether `body` was truncated.

      - `content_type: string`

        Value of the `Content-Type` response header.

      - `status_code: number`

        HTTP status code.

    - `method: string`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `refresh: BetaManagedAgentsRefreshObject`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `http_response: BetaManagedAgentsRefreshHTTPResponse`

      An HTTP response captured during a credential validation probe.

      - `body: string`

        Response body. May be truncated and has sensitive values scrubbed.

      - `body_truncated: boolean`

        Whether `body` was truncated.

      - `content_type: string`

        Value of the `Content-Type` response header.

      - `status_code: number`

        HTTP status code.

    - `status: "succeeded" or "failed" or "connect_error" or "no_refresh_token"`

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

  - `type: "vault_credential_validation"`

    - `"vault_credential_validation"`

  - `validated_at: string`

    A timestamp in RFC 3339 format

  - `vault_id: string`

    Identifier of the vault containing the credential.

### Beta Managed Agents Credential Validation Status

- `BetaManagedAgentsCredentialValidationStatus = "valid" or "invalid" or "unknown"`

  Overall verdict of a credential validation probe.

  - `"valid"`

  - `"invalid"`

  - `"unknown"`

### Beta Managed Agents Deleted Credential

- `BetaManagedAgentsDeletedCredential = object { id, type }`

  Confirmation of a deleted credential.

  - `id: string`

    Unique identifier of the deleted credential.

  - `type: "vault_credential_deleted"`

    - `"vault_credential_deleted"`

### Beta Managed Agents MCP OAuth Auth Response

- `BetaManagedAgentsMCPOAuthAuthResponse = object { mcp_server_url, type, expires_at, refresh }`

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

      - `BetaManagedAgentsTokenEndpointAuthNoneResponse = object { type }`

        Token endpoint requires no client authentication.

        - `type: "none"`

          - `"none"`

      - `BetaManagedAgentsTokenEndpointAuthBasicResponse = object { type }`

        Token endpoint uses HTTP Basic authentication with client credentials.

        - `type: "client_secret_basic"`

          - `"client_secret_basic"`

      - `BetaManagedAgentsTokenEndpointAuthPostResponse = object { type }`

        Token endpoint uses POST body authentication with client credentials.

        - `type: "client_secret_post"`

          - `"client_secret_post"`

    - `resource: optional string`

      OAuth resource indicator.

    - `scope: optional string`

      OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Create Params

- `BetaManagedAgentsMCPOAuthCreateParams = object { access_token, mcp_server_url, type, 2 more }`

  Parameters for creating an MCP OAuth credential.

  - `access_token: string`

    OAuth access token.

  - `mcp_server_url: string`

    URL of the MCP server this credential authenticates against.

  - `type: "mcp_oauth"`

    - `"mcp_oauth"`

  - `expires_at: optional string`

    A timestamp in RFC 3339 format

  - `refresh: optional BetaManagedAgentsMCPOAuthRefreshParams`

    OAuth refresh token parameters for creating a credential with refresh support.

    - `client_id: string`

      OAuth client ID.

    - `refresh_token: string`

      OAuth refresh token.

    - `token_endpoint: string`

      Token endpoint URL used to refresh the access token.

    - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneParam or BetaManagedAgentsTokenEndpointAuthBasicParam or BetaManagedAgentsTokenEndpointAuthPostParam`

      Token endpoint requires no client authentication.

      - `BetaManagedAgentsTokenEndpointAuthNoneParam = object { type }`

        Token endpoint requires no client authentication.

        - `type: "none"`

          - `"none"`

      - `BetaManagedAgentsTokenEndpointAuthBasicParam = object { client_secret, type }`

        Token endpoint uses HTTP Basic authentication with client credentials.

        - `client_secret: string`

          OAuth client secret.

        - `type: "client_secret_basic"`

          - `"client_secret_basic"`

      - `BetaManagedAgentsTokenEndpointAuthPostParam = object { client_secret, type }`

        Token endpoint uses POST body authentication with client credentials.

        - `client_secret: string`

          OAuth client secret.

        - `type: "client_secret_post"`

          - `"client_secret_post"`

    - `resource: optional string`

      OAuth resource indicator.

    - `scope: optional string`

      OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Params

- `BetaManagedAgentsMCPOAuthRefreshParams = object { client_id, refresh_token, token_endpoint, 3 more }`

  OAuth refresh token parameters for creating a credential with refresh support.

  - `client_id: string`

    OAuth client ID.

  - `refresh_token: string`

    OAuth refresh token.

  - `token_endpoint: string`

    Token endpoint URL used to refresh the access token.

  - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneParam or BetaManagedAgentsTokenEndpointAuthBasicParam or BetaManagedAgentsTokenEndpointAuthPostParam`

    Token endpoint requires no client authentication.

    - `BetaManagedAgentsTokenEndpointAuthNoneParam = object { type }`

      Token endpoint requires no client authentication.

      - `type: "none"`

        - `"none"`

    - `BetaManagedAgentsTokenEndpointAuthBasicParam = object { client_secret, type }`

      Token endpoint uses HTTP Basic authentication with client credentials.

      - `client_secret: string`

        OAuth client secret.

      - `type: "client_secret_basic"`

        - `"client_secret_basic"`

    - `BetaManagedAgentsTokenEndpointAuthPostParam = object { client_secret, type }`

      Token endpoint uses POST body authentication with client credentials.

      - `client_secret: string`

        OAuth client secret.

      - `type: "client_secret_post"`

        - `"client_secret_post"`

  - `resource: optional string`

    OAuth resource indicator.

  - `scope: optional string`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Response

- `BetaManagedAgentsMCPOAuthRefreshResponse = object { client_id, token_endpoint, token_endpoint_auth, 2 more }`

  OAuth refresh token configuration returned in credential responses.

  - `client_id: string`

    OAuth client ID.

  - `token_endpoint: string`

    Token endpoint URL used to refresh the access token.

  - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse or BetaManagedAgentsTokenEndpointAuthBasicResponse or BetaManagedAgentsTokenEndpointAuthPostResponse`

    Token endpoint requires no client authentication.

    - `BetaManagedAgentsTokenEndpointAuthNoneResponse = object { type }`

      Token endpoint requires no client authentication.

      - `type: "none"`

        - `"none"`

    - `BetaManagedAgentsTokenEndpointAuthBasicResponse = object { type }`

      Token endpoint uses HTTP Basic authentication with client credentials.

      - `type: "client_secret_basic"`

        - `"client_secret_basic"`

    - `BetaManagedAgentsTokenEndpointAuthPostResponse = object { type }`

      Token endpoint uses POST body authentication with client credentials.

      - `type: "client_secret_post"`

        - `"client_secret_post"`

  - `resource: optional string`

    OAuth resource indicator.

  - `scope: optional string`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Update Params

- `BetaManagedAgentsMCPOAuthRefreshUpdateParams = object { refresh_token, scope, token_endpoint_auth }`

  Parameters for updating OAuth refresh token configuration.

  - `refresh_token: optional string`

    Updated OAuth refresh token.

  - `scope: optional string`

    Updated OAuth scope for the refresh request.

  - `token_endpoint_auth: optional BetaManagedAgentsTokenEndpointAuthBasicUpdateParam or BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

    Updated HTTP Basic authentication parameters for the token endpoint.

    - `BetaManagedAgentsTokenEndpointAuthBasicUpdateParam = object { type, client_secret }`

      Updated HTTP Basic authentication parameters for the token endpoint.

      - `type: "client_secret_basic"`

        - `"client_secret_basic"`

      - `client_secret: optional string`

        Updated OAuth client secret.

    - `BetaManagedAgentsTokenEndpointAuthPostUpdateParam = object { type, client_secret }`

      Updated POST body authentication parameters for the token endpoint.

      - `type: "client_secret_post"`

        - `"client_secret_post"`

      - `client_secret: optional string`

        Updated OAuth client secret.

### Beta Managed Agents MCP OAuth Update Params

- `BetaManagedAgentsMCPOAuthUpdateParams = object { type, access_token, expires_at, refresh }`

  Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

  - `type: "mcp_oauth"`

    - `"mcp_oauth"`

  - `access_token: optional string`

    Updated OAuth access token.

  - `expires_at: optional string`

    A timestamp in RFC 3339 format

  - `refresh: optional BetaManagedAgentsMCPOAuthRefreshUpdateParams`

    Parameters for updating OAuth refresh token configuration.

    - `refresh_token: optional string`

      Updated OAuth refresh token.

    - `scope: optional string`

      Updated OAuth scope for the refresh request.

    - `token_endpoint_auth: optional BetaManagedAgentsTokenEndpointAuthBasicUpdateParam or BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

      Updated HTTP Basic authentication parameters for the token endpoint.

      - `BetaManagedAgentsTokenEndpointAuthBasicUpdateParam = object { type, client_secret }`

        Updated HTTP Basic authentication parameters for the token endpoint.

        - `type: "client_secret_basic"`

          - `"client_secret_basic"`

        - `client_secret: optional string`

          Updated OAuth client secret.

      - `BetaManagedAgentsTokenEndpointAuthPostUpdateParam = object { type, client_secret }`

        Updated POST body authentication parameters for the token endpoint.

        - `type: "client_secret_post"`

          - `"client_secret_post"`

        - `client_secret: optional string`

          Updated OAuth client secret.

### Beta Managed Agents MCP Probe

- `BetaManagedAgentsMCPProbe = object { http_response, method }`

  The failing step of an MCP validation probe.

  - `http_response: BetaManagedAgentsRefreshHTTPResponse`

    An HTTP response captured during a credential validation probe.

    - `body: string`

      Response body. May be truncated and has sensitive values scrubbed.

    - `body_truncated: boolean`

      Whether `body` was truncated.

    - `content_type: string`

      Value of the `Content-Type` response header.

    - `status_code: number`

      HTTP status code.

  - `method: string`

    The MCP method that failed (for example `initialize` or `tools/list`).

### Beta Managed Agents Refresh HTTP Response

- `BetaManagedAgentsRefreshHTTPResponse = object { body, body_truncated, content_type, status_code }`

  An HTTP response captured during a credential validation probe.

  - `body: string`

    Response body. May be truncated and has sensitive values scrubbed.

  - `body_truncated: boolean`

    Whether `body` was truncated.

  - `content_type: string`

    Value of the `Content-Type` response header.

  - `status_code: number`

    HTTP status code.

### Beta Managed Agents Refresh Object

- `BetaManagedAgentsRefreshObject = object { http_response, status }`

  Outcome of a refresh-token exchange attempted during credential validation.

  - `http_response: BetaManagedAgentsRefreshHTTPResponse`

    An HTTP response captured during a credential validation probe.

    - `body: string`

      Response body. May be truncated and has sensitive values scrubbed.

    - `body_truncated: boolean`

      Whether `body` was truncated.

    - `content_type: string`

      Value of the `Content-Type` response header.

    - `status_code: number`

      HTTP status code.

  - `status: "succeeded" or "failed" or "connect_error" or "no_refresh_token"`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `"succeeded"`

    - `"failed"`

    - `"connect_error"`

    - `"no_refresh_token"`

### Beta Managed Agents Static Bearer Auth Response

- `BetaManagedAgentsStaticBearerAuthResponse = object { mcp_server_url, type }`

  Static bearer token credential details for an MCP server.

  - `mcp_server_url: string`

    URL of the MCP server this credential authenticates against.

  - `type: "static_bearer"`

    - `"static_bearer"`

### Beta Managed Agents Static Bearer Create Params

- `BetaManagedAgentsStaticBearerCreateParams = object { token, mcp_server_url, type }`

  Parameters for creating a static bearer token credential.

  - `token: string`

    Static bearer token value.

  - `mcp_server_url: string`

    URL of the MCP server this credential authenticates against.

  - `type: "static_bearer"`

    - `"static_bearer"`

### Beta Managed Agents Static Bearer Update Params

- `BetaManagedAgentsStaticBearerUpdateParams = object { type, token }`

  Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

  - `type: "static_bearer"`

    - `"static_bearer"`

  - `token: optional string`

    Updated static bearer token value.

### Beta Managed Agents Token Endpoint Auth Basic Param

- `BetaManagedAgentsTokenEndpointAuthBasicParam = object { client_secret, type }`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `client_secret: string`

    OAuth client secret.

  - `type: "client_secret_basic"`

    - `"client_secret_basic"`

### Beta Managed Agents Token Endpoint Auth Basic Response

- `BetaManagedAgentsTokenEndpointAuthBasicResponse = object { type }`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `type: "client_secret_basic"`

    - `"client_secret_basic"`

### Beta Managed Agents Token Endpoint Auth Basic Update Param

- `BetaManagedAgentsTokenEndpointAuthBasicUpdateParam = object { type, client_secret }`

  Updated HTTP Basic authentication parameters for the token endpoint.

  - `type: "client_secret_basic"`

    - `"client_secret_basic"`

  - `client_secret: optional string`

    Updated OAuth client secret.

### Beta Managed Agents Token Endpoint Auth None Param

- `BetaManagedAgentsTokenEndpointAuthNoneParam = object { type }`

  Token endpoint requires no client authentication.

  - `type: "none"`

    - `"none"`

### Beta Managed Agents Token Endpoint Auth None Response

- `BetaManagedAgentsTokenEndpointAuthNoneResponse = object { type }`

  Token endpoint requires no client authentication.

  - `type: "none"`

    - `"none"`

### Beta Managed Agents Token Endpoint Auth Post Param

- `BetaManagedAgentsTokenEndpointAuthPostParam = object { client_secret, type }`

  Token endpoint uses POST body authentication with client credentials.

  - `client_secret: string`

    OAuth client secret.

  - `type: "client_secret_post"`

    - `"client_secret_post"`

### Beta Managed Agents Token Endpoint Auth Post Response

- `BetaManagedAgentsTokenEndpointAuthPostResponse = object { type }`

  Token endpoint uses POST body authentication with client credentials.

  - `type: "client_secret_post"`

    - `"client_secret_post"`

### Beta Managed Agents Token Endpoint Auth Post Update Param

- `BetaManagedAgentsTokenEndpointAuthPostUpdateParam = object { type, client_secret }`

  Updated POST body authentication parameters for the token endpoint.

  - `type: "client_secret_post"`

    - `"client_secret_post"`

  - `client_secret: optional string`

    Updated OAuth client secret.
