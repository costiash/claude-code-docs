# External Keys

## Create External Key

**post** `/v1/organizations/external_keys`

Create an external key config owned by the caller's organization.

### Body Parameters

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

    Azure Key Vault provider configuration.

    - `key_name: string`

      Name of the key within the vault.

    - `tenant_id: string`

      Azure AD tenant ID.

    - `type: "azure"`

      - `"azure"`

    - `vault_uri: string`

      Key Vault data-plane URI — https://<vault-name>.vault.azure.net or https://<hsm-name>.managedhsm.azure.net.

    - `client_id: optional string`

      Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

- `display_name: optional string`

  Human-friendly display name.

- `geo: optional "us"`

  Data residency geo. Only `us` is supported.

  - `"us"`

### Returns

- `id: string`

  Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

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

      Key Vault data-plane URI — https://<vault-name>.vault.azure.net or https://<hsm-name>.managedhsm.azure.net.

    - `client_id: optional string`

      Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

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

    Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

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

        Key Vault data-plane URI — https://<vault-name>.vault.azure.net or https://<hsm-name>.managedhsm.azure.net.

      - `client_id: optional string`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

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
        "type": "aws",
        "region": "us-east-1",
        "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek"
      },
      "type": "external_key",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "next_page": "next_page"
}
```

## Get External Key

**get** `/v1/organizations/external_keys/{external_key_id}`

Retrieve a single external key config in the caller's organization by ID.

### Path Parameters

- `external_key_id: string`

  ID of the External Key.

### Returns

- `id: string`

  Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

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

      Key Vault data-plane URI — https://<vault-name>.vault.azure.net or https://<hsm-name>.managedhsm.azure.net.

    - `client_id: optional string`

      Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

- `type: "external_key"`

  - `"external_key"`

- `updated_at: string`

### Example

```http
curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
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

## Update External Key

**post** `/v1/organizations/external_keys/{external_key_id}`

Partially update an external key config. Omitted fields are left unchanged.

`display_name` is always editable. `geo` and `provider_config` cannot
be changed once any workspace references this config, because previously
encrypted data requires the original key identity to decrypt.

### Path Parameters

- `external_key_id: string`

  ID of the External Key.

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

    Azure Key Vault provider configuration.

    - `key_name: string`

      Name of the key within the vault.

    - `tenant_id: string`

      Azure AD tenant ID.

    - `type: "azure"`

      - `"azure"`

    - `vault_uri: string`

      Key Vault data-plane URI — https://<vault-name>.vault.azure.net or https://<hsm-name>.managedhsm.azure.net.

    - `client_id: optional string`

      Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

### Returns

- `id: string`

  Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

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

      Key Vault data-plane URI — https://<vault-name>.vault.azure.net or https://<hsm-name>.managedhsm.azure.net.

    - `client_id: optional string`

      Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

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

## Delete External Key

**delete** `/v1/organizations/external_keys/{external_key_id}`

Delete an external key config.

The request is rejected if any workspace still references this config.

### Path Parameters

- `external_key_id: string`

  ID of the External Key.

### Returns

- `id: string`

  ID of the deleted External Key.

- `type: "external_key_deleted"`

  - `"external_key_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "ekey_01AbCdEfGhIjKlMnOpQrStUv",
  "type": "external_key_deleted"
}
```

## Validate External Key

**post** `/v1/organizations/external_keys/{external_key_id}/validate`

Validate an external key config against the customer's KMS.

Anthropic performs an encrypt/decrypt roundtrip against the configured
KMS key and waits up to 30 seconds for the result. The response status is
`success` if the roundtrip succeeded, or `failure` with an error
message if it failed or timed out.

### Path Parameters

- `external_key_id: string`

  ID of the External Key.

### Returns

- `error: string`

  Error message when status is `failure`. Null otherwise.

- `status: "failure" or "success"`

  `success` — encrypt/decrypt roundtrip succeeded. `failure` — the roundtrip failed or timed out; see `error`.

  - `"failure"`

  - `"success"`

- `type: "external_key_validation"`

  - `"external_key_validation"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID/validate \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "error": null,
  "status": "success",
  "type": "external_key_validation"
}
```

## Domain Types

### External Key Create Response

- `ExternalKeyCreateResponse object { id, created_at, display_name, 4 more }`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `id: string`

    Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

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

        Key Vault data-plane URI — https://<vault-name>.vault.azure.net or https://<hsm-name>.managedhsm.azure.net.

      - `client_id: optional string`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `type: "external_key"`

    - `"external_key"`

  - `updated_at: string`

### External Key List Response

- `ExternalKeyListResponse object { id, created_at, display_name, 4 more }`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `id: string`

    Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

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

        Key Vault data-plane URI — https://<vault-name>.vault.azure.net or https://<hsm-name>.managedhsm.azure.net.

      - `client_id: optional string`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `type: "external_key"`

    - `"external_key"`

  - `updated_at: string`

### External Key Retrieve Response

- `ExternalKeyRetrieveResponse object { id, created_at, display_name, 4 more }`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `id: string`

    Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

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

        Key Vault data-plane URI — https://<vault-name>.vault.azure.net or https://<hsm-name>.managedhsm.azure.net.

      - `client_id: optional string`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `type: "external_key"`

    - `"external_key"`

  - `updated_at: string`

### External Key Update Response

- `ExternalKeyUpdateResponse object { id, created_at, display_name, 4 more }`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `id: string`

    Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

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

        Key Vault data-plane URI — https://<vault-name>.vault.azure.net or https://<hsm-name>.managedhsm.azure.net.

      - `client_id: optional string`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `type: "external_key"`

    - `"external_key"`

  - `updated_at: string`

### External Key Delete Response

- `ExternalKeyDeleteResponse object { id, type }`

  - `id: string`

    ID of the deleted External Key.

  - `type: "external_key_deleted"`

    - `"external_key_deleted"`

### External Key Validate Response

- `ExternalKeyValidateResponse object { error, status, type }`

  Result of a validation roundtrip against the customer's KMS.

  HTTP 200 for both outcomes — the operation completed; `status` says
  whether the key works.

  - `error: string`

    Error message when status is `failure`. Null otherwise.

  - `status: "failure" or "success"`

    `success` — encrypt/decrypt roundtrip succeeded. `failure` — the roundtrip failed or timed out; see `error`.

    - `"failure"`

    - `"success"`

  - `type: "external_key_validation"`

    - `"external_key_validation"`
