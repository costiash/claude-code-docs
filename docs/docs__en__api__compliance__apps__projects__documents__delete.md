## Delete

**delete** `/v1/compliance/apps/projects/documents/{document_id}`

Delete a project document for compliance purposes.

Hard-deletes the project document permanently.

Returns:
ComplianceProjectDocumentDeleteResponse confirming the deletion

### Path Parameters

- `document_id: string`

  The document ID (tagged ID, e.g., claude_proj_doc_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  The ID of the project document that was deleted

- `type: "claude_project_document_deleted"`

  Constant string confirming deletion.

  - `"claude_project_document_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```
