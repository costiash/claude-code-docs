# Compliance API

# Activities

## List

**get** `/v1/compliance/activities`

List compliance activities for the authenticated parent organization.

Returns a paginated list of compliance activities that can be filtered by various criteria.

### Query Parameters

- `activity_types: optional array of "account_deleted" or "admin_api_key_created" or "admin_api_key_deleted" or 292 more`

  Filter activities by type

  - `"account_deleted"`

  - `"admin_api_key_created"`

  - `"admin_api_key_deleted"`

  - `"admin_api_key_updated"`

  - `"api_key_created"`

  - `"scoped_api_key_deleted"`

  - `"scoped_api_key_updated"`

  - `"claude_artifact_access_failed"`

  - `"claude_published_artifact_deleted"`

  - `"claude_artifact_published"`

  - `"claude_artifact_sharing_updated"`

  - `"claude_artifact_viewed"`

  - `"claude_chat_access_failed"`

  - `"claude_chat_snapshot_created"`

  - `"claude_chat_snapshot_viewed"`

  - `"claude_chat_created"`

  - `"claude_chat_deleted"`

  - `"claude_chat_deletion_failed"`

  - `"claude_chat_settings_updated"`

  - `"claude_chat_updated"`

  - `"desktop_extension_allowlisted"`

  - `"desktop_extension_blocklisted"`

  - `"desktop_extension_deleted"`

  - `"desktop_extension_removed_from_allowlist"`

  - `"desktop_extension_unblocked"`

  - `"desktop_extension_uploaded"`

  - `"desktop_extension_version_uploaded"`

  - `"plugin_installation_preference_updated"`

  - `"claude_chat_viewed"`

  - `"claude_code_review_config_updated"`

  - `"claude_code_review_repository_added"`

  - `"claude_code_review_repository_removed"`

  - `"claude_code_review_repository_updated"`

  - `"claude_code_security_center_config_updated"`

  - `"claude_file_access_failed"`

  - `"claude_file_deleted"`

  - `"claude_file_uploaded"`

  - `"claude_file_viewed"`

  - `"claude_gdrive_integration_created"`

  - `"claude_gdrive_integration_deleted"`

  - `"claude_gdrive_integration_updated"`

  - `"claude_github_integration_created"`

  - `"claude_github_integration_deleted"`

  - `"claude_github_integration_updated"`

  - `"claude_project_archived"`

  - `"claude_project_created"`

  - `"claude_project_deleted"`

  - `"claude_project_document_access_failed"`

  - `"claude_project_document_deleted"`

  - `"claude_project_document_deletion_failed"`

  - `"claude_project_document_uploaded"`

  - `"claude_project_document_viewed"`

  - `"claude_project_file_access_failed"`

  - `"claude_project_file_deleted"`

  - `"claude_project_file_deletion_failed"`

  - `"claude_project_file_uploaded"`

  - `"claude_project_reported"`

  - `"claude_project_sharing_updated"`

  - `"claude_project_viewed"`

  - `"claude_user_role_updated"`

  - `"claude_user_settings_updated"`

  - `"admin_request_created"`

  - `"compliance_api_accessed"`

  - `"domain_claim_initiated"`

  - `"end_user_invite_requested"`

  - `"environment_archived"`

  - `"environment_created"`

  - `"environment_deleted"`

  - `"environment_token_minted"`

  - `"environment_token_revoked"`

  - `"environment_updated"`

  - `"group_created"`

  - `"group_deleted"`

  - `"group_list_viewed"`

  - `"group_member_added"`

  - `"group_member_list_viewed"`

  - `"group_member_removed"`

  - `"group_updated"`

  - `"group_viewed"`

  - `"magic_link_login_failed"`

  - `"magic_link_login_initiated"`

  - `"magic_link_login_succeeded"`

  - `"social_login_succeeded"`

  - `"sso_login_failed"`

  - `"sso_login_initiated"`

  - `"sso_login_succeeded"`

  - `"service_created"`

  - `"service_deleted"`

  - `"service_key_created"`

  - `"service_key_revoked"`

  - `"platform_signing_key_created"`

  - `"platform_signing_key_deleted"`

  - `"platform_signing_key_rotated"`

  - `"user_logged_out"`

  - `"age_verified"`

  - `"anonymous_mobile_login_attempted"`

  - `"phone_code_sent"`

  - `"phone_code_verified"`

  - `"session_revoked"`

  - `"sso_second_factor_magic_link"`

  - `"org_user_deleted"`

  - `"org_user_invite_accepted"`

  - `"org_user_invite_deleted"`

  - `"org_user_invite_re_sent"`

  - `"org_user_invite_rejected"`

  - `"org_user_invite_sent"`

  - `"org_user_left"`

  - `"org_domain_add_initiated"`

  - `"org_domain_removed"`

  - `"org_domain_verified"`

  - `"org_join_proposal_decided"`

  - `"org_magic_link_second_factor_toggled"`

  - `"org_sso_add_initiated"`

  - `"org_sso_connection_activated"`

  - `"org_sso_connection_deactivated"`

  - `"org_sso_connection_deleted"`

  - `"org_sso_group_role_mappings_updated"`

  - `"org_sso_provisioning_mode_changed"`

  - `"org_sso_seat_tier_assignment_toggled"`

  - `"org_sso_seat_tier_mappings_updated"`

  - `"org_sso_toggled"`

  - `"org_directory_resync_completed"`

  - `"org_directory_resync_failed"`

  - `"org_directory_resync_started"`

  - `"org_directory_sync_activated"`

  - `"org_directory_sync_add_initiated"`

  - `"org_directory_sync_deleted"`

  - `"claude_organization_settings_updated"`

  - `"org_claude_code_data_sharing_disabled"`

  - `"org_claude_code_data_sharing_enabled"`

  - `"org_analytics_api_capability_updated"`

  - `"org_compliance_api_settings_updated"`

  - `"org_creation_blocked"`

  - `"org_parent_join_proposal_created"`

  - `"org_parent_search_performed"`

  - `"org_sync_deleting_synchronized_files_started"`

  - `"org_sync_synchronized_files_deleted"`

  - `"org_data_export_completed"`

  - `"org_data_export_started"`

  - `"org_members_exported"`

  - `"owned_projects_access_restored"`

  - `"audit_log_export_accessed"`

  - `"audit_log_export_started"`

  - `"org_data_export_accessed"`

  - `"organization_address_updated"`

  - `"primary_owner_transferred"`

  - `"role_assignment_granted"`

  - `"role_assignment_revoked"`

  - `"integration_user_connected"`

  - `"integration_user_disconnected"`

  - `"billing_emails_updated"`

  - `"extra_usage_billing_enabled"`

  - `"extra_usage_credit_granted"`

  - `"extra_usage_spend_limit_created"`

  - `"extra_usage_spend_limit_deleted"`

  - `"extra_usage_spend_limit_updated"`

  - `"invoice_collection_method_updated"`

  - `"managed_organization_setup_completed"`

  - `"payment_method_updated"`

  - `"platform_spend_limit_alert_emails_updated"`

  - `"platform_spend_limit_created"`

  - `"platform_spend_limit_deleted"`

  - `"platform_spend_limit_updated"`

  - `"prepaid_auto_recharge_disabled"`

  - `"prepaid_auto_recharge_updated"`

  - `"prepaid_extra_usage_auto_reload_disabled"`

  - `"prepaid_extra_usage_auto_reload_enabled"`

  - `"prepaid_extra_usage_auto_reload_settings_updated"`

  - `"seat_tier_changes_cancelled"`

  - `"seat_tiers_purchased"`

  - `"subscription_cancellation_scheduled"`

  - `"subscription_quantity_updated"`

  - `"subscription_renewed"`

  - `"subscription_resumed"`

  - `"subscription_started"`

  - `"subscription_upgraded"`

  - `"tunnel_token_minted"`

  - `"tunnel_token_revoked"`

  - `"user_consent_recorded"`

  - `"user_consent_revoked"`

  - `"workspace_member_spend_limit_created"`

  - `"workspace_member_spend_limit_deleted"`

  - `"workspace_member_spend_limit_updated"`

  - `"workspace_spend_limit_created"`

  - `"workspace_spend_limit_deleted"`

  - `"organization_icon_deleted"`

  - `"organization_icon_updated"`

  - `"org_ip_restriction_created"`

  - `"org_ip_restriction_deleted"`

  - `"org_ip_restriction_updated"`

  - `"org_bulk_delete_initiated"`

  - `"org_deleted_via_bulk"`

  - `"claude_skill_created"`

  - `"claude_skill_deleted"`

  - `"claude_skill_disabled"`

  - `"claude_skill_enabled"`

  - `"claude_skill_replaced"`

  - `"claude_command_created"`

  - `"claude_command_deleted"`

  - `"claude_command_replaced"`

  - `"claude_plugin_created"`

  - `"claude_plugin_deleted"`

  - `"claude_plugin_replaced"`

  - `"claude_plugin_updated"`

  - `"session_share_accessed"`

  - `"session_share_created"`

  - `"session_share_revoked"`

  - `"org_deletion_requested"`

  - `"org_invite_link_disabled"`

  - `"org_invite_link_generated"`

  - `"org_invite_link_regenerated"`

  - `"rbac_role_created"`

  - `"rbac_role_updated"`

  - `"rbac_role_deleted"`

  - `"rbac_role_assigned"`

  - `"rbac_role_unassigned"`

  - `"rbac_role_permission_added"`

  - `"rbac_role_permission_removed"`

  - `"org_claude_code_desktop_disabled"`

  - `"org_claude_code_desktop_enabled"`

  - `"org_cowork_disabled"`

  - `"org_cowork_enabled"`

  - `"org_cowork_agent_disabled"`

  - `"org_cowork_agent_enabled"`

  - `"org_work_across_apps_disabled"`

  - `"org_work_across_apps_enabled"`

  - `"org_hipaa_self_serve_enabled"`

  - `"org_taint_added"`

  - `"org_taint_removed"`

  - `"mcp_server_created"`

  - `"mcp_server_deleted"`

  - `"mcp_server_updated"`

  - `"mcp_tool_policy_updated"`

  - `"cli_plugin_exec_policy_updated"`

  - `"marketplace_created"`

  - `"marketplace_deleted"`

  - `"marketplace_updated"`

  - `"ghe_configuration_created"`

  - `"ghe_configuration_deleted"`

  - `"ghe_configuration_updated"`

  - `"ghe_user_connected"`

  - `"ghe_user_disconnected"`

  - `"ghe_webhook_signature_invalid"`

  - `"org_discoverability_enabled"`

  - `"org_discoverability_disabled"`

  - `"org_discoverability_settings_updated"`

  - `"org_join_request_created"`

  - `"org_join_request_approved"`

  - `"org_join_request_instant_approved"`

  - `"org_join_request_dismissed"`

  - `"org_join_requests_bulk_dismissed"`

  - `"org_member_invites_enabled"`

  - `"org_member_invites_disabled"`

  - `"lti_launch_initiated"`

  - `"lti_launch_success"`

  - `"lti_platform_created"`

  - `"lti_platform_updated"`

  - `"org_users_listed"`

  - `"org_user_viewed"`

  - `"org_invites_listed"`

  - `"org_invite_viewed"`

  - `"org_external_key_created"`

  - `"org_external_key_updated"`

  - `"org_external_key_deleted"`

  - `"org_external_key_validated"`

  - `"platform_workspace_created"`

  - `"platform_workspace_updated"`

  - `"platform_workspace_archived"`

  - `"platform_federation_issuer_archived"`

  - `"platform_federation_issuer_updated"`

  - `"platform_federation_rule_archived"`

  - `"platform_federation_rule_updated"`

  - `"platform_service_account_archived"`

  - `"platform_service_account_updated"`

  - `"platform_workspace_members_listed"`

  - `"platform_workspace_member_viewed"`

  - `"platform_workspace_member_added"`

  - `"platform_workspace_member_updated"`

  - `"platform_workspace_member_removed"`

  - `"platform_usage_report_messages_viewed"`

  - `"platform_usage_report_claude_code_viewed"`

  - `"platform_cost_report_viewed"`

  - `"platform_api_key_updated"`

  - `"platform_api_key_created"`

  - `"platform_workspace_rate_limit_updated"`

  - `"platform_workspace_rate_limit_deleted"`

  - `"platform_file_uploaded"`

  - `"platform_file_content_downloaded"`

  - `"platform_file_deleted"`

  - `"platform_skill_version_created"`

  - `"platform_skill_version_deleted"`

  - `"scim_user_created"`

  - `"scim_user_updated"`

  - `"scim_user_deleted"`

  - `"claude_pubsec_identity_configured"`

- `actor_ids: optional array of string`

  Filter activities by actor IDs (currently only `user_...` IDs are supported). Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.

- `after_id: optional string`

  Pagination cursor for retrieving the next page of results (heading backwards in time). To paginate, pass the `last_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `before_id: optional string`

  Pagination cursor for retrieving the previous page of results (heading forwards in time). To paginate, pass the `first_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `created_at: optional object { gt, gte, lt, lte }`

  - `gt: optional string`

    Filter activities created after this time (RFC 3339 format)

  - `gte: optional string`

    Filter activities created at or after this time (RFC 3339 format)

  - `lt: optional string`

    Filter activities created before this time (RFC 3339 format)

  - `lte: optional string`

    Filter activities created at or before this time (RFC 3339 format)

- `limit: optional number`

  Maximum results (default: 100, max: 5000)

- `organization_ids: optional array of string`

  Filter activities by organization IDs (accepts `org_...` or organization UUID). Enumerate IDs via `GET /v1/compliance/organizations`.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: optional array of map[unknown]`

- `first_id: optional string`

- `has_more: optional boolean`

- `last_id: optional string`

### Example

```http
curl https://api.anthropic.com/v1/compliance/activities \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Domain Types

### Activity List Response

- `ActivityListResponse = map[unknown]`

# Organizations

## List

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

## Domain Types

### Organization List Response

- `OrganizationListResponse = object { data }`

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

## List

**get** `/v1/compliance/organizations/{org_uuid}/users`

List current user members of an organization.

Returns:
List of user members with pagination info

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

- `data: array of object { id, created_at, email, full_name }`

  List of current organization members sorted by account creation date ascending

  - `id: string`

    User identifier (tagged ID)

  - `created_at: string`

    User account creation timestamp

  - `email: string`

    User's current email address

  - `full_name: string`

    User's current full name

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

### Example

```http
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/users \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Domain Types

### User List Response

- `UserListResponse = object { id, created_at, email, full_name }`

  User member information for compliance responses.

  - `id: string`

    User identifier (tagged ID)

  - `created_at: string`

    User account creation timestamp

  - `email: string`

    User's current email address

  - `full_name: string`

    User's current full name

# Roles

## List

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

## Retrieve

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

## Domain Types

### Role List Response

- `RoleListResponse = object { id, created_at, description, 2 more }`

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

- `RoleRetrieveResponse = object { id, created_at, description, 2 more }`

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

## List

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

## Domain Types

### Permission List Response

- `PermissionListResponse = object { action, resource_id, resource_type }`

  Permission granted by a role.

  - `action: string`

    Action permitted on the resource

  - `resource_id: string`

    Identifier of the resource the permission applies to

  - `resource_type: string`

    Type of resource the permission applies to

# Groups

## List

**get** `/v1/compliance/groups`

List Compliance Groups

### Query Parameters

- `limit: optional number`

  Maximum results (default: 500, max: 1000)

- `name_prefix: optional string`

  Filter groups by name prefix

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { id, created_at, description, 4 more }`

  List of groups

  - `id: string`

    Group identifier (tagged ID)

  - `created_at: string`

    Group creation timestamp (ISO 8601)

  - `description: string`

    Group description

  - `name: string`

    Group name

  - `roles: array of string`

    Role IDs assigned to this group.

  - `source_type: string`

    How the group was created ('direct' or 'scim')

  - `updated_at: string`

    Group last-updated timestamp (ISO 8601)

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

### Example

```http
curl https://api.anthropic.com/v1/compliance/groups \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Retrieve

**get** `/v1/compliance/groups/{group_id}`

Get Compliance Group

### Path Parameters

- `group_id: string`

  The group ID (tagged ID, e.g., rbac_group_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  Group identifier (tagged ID)

- `created_at: string`

  Group creation timestamp (ISO 8601)

- `description: string`

  Group description

- `name: string`

  Group name

- `roles: array of string`

  Role IDs assigned to this group.

- `source_type: string`

  How the group was created ('direct' or 'scim')

- `updated_at: string`

  Group last-updated timestamp (ISO 8601)

### Example

```http
curl https://api.anthropic.com/v1/compliance/groups/$GROUP_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Domain Types

### Group List Response

- `GroupListResponse = object { id, created_at, description, 4 more }`

  Group information for compliance responses.

  - `id: string`

    Group identifier (tagged ID)

  - `created_at: string`

    Group creation timestamp (ISO 8601)

  - `description: string`

    Group description

  - `name: string`

    Group name

  - `roles: array of string`

    Role IDs assigned to this group.

  - `source_type: string`

    How the group was created ('direct' or 'scim')

  - `updated_at: string`

    Group last-updated timestamp (ISO 8601)

### Group Retrieve Response

- `GroupRetrieveResponse = object { id, created_at, description, 4 more }`

  Group information for compliance responses.

  - `id: string`

    Group identifier (tagged ID)

  - `created_at: string`

    Group creation timestamp (ISO 8601)

  - `description: string`

    Group description

  - `name: string`

    Group name

  - `roles: array of string`

    Role IDs assigned to this group.

  - `source_type: string`

    How the group was created ('direct' or 'scim')

  - `updated_at: string`

    Group last-updated timestamp (ISO 8601)

# Members

## List

**get** `/v1/compliance/groups/{group_id}/members`

List Compliance Group Members

### Path Parameters

- `group_id: string`

  The group ID (tagged ID, e.g., rbac_group_abc123)

### Query Parameters

- `limit: optional number`

  Maximum results (default: 500, max: 1000)

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { created_at, email, updated_at, user_id }`

  List of group members

  - `created_at: string`

    Membership creation timestamp (ISO 8601)

  - `email: string`

    Member email address

  - `updated_at: string`

    Membership last-updated timestamp (ISO 8601)

  - `user_id: string`

    Member user identifier (tagged ID)

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

### Example

```http
curl https://api.anthropic.com/v1/compliance/groups/$GROUP_ID/members \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Domain Types

### Member List Response

- `MemberListResponse = object { created_at, email, updated_at, user_id }`

  Group member for compliance responses.

  - `created_at: string`

    Membership creation timestamp (ISO 8601)

  - `email: string`

    Member email address

  - `updated_at: string`

    Membership last-updated timestamp (ISO 8601)

  - `user_id: string`

    Member user identifier (tagged ID)

# Apps

# Chats

## List

**get** `/v1/compliance/apps/chats`

Lists chat metadata with filtering capabilities for targeted
compliance review. Results are sorted chronologically (time ascending)
by created_at, with ties broken by id.

### Query Parameters

- `user_ids: array of string`

  Filter to chats created by specific users. **Required**; pass 1–10 user IDs per request. Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.

- `after_id: optional string`

  Pagination cursor for retrieving the next page of results (heading backwards in time). To paginate, pass the `last_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `before_id: optional string`

  Pagination cursor for retrieving the previous page of results (heading forwards in time). To paginate, pass the `first_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `created_at: optional object { gt, gte, lt, lte }`

  - `gt: optional string`

    Filter chats created after this time (RFC 3339 format)

  - `gte: optional string`

    Filter chats created at or after this time (RFC 3339 format)

  - `lt: optional string`

    Filter chats created before this time (RFC 3339 format)

  - `lte: optional string`

    Filter chats created at or before this time (RFC 3339 format)

- `limit: optional number`

  Maximum results (default: 100, max: 1000)

- `organization_ids: optional array of string`

  Filter by organization IDs (accepts `org_...` or organization UUID). Enumerate IDs via `GET /v1/compliance/organizations`.

- `project_ids: optional array of string`

  Filter by project IDs (accepts `claude_proj_...`). Enumerate IDs via `GET /v1/compliance/apps/projects`.

- `updated_at: optional object { gt, gte, lt, lte }`

  - `gt: optional string`

    Filter chats updated after this time (RFC 3339 format)

  - `gte: optional string`

    Filter chats updated at or after this time (RFC 3339 format)

  - `lt: optional string`

    Filter chats updated before this time (RFC 3339 format)

  - `lte: optional string`

    Filter chats updated at or before this time (RFC 3339 format)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { id, created_at, deleted_at, 8 more }`

  List of chat metadata sorted chronologically by created_at, tie break by id

  - `id: string`

    Chat ID

  - `created_at: string`

    Creation timestamp

  - `deleted_at: string`

    Deletion timestamp if deleted

  - `href: string`

    URL to view this chat in claude.ai

  - `model: string`

    Model selected for this chat (e.g. 'claude-opus-4-7'). May be null for legacy chats that never had a model recorded.

  - `name: string`

    Chat name/title

  - `organization_id: string`

    Organization ID this chat belongs to

  - `organization_uuid: string`

    Organization UUID this chat belongs to

  - `project_id: string`

    Project ID this chat belongs to

  - `updated_at: string`

    Last update timestamp

  - `user: object { id, email_address }`

    User information for the chat creator

    - `id: string`

      User identifier

    - `email_address: string`

      User's email address

- `first_id: string`

  First chat ID in the current result set. To get the previous page, use this as before_id in your next request

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `last_id: string`

  Last chat ID in the current result set. To get the next page, use this as after_id in your next request

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/chats \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Delete

**delete** `/v1/compliance/apps/chats/{claude_chat_id}`

Permanently deletes a chat and all associated messages and
files. This is a destructive operation that cannot be undone.

### Path Parameters

- `claude_chat_id: string`

  The chat ID (tagged ID, e.g., claude_chat_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  The ID of the Claude chat that was deleted

- `type: optional "claude_chat_deleted"`

  Constant string confirming deletion

  - `"claude_chat_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/chats/$CLAUDE_CHAT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Messages

**get** `/v1/compliance/apps/chats/{claude_chat_id}/messages`

Retrieves message history and file metadata for a specific chat.

### Path Parameters

- `claude_chat_id: string`

  The chat ID (tagged ID, e.g., claude_chat_abc123)

### Query Parameters

- `after_id: optional string`

  Pagination cursor for retrieving the next page of results (heading backwards in time). To paginate, pass the `last_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `before_id: optional string`

  Pagination cursor for retrieving the previous page of results (heading forwards in time). To paginate, pass the `first_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `limit: optional number`

  Maximum results (max: 1000). When omitted, the full result set is returned in one response.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  Chat ID

- `chat_messages: array of object { id, artifacts, content, 4 more }`

  Array of chat messages in order of created_at

  - `id: string`

    Unique identifier for the message e.g. 'claude_chat_msg_abcd1234'

  - `artifacts: array of object { id, artifact_type, title, version_id }`

    Artifacts generated or updated by this message

    - `id: string`

      Artifact ID e.g. 'claude_artifact_abc123'

    - `artifact_type: string`

      MIME-like artifact type e.g. 'application/vnd.ant.code'

    - `title: string`

      Artifact title

    - `version_id: string`

      Artifact version ID e.g. 'claude_artifact_version_abc123'

  - `content: array of object { text, type }`

    Content blocks within the message

    - `text: string`

      Text content from human or assistant

    - `type: "text"`

      - `"text"`

  - `created_at: string`

    Message creation timestamp - For human: when they sent the message, For assistant: when it completed the last content block

  - `files: array of object { id, filename, mime_type }`

    File attachments

    - `id: string`

      File ID

    - `filename: string`

      Display name of the file

    - `mime_type: string`

      MIME type of the file when it was uploaded (e.g. 'application/pdf')

  - `generated_files: array of object { id, filename, mime_type }`

    Downloadable files the assistant created via tool use (e.g. PDF, spreadsheet, slide deck). Distinct from `files`, which are uploads attached to the message.

    - `id: string`

      Opaque generated-file id, e.g. 'claude_gen_file_abc123'. Treat as an opaque string; the encoding may change without notice.

    - `filename: string`

      Display name of the generated file

    - `mime_type: string`

      MIME type reported by the tool that produced the file

  - `role: "user" or "assistant"`

    Message sender (user or assistant)

    - `"user"`

    - `"assistant"`

- `created_at: string`

  Creation timestamp

- `deleted_at: string`

  Deletion timestamp if deleted

- `first_id: string`

  Opaque pagination cursor for the first message in the current result set. Pass as `before_id` on the next request to page backwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `has_more: boolean`

  Whether more chat messages exist beyond the current result set. Use `last_id` as `after_id` in a follow-up request to page forward.

- `href: string`

  URL to view this chat in claude.ai

- `last_id: string`

  Opaque pagination cursor for the last message in the current result set. Pass as `after_id` on the next request to page forwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `model: string`

  Model selected for this chat (e.g. 'claude-opus-4-7'). May be null for legacy chats that never had a model recorded.

- `name: string`

  Chat name

- `organization_id: string`

  Organization ID this chat belongs to

- `organization_uuid: string`

  Organization UUID this chat belongs to

- `project_id: string`

  Project ID this chat belongs to

- `updated_at: string`

  Last update timestamp

- `user: object { id, email_address }`

  User information

  - `id: string`

    User identifier

  - `email_address: string`

    User's email address

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/chats/$CLAUDE_CHAT_ID/messages \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Domain Types

### Chat List Response

- `ChatListResponse = object { id, created_at, deleted_at, 8 more }`

  Chat metadata for listing chats (without messages).

  - `id: string`

    Chat ID

  - `created_at: string`

    Creation timestamp

  - `deleted_at: string`

    Deletion timestamp if deleted

  - `href: string`

    URL to view this chat in claude.ai

  - `model: string`

    Model selected for this chat (e.g. 'claude-opus-4-7'). May be null for legacy chats that never had a model recorded.

  - `name: string`

    Chat name/title

  - `organization_id: string`

    Organization ID this chat belongs to

  - `organization_uuid: string`

    Organization UUID this chat belongs to

  - `project_id: string`

    Project ID this chat belongs to

  - `updated_at: string`

    Last update timestamp

  - `user: object { id, email_address }`

    User information for the chat creator

    - `id: string`

      User identifier

    - `email_address: string`

      User's email address

### Chat Delete Response

- `ChatDeleteResponse = object { id, type }`

  Response for deleting a Claude chat.

  - `id: string`

    The ID of the Claude chat that was deleted

  - `type: optional "claude_chat_deleted"`

    Constant string confirming deletion

    - `"claude_chat_deleted"`

### Chat Messages Response

- `ChatMessagesResponse = object { id, chat_messages, created_at, 12 more }`

  Complete chat conversation data for compliance purposes.

  - `id: string`

    Chat ID

  - `chat_messages: array of object { id, artifacts, content, 4 more }`

    Array of chat messages in order of created_at

    - `id: string`

      Unique identifier for the message e.g. 'claude_chat_msg_abcd1234'

    - `artifacts: array of object { id, artifact_type, title, version_id }`

      Artifacts generated or updated by this message

      - `id: string`

        Artifact ID e.g. 'claude_artifact_abc123'

      - `artifact_type: string`

        MIME-like artifact type e.g. 'application/vnd.ant.code'

      - `title: string`

        Artifact title

      - `version_id: string`

        Artifact version ID e.g. 'claude_artifact_version_abc123'

    - `content: array of object { text, type }`

      Content blocks within the message

      - `text: string`

        Text content from human or assistant

      - `type: "text"`

        - `"text"`

    - `created_at: string`

      Message creation timestamp - For human: when they sent the message, For assistant: when it completed the last content block

    - `files: array of object { id, filename, mime_type }`

      File attachments

      - `id: string`

        File ID

      - `filename: string`

        Display name of the file

      - `mime_type: string`

        MIME type of the file when it was uploaded (e.g. 'application/pdf')

    - `generated_files: array of object { id, filename, mime_type }`

      Downloadable files the assistant created via tool use (e.g. PDF, spreadsheet, slide deck). Distinct from `files`, which are uploads attached to the message.

      - `id: string`

        Opaque generated-file id, e.g. 'claude_gen_file_abc123'. Treat as an opaque string; the encoding may change without notice.

      - `filename: string`

        Display name of the generated file

      - `mime_type: string`

        MIME type reported by the tool that produced the file

    - `role: "user" or "assistant"`

      Message sender (user or assistant)

      - `"user"`

      - `"assistant"`

  - `created_at: string`

    Creation timestamp

  - `deleted_at: string`

    Deletion timestamp if deleted

  - `first_id: string`

    Opaque pagination cursor for the first message in the current result set. Pass as `before_id` on the next request to page backwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

  - `has_more: boolean`

    Whether more chat messages exist beyond the current result set. Use `last_id` as `after_id` in a follow-up request to page forward.

  - `href: string`

    URL to view this chat in claude.ai

  - `last_id: string`

    Opaque pagination cursor for the last message in the current result set. Pass as `after_id` on the next request to page forwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

  - `model: string`

    Model selected for this chat (e.g. 'claude-opus-4-7'). May be null for legacy chats that never had a model recorded.

  - `name: string`

    Chat name

  - `organization_id: string`

    Organization ID this chat belongs to

  - `organization_uuid: string`

    Organization UUID this chat belongs to

  - `project_id: string`

    Project ID this chat belongs to

  - `updated_at: string`

    Last update timestamp

  - `user: object { id, email_address }`

    User information

    - `id: string`

      User identifier

    - `email_address: string`

      User's email address

# Files

## Retrieve

**get** `/v1/compliance/apps/chats/files/{claude_file_id}`

Retrieves metadata for a file referenced in chat messages, without
downloading the file content. Use the sibling `/content` endpoint to
download the bytes.

### Path Parameters

- `claude_file_id: string`

  The file ID (tagged ID, e.g., claude_file_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  File ID

- `created_at: string`

  File creation timestamp

- `filename: string`

  Display name of the file, if set

- `message_ids: array of string`

  Chat message IDs this file is attached to. A file can be referenced by multiple messages.

- `mime_type: string`

  MIME type of the file's preferred downloadable variant (e.g. 'application/pdf'). May be null for files with no downloadable content (e.g. code-interpreter outputs).

- `size_bytes: number`

  Size in bytes of the file's preferred downloadable variant, if known

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Delete

**delete** `/v1/compliance/apps/chats/files/{claude_file_id}`

Permanently deletes a specific file. This is a destructive
operation that cannot be undone.

### Path Parameters

- `claude_file_id: string`

  The file ID (tagged ID, e.g., claude_file_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  The ID of the file that was deleted

- `type: optional "claude_file_deleted"`

  Constant string confirming deletion

  - `"claude_file_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Content

**get** `/v1/compliance/apps/chats/files/{claude_file_id}/content`

Downloads the binary content of a file referenced in chat messages.

### Path Parameters

- `claude_file_id: string`

  The file ID (tagged ID, e.g., claude_file_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID/content \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Domain Types

### File Retrieve Response

- `FileRetrieveResponse = object { id, created_at, filename, 3 more }`

  File metadata for GET /v1/compliance/apps/chats/files/{claude_file_id}.

  Returns metadata only. Use the sibling `/content` endpoint to download
  the file bytes.

  - `id: string`

    File ID

  - `created_at: string`

    File creation timestamp

  - `filename: string`

    Display name of the file, if set

  - `message_ids: array of string`

    Chat message IDs this file is attached to. A file can be referenced by multiple messages.

  - `mime_type: string`

    MIME type of the file's preferred downloadable variant (e.g. 'application/pdf'). May be null for files with no downloadable content (e.g. code-interpreter outputs).

  - `size_bytes: number`

    Size in bytes of the file's preferred downloadable variant, if known

### File Delete Response

- `FileDeleteResponse = object { id, type }`

  Response for deleting a compliance file.

  - `id: string`

    The ID of the file that was deleted

  - `type: optional "claude_file_deleted"`

    Constant string confirming deletion

    - `"claude_file_deleted"`

### File Content Response

- `FileContentResponse = unknown`

# Generated Files

## Content

**get** `/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content`

Downloads the binary content of a file the assistant created via tool use.

### Path Parameters

- `claude_gen_file_id: string`

  The generated-file id (e.g., 'claude_gen_file_abc123') as returned in `chat_messages[].generated_files[].id` from GET /apps/chats/{claude_chat_id}/messages.

### Header Parameters

- `"x-api-key": optional string`

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/chats/generated-files/$CLAUDE_GEN_FILE_ID/content \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Domain Types

### Generated File Content Response

- `GeneratedFileContentResponse = unknown`

# Projects

## List

**get** `/v1/compliance/apps/projects`

Lists project metadata with filtering capabilities. Results
are sorted chronologically (time ascending) by created_at.

### Query Parameters

- `created_at: optional object { gt, gte, lt, lte }`

  - `gt: optional string`

    Filter projects created after this time (RFC 3339 format)

  - `gte: optional string`

    Filter projects created at or after this time (RFC 3339 format)

  - `lt: optional string`

    Filter projects created before this time (RFC 3339 format)

  - `lte: optional string`

    Filter projects created at or before this time (RFC 3339 format)

- `limit: optional number`

  Maximum results (default: 20, max: 100)

- `organization_ids: optional array of string`

  Filter by organization IDs (accepts `org_...` or organization UUID). Enumerate IDs via `GET /v1/compliance/organizations`.

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `user_ids: optional array of string`

  Filter by user IDs. Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { id, created_at, is_private, 4 more }`

  List of projects sorted by creation date ascending

  - `id: string`

    Project identifier (tagged ID)

  - `created_at: string`

    Project creation timestamp

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

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/projects \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

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

## Delete

**delete** `/v1/compliance/apps/projects/{project_id}`

Delete a project for compliance purposes.

Hard-deletes the project and all its associated data including:

- All project documents and files
- All role assignments
- Knowledge base (if RAG is enabled)
- Sync sources

Project must have no attached chats - returns 409 if chats exist.

Returns:
ClaudeProjectDeleteResponse confirming the deletion

Raises:
ConflictException: If project has chats attached
NotFoundException: If project doesn't exist or already deleted

### Path Parameters

- `project_id: string`

  The project ID (tagged ID, e.g., claude_proj_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  The ID of the Claude project that was deleted

- `type: optional "claude_project_deleted"`

  Constant string confirming deletion.

  - `"claude_project_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

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

## Domain Types

### Project List Response

- `ProjectListResponse = object { id, created_at, is_private, 4 more }`

  Project information for compliance responses.

  - `id: string`

    Project identifier (tagged ID)

  - `created_at: string`

    Project creation timestamp

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

### Project Retrieve Response

- `ProjectRetrieveResponse = object { id, attachments_count, chats_count, 8 more }`

  Detailed project information for compliance responses.

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

### Project Delete Response

- `ProjectDeleteResponse = object { id, type }`

  Response for deleting a Claude project.

  - `id: string`

    The ID of the Claude project that was deleted

  - `type: optional "claude_project_deleted"`

    Constant string confirming deletion.

    - `"claude_project_deleted"`

### Project Attachments Response

- `ProjectAttachmentsResponse = object { data, has_more, next_page }`

  List of project attachments with pagination info.

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

# Artifacts

## Content

**get** `/v1/compliance/apps/artifacts/{artifact_version_id}/content`

Download the content of an artifact version for compliance purposes.

Returns the full text content of the artifact version.

### Path Parameters

- `artifact_version_id: string`

  The artifact version ID (tagged ID, e.g., claude_artifact_version_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/artifacts/$ARTIFACT_VERSION_ID/content \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Domain Types

### Artifact Content Response

- `ArtifactContentResponse = unknown`
