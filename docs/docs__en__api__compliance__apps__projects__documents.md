# Documents

## Retrieve

**get** `/v1/compliance/apps/projects/documents/{document_id}`

Get detailed information for a specific project document.

Returns:
Project document information including content and metadata

### Path Parameters

- `document_id: string`

  The document ID (tagged ID, e.g., claude_proj_doc_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  Project document identifier (tagged ID)

- `content: string`

  Document text content

- `created_at: string`

  Document creation timestamp

- `filename: string`

  Document filename

- `user: object { id, email_address }`

  User information for project creator.

  - `id: string`

    User identifier (tagged ID)

  - `email_address: string`

    User's email address

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

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

## Domain Types

### Document Retrieve Response

- `DocumentRetrieveResponse = object { id, content, created_at, 2 more }`

  Project document information for compliance responses.

  - `id: string`

    Project document identifier (tagged ID)

  - `content: string`

    Document text content

  - `created_at: string`

    Document creation timestamp

  - `filename: string`

    Document filename

  - `user: object { id, email_address }`

    User information for project creator.

    - `id: string`

      User identifier (tagged ID)

    - `email_address: string`

      User's email address

### Document Delete Response

- `DocumentDeleteResponse = object { id, type }`

  Response for deleting a project document.

  - `id: string`

    The ID of the project document that was deleted

  - `type: "claude_project_document_deleted"`

    Constant string confirming deletion.

    - `"claude_project_document_deleted"`
