## List project collaborators

**get** `/v1/compliance/apps/projects/{project_id}/collaborators`

List the users, groups, and organization-wide grants on a project.

Each entry represents one active role assignment on the project. Principals
are returned as a discriminated union on `type` — an individual user, an
RBAC group, the whole organization, or all holders of an organization-level
role.

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

- `data: array of object { granted_at, role, type, user_id }  or object { granted_at, group_id, role, type }  or object { granted_at, organization_uuid, role, type }  or object { granted_at, organization_role, role, type }`

  List of collaborators sorted chronologically by granted_at, tie break by the underlying role-assignment UUID

  - `ComplianceProjectUserCollaborator object { granted_at, role, type, user_id }`

    An individual user granted a role on a project.

    - `granted_at: string`

      When this collaborator was granted access (RFC 3339 format)

    - `role: "admin" or "editor" or "owner" or "viewer"`

      Role granted on the project

      - `"admin"`

      - `"editor"`

      - `"owner"`

      - `"viewer"`

    - `type: "user"`

      Discriminator marking this as an individual user collaborator

      - `"user"`

    - `user_id: string`

      Identifier of the user granted access (tagged ID), or null if their account has since been deleted

  - `ComplianceProjectGroupCollaborator object { granted_at, group_id, role, type }`

    An RBAC group granted a role on a project.

    - `granted_at: string`

      When this collaborator was granted access (RFC 3339 format)

    - `group_id: string`

      Identifier of the group granted access (tagged ID)

    - `role: "admin" or "editor" or "owner" or "viewer"`

      Role granted on the project

      - `"admin"`

      - `"editor"`

      - `"owner"`

      - `"viewer"`

    - `type: "group"`

      Discriminator marking this as a group collaborator

      - `"group"`

  - `ComplianceProjectOrganizationCollaborator object { granted_at, organization_uuid, role, type }`

    An entire organization granted a role on a project.

    - `granted_at: string`

      When this collaborator was granted access (RFC 3339 format)

    - `organization_uuid: string`

      UUID of the organization granted access

    - `role: "admin" or "editor" or "owner" or "viewer"`

      Role granted on the project

      - `"admin"`

      - `"editor"`

      - `"owner"`

      - `"viewer"`

    - `type: "organization"`

      Discriminator marking this as an organization-wide grant

      - `"organization"`

  - `ComplianceProjectOrganizationRoleCollaborator object { granted_at, organization_role, role, type }`

    All holders of an organization-level role granted a role on a project.

    - `granted_at: string`

      When this collaborator was granted access (RFC 3339 format)

    - `organization_role: string`

      The organization-level role whose holders are granted access

    - `role: "admin" or "editor" or "owner" or "viewer"`

      Role granted on the project

      - `"admin"`

      - `"editor"`

      - `"owner"`

      - `"viewer"`

    - `type: "organization_role"`

      Discriminator marking this as a grant to all organization members holding a specific org-level role

      - `"organization_role"`

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string`

  To get the next page, use the 'next_page' from the current response as the 'page' in your next request

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID/collaborators \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "data": [
    {
      "granted_at": "2019-12-27T18:11:19.117Z",
      "role": "admin",
      "type": "user",
      "user_id": "user_id"
    }
  ],
  "has_more": true,
  "next_page": "next_page"
}
```
