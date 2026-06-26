## Get project details

**get** `/v1/compliance/apps/projects/{project_id}`

Get detailed information for a specific project.

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

- `deleted_at: string`

  Timestamp when the project was deleted by an end user, or null otherwise

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

- `organization_uuid: string`

  Organization UUID this project belongs to

- `updated_at: string`

  Project last update timestamp

- `user: object { id, email_address }`

  The user who created a project or project document.

  Fields that reference this type are null when the creator's account has
  been deleted or the creator is no longer a member of any organization
  under the parent organization.

  - `id: string`

    User identifier (tagged ID)

  - `email_address: string`

    User's email address

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "id": "claude_proj_01Nm7PqRsTuVwXyZaBcDeFgH",
  "attachments_count": 3,
  "chats_count": 14,
  "created_at": "2025-03-12T18:22:41.123456Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "description": "Planning and research for the Q3 launch",
  "instructions": "Focus on concise, actionable answers.",
  "is_private": true,
  "name": "Q3 Product Launch",
  "organization_id": "org_015eofRkKpogX7uDKUyvBTph",
  "organization_uuid": "a1b2c3d4-e5f6-4789-a012-3456789abcde",
  "updated_at": "2025-03-14T09:05:17.456789Z",
  "user": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "email_address": "jane.doe@example.com"
  }
}
```
