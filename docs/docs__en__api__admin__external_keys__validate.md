## Validate External Key

**post** `/v1/organizations/external_keys/{external_key_id}/validate`

Validate an external key config against the customer's KMS.

Anthropic performs an encrypt/decrypt roundtrip against the configured
KMS key and waits up to 30 seconds for the result. The response status is
`success` if the roundtrip succeeded, or `failure` with an error
message if it failed or timed out.

### Path Parameters

- `external_key_id: string`

  ID of the External Key to validate.

### Returns

- `error: string`

  Error message when status is `failure`. Null otherwise.

- `status: "success" or "failure"`

  `success` — encrypt/decrypt roundtrip succeeded. `failure` — the roundtrip failed or timed out; see `error`.

  - `"success"`

  - `"failure"`

- `type: "external_key_validation"`

  - `"external_key_validation"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID/validate \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

#### Response

```json
{
  "error": null,
  "status": "success",
  "type": "external_key_validation"
}
```
