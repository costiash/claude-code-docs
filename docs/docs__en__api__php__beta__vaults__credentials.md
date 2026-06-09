# Credentials

## Create Credential

`$client->beta->vaults->credentials->create(string vaultID, Auth auth, ?string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas): ManagedAgentsCredential`

**post** `/v1/vaults/{vault_id}/credentials`

Create Credential

### Parameters

- `vaultID: string`

- `auth: Auth`

  Authentication details for creating a credential.

- `displayName?:optional string`

  Human-readable name for the credential. Up to 255 characters.

- `metadata?:optional array<string,string>`

  Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsCredential`

  - `string id`

    Unique identifier for the credential.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `string vaultID`

    Identifier of the vault this credential belongs to.

  - `?string displayName`

    Human-readable name for the credential.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsCredential = $client->beta->vaults->credentials->create(
  'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  auth: [
    'token' => 'bearer_exampletoken',
    'mcpServerURL' => 'https://example-server.modelcontextprotocol.io/sse',
    'type' => 'static_bearer',
  ],
  displayName: 'Example credential',
  metadata: ['environment' => 'production'],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsCredential);
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

`$client->beta->vaults->credentials->list(string vaultID, ?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<ManagedAgentsCredential>`

**get** `/v1/vaults/{vault_id}/credentials`

List Credentials

### Parameters

- `vaultID: string`

- `includeArchived?:optional bool`

  Whether to include archived credentials in the results.

- `limit?:optional int`

  Maximum number of credentials to return per page. Defaults to 20, maximum 100.

- `page?:optional string`

  Opaque pagination token from a previous `list_credentials` response.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsCredential`

  - `string id`

    Unique identifier for the credential.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `string vaultID`

    Identifier of the vault this credential belongs to.

  - `?string displayName`

    Human-readable name for the credential.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->vaults->credentials->list(
  'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  includeArchived: true,
  limit: 0,
  page: 'page',
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
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

`$client->beta->vaults->credentials->retrieve(string credentialID, string vaultID, ?list<AnthropicBeta> betas): ManagedAgentsCredential`

**get** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Get Credential

### Parameters

- `vaultID: string`

- `credentialID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsCredential`

  - `string id`

    Unique identifier for the credential.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `string vaultID`

    Identifier of the vault this credential belongs to.

  - `?string displayName`

    Human-readable name for the credential.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsCredential = $client->beta->vaults->credentials->retrieve(
  'vcrd_011CZkZEMt8gZan2iYOQfSkw',
  vaultID: 'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsCredential);
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

`$client->beta->vaults->credentials->update(string credentialID, string vaultID, ?Auth auth, ?string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas): ManagedAgentsCredential`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update Credential

### Parameters

- `vaultID: string`

- `credentialID: string`

- `auth?:optional Auth`

  Updated authentication details for a credential.

- `displayName?:optional string`

  Updated human-readable name for the credential. 1-255 characters.

- `metadata?:optional array<string,string>`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsCredential`

  - `string id`

    Unique identifier for the credential.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `string vaultID`

    Identifier of the vault this credential belongs to.

  - `?string displayName`

    Human-readable name for the credential.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsCredential = $client->beta->vaults->credentials->update(
  'vcrd_011CZkZEMt8gZan2iYOQfSkw',
  vaultID: 'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  auth: [
    'type' => 'mcp_oauth',
    'accessToken' => 'x',
    'expiresAt' => new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
    'refresh' => [
      'refreshToken' => 'x',
      'scope' => 'scope',
      'tokenEndpointAuth' => [
        'type' => 'client_secret_basic', 'clientSecret' => 'x'
      ],
    ],
  ],
  displayName: 'Example credential',
  metadata: ['environment' => 'production'],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsCredential);
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

`$client->beta->vaults->credentials->delete(string credentialID, string vaultID, ?list<AnthropicBeta> betas): ManagedAgentsDeletedCredential`

**delete** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete Credential

### Parameters

- `vaultID: string`

- `credentialID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsDeletedCredential`

  - `string id`

    Unique identifier of the deleted credential.

  - `Type type`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeletedCredential = $client
  ->beta
  ->vaults
  ->credentials
  ->delete(
  'vcrd_011CZkZEMt8gZan2iYOQfSkw',
  vaultID: 'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsDeletedCredential);
```

#### Response

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "type": "vault_credential_deleted"
}
```

## Archive Credential

`$client->beta->vaults->credentials->archive(string credentialID, string vaultID, ?list<AnthropicBeta> betas): ManagedAgentsCredential`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/archive`

Archive Credential

### Parameters

- `vaultID: string`

- `credentialID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsCredential`

  - `string id`

    Unique identifier for the credential.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `string vaultID`

    Identifier of the vault this credential belongs to.

  - `?string displayName`

    Human-readable name for the credential.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsCredential = $client->beta->vaults->credentials->archive(
  'vcrd_011CZkZEMt8gZan2iYOQfSkw',
  vaultID: 'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsCredential);
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

`$client->beta->vaults->credentials->mcpOAuthValidate(string credentialID, string vaultID, ?list<AnthropicBeta> betas): ManagedAgentsCredentialValidation`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate Credential

### Parameters

- `vaultID: string`

- `credentialID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsCredentialValidation`

  - `string credentialID`

    Unique identifier of the credential that was validated.

  - `bool hasRefreshToken`

    Whether the credential has a refresh token configured.

  - `?ManagedAgentsMCPProbe mcpProbe`

    The failing step of an MCP validation probe.

  - `?ManagedAgentsRefreshObject refresh`

    Outcome of a refresh-token exchange attempted during credential validation.

  - `ManagedAgentsCredentialValidationStatus status`

    Overall verdict of a credential validation probe.

  - `Type type`

  - `\Datetime validatedAt`

    A timestamp in RFC 3339 format

  - `string vaultID`

    Identifier of the vault containing the credential.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsCredentialValidation = $client
  ->beta
  ->vaults
  ->credentials
  ->mcpOAuthValidate(
  'vcrd_011CZkZEMt8gZan2iYOQfSkw',
  vaultID: 'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsCredentialValidation);
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

- `ManagedAgentsCredential`

  - `string id`

    Unique identifier for the credential.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `string vaultID`

    Identifier of the vault this credential belongs to.

  - `?string displayName`

    Human-readable name for the credential.

### Beta Managed Agents Credential Networking Params

- `ManagedAgentsCredentialNetworkingParams`

  - `ManagedAgentsUnrestrictedCredentialNetworkingParams`

    - `Type type`

  - `ManagedAgentsLimitedCredentialNetworkingParams`

    - `list<string> allowedHosts`

      Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

    - `Type type`

### Beta Managed Agents Credential Validation

- `ManagedAgentsCredentialValidation`

  - `string credentialID`

    Unique identifier of the credential that was validated.

  - `bool hasRefreshToken`

    Whether the credential has a refresh token configured.

  - `?ManagedAgentsMCPProbe mcpProbe`

    The failing step of an MCP validation probe.

  - `?ManagedAgentsRefreshObject refresh`

    Outcome of a refresh-token exchange attempted during credential validation.

  - `ManagedAgentsCredentialValidationStatus status`

    Overall verdict of a credential validation probe.

  - `Type type`

  - `\Datetime validatedAt`

    A timestamp in RFC 3339 format

  - `string vaultID`

    Identifier of the vault containing the credential.

### Beta Managed Agents Credential Validation Status

- `ManagedAgentsCredentialValidationStatus`

  - `"valid"`

  - `"invalid"`

  - `"unknown"`

### Beta Managed Agents Deleted Credential

- `ManagedAgentsDeletedCredential`

  - `string id`

    Unique identifier of the deleted credential.

  - `Type type`

### Beta Managed Agents Environment Variable Auth Response

- `ManagedAgentsEnvironmentVariableAuthResponse`

  - `Networking networking`

    Outbound hosts the secret value is substituted on.

  - `string secretName`

    Name of the environment variable.

  - `Type type`

### Beta Managed Agents Environment Variable Create Params

- `ManagedAgentsEnvironmentVariableCreateParams`

  - `ManagedAgentsCredentialNetworkingParams networking`

    Outbound hosts the secret value is substituted on.

  - `string secretName`

    Name of the environment variable. Immutable after create.

  - `string secretValue`

    Secret value. Write-only; never returned in responses.

  - `Type type`

### Beta Managed Agents Environment Variable Update Params

- `ManagedAgentsEnvironmentVariableUpdateParams`

  - `Type type`

  - `?ManagedAgentsCredentialNetworkingParams networking`

    Updated networking scope. Full replacement.

  - `?string secretValue`

    Updated secret value.

### Beta Managed Agents Limited Credential Networking Params

- `ManagedAgentsLimitedCredentialNetworkingParams`

  - `list<string> allowedHosts`

    Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

  - `Type type`

### Beta Managed Agents Limited Credential Networking Response

- `ManagedAgentsLimitedCredentialNetworkingResponse`

  - `list<string> allowedHosts`

    Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

  - `Type type`

### Beta Managed Agents MCP OAuth Auth Response

- `ManagedAgentsMCPOAuthAuthResponse`

  - `string mcpServerURL`

    URL of the MCP server this credential authenticates against.

  - `Type type`

  - `?\Datetime expiresAt`

    A timestamp in RFC 3339 format

  - `?ManagedAgentsMCPOAuthRefreshResponse refresh`

    OAuth refresh token configuration returned in credential responses.

### Beta Managed Agents MCP OAuth Create Params

- `ManagedAgentsMCPOAuthCreateParams`

  - `string accessToken`

    OAuth access token.

  - `string mcpServerURL`

    URL of the MCP server this credential authenticates against.

  - `Type type`

  - `?\Datetime expiresAt`

    A timestamp in RFC 3339 format

  - `?ManagedAgentsMCPOAuthRefreshParams refresh`

    OAuth refresh token parameters for creating a credential with refresh support.

### Beta Managed Agents MCP OAuth Refresh Params

- `ManagedAgentsMCPOAuthRefreshParams`

  - `string clientID`

    OAuth client ID.

  - `string refreshToken`

    OAuth refresh token.

  - `string tokenEndpoint`

    Token endpoint URL used to refresh the access token.

  - `TokenEndpointAuth tokenEndpointAuth`

    Token endpoint requires no client authentication.

  - `?string resource`

    OAuth resource indicator.

  - `?string scope`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Response

- `ManagedAgentsMCPOAuthRefreshResponse`

  - `string clientID`

    OAuth client ID.

  - `string tokenEndpoint`

    Token endpoint URL used to refresh the access token.

  - `TokenEndpointAuth tokenEndpointAuth`

    Token endpoint requires no client authentication.

  - `?string resource`

    OAuth resource indicator.

  - `?string scope`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Update Params

- `ManagedAgentsMCPOAuthRefreshUpdateParams`

  - `?string refreshToken`

    Updated OAuth refresh token.

  - `?string scope`

    Updated OAuth scope for the refresh request.

  - `?TokenEndpointAuth tokenEndpointAuth`

    Updated HTTP Basic authentication parameters for the token endpoint.

### Beta Managed Agents MCP OAuth Update Params

- `ManagedAgentsMCPOAuthUpdateParams`

  - `Type type`

  - `?string accessToken`

    Updated OAuth access token.

  - `?\Datetime expiresAt`

    A timestamp in RFC 3339 format

  - `?ManagedAgentsMCPOAuthRefreshUpdateParams refresh`

    Parameters for updating OAuth refresh token configuration.

### Beta Managed Agents MCP Probe

- `ManagedAgentsMCPProbe`

  - `?ManagedAgentsRefreshHTTPResponse httpResponse`

    An HTTP response captured during a credential validation probe.

  - `string method`

    The MCP method that failed (for example `initialize` or `tools/list`).

### Beta Managed Agents Refresh HTTP Response

- `ManagedAgentsRefreshHTTPResponse`

  - `string body`

    Response body. May be truncated and has sensitive values scrubbed.

  - `bool bodyTruncated`

    Whether `body` was truncated.

  - `string contentType`

    Value of the `Content-Type` response header.

  - `int statusCode`

    HTTP status code.

### Beta Managed Agents Refresh Object

- `ManagedAgentsRefreshObject`

  - `?ManagedAgentsRefreshHTTPResponse httpResponse`

    An HTTP response captured during a credential validation probe.

  - `Status status`

    Outcome of a refresh-token exchange attempted during credential validation.

### Beta Managed Agents Static Bearer Auth Response

- `ManagedAgentsStaticBearerAuthResponse`

  - `string mcpServerURL`

    URL of the MCP server this credential authenticates against.

  - `Type type`

### Beta Managed Agents Static Bearer Create Params

- `ManagedAgentsStaticBearerCreateParams`

  - `string token`

    Static bearer token value.

  - `string mcpServerURL`

    URL of the MCP server this credential authenticates against.

  - `Type type`

### Beta Managed Agents Static Bearer Update Params

- `ManagedAgentsStaticBearerUpdateParams`

  - `Type type`

  - `?string token`

    Updated static bearer token value.

### Beta Managed Agents Token Endpoint Auth Basic Param

- `ManagedAgentsTokenEndpointAuthBasicParam`

  - `string clientSecret`

    OAuth client secret.

  - `Type type`

### Beta Managed Agents Token Endpoint Auth Basic Response

- `ManagedAgentsTokenEndpointAuthBasicResponse`

  - `Type type`

### Beta Managed Agents Token Endpoint Auth Basic Update Param

- `ManagedAgentsTokenEndpointAuthBasicUpdateParam`

  - `Type type`

  - `?string clientSecret`

    Updated OAuth client secret.

### Beta Managed Agents Token Endpoint Auth None Param

- `ManagedAgentsTokenEndpointAuthNoneParam`

  - `Type type`

### Beta Managed Agents Token Endpoint Auth None Response

- `ManagedAgentsTokenEndpointAuthNoneResponse`

  - `Type type`

### Beta Managed Agents Token Endpoint Auth Post Param

- `ManagedAgentsTokenEndpointAuthPostParam`

  - `string clientSecret`

    OAuth client secret.

  - `Type type`

### Beta Managed Agents Token Endpoint Auth Post Response

- `ManagedAgentsTokenEndpointAuthPostResponse`

  - `Type type`

### Beta Managed Agents Token Endpoint Auth Post Update Param

- `ManagedAgentsTokenEndpointAuthPostUpdateParam`

  - `Type type`

  - `?string clientSecret`

    Updated OAuth client secret.

### Beta Managed Agents Unrestricted Credential Networking Params

- `ManagedAgentsUnrestrictedCredentialNetworkingParams`

  - `Type type`

### Beta Managed Agents Unrestricted Credential Networking Response

- `ManagedAgentsUnrestrictedCredentialNetworkingResponse`

  - `Type type`
