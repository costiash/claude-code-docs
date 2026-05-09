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
