## Delete

`$ ant beta:vaults delete`

**delete** `/v1/vaults/{vault_id}`

Delete Vault

### Parameters

- `--vault-id: string`

  Path parameter vault_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deleted_vault: object { id, type }`

  Confirmation of a deleted vault.

  - `id: string`

    Unique identifier of the deleted vault.

  - `type: "vault_deleted"`

    - `"vault_deleted"`

### Example

```cli
ant beta:vaults delete \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv
```
