## Create External Key

**post** `/v1/organizations/external_keys`

Create an external key config owned by the caller's organization.

### Body Parameters

- `display_name: string`

  Human-friendly display name.

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

- `geo: optional "us"`

  Data residency geo. Only `us` is supported.

  - `"us"`

### Returns

- `id: string`

  Tagged ID of the external key config.

- `created_at: string`

- `display_name: string`

  Human-friendly display name.

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
curl https://api.anthropic.com/v1/organizations/external_keys \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "display_name": "x",
          "provider_config": {
            "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
            "type": "aws"
          }
        }'
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
