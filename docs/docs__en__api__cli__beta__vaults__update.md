## Update

`$ ant beta:vaults update`

**post** `/v1/vaults/{vault_id}`

Update Vault

### Parameters

- `--vault-id: string`

  Path param: Path parameter vault_id

- `--display-name: optional string`

  Body param: Updated human-readable name for the vault. 1-255 characters.

- `--metadata: optional map[string]`

  Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

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
ant beta:vaults update \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv
```
