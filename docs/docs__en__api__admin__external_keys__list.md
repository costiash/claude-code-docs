## List External Keys

**get** `/v1/organizations/external_keys`

List external key configs in the caller's organization.

Results are ordered by creation time (newest first). Use the
`next_page` cursor from the response to fetch subsequent pages.

### Query Parameters

- `limit: optional number`

  Number of results per page.

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

### Returns

- `data: array of object { id, created_at, display_name, 4 more }`

  - `id: string`

    Tagged ID of the external key config.

  - `created_at: string`

  - `display_name: string`

    Human-friendly display name.

  - `geo: string`

    Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

  - `provider_config: object { kms_arn, role_arn, type, region }  or object { key_name, type }  or object { key_name, tenant_id, type, 2 more }`

    KMS provider identity and auth coordinates.

    - `Aws object { kms_arn, role_arn, type, region }`

      - `kms_arn: string`

        Full ARN of the AWS KMS key.

      - `role_arn: string`

        IAM role ARN that Anthropic assumes to access the KMS key.

      - `type: "aws"`

        - `"aws"`

      - `region: optional string`

        AWS region. Derived from kms_arn if omitted.

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

- `next_page: string`

  Opaque cursor for the next page, or null if no more results. Pass as `?page=` to fetch the next page.

### Example

```http
curl https://api.anthropic.com/v1/organizations/external_keys \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_name": "prod-us-key",
      "geo": "us",
      "provider_config": {
        "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
        "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek",
        "type": "aws",
        "region": "us-east-1"
      },
      "type": "external_key",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "next_page": "next_page"
}
```
