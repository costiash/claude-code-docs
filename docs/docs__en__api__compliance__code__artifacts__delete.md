## Delete Code Artifact

**delete** `/v1/compliance/code/artifacts/{artifact_id}`

Permanently deletes a Code Artifact and all its versions. This is a
destructive operation that cannot be undone. A 200 response means the
deletion is initiated and the Artifact is claimed; content removal
completes asynchronously.

Returns 404 for Artifacts that don't exist or belong to another parent
organization. Returns 404 on a repeated delete of an already-deleted
Artifact.

### Path Parameters

- `artifact_id: string`

  The Artifact ID (tagged ID, e.g., cart_abc123)

### Query Parameters

- `organization_uuid: optional string`

  The Artifact's owning organization UUID, from the list response. Strongly recommended — without it the route scans across child organizations and, for parents with many children, returns 400 rather than scanning further.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  The ID of the Artifact that was deleted

- `type: "code_artifact_deleted"`

  Constant string confirming deletion

  - `"code_artifact_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/compliance/code/artifacts/$ARTIFACT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "id": "cart_xyz789",
  "type": "code_artifact_deleted"
}
```
