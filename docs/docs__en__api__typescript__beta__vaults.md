# Vaults

## Create

`client.beta.vaults.create(VaultCreateParamsparams, RequestOptionsoptions?): BetaManagedAgentsVault`

**post** `/v1/vaults`

Create Vault

### Parameters

- `params: VaultCreateParams`

  - `display_name: string`

    Body param: Human-readable name for the vault. 1-255 characters.

  - `metadata?: Record<string, string>`

    Body param: Arbitrary key-value metadata to attach to the vault.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 18 more`

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

### Returns

- `BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `id: string`

    Unique identifier for the vault.

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata attached to the vault.

  - `type: "vault"`

    - `"vault"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsVault = await client.beta.vaults.create({ display_name: 'Example vault' });

console.log(betaManagedAgentsVault.id);
```

## List

`client.beta.vaults.list(VaultListParamsparams?, RequestOptionsoptions?): PageCursor<BetaManagedAgentsVault>`

**get** `/v1/vaults`

List Vaults

### Parameters

- `params: VaultListParams`

  - `include_archived?: boolean`

    Query param: Whether to include archived vaults in the results.

  - `limit?: number`

    Query param: Maximum number of vaults to return per page. Defaults to 20, maximum 100.

  - `page?: string`

    Query param: Opaque pagination token from a previous `list_vaults` response.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 18 more`

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

### Returns

- `BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `id: string`

    Unique identifier for the vault.

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata attached to the vault.

  - `type: "vault"`

    - `"vault"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsVault of client.beta.vaults.list()) {
  console.log(betaManagedAgentsVault.id);
}
```

## Retrieve

`client.beta.vaults.retrieve(stringvaultID, VaultRetrieveParamsparams?, RequestOptionsoptions?): BetaManagedAgentsVault`

**get** `/v1/vaults/{vault_id}`

Get Vault

### Parameters

- `vaultID: string`

- `params: VaultRetrieveParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 18 more`

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

### Returns

- `BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `id: string`

    Unique identifier for the vault.

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata attached to the vault.

  - `type: "vault"`

    - `"vault"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsVault = await client.beta.vaults.retrieve('vlt_011CZkZDLs7fYzm1hXNPeRjv');

console.log(betaManagedAgentsVault.id);
```

## Update

`client.beta.vaults.update(stringvaultID, VaultUpdateParamsparams, RequestOptionsoptions?): BetaManagedAgentsVault`

**post** `/v1/vaults/{vault_id}`

Update Vault

### Parameters

- `vaultID: string`

- `params: VaultUpdateParams`

  - `display_name?: string | null`

    Body param: Updated human-readable name for the vault. 1-255 characters.

  - `metadata?: Record<string, string | null> | null`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 18 more`

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

### Returns

- `BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `id: string`

    Unique identifier for the vault.

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata attached to the vault.

  - `type: "vault"`

    - `"vault"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsVault = await client.beta.vaults.update('vlt_011CZkZDLs7fYzm1hXNPeRjv');

console.log(betaManagedAgentsVault.id);
```

## Delete

`client.beta.vaults.delete(stringvaultID, VaultDeleteParamsparams?, RequestOptionsoptions?): BetaManagedAgentsDeletedVault`

**delete** `/v1/vaults/{vault_id}`

Delete Vault

### Parameters

- `vaultID: string`

- `params: VaultDeleteParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 18 more`

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

### Returns

- `BetaManagedAgentsDeletedVault`

  Confirmation of a deleted vault.

  - `id: string`

    Unique identifier of the deleted vault.

  - `type: "vault_deleted"`

    - `"vault_deleted"`

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsDeletedVault = await client.beta.vaults.delete(
  'vlt_011CZkZDLs7fYzm1hXNPeRjv',
);

console.log(betaManagedAgentsDeletedVault.id);
```

## Archive

`client.beta.vaults.archive(stringvaultID, VaultArchiveParamsparams?, RequestOptionsoptions?): BetaManagedAgentsVault`

**post** `/v1/vaults/{vault_id}/archive`

Archive Vault

### Parameters

- `vaultID: string`

- `params: VaultArchiveParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 18 more`

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

### Returns

- `BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `id: string`

    Unique identifier for the vault.

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata attached to the vault.

  - `type: "vault"`

    - `"vault"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsVault = await client.beta.vaults.archive('vlt_011CZkZDLs7fYzm1hXNPeRjv');

console.log(betaManagedAgentsVault.id);
```

## Domain Types

### Beta Managed Agents Deleted Vault

- `BetaManagedAgentsDeletedVault`

  Confirmation of a deleted vault.

  - `id: string`

    Unique identifier of the deleted vault.

  - `type: "vault_deleted"`

    - `"vault_deleted"`

### Beta Managed Agents Vault

- `BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `id: string`

    Unique identifier for the vault.

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata attached to the vault.

  - `type: "vault"`

    - `"vault"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

# Credentials

## Create

`client.beta.vaults.credentials.create(stringvaultID, CredentialCreateParamsparams, RequestOptionsoptions?): BetaManagedAgentsCredential`

**post** `/v1/vaults/{vault_id}/credentials`

Create Credential

### Parameters

- `vaultID: string`

- `params: CredentialCreateParams`

  - `auth: BetaManagedAgentsMCPOAuthCreateParams | BetaManagedAgentsStaticBearerCreateParams`

    Body param: Authentication details for creating a credential.

    - `BetaManagedAgentsMCPOAuthCreateParams`

      Parameters for creating an MCP OAuth credential.

      - `access_token: string`

        OAuth access token.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "mcp_oauth"`

        - `"mcp_oauth"`

      - `expires_at?: string | null`

        A timestamp in RFC 3339 format

      - `refresh?: BetaManagedAgentsMCPOAuthRefreshParams | null`

        OAuth refresh token parameters for creating a credential with refresh support.

        - `client_id: string`

          OAuth client ID.

        - `refresh_token: string`

          OAuth refresh token.

        - `token_endpoint: string`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneParam | BetaManagedAgentsTokenEndpointAuthBasicParam | BetaManagedAgentsTokenEndpointAuthPostParam`

          Token endpoint requires no client authentication.

          - `BetaManagedAgentsTokenEndpointAuthNoneParam`

            Token endpoint requires no client authentication.

            - `type: "none"`

              - `"none"`

          - `BetaManagedAgentsTokenEndpointAuthBasicParam`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `client_secret: string`

              OAuth client secret.

            - `type: "client_secret_basic"`

              - `"client_secret_basic"`

          - `BetaManagedAgentsTokenEndpointAuthPostParam`

            Token endpoint uses POST body authentication with client credentials.

            - `client_secret: string`

              OAuth client secret.

            - `type: "client_secret_post"`

              - `"client_secret_post"`

        - `resource?: string | null`

          OAuth resource indicator.

        - `scope?: string | null`

          OAuth scope for the refresh request.

    - `BetaManagedAgentsStaticBearerCreateParams`

      Parameters for creating a static bearer token credential.

      - `token: string`

        Static bearer token value.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "static_bearer"`

        - `"static_bearer"`

  - `display_name?: string | null`

    Body param: Human-readable name for the credential. Up to 255 characters.

  - `metadata?: Record<string, string>`

    Body param: Arbitrary key-value metadata to attach to the credential.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 18 more`

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

const betaManagedAgentsCredential = await client.beta.vaults.credentials.create(
  'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  {
    auth: {
      token: 'bearer_exampletoken',
      mcp_server_url: 'https://example-server.modelcontextprotocol.io/sse',
      type: 'static_bearer',
    },
  },
);

console.log(betaManagedAgentsCredential.id);
```

## List

`client.beta.vaults.credentials.list(stringvaultID, CredentialListParamsparams?, RequestOptionsoptions?): PageCursor<BetaManagedAgentsCredential>`

**get** `/v1/vaults/{vault_id}/credentials`

List Credentials

### Parameters

- `vaultID: string`

- `params: CredentialListParams`

  - `include_archived?: boolean`

    Query param: Whether to include archived credentials in the results.

  - `limit?: number`

    Query param: Maximum number of credentials to return per page. Defaults to 20, maximum 100.

  - `page?: string`

    Query param: Opaque pagination token from a previous `list_credentials` response.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 18 more`

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

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsCredential of client.beta.vaults.credentials.list(
  'vlt_011CZkZDLs7fYzm1hXNPeRjv',
)) {
  console.log(betaManagedAgentsCredential.id);
}
```

## Retrieve

`client.beta.vaults.credentials.retrieve(stringcredentialID, CredentialRetrieveParamsparams, RequestOptionsoptions?): BetaManagedAgentsCredential`

**get** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Get Credential

### Parameters

- `credentialID: string`

- `params: CredentialRetrieveParams`

  - `vault_id: string`

    Path param: Path parameter vault_id

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 18 more`

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

const betaManagedAgentsCredential = await client.beta.vaults.credentials.retrieve(
  'vcrd_011CZkZEMt8gZan2iYOQfSkw',
  { vault_id: 'vlt_011CZkZDLs7fYzm1hXNPeRjv' },
);

console.log(betaManagedAgentsCredential.id);
```

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

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 18 more`

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

## Delete

`client.beta.vaults.credentials.delete(stringcredentialID, CredentialDeleteParamsparams, RequestOptionsoptions?): BetaManagedAgentsDeletedCredential`

**delete** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete Credential

### Parameters

- `credentialID: string`

- `params: CredentialDeleteParams`

  - `vault_id: string`

    Path param: Path parameter vault_id

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 18 more`

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

### Returns

- `BetaManagedAgentsDeletedCredential`

  Confirmation of a deleted credential.

  - `id: string`

    Unique identifier of the deleted credential.

  - `type: "vault_credential_deleted"`

    - `"vault_credential_deleted"`

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsDeletedCredential = await client.beta.vaults.credentials.delete(
  'vcrd_011CZkZEMt8gZan2iYOQfSkw',
  { vault_id: 'vlt_011CZkZDLs7fYzm1hXNPeRjv' },
);

console.log(betaManagedAgentsDeletedCredential.id);
```

## Archive

`client.beta.vaults.credentials.archive(stringcredentialID, CredentialArchiveParamsparams, RequestOptionsoptions?): BetaManagedAgentsCredential`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/archive`

Archive Credential

### Parameters

- `credentialID: string`

- `params: CredentialArchiveParams`

  - `vault_id: string`

    Path param: Path parameter vault_id

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 18 more`

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

const betaManagedAgentsCredential = await client.beta.vaults.credentials.archive(
  'vcrd_011CZkZEMt8gZan2iYOQfSkw',
  { vault_id: 'vlt_011CZkZDLs7fYzm1hXNPeRjv' },
);

console.log(betaManagedAgentsCredential.id);
```

## Domain Types

### Beta Managed Agents Credential

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

### Beta Managed Agents Deleted Credential

- `BetaManagedAgentsDeletedCredential`

  Confirmation of a deleted credential.

  - `id: string`

    Unique identifier of the deleted credential.

  - `type: "vault_credential_deleted"`

    - `"vault_credential_deleted"`

### Beta Managed Agents MCP OAuth Auth Response

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

### Beta Managed Agents MCP OAuth Create Params

- `BetaManagedAgentsMCPOAuthCreateParams`

  Parameters for creating an MCP OAuth credential.

  - `access_token: string`

    OAuth access token.

  - `mcp_server_url: string`

    URL of the MCP server this credential authenticates against.

  - `type: "mcp_oauth"`

    - `"mcp_oauth"`

  - `expires_at?: string | null`

    A timestamp in RFC 3339 format

  - `refresh?: BetaManagedAgentsMCPOAuthRefreshParams | null`

    OAuth refresh token parameters for creating a credential with refresh support.

    - `client_id: string`

      OAuth client ID.

    - `refresh_token: string`

      OAuth refresh token.

    - `token_endpoint: string`

      Token endpoint URL used to refresh the access token.

    - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneParam | BetaManagedAgentsTokenEndpointAuthBasicParam | BetaManagedAgentsTokenEndpointAuthPostParam`

      Token endpoint requires no client authentication.

      - `BetaManagedAgentsTokenEndpointAuthNoneParam`

        Token endpoint requires no client authentication.

        - `type: "none"`

          - `"none"`

      - `BetaManagedAgentsTokenEndpointAuthBasicParam`

        Token endpoint uses HTTP Basic authentication with client credentials.

        - `client_secret: string`

          OAuth client secret.

        - `type: "client_secret_basic"`

          - `"client_secret_basic"`

      - `BetaManagedAgentsTokenEndpointAuthPostParam`

        Token endpoint uses POST body authentication with client credentials.

        - `client_secret: string`

          OAuth client secret.

        - `type: "client_secret_post"`

          - `"client_secret_post"`

    - `resource?: string | null`

      OAuth resource indicator.

    - `scope?: string | null`

      OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Params

- `BetaManagedAgentsMCPOAuthRefreshParams`

  OAuth refresh token parameters for creating a credential with refresh support.

  - `client_id: string`

    OAuth client ID.

  - `refresh_token: string`

    OAuth refresh token.

  - `token_endpoint: string`

    Token endpoint URL used to refresh the access token.

  - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneParam | BetaManagedAgentsTokenEndpointAuthBasicParam | BetaManagedAgentsTokenEndpointAuthPostParam`

    Token endpoint requires no client authentication.

    - `BetaManagedAgentsTokenEndpointAuthNoneParam`

      Token endpoint requires no client authentication.

      - `type: "none"`

        - `"none"`

    - `BetaManagedAgentsTokenEndpointAuthBasicParam`

      Token endpoint uses HTTP Basic authentication with client credentials.

      - `client_secret: string`

        OAuth client secret.

      - `type: "client_secret_basic"`

        - `"client_secret_basic"`

    - `BetaManagedAgentsTokenEndpointAuthPostParam`

      Token endpoint uses POST body authentication with client credentials.

      - `client_secret: string`

        OAuth client secret.

      - `type: "client_secret_post"`

        - `"client_secret_post"`

  - `resource?: string | null`

    OAuth resource indicator.

  - `scope?: string | null`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Response

- `BetaManagedAgentsMCPOAuthRefreshResponse`

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

### Beta Managed Agents MCP OAuth Refresh Update Params

- `BetaManagedAgentsMCPOAuthRefreshUpdateParams`

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

### Beta Managed Agents MCP OAuth Update Params

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

### Beta Managed Agents Static Bearer Auth Response

- `BetaManagedAgentsStaticBearerAuthResponse`

  Static bearer token credential details for an MCP server.

  - `mcp_server_url: string`

    URL of the MCP server this credential authenticates against.

  - `type: "static_bearer"`

    - `"static_bearer"`

### Beta Managed Agents Static Bearer Create Params

- `BetaManagedAgentsStaticBearerCreateParams`

  Parameters for creating a static bearer token credential.

  - `token: string`

    Static bearer token value.

  - `mcp_server_url: string`

    URL of the MCP server this credential authenticates against.

  - `type: "static_bearer"`

    - `"static_bearer"`

### Beta Managed Agents Static Bearer Update Params

- `BetaManagedAgentsStaticBearerUpdateParams`

  Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

  - `type: "static_bearer"`

    - `"static_bearer"`

  - `token?: string | null`

    Updated static bearer token value.

### Beta Managed Agents Token Endpoint Auth Basic Param

- `BetaManagedAgentsTokenEndpointAuthBasicParam`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `client_secret: string`

    OAuth client secret.

  - `type: "client_secret_basic"`

    - `"client_secret_basic"`

### Beta Managed Agents Token Endpoint Auth Basic Response

- `BetaManagedAgentsTokenEndpointAuthBasicResponse`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `type: "client_secret_basic"`

    - `"client_secret_basic"`

### Beta Managed Agents Token Endpoint Auth Basic Update Param

- `BetaManagedAgentsTokenEndpointAuthBasicUpdateParam`

  Updated HTTP Basic authentication parameters for the token endpoint.

  - `type: "client_secret_basic"`

    - `"client_secret_basic"`

  - `client_secret?: string | null`

    Updated OAuth client secret.

### Beta Managed Agents Token Endpoint Auth None Param

- `BetaManagedAgentsTokenEndpointAuthNoneParam`

  Token endpoint requires no client authentication.

  - `type: "none"`

    - `"none"`

### Beta Managed Agents Token Endpoint Auth None Response

- `BetaManagedAgentsTokenEndpointAuthNoneResponse`

  Token endpoint requires no client authentication.

  - `type: "none"`

    - `"none"`

### Beta Managed Agents Token Endpoint Auth Post Param

- `BetaManagedAgentsTokenEndpointAuthPostParam`

  Token endpoint uses POST body authentication with client credentials.

  - `client_secret: string`

    OAuth client secret.

  - `type: "client_secret_post"`

    - `"client_secret_post"`

### Beta Managed Agents Token Endpoint Auth Post Response

- `BetaManagedAgentsTokenEndpointAuthPostResponse`

  Token endpoint uses POST body authentication with client credentials.

  - `type: "client_secret_post"`

    - `"client_secret_post"`

### Beta Managed Agents Token Endpoint Auth Post Update Param

- `BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

  Updated POST body authentication parameters for the token endpoint.

  - `type: "client_secret_post"`

    - `"client_secret_post"`

  - `client_secret?: string | null`

    Updated OAuth client secret.
