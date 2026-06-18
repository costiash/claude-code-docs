# Organizations

## List organizations

**get** `/v1/compliance/organizations`

List organizations under the parent organization.

Returns a list of organizations sorted by creation date in ascending order.
This endpoint does not support pagination and will return an error if the
response would exceed 1,000 organizations.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { created_at, name, uuid }`

  List of organizations sorted by creation date, ascending

  - `created_at: string`

    Organization creation time (RFC 3339 format)

  - `name: string`

    Organization name

  - `uuid: string`

    Unique identifier for the organization (UUID format)

### Example

```http
curl https://api.anthropic.com/v1/compliance/organizations \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "data": [
    {
      "created_at": "created_at",
      "name": "name",
      "uuid": "uuid"
    }
  ]
}
```

## Domain Types

### Organization List Response

- `OrganizationListResponse object { data }`

  List of organizations under a parent organization.

  - `data: array of object { created_at, name, uuid }`

    List of organizations sorted by creation date, ascending

    - `created_at: string`

      Organization creation time (RFC 3339 format)

    - `name: string`

      Organization name

    - `uuid: string`

      Unique identifier for the organization (UUID format)

# Users

## List organization users

**get** `/v1/compliance/organizations/{org_uuid}/users`

List current user members of an organization.

### Path Parameters

- `org_uuid: string`

  The organization UUID

### Query Parameters

- `limit: optional number`

  Maximum results (default: 500, max: 1000)

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { id, created_at, email, 2 more }`

  List of current organization members sorted by organization join date ascending

  - `id: string`

    User identifier (tagged ID)

  - `created_at: string`

    User account creation timestamp

  - `email: string`

    User's current email address

  - `full_name: string`

    User's current full name

  - `organization_role: "admin" or "billing" or "claude_code_user" or 6 more`

    User's built-in role within the organization. This is distinct from any custom RBAC roles that may also be assigned.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

    - `"user"`

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

### Example

```http
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/users \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "email": "email",
      "full_name": "full_name",
      "organization_role": "admin"
    }
  ],
  "has_more": true,
  "next_page": "next_page"
}
```

## Domain Types

### User List Response

- `UserListResponse object { id, created_at, email, 2 more }`

  User member information for compliance responses.

  - `id: string`

    User identifier (tagged ID)

  - `created_at: string`

    User account creation timestamp

  - `email: string`

    User's current email address

  - `full_name: string`

    User's current full name

  - `organization_role: "admin" or "billing" or "claude_code_user" or 6 more`

    User's built-in role within the organization. This is distinct from any custom RBAC roles that may also be assigned.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

    - `"user"`

# Roles

## List Compliance Roles

**get** `/v1/compliance/organizations/{org_uuid}/roles`

List Compliance Roles

### Path Parameters

- `org_uuid: string`

  The organization UUID

### Query Parameters

- `limit: optional number`

  Maximum results (default: 500, max: 1000)

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { id, created_at, description, 2 more }`

  List of roles

  - `id: string`

    Role identifier (tagged ID)

  - `created_at: string`

    Role creation timestamp (ISO 8601)

  - `description: string`

    Role description

  - `name: string`

    Role name

  - `updated_at: string`

    Role last-updated timestamp (ISO 8601)

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

### Example

```http
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "created_at": "created_at",
      "description": "description",
      "name": "name",
      "updated_at": "updated_at"
    }
  ],
  "has_more": true,
  "next_page": "next_page"
}
```

## Get Compliance Role

**get** `/v1/compliance/organizations/{org_uuid}/roles/{role_id}`

Get Compliance Role

### Path Parameters

- `org_uuid: string`

  The organization UUID

- `role_id: string`

  The role ID (tagged ID, e.g., rbac_role_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  Role identifier (tagged ID)

- `created_at: string`

  Role creation timestamp (ISO 8601)

- `description: string`

  Role description

- `name: string`

  Role name

- `updated_at: string`

  Role last-updated timestamp (ISO 8601)

### Example

```http
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles/$ROLE_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "id": "id",
  "created_at": "created_at",
  "description": "description",
  "name": "name",
  "updated_at": "updated_at"
}
```

## Domain Types

### Role List Response

- `RoleListResponse object { id, created_at, description, 2 more }`

  Role information for compliance responses.

  - `id: string`

    Role identifier (tagged ID)

  - `created_at: string`

    Role creation timestamp (ISO 8601)

  - `description: string`

    Role description

  - `name: string`

    Role name

  - `updated_at: string`

    Role last-updated timestamp (ISO 8601)

### Role Retrieve Response

- `RoleRetrieveResponse object { id, created_at, description, 2 more }`

  Role information for compliance responses.

  - `id: string`

    Role identifier (tagged ID)

  - `created_at: string`

    Role creation timestamp (ISO 8601)

  - `description: string`

    Role description

  - `name: string`

    Role name

  - `updated_at: string`

    Role last-updated timestamp (ISO 8601)

# Permissions

## List Compliance Role Permissions

**get** `/v1/compliance/organizations/{org_uuid}/roles/{role_id}/permissions`

List Compliance Role Permissions

### Path Parameters

- `org_uuid: string`

  The organization UUID

- `role_id: string`

  The role ID (tagged ID, e.g., rbac_role_abc123)

### Query Parameters

- `limit: optional number`

  Maximum results (default: 500, max: 1000)

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { action, resource_id, resource_type }`

  List of permissions

  - `action: string`

    Action permitted on the resource

  - `resource_id: string`

    Identifier of the resource the permission applies to

  - `resource_type: string`

    Type of resource the permission applies to

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

### Example

```http
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles/$ROLE_ID/permissions \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "data": [
    {
      "action": "action",
      "resource_id": "resource_id",
      "resource_type": "resource_type"
    }
  ],
  "has_more": true,
  "next_page": "next_page"
}
```

## Domain Types

### Permission List Response

- `PermissionListResponse object { action, resource_id, resource_type }`

  Permission granted by a role.

  - `action: string`

    Action permitted on the resource

  - `resource_id: string`

    Identifier of the resource the permission applies to

  - `resource_type: string`

    Type of resource the permission applies to

# Settings

## Get effective organization settings

**get** `/v1/compliance/organizations/{organization_id}/settings`

Retrieve the effective settings for an organization.

Returns the settings currently in force for the given organization — the
enforced state after all policies are applied, which may differ from what
is configured in the admin console. Settings an organization's
administrators cannot change (for example, ones controlled by Anthropic
policy or not available to the organization) are omitted from the list.

The organization must belong to the API key's organization hierarchy;
unknown organizations and organizations outside the hierarchy return 404.

### Path Parameters

- `organization_id: string`

  The organization's UUID

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `api_keys: array of object { id, created_at, created_by_id, 4 more }`

  Compliance API keys configured for the organization hierarchy, ordered by creation time ascending. Key secret values are never included.

  - `id: string`

    Unique identifier for the API key.

  - `created_at: string`

    When the key was created.

  - `created_by_id: string`

    Identifier of the user who created the key, or null when the key was created by automation or its creator's account no longer exists.

  - `is_active: boolean`

    Whether the key is currently active. A deactivated key is listed for audit visibility but cannot authenticate requests.

  - `name: string`

    The name given to the API key when it was created.

  - `scopes: array of string`

    The permission scopes granted to the key.

  - `type: optional "compliance_api_key"`

    - `"compliance_api_key"`

- `organization_id: string`

- `settings: array of object { name, value, type }  or object { name, value, type }  or object { name, value, type }  or 2 more`

  - `Boolean object { name, value, type }`

    A setting whose enforced value is a single true/false flag.

    - `name: "api_workbench_feedback_collection_enabled" or "claude_ai_feedback_collection_enabled" or "claude_code_trusted_devices_required" or 9 more`

      - `"api_workbench_feedback_collection_enabled"`

      - `"claude_ai_feedback_collection_enabled"`

      - `"claude_code_trusted_devices_required"`

      - `"code_execution_enabled"`

      - `"code_execution_network_egress_enabled"`

      - `"content_redaction_enabled"`

      - `"directory_sync_enabled"`

      - `"frontier_data_use_enabled"`

      - `"ip_allowlist_enabled"`

      - `"sso_claude_ai_enforced"`

      - `"sso_console_enforced"`

      - `"sso_enabled"`

    - `value: boolean`

    - `type: optional "boolean"`

      - `"boolean"`

  - `Integer object { name, value, type }`

    A setting whose enforced value is a whole number; null means no limit
    is in force.

    - `name: "account_session_duration_seconds"`

      - `"account_session_duration_seconds"`

    - `value: number`

    - `type: optional "integer"`

      - `"integer"`

  - `StringList object { name, value, type }`

    A setting whose enforced value is a list of strings.

    - `name: "allowed_invite_domains" or "ip_allowlist_ip_ranges"`

      - `"allowed_invite_domains"`

      - `"ip_allowlist_ip_ranges"`

    - `value: array of string`

    - `type: optional "string_list"`

      - `"string_list"`

  - `ProvisioningMode object { value, name, type }`

    How organization members are provisioned, resolved to the enforced mode.

    A configured mode is reported only while the mechanism that enforces it is
    active: just-in-time modes require single sign-on to be enabled, and SCIM
    modes require directory sync to be enabled. Otherwise `login_only` is
    reported, regardless of any stored configuration.

    - `value: "jit_advanced" or "jit_permissive" or "login_only" or 2 more`

      How organization members are provisioned under SSO.

      - `"jit_advanced"`

      - `"jit_permissive"`

      - `"login_only"`

      - `"scim_advanced"`

      - `"scim_permissive"`

    - `name: optional "sso_provisioning_mode"`

      - `"sso_provisioning_mode"`

    - `type: optional "provisioning_mode"`

      - `"provisioning_mode"`

  - `DataRetention object { value, name, type }`

    The data retention periods in force, keyed by the type of data they
    apply to.

    A key of `all` covers every data type and is exclusive: when present it
    is the only key. A missing key means no organization-level
    administrator-configured retention period is in force for that data type;
    Anthropic's service defaults may still apply.

    - `value: map[object { duration, timescale, type }  or object { type } ]`

      - `Fixed object { duration, timescale, type }`

        A fixed retention window measured from each item's last activity.

        - `duration: number`

        - `timescale: "day" or "month"`

          - `"day"`

          - `"month"`

        - `type: optional "fixed"`

          - `"fixed"`

      - `Indefinite object { type }`

        An indefinite retention period: data is kept with no time limit.

        - `type: optional "indefinite"`

          - `"indefinite"`

    - `name: optional "data_retention_periods"`

      - `"data_retention_periods"`

    - `type: optional "data_retention"`

      - `"data_retention"`

- `type: optional "effective_organization_settings"`

  - `"effective_organization_settings"`

### Example

```http
curl https://api.anthropic.com/v1/compliance/organizations/$ORGANIZATION_ID/settings \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "api_keys": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "created_by_id": "created_by_id",
      "is_active": true,
      "name": "name",
      "scopes": [
        "string"
      ],
      "type": "compliance_api_key"
    }
  ],
  "organization_id": "organization_id",
  "settings": [
    {
      "name": "api_workbench_feedback_collection_enabled",
      "value": true,
      "type": "boolean"
    }
  ],
  "type": "effective_organization_settings"
}
```

## Domain Types

### Setting Retrieve Response

- `SettingRetrieveResponse object { api_keys, organization_id, settings, type }`

  The resolved settings in force for one organization at read time.

  Settings appear at most once each, in a fixed relative order, and values
  reflect the enforced state. A setting the organization's administrators
  cannot change — for example, one controlled by Anthropic policy or not
  available to the organization — is omitted from the list.

  - `api_keys: array of object { id, created_at, created_by_id, 4 more }`

    Compliance API keys configured for the organization hierarchy, ordered by creation time ascending. Key secret values are never included.

    - `id: string`

      Unique identifier for the API key.

    - `created_at: string`

      When the key was created.

    - `created_by_id: string`

      Identifier of the user who created the key, or null when the key was created by automation or its creator's account no longer exists.

    - `is_active: boolean`

      Whether the key is currently active. A deactivated key is listed for audit visibility but cannot authenticate requests.

    - `name: string`

      The name given to the API key when it was created.

    - `scopes: array of string`

      The permission scopes granted to the key.

    - `type: optional "compliance_api_key"`

      - `"compliance_api_key"`

  - `organization_id: string`

  - `settings: array of object { name, value, type }  or object { name, value, type }  or object { name, value, type }  or 2 more`

    - `Boolean object { name, value, type }`

      A setting whose enforced value is a single true/false flag.

      - `name: "api_workbench_feedback_collection_enabled" or "claude_ai_feedback_collection_enabled" or "claude_code_trusted_devices_required" or 9 more`

        - `"api_workbench_feedback_collection_enabled"`

        - `"claude_ai_feedback_collection_enabled"`

        - `"claude_code_trusted_devices_required"`

        - `"code_execution_enabled"`

        - `"code_execution_network_egress_enabled"`

        - `"content_redaction_enabled"`

        - `"directory_sync_enabled"`

        - `"frontier_data_use_enabled"`

        - `"ip_allowlist_enabled"`

        - `"sso_claude_ai_enforced"`

        - `"sso_console_enforced"`

        - `"sso_enabled"`

      - `value: boolean`

      - `type: optional "boolean"`

        - `"boolean"`

    - `Integer object { name, value, type }`

      A setting whose enforced value is a whole number; null means no limit
      is in force.

      - `name: "account_session_duration_seconds"`

        - `"account_session_duration_seconds"`

      - `value: number`

      - `type: optional "integer"`

        - `"integer"`

    - `StringList object { name, value, type }`

      A setting whose enforced value is a list of strings.

      - `name: "allowed_invite_domains" or "ip_allowlist_ip_ranges"`

        - `"allowed_invite_domains"`

        - `"ip_allowlist_ip_ranges"`

      - `value: array of string`

      - `type: optional "string_list"`

        - `"string_list"`

    - `ProvisioningMode object { value, name, type }`

      How organization members are provisioned, resolved to the enforced mode.

      A configured mode is reported only while the mechanism that enforces it is
      active: just-in-time modes require single sign-on to be enabled, and SCIM
      modes require directory sync to be enabled. Otherwise `login_only` is
      reported, regardless of any stored configuration.

      - `value: "jit_advanced" or "jit_permissive" or "login_only" or 2 more`

        How organization members are provisioned under SSO.

        - `"jit_advanced"`

        - `"jit_permissive"`

        - `"login_only"`

        - `"scim_advanced"`

        - `"scim_permissive"`

      - `name: optional "sso_provisioning_mode"`

        - `"sso_provisioning_mode"`

      - `type: optional "provisioning_mode"`

        - `"provisioning_mode"`

    - `DataRetention object { value, name, type }`

      The data retention periods in force, keyed by the type of data they
      apply to.

      A key of `all` covers every data type and is exclusive: when present it
      is the only key. A missing key means no organization-level
      administrator-configured retention period is in force for that data type;
      Anthropic's service defaults may still apply.

      - `value: map[object { duration, timescale, type }  or object { type } ]`

        - `Fixed object { duration, timescale, type }`

          A fixed retention window measured from each item's last activity.

          - `duration: number`

          - `timescale: "day" or "month"`

            - `"day"`

            - `"month"`

          - `type: optional "fixed"`

            - `"fixed"`

        - `Indefinite object { type }`

          An indefinite retention period: data is kept with no time limit.

          - `type: optional "indefinite"`

            - `"indefinite"`

      - `name: optional "data_retention_periods"`

        - `"data_retention_periods"`

      - `type: optional "data_retention"`

        - `"data_retention"`

  - `type: optional "effective_organization_settings"`

    - `"effective_organization_settings"`
