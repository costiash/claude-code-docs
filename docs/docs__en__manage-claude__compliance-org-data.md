# List organizations, users, roles, and groups

Enumerate organizations under your parent organization, their users, roles, and groups through the Compliance API.

---

<Note>
  The Compliance API is available only on the Claude Enterprise plan and must be enabled before use. See [Get access to the Compliance API](/docs/en/manage-claude/compliance-api-access).
</Note>

<Check>
  **Required scope:** `read:compliance_org_data` on the Compliance Access Key. The user and group-member endpoints require `read:compliance_user_data` instead.

  Compliance Access Keys (`sk-ant-api01-...`) created in claude.ai are the only key type accepted; see [Get access to the Compliance API](/docs/en/manage-claude/compliance-api-access) to provision one. Calls authenticated with an Admin API key (`sk-ant-admin01-...`) return [403 Forbidden](/docs/en/manage-claude/compliance-errors#403-forbidden).
</Check>

The endpoints on this page expose the directory side of a Claude Enterprise organization: its linked organizations, the users in each one, the roles defined on each, and its role-based access control (RBAC) or SCIM (System for Cross-domain Identity Management)-provisioned groups and their members. Use them to seed eDiscovery user lists, build reporting dashboards, and reconcile group membership against an external system of record. Compliance Access Keys are bound to a parent organization and return data from every linked organization underneath, so a single key reaches the entire tree.

## List organizations

The [List organizations](/docs/en/api/compliance/organizations/list) endpoint returns every organization under the parent the key is bound to.

The following call lists every organization under your parent. The response is a single `data` array of organization records sorted by `created_at` ascending. The endpoint returns up to 1,000 organizations in one call; if your tree exceeds that, it returns a [500 error](/docs/en/manage-claude/compliance-errors#500-internal-server-error).

<CodeGroup>
```bash cURL nocheck
curl --fail-with-body -sS \
  "https://api.anthropic.com/v1/compliance/organizations" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY"
```
</CodeGroup>

```json Response
{
  "data": [
    {
      "uuid": "91012d09-e48b-438e-a489-1bebfd8fa6f9",
      "name": "Acme Engineering",
      "created_at": "2025-06-01T10:00:00Z"
    },
    {
      "uuid": "5a1b2c3d-4e5f-6789-abcd-ef0123456789",
      "name": "Acme Legal",
      "created_at": "2025-07-15T14:30:00Z"
    }
  ]
}
```

The `uuid` field is the canonical identifier for downstream lookups. The following table maps it to the other organization identifiers across the Compliance API:

| Field                | Where                                                                                                                                                                                                  | Relationship to `uuid`                       |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- |
| `{org_uuid}`         | Path parameter on per-organization endpoints on this page                                                                                                                                              | Same value                                   |
| `organization_uuid`  | Activity Feed record                                                                                                                                                                                   | Same value; join on these two fields directly |
| `organization_id`    | Activity Feed record                                                                                                                                                                                   | Same organization, `org_`-prefixed           |
| `organization_ids[]` | Filter on [Query the Activity Feed](/docs/en/manage-claude/compliance-activity-feed) and [Retrieve chats and messages](/docs/en/manage-claude/compliance-content-data#retrieve-chats-and-messages) | Accepts `uuid` or the `org_`-prefixed form   |

Most other Anthropic APIs use the `org_`-prefixed form.

If your tree exceeds the 1,000-organization cap, contact Anthropic support. There is currently no activity type for an organization being created or joining the tree, so relist periodically to detect newly linked organizations. To detect deleted organizations, watch the `org_deletion_requested` and `org_deleted_via_bulk` activity types; see [Query the Activity Feed](/docs/en/manage-claude/compliance-activity-feed).

## List organization users

The [List organization users](/docs/en/api/compliance/organizations/users/list) endpoint returns a paginated list of user records for one organization.

This endpoint requires `read:compliance_user_data`, not `read:compliance_org_data`. Create the Compliance Access Key with both scopes when you intend to use it for directory enumeration; otherwise the call returns [403 Forbidden](/docs/en/manage-claude/compliance-errors#403-forbidden).

See [List organization users](/docs/en/api/compliance/organizations/users/list) in the API reference for the `limit` and `page` query parameter defaults and ranges.

Results are sorted by account creation date ascending. Unlike the Activity Feed's `before_id`/`after_id` cursors (see [Paginate results](/docs/en/manage-claude/compliance-activity-feed#paginate-results)), the directory endpoints paginate with a `next_page` token: when `has_more` is `true`, pass `next_page` back unchanged as the `page` query parameter on the next request.

<CodeGroup>
```bash cURL nocheck
org_uuid="91012d09-e48b-438e-a489-1bebfd8fa6f9"

curl --fail-with-body -sS -G \
  "https://api.anthropic.com/v1/compliance/organizations/$org_uuid/users" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY" \
  --data-urlencode "limit=500"
```
</CodeGroup>

```json Response
{
  "data": [
    {
      "id": "user_01XyDMpzjS89pFZXqSFUBDr6",
      "full_name": "Priya Sharma",
      "email": "priya@example.com",
      "created_at": "2025-06-01T10:00:00Z"
    }
  ],
  "has_more": true,
  "next_page": "page_8aW5kZXgicG9zaXRpb25fdG9rZW5fOTE0"
}
```

The user IDs returned here are the same `user_...` identifiers accepted by the [Query the Activity Feed](/docs/en/manage-claude/compliance-activity-feed) `actor_ids[]` filter and the [Retrieve chats and messages](/docs/en/manage-claude/compliance-content-data#retrieve-chats-and-messages) `user_ids[]` filter. A typical eDiscovery flow lists users for one or more organizations, filters against your own external records, and feeds the resulting IDs into chat and project queries.

A user only appears here while they are an active member of the organization. Removed users are dropped from the list immediately. Their historical activity remains queryable through the Activity Feed for the full retention window, indexed by the same `user_...` ID.

## List roles

The [List Compliance Roles](/docs/en/api/compliance/organizations/roles/list) endpoint returns a paginated list of role records defined on one organization, and [Get Compliance Role](/docs/en/api/compliance/organizations/roles/retrieve) returns one role by ID.

Both role endpoints require `read:compliance_org_data`. The list endpoint accepts the same `limit` and `page` parameters as [List organization users](#list-organization-users).

<CodeGroup>
```bash cURL nocheck
org_uuid="91012d09-e48b-438e-a489-1bebfd8fa6f9"

curl --fail-with-body -sS \
  "https://api.anthropic.com/v1/compliance/organizations/${org_uuid}/roles" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY"
```
</CodeGroup>

```json Response
{
  "data": [
    {
      "id": "rbac_role_01N2pQrS8tUvWxYz5AbCdEfGh",
      "name": "Compliance Reviewer",
      "description": "Read-only access to chat and project content for legal review.",
      "created_at": "2025-06-01T10:00:00Z",
      "updated_at": "2025-06-15T14:30:00Z"
    }
  ],
  "has_more": false,
  "next_page": null
}
```

See the [List Compliance Roles](/docs/en/api/compliance/organizations/roles/list) response schema for the full role record shape. To list the permissions currently granted to a role, use [List Compliance Role Permissions](/docs/en/api/compliance/organizations/roles/permissions/list). To audit historical role assignments and permission changes, query the RBAC activity types (for example, `rbac_role_assigned` and `rbac_role_permission_added`) through the Activity Feed; see [Filter activities](/docs/en/manage-claude/compliance-activity-feed#filter-activities).

## List groups and members

The [List Compliance Groups](/docs/en/api/compliance/groups/list) endpoint returns a paginated list of RBAC and SCIM-provisioned groups, and [Get Compliance Group](/docs/en/api/compliance/groups/retrieve) returns one group by ID. The [List Compliance Group Members](/docs/en/api/compliance/groups/members/list) endpoint returns the members of one group.

The group list and retrieval endpoints require `read:compliance_org_data`. The members endpoint requires `read:compliance_user_data`. Create the key with both scopes to walk groups end to end. Both list endpoints accept the same `limit` and `page` parameters as [List organization users](#list-organization-users).

See the [List Compliance Groups](/docs/en/api/compliance/groups/list) response schema for the full group record shape. The `roles` array lists role IDs assigned to the group, matching IDs from [List roles](#list-roles). `source_type` is the discriminator between groups created manually through claude.ai (`direct`) and groups synced from an external identity provider through SCIM (`scim`).

List groups, then for each group list its members:

<CodeGroup>
```bash cURL nocheck
curl --fail-with-body -sS -G \
  "https://api.anthropic.com/v1/compliance/groups" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY"
```
</CodeGroup>

```json Response
{
  "data": [
    {
      "id": "rbac_group_01P9qRsTuVwXyZa2BcDeFgHjK",
      "name": "Engineering",
      "description": "Engineering team members",
      "source_type": "scim",
      "roles": ["rbac_role_01N2pQrS8tUvWxYz5AbCdEfGh"],
      "created_at": "2025-06-01T10:00:00Z",
      "updated_at": "2025-06-15T14:30:00Z"
    }
  ],
  "has_more": false,
  "next_page": null
}
```

For each group ID, list its members:

<CodeGroup>
```bash cURL nocheck
group_id="rbac_group_01P9qRsTuVwXyZa2BcDeFgHjK"

curl --fail-with-body -sS -G \
  "https://api.anthropic.com/v1/compliance/groups/$group_id/members" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY"
```
</CodeGroup>

```json Response
{
  "data": [
    {
      "user_id": "user_01XyDMpzjS89pFZXqSFUBDr6",
      "email": "priya@example.com",
      "created_at": "2025-06-01T10:00:00Z",
      "updated_at": "2025-06-15T14:30:00Z"
    }
  ],
  "has_more": false,
  "next_page": null
}
```

See the [List Compliance Group Members](/docs/en/api/compliance/groups/members/list) response schema for the full member record shape. The `user_id` field is the same `user_...` identifier the Activity Feed and chat list accept. To get a member's full name, look it up through the organization users list.

## Next steps

<CardGroup cols={2}>
  <Card title="Compliance organizations API reference" href="/docs/en/api/compliance/organizations">
    The full request and response schema for every organization, user, role, and group endpoint.
  </Card>
  <Card title="Handle Compliance API errors" href="/docs/en/manage-claude/compliance-errors">
    Verbatim error payloads and the fix for each.
  </Card>
</CardGroup>