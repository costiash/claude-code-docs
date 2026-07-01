## Update External Key

**post** `/v1/organizations/external_keys/{external_key_id}`

Partially update an external key config. Omitted fields are left unchanged.

`display_name` is always editable. `geo` and `provider_config` cannot
be changed once any workspace references this config, because previously
encrypted data requires the original key identity to decrypt.

### Path Parameters

- `external_key_id: string`

  ID of the External Key to update.

### Body Parameters

- `display_name: optional string`

  Human-friendly display name.

- `geo: optional "us"`

  Data residency geo. Only `us` is supported.

  - `"us"`

- `provider_config: optional object { kms_arn, type, region, role_arn }  or object { key_name, type }  or object { key_name, tenant_id, type, 2 more }`

  KMS provider identity and auth coordinates.

  - `Aws object { kms_arn, type, region, role_arn }`

    - `kms_arn: string`

      Full ARN of the AWS KMS key.

    - `type: "aws"`

      - `"aws"`

    - `region: optional string`

      AWS region. Derived from kms_arn if omitted.

    - `role_arn: optional string`

      IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

  - `Gcp object { key_name, type }`

    - `key_name: string`

      Full resource name of the Cloud KMS key.

    - `type: "gcp"`

      - `"gcp"`

  - `Azure object { key_name, tenant_id, type, 2 more }`

    - `key_name: string`

      Name of the key within the vault.

    - `tenant_id: string`

      Azure AD tenant ID.

    - `type: "azure"`

      - `"azure"`

    - `vault_uri: string`

      Key Vault URI.

    - `client_id: optional string`

      Azure AD application (client) ID. Omit to use Anthropic's multi-tenant app. Provide only if using a single-tenant app registration in the customer's directory.

### Returns

- `id: string`

  Tagged ID of the external key config.

- `created_at: string`

- `display_name: string`

  Human-friendly display name. Null if none was set.

- `geo: string`

  Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

- `provider_config: object { kms_arn, type, region, role_arn }  or object { key_name, type }  or object { key_name, tenant_id, type, 2 more }`

  KMS provider identity and auth coordinates.

  - `Aws object { kms_arn, type, region, role_arn }`

    - `kms_arn: string`

      Full ARN of the AWS KMS key.

    - `type: "aws"`

      - `"aws"`

    - `region: optional string`

      AWS region. Derived from kms_arn if omitted.

    - `role_arn: optional string`

      IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

  - `Gcp object { key_name, type }`

    - `key_name: string`

      Full resource name of the Cloud KMS key.

    - `type: "gcp"`

      - `"gcp"`

  - `Azure object { key_name, tenant_id, type, 2 more }`

    - `key_name: string`

      Name of the key within the vault.

    - `tenant_id: string`

      Azure AD tenant ID.

    - `type: "azure"`

      - `"azure"`

    - `vault_uri: string`

      Key Vault URI.

    - `client_id: optional string`

      Azure AD application (client) ID. Omit to use Anthropic's multi-tenant app. Provide only if using a single-tenant app registration in the customer's directory.

- `type: "external_key"`

  - `"external_key"`

- `updated_at: string`

### Example

```http
curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{}'
```

#### Response

```json
{
  "id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "prod-us-key",
  "geo": "us",
  "provider_config": {
    "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
    "type": "aws",
    "region": "us-east-1",
    "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek"
  },
  "type": "external_key",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```
