# Vaults

## Create

`beta.vaults.create(VaultCreateParams**kwargs)  -> BetaManagedAgentsVault`

**post** `/v1/vaults`

Create Vault

### Parameters

- `display_name: str`

  Human-readable name for the vault. 1-255 characters.

- `metadata: Optional[Dict[str, str]]`

  Arbitrary key-value metadata to attach to the vault. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 20 more]`

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

### Returns

- `class BetaManagedAgentsVault: …`

  A vault that stores credentials for use by agents during sessions.

  - `id: str`

    Unique identifier for the vault.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `display_name: str`

    Human-readable name for the vault.

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata attached to the vault.

  - `type: Literal["vault"]`

    - `"vault"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_vault = client.beta.vaults.create(
    display_name="Example vault",
)
print(beta_managed_agents_vault.id)
```

## List

`beta.vaults.list(VaultListParams**kwargs)  -> SyncPageCursor[BetaManagedAgentsVault]`

**get** `/v1/vaults`

List Vaults

### Parameters

- `include_archived: Optional[bool]`

  Whether to include archived vaults in the results.

- `limit: Optional[int]`

  Maximum number of vaults to return per page. Defaults to 20, maximum 100.

- `page: Optional[str]`

  Opaque pagination token from a previous `list_vaults` response.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 20 more]`

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

### Returns

- `class BetaManagedAgentsVault: …`

  A vault that stores credentials for use by agents during sessions.

  - `id: str`

    Unique identifier for the vault.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `display_name: str`

    Human-readable name for the vault.

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata attached to the vault.

  - `type: Literal["vault"]`

    - `"vault"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.vaults.list()
page = page.data[0]
print(page.id)
```

## Retrieve

`beta.vaults.retrieve(strvault_id, VaultRetrieveParams**kwargs)  -> BetaManagedAgentsVault`

**get** `/v1/vaults/{vault_id}`

Get Vault

### Parameters

- `vault_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 20 more]`

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

### Returns

- `class BetaManagedAgentsVault: …`

  A vault that stores credentials for use by agents during sessions.

  - `id: str`

    Unique identifier for the vault.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `display_name: str`

    Human-readable name for the vault.

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata attached to the vault.

  - `type: Literal["vault"]`

    - `"vault"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_vault = client.beta.vaults.retrieve(
    vault_id="vlt_011CZkZDLs7fYzm1hXNPeRjv",
)
print(beta_managed_agents_vault.id)
```

## Update

`beta.vaults.update(strvault_id, VaultUpdateParams**kwargs)  -> BetaManagedAgentsVault`

**post** `/v1/vaults/{vault_id}`

Update Vault

### Parameters

- `vault_id: str`

- `display_name: Optional[str]`

  Updated human-readable name for the vault. 1-255 characters.

- `metadata: Optional[Dict[str, Optional[str]]]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 20 more]`

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

### Returns

- `class BetaManagedAgentsVault: …`

  A vault that stores credentials for use by agents during sessions.

  - `id: str`

    Unique identifier for the vault.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `display_name: str`

    Human-readable name for the vault.

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata attached to the vault.

  - `type: Literal["vault"]`

    - `"vault"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_vault = client.beta.vaults.update(
    vault_id="vlt_011CZkZDLs7fYzm1hXNPeRjv",
)
print(beta_managed_agents_vault.id)
```

## Delete

`beta.vaults.delete(strvault_id, VaultDeleteParams**kwargs)  -> BetaManagedAgentsDeletedVault`

**delete** `/v1/vaults/{vault_id}`

Delete Vault

### Parameters

- `vault_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 20 more]`

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

### Returns

- `class BetaManagedAgentsDeletedVault: …`

  Confirmation of a deleted vault.

  - `id: str`

    Unique identifier of the deleted vault.

  - `type: Literal["vault_deleted"]`

    - `"vault_deleted"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_deleted_vault = client.beta.vaults.delete(
    vault_id="vlt_011CZkZDLs7fYzm1hXNPeRjv",
)
print(beta_managed_agents_deleted_vault.id)
```

## Archive

`beta.vaults.archive(strvault_id, VaultArchiveParams**kwargs)  -> BetaManagedAgentsVault`

**post** `/v1/vaults/{vault_id}/archive`

Archive Vault

### Parameters

- `vault_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 20 more]`

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

### Returns

- `class BetaManagedAgentsVault: …`

  A vault that stores credentials for use by agents during sessions.

  - `id: str`

    Unique identifier for the vault.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `display_name: str`

    Human-readable name for the vault.

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata attached to the vault.

  - `type: Literal["vault"]`

    - `"vault"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_vault = client.beta.vaults.archive(
    vault_id="vlt_011CZkZDLs7fYzm1hXNPeRjv",
)
print(beta_managed_agents_vault.id)
```

## Domain Types

### Beta Managed Agents Deleted Vault

- `class BetaManagedAgentsDeletedVault: …`

  Confirmation of a deleted vault.

  - `id: str`

    Unique identifier of the deleted vault.

  - `type: Literal["vault_deleted"]`

    - `"vault_deleted"`

### Beta Managed Agents Vault

- `class BetaManagedAgentsVault: …`

  A vault that stores credentials for use by agents during sessions.

  - `id: str`

    Unique identifier for the vault.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `display_name: str`

    Human-readable name for the vault.

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata attached to the vault.

  - `type: Literal["vault"]`

    - `"vault"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

# Credentials

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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 20 more]`

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

## List

`beta.vaults.credentials.list(strvault_id, CredentialListParams**kwargs)  -> SyncPageCursor[BetaManagedAgentsCredential]`

**get** `/v1/vaults/{vault_id}/credentials`

List Credentials

### Parameters

- `vault_id: str`

- `include_archived: Optional[bool]`

  Whether to include archived credentials in the results.

- `limit: Optional[int]`

  Maximum number of credentials to return per page. Defaults to 20, maximum 100.

- `page: Optional[str]`

  Opaque pagination token from a previous `list_credentials` response.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 20 more]`

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
page = client.beta.vaults.credentials.list(
    vault_id="vlt_011CZkZDLs7fYzm1hXNPeRjv",
)
page = page.data[0]
print(page.id)
```

## Retrieve

`beta.vaults.credentials.retrieve(strcredential_id, CredentialRetrieveParams**kwargs)  -> BetaManagedAgentsCredential`

**get** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Get Credential

### Parameters

- `vault_id: str`

- `credential_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 20 more]`

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
beta_managed_agents_credential = client.beta.vaults.credentials.retrieve(
    credential_id="vcrd_011CZkZEMt8gZan2iYOQfSkw",
    vault_id="vlt_011CZkZDLs7fYzm1hXNPeRjv",
)
print(beta_managed_agents_credential.id)
```

## Update

`beta.vaults.credentials.update(strcredential_id, CredentialUpdateParams**kwargs)  -> BetaManagedAgentsCredential`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update Credential

### Parameters

- `vault_id: str`

- `credential_id: str`

- `auth: Optional[Auth]`

  Updated authentication details for a credential.

  - `class BetaManagedAgentsMCPOAuthUpdateParams: …`

    Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

    - `type: Literal["mcp_oauth"]`

      - `"mcp_oauth"`

    - `access_token: Optional[str]`

      Updated OAuth access token.

    - `expires_at: Optional[datetime]`

      A timestamp in RFC 3339 format

    - `refresh: Optional[BetaManagedAgentsMCPOAuthRefreshUpdateParams]`

      Parameters for updating OAuth refresh token configuration.

      - `refresh_token: Optional[str]`

        Updated OAuth refresh token.

      - `scope: Optional[str]`

        Updated OAuth scope for the refresh request.

      - `token_endpoint_auth: Optional[TokenEndpointAuth]`

        Updated HTTP Basic authentication parameters for the token endpoint.

        - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam: …`

          Updated HTTP Basic authentication parameters for the token endpoint.

          - `type: Literal["client_secret_basic"]`

            - `"client_secret_basic"`

          - `client_secret: Optional[str]`

            Updated OAuth client secret.

        - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam: …`

          Updated POST body authentication parameters for the token endpoint.

          - `type: Literal["client_secret_post"]`

            - `"client_secret_post"`

          - `client_secret: Optional[str]`

            Updated OAuth client secret.

  - `class BetaManagedAgentsStaticBearerUpdateParams: …`

    Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

    - `type: Literal["static_bearer"]`

      - `"static_bearer"`

    - `token: Optional[str]`

      Updated static bearer token value.

- `display_name: Optional[str]`

  Updated human-readable name for the credential. 1-255 characters.

- `metadata: Optional[Dict[str, Optional[str]]]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 20 more]`

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
beta_managed_agents_credential = client.beta.vaults.credentials.update(
    credential_id="vcrd_011CZkZEMt8gZan2iYOQfSkw",
    vault_id="vlt_011CZkZDLs7fYzm1hXNPeRjv",
)
print(beta_managed_agents_credential.id)
```

## Delete

`beta.vaults.credentials.delete(strcredential_id, CredentialDeleteParams**kwargs)  -> BetaManagedAgentsDeletedCredential`

**delete** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete Credential

### Parameters

- `vault_id: str`

- `credential_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 20 more]`

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

### Returns

- `class BetaManagedAgentsDeletedCredential: …`

  Confirmation of a deleted credential.

  - `id: str`

    Unique identifier of the deleted credential.

  - `type: Literal["vault_credential_deleted"]`

    - `"vault_credential_deleted"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_deleted_credential = client.beta.vaults.credentials.delete(
    credential_id="vcrd_011CZkZEMt8gZan2iYOQfSkw",
    vault_id="vlt_011CZkZDLs7fYzm1hXNPeRjv",
)
print(beta_managed_agents_deleted_credential.id)
```

## Archive

`beta.vaults.credentials.archive(strcredential_id, CredentialArchiveParams**kwargs)  -> BetaManagedAgentsCredential`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/archive`

Archive Credential

### Parameters

- `vault_id: str`

- `credential_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 20 more]`

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
beta_managed_agents_credential = client.beta.vaults.credentials.archive(
    credential_id="vcrd_011CZkZEMt8gZan2iYOQfSkw",
    vault_id="vlt_011CZkZDLs7fYzm1hXNPeRjv",
)
print(beta_managed_agents_credential.id)
```

## Domain Types

### Beta Managed Agents Credential

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

### Beta Managed Agents Deleted Credential

- `class BetaManagedAgentsDeletedCredential: …`

  Confirmation of a deleted credential.

  - `id: str`

    Unique identifier of the deleted credential.

  - `type: Literal["vault_credential_deleted"]`

    - `"vault_credential_deleted"`

### Beta Managed Agents MCP OAuth Auth Response

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

### Beta Managed Agents MCP OAuth Create Params

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

### Beta Managed Agents MCP OAuth Refresh Params

- `class BetaManagedAgentsMCPOAuthRefreshParams: …`

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

### Beta Managed Agents MCP OAuth Refresh Response

- `class BetaManagedAgentsMCPOAuthRefreshResponse: …`

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

### Beta Managed Agents MCP OAuth Refresh Update Params

- `class BetaManagedAgentsMCPOAuthRefreshUpdateParams: …`

  Parameters for updating OAuth refresh token configuration.

  - `refresh_token: Optional[str]`

    Updated OAuth refresh token.

  - `scope: Optional[str]`

    Updated OAuth scope for the refresh request.

  - `token_endpoint_auth: Optional[TokenEndpointAuth]`

    Updated HTTP Basic authentication parameters for the token endpoint.

    - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam: …`

      Updated HTTP Basic authentication parameters for the token endpoint.

      - `type: Literal["client_secret_basic"]`

        - `"client_secret_basic"`

      - `client_secret: Optional[str]`

        Updated OAuth client secret.

    - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam: …`

      Updated POST body authentication parameters for the token endpoint.

      - `type: Literal["client_secret_post"]`

        - `"client_secret_post"`

      - `client_secret: Optional[str]`

        Updated OAuth client secret.

### Beta Managed Agents MCP OAuth Update Params

- `class BetaManagedAgentsMCPOAuthUpdateParams: …`

  Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

  - `type: Literal["mcp_oauth"]`

    - `"mcp_oauth"`

  - `access_token: Optional[str]`

    Updated OAuth access token.

  - `expires_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `refresh: Optional[BetaManagedAgentsMCPOAuthRefreshUpdateParams]`

    Parameters for updating OAuth refresh token configuration.

    - `refresh_token: Optional[str]`

      Updated OAuth refresh token.

    - `scope: Optional[str]`

      Updated OAuth scope for the refresh request.

    - `token_endpoint_auth: Optional[TokenEndpointAuth]`

      Updated HTTP Basic authentication parameters for the token endpoint.

      - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam: …`

        Updated HTTP Basic authentication parameters for the token endpoint.

        - `type: Literal["client_secret_basic"]`

          - `"client_secret_basic"`

        - `client_secret: Optional[str]`

          Updated OAuth client secret.

      - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam: …`

        Updated POST body authentication parameters for the token endpoint.

        - `type: Literal["client_secret_post"]`

          - `"client_secret_post"`

        - `client_secret: Optional[str]`

          Updated OAuth client secret.

### Beta Managed Agents Static Bearer Auth Response

- `class BetaManagedAgentsStaticBearerAuthResponse: …`

  Static bearer token credential details for an MCP server.

  - `mcp_server_url: str`

    URL of the MCP server this credential authenticates against.

  - `type: Literal["static_bearer"]`

    - `"static_bearer"`

### Beta Managed Agents Static Bearer Create Params

- `class BetaManagedAgentsStaticBearerCreateParams: …`

  Parameters for creating a static bearer token credential.

  - `token: str`

    Static bearer token value.

  - `mcp_server_url: str`

    URL of the MCP server this credential authenticates against.

  - `type: Literal["static_bearer"]`

    - `"static_bearer"`

### Beta Managed Agents Static Bearer Update Params

- `class BetaManagedAgentsStaticBearerUpdateParams: …`

  Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

  - `type: Literal["static_bearer"]`

    - `"static_bearer"`

  - `token: Optional[str]`

    Updated static bearer token value.

### Beta Managed Agents Token Endpoint Auth Basic Param

- `class BetaManagedAgentsTokenEndpointAuthBasicParam: …`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `client_secret: str`

    OAuth client secret.

  - `type: Literal["client_secret_basic"]`

    - `"client_secret_basic"`

### Beta Managed Agents Token Endpoint Auth Basic Response

- `class BetaManagedAgentsTokenEndpointAuthBasicResponse: …`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `type: Literal["client_secret_basic"]`

    - `"client_secret_basic"`

### Beta Managed Agents Token Endpoint Auth Basic Update Param

- `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam: …`

  Updated HTTP Basic authentication parameters for the token endpoint.

  - `type: Literal["client_secret_basic"]`

    - `"client_secret_basic"`

  - `client_secret: Optional[str]`

    Updated OAuth client secret.

### Beta Managed Agents Token Endpoint Auth None Param

- `class BetaManagedAgentsTokenEndpointAuthNoneParam: …`

  Token endpoint requires no client authentication.

  - `type: Literal["none"]`

    - `"none"`

### Beta Managed Agents Token Endpoint Auth None Response

- `class BetaManagedAgentsTokenEndpointAuthNoneResponse: …`

  Token endpoint requires no client authentication.

  - `type: Literal["none"]`

    - `"none"`

### Beta Managed Agents Token Endpoint Auth Post Param

- `class BetaManagedAgentsTokenEndpointAuthPostParam: …`

  Token endpoint uses POST body authentication with client credentials.

  - `client_secret: str`

    OAuth client secret.

  - `type: Literal["client_secret_post"]`

    - `"client_secret_post"`

### Beta Managed Agents Token Endpoint Auth Post Response

- `class BetaManagedAgentsTokenEndpointAuthPostResponse: …`

  Token endpoint uses POST body authentication with client credentials.

  - `type: Literal["client_secret_post"]`

    - `"client_secret_post"`

### Beta Managed Agents Token Endpoint Auth Post Update Param

- `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam: …`

  Updated POST body authentication parameters for the token endpoint.

  - `type: Literal["client_secret_post"]`

    - `"client_secret_post"`

  - `client_secret: Optional[str]`

    Updated OAuth client secret.
