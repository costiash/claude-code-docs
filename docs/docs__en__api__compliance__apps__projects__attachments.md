## Attachments

**get** `/v1/compliance/apps/projects/{project_id}/attachments`

List files and documents attached to a project.

List files and project documents attached to the project referenced by project_id.
This includes the IDs of attached files, and attached project documents.

The raw binary content of attached files can be downloaded using the
GET /v1/compliance/apps/chats/files/{claude_file_id}/content endpoint.

The text content of attached project documents can be fetched using the
GET /v1/compliance/apps/projects/documents/{claude_proj_doc_id} endpoint.

Returns:
List of project attachments with pagination info

Raises:
NotFoundException: If project doesn't exist or project_id format is invalid

### Path Parameters

- `project_id: string`

  The project ID (tagged ID, e.g., claude_proj_abc123)

### Query Parameters

- `limit: optional number`

  Maximum results (default: 20, max: 100)

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { id, created_at, filename, 2 more }  or object { id, created_at, filename, 2 more }`

  List of attachments sorted chronologically by created_at, tie break by id

  - `ComplianceProjectFileReference = object { id, created_at, filename, 2 more }`

    File attachment reference for compliance responses.

    - `id: string`

      File identifier (e.g., 'claude_file_abcd')

    - `created_at: string`

      Creation timestamp (RFC 3339 format)

    - `filename: string`

      Display name of the file (e.g., 'document.pdf')

    - `mime_type: string`

      MIME type of the file when it was uploaded (e.g., 'application/pdf')

    - `type: "project_file"`

      Discriminator marking this as a binary file

      - `"project_file"`

  - `ComplianceProjectDocReference = object { id, created_at, filename, 2 more }`

    Project document attachment reference for compliance responses.

    - `id: string`

      Project document identifier (e.g., 'claude_proj_doc_abcd')

    - `created_at: string`

      Creation timestamp (RFC 3339 format)

    - `filename: string`

      Display name of the document (e.g., 'document.txt')

    - `mime_type: "text/plain"`

      MIME type of the project document, always set to plain text

      - `"text/plain"`

    - `type: "project_doc"`

      Discriminator marking this as a plain text document

      - `"project_doc"`

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string`

  To get the next page, use the 'next_page' from the current response as the 'page' in your next request

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID/attachments \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```
