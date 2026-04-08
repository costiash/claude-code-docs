## Create

`$ ant beta:vaults create`

**post** `/v1/vaults`

Create Vault

### Parameters

- `--display-name: string`

  Body param: Human-readable name for the vault. 1-255 characters.

- `--metadata: optional map[string]`

  Body param: Arbitrary key-value metadata to attach to the vault.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_vault: object { id, archived_at, created_at, 4 more }`

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

```cli
ant beta:vaults create \
  --api-key my-anthropic-api-key \
  --display-name 'Example vault'
```
