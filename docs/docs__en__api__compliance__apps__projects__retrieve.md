## Retrieve

**get** `/v1/compliance/apps/projects/{project_id}`

Get detailed information for a specific project.

Returns:
Detailed project information including description, instructions, and counts

### Path Parameters

- `project_id: string`

  The project ID (tagged ID, e.g., claude_proj_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  Project identifier (tagged ID)

- `attachments_count: number`

  Number of attachments contained within this project

- `chats_count: number`

  Number of chats contained within this project

- `created_at: string`

  Project creation timestamp

- `description: string`

  Project description

- `instructions: string`

  Project's custom instructions / prompt

- `is_private: boolean`

  If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

- `name: string`

  Project name

- `organization_id: string`

  Organization identifier (tagged ID)

- `updated_at: string`

  Project last update timestamp

- `user: object { id, email_address }`

  User information for project creator.

  - `id: string`

    User identifier (tagged ID)

  - `email_address: string`

    User's email address

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```
