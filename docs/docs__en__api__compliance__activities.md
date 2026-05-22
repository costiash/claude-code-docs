# Activities

## Query compliance activities

**get** `/v1/compliance/activities`

List compliance activities for the authenticated parent organization.

Returns a paginated list of compliance activities that can be filtered by various criteria.

### Query Parameters

- `activity_types: optional array of "account_deleted" or "admin_api_key_created" or "admin_api_key_deleted" or 302 more`

  Filter activities by type. See the response `data` schema for the additional fields each type returns.

  - `"account_deleted"`

    User-initiated self-service account deletion.

  - `"admin_api_key_created"`

    An admin API key was created.

  - `"admin_api_key_deleted"`

    An admin API key was deleted.

  - `"admin_api_key_updated"`

    An admin API key was updated (renamed or activated/deactivated).

  - `"admin_connector_request_resolved"`

    Admin approved or dismissed pending member requests to enable an MCP connector.

  - `"admin_request_created"`

    Admin request created by an org member (seat upgrade, limit increase, join org, end-user invite).

  - `"age_verified"`

    User age was verified.

  - `"anonymous_mobile_login_attempted"`

    Anonymous mobile login was attempted.

  - `"api_key_created"`

    Activity logged when a new API key is created.

  - `"audit_log_export_accessed"`

    Audit log export file was accessed/downloaded via signed URL.

  - `"audit_log_export_started"`

    Audit log export was initiated.

  - `"billing_emails_updated"`

    The organization's billing email recipients were updated.

  - `"claude_artifact_access_failed"`

    An attempt to access an artifact failed.

  - `"claude_artifact_created"`

    An artifact was created.

  - `"claude_artifact_published"`

    An artifact was published and made publicly accessible.

  - `"claude_artifact_sharing_updated"`

    An artifact's sharing settings were updated.

  - `"claude_artifact_viewed"`

    An artifact was viewed.

  - `"claude_chat_access_failed"`

    An attempt to access a chat failed.

  - `"claude_chat_created"`

    User created a chat.

  - `"claude_chat_deleted"`

    User deleted a chat.

  - `"claude_chat_deletion_failed"`

    A request to delete a chat failed.

  - `"claude_chat_settings_updated"`

    User updated the settings for a conversation.

  - `"claude_chat_snapshot_created"`

    User created/shared a chat snapshot.

  - `"claude_chat_snapshot_viewed"`

    User viewed a chat snapshot (authenticated or public/unauthenticated).

  - `"claude_chat_updated"`

    User updated the chat metadata (e.g name, model).

  - `"claude_chat_viewed"`

    User viewed a chat.

  - `"claude_code_review_config_updated"`

    Claude Code Review configuration was enabled/disabled for an org.

  - `"claude_code_review_repository_added"`

    A repository was added to org-level Claude Code Review configuration.

  - `"claude_code_review_repository_removed"`

    A repository was removed from org-level Claude Code Review configuration.

  - `"claude_code_review_repository_updated"`

    A Claude Code Review repository configuration was updated.

  - `"claude_code_security_center_config_updated"`

    Claude Code Security Center scanning was enabled/disabled for an org.

  - `"claude_code_security_scan_cancelled"`

    In-flight Claude Code Security scans were cancelled for a project.

  - `"claude_code_security_scan_project_updated"`

    A Claude Code Security scan project was archived or unarchived.

  - `"claude_code_security_scan_schedule_deleted"`

    A recurring scan schedule was deleted for a Claude Code Security project.

  - `"claude_code_security_scan_schedule_updated"`

    A recurring scan schedule was set or replaced for a Claude Code Security project.

  - `"claude_code_security_webhook_created"`

    An outbound webhook was created for a Claude Code Security scan project.

  - `"claude_code_security_webhook_deleted"`

    An outbound webhook for a Claude Code Security scan project was deleted.

  - `"claude_code_security_webhook_secret_updated"`

    The HMAC signing secret for a Claude Code Security webhook was rotated.

  - `"claude_code_security_webhook_updated"`

    An outbound webhook for a Claude Code Security scan project was updated.

  - `"claude_code_team_memory_acl_updated"`

    An RBAC group was added to or removed from the Claude Code team-memory ACL.

  - `"claude_command_created"`

    Command was created.

  - `"claude_command_deleted"`

    Command was deleted.

  - `"claude_command_replaced"`

    Command was replaced.

  - `"claude_file_access_failed"`

    An attempt to access a file failed.

  - `"claude_file_deleted"`

    A file was deleted.

  - `"claude_file_uploaded"`

    A file was uploaded.

  - `"claude_file_viewed"`

    A file was viewed.

  - `"claude_gdrive_integration_created"`

    A Google Drive integration was enabled for the organization.

  - `"claude_gdrive_integration_deleted"`

    A Google Drive integration was disabled for the organization.

  - `"claude_gdrive_integration_updated"`

    A Google Drive integration's configuration was updated.

  - `"claude_github_integration_created"`

    A GitHub integration was enabled for the organization.

  - `"claude_github_integration_deleted"`

    A GitHub integration was disabled for the organization.

  - `"claude_github_integration_updated"`

    A GitHub integration's configuration was updated.

  - `"claude_organization_settings_updated"`

    Organization settings were updated.

  - `"claude_plugin_created"`

    Plugin was created.

  - `"claude_plugin_deleted"`

    Plugin was deleted.

  - `"claude_plugin_replaced"`

    Plugin was replaced.

  - `"claude_plugin_updated"`

    Plugin was updated.

  - `"claude_project_archived"`

    A Claude project was archived.

  - `"claude_project_created"`

    A Claude project was created.

  - `"claude_project_deleted"`

    A Claude project was deleted.

  - `"claude_project_document_access_failed"`

    An attempt to access a document in a Claude project failed.

  - `"claude_project_document_deleted"`

    A document was deleted from a Claude project.

  - `"claude_project_document_deletion_failed"`

    A request to delete a document from a Claude project failed.

  - `"claude_project_document_uploaded"`

    A document was uploaded to a Claude project.

  - `"claude_project_document_viewed"`

    A document in a Claude project was viewed.

  - `"claude_project_file_access_failed"`

    An attempt to access a file in a Claude project failed.

  - `"claude_project_file_deleted"`

    A file was deleted from a Claude project.

  - `"claude_project_file_deletion_failed"`

    A request to delete a file from a Claude project failed.

  - `"claude_project_file_uploaded"`

    A file was uploaded to a Claude project.

  - `"claude_project_reported"`

    A Claude project was reported.

  - `"claude_project_sharing_updated"`

    A Claude project's sharing settings were updated.

  - `"claude_project_viewed"`

    A Claude project was viewed.

  - `"claude_published_artifact_deleted"`

    A published artifact was unpublished/deleted by its creator.

  - `"claude_pubsec_identity_configured"`

    SAML IdP configuration updated for a public sector organization.

  - `"claude_skill_created"`

    Skill was created.

  - `"claude_skill_deleted"`

    Skill was deleted.

  - `"claude_skill_disabled"`

    User disabled a skill for their account.

  - `"claude_skill_enabled"`

    User enabled a skill for their account.

  - `"claude_skill_replaced"`

    Skill was replaced.

  - `"claude_user_role_updated"`

    A user's role within the organization was changed, or the user was added to or removed from the organization.

  - `"claude_user_settings_updated"`

    User updated their personal settings.

  - `"cli_plugin_exec_policy_updated"`

    Admin set or cleared the per-op permission ceiling for a plugin CLI.

  - `"compliance_api_accessed"`

    Logging event auto-generated for each compliance API request.

  - `"desktop_extension_allowlisted"`

    A desktop extension was added to an org's allowlist.

  - `"desktop_extension_blocklisted"`

    A desktop extension was added to the global blocklist.

  - `"desktop_extension_deleted"`

    A desktop extension was deleted, either globally by an admin or org-scoped by an org owner.

  - `"desktop_extension_removed_from_allowlist"`

    A desktop extension was removed from an org's allowlist.

  - `"desktop_extension_unblocked"`

    A desktop extension was removed from the global blocklist.

  - `"desktop_extension_uploaded"`

    A desktop extension was uploaded, either globally by an admin or org-scoped by an org owner.

  - `"desktop_extension_version_uploaded"`

    A new version of an existing org-owned desktop extension was uploaded.

  - `"domain_claim_initiated"`

    Domain capture claim initiated over personal accounts on verified domains.

  - `"end_user_invite_requested"`

    Non-admin member submitted an invite request for a new org member.

  - `"extra_usage_billing_enabled"`

    Usage credit billing was enabled for an organization.

  - `"extra_usage_credit_granted"`

    A promotional usage credit grant was claimed.

  - `"extra_usage_spend_limit_created"`

    Usage credit spend limit was created.

  - `"extra_usage_spend_limit_deleted"`

    Usage credit spend limit was deleted.

  - `"extra_usage_spend_limit_increase_request_approved"`

    A usage credit spend limit increase request was approved.

  - `"extra_usage_spend_limit_increase_request_denied"`

    A usage credit spend limit increase request was denied.

  - `"extra_usage_spend_limit_updated"`

    Usage credit spend limit was updated.

  - `"ghe_configuration_created"`

    Admin created a GHE configuration.

  - `"ghe_configuration_deleted"`

    Admin deleted a GHE configuration.

  - `"ghe_configuration_updated"`

    Admin updated a GHE configuration.

  - `"ghe_user_connected"`

    User connected to a GHE instance.

  - `"ghe_user_disconnected"`

    User disconnected from a GHE instance.

  - `"ghe_webhook_signature_invalid"`

    Webhook signature validation failed.

  - `"group_created"`

    A group was created (RBAC admin or SCIM provisioning).

  - `"group_deleted"`

    A group was deleted (RBAC admin or SCIM provisioning).

  - `"group_list_viewed"`

    Admin viewed the list of RBAC groups.

  - `"group_member_added"`

    One or more members were added to a group.

  - `"group_member_list_viewed"`

    Admin viewed the members of an RBAC group.

  - `"group_member_removed"`

    One or more members were removed from a group.

  - `"group_updated"`

    A group was updated (RBAC admin or SCIM provisioning).

  - `"group_viewed"`

    A group was viewed.

  - `"integration_user_connected"`

    User connected to an integration.

  - `"integration_user_disconnected"`

    User disconnected from an integration.

  - `"invoice_collection_method_updated"`

    Invoice collection method was changed.

  - `"lti_launch_initiated"`

    LTI launch was initiated.

  - `"lti_launch_success"`

    LTI launch completed successfully.

  - `"lti_platform_created"`

    Admin created an LTI platform integration.

  - `"lti_platform_updated"`

    Admin updated an LTI platform integration.

  - `"magic_link_login_failed"`

    A magic link sign-in attempt failed.

  - `"magic_link_login_initiated"`

    A user requested a magic link sign-in email.

  - `"magic_link_login_succeeded"`

    A user successfully signed in with a magic link email.

  - `"managed_organization_setup_completed"`

    Managed (AWS Marketplace) organization setup was completed.

  - `"marketplace_created"`

    Admin created an organization marketplace.

  - `"marketplace_deleted"`

    Admin deleted an organization marketplace.

  - `"marketplace_updated"`

    Admin updated an organization marketplace.

  - `"marketplace_webhook_deleted"`

    Admin removed the GitHub push webhook for a marketplace.

  - `"marketplace_webhook_provisioned"`

    Admin provisioned a GitHub push webhook for a marketplace.

  - `"mcp_server_created"`

    An MCP server was added to the organization.

  - `"mcp_server_deleted"`

    An MCP server was removed from the organization.

  - `"mcp_server_updated"`

    An MCP server's configuration was updated.

  - `"mcp_tool_policy_updated"`

    The permission restriction for an MCP tool was set or cleared.

  - `"org_analytics_api_capability_updated"`

    Organization analytics_api capability was enabled or disabled.

  - `"org_bulk_delete_initiated"`

    Organization bulk deletion was initiated.

  - `"org_claude_code_data_sharing_disabled"`

    Organization Claude Code data sharing was disabled.

  - `"org_claude_code_data_sharing_enabled"`

    Organization Claude Code data sharing was enabled.

  - `"org_claude_code_desktop_disabled"`

    Organization Claude Code Desktop was disabled.

  - `"org_claude_code_desktop_enabled"`

    Organization Claude Code Desktop was enabled.

  - `"org_compliance_api_settings_updated"`

    Organization compliance API settings were updated.

  - `"org_cowork_agent_disabled"`

    Organization Cowork Agent was disabled.

  - `"org_cowork_agent_enabled"`

    Organization Cowork Agent was enabled.

  - `"org_cowork_disabled"`

    Organization cowork was disabled.

  - `"org_cowork_enabled"`

    Organization cowork was enabled.

  - `"org_creation_blocked"`

    Organization creation was blocked.

  - `"org_data_export_accessed"`

    Organization data export file was accessed/downloaded via signed URL.

  - `"org_data_export_completed"`

    Organization data export was completed.

  - `"org_data_export_started"`

    Organization data export was started.

  - `"org_deleted_via_bulk"`

    Organization was deleted via bulk operation.

  - `"org_deletion_requested"`

    Organization deletion was requested.

  - `"org_directory_resync_completed"`

    Organization directory resync completed successfully.

  - `"org_directory_resync_failed"`

    Organization directory resync failed.

  - `"org_directory_resync_started"`

    Organization directory resync was started asynchronously.

  - `"org_directory_sync_activated"`

    Organization directory sync was activated.

  - `"org_directory_sync_add_initiated"`

    Organization directory sync setup was initiated.

  - `"org_directory_sync_deleted"`

    Organization directory sync was deleted.

  - `"org_discoverability_disabled"`

    Admin disabled organization discoverability.

  - `"org_discoverability_enabled"`

    Admin enabled organization discoverability.

  - `"org_discoverability_settings_updated"`

    Admin updated organization discoverability settings.

  - `"org_domain_add_initiated"`

    Organization domain verification was initiated.

  - `"org_domain_removed"`

    Organization domain was removed.

  - `"org_domain_verified"`

    Organization domain was verified.

  - `"org_hipaa_self_serve_enabled"`

    A primary owner click-accepted the BAA and enabled HIPAA protections
    for the organization via the self-serve flow.

  - `"org_invite_link_disabled"`

    Organization invite link was disabled.

  - `"org_invite_link_generated"`

    Organization invite link was generated.

  - `"org_invite_link_regenerated"`

    Organization invite link was regenerated (previous link invalidated).

  - `"org_invite_viewed"`

    An organization invite was viewed.

  - `"org_invites_listed"`

    Organization invites were listed.

  - `"org_ip_restriction_created"`

    Organization IP restriction was created.

  - `"org_ip_restriction_deleted"`

    Organization IP restriction was deleted.

  - `"org_ip_restriction_updated"`

    Organization IP restriction was updated.

  - `"org_join_proposal_decided"`

    Approve or reject decision on a parent-org join proposal.

  - `"org_join_request_approved"`

    Admin approved a join request.

  - `"org_join_request_created"`

    User requested to join an organization.

  - `"org_join_request_dismissed"`

    Admin dismissed a join request.

  - `"org_join_request_instant_approved"`

    Join request was instantly approved.

  - `"org_join_requests_bulk_dismissed"`

    Admin bulk-dismissed join requests.

  - `"org_magic_link_second_factor_toggled"`

    Organization magic link second factor was toggled.

  - `"org_member_invites_disabled"`

    Admin disabled member invites for the organization.

  - `"org_member_invites_enabled"`

    Admin enabled member invites for the organization.

  - `"org_members_exported"`

    Organization members list was exported as CSV.

  - `"org_parent_join_proposal_created"`

    Organization parent join proposal was created.

  - `"org_parent_search_performed"`

    Organization parent search was performed.

  - `"org_sso_add_initiated"`

    Organization SSO setup was initiated.

  - `"org_sso_connection_activated"`

    Organization SSO connection was activated.

  - `"org_sso_connection_deactivated"`

    Organization SSO connection was deactivated.

  - `"org_sso_connection_deleted"`

    Organization SSO connection was deleted.

  - `"org_sso_group_role_mappings_updated"`

    Organization SSO group role mappings were updated.

  - `"org_sso_provisioning_mode_changed"`

    Organization SSO provisioning mode was changed.

  - `"org_sso_seat_tier_assignment_toggled"`

    Organization SSO seat tier assignment was toggled.

  - `"org_sso_seat_tier_mappings_updated"`

    Organization SSO seat tier mappings were updated.

  - `"org_sso_toggled"`

    Organization SSO was toggled on or off.

  - `"org_sync_deleting_synchronized_files_started"`

    Organization started deleting synchronized files.

  - `"org_sync_synchronized_files_deleted"`

    Organization synchronized files were deleted.

  - `"org_taint_added"`

    A taint was added to an organization.

  - `"org_taint_removed"`

    A taint was removed from an organization.

  - `"org_user_deleted"`

    User was removed from organization.

  - `"org_user_invite_accepted"`

    Organization user invite was accepted.

  - `"org_user_invite_deleted"`

    Organization user invite was deleted.

  - `"org_user_invite_re_sent"`

    Organization user invite was re-sent.

  - `"org_user_invite_rejected"`

    Organization user invite was rejected.

  - `"org_user_invite_sent"`

    Organization user invite was sent.

  - `"org_user_left"`

    User removed themselves from organization.

  - `"org_user_viewed"`

    An organization user was viewed.

  - `"org_users_listed"`

    Organization users were listed.

  - `"org_work_across_apps_disabled"`

    Organization Work Across Apps was disabled.

  - `"org_work_across_apps_enabled"`

    Organization Work Across Apps was enabled.

  - `"organization_address_updated"`

    The organization's billing or shipping address was updated.

  - `"organization_icon_deleted"`

    Organization's custom icon deleted.

  - `"organization_icon_updated"`

    Organization's custom icon uploaded or replaced.

  - `"owned_projects_access_restored"`

    Access to owned projects was restored.

  - `"payment_method_updated"`

    The organization's default payment method was updated.

  - `"phone_code_sent"`

    User requested a phone verification code.

  - `"phone_code_verified"`

    User successfully verified their phone code.

  - `"platform_api_key_created"`

    An API key was created.

  - `"platform_api_key_updated"`

    An API key was updated.

  - `"platform_cost_report_viewed"`

    The cost report was viewed.

  - `"platform_federation_issuer_archived"`

    An OIDC federation issuer was archived.

  - `"platform_federation_issuer_updated"`

    An OIDC federation issuer was updated.

  - `"platform_federation_rule_archived"`

    An OIDC federation rule was archived.

  - `"platform_federation_rule_updated"`

    An OIDC federation rule was updated.

  - `"platform_federation_rule_workspace_added"`

    A federation rule was enabled for a workspace.

  - `"platform_federation_rule_workspace_removed"`

    A federation rule was disabled for a workspace.

  - `"platform_file_content_downloaded"`

    Activity logged when file content is downloaded via GET /v1/files/{file_id}/content.

  - `"platform_file_deleted"`

    Activity logged when a file is deleted via DELETE /v1/files/{file_id}.

  - `"platform_file_uploaded"`

    Activity logged when a file is uploaded via POST /v1/files.

  - `"platform_service_account_archived"`

    A service account was archived.

  - `"platform_service_account_updated"`

    A service account was updated.

  - `"platform_service_account_workspace_member_added"`

    A service account was added as a member of a workspace.

  - `"platform_service_account_workspace_member_removed"`

    A service account was removed from a workspace.

  - `"platform_service_account_workspace_member_updated"`

    A service account's workspace membership role was updated.

  - `"platform_signing_key_created"`

    Activity logged when a new request-signing key is registered for the org.

  - `"platform_signing_key_deleted"`

    Activity logged when a signing key is permanently deleted.

  - `"platform_signing_key_rotated"`

    Activity logged when an in-memory signing key is rotated.

  - `"platform_skill_version_created"`

    Activity logged when a skill version is created via POST /v1/skills/{skill_id}/versions.

  - `"platform_skill_version_deleted"`

    Activity logged when a skill version is deleted via DELETE /v1/skills/{skill_id}/versions/{version}.

  - `"platform_spend_limit_alert_emails_updated"`

    Spend limit alert email addresses and role targets were updated for an org.

  - `"platform_spend_limit_created"`

    An org-level fixed-dollar spend limit was created.

  - `"platform_spend_limit_deleted"`

    An org-level spend limit was removed.

  - `"platform_spend_limit_updated"`

    An org-level spend limit snooze/ignore state was changed.

  - `"platform_usage_report_claude_code_viewed"`

    The Claude Code usage report was viewed.

  - `"platform_usage_report_messages_viewed"`

    The messages usage report was viewed.

  - `"platform_workspace_archived"`

    A workspace was archived.

  - `"platform_workspace_created"`

    A workspace was created.

  - `"platform_workspace_member_added"`

    A member was added to a workspace.

  - `"platform_workspace_member_removed"`

    A member was removed from a workspace.

  - `"platform_workspace_member_updated"`

    A workspace member was updated.

  - `"platform_workspace_member_viewed"`

    A workspace member was viewed.

  - `"platform_workspace_members_listed"`

    Workspace members were listed.

  - `"platform_workspace_rate_limit_deleted"`

    A workspace rate limit was deleted.

  - `"platform_workspace_rate_limit_updated"`

    A workspace rate limit was created or updated.

  - `"platform_workspace_updated"`

    A workspace was updated.

  - `"plugin_installation_preference_updated"`

    An org admin changed the installation preference for a plugin.

  - `"prepaid_auto_recharge_disabled"`

    Auto-recharge was disabled for API prepaid org.

  - `"prepaid_auto_recharge_updated"`

    Auto-recharge settings were updated for API prepaid org.

  - `"prepaid_extra_usage_auto_reload_disabled"`

    Prepaid usage credit auto-reload was disabled.

  - `"prepaid_extra_usage_auto_reload_enabled"`

    Prepaid usage credit auto-reload was enabled.

  - `"prepaid_extra_usage_auto_reload_settings_updated"`

    Prepaid usage credit auto-reload settings were updated.

  - `"primary_owner_transferred"`

    Primary owner role was transferred to another org member.

  - `"rbac_role_assigned"`

    Admin assigned an RBAC custom role to a principal.

  - `"rbac_role_created"`

    Admin created an RBAC custom role.

  - `"rbac_role_deleted"`

    Admin deleted an RBAC custom role.

  - `"rbac_role_permission_added"`

    Admin added a permission to an RBAC custom role.

  - `"rbac_role_permission_removed"`

    Admin removed a permission from an RBAC custom role.

  - `"rbac_role_unassigned"`

    Admin unassigned an RBAC custom role from a principal.

  - `"rbac_role_updated"`

    Admin updated an RBAC custom role.

  - `"role_assignment_granted"`

    Role assignment was granted.

  - `"role_assignment_revoked"`

    Role assignment was revoked.

  - `"scim_user_created"`

    A SCIM user was provisioned.

  - `"scim_user_deleted"`

    A SCIM user was deleted.

  - `"scim_user_updated"`

    A SCIM user was updated.

  - `"scoped_api_key_deleted"`

    A scoped API key was deleted.

  - `"scoped_api_key_updated"`

    A scoped API key was renamed or its activation state changed.

  - `"seat_tier_changes_cancelled"`

    Scheduled seat tier downgrades were cancelled.

  - `"seat_tiers_purchased"`

    Seat tiers were purchased or upgraded on a subscription.

  - `"service_created"`

    Activity logged when an org service is explicitly created.

  - `"service_deleted"`

    Activity logged when an org service is deleted.

  - `"service_key_created"`

    Activity logged when a new org service key is created.

  - `"service_key_revoked"`

    Activity logged when an org service key is revoked.

  - `"session_revoked"`

    User revoked a specific session.

  - `"session_share_accessed"`

    Session share was accessed.

  - `"session_share_created"`

    Session share was created.

  - `"session_share_revoked"`

    Session share was revoked.

  - `"social_login_succeeded"`

    A user successfully signed in with a social identity provider (Google, Apple, or Microsoft).

  - `"sso_login_failed"`

    An SSO sign-in attempt failed.

  - `"sso_login_initiated"`

    A user started an SSO sign-in flow.

  - `"sso_login_succeeded"`

    A user successfully signed in with SSO.

  - `"sso_second_factor_magic_link"`

    SSO second factor magic link was used.

  - `"subscription_cancellation_scheduled"`

    Subscription cancellation was scheduled at end of billing period.

  - `"subscription_quantity_updated"`

    Contracted subscription seat quantity was updated.

  - `"subscription_renewed"`

    A cancelled subscription was renewed.

  - `"subscription_resumed"`

    A scheduled subscription cancellation was reversed.

  - `"subscription_started"`

    A new subscription was created (Team or Enterprise).

  - `"subscription_upgraded"`

    Subscription plan was upgraded (e.g. Team to Enterprise).

  - `"tunnel_token_minted"`

    An OAuth bearer token for the tunnel management API was minted.

  - `"tunnel_token_revoked"`

    An OAuth bearer token for the tunnel management API was revoked.

  - `"user_consent_recorded"`

    User granted a consent for a specific entity (e.g. consumer health consent for an MCP server).

  - `"user_consent_revoked"`

    User revoked a previously granted consent for a specific entity.

  - `"user_logged_out"`

    A user signed out of one or all sessions.

  - `"workspace_member_spend_limit_created"`

    A per-member or workspace-default Claude Code spend limit was created.

  - `"workspace_member_spend_limit_deleted"`

    A per-member or workspace-default Claude Code spend limit was deleted.

  - `"workspace_member_spend_limit_updated"`

    A per-member Claude Code spend limit amount was updated.

  - `"workspace_spend_limit_created"`

    A workspace-level API spend limit was created.

  - `"workspace_spend_limit_deleted"`

    A workspace-level API spend limit was deleted.

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

- `data: optional array of object { actor, id, created_at, 3 more }  or object { actor, admin_api_key_id, scopes, 5 more }  or object { actor, admin_api_key_id, id, 4 more }  or 302 more`

  List of activity records. Each element's `type` field identifies which activity it is and which additional fields are present.

  - `AccountDeleted object { actor, id, created_at, 3 more }`

    User-initiated self-service account deletion.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "account_deleted"`

      - `"account_deleted"`

  - `AdminAPIKeyCreated object { actor, admin_api_key_id, scopes, 5 more }`

    An admin API key was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `admin_api_key_id: string`

      Tagged ID of the created admin API key

    - `scopes: array of string`

      Scopes granted to the key (empty for legacy non-scoped admin keys)

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "admin_api_key_created"`

      - `"admin_api_key_created"`

  - `AdminAPIKeyDeleted object { actor, admin_api_key_id, id, 4 more }`

    An admin API key was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `admin_api_key_id: string`

      Tagged ID of the deleted admin API key

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "admin_api_key_deleted"`

      - `"admin_api_key_deleted"`

  - `AdminAPIKeyUpdated object { actor, admin_api_key_id, updates, 5 more }`

    An admin API key was updated (renamed or activated/deactivated).

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `admin_api_key_id: string`

      Tagged ID of the updated admin API key

    - `updates: array of object { current_value, previous_value, type }`

      - `current_value: string`

      - `previous_value: string`

      - `type: "name" or "status"`

        - `"name"`

        - `"status"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "admin_api_key_updated"`

      - `"admin_api_key_updated"`

  - `AdminConnectorRequestResolved object { actor, decision, mcp_server_id, 6 more }`

    Admin approved or dismissed pending member requests to enable an MCP connector.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `decision: "approved" or "dismissed"`

      - `"approved"`

      - `"dismissed"`

    - `mcp_server_id: string`

    - `resolved_count: number`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "admin_connector_request_resolved"`

      - `"admin_connector_request_resolved"`

  - `AdminRequestCreated object { actor, request_type, id, 4 more }`

    Admin request created by an org member (seat upgrade, limit increase, join org, end-user invite).

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `request_type: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "admin_request_created"`

      - `"admin_request_created"`

  - `AgeVerified object { actor, id, created_at, 3 more }`

    User age was verified.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "age_verified"`

      - `"age_verified"`

  - `AnonymousMobileLoginAttempted object { actor, id, created_at, 3 more }`

    Anonymous mobile login was attempted.

    - `actor: object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `ip_address: string`

      - `user_agent: string`

      - `type: optional "unauthenticated_user_actor"`

        - `"unauthenticated_user_actor"`

      - `unauthenticated_email_address: optional string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "anonymous_mobile_login_attempted"`

      - `"anonymous_mobile_login_attempted"`

  - `APIKeyCreated object { actor, api_key_id, scopes, 5 more }`

    Activity logged when a new API key is created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `api_key_id: string`

      The tagged ID of the created API key

    - `scopes: array of string`

      The scopes for this API key

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "api_key_created"`

      - `"api_key_created"`

  - `ClaudeArtifactAccessFailed object { actor, claude_artifact_id, claude_artifact_version_id, 5 more }`

    An attempt to access an artifact failed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `claude_artifact_id: string`

    - `claude_artifact_version_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_artifact_access_failed"`

      - `"claude_artifact_access_failed"`

  - `ClaudeArtifactCreated object { actor, claude_artifact_id, id, 4 more }`

    An artifact was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_artifact_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_artifact_created"`

      - `"claude_artifact_created"`

  - `ClaudePublishedArtifactDeleted object { actor, claude_published_artifact_id, id, 4 more }`

    A published artifact was unpublished/deleted by its creator.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_published_artifact_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_published_artifact_deleted"`

      - `"claude_published_artifact_deleted"`

  - `ClaudeArtifactPublished object { actor, artifact_type, claude_published_artifact_id, 6 more }`

    An artifact was published and made publicly accessible.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `artifact_type: string`

      Artifact type (code, html, react, etc.)

    - `claude_published_artifact_id: string`

    - `title: string`

      Title of the published artifact

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_artifact_published"`

      - `"claude_artifact_published"`

  - `ClaudeArtifactSharingUpdated object { actor, audience, claude_artifact_id, 6 more }`

    An artifact's sharing settings were updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `audience: array of object { type }`

      Sharing audience for the project. If empty, this it's only visible to the creating user.

      - `type: optional "organization"`

        - `"organization"`

    - `claude_artifact_id: string`

    - `claude_artifact_version_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_artifact_sharing_updated"`

      - `"claude_artifact_sharing_updated"`

  - `ClaudeArtifactViewed object { actor, claude_artifact_id, id, 4 more }`

    An artifact was viewed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_artifact_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_artifact_viewed"`

      - `"claude_artifact_viewed"`

  - `AuditLogExportAccessed object { actor, id, created_at, 3 more }`

    Audit log export file was accessed/downloaded via signed URL.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "audit_log_export_accessed"`

      - `"audit_log_export_accessed"`

  - `AuditLogExportStarted object { actor, id, created_at, 5 more }`

    Audit log export was initiated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `from_date: optional string`

      Start date of the export range

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `to_date: optional string`

      End date of the export range

    - `type: optional "audit_log_export_started"`

      - `"audit_log_export_started"`

  - `BillingEmailsUpdated object { actor, id, cc_email_count, 6 more }`

    The organization's billing email recipients were updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `cc_email_count: optional number`

      Number of 'cc' email recipients.

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `primary_email_set: optional boolean`

      Whether a primary billing email is configured.

    - `to_email_count: optional number`

      Number of 'to' email recipients.

    - `type: optional "billing_emails_updated"`

      - `"billing_emails_updated"`

  - `ClaudeChatAccessFailed object { actor, claude_chat_id, id, 4 more }`

    An attempt to access a chat failed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `claude_chat_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_chat_access_failed"`

      - `"claude_chat_access_failed"`

  - `ClaudeChatCreated object { actor, claude_chat_id, id, 5 more }`

    User created a chat.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_chat_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `claude_project_id: optional string`

      Project ID this chat belongs to, if any

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_chat_created"`

      - `"claude_chat_created"`

  - `ClaudeChatDeleted object { actor, claude_chat_id, id, 5 more }`

    User deleted a chat.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_chat_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `claude_project_id: optional string`

      Project ID this chat belongs to, if any

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_chat_deleted"`

      - `"claude_chat_deleted"`

  - `ClaudeChatDeletionFailed object { actor, claude_chat_id, id, 4 more }`

    A request to delete a chat failed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `claude_chat_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_chat_deletion_failed"`

      - `"claude_chat_deletion_failed"`

  - `ClaudeChatSettingsUpdated object { actor, claude_chat_id, id, 5 more }`

    User updated the settings for a conversation.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_chat_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `claude_project_id: optional string`

      Project ID this chat belongs to, if any

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_chat_settings_updated"`

      - `"claude_chat_settings_updated"`

  - `ClaudeChatSnapshotCreated object { actor, claude_chat_id, claude_chat_snapshot_id, 5 more }`

    User created/shared a chat snapshot.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_chat_id: string`

    - `claude_chat_snapshot_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_chat_snapshot_created"`

      - `"claude_chat_snapshot_created"`

  - `ClaudeChatSnapshotViewed object { actor, claude_chat_snapshot_id, id, 5 more }`

    User viewed a chat snapshot (authenticated or public/unauthenticated).

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `claude_chat_snapshot_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `claude_chat_id: optional string`

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_chat_snapshot_viewed"`

      - `"claude_chat_snapshot_viewed"`

  - `ClaudeChatUpdated object { actor, claude_chat_id, id, 5 more }`

    User updated the chat metadata (e.g name, model).

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_chat_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `claude_project_id: optional string`

      Project ID this chat belongs to, if any

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_chat_updated"`

      - `"claude_chat_updated"`

  - `ClaudeChatViewed object { actor, claude_chat_id, id, 5 more }`

    User viewed a chat.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_chat_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `claude_project_id: optional string`

      Project ID this chat belongs to, if any

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_chat_viewed"`

      - `"claude_chat_viewed"`

  - `ClaudeCodeReviewConfigUpdated object { actor, enabled, id, 7 more }`

    Claude Code Review configuration was enabled/disabled for an org.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `enabled: boolean`

      Whether code review is now enabled

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `environment_id: optional string`

      Environment used for code review

    - `model: optional string`

      Model configured for code review

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `per_review_limit_usd: optional string`

      Per-review spend limit in USD

    - `type: optional "claude_code_review_config_updated"`

      - `"claude_code_review_config_updated"`

  - `ClaudeCodeReviewRepositoryAdded object { actor, config_id, repo_name, 7 more }`

    A repository was added to org-level Claude Code Review configuration.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `config_id: string`

      ID of the repository configuration

    - `repo_name: string`

      Repository name

    - `repo_owner: string`

      Repository owner (GitHub org/user)

    - `trigger_mode: string`

      When code review is triggered

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_code_review_repository_added"`

      - `"claude_code_review_repository_added"`

  - `ClaudeCodeReviewRepositoryRemoved object { actor, config_id, repo_name, 6 more }`

    A repository was removed from org-level Claude Code Review configuration.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `config_id: string`

      ID of the deleted repository configuration

    - `repo_name: string`

      Repository name at deletion time

    - `repo_owner: string`

      Repository owner at deletion time

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_code_review_repository_removed"`

      - `"claude_code_review_repository_removed"`

  - `ClaudeCodeReviewRepositoryUpdated object { actor, config_id, repo_name, 8 more }`

    A Claude Code Review repository configuration was updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `config_id: string`

      ID of the repository configuration

    - `repo_name: string`

      Repository name

    - `repo_owner: string`

      Repository owner

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `status: optional string`

      Updated status (ACTIVE/INACTIVE)

    - `trigger_mode: optional string`

      Updated trigger mode

    - `type: optional "claude_code_review_repository_updated"`

      - `"claude_code_review_repository_updated"`

  - `ClaudeCodeSecurityCenterConfigUpdated object { actor, enabled, id, 5 more }`

    Claude Code Security Center scanning was enabled/disabled for an org.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `enabled: boolean`

      Whether Security Center is now enabled

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `environment_id: optional string`

      Environment used for security scanning

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_code_security_center_config_updated"`

      - `"claude_code_security_center_config_updated"`

  - `ClaudeCodeSecurityScanCancelled object { actor, scan_project_id, scans_cancelled, 5 more }`

    In-flight Claude Code Security scans were cancelled for a project.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `scan_project_id: string`

      Tagged ID of the scan project

    - `scans_cancelled: number`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_code_security_scan_cancelled"`

      - `"claude_code_security_scan_cancelled"`

  - `ClaudeCodeSecurityScanProjectUpdated object { action, actor, scan_project_id, 5 more }`

    A Claude Code Security scan project was archived or unarchived.

    - `action: "archived" or "unarchived"`

      - `"archived"`

      - `"unarchived"`

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `scan_project_id: string`

      Tagged ID of the scan project

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_code_security_scan_project_updated"`

      - `"claude_code_security_scan_project_updated"`

  - `ClaudeCodeSecurityScanScheduleDeleted object { actor, scan_project_id, id, 4 more }`

    A recurring scan schedule was deleted for a Claude Code Security project.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `scan_project_id: string`

      Tagged ID of the scan project

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_code_security_scan_schedule_deleted"`

      - `"claude_code_security_scan_schedule_deleted"`

  - `ClaudeCodeSecurityScanScheduleUpdated object { actor, cadence, scan_project_id, 5 more }`

    A recurring scan schedule was set or replaced for a Claude Code Security project.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `cadence: string`

    - `scan_project_id: string`

      Tagged ID of the scan project

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_code_security_scan_schedule_updated"`

      - `"claude_code_security_scan_schedule_updated"`

  - `ClaudeCodeSecurityWebhookCreated object { actor, scan_project_id, url, 6 more }`

    An outbound webhook was created for a Claude Code Security scan project.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `scan_project_id: string`

      Tagged ID of the scan project

    - `url: string`

    - `webhook_id: string`

      Tagged ID of the webhook

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_code_security_webhook_created"`

      - `"claude_code_security_webhook_created"`

  - `ClaudeCodeSecurityWebhookDeleted object { actor, scan_project_id, webhook_id, 5 more }`

    An outbound webhook for a Claude Code Security scan project was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `scan_project_id: string`

      Tagged ID of the scan project

    - `webhook_id: string`

      Tagged ID of the webhook

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_code_security_webhook_deleted"`

      - `"claude_code_security_webhook_deleted"`

  - `ClaudeCodeSecurityWebhookSecretUpdated object { actor, scan_project_id, webhook_id, 5 more }`

    The HMAC signing secret for a Claude Code Security webhook was rotated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `scan_project_id: string`

      Tagged ID of the scan project

    - `webhook_id: string`

      Tagged ID of the webhook

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_code_security_webhook_secret_updated"`

      - `"claude_code_security_webhook_secret_updated"`

  - `ClaudeCodeSecurityWebhookUpdated object { actor, scan_project_id, webhook_id, 5 more }`

    An outbound webhook for a Claude Code Security scan project was updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `scan_project_id: string`

      Tagged ID of the scan project

    - `webhook_id: string`

      Tagged ID of the webhook

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_code_security_webhook_updated"`

      - `"claude_code_security_webhook_updated"`

  - `ClaudeCodeTeamMemoryACLUpdated object { action, actor, group_id, 6 more }`

    An RBAC group was added to or removed from the Claude Code team-memory ACL.

    - `action: "removed" or "set"`

      Whether the group was set (added/updated) or removed

      - `"removed"`

      - `"set"`

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `group_id: string`

      Tagged ID of the RBAC group

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `access_level: optional string`

      Access level granted (when action=set)

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_code_team_memory_acl_updated"`

      - `"claude_code_team_memory_acl_updated"`

  - `CliPluginExecPolicyUpdated object { actor, cli_name, marketplace_id, 9 more }`

    Admin set or cleared the per-op permission ceiling for a plugin CLI.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `cli_name: string`

      CLI name as declared by the plugin manifest

    - `marketplace_id: string`

      Marketplace ID owning the plugin

    - `max_permission: string`

      New max_permission value ('allow' | 'ask' | 'blocked'), or null when cleared

    - `op_name: string`

      Op name (or '*' for the per-CLI default)

    - `plugin_id: string`

      Plugin ID resolved from the URL

    - `plugin_name: string`

      Plugin name within its marketplace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "cli_plugin_exec_policy_updated"`

      - `"cli_plugin_exec_policy_updated"`

  - `ClaudeCommandCreated object { actor, id, command_id, 5 more }`

    Command was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `command_id: optional string`

    - `command_name: optional string`

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_command_created"`

      - `"claude_command_created"`

  - `ClaudeCommandDeleted object { actor, id, command_id, 5 more }`

    Command was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `command_id: optional string`

    - `command_name: optional string`

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_command_deleted"`

      - `"claude_command_deleted"`

  - `ClaudeCommandReplaced object { actor, id, command_id, 5 more }`

    Command was replaced.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `command_id: optional string`

    - `command_name: optional string`

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_command_replaced"`

      - `"claude_command_replaced"`

  - `ComplianceAPIAccessed object { actor, request_id, request_method, 8 more }`

    Logging event auto-generated for each compliance API request.

    - `actor: object { api_key_id, ip_address, user_agent, type }`

      - `api_key_id: string`

      - `ip_address: string`

      - `user_agent: string`

      - `type: optional "api_actor"`

        - `"api_actor"`

    - `request_id: string`

    - `request_method: "DELETE" or "GET" or "POST" or "PUT"`

      - `"DELETE"`

      - `"GET"`

      - `"POST"`

      - `"PUT"`

    - `status_code: number`

      HTTP status code

    - `url: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `request_body: optional string`

      Serialized JSON request body

    - `type: optional "compliance_api_accessed"`

      - `"compliance_api_accessed"`

  - `DesktopExtensionAllowlisted object { actor, extension_id, id, 4 more }`

    A desktop extension was added to an org's allowlist.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `extension_id: string`

      Allowlisted DXT extension ID

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "desktop_extension_allowlisted"`

      - `"desktop_extension_allowlisted"`

  - `DesktopExtensionBlocklisted object { actor, extension_id, id, 4 more }`

    A desktop extension was added to the global blocklist.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `extension_id: string`

      Blocklisted DXT extension ID

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "desktop_extension_blocklisted"`

      - `"desktop_extension_blocklisted"`

  - `DesktopExtensionDeleted object { actor, extension_id, id, 5 more }`

    A desktop extension was deleted, either globally by an admin or org-scoped by an org owner.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `extension_id: string`

      DXT extension ID

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "desktop_extension_deleted"`

      - `"desktop_extension_deleted"`

    - `version: optional string`

      Specific version deleted (null if all versions)

  - `DesktopExtensionRemovedFromAllowlist object { actor, extension_id, id, 4 more }`

    A desktop extension was removed from an org's allowlist.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `extension_id: string`

      DXT extension ID removed from allowlist

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "desktop_extension_removed_from_allowlist"`

      - `"desktop_extension_removed_from_allowlist"`

  - `DesktopExtensionUnblocked object { actor, extension_id, id, 4 more }`

    A desktop extension was removed from the global blocklist.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `extension_id: string`

      Unblocked DXT extension ID

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "desktop_extension_unblocked"`

      - `"desktop_extension_unblocked"`

  - `DesktopExtensionUploaded object { actor, extension_id, version, 5 more }`

    A desktop extension was uploaded, either globally by an admin or org-scoped by an org owner.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `extension_id: string`

      DXT extension ID

    - `version: string`

      Version string from the manifest

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "desktop_extension_uploaded"`

      - `"desktop_extension_uploaded"`

  - `DesktopExtensionVersionUploaded object { actor, extension_id, version, 5 more }`

    A new version of an existing org-owned desktop extension was uploaded.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `extension_id: string`

      DXT extension ID

    - `version: string`

      Version string from the manifest

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "desktop_extension_version_uploaded"`

      - `"desktop_extension_version_uploaded"`

  - `DomainClaimInitiated object { actor, id, created_at, 3 more }`

    Domain capture claim initiated over personal accounts on verified domains.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "domain_claim_initiated"`

      - `"domain_claim_initiated"`

  - `EndUserInviteRequested object { actor, invitee_email, id, 4 more }`

    Non-admin member submitted an invite request for a new org member.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `invitee_email: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "end_user_invite_requested"`

      - `"end_user_invite_requested"`

  - `ExtraUsageBillingEnabled object { actor, id, created_at, 3 more }`

    Usage credit billing was enabled for an organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "extra_usage_billing_enabled"`

      - `"extra_usage_billing_enabled"`

  - `ExtraUsageCreditGranted object { actor, id, created_at, 3 more }`

    A promotional usage credit grant was claimed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "extra_usage_credit_granted"`

      - `"extra_usage_credit_granted"`

  - `ExtraUsageSpendLimitCreated object { actor, id, amount, 8 more }`

    Usage credit spend limit was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }  or object { api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `amount: optional number`

      The monthly credit limit amount in minor units (e.g. cents).

    - `created_at: optional string`

      When this activity occurred.

    - `is_enabled: optional boolean`

      Whether the spend limit is enabled.

    - `limit_type: optional string`

      The type of spend limit created (e.g. organization, seat_tier, member, service, group).

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `spend_limit_id: optional string`

      Tagged ID of the spend limit.

    - `type: optional "extra_usage_spend_limit_created"`

      - `"extra_usage_spend_limit_created"`

    - `user_id: optional string`

      Tagged ID of the user who performed the action.

  - `ExtraUsageSpendLimitDeleted object { actor, id, created_at, 5 more }`

    Usage credit spend limit was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }  or object { api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `spend_limit_id: optional string`

      Tagged ID of the spend limit.

    - `type: optional "extra_usage_spend_limit_deleted"`

      - `"extra_usage_spend_limit_deleted"`

    - `user_id: optional string`

      Tagged ID of the user who performed the action.

  - `ExtraUsageSpendLimitIncreaseRequestApproved object { actor, id, amount, 7 more }`

    A usage credit spend limit increase request was approved.

    - `actor: object { api_key_id, ip_address, user_agent, type }`

      - `api_key_id: string`

      - `ip_address: string`

      - `user_agent: string`

      - `type: optional "api_actor"`

        - `"api_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `amount: optional number`

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `requester_user_id: optional string`

    - `spend_limit_id: optional string`

    - `spend_limit_increase_request_id: optional string`

    - `type: optional "extra_usage_spend_limit_increase_request_approved"`

      - `"extra_usage_spend_limit_increase_request_approved"`

  - `ExtraUsageSpendLimitIncreaseRequestDenied object { actor, id, created_at, 5 more }`

    A usage credit spend limit increase request was denied.

    - `actor: object { api_key_id, ip_address, user_agent, type }`

      - `api_key_id: string`

      - `ip_address: string`

      - `user_agent: string`

      - `type: optional "api_actor"`

        - `"api_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `requester_user_id: optional string`

    - `spend_limit_increase_request_id: optional string`

    - `type: optional "extra_usage_spend_limit_increase_request_denied"`

      - `"extra_usage_spend_limit_increase_request_denied"`

  - `ExtraUsageSpendLimitUpdated object { actor, id, amount, 8 more }`

    Usage credit spend limit was updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }  or object { api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `amount: optional number`

      The new monthly credit limit amount in minor units (e.g. cents).

    - `created_at: optional string`

      When this activity occurred.

    - `is_enabled: optional boolean`

      Whether the spend limit is enabled.

    - `limit_type: optional string`

      The type of spend limit updated (e.g. organization, seat_tier, member, service, group).

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `spend_limit_id: optional string`

      Tagged ID of the spend limit.

    - `type: optional "extra_usage_spend_limit_updated"`

      - `"extra_usage_spend_limit_updated"`

    - `user_id: optional string`

      Tagged ID of the user who performed the action.

  - `ClaudeFileAccessFailed object { actor, claude_file_id, filename, 7 more }`

    An attempt to access a file failed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `claude_file_id: string`

    - `filename: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `claude_artifact_id: optional string`

      Artifact ID if file was accessed via an artifact

    - `claude_project_id: optional string`

      Project ID if file was accessed via a project

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_file_access_failed"`

      - `"claude_file_access_failed"`

  - `ClaudeFileDeleted object { actor, claude_file_id, filename, 5 more }`

    A file was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_file_id: string`

    - `filename: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_file_deleted"`

      - `"claude_file_deleted"`

  - `ClaudeFileUploaded object { actor, claude_file_id, filename, 7 more }`

    A file was uploaded.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_file_id: string`

    - `filename: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `claude_chat_id: optional string`

      Chat ID if file was uploaded to a chat

    - `claude_project_id: optional string`

      Project ID if file was uploaded to a project

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_file_uploaded"`

      - `"claude_file_uploaded"`

  - `ClaudeFileViewed object { actor, claude_file_id, filename, 7 more }`

    A file was viewed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_file_id: string`

    - `filename: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `claude_artifact_id: optional string`

      Artifact ID if file was accessed via an artifact

    - `claude_project_id: optional string`

      Project ID if file was accessed via a project

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_file_viewed"`

      - `"claude_file_viewed"`

  - `GheConfigurationCreated object { actor, ghe_configuration_id, id, 4 more }`

    Admin created a GHE configuration.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `ghe_configuration_id: string`

      ID of the GHE configuration

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "ghe_configuration_created"`

      - `"ghe_configuration_created"`

  - `GheConfigurationDeleted object { actor, ghe_configuration_id, id, 4 more }`

    Admin deleted a GHE configuration.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `ghe_configuration_id: string`

      ID of the GHE configuration

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "ghe_configuration_deleted"`

      - `"ghe_configuration_deleted"`

  - `GheConfigurationUpdated object { actor, ghe_configuration_id, id, 4 more }`

    Admin updated a GHE configuration.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `ghe_configuration_id: string`

      ID of the GHE configuration

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "ghe_configuration_updated"`

      - `"ghe_configuration_updated"`

  - `GheUserConnected object { actor, id, created_at, 4 more }`

    User connected to a GHE instance.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `ghe_configuration_id: optional string`

      ID of the GHE configuration

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "ghe_user_connected"`

      - `"ghe_user_connected"`

  - `GheUserDisconnected object { actor, id, created_at, 4 more }`

    User disconnected from a GHE instance.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `ghe_configuration_id: optional string`

      ID of the GHE configuration

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "ghe_user_disconnected"`

      - `"ghe_user_disconnected"`

  - `GheWebhookSignatureInvalid object { actor, ghe_configuration_id, id, 4 more }`

    Webhook signature validation failed.

    - `actor: object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `ip_address: string`

      - `user_agent: string`

      - `type: optional "unauthenticated_user_actor"`

        - `"unauthenticated_user_actor"`

      - `unauthenticated_email_address: optional string`

    - `ghe_configuration_id: string`

      ID of the GHE configuration

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "ghe_webhook_signature_invalid"`

      - `"ghe_webhook_signature_invalid"`

  - `ClaudeGitHubIntegrationCreated object { actor, integration_id, id, 6 more }`

    A GitHub integration was enabled for the organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `integration_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_name: optional string`

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `repository_name: optional string`

    - `type: optional "claude_github_integration_created"`

      - `"claude_github_integration_created"`

  - `ClaudeGitHubIntegrationDeleted object { actor, integration_id, id, 6 more }`

    A GitHub integration was disabled for the organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `integration_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_name: optional string`

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `repository_name: optional string`

    - `type: optional "claude_github_integration_deleted"`

      - `"claude_github_integration_deleted"`

  - `ClaudeGitHubIntegrationUpdated object { actor, integration_id, id, 6 more }`

    A GitHub integration's configuration was updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `integration_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_name: optional string`

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `repository_name: optional string`

    - `type: optional "claude_github_integration_updated"`

      - `"claude_github_integration_updated"`

  - `ClaudeGdriveIntegrationCreated object { actor, integration_id, id, 5 more }`

    A Google Drive integration was enabled for the organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `integration_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `folder_id: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_gdrive_integration_created"`

      - `"claude_gdrive_integration_created"`

  - `ClaudeGdriveIntegrationDeleted object { actor, integration_id, id, 5 more }`

    A Google Drive integration was disabled for the organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `integration_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `folder_id: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_gdrive_integration_deleted"`

      - `"claude_gdrive_integration_deleted"`

  - `ClaudeGdriveIntegrationUpdated object { actor, integration_id, id, 5 more }`

    A Google Drive integration's configuration was updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `integration_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `folder_id: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_gdrive_integration_updated"`

      - `"claude_gdrive_integration_updated"`

  - `GroupCreated object { actor, group_id, group_name, 5 more }`

    A group was created (RBAC admin or SCIM provisioning).

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }  or object { directory_id, workos_event_id, idp_connection_type, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

    - `group_id: string`

      Tagged ID of the created group

    - `group_name: string`

      Name of the created group

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "group_created"`

      - `"group_created"`

  - `GroupDeleted object { actor, group_id, id, 4 more }`

    A group was deleted (RBAC admin or SCIM provisioning).

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }  or object { directory_id, workos_event_id, idp_connection_type, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

    - `group_id: string`

      Tagged ID of the deleted group

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "group_deleted"`

      - `"group_deleted"`

  - `GroupListViewed object { actor, id, created_at, 3 more }`

    Admin viewed the list of RBAC groups.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "group_list_viewed"`

      - `"group_list_viewed"`

  - `GroupMemberAdded object { actor, group_id, member_ids, 5 more }`

    One or more members were added to a group.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }  or object { directory_id, workos_event_id, idp_connection_type, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

    - `group_id: string`

      Tagged ID of the group

    - `member_ids: array of string`

      Tagged IDs of the members added

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "group_member_added"`

      - `"group_member_added"`

  - `GroupMemberListViewed object { actor, group_id, id, 4 more }`

    Admin viewed the members of an RBAC group.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `group_id: string`

      Tagged ID of the group

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "group_member_list_viewed"`

      - `"group_member_list_viewed"`

  - `GroupMemberRemoved object { actor, group_id, member_ids, 5 more }`

    One or more members were removed from a group.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }  or object { directory_id, workos_event_id, idp_connection_type, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

    - `group_id: string`

      Tagged ID of the group

    - `member_ids: array of string`

      Tagged IDs of the members removed

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "group_member_removed"`

      - `"group_member_removed"`

  - `GroupUpdated object { actor, group_id, id, 4 more }`

    A group was updated (RBAC admin or SCIM provisioning).

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }  or object { directory_id, workos_event_id, idp_connection_type, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

    - `group_id: string`

      Tagged ID of the updated group

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "group_updated"`

      - `"group_updated"`

  - `GroupViewed object { actor, group_id, id, 4 more }`

    A group was viewed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

    - `group_id: string`

      Tagged ID of the viewed group

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "group_viewed"`

      - `"group_viewed"`

  - `IntegrationUserConnected object { actor, id, created_at, 4 more }`

    User connected to an integration.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `integration_type: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "integration_user_connected"`

      - `"integration_user_connected"`

  - `IntegrationUserDisconnected object { actor, id, created_at, 4 more }`

    User disconnected from an integration.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `integration_type: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "integration_user_disconnected"`

      - `"integration_user_disconnected"`

  - `InvoiceCollectionMethodUpdated object { actor, id, created_at, 4 more }`

    Invoice collection method was changed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `new_collection_method: optional string`

      New collection method (e.g. charge_automatically, send_invoice).

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "invoice_collection_method_updated"`

      - `"invoice_collection_method_updated"`

  - `UserLoggedOut object { actor, id, created_at, 3 more }`

    A user signed out of one or all sessions.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "user_logged_out"`

      - `"user_logged_out"`

  - `LtiLaunchInitiated object { actor, id, created_at, 3 more }`

    LTI launch was initiated.

    - `actor: object { ip_address, user_agent, type, unauthenticated_email_address }  or object { email_address, ip_address, user_agent, 2 more }`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "lti_launch_initiated"`

      - `"lti_launch_initiated"`

  - `LtiLaunchSuccess object { actor, id, created_at, 3 more }`

    LTI launch completed successfully.

    - `actor: object { ip_address, user_agent, type, unauthenticated_email_address }  or object { email_address, ip_address, user_agent, 2 more }`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "lti_launch_success"`

      - `"lti_launch_success"`

  - `LtiPlatformCreated object { actor, lti_platform_id, lti_platform_issuer, 5 more }`

    Admin created an LTI platform integration.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `lti_platform_id: string`

      UUID of the LTI platform

    - `lti_platform_issuer: string`

      Platform issuer URL

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "lti_platform_created"`

      - `"lti_platform_created"`

  - `LtiPlatformUpdated object { actor, lti_platform_id, id, 5 more }`

    Admin updated an LTI platform integration.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `lti_platform_id: string`

      UUID of the LTI platform

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `lti_platform_issuer: optional string`

      Platform issuer URL

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "lti_platform_updated"`

      - `"lti_platform_updated"`

  - `MagicLinkLoginFailed object { actor, id, created_at, 3 more }`

    A magic link sign-in attempt failed.

    - `actor: object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `ip_address: string`

      - `user_agent: string`

      - `type: optional "unauthenticated_user_actor"`

        - `"unauthenticated_user_actor"`

      - `unauthenticated_email_address: optional string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "magic_link_login_failed"`

      - `"magic_link_login_failed"`

  - `MagicLinkLoginInitiated object { actor, id, created_at, 3 more }`

    A user requested a magic link sign-in email.

    - `actor: object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `ip_address: string`

      - `user_agent: string`

      - `type: optional "unauthenticated_user_actor"`

        - `"unauthenticated_user_actor"`

      - `unauthenticated_email_address: optional string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "magic_link_login_initiated"`

      - `"magic_link_login_initiated"`

  - `MagicLinkLoginSucceeded object { actor, id, auth_method, 5 more }`

    A user successfully signed in with a magic link email.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `auth_method: optional "magic_link"`

      The method the user used to authenticate. May be absent on activities recorded before this field was introduced.

      - `"magic_link"`

    - `created_at: optional string`

      When this activity occurred.

    - `mfa_method: optional "not_used"`

      The second authentication factor performed during this login, if any. `null` when the second-factor status is not recorded on this event — for example, when authentication was delegated to an external identity provider and any second factor is not visible to Anthropic, or when this event is one step of a multi-step login whose MFA is reported on another activity. May be absent on activities recorded before this field was introduced.

      - `"not_used"`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "magic_link_login_succeeded"`

      - `"magic_link_login_succeeded"`

  - `ManagedOrganizationSetupCompleted object { actor, id, created_at, 3 more }`

    Managed (AWS Marketplace) organization setup was completed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "managed_organization_setup_completed"`

      - `"managed_organization_setup_completed"`

  - `MarketplaceCreated object { actor, marketplace_id, id, 4 more }`

    Admin created an organization marketplace.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `marketplace_id: string`

      Tagged ID of the marketplace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "marketplace_created"`

      - `"marketplace_created"`

  - `MarketplaceDeleted object { actor, marketplace_id, id, 4 more }`

    Admin deleted an organization marketplace.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `marketplace_id: string`

      Tagged ID of the marketplace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "marketplace_deleted"`

      - `"marketplace_deleted"`

  - `MarketplaceUpdated object { actor, marketplace_id, id, 4 more }`

    Admin updated an organization marketplace.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `marketplace_id: string`

      Tagged ID of the marketplace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "marketplace_updated"`

      - `"marketplace_updated"`

  - `MarketplaceWebhookDeleted object { actor, marketplace_id, id, 4 more }`

    Admin removed the GitHub push webhook for a marketplace.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `marketplace_id: string`

      Tagged ID of the marketplace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "marketplace_webhook_deleted"`

      - `"marketplace_webhook_deleted"`

  - `MarketplaceWebhookProvisioned object { actor, marketplace_id, id, 5 more }`

    Admin provisioned a GitHub push webhook for a marketplace.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `marketplace_id: string`

      Tagged ID of the marketplace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `github_webhook_id: optional number`

      GitHub-assigned webhook ID returned by the hooks API

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "marketplace_webhook_provisioned"`

      - `"marketplace_webhook_provisioned"`

  - `McpServerCreated object { actor, mcp_server_id, mcp_server_name, 5 more }`

    An MCP server was added to the organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `mcp_server_id: string`

      Tagged ID of the MCP server

    - `mcp_server_name: string`

      Display name of the MCP server

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "mcp_server_created"`

      - `"mcp_server_created"`

  - `McpServerDeleted object { actor, mcp_server_id, mcp_server_name, 5 more }`

    An MCP server was removed from the organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `mcp_server_id: string`

      Tagged ID of the MCP server

    - `mcp_server_name: string`

      Display name of the MCP server

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "mcp_server_deleted"`

      - `"mcp_server_deleted"`

  - `McpServerUpdated object { actor, mcp_server_id, mcp_server_name, 5 more }`

    An MCP server's configuration was updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `mcp_server_id: string`

      Tagged ID of the MCP server

    - `mcp_server_name: string`

      Display name of the MCP server

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "mcp_server_updated"`

      - `"mcp_server_updated"`

  - `McpToolPolicyUpdated object { actor, max_permission, mcp_server_id, 7 more }`

    The permission restriction for an MCP tool was set or cleared.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `max_permission: string`

      New max_permission value ('allow' | 'ask' | 'blocked'), or null when cleared

    - `mcp_server_id: string`

      Tagged ID of the MCP server

    - `mcp_server_name: string`

      Display name of the MCP server

    - `tool_name: string`

      Tool name (or '*' for the MCP-server-wide default)

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "mcp_tool_policy_updated"`

      - `"mcp_tool_policy_updated"`

  - `OrgAnalyticsAPICapabilityUpdated object { actor, id, created_at, 3 more }`

    Organization analytics_api capability was enabled or disabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_analytics_api_capability_updated"`

      - `"org_analytics_api_capability_updated"`

  - `OrgBulkDeleteInitiated object { actor, id, created_at, 3 more }`

    Organization bulk deletion was initiated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_bulk_delete_initiated"`

      - `"org_bulk_delete_initiated"`

  - `OrgClaudeCodeDataSharingDisabled object { actor, id, created_at, 3 more }`

    Organization Claude Code data sharing was disabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_claude_code_data_sharing_disabled"`

      - `"org_claude_code_data_sharing_disabled"`

  - `OrgClaudeCodeDataSharingEnabled object { actor, id, created_at, 3 more }`

    Organization Claude Code data sharing was enabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_claude_code_data_sharing_enabled"`

      - `"org_claude_code_data_sharing_enabled"`

  - `OrgClaudeCodeDesktopDisabled object { actor, id, created_at, 3 more }`

    Organization Claude Code Desktop was disabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_claude_code_desktop_disabled"`

      - `"org_claude_code_desktop_disabled"`

  - `OrgClaudeCodeDesktopEnabled object { actor, id, created_at, 3 more }`

    Organization Claude Code Desktop was enabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_claude_code_desktop_enabled"`

      - `"org_claude_code_desktop_enabled"`

  - `OrgComplianceAPISettingsUpdated object { actor, id, compliance_api_enabled, 5 more }`

    Organization compliance API settings were updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }  or object { admin_api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `compliance_api_enabled: optional boolean`

    - `compliance_api_logging_enabled: optional boolean`

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_compliance_api_settings_updated"`

      - `"org_compliance_api_settings_updated"`

  - `OrgCoworkAgentDisabled object { actor, id, created_at, 3 more }`

    Organization Cowork Agent was disabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_cowork_agent_disabled"`

      - `"org_cowork_agent_disabled"`

  - `OrgCoworkAgentEnabled object { actor, id, created_at, 3 more }`

    Organization Cowork Agent was enabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_cowork_agent_enabled"`

      - `"org_cowork_agent_enabled"`

  - `OrgCoworkDisabled object { actor, id, created_at, 3 more }`

    Organization cowork was disabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_cowork_disabled"`

      - `"org_cowork_disabled"`

  - `OrgCoworkEnabled object { actor, id, created_at, 3 more }`

    Organization cowork was enabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_cowork_enabled"`

      - `"org_cowork_enabled"`

  - `OrgCreationBlocked object { actor, id, created_at, 4 more }`

    Organization creation was blocked.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `reason: optional string`

    - `type: optional "org_creation_blocked"`

      - `"org_creation_blocked"`

  - `OrgDataExportAccessed object { actor, id, created_at, 3 more }`

    Organization data export file was accessed/downloaded via signed URL.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_data_export_accessed"`

      - `"org_data_export_accessed"`

  - `OrgDataExportCompleted object { actor, id, created_at, 3 more }`

    Organization data export was completed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_data_export_completed"`

      - `"org_data_export_completed"`

  - `OrgDataExportStarted object { actor, id, created_at, 3 more }`

    Organization data export was started.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_data_export_started"`

      - `"org_data_export_started"`

  - `OrgDeletedViaBulk object { actor, id, created_at, 3 more }`

    Organization was deleted via bulk operation.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_deleted_via_bulk"`

      - `"org_deleted_via_bulk"`

  - `OrgDeletionRequested object { actor, id, created_at, 3 more }`

    Organization deletion was requested.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_deletion_requested"`

      - `"org_deletion_requested"`

  - `OrgDirectoryResyncCompleted object { actor, resync_uuid, id, 4 more }`

    Organization directory resync completed successfully.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `resync_uuid: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_directory_resync_completed"`

      - `"org_directory_resync_completed"`

  - `OrgDirectoryResyncFailed object { actor, resync_uuid, id, 4 more }`

    Organization directory resync failed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `resync_uuid: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_directory_resync_failed"`

      - `"org_directory_resync_failed"`

  - `OrgDirectoryResyncStarted object { actor, resync_uuid, sync_destinations, 5 more }`

    Organization directory resync was started asynchronously.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `resync_uuid: string`

    - `sync_destinations: array of string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_directory_resync_started"`

      - `"org_directory_resync_started"`

  - `OrgDirectorySyncActivated object { actor, id, created_at, 3 more }`

    Organization directory sync was activated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }  or object { directory_id, workos_event_id, idp_connection_type, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_directory_sync_activated"`

      - `"org_directory_sync_activated"`

  - `OrgDirectorySyncAddInitiated object { actor, id, created_at, 3 more }`

    Organization directory sync setup was initiated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_directory_sync_add_initiated"`

      - `"org_directory_sync_add_initiated"`

  - `OrgDirectorySyncDeleted object { actor, id, created_at, 3 more }`

    Organization directory sync was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }  or object { directory_id, workos_event_id, idp_connection_type, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_directory_sync_deleted"`

      - `"org_directory_sync_deleted"`

  - `OrgDiscoverabilityDisabled object { actor, id, created_at, 3 more }`

    Admin disabled organization discoverability.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_discoverability_disabled"`

      - `"org_discoverability_disabled"`

  - `OrgDiscoverabilityEnabled object { actor, id, created_at, 3 more }`

    Admin enabled organization discoverability.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_discoverability_enabled"`

      - `"org_discoverability_enabled"`

  - `OrgDiscoverabilitySettingsUpdated object { actor, id, created_at, 3 more }`

    Admin updated organization discoverability settings.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_discoverability_settings_updated"`

      - `"org_discoverability_settings_updated"`

  - `OrgDomainAddInitiated object { actor, id, created_at, 3 more }`

    Organization domain verification was initiated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_domain_add_initiated"`

      - `"org_domain_add_initiated"`

  - `OrgDomainRemoved object { actor, id, created_at, 4 more }`

    Organization domain was removed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `domain: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_domain_removed"`

      - `"org_domain_removed"`

  - `OrgDomainVerified object { actor, id, created_at, 4 more }`

    Organization domain was verified.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `domain: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_domain_verified"`

      - `"org_domain_verified"`

  - `OrgHipaaSelfServeEnabled object { actor, baa_content_hash, baa_version_label, 6 more }`

    A primary owner click-accepted the BAA and enabled HIPAA protections
    for the organization via the self-serve flow.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `baa_content_hash: string`

    - `baa_version_label: string`

    - `setup_guide_content_hash: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_hipaa_self_serve_enabled"`

      - `"org_hipaa_self_serve_enabled"`

  - `OrgIPRestrictionCreated object { actor, id, created_at, 3 more }`

    Organization IP restriction was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_ip_restriction_created"`

      - `"org_ip_restriction_created"`

  - `OrgIPRestrictionDeleted object { actor, id, created_at, 3 more }`

    Organization IP restriction was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_ip_restriction_deleted"`

      - `"org_ip_restriction_deleted"`

  - `OrgIPRestrictionUpdated object { actor, id, created_at, 3 more }`

    Organization IP restriction was updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_ip_restriction_updated"`

      - `"org_ip_restriction_updated"`

  - `OrgInviteLinkDisabled object { actor, id, created_at, 3 more }`

    Organization invite link was disabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_invite_link_disabled"`

      - `"org_invite_link_disabled"`

  - `OrgInviteLinkGenerated object { actor, id, created_at, 3 more }`

    Organization invite link was generated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_invite_link_generated"`

      - `"org_invite_link_generated"`

  - `OrgInviteLinkRegenerated object { actor, id, created_at, 3 more }`

    Organization invite link was regenerated (previous link invalidated).

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_invite_link_regenerated"`

      - `"org_invite_link_regenerated"`

  - `OrgInviteViewed object { actor, invite_id, id, 4 more }`

    An organization invite was viewed.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `invite_id: string`

      Tagged ID of the viewed invite

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_invite_viewed"`

      - `"org_invite_viewed"`

  - `OrgInvitesListed object { actor, id, created_at, 3 more }`

    Organization invites were listed.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_invites_listed"`

      - `"org_invites_listed"`

  - `OrgJoinProposalDecided object { actor, approved, id, 4 more }`

    Approve or reject decision on a parent-org join proposal.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `approved: boolean`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_join_proposal_decided"`

      - `"org_join_proposal_decided"`

  - `OrgJoinRequestApproved object { actor, id, created_at, 3 more }`

    Admin approved a join request.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_join_request_approved"`

      - `"org_join_request_approved"`

  - `OrgJoinRequestCreated object { actor, id, created_at, 3 more }`

    User requested to join an organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_join_request_created"`

      - `"org_join_request_created"`

  - `OrgJoinRequestDismissed object { actor, id, created_at, 3 more }`

    Admin dismissed a join request.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_join_request_dismissed"`

      - `"org_join_request_dismissed"`

  - `OrgJoinRequestInstantApproved object { actor, id, created_at, 3 more }`

    Join request was instantly approved.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_join_request_instant_approved"`

      - `"org_join_request_instant_approved"`

  - `OrgJoinRequestsBulkDismissed object { actor, id, created_at, 3 more }`

    Admin bulk-dismissed join requests.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_join_requests_bulk_dismissed"`

      - `"org_join_requests_bulk_dismissed"`

  - `OrgMagicLinkSecondFactorToggled object { actor, enabled, id, 4 more }`

    Organization magic link second factor was toggled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `enabled: boolean`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_magic_link_second_factor_toggled"`

      - `"org_magic_link_second_factor_toggled"`

  - `OrgMemberInvitesDisabled object { actor, id, created_at, 3 more }`

    Admin disabled member invites for the organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_member_invites_disabled"`

      - `"org_member_invites_disabled"`

  - `OrgMemberInvitesEnabled object { actor, id, created_at, 3 more }`

    Admin enabled member invites for the organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_member_invites_enabled"`

      - `"org_member_invites_enabled"`

  - `OrgMembersExported object { actor, id, created_at, 3 more }`

    Organization members list was exported as CSV.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_members_exported"`

      - `"org_members_exported"`

  - `OrgParentJoinProposalCreated object { actor, id, created_at, 3 more }`

    Organization parent join proposal was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_parent_join_proposal_created"`

      - `"org_parent_join_proposal_created"`

  - `OrgParentSearchPerformed object { actor, id, created_at, 3 more }`

    Organization parent search was performed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_parent_search_performed"`

      - `"org_parent_search_performed"`

  - `OrgSSOAddInitiated object { actor, id, created_at, 3 more }`

    Organization SSO setup was initiated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_sso_add_initiated"`

      - `"org_sso_add_initiated"`

  - `OrgSSOConnectionActivated object { actor, id, connection_id, 5 more }`

    Organization SSO connection was activated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }  or object { directory_id, workos_event_id, idp_connection_type, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `connection_id: optional string`

    - `connection_type: optional string`

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_sso_connection_activated"`

      - `"org_sso_connection_activated"`

  - `OrgSSOConnectionDeactivated object { actor, id, connection_id, 4 more }`

    Organization SSO connection was deactivated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }  or object { directory_id, workos_event_id, idp_connection_type, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `connection_id: optional string`

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_sso_connection_deactivated"`

      - `"org_sso_connection_deactivated"`

  - `OrgSSOConnectionDeleted object { actor, id, connection_id, 4 more }`

    Organization SSO connection was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }  or object { directory_id, workos_event_id, idp_connection_type, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `connection_id: optional string`

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_sso_connection_deleted"`

      - `"org_sso_connection_deleted"`

  - `OrgSSOGroupRoleMappingsUpdated object { actor, id, created_at, 3 more }`

    Organization SSO group role mappings were updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_sso_group_role_mappings_updated"`

      - `"org_sso_group_role_mappings_updated"`

  - `OrgSSOProvisioningModeChanged object { actor, id, created_at, 5 more }`

    Organization SSO provisioning mode was changed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `new_mode: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `previous_mode: optional string`

    - `type: optional "org_sso_provisioning_mode_changed"`

      - `"org_sso_provisioning_mode_changed"`

  - `OrgSSOSeatTierAssignmentToggled object { actor, enabled, id, 4 more }`

    Organization SSO seat tier assignment was toggled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `enabled: boolean`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_sso_seat_tier_assignment_toggled"`

      - `"org_sso_seat_tier_assignment_toggled"`

  - `OrgSSOSeatTierMappingsUpdated object { actor, id, created_at, 3 more }`

    Organization SSO seat tier mappings were updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_sso_seat_tier_mappings_updated"`

      - `"org_sso_seat_tier_mappings_updated"`

  - `OrgSSOToggled object { actor, enabled, id, 4 more }`

    Organization SSO was toggled on or off.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `enabled: boolean`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_sso_toggled"`

      - `"org_sso_toggled"`

  - `OrgSyncDeletingSynchronizedFilesStarted object { actor, id, created_at, 3 more }`

    Organization started deleting synchronized files.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_sync_deleting_synchronized_files_started"`

      - `"org_sync_deleting_synchronized_files_started"`

  - `OrgSyncSynchronizedFilesDeleted object { actor, id, created_at, 3 more }`

    Organization synchronized files were deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_sync_synchronized_files_deleted"`

      - `"org_sync_synchronized_files_deleted"`

  - `OrgTaintAdded object { actor, id, created_at, 4 more }`

    A taint was added to an organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `taint: optional string`

    - `type: optional "org_taint_added"`

      - `"org_taint_added"`

  - `OrgTaintRemoved object { actor, id, created_at, 4 more }`

    A taint was removed from an organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `taint: optional string`

    - `type: optional "org_taint_removed"`

      - `"org_taint_removed"`

  - `OrgUserDeleted object { actor, id, created_at, 5 more }`

    User was removed from organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }  or object { admin_api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `deleted_user_email: optional string`

    - `deleted_user_id: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_user_deleted"`

      - `"org_user_deleted"`

  - `OrgUserInviteAccepted object { actor, id, created_at, 4 more }`

    Organization user invite was accepted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `invite_id: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_user_invite_accepted"`

      - `"org_user_invite_accepted"`

  - `OrgUserInviteDeleted object { actor, id, created_at, 4 more }`

    Organization user invite was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }  or object { admin_api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `invite_id: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_user_invite_deleted"`

      - `"org_user_invite_deleted"`

  - `OrgUserInviteReSent object { actor, id, created_at, 4 more }`

    Organization user invite was re-sent.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `invited_email: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_user_invite_re_sent"`

      - `"org_user_invite_re_sent"`

  - `OrgUserInviteRejected object { actor, id, created_at, 4 more }`

    Organization user invite was rejected.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `invite_id: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_user_invite_rejected"`

      - `"org_user_invite_rejected"`

  - `OrgUserInviteSent object { actor, id, created_at, 5 more }`

    Organization user invite was sent.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }  or object { admin_api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `invited_email: optional string`

    - `invited_role: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_user_invite_sent"`

      - `"org_user_invite_sent"`

  - `OrgUserLeft object { actor, id, created_at, 4 more }`

    User removed themselves from organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `previous_role: optional string`

    - `type: optional "org_user_left"`

      - `"org_user_left"`

  - `OrgUserViewed object { actor, user_id, id, 4 more }`

    An organization user was viewed.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `user_id: string`

      Tagged ID of the viewed user

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_user_viewed"`

      - `"org_user_viewed"`

  - `OrgUsersListed object { actor, id, created_at, 3 more }`

    Organization users were listed.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_users_listed"`

      - `"org_users_listed"`

  - `OrgWorkAcrossAppsDisabled object { actor, id, created_at, 3 more }`

    Organization Work Across Apps was disabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_work_across_apps_disabled"`

      - `"org_work_across_apps_disabled"`

  - `OrgWorkAcrossAppsEnabled object { actor, id, created_at, 3 more }`

    Organization Work Across Apps was enabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_work_across_apps_enabled"`

      - `"org_work_across_apps_enabled"`

  - `OrganizationAddressUpdated object { actor, id, billing_address_updated, 7 more }`

    The organization's billing or shipping address was updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `billing_address_updated: optional boolean`

    - `billing_name_updated: optional boolean`

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `shipping_address_updated: optional boolean`

    - `shipping_name_updated: optional boolean`

    - `type: optional "organization_address_updated"`

      - `"organization_address_updated"`

  - `OrganizationIconDeleted object { actor, id, created_at, 3 more }`

    Organization's custom icon deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "organization_icon_deleted"`

      - `"organization_icon_deleted"`

  - `OrganizationIconUpdated object { actor, id, created_at, 3 more }`

    Organization's custom icon uploaded or replaced.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "organization_icon_updated"`

      - `"organization_icon_updated"`

  - `ClaudeOrganizationSettingsUpdated object { actor, updates, id, 4 more }`

    Organization settings were updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `updates: array of object { current_value, previous_value, type }  or object { current_value, previous_value, type }  or object { current_value, previous_value, type }  or 38 more`

      - `OrganizationName object { current_value, previous_value, type }`

        - `current_value: string`

        - `previous_value: string`

        - `type: optional "name"`

          - `"name"`

      - `OrganizationCapabilities object { current_value, previous_value, type }`

        - `current_value: array of string`

        - `previous_value: array of string`

        - `type: optional "capabilities"`

          - `"capabilities"`

      - `OrganizationRedactContent object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "redact_content"`

          - `"redact_content"`

      - `PublicProjectsEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "public_projects_enabled"`

          - `"public_projects_enabled"`

      - `WebSearchEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "web_search_enabled"`

          - `"web_search_enabled"`

      - `GeolocationEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "geolocation_enabled"`

          - `"geolocation_enabled"`

      - `OrgMemoryEnabledSetting object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "enabled_saffron"`

          - `"enabled_saffron"`

      - `DataRetentionPeriods object { current_value, previous_value, type }`

        - `current_value: array of object { data_type, duration, timescale }`

          - `data_type: "all" or "chat" or "project"`

            - `"all"`

            - `"chat"`

            - `"project"`

          - `duration: number`

          - `timescale: "day" or "indefinite" or "month"`

            - `"day"`

            - `"indefinite"`

            - `"month"`

        - `previous_value: array of object { data_type, duration, timescale }`

          - `data_type: "all" or "chat" or "project"`

            - `"all"`

            - `"chat"`

            - `"project"`

          - `duration: number`

          - `timescale: "day" or "indefinite" or "month"`

            - `"day"`

            - `"indefinite"`

            - `"month"`

        - `type: optional "data_retention_periods"`

          - `"data_retention_periods"`

      - `MembersLimit object { current_value, previous_value, type }`

        - `current_value: number`

        - `previous_value: number`

        - `type: optional "members_limit"`

          - `"members_limit"`

      - `ClaudeAPIInArtifactsEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "claude_api_in_artifacts_enabled"`

          - `"claude_api_in_artifacts_enabled"`

      - `WorkbenchCompletionFeedbackEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "workbench_completion_feedback_enabled"`

          - `"workbench_completion_feedback_enabled"`

      - `ClaudeAICompletionFeedbackEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "claude_ai_completion_feedback_enabled"`

          - `"claude_ai_completion_feedback_enabled"`

      - `ClaudeAIIntegrationSharingEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "claude_ai_integration_sharing_enabled"`

          - `"claude_ai_integration_sharing_enabled"`

      - `ClaudeAIChatSharingEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "claude_ai_chat_sharing_enabled"`

          - `"claude_ai_chat_sharing_enabled"`

      - `ClaudeAiccrSharingEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "claude_ai_ccr_sharing_enabled"`

          - `"claude_ai_ccr_sharing_enabled"`

      - `BatchesDownloadUiVisibility object { current_value, previous_value, type }`

        - `current_value: "all" or "none" or "selected"`

          - `"all"`

          - `"none"`

          - `"selected"`

        - `previous_value: "all" or "none" or "selected"`

          - `"all"`

          - `"none"`

          - `"selected"`

        - `type: optional "batches_download_ui_visibility"`

          - `"batches_download_ui_visibility"`

      - `AllowedInviteDomains object { current_value, previous_value, type }`

        - `current_value: array of string`

        - `previous_value: array of string`

        - `type: optional "allowed_invite_domains"`

          - `"allowed_invite_domains"`

      - `WebSearchAPISettingsChanged object { current_value, previous_value, type }`

        - `current_value: object { domain_filters, is_enabled }`

          - `domain_filters: object { allowed_domains, blocked_domains }`

            Allowed/blocked domain filters shared by web_search and web_fetch tools.

            - `allowed_domains: optional array of string`

            - `blocked_domains: optional array of string`

          - `is_enabled: boolean`

        - `previous_value: object { domain_filters, is_enabled }`

          - `domain_filters: object { allowed_domains, blocked_domains }`

            Allowed/blocked domain filters shared by web_search and web_fetch tools.

            - `allowed_domains: optional array of string`

            - `blocked_domains: optional array of string`

          - `is_enabled: boolean`

        - `type: optional "web_search_api_settings"`

          - `"web_search_api_settings"`

      - `WebFetchAPISettingsChanged object { current_value, previous_value, type }`

        - `current_value: object { domain_filters, is_enabled }`

          - `domain_filters: object { allowed_domains, blocked_domains }`

            Allowed/blocked domain filters shared by web_search and web_fetch tools.

            - `allowed_domains: optional array of string`

            - `blocked_domains: optional array of string`

          - `is_enabled: boolean`

        - `previous_value: object { domain_filters, is_enabled }`

          - `domain_filters: object { allowed_domains, blocked_domains }`

            Allowed/blocked domain filters shared by web_search and web_fetch tools.

            - `allowed_domains: optional array of string`

            - `blocked_domains: optional array of string`

          - `is_enabled: boolean`

        - `type: optional "web_fetch_api_settings"`

          - `"web_fetch_api_settings"`

      - `DefaultWorkspaceSettings object { current_value, previous_value, type }`

        - `current_value: object { enable_api_keys }`

          - `enable_api_keys: optional boolean`

        - `previous_value: object { enable_api_keys }`

          - `enable_api_keys: optional boolean`

        - `type: optional "default_workspace_settings"`

          - `"default_workspace_settings"`

      - `BatchesDownloadUiEnabledWorkspaceIDs object { current_value, previous_value, type }`

        - `current_value: array of string`

        - `previous_value: array of string`

        - `type: optional "batches_download_ui_enabled_workspace_ids"`

          - `"batches_download_ui_enabled_workspace_ids"`

      - `ClaudeCodeManagedSettings object { current_value, current_version, previous_value, 3 more }`

        The organization's Claude Code managed settings were changed.

        The full previous and current settings content is provided in the
        `previous_value` and `current_value` fields.

        - `current_value: optional map[unknown]`

        - `current_version: optional number`

        - `previous_value: optional map[unknown]`

        - `previous_version: optional number`

        - `settings_uuid: optional string`

        - `type: optional "claude_code_managed_settings"`

          - `"claude_code_managed_settings"`

      - `AccountSessionDurationSeconds object { current_value, previous_value, type }`

        Tracks changes to the enterprise account session duration setting (in seconds).

        - `current_value: number`

        - `previous_value: number`

        - `type: optional "account_session_duration_seconds"`

          - `"account_session_duration_seconds"`

      - `VcsConnections object { current_value, previous_value, type }`

        Tracks changes to VCS (GitHub, etc.) organization connections.

        - `current_value: array of object { org_name, type, metadata, org_id }`

          - `org_name: string`

          - `type: "github"`

            Supported Version Control System providers.

            - `"github"`

          - `metadata: optional map[string]`

          - `org_id: optional string`

        - `previous_value: array of object { org_name, type, metadata, org_id }`

          - `org_name: string`

          - `type: "github"`

            Supported Version Control System providers.

            - `"github"`

          - `metadata: optional map[string]`

          - `org_id: optional string`

        - `type: optional "vcs_connections"`

          - `"vcs_connections"`

      - `DisabledAdminRequestTypes object { current_value, previous_value, type }`

        Tracks changes to which admin request types are disabled.

        - `current_value: array of string`

        - `previous_value: array of string`

        - `type: optional "disabled_admin_request_types"`

          - `"disabled_admin_request_types"`

      - `CodeExecutionNetworkEgressEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "code_execution_network_egress_enabled"`

          - `"code_execution_network_egress_enabled"`

      - `CodeExecutionDomainAllowlistChanged object { current_value, previous_value, type }`

        - `current_value: array of string`

        - `previous_value: array of string`

        - `type: optional "code_execution_domain_allowlist_changed"`

          - `"code_execution_domain_allowlist_changed"`

      - `CodeExecutionDomainAllowlistTemplateChanged object { current_value, previous_value, type }`

        - `current_value: "custom" or "full_egress" or "package_managers"`

          - `"custom"`

          - `"full_egress"`

          - `"package_managers"`

        - `previous_value: "custom" or "full_egress" or "package_managers"`

          - `"custom"`

          - `"full_egress"`

          - `"package_managers"`

        - `type: optional "code_execution_domain_allowlist_template_changed"`

          - `"code_execution_domain_allowlist_template_changed"`

      - `ChatEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "chat_enabled"`

          - `"chat_enabled"`

      - `ClaudeCodeQuickWebSetupEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "claude_code_quick_web_setup_enabled"`

          - `"claude_code_quick_web_setup_enabled"`

      - `ClaudeCodeTeamMemoryMode object { current_value, previous_value, type }`

        - `current_value: "all_org_members" or "github_repo" or "off" or "specific_groups"`

          - `"all_org_members"`

          - `"github_repo"`

          - `"off"`

          - `"specific_groups"`

        - `previous_value: "all_org_members" or "github_repo" or "off" or "specific_groups"`

          - `"all_org_members"`

          - `"github_repo"`

          - `"off"`

          - `"specific_groups"`

        - `type: optional "claude_code_team_memory_mode"`

          - `"claude_code_team_memory_mode"`

      - `BrowserExtensionSettingsUpdated object { current_value, previous_value, type }`

        - `current_value: map[unknown]`

        - `previous_value: map[unknown]`

        - `type: optional "browser_extension_settings"`

          - `"browser_extension_settings"`

      - `DesktopExtensionAllowlistEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "is_desktop_extension_allowlist_enabled"`

          - `"is_desktop_extension_allowlist_enabled"`

      - `ClaudeDesignEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "claude_ai_design_enabled"`

          - `"claude_ai_design_enabled"`

      - `ClaudeAISkillSharingEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "claude_ai_skill_sharing_enabled"`

          - `"claude_ai_skill_sharing_enabled"`

      - `ClaudeAISkillSharingOrgEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "claude_ai_skill_sharing_org_enabled"`

          - `"claude_ai_skill_sharing_org_enabled"`

      - `ClaudeCodeRemoteControlEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "claude_code_remote_control_enabled"`

          - `"claude_code_remote_control_enabled"`

      - `ClaudeCodeRoutinesEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "claude_code_routines_enabled"`

          - `"claude_code_routines_enabled"`

      - `FrontierServicesDataUseEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "frontier_services_data_use_enabled"`

          - `"frontier_services_data_use_enabled"`

      - `LtiCourseProjectsEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "lti_course_projects_enabled"`

          - `"lti_course_projects_enabled"`

      - `ManagedAgentsEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "managed_agents_enabled"`

          - `"managed_agents_enabled"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_organization_settings_updated"`

      - `"claude_organization_settings_updated"`

  - `OwnedProjectsAccessRestored object { actor, id, created_at, 4 more }`

    Access to owned projects was restored.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "owned_projects_access_restored"`

      - `"owned_projects_access_restored"`

    - `user_id: optional string`

  - `PaymentMethodUpdated object { actor, id, created_at, 3 more }`

    The organization's default payment method was updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "payment_method_updated"`

      - `"payment_method_updated"`

  - `PhoneCodeSent object { actor, id, created_at, 3 more }`

    User requested a phone verification code.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "phone_code_sent"`

      - `"phone_code_sent"`

  - `PhoneCodeVerified object { actor, id, created_at, 3 more }`

    User successfully verified their phone code.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "phone_code_verified"`

      - `"phone_code_verified"`

  - `PlatformAPIKeyCreated object { actor, api_key_id, id, 4 more }`

    An API key was created.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `api_key_id: string`

      Tagged ID of the created API key

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_api_key_created"`

      - `"platform_api_key_created"`

  - `PlatformAPIKeyUpdated object { actor, api_key_id, updates, 5 more }`

    An API key was updated.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `api_key_id: string`

      Tagged ID of the updated API key

    - `updates: array of object { current_value, previous_value, type }`

      - `current_value: string`

      - `previous_value: string`

      - `type: "name" or "status" or "workspace"`

        - `"name"`

        - `"status"`

        - `"workspace"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_api_key_updated"`

      - `"platform_api_key_updated"`

  - `PlatformCostReportViewed object { actor, id, created_at, 3 more }`

    The cost report was viewed.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_cost_report_viewed"`

      - `"platform_cost_report_viewed"`

  - `PlatformFederationIssuerArchived object { actor, federation_issuer_id, id, 4 more }`

    An OIDC federation issuer was archived.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `federation_issuer_id: string`

      Tagged ID of the archived issuer

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_federation_issuer_archived"`

      - `"platform_federation_issuer_archived"`

  - `PlatformFederationIssuerUpdated object { actor, federation_issuer_id, updates, 5 more }`

    An OIDC federation issuer was updated.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `federation_issuer_id: string`

      Tagged ID of the updated issuer

    - `updates: array of object { current_value, previous_value, type }`

      - `current_value: string`

      - `previous_value: string`

      - `type: "ca_cert_pem_sha256" or "check_jti" or "discovery_base" or 7 more`

        - `"ca_cert_pem_sha256"`

        - `"check_jti"`

        - `"discovery_base"`

        - `"issuer_url"`

        - `"jwks_keys_sha256"`

        - `"jwks_polling_disabled_at"`

        - `"jwks_source"`

        - `"jwks_url"`

        - `"max_jwt_lifetime_seconds"`

        - `"name"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_federation_issuer_updated"`

      - `"platform_federation_issuer_updated"`

  - `PlatformFederationRuleArchived object { actor, federation_rule_id, id, 4 more }`

    An OIDC federation rule was archived.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `federation_rule_id: string`

      Tagged ID of the archived rule

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_federation_rule_archived"`

      - `"platform_federation_rule_archived"`

  - `PlatformFederationRuleUpdated object { actor, federation_rule_id, updates, 5 more }`

    An OIDC federation rule was updated.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `federation_rule_id: string`

      Tagged ID of the updated rule

    - `updates: array of object { current_value, previous_value, type }`

      - `current_value: string`

      - `previous_value: string`

      - `type: "applies_to_all_workspaces" or "attributes" or "description" or 11 more`

        - `"applies_to_all_workspaces"`

        - `"attributes"`

        - `"description"`

        - `"match_audience"`

        - `"match_claims"`

        - `"match_condition"`

        - `"match_subject_prefix"`

        - `"name"`

        - `"oauth_scope"`

        - `"target_id"`

        - `"target_lookup_attr"`

        - `"target_type"`

        - `"token_lifetime_seconds"`

        - `"workspace_id"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_federation_rule_updated"`

      - `"platform_federation_rule_updated"`

  - `PlatformFederationRuleWorkspaceAdded object { actor, federation_rule_id, workspace_id, 5 more }`

    A federation rule was enabled for a workspace.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `federation_rule_id: string`

      Tagged ID of the federation rule

    - `workspace_id: string`

      Tagged ID of the workspace the rule was enabled for

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_federation_rule_workspace_added"`

      - `"platform_federation_rule_workspace_added"`

  - `PlatformFederationRuleWorkspaceRemoved object { actor, federation_rule_id, workspace_id, 5 more }`

    A federation rule was disabled for a workspace.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `federation_rule_id: string`

      Tagged ID of the federation rule

    - `workspace_id: string`

      Tagged ID of the workspace the rule was disabled for

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_federation_rule_workspace_removed"`

      - `"platform_federation_rule_workspace_removed"`

  - `PlatformFileContentDownloaded object { actor, file_id, id, 4 more }`

    Activity logged when file content is downloaded via GET /v1/files/{file_id}/content.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

    - `file_id: string`

      The tagged ID of the downloaded file

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_file_content_downloaded"`

      - `"platform_file_content_downloaded"`

  - `PlatformFileDeleted object { actor, file_id, id, 4 more }`

    Activity logged when a file is deleted via DELETE /v1/files/{file_id}.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

    - `file_id: string`

      The tagged ID of the deleted file

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_file_deleted"`

      - `"platform_file_deleted"`

  - `PlatformFileUploaded object { actor, file_id, id, 5 more }`

    Activity logged when a file is uploaded via POST /v1/files.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

    - `file_id: string`

      The tagged ID of the uploaded file

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `session_id: optional string`

      The tagged session ID (agent-api only)

    - `type: optional "platform_file_uploaded"`

      - `"platform_file_uploaded"`

  - `PlatformServiceAccountArchived object { actor, service_account_id, id, 4 more }`

    A service account was archived.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `service_account_id: string`

      Tagged ID of the archived service account

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_service_account_archived"`

      - `"platform_service_account_archived"`

  - `PlatformServiceAccountUpdated object { actor, service_account_id, updates, 5 more }`

    A service account was updated.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `service_account_id: string`

      Tagged ID of the updated service account

    - `updates: array of object { current_value, previous_value, type }`

      - `current_value: string`

      - `previous_value: string`

      - `type: "description"`

        - `"description"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_service_account_updated"`

      - `"platform_service_account_updated"`

  - `PlatformServiceAccountWorkspaceMemberAdded object { actor, service_account_id, workspace_id, 5 more }`

    A service account was added as a member of a workspace.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `service_account_id: string`

      Tagged ID of the service account

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_service_account_workspace_member_added"`

      - `"platform_service_account_workspace_member_added"`

  - `PlatformServiceAccountWorkspaceMemberRemoved object { actor, service_account_id, workspace_id, 5 more }`

    A service account was removed from a workspace.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `service_account_id: string`

      Tagged ID of the service account

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_service_account_workspace_member_removed"`

      - `"platform_service_account_workspace_member_removed"`

  - `PlatformServiceAccountWorkspaceMemberUpdated object { actor, service_account_id, updates, 6 more }`

    A service account's workspace membership role was updated.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `service_account_id: string`

      Tagged ID of the service account

    - `updates: array of object { current_value, previous_value, type }`

      - `current_value: string`

      - `previous_value: string`

      - `type: "workspace_role"`

        - `"workspace_role"`

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_service_account_workspace_member_updated"`

      - `"platform_service_account_workspace_member_updated"`

  - `PlatformSigningKeyCreated object { actor, algorithm, key_backing_type, 7 more }`

    Activity logged when a new request-signing key is registered for the org.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `algorithm: string`

      The signing algorithm (e.g. ecdsa-p256-sha256)

    - `key_backing_type: string`

      The backing type of the key (IN_MEMORY or CLOUD_KMS)

    - `signing_key_id: string`

      The tagged ID of the created signing key

    - `status: string`

      The initial status of the key (ACTIVE or PENDING)

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_signing_key_created"`

      - `"platform_signing_key_created"`

  - `PlatformSigningKeyDeleted object { actor, algorithm, key_backing_type, 7 more }`

    Activity logged when a signing key is permanently deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `algorithm: string`

      The algorithm of the deleted key

    - `key_backing_type: string`

      The backing type of the deleted key (IN_MEMORY or CLOUD_KMS)

    - `key_name: string`

      The name of the deleted key

    - `signing_key_id: string`

      The tagged ID of the deleted signing key

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_signing_key_deleted"`

      - `"platform_signing_key_deleted"`

  - `PlatformSigningKeyRotated object { actor, algorithm, key_group_identifier, 7 more }`

    Activity logged when an in-memory signing key is rotated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `algorithm: string`

      The algorithm of the new key

    - `key_group_identifier: string`

      The key group identifier linking old and new keys

    - `new_signing_key_id: string`

      The tagged ID of the newly created key

    - `old_signing_key_id: string`

      The tagged ID of the expired old key

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_signing_key_rotated"`

      - `"platform_signing_key_rotated"`

  - `PlatformSkillVersionCreated object { actor, skill_id, version, 5 more }`

    Activity logged when a skill version is created via POST /v1/skills/{skill_id}/versions.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

    - `skill_id: string`

      The tagged ID of the skill

    - `version: string`

      The version number of the created version

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_skill_version_created"`

      - `"platform_skill_version_created"`

  - `PlatformSkillVersionDeleted object { actor, skill_id, version, 5 more }`

    Activity logged when a skill version is deleted via DELETE /v1/skills/{skill_id}/versions/{version}.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

    - `skill_id: string`

      The tagged ID of the skill

    - `version: string`

      The version number of the deleted version

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_skill_version_deleted"`

      - `"platform_skill_version_deleted"`

  - `PlatformSpendLimitAlertEmailsUpdated object { actor, id, alert_emails, 5 more }`

    Spend limit alert email addresses and role targets were updated for an org.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `alert_emails: optional array of string`

      Updated list of alert email addresses.

    - `alerted_roles: optional array of string`

      Updated list of alerted roles.

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_spend_limit_alert_emails_updated"`

      - `"platform_spend_limit_alert_emails_updated"`

  - `PlatformSpendLimitCreated object { actor, id, created_at, 5 more }`

    An org-level fixed-dollar spend limit was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `limit_action: optional string`

      The action taken when the limit is reached (notify_only or notify_and_pause).

    - `limit_usd: optional number`

      The spend limit threshold in USD cents.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_spend_limit_created"`

      - `"platform_spend_limit_created"`

  - `PlatformSpendLimitDeleted object { actor, id, created_at, 4 more }`

    An org-level spend limit was removed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `spend_limit_id: optional string`

      UUID of the deleted spend limit.

    - `type: optional "platform_spend_limit_deleted"`

      - `"platform_spend_limit_deleted"`

  - `PlatformSpendLimitUpdated object { actor, id, created_at, 5 more }`

    An org-level spend limit snooze/ignore state was changed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `ignore: optional boolean`

      Whether the limit is being snoozed (ignored).

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `spend_limit_id: optional string`

      UUID of the spend limit.

    - `type: optional "platform_spend_limit_updated"`

      - `"platform_spend_limit_updated"`

  - `PlatformUsageReportClaudeCodeViewed object { actor, id, created_at, 3 more }`

    The Claude Code usage report was viewed.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_usage_report_claude_code_viewed"`

      - `"platform_usage_report_claude_code_viewed"`

  - `PlatformUsageReportMessagesViewed object { actor, id, created_at, 3 more }`

    The messages usage report was viewed.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_usage_report_messages_viewed"`

      - `"platform_usage_report_messages_viewed"`

  - `PlatformWorkspaceArchived object { actor, workspace_id, id, 4 more }`

    A workspace was archived.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `workspace_id: string`

      Tagged ID of the archived workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_workspace_archived"`

      - `"platform_workspace_archived"`

  - `PlatformWorkspaceCreated object { actor, workspace_id, id, 4 more }`

    A workspace was created.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `workspace_id: string`

      Tagged ID of the created workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_workspace_created"`

      - `"platform_workspace_created"`

  - `PlatformWorkspaceMemberAdded object { actor, user_id, workspace_id, 5 more }`

    A member was added to a workspace.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `user_id: string`

      Tagged ID of the added member

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_workspace_member_added"`

      - `"platform_workspace_member_added"`

  - `PlatformWorkspaceMemberRemoved object { actor, user_id, workspace_id, 5 more }`

    A member was removed from a workspace.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `user_id: string`

      Tagged ID of the removed member

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_workspace_member_removed"`

      - `"platform_workspace_member_removed"`

  - `PlatformWorkspaceMemberUpdated object { actor, updates, user_id, 6 more }`

    A workspace member was updated.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `updates: array of object { current_value, previous_value, type }`

      - `current_value: string`

      - `previous_value: string`

      - `type: "workspace_role"`

        - `"workspace_role"`

    - `user_id: string`

      Tagged ID of the updated member

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_workspace_member_updated"`

      - `"platform_workspace_member_updated"`

  - `PlatformWorkspaceMemberViewed object { actor, user_id, workspace_id, 5 more }`

    A workspace member was viewed.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `user_id: string`

      Tagged ID of the viewed member

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_workspace_member_viewed"`

      - `"platform_workspace_member_viewed"`

  - `PlatformWorkspaceMembersListed object { actor, workspace_id, id, 4 more }`

    Workspace members were listed.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_workspace_members_listed"`

      - `"platform_workspace_members_listed"`

  - `PlatformWorkspaceRateLimitDeleted object { actor, limiter_type, model_group, 6 more }`

    A workspace rate limit was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `limiter_type: string`

      Type of rate limiter

    - `model_group: string`

      Model group the rate limit applied to

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_workspace_rate_limit_deleted"`

      - `"platform_workspace_rate_limit_deleted"`

  - `PlatformWorkspaceRateLimitUpdated object { actor, limiter_type, model_group, 7 more }`

    A workspace rate limit was created or updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `limiter_type: string`

      Type of rate limiter

    - `model_group: string`

      Model group the rate limit applies to

    - `value: number`

      New rate limit value

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_workspace_rate_limit_updated"`

      - `"platform_workspace_rate_limit_updated"`

  - `PlatformWorkspaceUpdated object { actor, updates, workspace_id, 5 more }`

    A workspace was updated.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `updates: array of object { current_value, previous_value, type }`

      - `current_value: string`

      - `previous_value: string`

      - `type: "allowed_inference_geos" or "default_inference_geo" or "display_color" or "name"`

        - `"allowed_inference_geos"`

        - `"default_inference_geo"`

        - `"display_color"`

        - `"name"`

    - `workspace_id: string`

      Tagged ID of the updated workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_workspace_updated"`

      - `"platform_workspace_updated"`

  - `ClaudePluginCreated object { actor, id, created_at, 5 more }`

    Plugin was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `plugin_id: optional string`

    - `plugin_name: optional string`

    - `type: optional "claude_plugin_created"`

      - `"claude_plugin_created"`

  - `ClaudePluginDeleted object { actor, id, created_at, 5 more }`

    Plugin was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `plugin_id: optional string`

    - `plugin_name: optional string`

    - `type: optional "claude_plugin_deleted"`

      - `"claude_plugin_deleted"`

  - `PluginInstallationPreferenceUpdated object { actor, marketplace_id, plugin_name, 9 more }`

    An org admin changed the installation preference for a plugin.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `marketplace_id: string`

      Marketplace ID

    - `plugin_name: string`

      Plugin name

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `action: optional string`

      Action taken (e.g. 'deleted' for clearing an override)

    - `created_at: optional string`

      When this activity occurred.

    - `group_id: optional string`

      Tagged group ID for group-level overrides (null for org-level)

    - `group_name: optional string`

      Group name for group-level overrides

    - `installation_preference: optional string`

      New installation preference value (set only when action is an update; null for delete actions)

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "plugin_installation_preference_updated"`

      - `"plugin_installation_preference_updated"`

  - `ClaudePluginReplaced object { actor, id, created_at, 5 more }`

    Plugin was replaced.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `plugin_id: optional string`

    - `plugin_name: optional string`

    - `type: optional "claude_plugin_replaced"`

      - `"claude_plugin_replaced"`

  - `ClaudePluginUpdated object { actor, id, created_at, 5 more }`

    Plugin was updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `plugin_id: optional string`

    - `plugin_name: optional string`

    - `type: optional "claude_plugin_updated"`

      - `"claude_plugin_updated"`

  - `PrepaidAutoRechargeDisabled object { actor, id, created_at, 3 more }`

    Auto-recharge was disabled for API prepaid org.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "prepaid_auto_recharge_disabled"`

      - `"prepaid_auto_recharge_disabled"`

  - `PrepaidAutoRechargeUpdated object { actor, id, created_at, 5 more }`

    Auto-recharge settings were updated for API prepaid org.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `target_amount: optional number`

      Target recharge amount in minor units.

    - `threshold_amount: optional number`

      Threshold amount to trigger recharge in minor units.

    - `type: optional "prepaid_auto_recharge_updated"`

      - `"prepaid_auto_recharge_updated"`

  - `PrepaidExtraUsageAutoReloadDisabled object { actor, id, created_at, 3 more }`

    Prepaid usage credit auto-reload was disabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "prepaid_extra_usage_auto_reload_disabled"`

      - `"prepaid_extra_usage_auto_reload_disabled"`

  - `PrepaidExtraUsageAutoReloadEnabled object { actor, id, created_at, 3 more }`

    Prepaid usage credit auto-reload was enabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "prepaid_extra_usage_auto_reload_enabled"`

      - `"prepaid_extra_usage_auto_reload_enabled"`

  - `PrepaidExtraUsageAutoReloadSettingsUpdated object { actor, id, created_at, 3 more }`

    Prepaid usage credit auto-reload settings were updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "prepaid_extra_usage_auto_reload_settings_updated"`

      - `"prepaid_extra_usage_auto_reload_settings_updated"`

  - `PrimaryOwnerTransferred object { actor, new_owner_id, previous_owner_id, 5 more }`

    Primary owner role was transferred to another org member.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `new_owner_id: string`

    - `previous_owner_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "primary_owner_transferred"`

      - `"primary_owner_transferred"`

  - `ClaudeProjectArchived object { actor, claude_project_id, id, 4 more }`

    A Claude project was archived.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_archived"`

      - `"claude_project_archived"`

  - `ClaudeProjectCreated object { actor, claude_project_id, id, 4 more }`

    A Claude project was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_created"`

      - `"claude_project_created"`

  - `ClaudeProjectDeleted object { actor, claude_project_id, id, 4 more }`

    A Claude project was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_deleted"`

      - `"claude_project_deleted"`

  - `ClaudeProjectDocumentAccessFailed object { actor, claude_project_document_id, claude_project_id, 6 more }`

    An attempt to access a document in a Claude project failed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `claude_project_document_id: string`

    - `claude_project_id: string`

    - `filename: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_document_access_failed"`

      - `"claude_project_document_access_failed"`

  - `ClaudeProjectDocumentDeleted object { actor, claude_project_document_id, claude_project_id, 6 more }`

    A document was deleted from a Claude project.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_project_document_id: string`

    - `claude_project_id: string`

    - `filename: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_document_deleted"`

      - `"claude_project_document_deleted"`

  - `ClaudeProjectDocumentDeletionFailed object { actor, claude_project_document_id, claude_project_id, 6 more }`

    A request to delete a document from a Claude project failed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `claude_project_document_id: string`

    - `claude_project_id: string`

    - `filename: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_document_deletion_failed"`

      - `"claude_project_document_deletion_failed"`

  - `ClaudeProjectDocumentUploaded object { actor, claude_project_document_id, claude_project_id, 6 more }`

    A document was uploaded to a Claude project.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_project_document_id: string`

    - `claude_project_id: string`

    - `filename: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_document_uploaded"`

      - `"claude_project_document_uploaded"`

  - `ClaudeProjectDocumentViewed object { actor, claude_project_document_id, claude_project_id, 6 more }`

    A document in a Claude project was viewed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_project_document_id: string`

    - `claude_project_id: string`

    - `filename: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_document_viewed"`

      - `"claude_project_document_viewed"`

  - `ClaudeProjectFileAccessFailed object { actor, claude_file_id, claude_project_id, 5 more }`

    An attempt to access a file in a Claude project failed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `claude_file_id: string`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_file_access_failed"`

      - `"claude_project_file_access_failed"`

  - `ClaudeProjectFileDeleted object { actor, claude_file_id, claude_project_id, 5 more }`

    A file was deleted from a Claude project.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `claude_file_id: string`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_file_deleted"`

      - `"claude_project_file_deleted"`

  - `ClaudeProjectFileDeletionFailed object { actor, claude_file_id, claude_project_id, 5 more }`

    A request to delete a file from a Claude project failed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `claude_file_id: string`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_file_deletion_failed"`

      - `"claude_project_file_deletion_failed"`

  - `ClaudeProjectFileUploaded object { actor, claude_file_id, claude_project_id, 6 more }`

    A file was uploaded to a Claude project.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `claude_file_id: string`

    - `claude_project_id: string`

    - `filename: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_file_uploaded"`

      - `"claude_project_file_uploaded"`

  - `ClaudeProjectReported object { actor, claude_project_id, id, 4 more }`

    A Claude project was reported.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_reported"`

      - `"claude_project_reported"`

  - `ClaudeProjectSharingUpdated object { actor, audience, claude_project_id, 5 more }`

    A Claude project's sharing settings were updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `audience: array of object { type }  or object { type }`

      Sharing audience for the project. If empty, this it's only visible to the creating user.

      - `ProjectSharingAudiencePublic object { type }`

        - `type: optional "public"`

          - `"public"`

      - `ProjectSharingAudienceOrganization object { type }`

        - `type: optional "organization"`

          - `"organization"`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_sharing_updated"`

      - `"claude_project_sharing_updated"`

  - `ClaudeProjectViewed object { actor, claude_project_id, id, 5 more }`

    A Claude project was viewed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `preview_only: optional boolean`

    - `type: optional "claude_project_viewed"`

      - `"claude_project_viewed"`

  - `ClaudePubsecIdentityConfigured object { actor, idp_saml_config_updated, magic_link_toggled, 6 more }`

    SAML IdP configuration updated for a public sector organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `idp_saml_config_updated: boolean`

    - `magic_link_toggled: boolean`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `magic_link_enabled: optional boolean`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_pubsec_identity_configured"`

      - `"claude_pubsec_identity_configured"`

  - `RbacRoleAssigned object { actor, principal_id, principal_type, 6 more }`

    Admin assigned an RBAC custom role to a principal.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `principal_id: string`

      Tagged ID of the principal

    - `principal_type: string`

      Type of principal: account or group

    - `role_id: string`

      Tagged ID of the role

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "rbac_role_assigned"`

      - `"rbac_role_assigned"`

  - `RbacRoleCreated object { actor, role_id, role_name, 5 more }`

    Admin created an RBAC custom role.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `role_id: string`

      Tagged ID of the created role

    - `role_name: string`

      Name of the created role

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "rbac_role_created"`

      - `"rbac_role_created"`

  - `RbacRoleDeleted object { actor, role_id, id, 4 more }`

    Admin deleted an RBAC custom role.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `role_id: string`

      Tagged ID of the deleted role

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "rbac_role_deleted"`

      - `"rbac_role_deleted"`

  - `RbacRolePermissionAdded object { action, actor, resource_id, 7 more }`

    Admin added a permission to an RBAC custom role.

    - `action: string`

      Action permitted on the resource

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `resource_id: string`

      ID of the resource

    - `resource_type: string`

      Type of resource the permission applies to

    - `role_id: string`

      Tagged ID of the role

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "rbac_role_permission_added"`

      - `"rbac_role_permission_added"`

  - `RbacRolePermissionRemoved object { action, actor, resource_id, 7 more }`

    Admin removed a permission from an RBAC custom role.

    - `action: string`

      Action that was permitted on the resource

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `resource_id: string`

      ID of the resource

    - `resource_type: string`

      Type of resource the permission applied to

    - `role_id: string`

      Tagged ID of the role

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "rbac_role_permission_removed"`

      - `"rbac_role_permission_removed"`

  - `RbacRoleUnassigned object { actor, principal_id, principal_type, 6 more }`

    Admin unassigned an RBAC custom role from a principal.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `principal_id: string`

      Tagged ID of the principal

    - `principal_type: string`

      Type of principal: account or group

    - `role_id: string`

      Tagged ID of the role

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "rbac_role_unassigned"`

      - `"rbac_role_unassigned"`

  - `RbacRoleUpdated object { actor, role_id, id, 4 more }`

    Admin updated an RBAC custom role.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `role_id: string`

      Tagged ID of the updated role

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "rbac_role_updated"`

      - `"rbac_role_updated"`

  - `RoleAssignmentGranted object { actor, id, created_at, 8 more }`

    Role assignment was granted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `resource_id: optional string`

    - `resource_type: optional string`

    - `role: optional string`

    - `target_id: optional string`

    - `target_type: optional string`

    - `type: optional "role_assignment_granted"`

      - `"role_assignment_granted"`

  - `RoleAssignmentRevoked object { actor, id, created_at, 8 more }`

    Role assignment was revoked.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `resource_id: optional string`

    - `resource_type: optional string`

    - `role: optional string`

    - `target_id: optional string`

    - `target_type: optional string`

    - `type: optional "role_assignment_revoked"`

      - `"role_assignment_revoked"`

  - `SSOLoginFailed object { actor, id, created_at, 3 more }`

    An SSO sign-in attempt failed.

    - `actor: object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `ip_address: string`

      - `user_agent: string`

      - `type: optional "unauthenticated_user_actor"`

        - `"unauthenticated_user_actor"`

      - `unauthenticated_email_address: optional string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "sso_login_failed"`

      - `"sso_login_failed"`

  - `SSOLoginInitiated object { actor, id, created_at, 3 more }`

    A user started an SSO sign-in flow.

    - `actor: object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `ip_address: string`

      - `user_agent: string`

      - `type: optional "unauthenticated_user_actor"`

        - `"unauthenticated_user_actor"`

      - `unauthenticated_email_address: optional string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "sso_login_initiated"`

      - `"sso_login_initiated"`

  - `SSOLoginSucceeded object { actor, id, auth_method, 5 more }`

    A user successfully signed in with SSO.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `auth_method: optional "sso"`

      The method the user used to authenticate. May be absent on activities recorded before this field was introduced.

      - `"sso"`

    - `created_at: optional string`

      When this activity occurred.

    - `mfa_method: optional "not_used"`

      The second authentication factor performed during this login, if any. `null` when the second-factor status is not recorded on this event — for example, when authentication was delegated to an external identity provider and any second factor is not visible to Anthropic, or when this event is one step of a multi-step login whose MFA is reported on another activity. May be absent on activities recorded before this field was introduced.

      - `"not_used"`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "sso_login_succeeded"`

      - `"sso_login_succeeded"`

  - `SSOSecondFactorMagicLink object { actor, id, created_at, 3 more }`

    SSO second factor magic link was used.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "sso_second_factor_magic_link"`

      - `"sso_second_factor_magic_link"`

  - `ScimUserCreated object { actor, user_id, id, 4 more }`

    A SCIM user was provisioned.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { directory_id, workos_event_id, idp_connection_type, type }`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

    - `user_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "scim_user_created"`

      - `"scim_user_created"`

  - `ScimUserDeleted object { actor, user_id, id, 4 more }`

    A SCIM user was deleted.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { directory_id, workos_event_id, idp_connection_type, type }`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

    - `user_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "scim_user_deleted"`

      - `"scim_user_deleted"`

  - `ScimUserUpdated object { actor, user_id, id, 4 more }`

    A SCIM user was updated.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { directory_id, workos_event_id, idp_connection_type, type }`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

    - `user_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "scim_user_updated"`

      - `"scim_user_updated"`

  - `ScopedAPIKeyDeleted object { actor, api_key_id, api_key_name, 6 more }`

    A scoped API key was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `api_key_id: string`

      Tagged ID of the deleted scoped API key

    - `api_key_name: string`

      Name of the deleted scoped API key

    - `scopes: array of string`

      Scopes the deleted key had

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "scoped_api_key_deleted"`

      - `"scoped_api_key_deleted"`

  - `ScopedAPIKeyUpdated object { actor, api_key_id, updates, 5 more }`

    A scoped API key was renamed or its activation state changed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `api_key_id: string`

      Tagged ID of the updated scoped API key

    - `updates: array of object { current_value, previous_value, type }`

      - `current_value: string`

      - `previous_value: string`

      - `type: "activation_state" or "name"`

        - `"activation_state"`

        - `"name"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "scoped_api_key_updated"`

      - `"scoped_api_key_updated"`

  - `SeatTierChangesCancelled object { actor, id, created_at, 3 more }`

    Scheduled seat tier downgrades were cancelled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "seat_tier_changes_cancelled"`

      - `"seat_tier_changes_cancelled"`

  - `SeatTiersPurchased object { actor, id, created_at, 4 more }`

    Seat tiers were purchased or upgraded on a subscription.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `item_allocations: optional map[number]`

      Desired seat tier allocations (item type to quantity).

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "seat_tiers_purchased"`

      - `"seat_tiers_purchased"`

  - `ServiceCreated object { actor, service_name, id, 4 more }`

    Activity logged when an org service is explicitly created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `service_name: string`

      The org service name (e.g., 'external:my-service')

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "service_created"`

      - `"service_created"`

  - `ServiceDeleted object { actor, service_name, id, 4 more }`

    Activity logged when an org service is deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `service_name: string`

      The org service name (e.g., 'external:my-service')

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "service_deleted"`

      - `"service_deleted"`

  - `ServiceKeyCreated object { actor, is_service_created, key_name, 8 more }`

    Activity logged when a new org service key is created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `is_service_created: boolean`

      Whether the org service was implicitly created in this request

    - `key_name: string`

      The human-readable name of the key

    - `scopes: array of string`

      The scopes granted to this service key

    - `service_key_id: string`

      The ID of the created service key

    - `service_name: string`

      The service name this key belongs to

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "service_key_created"`

      - `"service_key_created"`

  - `ServiceKeyRevoked object { actor, service_key_id, service_name, 5 more }`

    Activity logged when an org service key is revoked.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `service_key_id: string`

      The tagged ID of the revoked service key

    - `service_name: string`

      The service name this key belongs to

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "service_key_revoked"`

      - `"service_key_revoked"`

  - `SessionRevoked object { actor, id, created_at, 3 more }`

    User revoked a specific session.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "session_revoked"`

      - `"session_revoked"`

  - `SessionShareAccessed object { actor, id, created_at, 4 more }`

    Session share was accessed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `share_id: optional string`

    - `type: optional "session_share_accessed"`

      - `"session_share_accessed"`

  - `SessionShareCreated object { actor, id, created_at, 4 more }`

    Session share was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `share_id: optional string`

    - `type: optional "session_share_created"`

      - `"session_share_created"`

  - `SessionShareRevoked object { actor, id, created_at, 4 more }`

    Session share was revoked.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `share_id: optional string`

    - `type: optional "session_share_revoked"`

      - `"session_share_revoked"`

  - `ClaudeSkillCreated object { actor, id, created_at, 5 more }`

    Skill was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `skill_id: optional string`

    - `skill_name: optional string`

    - `type: optional "claude_skill_created"`

      - `"claude_skill_created"`

  - `ClaudeSkillDeleted object { actor, id, created_at, 5 more }`

    Skill was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `skill_id: optional string`

    - `skill_name: optional string`

    - `type: optional "claude_skill_deleted"`

      - `"claude_skill_deleted"`

  - `ClaudeSkillDisabled object { actor, id, created_at, 5 more }`

    User disabled a skill for their account.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `skill_id: optional string`

    - `skill_name: optional string`

    - `type: optional "claude_skill_disabled"`

      - `"claude_skill_disabled"`

  - `ClaudeSkillEnabled object { actor, id, created_at, 5 more }`

    User enabled a skill for their account.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `skill_id: optional string`

    - `skill_name: optional string`

    - `type: optional "claude_skill_enabled"`

      - `"claude_skill_enabled"`

  - `ClaudeSkillReplaced object { actor, id, created_at, 5 more }`

    Skill was replaced.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `skill_id: optional string`

    - `skill_name: optional string`

    - `type: optional "claude_skill_replaced"`

      - `"claude_skill_replaced"`

  - `SocialLoginSucceeded object { actor, provider, id, 6 more }`

    A user successfully signed in with a social identity provider (Google, Apple, or Microsoft).

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `provider: "apple" or "google" or "microsoft"`

      - `"apple"`

      - `"google"`

      - `"microsoft"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `auth_method: optional "social"`

      The method the user used to authenticate. May be absent on activities recorded before this field was introduced.

      - `"social"`

    - `created_at: optional string`

      When this activity occurred.

    - `mfa_method: optional "not_used"`

      The second authentication factor performed during this login, if any. `null` when the second-factor status is not recorded on this event — for example, when authentication was delegated to an external identity provider and any second factor is not visible to Anthropic, or when this event is one step of a multi-step login whose MFA is reported on another activity. May be absent on activities recorded before this field was introduced.

      - `"not_used"`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "social_login_succeeded"`

      - `"social_login_succeeded"`

  - `SubscriptionCancellationScheduled object { actor, id, created_at, 3 more }`

    Subscription cancellation was scheduled at end of billing period.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "subscription_cancellation_scheduled"`

      - `"subscription_cancellation_scheduled"`

  - `SubscriptionQuantityUpdated object { actor, added_seats, new_quantity, 6 more }`

    Contracted subscription seat quantity was updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `added_seats: number`

    - `new_quantity: number`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `previous_quantity: optional number`

    - `type: optional "subscription_quantity_updated"`

      - `"subscription_quantity_updated"`

  - `SubscriptionRenewed object { actor, id, billing_interval, 5 more }`

    A cancelled subscription was renewed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `billing_interval: optional string`

      Billing interval (e.g. monthly, annual).

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `plan_type: optional string`

      Plan type being renewed into (e.g. team).

    - `type: optional "subscription_renewed"`

      - `"subscription_renewed"`

  - `SubscriptionResumed object { actor, id, created_at, 3 more }`

    A scheduled subscription cancellation was reversed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "subscription_resumed"`

      - `"subscription_resumed"`

  - `SubscriptionStarted object { actor, id, billing_interval, 6 more }`

    A new subscription was created (Team or Enterprise).

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `billing_interval: optional string`

      Billing interval (e.g. monthly, annual).

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `plan_type: optional string`

      Type of subscription started (e.g. team, enterprise).

    - `seat_count: optional number`

      Number of seats purchased.

    - `type: optional "subscription_started"`

      - `"subscription_started"`

  - `SubscriptionUpgraded object { actor, id, created_at, 5 more }`

    Subscription plan was upgraded (e.g. Team to Enterprise).

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `new_plan: optional string`

      New plan type after upgrade.

    - `old_plan: optional string`

      Previous plan type.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "subscription_upgraded"`

      - `"subscription_upgraded"`

  - `TunnelTokenMinted object { actor, token_id, id, 5 more }`

    An OAuth bearer token for the tunnel management API was minted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `token_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `token_name: optional string`

    - `type: optional "tunnel_token_minted"`

      - `"tunnel_token_minted"`

  - `TunnelTokenRevoked object { actor, token_id, id, 4 more }`

    An OAuth bearer token for the tunnel management API was revoked.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `token_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "tunnel_token_revoked"`

      - `"tunnel_token_revoked"`

  - `UserConsentRecorded object { actor, consent_type, entity_id, 6 more }`

    User granted a consent for a specific entity (e.g. consumer health consent for an MCP server).

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `consent_type: string`

    - `entity_id: string`

    - `entity_type: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "user_consent_recorded"`

      - `"user_consent_recorded"`

  - `UserConsentRevoked object { actor, id, consent_id, 7 more }`

    User revoked a previously granted consent for a specific entity.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `consent_id: optional string`

    - `consent_type: optional string`

    - `created_at: optional string`

      When this activity occurred.

    - `entity_id: optional string`

    - `entity_type: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "user_consent_revoked"`

      - `"user_consent_revoked"`

  - `ClaudeUserRoleUpdated object { actor, current_role, previous_role, 7 more }`

    A user's role within the organization was changed, or the user was added to or removed from the organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { admin_api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

    - `current_role: string`

      If null, then user was removed from the Organization

    - `previous_role: string`

      If null, then user was added to the Organization

    - `user_email: string`

      Email of the user whose role was changed

    - `user_id: string`

      ID of the user whose role was changed

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_user_role_updated"`

      - `"claude_user_role_updated"`

  - `ClaudeUserSettingsUpdated object { actor, updates, id, 4 more }`

    User updated their personal settings.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `updates: array of object { current_value, previous_value, type }  or object { current_value, previous_value, type }  or object { current_value, previous_value, type }  or 19 more`

      - `FullName object { current_value, previous_value, type }`

        - `current_value: string`

        - `previous_value: string`

        - `type: optional "full_name"`

          - `"full_name"`

      - `DisplayName object { current_value, previous_value, type }`

        - `current_value: string`

        - `previous_value: string`

        - `type: optional "display_name"`

          - `"display_name"`

      - `ArtifactsEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "artifacts_enabled"`

          - `"artifacts_enabled"`

      - `LatexEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "latex_enabled"`

          - `"latex_enabled"`

      - `AnalysisToolEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "analysis_tool_enabled"`

          - `"analysis_tool_enabled"`

      - `ChatSuggestionsEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "chat_suggestions_enabled"`

          - `"chat_suggestions_enabled"`

      - `MultimodalPdfsEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "multimodal_pdfs_enabled"`

          - `"multimodal_pdfs_enabled"`

      - `GDriveEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "gdrive_enabled"`

          - `"gdrive_enabled"`

      - `GDriveIndexingEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "gdrive_indexing_enabled"`

          - `"gdrive_indexing_enabled"`

      - `WebSearchEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "web_search_enabled"`

          - `"web_search_enabled"`

      - `GeolocationEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "geolocation_enabled"`

          - `"geolocation_enabled"`

      - `UserMemoryEnabledSetting object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "enabled_saffron"`

          - `"enabled_saffron"`

      - `McpToolsEnabled object { current_value, previous_value, type }`

        - `current_value: map[boolean]`

        - `previous_value: map[boolean]`

        - `type: optional "mcp_tools_enabled"`

          - `"mcp_tools_enabled"`

      - `CliOpPermissionsEnabled object { current_value, previous_value, type }`

        - `current_value: map[string]`

        - `previous_value: map[string]`

        - `type: optional "cli_op_permissions_enabled"`

          - `"cli_op_permissions_enabled"`

      - `GoogleDriveSearchEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "google_drive_search_enabled"`

          - `"google_drive_search_enabled"`

      - `GmailIntegrationEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "gmail_integration_enabled"`

          - `"gmail_integration_enabled"`

      - `GoogleCalendarIntegrationEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "google_calendar_integration_enabled"`

          - `"google_calendar_integration_enabled"`

      - `ThinkingModeEnabled object { current_value, previous_value, type }`

        - `current_value: "adaptive" or "extended" or "off"`

          - `"adaptive"`

          - `"extended"`

          - `"off"`

        - `previous_value: "adaptive" or "extended" or "off"`

          - `"adaptive"`

          - `"extended"`

          - `"off"`

        - `type: optional "thinking_mode_enabled"`

          - `"thinking_mode_enabled"`

      - `ResearchModeEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "research_mode_enabled"`

          - `"research_mode_enabled"`

      - `ComputerUseEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "computer_use_enabled"`

          - `"computer_use_enabled"`

      - `ClaudeAPIInArtifactsEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "claude_api_in_artifacts_enabled"`

          - `"claude_api_in_artifacts_enabled"`

      - `ConversationPreferences object { type }`

        The 'conversation_preferences' for the user were updated. Values omitted.

        - `type: optional "conversation_preferences"`

          - `"conversation_preferences"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_user_settings_updated"`

      - `"claude_user_settings_updated"`

  - `WorkspaceMemberSpendLimitCreated object { actor, id, account_id, 7 more }`

    A per-member or workspace-default Claude Code spend limit was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `account_id: optional string`

      Tagged ID of the user (null for workspace-wide default).

    - `created_at: optional string`

      When this activity occurred.

    - `limit_action: optional string`

      The action taken when the limit is reached.

    - `limit_usd: optional number`

      The spend limit threshold in USD cents.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "workspace_member_spend_limit_created"`

      - `"workspace_member_spend_limit_created"`

    - `workspace_id: optional string`

      Tagged ID of the workspace.

  - `WorkspaceMemberSpendLimitDeleted object { actor, id, account_id, 6 more }`

    A per-member or workspace-default Claude Code spend limit was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `account_id: optional string`

      Tagged ID of the user (null for workspace-wide default).

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `spend_limit_id: optional string`

      UUID of the deleted spend limit.

    - `type: optional "workspace_member_spend_limit_deleted"`

      - `"workspace_member_spend_limit_deleted"`

    - `workspace_id: optional string`

      Tagged ID of the workspace.

  - `WorkspaceMemberSpendLimitUpdated object { actor, id, account_id, 7 more }`

    A per-member Claude Code spend limit amount was updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `account_id: optional string`

      Tagged ID of the user (null for workspace-wide default).

    - `created_at: optional string`

      When this activity occurred.

    - `new_limit_usd: optional number`

      The new spend limit threshold in USD cents.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `spend_limit_id: optional string`

      UUID of the spend limit.

    - `type: optional "workspace_member_spend_limit_updated"`

      - `"workspace_member_spend_limit_updated"`

    - `workspace_id: optional string`

      Tagged ID of the workspace.

  - `WorkspaceSpendLimitCreated object { actor, id, created_at, 6 more }`

    A workspace-level API spend limit was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `limit_action: optional string`

      The action taken when the limit is reached (notify_only or notify_and_pause).

    - `limit_usd: optional number`

      The spend limit threshold in USD cents.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "workspace_spend_limit_created"`

      - `"workspace_spend_limit_created"`

    - `workspace_id: optional string`

      Tagged ID of the workspace.

  - `WorkspaceSpendLimitDeleted object { actor, id, created_at, 5 more }`

    A workspace-level API spend limit was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `spend_limit_id: optional string`

      UUID of the deleted spend limit.

    - `type: optional "workspace_spend_limit_deleted"`

      - `"workspace_spend_limit_deleted"`

    - `workspace_id: optional string`

      Tagged ID of the workspace.

- `first_id: optional string`

- `has_more: optional boolean`

- `last_id: optional string`

### Example

```http
curl https://api.anthropic.com/v1/compliance/activities \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "data": [
    {
      "actor": {
        "email_address": "dev@stainless.com",
        "ip_address": "ip_address",
        "user_agent": "user_agent",
        "user_id": "user_id",
        "type": "user_actor"
      },
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "organization_id": "organization_id",
      "organization_uuid": "organization_uuid",
      "type": "account_deleted"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

## Domain Types

### Activity List Response

- `ActivityListResponse = object { actor, id, created_at, 3 more }  or object { actor, admin_api_key_id, scopes, 5 more }  or object { actor, admin_api_key_id, id, 4 more }  or 302 more`

  User-initiated self-service account deletion.

  - `AccountDeleted object { actor, id, created_at, 3 more }`

    User-initiated self-service account deletion.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "account_deleted"`

      - `"account_deleted"`

  - `AdminAPIKeyCreated object { actor, admin_api_key_id, scopes, 5 more }`

    An admin API key was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `admin_api_key_id: string`

      Tagged ID of the created admin API key

    - `scopes: array of string`

      Scopes granted to the key (empty for legacy non-scoped admin keys)

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "admin_api_key_created"`

      - `"admin_api_key_created"`

  - `AdminAPIKeyDeleted object { actor, admin_api_key_id, id, 4 more }`

    An admin API key was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `admin_api_key_id: string`

      Tagged ID of the deleted admin API key

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "admin_api_key_deleted"`

      - `"admin_api_key_deleted"`

  - `AdminAPIKeyUpdated object { actor, admin_api_key_id, updates, 5 more }`

    An admin API key was updated (renamed or activated/deactivated).

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `admin_api_key_id: string`

      Tagged ID of the updated admin API key

    - `updates: array of object { current_value, previous_value, type }`

      - `current_value: string`

      - `previous_value: string`

      - `type: "name" or "status"`

        - `"name"`

        - `"status"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "admin_api_key_updated"`

      - `"admin_api_key_updated"`

  - `AdminConnectorRequestResolved object { actor, decision, mcp_server_id, 6 more }`

    Admin approved or dismissed pending member requests to enable an MCP connector.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `decision: "approved" or "dismissed"`

      - `"approved"`

      - `"dismissed"`

    - `mcp_server_id: string`

    - `resolved_count: number`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "admin_connector_request_resolved"`

      - `"admin_connector_request_resolved"`

  - `AdminRequestCreated object { actor, request_type, id, 4 more }`

    Admin request created by an org member (seat upgrade, limit increase, join org, end-user invite).

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `request_type: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "admin_request_created"`

      - `"admin_request_created"`

  - `AgeVerified object { actor, id, created_at, 3 more }`

    User age was verified.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "age_verified"`

      - `"age_verified"`

  - `AnonymousMobileLoginAttempted object { actor, id, created_at, 3 more }`

    Anonymous mobile login was attempted.

    - `actor: object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `ip_address: string`

      - `user_agent: string`

      - `type: optional "unauthenticated_user_actor"`

        - `"unauthenticated_user_actor"`

      - `unauthenticated_email_address: optional string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "anonymous_mobile_login_attempted"`

      - `"anonymous_mobile_login_attempted"`

  - `APIKeyCreated object { actor, api_key_id, scopes, 5 more }`

    Activity logged when a new API key is created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `api_key_id: string`

      The tagged ID of the created API key

    - `scopes: array of string`

      The scopes for this API key

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "api_key_created"`

      - `"api_key_created"`

  - `ClaudeArtifactAccessFailed object { actor, claude_artifact_id, claude_artifact_version_id, 5 more }`

    An attempt to access an artifact failed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `claude_artifact_id: string`

    - `claude_artifact_version_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_artifact_access_failed"`

      - `"claude_artifact_access_failed"`

  - `ClaudeArtifactCreated object { actor, claude_artifact_id, id, 4 more }`

    An artifact was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_artifact_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_artifact_created"`

      - `"claude_artifact_created"`

  - `ClaudePublishedArtifactDeleted object { actor, claude_published_artifact_id, id, 4 more }`

    A published artifact was unpublished/deleted by its creator.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_published_artifact_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_published_artifact_deleted"`

      - `"claude_published_artifact_deleted"`

  - `ClaudeArtifactPublished object { actor, artifact_type, claude_published_artifact_id, 6 more }`

    An artifact was published and made publicly accessible.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `artifact_type: string`

      Artifact type (code, html, react, etc.)

    - `claude_published_artifact_id: string`

    - `title: string`

      Title of the published artifact

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_artifact_published"`

      - `"claude_artifact_published"`

  - `ClaudeArtifactSharingUpdated object { actor, audience, claude_artifact_id, 6 more }`

    An artifact's sharing settings were updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `audience: array of object { type }`

      Sharing audience for the project. If empty, this it's only visible to the creating user.

      - `type: optional "organization"`

        - `"organization"`

    - `claude_artifact_id: string`

    - `claude_artifact_version_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_artifact_sharing_updated"`

      - `"claude_artifact_sharing_updated"`

  - `ClaudeArtifactViewed object { actor, claude_artifact_id, id, 4 more }`

    An artifact was viewed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_artifact_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_artifact_viewed"`

      - `"claude_artifact_viewed"`

  - `AuditLogExportAccessed object { actor, id, created_at, 3 more }`

    Audit log export file was accessed/downloaded via signed URL.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "audit_log_export_accessed"`

      - `"audit_log_export_accessed"`

  - `AuditLogExportStarted object { actor, id, created_at, 5 more }`

    Audit log export was initiated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `from_date: optional string`

      Start date of the export range

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `to_date: optional string`

      End date of the export range

    - `type: optional "audit_log_export_started"`

      - `"audit_log_export_started"`

  - `BillingEmailsUpdated object { actor, id, cc_email_count, 6 more }`

    The organization's billing email recipients were updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `cc_email_count: optional number`

      Number of 'cc' email recipients.

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `primary_email_set: optional boolean`

      Whether a primary billing email is configured.

    - `to_email_count: optional number`

      Number of 'to' email recipients.

    - `type: optional "billing_emails_updated"`

      - `"billing_emails_updated"`

  - `ClaudeChatAccessFailed object { actor, claude_chat_id, id, 4 more }`

    An attempt to access a chat failed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `claude_chat_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_chat_access_failed"`

      - `"claude_chat_access_failed"`

  - `ClaudeChatCreated object { actor, claude_chat_id, id, 5 more }`

    User created a chat.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_chat_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `claude_project_id: optional string`

      Project ID this chat belongs to, if any

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_chat_created"`

      - `"claude_chat_created"`

  - `ClaudeChatDeleted object { actor, claude_chat_id, id, 5 more }`

    User deleted a chat.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_chat_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `claude_project_id: optional string`

      Project ID this chat belongs to, if any

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_chat_deleted"`

      - `"claude_chat_deleted"`

  - `ClaudeChatDeletionFailed object { actor, claude_chat_id, id, 4 more }`

    A request to delete a chat failed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `claude_chat_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_chat_deletion_failed"`

      - `"claude_chat_deletion_failed"`

  - `ClaudeChatSettingsUpdated object { actor, claude_chat_id, id, 5 more }`

    User updated the settings for a conversation.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_chat_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `claude_project_id: optional string`

      Project ID this chat belongs to, if any

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_chat_settings_updated"`

      - `"claude_chat_settings_updated"`

  - `ClaudeChatSnapshotCreated object { actor, claude_chat_id, claude_chat_snapshot_id, 5 more }`

    User created/shared a chat snapshot.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_chat_id: string`

    - `claude_chat_snapshot_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_chat_snapshot_created"`

      - `"claude_chat_snapshot_created"`

  - `ClaudeChatSnapshotViewed object { actor, claude_chat_snapshot_id, id, 5 more }`

    User viewed a chat snapshot (authenticated or public/unauthenticated).

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `claude_chat_snapshot_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `claude_chat_id: optional string`

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_chat_snapshot_viewed"`

      - `"claude_chat_snapshot_viewed"`

  - `ClaudeChatUpdated object { actor, claude_chat_id, id, 5 more }`

    User updated the chat metadata (e.g name, model).

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_chat_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `claude_project_id: optional string`

      Project ID this chat belongs to, if any

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_chat_updated"`

      - `"claude_chat_updated"`

  - `ClaudeChatViewed object { actor, claude_chat_id, id, 5 more }`

    User viewed a chat.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_chat_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `claude_project_id: optional string`

      Project ID this chat belongs to, if any

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_chat_viewed"`

      - `"claude_chat_viewed"`

  - `ClaudeCodeReviewConfigUpdated object { actor, enabled, id, 7 more }`

    Claude Code Review configuration was enabled/disabled for an org.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `enabled: boolean`

      Whether code review is now enabled

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `environment_id: optional string`

      Environment used for code review

    - `model: optional string`

      Model configured for code review

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `per_review_limit_usd: optional string`

      Per-review spend limit in USD

    - `type: optional "claude_code_review_config_updated"`

      - `"claude_code_review_config_updated"`

  - `ClaudeCodeReviewRepositoryAdded object { actor, config_id, repo_name, 7 more }`

    A repository was added to org-level Claude Code Review configuration.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `config_id: string`

      ID of the repository configuration

    - `repo_name: string`

      Repository name

    - `repo_owner: string`

      Repository owner (GitHub org/user)

    - `trigger_mode: string`

      When code review is triggered

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_code_review_repository_added"`

      - `"claude_code_review_repository_added"`

  - `ClaudeCodeReviewRepositoryRemoved object { actor, config_id, repo_name, 6 more }`

    A repository was removed from org-level Claude Code Review configuration.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `config_id: string`

      ID of the deleted repository configuration

    - `repo_name: string`

      Repository name at deletion time

    - `repo_owner: string`

      Repository owner at deletion time

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_code_review_repository_removed"`

      - `"claude_code_review_repository_removed"`

  - `ClaudeCodeReviewRepositoryUpdated object { actor, config_id, repo_name, 8 more }`

    A Claude Code Review repository configuration was updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `config_id: string`

      ID of the repository configuration

    - `repo_name: string`

      Repository name

    - `repo_owner: string`

      Repository owner

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `status: optional string`

      Updated status (ACTIVE/INACTIVE)

    - `trigger_mode: optional string`

      Updated trigger mode

    - `type: optional "claude_code_review_repository_updated"`

      - `"claude_code_review_repository_updated"`

  - `ClaudeCodeSecurityCenterConfigUpdated object { actor, enabled, id, 5 more }`

    Claude Code Security Center scanning was enabled/disabled for an org.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `enabled: boolean`

      Whether Security Center is now enabled

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `environment_id: optional string`

      Environment used for security scanning

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_code_security_center_config_updated"`

      - `"claude_code_security_center_config_updated"`

  - `ClaudeCodeSecurityScanCancelled object { actor, scan_project_id, scans_cancelled, 5 more }`

    In-flight Claude Code Security scans were cancelled for a project.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `scan_project_id: string`

      Tagged ID of the scan project

    - `scans_cancelled: number`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_code_security_scan_cancelled"`

      - `"claude_code_security_scan_cancelled"`

  - `ClaudeCodeSecurityScanProjectUpdated object { action, actor, scan_project_id, 5 more }`

    A Claude Code Security scan project was archived or unarchived.

    - `action: "archived" or "unarchived"`

      - `"archived"`

      - `"unarchived"`

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `scan_project_id: string`

      Tagged ID of the scan project

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_code_security_scan_project_updated"`

      - `"claude_code_security_scan_project_updated"`

  - `ClaudeCodeSecurityScanScheduleDeleted object { actor, scan_project_id, id, 4 more }`

    A recurring scan schedule was deleted for a Claude Code Security project.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `scan_project_id: string`

      Tagged ID of the scan project

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_code_security_scan_schedule_deleted"`

      - `"claude_code_security_scan_schedule_deleted"`

  - `ClaudeCodeSecurityScanScheduleUpdated object { actor, cadence, scan_project_id, 5 more }`

    A recurring scan schedule was set or replaced for a Claude Code Security project.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `cadence: string`

    - `scan_project_id: string`

      Tagged ID of the scan project

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_code_security_scan_schedule_updated"`

      - `"claude_code_security_scan_schedule_updated"`

  - `ClaudeCodeSecurityWebhookCreated object { actor, scan_project_id, url, 6 more }`

    An outbound webhook was created for a Claude Code Security scan project.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `scan_project_id: string`

      Tagged ID of the scan project

    - `url: string`

    - `webhook_id: string`

      Tagged ID of the webhook

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_code_security_webhook_created"`

      - `"claude_code_security_webhook_created"`

  - `ClaudeCodeSecurityWebhookDeleted object { actor, scan_project_id, webhook_id, 5 more }`

    An outbound webhook for a Claude Code Security scan project was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `scan_project_id: string`

      Tagged ID of the scan project

    - `webhook_id: string`

      Tagged ID of the webhook

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_code_security_webhook_deleted"`

      - `"claude_code_security_webhook_deleted"`

  - `ClaudeCodeSecurityWebhookSecretUpdated object { actor, scan_project_id, webhook_id, 5 more }`

    The HMAC signing secret for a Claude Code Security webhook was rotated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `scan_project_id: string`

      Tagged ID of the scan project

    - `webhook_id: string`

      Tagged ID of the webhook

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_code_security_webhook_secret_updated"`

      - `"claude_code_security_webhook_secret_updated"`

  - `ClaudeCodeSecurityWebhookUpdated object { actor, scan_project_id, webhook_id, 5 more }`

    An outbound webhook for a Claude Code Security scan project was updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `scan_project_id: string`

      Tagged ID of the scan project

    - `webhook_id: string`

      Tagged ID of the webhook

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_code_security_webhook_updated"`

      - `"claude_code_security_webhook_updated"`

  - `ClaudeCodeTeamMemoryACLUpdated object { action, actor, group_id, 6 more }`

    An RBAC group was added to or removed from the Claude Code team-memory ACL.

    - `action: "removed" or "set"`

      Whether the group was set (added/updated) or removed

      - `"removed"`

      - `"set"`

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `group_id: string`

      Tagged ID of the RBAC group

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `access_level: optional string`

      Access level granted (when action=set)

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_code_team_memory_acl_updated"`

      - `"claude_code_team_memory_acl_updated"`

  - `CliPluginExecPolicyUpdated object { actor, cli_name, marketplace_id, 9 more }`

    Admin set or cleared the per-op permission ceiling for a plugin CLI.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `cli_name: string`

      CLI name as declared by the plugin manifest

    - `marketplace_id: string`

      Marketplace ID owning the plugin

    - `max_permission: string`

      New max_permission value ('allow' | 'ask' | 'blocked'), or null when cleared

    - `op_name: string`

      Op name (or '*' for the per-CLI default)

    - `plugin_id: string`

      Plugin ID resolved from the URL

    - `plugin_name: string`

      Plugin name within its marketplace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "cli_plugin_exec_policy_updated"`

      - `"cli_plugin_exec_policy_updated"`

  - `ClaudeCommandCreated object { actor, id, command_id, 5 more }`

    Command was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `command_id: optional string`

    - `command_name: optional string`

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_command_created"`

      - `"claude_command_created"`

  - `ClaudeCommandDeleted object { actor, id, command_id, 5 more }`

    Command was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `command_id: optional string`

    - `command_name: optional string`

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_command_deleted"`

      - `"claude_command_deleted"`

  - `ClaudeCommandReplaced object { actor, id, command_id, 5 more }`

    Command was replaced.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `command_id: optional string`

    - `command_name: optional string`

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_command_replaced"`

      - `"claude_command_replaced"`

  - `ComplianceAPIAccessed object { actor, request_id, request_method, 8 more }`

    Logging event auto-generated for each compliance API request.

    - `actor: object { api_key_id, ip_address, user_agent, type }`

      - `api_key_id: string`

      - `ip_address: string`

      - `user_agent: string`

      - `type: optional "api_actor"`

        - `"api_actor"`

    - `request_id: string`

    - `request_method: "DELETE" or "GET" or "POST" or "PUT"`

      - `"DELETE"`

      - `"GET"`

      - `"POST"`

      - `"PUT"`

    - `status_code: number`

      HTTP status code

    - `url: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `request_body: optional string`

      Serialized JSON request body

    - `type: optional "compliance_api_accessed"`

      - `"compliance_api_accessed"`

  - `DesktopExtensionAllowlisted object { actor, extension_id, id, 4 more }`

    A desktop extension was added to an org's allowlist.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `extension_id: string`

      Allowlisted DXT extension ID

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "desktop_extension_allowlisted"`

      - `"desktop_extension_allowlisted"`

  - `DesktopExtensionBlocklisted object { actor, extension_id, id, 4 more }`

    A desktop extension was added to the global blocklist.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `extension_id: string`

      Blocklisted DXT extension ID

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "desktop_extension_blocklisted"`

      - `"desktop_extension_blocklisted"`

  - `DesktopExtensionDeleted object { actor, extension_id, id, 5 more }`

    A desktop extension was deleted, either globally by an admin or org-scoped by an org owner.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `extension_id: string`

      DXT extension ID

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "desktop_extension_deleted"`

      - `"desktop_extension_deleted"`

    - `version: optional string`

      Specific version deleted (null if all versions)

  - `DesktopExtensionRemovedFromAllowlist object { actor, extension_id, id, 4 more }`

    A desktop extension was removed from an org's allowlist.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `extension_id: string`

      DXT extension ID removed from allowlist

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "desktop_extension_removed_from_allowlist"`

      - `"desktop_extension_removed_from_allowlist"`

  - `DesktopExtensionUnblocked object { actor, extension_id, id, 4 more }`

    A desktop extension was removed from the global blocklist.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `extension_id: string`

      Unblocked DXT extension ID

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "desktop_extension_unblocked"`

      - `"desktop_extension_unblocked"`

  - `DesktopExtensionUploaded object { actor, extension_id, version, 5 more }`

    A desktop extension was uploaded, either globally by an admin or org-scoped by an org owner.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `extension_id: string`

      DXT extension ID

    - `version: string`

      Version string from the manifest

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "desktop_extension_uploaded"`

      - `"desktop_extension_uploaded"`

  - `DesktopExtensionVersionUploaded object { actor, extension_id, version, 5 more }`

    A new version of an existing org-owned desktop extension was uploaded.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `extension_id: string`

      DXT extension ID

    - `version: string`

      Version string from the manifest

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "desktop_extension_version_uploaded"`

      - `"desktop_extension_version_uploaded"`

  - `DomainClaimInitiated object { actor, id, created_at, 3 more }`

    Domain capture claim initiated over personal accounts on verified domains.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "domain_claim_initiated"`

      - `"domain_claim_initiated"`

  - `EndUserInviteRequested object { actor, invitee_email, id, 4 more }`

    Non-admin member submitted an invite request for a new org member.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `invitee_email: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "end_user_invite_requested"`

      - `"end_user_invite_requested"`

  - `ExtraUsageBillingEnabled object { actor, id, created_at, 3 more }`

    Usage credit billing was enabled for an organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "extra_usage_billing_enabled"`

      - `"extra_usage_billing_enabled"`

  - `ExtraUsageCreditGranted object { actor, id, created_at, 3 more }`

    A promotional usage credit grant was claimed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "extra_usage_credit_granted"`

      - `"extra_usage_credit_granted"`

  - `ExtraUsageSpendLimitCreated object { actor, id, amount, 8 more }`

    Usage credit spend limit was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }  or object { api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `amount: optional number`

      The monthly credit limit amount in minor units (e.g. cents).

    - `created_at: optional string`

      When this activity occurred.

    - `is_enabled: optional boolean`

      Whether the spend limit is enabled.

    - `limit_type: optional string`

      The type of spend limit created (e.g. organization, seat_tier, member, service, group).

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `spend_limit_id: optional string`

      Tagged ID of the spend limit.

    - `type: optional "extra_usage_spend_limit_created"`

      - `"extra_usage_spend_limit_created"`

    - `user_id: optional string`

      Tagged ID of the user who performed the action.

  - `ExtraUsageSpendLimitDeleted object { actor, id, created_at, 5 more }`

    Usage credit spend limit was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }  or object { api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `spend_limit_id: optional string`

      Tagged ID of the spend limit.

    - `type: optional "extra_usage_spend_limit_deleted"`

      - `"extra_usage_spend_limit_deleted"`

    - `user_id: optional string`

      Tagged ID of the user who performed the action.

  - `ExtraUsageSpendLimitIncreaseRequestApproved object { actor, id, amount, 7 more }`

    A usage credit spend limit increase request was approved.

    - `actor: object { api_key_id, ip_address, user_agent, type }`

      - `api_key_id: string`

      - `ip_address: string`

      - `user_agent: string`

      - `type: optional "api_actor"`

        - `"api_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `amount: optional number`

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `requester_user_id: optional string`

    - `spend_limit_id: optional string`

    - `spend_limit_increase_request_id: optional string`

    - `type: optional "extra_usage_spend_limit_increase_request_approved"`

      - `"extra_usage_spend_limit_increase_request_approved"`

  - `ExtraUsageSpendLimitIncreaseRequestDenied object { actor, id, created_at, 5 more }`

    A usage credit spend limit increase request was denied.

    - `actor: object { api_key_id, ip_address, user_agent, type }`

      - `api_key_id: string`

      - `ip_address: string`

      - `user_agent: string`

      - `type: optional "api_actor"`

        - `"api_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `requester_user_id: optional string`

    - `spend_limit_increase_request_id: optional string`

    - `type: optional "extra_usage_spend_limit_increase_request_denied"`

      - `"extra_usage_spend_limit_increase_request_denied"`

  - `ExtraUsageSpendLimitUpdated object { actor, id, amount, 8 more }`

    Usage credit spend limit was updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }  or object { api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `amount: optional number`

      The new monthly credit limit amount in minor units (e.g. cents).

    - `created_at: optional string`

      When this activity occurred.

    - `is_enabled: optional boolean`

      Whether the spend limit is enabled.

    - `limit_type: optional string`

      The type of spend limit updated (e.g. organization, seat_tier, member, service, group).

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `spend_limit_id: optional string`

      Tagged ID of the spend limit.

    - `type: optional "extra_usage_spend_limit_updated"`

      - `"extra_usage_spend_limit_updated"`

    - `user_id: optional string`

      Tagged ID of the user who performed the action.

  - `ClaudeFileAccessFailed object { actor, claude_file_id, filename, 7 more }`

    An attempt to access a file failed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `claude_file_id: string`

    - `filename: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `claude_artifact_id: optional string`

      Artifact ID if file was accessed via an artifact

    - `claude_project_id: optional string`

      Project ID if file was accessed via a project

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_file_access_failed"`

      - `"claude_file_access_failed"`

  - `ClaudeFileDeleted object { actor, claude_file_id, filename, 5 more }`

    A file was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_file_id: string`

    - `filename: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_file_deleted"`

      - `"claude_file_deleted"`

  - `ClaudeFileUploaded object { actor, claude_file_id, filename, 7 more }`

    A file was uploaded.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_file_id: string`

    - `filename: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `claude_chat_id: optional string`

      Chat ID if file was uploaded to a chat

    - `claude_project_id: optional string`

      Project ID if file was uploaded to a project

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_file_uploaded"`

      - `"claude_file_uploaded"`

  - `ClaudeFileViewed object { actor, claude_file_id, filename, 7 more }`

    A file was viewed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_file_id: string`

    - `filename: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `claude_artifact_id: optional string`

      Artifact ID if file was accessed via an artifact

    - `claude_project_id: optional string`

      Project ID if file was accessed via a project

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_file_viewed"`

      - `"claude_file_viewed"`

  - `GheConfigurationCreated object { actor, ghe_configuration_id, id, 4 more }`

    Admin created a GHE configuration.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `ghe_configuration_id: string`

      ID of the GHE configuration

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "ghe_configuration_created"`

      - `"ghe_configuration_created"`

  - `GheConfigurationDeleted object { actor, ghe_configuration_id, id, 4 more }`

    Admin deleted a GHE configuration.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `ghe_configuration_id: string`

      ID of the GHE configuration

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "ghe_configuration_deleted"`

      - `"ghe_configuration_deleted"`

  - `GheConfigurationUpdated object { actor, ghe_configuration_id, id, 4 more }`

    Admin updated a GHE configuration.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `ghe_configuration_id: string`

      ID of the GHE configuration

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "ghe_configuration_updated"`

      - `"ghe_configuration_updated"`

  - `GheUserConnected object { actor, id, created_at, 4 more }`

    User connected to a GHE instance.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `ghe_configuration_id: optional string`

      ID of the GHE configuration

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "ghe_user_connected"`

      - `"ghe_user_connected"`

  - `GheUserDisconnected object { actor, id, created_at, 4 more }`

    User disconnected from a GHE instance.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `ghe_configuration_id: optional string`

      ID of the GHE configuration

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "ghe_user_disconnected"`

      - `"ghe_user_disconnected"`

  - `GheWebhookSignatureInvalid object { actor, ghe_configuration_id, id, 4 more }`

    Webhook signature validation failed.

    - `actor: object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `ip_address: string`

      - `user_agent: string`

      - `type: optional "unauthenticated_user_actor"`

        - `"unauthenticated_user_actor"`

      - `unauthenticated_email_address: optional string`

    - `ghe_configuration_id: string`

      ID of the GHE configuration

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "ghe_webhook_signature_invalid"`

      - `"ghe_webhook_signature_invalid"`

  - `ClaudeGitHubIntegrationCreated object { actor, integration_id, id, 6 more }`

    A GitHub integration was enabled for the organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `integration_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_name: optional string`

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `repository_name: optional string`

    - `type: optional "claude_github_integration_created"`

      - `"claude_github_integration_created"`

  - `ClaudeGitHubIntegrationDeleted object { actor, integration_id, id, 6 more }`

    A GitHub integration was disabled for the organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `integration_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_name: optional string`

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `repository_name: optional string`

    - `type: optional "claude_github_integration_deleted"`

      - `"claude_github_integration_deleted"`

  - `ClaudeGitHubIntegrationUpdated object { actor, integration_id, id, 6 more }`

    A GitHub integration's configuration was updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `integration_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_name: optional string`

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `repository_name: optional string`

    - `type: optional "claude_github_integration_updated"`

      - `"claude_github_integration_updated"`

  - `ClaudeGdriveIntegrationCreated object { actor, integration_id, id, 5 more }`

    A Google Drive integration was enabled for the organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `integration_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `folder_id: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_gdrive_integration_created"`

      - `"claude_gdrive_integration_created"`

  - `ClaudeGdriveIntegrationDeleted object { actor, integration_id, id, 5 more }`

    A Google Drive integration was disabled for the organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `integration_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `folder_id: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_gdrive_integration_deleted"`

      - `"claude_gdrive_integration_deleted"`

  - `ClaudeGdriveIntegrationUpdated object { actor, integration_id, id, 5 more }`

    A Google Drive integration's configuration was updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `integration_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `folder_id: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_gdrive_integration_updated"`

      - `"claude_gdrive_integration_updated"`

  - `GroupCreated object { actor, group_id, group_name, 5 more }`

    A group was created (RBAC admin or SCIM provisioning).

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }  or object { directory_id, workos_event_id, idp_connection_type, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

    - `group_id: string`

      Tagged ID of the created group

    - `group_name: string`

      Name of the created group

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "group_created"`

      - `"group_created"`

  - `GroupDeleted object { actor, group_id, id, 4 more }`

    A group was deleted (RBAC admin or SCIM provisioning).

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }  or object { directory_id, workos_event_id, idp_connection_type, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

    - `group_id: string`

      Tagged ID of the deleted group

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "group_deleted"`

      - `"group_deleted"`

  - `GroupListViewed object { actor, id, created_at, 3 more }`

    Admin viewed the list of RBAC groups.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "group_list_viewed"`

      - `"group_list_viewed"`

  - `GroupMemberAdded object { actor, group_id, member_ids, 5 more }`

    One or more members were added to a group.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }  or object { directory_id, workos_event_id, idp_connection_type, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

    - `group_id: string`

      Tagged ID of the group

    - `member_ids: array of string`

      Tagged IDs of the members added

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "group_member_added"`

      - `"group_member_added"`

  - `GroupMemberListViewed object { actor, group_id, id, 4 more }`

    Admin viewed the members of an RBAC group.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `group_id: string`

      Tagged ID of the group

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "group_member_list_viewed"`

      - `"group_member_list_viewed"`

  - `GroupMemberRemoved object { actor, group_id, member_ids, 5 more }`

    One or more members were removed from a group.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }  or object { directory_id, workos_event_id, idp_connection_type, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

    - `group_id: string`

      Tagged ID of the group

    - `member_ids: array of string`

      Tagged IDs of the members removed

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "group_member_removed"`

      - `"group_member_removed"`

  - `GroupUpdated object { actor, group_id, id, 4 more }`

    A group was updated (RBAC admin or SCIM provisioning).

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }  or object { directory_id, workos_event_id, idp_connection_type, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

    - `group_id: string`

      Tagged ID of the updated group

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "group_updated"`

      - `"group_updated"`

  - `GroupViewed object { actor, group_id, id, 4 more }`

    A group was viewed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

    - `group_id: string`

      Tagged ID of the viewed group

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "group_viewed"`

      - `"group_viewed"`

  - `IntegrationUserConnected object { actor, id, created_at, 4 more }`

    User connected to an integration.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `integration_type: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "integration_user_connected"`

      - `"integration_user_connected"`

  - `IntegrationUserDisconnected object { actor, id, created_at, 4 more }`

    User disconnected from an integration.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `integration_type: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "integration_user_disconnected"`

      - `"integration_user_disconnected"`

  - `InvoiceCollectionMethodUpdated object { actor, id, created_at, 4 more }`

    Invoice collection method was changed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `new_collection_method: optional string`

      New collection method (e.g. charge_automatically, send_invoice).

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "invoice_collection_method_updated"`

      - `"invoice_collection_method_updated"`

  - `UserLoggedOut object { actor, id, created_at, 3 more }`

    A user signed out of one or all sessions.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "user_logged_out"`

      - `"user_logged_out"`

  - `LtiLaunchInitiated object { actor, id, created_at, 3 more }`

    LTI launch was initiated.

    - `actor: object { ip_address, user_agent, type, unauthenticated_email_address }  or object { email_address, ip_address, user_agent, 2 more }`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "lti_launch_initiated"`

      - `"lti_launch_initiated"`

  - `LtiLaunchSuccess object { actor, id, created_at, 3 more }`

    LTI launch completed successfully.

    - `actor: object { ip_address, user_agent, type, unauthenticated_email_address }  or object { email_address, ip_address, user_agent, 2 more }`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "lti_launch_success"`

      - `"lti_launch_success"`

  - `LtiPlatformCreated object { actor, lti_platform_id, lti_platform_issuer, 5 more }`

    Admin created an LTI platform integration.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `lti_platform_id: string`

      UUID of the LTI platform

    - `lti_platform_issuer: string`

      Platform issuer URL

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "lti_platform_created"`

      - `"lti_platform_created"`

  - `LtiPlatformUpdated object { actor, lti_platform_id, id, 5 more }`

    Admin updated an LTI platform integration.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `lti_platform_id: string`

      UUID of the LTI platform

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `lti_platform_issuer: optional string`

      Platform issuer URL

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "lti_platform_updated"`

      - `"lti_platform_updated"`

  - `MagicLinkLoginFailed object { actor, id, created_at, 3 more }`

    A magic link sign-in attempt failed.

    - `actor: object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `ip_address: string`

      - `user_agent: string`

      - `type: optional "unauthenticated_user_actor"`

        - `"unauthenticated_user_actor"`

      - `unauthenticated_email_address: optional string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "magic_link_login_failed"`

      - `"magic_link_login_failed"`

  - `MagicLinkLoginInitiated object { actor, id, created_at, 3 more }`

    A user requested a magic link sign-in email.

    - `actor: object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `ip_address: string`

      - `user_agent: string`

      - `type: optional "unauthenticated_user_actor"`

        - `"unauthenticated_user_actor"`

      - `unauthenticated_email_address: optional string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "magic_link_login_initiated"`

      - `"magic_link_login_initiated"`

  - `MagicLinkLoginSucceeded object { actor, id, auth_method, 5 more }`

    A user successfully signed in with a magic link email.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `auth_method: optional "magic_link"`

      The method the user used to authenticate. May be absent on activities recorded before this field was introduced.

      - `"magic_link"`

    - `created_at: optional string`

      When this activity occurred.

    - `mfa_method: optional "not_used"`

      The second authentication factor performed during this login, if any. `null` when the second-factor status is not recorded on this event — for example, when authentication was delegated to an external identity provider and any second factor is not visible to Anthropic, or when this event is one step of a multi-step login whose MFA is reported on another activity. May be absent on activities recorded before this field was introduced.

      - `"not_used"`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "magic_link_login_succeeded"`

      - `"magic_link_login_succeeded"`

  - `ManagedOrganizationSetupCompleted object { actor, id, created_at, 3 more }`

    Managed (AWS Marketplace) organization setup was completed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "managed_organization_setup_completed"`

      - `"managed_organization_setup_completed"`

  - `MarketplaceCreated object { actor, marketplace_id, id, 4 more }`

    Admin created an organization marketplace.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `marketplace_id: string`

      Tagged ID of the marketplace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "marketplace_created"`

      - `"marketplace_created"`

  - `MarketplaceDeleted object { actor, marketplace_id, id, 4 more }`

    Admin deleted an organization marketplace.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `marketplace_id: string`

      Tagged ID of the marketplace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "marketplace_deleted"`

      - `"marketplace_deleted"`

  - `MarketplaceUpdated object { actor, marketplace_id, id, 4 more }`

    Admin updated an organization marketplace.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `marketplace_id: string`

      Tagged ID of the marketplace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "marketplace_updated"`

      - `"marketplace_updated"`

  - `MarketplaceWebhookDeleted object { actor, marketplace_id, id, 4 more }`

    Admin removed the GitHub push webhook for a marketplace.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `marketplace_id: string`

      Tagged ID of the marketplace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "marketplace_webhook_deleted"`

      - `"marketplace_webhook_deleted"`

  - `MarketplaceWebhookProvisioned object { actor, marketplace_id, id, 5 more }`

    Admin provisioned a GitHub push webhook for a marketplace.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `marketplace_id: string`

      Tagged ID of the marketplace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `github_webhook_id: optional number`

      GitHub-assigned webhook ID returned by the hooks API

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "marketplace_webhook_provisioned"`

      - `"marketplace_webhook_provisioned"`

  - `McpServerCreated object { actor, mcp_server_id, mcp_server_name, 5 more }`

    An MCP server was added to the organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `mcp_server_id: string`

      Tagged ID of the MCP server

    - `mcp_server_name: string`

      Display name of the MCP server

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "mcp_server_created"`

      - `"mcp_server_created"`

  - `McpServerDeleted object { actor, mcp_server_id, mcp_server_name, 5 more }`

    An MCP server was removed from the organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `mcp_server_id: string`

      Tagged ID of the MCP server

    - `mcp_server_name: string`

      Display name of the MCP server

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "mcp_server_deleted"`

      - `"mcp_server_deleted"`

  - `McpServerUpdated object { actor, mcp_server_id, mcp_server_name, 5 more }`

    An MCP server's configuration was updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `mcp_server_id: string`

      Tagged ID of the MCP server

    - `mcp_server_name: string`

      Display name of the MCP server

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "mcp_server_updated"`

      - `"mcp_server_updated"`

  - `McpToolPolicyUpdated object { actor, max_permission, mcp_server_id, 7 more }`

    The permission restriction for an MCP tool was set or cleared.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `max_permission: string`

      New max_permission value ('allow' | 'ask' | 'blocked'), or null when cleared

    - `mcp_server_id: string`

      Tagged ID of the MCP server

    - `mcp_server_name: string`

      Display name of the MCP server

    - `tool_name: string`

      Tool name (or '*' for the MCP-server-wide default)

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "mcp_tool_policy_updated"`

      - `"mcp_tool_policy_updated"`

  - `OrgAnalyticsAPICapabilityUpdated object { actor, id, created_at, 3 more }`

    Organization analytics_api capability was enabled or disabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_analytics_api_capability_updated"`

      - `"org_analytics_api_capability_updated"`

  - `OrgBulkDeleteInitiated object { actor, id, created_at, 3 more }`

    Organization bulk deletion was initiated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_bulk_delete_initiated"`

      - `"org_bulk_delete_initiated"`

  - `OrgClaudeCodeDataSharingDisabled object { actor, id, created_at, 3 more }`

    Organization Claude Code data sharing was disabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_claude_code_data_sharing_disabled"`

      - `"org_claude_code_data_sharing_disabled"`

  - `OrgClaudeCodeDataSharingEnabled object { actor, id, created_at, 3 more }`

    Organization Claude Code data sharing was enabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_claude_code_data_sharing_enabled"`

      - `"org_claude_code_data_sharing_enabled"`

  - `OrgClaudeCodeDesktopDisabled object { actor, id, created_at, 3 more }`

    Organization Claude Code Desktop was disabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_claude_code_desktop_disabled"`

      - `"org_claude_code_desktop_disabled"`

  - `OrgClaudeCodeDesktopEnabled object { actor, id, created_at, 3 more }`

    Organization Claude Code Desktop was enabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_claude_code_desktop_enabled"`

      - `"org_claude_code_desktop_enabled"`

  - `OrgComplianceAPISettingsUpdated object { actor, id, compliance_api_enabled, 5 more }`

    Organization compliance API settings were updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }  or object { admin_api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `compliance_api_enabled: optional boolean`

    - `compliance_api_logging_enabled: optional boolean`

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_compliance_api_settings_updated"`

      - `"org_compliance_api_settings_updated"`

  - `OrgCoworkAgentDisabled object { actor, id, created_at, 3 more }`

    Organization Cowork Agent was disabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_cowork_agent_disabled"`

      - `"org_cowork_agent_disabled"`

  - `OrgCoworkAgentEnabled object { actor, id, created_at, 3 more }`

    Organization Cowork Agent was enabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_cowork_agent_enabled"`

      - `"org_cowork_agent_enabled"`

  - `OrgCoworkDisabled object { actor, id, created_at, 3 more }`

    Organization cowork was disabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_cowork_disabled"`

      - `"org_cowork_disabled"`

  - `OrgCoworkEnabled object { actor, id, created_at, 3 more }`

    Organization cowork was enabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_cowork_enabled"`

      - `"org_cowork_enabled"`

  - `OrgCreationBlocked object { actor, id, created_at, 4 more }`

    Organization creation was blocked.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `reason: optional string`

    - `type: optional "org_creation_blocked"`

      - `"org_creation_blocked"`

  - `OrgDataExportAccessed object { actor, id, created_at, 3 more }`

    Organization data export file was accessed/downloaded via signed URL.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_data_export_accessed"`

      - `"org_data_export_accessed"`

  - `OrgDataExportCompleted object { actor, id, created_at, 3 more }`

    Organization data export was completed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_data_export_completed"`

      - `"org_data_export_completed"`

  - `OrgDataExportStarted object { actor, id, created_at, 3 more }`

    Organization data export was started.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_data_export_started"`

      - `"org_data_export_started"`

  - `OrgDeletedViaBulk object { actor, id, created_at, 3 more }`

    Organization was deleted via bulk operation.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_deleted_via_bulk"`

      - `"org_deleted_via_bulk"`

  - `OrgDeletionRequested object { actor, id, created_at, 3 more }`

    Organization deletion was requested.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_deletion_requested"`

      - `"org_deletion_requested"`

  - `OrgDirectoryResyncCompleted object { actor, resync_uuid, id, 4 more }`

    Organization directory resync completed successfully.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `resync_uuid: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_directory_resync_completed"`

      - `"org_directory_resync_completed"`

  - `OrgDirectoryResyncFailed object { actor, resync_uuid, id, 4 more }`

    Organization directory resync failed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `resync_uuid: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_directory_resync_failed"`

      - `"org_directory_resync_failed"`

  - `OrgDirectoryResyncStarted object { actor, resync_uuid, sync_destinations, 5 more }`

    Organization directory resync was started asynchronously.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `resync_uuid: string`

    - `sync_destinations: array of string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_directory_resync_started"`

      - `"org_directory_resync_started"`

  - `OrgDirectorySyncActivated object { actor, id, created_at, 3 more }`

    Organization directory sync was activated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }  or object { directory_id, workos_event_id, idp_connection_type, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_directory_sync_activated"`

      - `"org_directory_sync_activated"`

  - `OrgDirectorySyncAddInitiated object { actor, id, created_at, 3 more }`

    Organization directory sync setup was initiated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_directory_sync_add_initiated"`

      - `"org_directory_sync_add_initiated"`

  - `OrgDirectorySyncDeleted object { actor, id, created_at, 3 more }`

    Organization directory sync was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }  or object { directory_id, workos_event_id, idp_connection_type, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_directory_sync_deleted"`

      - `"org_directory_sync_deleted"`

  - `OrgDiscoverabilityDisabled object { actor, id, created_at, 3 more }`

    Admin disabled organization discoverability.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_discoverability_disabled"`

      - `"org_discoverability_disabled"`

  - `OrgDiscoverabilityEnabled object { actor, id, created_at, 3 more }`

    Admin enabled organization discoverability.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_discoverability_enabled"`

      - `"org_discoverability_enabled"`

  - `OrgDiscoverabilitySettingsUpdated object { actor, id, created_at, 3 more }`

    Admin updated organization discoverability settings.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_discoverability_settings_updated"`

      - `"org_discoverability_settings_updated"`

  - `OrgDomainAddInitiated object { actor, id, created_at, 3 more }`

    Organization domain verification was initiated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_domain_add_initiated"`

      - `"org_domain_add_initiated"`

  - `OrgDomainRemoved object { actor, id, created_at, 4 more }`

    Organization domain was removed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `domain: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_domain_removed"`

      - `"org_domain_removed"`

  - `OrgDomainVerified object { actor, id, created_at, 4 more }`

    Organization domain was verified.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `domain: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_domain_verified"`

      - `"org_domain_verified"`

  - `OrgHipaaSelfServeEnabled object { actor, baa_content_hash, baa_version_label, 6 more }`

    A primary owner click-accepted the BAA and enabled HIPAA protections
    for the organization via the self-serve flow.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `baa_content_hash: string`

    - `baa_version_label: string`

    - `setup_guide_content_hash: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_hipaa_self_serve_enabled"`

      - `"org_hipaa_self_serve_enabled"`

  - `OrgIPRestrictionCreated object { actor, id, created_at, 3 more }`

    Organization IP restriction was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_ip_restriction_created"`

      - `"org_ip_restriction_created"`

  - `OrgIPRestrictionDeleted object { actor, id, created_at, 3 more }`

    Organization IP restriction was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_ip_restriction_deleted"`

      - `"org_ip_restriction_deleted"`

  - `OrgIPRestrictionUpdated object { actor, id, created_at, 3 more }`

    Organization IP restriction was updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_ip_restriction_updated"`

      - `"org_ip_restriction_updated"`

  - `OrgInviteLinkDisabled object { actor, id, created_at, 3 more }`

    Organization invite link was disabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_invite_link_disabled"`

      - `"org_invite_link_disabled"`

  - `OrgInviteLinkGenerated object { actor, id, created_at, 3 more }`

    Organization invite link was generated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_invite_link_generated"`

      - `"org_invite_link_generated"`

  - `OrgInviteLinkRegenerated object { actor, id, created_at, 3 more }`

    Organization invite link was regenerated (previous link invalidated).

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_invite_link_regenerated"`

      - `"org_invite_link_regenerated"`

  - `OrgInviteViewed object { actor, invite_id, id, 4 more }`

    An organization invite was viewed.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `invite_id: string`

      Tagged ID of the viewed invite

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_invite_viewed"`

      - `"org_invite_viewed"`

  - `OrgInvitesListed object { actor, id, created_at, 3 more }`

    Organization invites were listed.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_invites_listed"`

      - `"org_invites_listed"`

  - `OrgJoinProposalDecided object { actor, approved, id, 4 more }`

    Approve or reject decision on a parent-org join proposal.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `approved: boolean`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_join_proposal_decided"`

      - `"org_join_proposal_decided"`

  - `OrgJoinRequestApproved object { actor, id, created_at, 3 more }`

    Admin approved a join request.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_join_request_approved"`

      - `"org_join_request_approved"`

  - `OrgJoinRequestCreated object { actor, id, created_at, 3 more }`

    User requested to join an organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_join_request_created"`

      - `"org_join_request_created"`

  - `OrgJoinRequestDismissed object { actor, id, created_at, 3 more }`

    Admin dismissed a join request.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_join_request_dismissed"`

      - `"org_join_request_dismissed"`

  - `OrgJoinRequestInstantApproved object { actor, id, created_at, 3 more }`

    Join request was instantly approved.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_join_request_instant_approved"`

      - `"org_join_request_instant_approved"`

  - `OrgJoinRequestsBulkDismissed object { actor, id, created_at, 3 more }`

    Admin bulk-dismissed join requests.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_join_requests_bulk_dismissed"`

      - `"org_join_requests_bulk_dismissed"`

  - `OrgMagicLinkSecondFactorToggled object { actor, enabled, id, 4 more }`

    Organization magic link second factor was toggled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `enabled: boolean`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_magic_link_second_factor_toggled"`

      - `"org_magic_link_second_factor_toggled"`

  - `OrgMemberInvitesDisabled object { actor, id, created_at, 3 more }`

    Admin disabled member invites for the organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_member_invites_disabled"`

      - `"org_member_invites_disabled"`

  - `OrgMemberInvitesEnabled object { actor, id, created_at, 3 more }`

    Admin enabled member invites for the organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_member_invites_enabled"`

      - `"org_member_invites_enabled"`

  - `OrgMembersExported object { actor, id, created_at, 3 more }`

    Organization members list was exported as CSV.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_members_exported"`

      - `"org_members_exported"`

  - `OrgParentJoinProposalCreated object { actor, id, created_at, 3 more }`

    Organization parent join proposal was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_parent_join_proposal_created"`

      - `"org_parent_join_proposal_created"`

  - `OrgParentSearchPerformed object { actor, id, created_at, 3 more }`

    Organization parent search was performed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_parent_search_performed"`

      - `"org_parent_search_performed"`

  - `OrgSSOAddInitiated object { actor, id, created_at, 3 more }`

    Organization SSO setup was initiated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_sso_add_initiated"`

      - `"org_sso_add_initiated"`

  - `OrgSSOConnectionActivated object { actor, id, connection_id, 5 more }`

    Organization SSO connection was activated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }  or object { directory_id, workos_event_id, idp_connection_type, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `connection_id: optional string`

    - `connection_type: optional string`

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_sso_connection_activated"`

      - `"org_sso_connection_activated"`

  - `OrgSSOConnectionDeactivated object { actor, id, connection_id, 4 more }`

    Organization SSO connection was deactivated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }  or object { directory_id, workos_event_id, idp_connection_type, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `connection_id: optional string`

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_sso_connection_deactivated"`

      - `"org_sso_connection_deactivated"`

  - `OrgSSOConnectionDeleted object { actor, id, connection_id, 4 more }`

    Organization SSO connection was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }  or object { directory_id, workos_event_id, idp_connection_type, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `connection_id: optional string`

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_sso_connection_deleted"`

      - `"org_sso_connection_deleted"`

  - `OrgSSOGroupRoleMappingsUpdated object { actor, id, created_at, 3 more }`

    Organization SSO group role mappings were updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_sso_group_role_mappings_updated"`

      - `"org_sso_group_role_mappings_updated"`

  - `OrgSSOProvisioningModeChanged object { actor, id, created_at, 5 more }`

    Organization SSO provisioning mode was changed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `new_mode: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `previous_mode: optional string`

    - `type: optional "org_sso_provisioning_mode_changed"`

      - `"org_sso_provisioning_mode_changed"`

  - `OrgSSOSeatTierAssignmentToggled object { actor, enabled, id, 4 more }`

    Organization SSO seat tier assignment was toggled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `enabled: boolean`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_sso_seat_tier_assignment_toggled"`

      - `"org_sso_seat_tier_assignment_toggled"`

  - `OrgSSOSeatTierMappingsUpdated object { actor, id, created_at, 3 more }`

    Organization SSO seat tier mappings were updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_sso_seat_tier_mappings_updated"`

      - `"org_sso_seat_tier_mappings_updated"`

  - `OrgSSOToggled object { actor, enabled, id, 4 more }`

    Organization SSO was toggled on or off.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `enabled: boolean`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_sso_toggled"`

      - `"org_sso_toggled"`

  - `OrgSyncDeletingSynchronizedFilesStarted object { actor, id, created_at, 3 more }`

    Organization started deleting synchronized files.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_sync_deleting_synchronized_files_started"`

      - `"org_sync_deleting_synchronized_files_started"`

  - `OrgSyncSynchronizedFilesDeleted object { actor, id, created_at, 3 more }`

    Organization synchronized files were deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_sync_synchronized_files_deleted"`

      - `"org_sync_synchronized_files_deleted"`

  - `OrgTaintAdded object { actor, id, created_at, 4 more }`

    A taint was added to an organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `taint: optional string`

    - `type: optional "org_taint_added"`

      - `"org_taint_added"`

  - `OrgTaintRemoved object { actor, id, created_at, 4 more }`

    A taint was removed from an organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `taint: optional string`

    - `type: optional "org_taint_removed"`

      - `"org_taint_removed"`

  - `OrgUserDeleted object { actor, id, created_at, 5 more }`

    User was removed from organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }  or object { admin_api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `deleted_user_email: optional string`

    - `deleted_user_id: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_user_deleted"`

      - `"org_user_deleted"`

  - `OrgUserInviteAccepted object { actor, id, created_at, 4 more }`

    Organization user invite was accepted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `invite_id: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_user_invite_accepted"`

      - `"org_user_invite_accepted"`

  - `OrgUserInviteDeleted object { actor, id, created_at, 4 more }`

    Organization user invite was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }  or object { admin_api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `invite_id: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_user_invite_deleted"`

      - `"org_user_invite_deleted"`

  - `OrgUserInviteReSent object { actor, id, created_at, 4 more }`

    Organization user invite was re-sent.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `invited_email: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_user_invite_re_sent"`

      - `"org_user_invite_re_sent"`

  - `OrgUserInviteRejected object { actor, id, created_at, 4 more }`

    Organization user invite was rejected.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `invite_id: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_user_invite_rejected"`

      - `"org_user_invite_rejected"`

  - `OrgUserInviteSent object { actor, id, created_at, 5 more }`

    Organization user invite was sent.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }  or object { admin_api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `invited_email: optional string`

    - `invited_role: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_user_invite_sent"`

      - `"org_user_invite_sent"`

  - `OrgUserLeft object { actor, id, created_at, 4 more }`

    User removed themselves from organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `previous_role: optional string`

    - `type: optional "org_user_left"`

      - `"org_user_left"`

  - `OrgUserViewed object { actor, user_id, id, 4 more }`

    An organization user was viewed.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `user_id: string`

      Tagged ID of the viewed user

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_user_viewed"`

      - `"org_user_viewed"`

  - `OrgUsersListed object { actor, id, created_at, 3 more }`

    Organization users were listed.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_users_listed"`

      - `"org_users_listed"`

  - `OrgWorkAcrossAppsDisabled object { actor, id, created_at, 3 more }`

    Organization Work Across Apps was disabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_work_across_apps_disabled"`

      - `"org_work_across_apps_disabled"`

  - `OrgWorkAcrossAppsEnabled object { actor, id, created_at, 3 more }`

    Organization Work Across Apps was enabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "org_work_across_apps_enabled"`

      - `"org_work_across_apps_enabled"`

  - `OrganizationAddressUpdated object { actor, id, billing_address_updated, 7 more }`

    The organization's billing or shipping address was updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `billing_address_updated: optional boolean`

    - `billing_name_updated: optional boolean`

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `shipping_address_updated: optional boolean`

    - `shipping_name_updated: optional boolean`

    - `type: optional "organization_address_updated"`

      - `"organization_address_updated"`

  - `OrganizationIconDeleted object { actor, id, created_at, 3 more }`

    Organization's custom icon deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "organization_icon_deleted"`

      - `"organization_icon_deleted"`

  - `OrganizationIconUpdated object { actor, id, created_at, 3 more }`

    Organization's custom icon uploaded or replaced.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "organization_icon_updated"`

      - `"organization_icon_updated"`

  - `ClaudeOrganizationSettingsUpdated object { actor, updates, id, 4 more }`

    Organization settings were updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `updates: array of object { current_value, previous_value, type }  or object { current_value, previous_value, type }  or object { current_value, previous_value, type }  or 38 more`

      - `OrganizationName object { current_value, previous_value, type }`

        - `current_value: string`

        - `previous_value: string`

        - `type: optional "name"`

          - `"name"`

      - `OrganizationCapabilities object { current_value, previous_value, type }`

        - `current_value: array of string`

        - `previous_value: array of string`

        - `type: optional "capabilities"`

          - `"capabilities"`

      - `OrganizationRedactContent object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "redact_content"`

          - `"redact_content"`

      - `PublicProjectsEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "public_projects_enabled"`

          - `"public_projects_enabled"`

      - `WebSearchEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "web_search_enabled"`

          - `"web_search_enabled"`

      - `GeolocationEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "geolocation_enabled"`

          - `"geolocation_enabled"`

      - `OrgMemoryEnabledSetting object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "enabled_saffron"`

          - `"enabled_saffron"`

      - `DataRetentionPeriods object { current_value, previous_value, type }`

        - `current_value: array of object { data_type, duration, timescale }`

          - `data_type: "all" or "chat" or "project"`

            - `"all"`

            - `"chat"`

            - `"project"`

          - `duration: number`

          - `timescale: "day" or "indefinite" or "month"`

            - `"day"`

            - `"indefinite"`

            - `"month"`

        - `previous_value: array of object { data_type, duration, timescale }`

          - `data_type: "all" or "chat" or "project"`

            - `"all"`

            - `"chat"`

            - `"project"`

          - `duration: number`

          - `timescale: "day" or "indefinite" or "month"`

            - `"day"`

            - `"indefinite"`

            - `"month"`

        - `type: optional "data_retention_periods"`

          - `"data_retention_periods"`

      - `MembersLimit object { current_value, previous_value, type }`

        - `current_value: number`

        - `previous_value: number`

        - `type: optional "members_limit"`

          - `"members_limit"`

      - `ClaudeAPIInArtifactsEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "claude_api_in_artifacts_enabled"`

          - `"claude_api_in_artifacts_enabled"`

      - `WorkbenchCompletionFeedbackEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "workbench_completion_feedback_enabled"`

          - `"workbench_completion_feedback_enabled"`

      - `ClaudeAICompletionFeedbackEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "claude_ai_completion_feedback_enabled"`

          - `"claude_ai_completion_feedback_enabled"`

      - `ClaudeAIIntegrationSharingEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "claude_ai_integration_sharing_enabled"`

          - `"claude_ai_integration_sharing_enabled"`

      - `ClaudeAIChatSharingEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "claude_ai_chat_sharing_enabled"`

          - `"claude_ai_chat_sharing_enabled"`

      - `ClaudeAiccrSharingEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "claude_ai_ccr_sharing_enabled"`

          - `"claude_ai_ccr_sharing_enabled"`

      - `BatchesDownloadUiVisibility object { current_value, previous_value, type }`

        - `current_value: "all" or "none" or "selected"`

          - `"all"`

          - `"none"`

          - `"selected"`

        - `previous_value: "all" or "none" or "selected"`

          - `"all"`

          - `"none"`

          - `"selected"`

        - `type: optional "batches_download_ui_visibility"`

          - `"batches_download_ui_visibility"`

      - `AllowedInviteDomains object { current_value, previous_value, type }`

        - `current_value: array of string`

        - `previous_value: array of string`

        - `type: optional "allowed_invite_domains"`

          - `"allowed_invite_domains"`

      - `WebSearchAPISettingsChanged object { current_value, previous_value, type }`

        - `current_value: object { domain_filters, is_enabled }`

          - `domain_filters: object { allowed_domains, blocked_domains }`

            Allowed/blocked domain filters shared by web_search and web_fetch tools.

            - `allowed_domains: optional array of string`

            - `blocked_domains: optional array of string`

          - `is_enabled: boolean`

        - `previous_value: object { domain_filters, is_enabled }`

          - `domain_filters: object { allowed_domains, blocked_domains }`

            Allowed/blocked domain filters shared by web_search and web_fetch tools.

            - `allowed_domains: optional array of string`

            - `blocked_domains: optional array of string`

          - `is_enabled: boolean`

        - `type: optional "web_search_api_settings"`

          - `"web_search_api_settings"`

      - `WebFetchAPISettingsChanged object { current_value, previous_value, type }`

        - `current_value: object { domain_filters, is_enabled }`

          - `domain_filters: object { allowed_domains, blocked_domains }`

            Allowed/blocked domain filters shared by web_search and web_fetch tools.

            - `allowed_domains: optional array of string`

            - `blocked_domains: optional array of string`

          - `is_enabled: boolean`

        - `previous_value: object { domain_filters, is_enabled }`

          - `domain_filters: object { allowed_domains, blocked_domains }`

            Allowed/blocked domain filters shared by web_search and web_fetch tools.

            - `allowed_domains: optional array of string`

            - `blocked_domains: optional array of string`

          - `is_enabled: boolean`

        - `type: optional "web_fetch_api_settings"`

          - `"web_fetch_api_settings"`

      - `DefaultWorkspaceSettings object { current_value, previous_value, type }`

        - `current_value: object { enable_api_keys }`

          - `enable_api_keys: optional boolean`

        - `previous_value: object { enable_api_keys }`

          - `enable_api_keys: optional boolean`

        - `type: optional "default_workspace_settings"`

          - `"default_workspace_settings"`

      - `BatchesDownloadUiEnabledWorkspaceIDs object { current_value, previous_value, type }`

        - `current_value: array of string`

        - `previous_value: array of string`

        - `type: optional "batches_download_ui_enabled_workspace_ids"`

          - `"batches_download_ui_enabled_workspace_ids"`

      - `ClaudeCodeManagedSettings object { current_value, current_version, previous_value, 3 more }`

        The organization's Claude Code managed settings were changed.

        The full previous and current settings content is provided in the
        `previous_value` and `current_value` fields.

        - `current_value: optional map[unknown]`

        - `current_version: optional number`

        - `previous_value: optional map[unknown]`

        - `previous_version: optional number`

        - `settings_uuid: optional string`

        - `type: optional "claude_code_managed_settings"`

          - `"claude_code_managed_settings"`

      - `AccountSessionDurationSeconds object { current_value, previous_value, type }`

        Tracks changes to the enterprise account session duration setting (in seconds).

        - `current_value: number`

        - `previous_value: number`

        - `type: optional "account_session_duration_seconds"`

          - `"account_session_duration_seconds"`

      - `VcsConnections object { current_value, previous_value, type }`

        Tracks changes to VCS (GitHub, etc.) organization connections.

        - `current_value: array of object { org_name, type, metadata, org_id }`

          - `org_name: string`

          - `type: "github"`

            Supported Version Control System providers.

            - `"github"`

          - `metadata: optional map[string]`

          - `org_id: optional string`

        - `previous_value: array of object { org_name, type, metadata, org_id }`

          - `org_name: string`

          - `type: "github"`

            Supported Version Control System providers.

            - `"github"`

          - `metadata: optional map[string]`

          - `org_id: optional string`

        - `type: optional "vcs_connections"`

          - `"vcs_connections"`

      - `DisabledAdminRequestTypes object { current_value, previous_value, type }`

        Tracks changes to which admin request types are disabled.

        - `current_value: array of string`

        - `previous_value: array of string`

        - `type: optional "disabled_admin_request_types"`

          - `"disabled_admin_request_types"`

      - `CodeExecutionNetworkEgressEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "code_execution_network_egress_enabled"`

          - `"code_execution_network_egress_enabled"`

      - `CodeExecutionDomainAllowlistChanged object { current_value, previous_value, type }`

        - `current_value: array of string`

        - `previous_value: array of string`

        - `type: optional "code_execution_domain_allowlist_changed"`

          - `"code_execution_domain_allowlist_changed"`

      - `CodeExecutionDomainAllowlistTemplateChanged object { current_value, previous_value, type }`

        - `current_value: "custom" or "full_egress" or "package_managers"`

          - `"custom"`

          - `"full_egress"`

          - `"package_managers"`

        - `previous_value: "custom" or "full_egress" or "package_managers"`

          - `"custom"`

          - `"full_egress"`

          - `"package_managers"`

        - `type: optional "code_execution_domain_allowlist_template_changed"`

          - `"code_execution_domain_allowlist_template_changed"`

      - `ChatEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "chat_enabled"`

          - `"chat_enabled"`

      - `ClaudeCodeQuickWebSetupEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "claude_code_quick_web_setup_enabled"`

          - `"claude_code_quick_web_setup_enabled"`

      - `ClaudeCodeTeamMemoryMode object { current_value, previous_value, type }`

        - `current_value: "all_org_members" or "github_repo" or "off" or "specific_groups"`

          - `"all_org_members"`

          - `"github_repo"`

          - `"off"`

          - `"specific_groups"`

        - `previous_value: "all_org_members" or "github_repo" or "off" or "specific_groups"`

          - `"all_org_members"`

          - `"github_repo"`

          - `"off"`

          - `"specific_groups"`

        - `type: optional "claude_code_team_memory_mode"`

          - `"claude_code_team_memory_mode"`

      - `BrowserExtensionSettingsUpdated object { current_value, previous_value, type }`

        - `current_value: map[unknown]`

        - `previous_value: map[unknown]`

        - `type: optional "browser_extension_settings"`

          - `"browser_extension_settings"`

      - `DesktopExtensionAllowlistEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "is_desktop_extension_allowlist_enabled"`

          - `"is_desktop_extension_allowlist_enabled"`

      - `ClaudeDesignEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "claude_ai_design_enabled"`

          - `"claude_ai_design_enabled"`

      - `ClaudeAISkillSharingEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "claude_ai_skill_sharing_enabled"`

          - `"claude_ai_skill_sharing_enabled"`

      - `ClaudeAISkillSharingOrgEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "claude_ai_skill_sharing_org_enabled"`

          - `"claude_ai_skill_sharing_org_enabled"`

      - `ClaudeCodeRemoteControlEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "claude_code_remote_control_enabled"`

          - `"claude_code_remote_control_enabled"`

      - `ClaudeCodeRoutinesEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "claude_code_routines_enabled"`

          - `"claude_code_routines_enabled"`

      - `FrontierServicesDataUseEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "frontier_services_data_use_enabled"`

          - `"frontier_services_data_use_enabled"`

      - `LtiCourseProjectsEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "lti_course_projects_enabled"`

          - `"lti_course_projects_enabled"`

      - `ManagedAgentsEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "managed_agents_enabled"`

          - `"managed_agents_enabled"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_organization_settings_updated"`

      - `"claude_organization_settings_updated"`

  - `OwnedProjectsAccessRestored object { actor, id, created_at, 4 more }`

    Access to owned projects was restored.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "owned_projects_access_restored"`

      - `"owned_projects_access_restored"`

    - `user_id: optional string`

  - `PaymentMethodUpdated object { actor, id, created_at, 3 more }`

    The organization's default payment method was updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "payment_method_updated"`

      - `"payment_method_updated"`

  - `PhoneCodeSent object { actor, id, created_at, 3 more }`

    User requested a phone verification code.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "phone_code_sent"`

      - `"phone_code_sent"`

  - `PhoneCodeVerified object { actor, id, created_at, 3 more }`

    User successfully verified their phone code.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "phone_code_verified"`

      - `"phone_code_verified"`

  - `PlatformAPIKeyCreated object { actor, api_key_id, id, 4 more }`

    An API key was created.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `api_key_id: string`

      Tagged ID of the created API key

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_api_key_created"`

      - `"platform_api_key_created"`

  - `PlatformAPIKeyUpdated object { actor, api_key_id, updates, 5 more }`

    An API key was updated.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `api_key_id: string`

      Tagged ID of the updated API key

    - `updates: array of object { current_value, previous_value, type }`

      - `current_value: string`

      - `previous_value: string`

      - `type: "name" or "status" or "workspace"`

        - `"name"`

        - `"status"`

        - `"workspace"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_api_key_updated"`

      - `"platform_api_key_updated"`

  - `PlatformCostReportViewed object { actor, id, created_at, 3 more }`

    The cost report was viewed.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_cost_report_viewed"`

      - `"platform_cost_report_viewed"`

  - `PlatformFederationIssuerArchived object { actor, federation_issuer_id, id, 4 more }`

    An OIDC federation issuer was archived.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `federation_issuer_id: string`

      Tagged ID of the archived issuer

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_federation_issuer_archived"`

      - `"platform_federation_issuer_archived"`

  - `PlatformFederationIssuerUpdated object { actor, federation_issuer_id, updates, 5 more }`

    An OIDC federation issuer was updated.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `federation_issuer_id: string`

      Tagged ID of the updated issuer

    - `updates: array of object { current_value, previous_value, type }`

      - `current_value: string`

      - `previous_value: string`

      - `type: "ca_cert_pem_sha256" or "check_jti" or "discovery_base" or 7 more`

        - `"ca_cert_pem_sha256"`

        - `"check_jti"`

        - `"discovery_base"`

        - `"issuer_url"`

        - `"jwks_keys_sha256"`

        - `"jwks_polling_disabled_at"`

        - `"jwks_source"`

        - `"jwks_url"`

        - `"max_jwt_lifetime_seconds"`

        - `"name"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_federation_issuer_updated"`

      - `"platform_federation_issuer_updated"`

  - `PlatformFederationRuleArchived object { actor, federation_rule_id, id, 4 more }`

    An OIDC federation rule was archived.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `federation_rule_id: string`

      Tagged ID of the archived rule

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_federation_rule_archived"`

      - `"platform_federation_rule_archived"`

  - `PlatformFederationRuleUpdated object { actor, federation_rule_id, updates, 5 more }`

    An OIDC federation rule was updated.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `federation_rule_id: string`

      Tagged ID of the updated rule

    - `updates: array of object { current_value, previous_value, type }`

      - `current_value: string`

      - `previous_value: string`

      - `type: "applies_to_all_workspaces" or "attributes" or "description" or 11 more`

        - `"applies_to_all_workspaces"`

        - `"attributes"`

        - `"description"`

        - `"match_audience"`

        - `"match_claims"`

        - `"match_condition"`

        - `"match_subject_prefix"`

        - `"name"`

        - `"oauth_scope"`

        - `"target_id"`

        - `"target_lookup_attr"`

        - `"target_type"`

        - `"token_lifetime_seconds"`

        - `"workspace_id"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_federation_rule_updated"`

      - `"platform_federation_rule_updated"`

  - `PlatformFederationRuleWorkspaceAdded object { actor, federation_rule_id, workspace_id, 5 more }`

    A federation rule was enabled for a workspace.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `federation_rule_id: string`

      Tagged ID of the federation rule

    - `workspace_id: string`

      Tagged ID of the workspace the rule was enabled for

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_federation_rule_workspace_added"`

      - `"platform_federation_rule_workspace_added"`

  - `PlatformFederationRuleWorkspaceRemoved object { actor, federation_rule_id, workspace_id, 5 more }`

    A federation rule was disabled for a workspace.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `federation_rule_id: string`

      Tagged ID of the federation rule

    - `workspace_id: string`

      Tagged ID of the workspace the rule was disabled for

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_federation_rule_workspace_removed"`

      - `"platform_federation_rule_workspace_removed"`

  - `PlatformFileContentDownloaded object { actor, file_id, id, 4 more }`

    Activity logged when file content is downloaded via GET /v1/files/{file_id}/content.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

    - `file_id: string`

      The tagged ID of the downloaded file

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_file_content_downloaded"`

      - `"platform_file_content_downloaded"`

  - `PlatformFileDeleted object { actor, file_id, id, 4 more }`

    Activity logged when a file is deleted via DELETE /v1/files/{file_id}.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

    - `file_id: string`

      The tagged ID of the deleted file

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_file_deleted"`

      - `"platform_file_deleted"`

  - `PlatformFileUploaded object { actor, file_id, id, 5 more }`

    Activity logged when a file is uploaded via POST /v1/files.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

    - `file_id: string`

      The tagged ID of the uploaded file

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `session_id: optional string`

      The tagged session ID (agent-api only)

    - `type: optional "platform_file_uploaded"`

      - `"platform_file_uploaded"`

  - `PlatformServiceAccountArchived object { actor, service_account_id, id, 4 more }`

    A service account was archived.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `service_account_id: string`

      Tagged ID of the archived service account

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_service_account_archived"`

      - `"platform_service_account_archived"`

  - `PlatformServiceAccountUpdated object { actor, service_account_id, updates, 5 more }`

    A service account was updated.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `service_account_id: string`

      Tagged ID of the updated service account

    - `updates: array of object { current_value, previous_value, type }`

      - `current_value: string`

      - `previous_value: string`

      - `type: "description"`

        - `"description"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_service_account_updated"`

      - `"platform_service_account_updated"`

  - `PlatformServiceAccountWorkspaceMemberAdded object { actor, service_account_id, workspace_id, 5 more }`

    A service account was added as a member of a workspace.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `service_account_id: string`

      Tagged ID of the service account

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_service_account_workspace_member_added"`

      - `"platform_service_account_workspace_member_added"`

  - `PlatformServiceAccountWorkspaceMemberRemoved object { actor, service_account_id, workspace_id, 5 more }`

    A service account was removed from a workspace.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `service_account_id: string`

      Tagged ID of the service account

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_service_account_workspace_member_removed"`

      - `"platform_service_account_workspace_member_removed"`

  - `PlatformServiceAccountWorkspaceMemberUpdated object { actor, service_account_id, updates, 6 more }`

    A service account's workspace membership role was updated.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `service_account_id: string`

      Tagged ID of the service account

    - `updates: array of object { current_value, previous_value, type }`

      - `current_value: string`

      - `previous_value: string`

      - `type: "workspace_role"`

        - `"workspace_role"`

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_service_account_workspace_member_updated"`

      - `"platform_service_account_workspace_member_updated"`

  - `PlatformSigningKeyCreated object { actor, algorithm, key_backing_type, 7 more }`

    Activity logged when a new request-signing key is registered for the org.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `algorithm: string`

      The signing algorithm (e.g. ecdsa-p256-sha256)

    - `key_backing_type: string`

      The backing type of the key (IN_MEMORY or CLOUD_KMS)

    - `signing_key_id: string`

      The tagged ID of the created signing key

    - `status: string`

      The initial status of the key (ACTIVE or PENDING)

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_signing_key_created"`

      - `"platform_signing_key_created"`

  - `PlatformSigningKeyDeleted object { actor, algorithm, key_backing_type, 7 more }`

    Activity logged when a signing key is permanently deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `algorithm: string`

      The algorithm of the deleted key

    - `key_backing_type: string`

      The backing type of the deleted key (IN_MEMORY or CLOUD_KMS)

    - `key_name: string`

      The name of the deleted key

    - `signing_key_id: string`

      The tagged ID of the deleted signing key

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_signing_key_deleted"`

      - `"platform_signing_key_deleted"`

  - `PlatformSigningKeyRotated object { actor, algorithm, key_group_identifier, 7 more }`

    Activity logged when an in-memory signing key is rotated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `algorithm: string`

      The algorithm of the new key

    - `key_group_identifier: string`

      The key group identifier linking old and new keys

    - `new_signing_key_id: string`

      The tagged ID of the newly created key

    - `old_signing_key_id: string`

      The tagged ID of the expired old key

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_signing_key_rotated"`

      - `"platform_signing_key_rotated"`

  - `PlatformSkillVersionCreated object { actor, skill_id, version, 5 more }`

    Activity logged when a skill version is created via POST /v1/skills/{skill_id}/versions.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

    - `skill_id: string`

      The tagged ID of the skill

    - `version: string`

      The version number of the created version

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_skill_version_created"`

      - `"platform_skill_version_created"`

  - `PlatformSkillVersionDeleted object { actor, skill_id, version, 5 more }`

    Activity logged when a skill version is deleted via DELETE /v1/skills/{skill_id}/versions/{version}.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

    - `skill_id: string`

      The tagged ID of the skill

    - `version: string`

      The version number of the deleted version

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_skill_version_deleted"`

      - `"platform_skill_version_deleted"`

  - `PlatformSpendLimitAlertEmailsUpdated object { actor, id, alert_emails, 5 more }`

    Spend limit alert email addresses and role targets were updated for an org.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `alert_emails: optional array of string`

      Updated list of alert email addresses.

    - `alerted_roles: optional array of string`

      Updated list of alerted roles.

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_spend_limit_alert_emails_updated"`

      - `"platform_spend_limit_alert_emails_updated"`

  - `PlatformSpendLimitCreated object { actor, id, created_at, 5 more }`

    An org-level fixed-dollar spend limit was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `limit_action: optional string`

      The action taken when the limit is reached (notify_only or notify_and_pause).

    - `limit_usd: optional number`

      The spend limit threshold in USD cents.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_spend_limit_created"`

      - `"platform_spend_limit_created"`

  - `PlatformSpendLimitDeleted object { actor, id, created_at, 4 more }`

    An org-level spend limit was removed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `spend_limit_id: optional string`

      UUID of the deleted spend limit.

    - `type: optional "platform_spend_limit_deleted"`

      - `"platform_spend_limit_deleted"`

  - `PlatformSpendLimitUpdated object { actor, id, created_at, 5 more }`

    An org-level spend limit snooze/ignore state was changed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `ignore: optional boolean`

      Whether the limit is being snoozed (ignored).

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `spend_limit_id: optional string`

      UUID of the spend limit.

    - `type: optional "platform_spend_limit_updated"`

      - `"platform_spend_limit_updated"`

  - `PlatformUsageReportClaudeCodeViewed object { actor, id, created_at, 3 more }`

    The Claude Code usage report was viewed.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_usage_report_claude_code_viewed"`

      - `"platform_usage_report_claude_code_viewed"`

  - `PlatformUsageReportMessagesViewed object { actor, id, created_at, 3 more }`

    The messages usage report was viewed.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_usage_report_messages_viewed"`

      - `"platform_usage_report_messages_viewed"`

  - `PlatformWorkspaceArchived object { actor, workspace_id, id, 4 more }`

    A workspace was archived.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `workspace_id: string`

      Tagged ID of the archived workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_workspace_archived"`

      - `"platform_workspace_archived"`

  - `PlatformWorkspaceCreated object { actor, workspace_id, id, 4 more }`

    A workspace was created.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `workspace_id: string`

      Tagged ID of the created workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_workspace_created"`

      - `"platform_workspace_created"`

  - `PlatformWorkspaceMemberAdded object { actor, user_id, workspace_id, 5 more }`

    A member was added to a workspace.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `user_id: string`

      Tagged ID of the added member

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_workspace_member_added"`

      - `"platform_workspace_member_added"`

  - `PlatformWorkspaceMemberRemoved object { actor, user_id, workspace_id, 5 more }`

    A member was removed from a workspace.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `user_id: string`

      Tagged ID of the removed member

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_workspace_member_removed"`

      - `"platform_workspace_member_removed"`

  - `PlatformWorkspaceMemberUpdated object { actor, updates, user_id, 6 more }`

    A workspace member was updated.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `updates: array of object { current_value, previous_value, type }`

      - `current_value: string`

      - `previous_value: string`

      - `type: "workspace_role"`

        - `"workspace_role"`

    - `user_id: string`

      Tagged ID of the updated member

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_workspace_member_updated"`

      - `"platform_workspace_member_updated"`

  - `PlatformWorkspaceMemberViewed object { actor, user_id, workspace_id, 5 more }`

    A workspace member was viewed.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `user_id: string`

      Tagged ID of the viewed member

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_workspace_member_viewed"`

      - `"platform_workspace_member_viewed"`

  - `PlatformWorkspaceMembersListed object { actor, workspace_id, id, 4 more }`

    Workspace members were listed.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_workspace_members_listed"`

      - `"platform_workspace_members_listed"`

  - `PlatformWorkspaceRateLimitDeleted object { actor, limiter_type, model_group, 6 more }`

    A workspace rate limit was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `limiter_type: string`

      Type of rate limiter

    - `model_group: string`

      Model group the rate limit applied to

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_workspace_rate_limit_deleted"`

      - `"platform_workspace_rate_limit_deleted"`

  - `PlatformWorkspaceRateLimitUpdated object { actor, limiter_type, model_group, 7 more }`

    A workspace rate limit was created or updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `limiter_type: string`

      Type of rate limiter

    - `model_group: string`

      Model group the rate limit applies to

    - `value: number`

      New rate limit value

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_workspace_rate_limit_updated"`

      - `"platform_workspace_rate_limit_updated"`

  - `PlatformWorkspaceUpdated object { actor, updates, workspace_id, 5 more }`

    A workspace was updated.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

    - `updates: array of object { current_value, previous_value, type }`

      - `current_value: string`

      - `previous_value: string`

      - `type: "allowed_inference_geos" or "default_inference_geo" or "display_color" or "name"`

        - `"allowed_inference_geos"`

        - `"default_inference_geo"`

        - `"display_color"`

        - `"name"`

    - `workspace_id: string`

      Tagged ID of the updated workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "platform_workspace_updated"`

      - `"platform_workspace_updated"`

  - `ClaudePluginCreated object { actor, id, created_at, 5 more }`

    Plugin was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `plugin_id: optional string`

    - `plugin_name: optional string`

    - `type: optional "claude_plugin_created"`

      - `"claude_plugin_created"`

  - `ClaudePluginDeleted object { actor, id, created_at, 5 more }`

    Plugin was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `plugin_id: optional string`

    - `plugin_name: optional string`

    - `type: optional "claude_plugin_deleted"`

      - `"claude_plugin_deleted"`

  - `PluginInstallationPreferenceUpdated object { actor, marketplace_id, plugin_name, 9 more }`

    An org admin changed the installation preference for a plugin.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `marketplace_id: string`

      Marketplace ID

    - `plugin_name: string`

      Plugin name

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `action: optional string`

      Action taken (e.g. 'deleted' for clearing an override)

    - `created_at: optional string`

      When this activity occurred.

    - `group_id: optional string`

      Tagged group ID for group-level overrides (null for org-level)

    - `group_name: optional string`

      Group name for group-level overrides

    - `installation_preference: optional string`

      New installation preference value (set only when action is an update; null for delete actions)

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "plugin_installation_preference_updated"`

      - `"plugin_installation_preference_updated"`

  - `ClaudePluginReplaced object { actor, id, created_at, 5 more }`

    Plugin was replaced.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `plugin_id: optional string`

    - `plugin_name: optional string`

    - `type: optional "claude_plugin_replaced"`

      - `"claude_plugin_replaced"`

  - `ClaudePluginUpdated object { actor, id, created_at, 5 more }`

    Plugin was updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `plugin_id: optional string`

    - `plugin_name: optional string`

    - `type: optional "claude_plugin_updated"`

      - `"claude_plugin_updated"`

  - `PrepaidAutoRechargeDisabled object { actor, id, created_at, 3 more }`

    Auto-recharge was disabled for API prepaid org.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "prepaid_auto_recharge_disabled"`

      - `"prepaid_auto_recharge_disabled"`

  - `PrepaidAutoRechargeUpdated object { actor, id, created_at, 5 more }`

    Auto-recharge settings were updated for API prepaid org.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `target_amount: optional number`

      Target recharge amount in minor units.

    - `threshold_amount: optional number`

      Threshold amount to trigger recharge in minor units.

    - `type: optional "prepaid_auto_recharge_updated"`

      - `"prepaid_auto_recharge_updated"`

  - `PrepaidExtraUsageAutoReloadDisabled object { actor, id, created_at, 3 more }`

    Prepaid usage credit auto-reload was disabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "prepaid_extra_usage_auto_reload_disabled"`

      - `"prepaid_extra_usage_auto_reload_disabled"`

  - `PrepaidExtraUsageAutoReloadEnabled object { actor, id, created_at, 3 more }`

    Prepaid usage credit auto-reload was enabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "prepaid_extra_usage_auto_reload_enabled"`

      - `"prepaid_extra_usage_auto_reload_enabled"`

  - `PrepaidExtraUsageAutoReloadSettingsUpdated object { actor, id, created_at, 3 more }`

    Prepaid usage credit auto-reload settings were updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "prepaid_extra_usage_auto_reload_settings_updated"`

      - `"prepaid_extra_usage_auto_reload_settings_updated"`

  - `PrimaryOwnerTransferred object { actor, new_owner_id, previous_owner_id, 5 more }`

    Primary owner role was transferred to another org member.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `new_owner_id: string`

    - `previous_owner_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "primary_owner_transferred"`

      - `"primary_owner_transferred"`

  - `ClaudeProjectArchived object { actor, claude_project_id, id, 4 more }`

    A Claude project was archived.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_archived"`

      - `"claude_project_archived"`

  - `ClaudeProjectCreated object { actor, claude_project_id, id, 4 more }`

    A Claude project was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_created"`

      - `"claude_project_created"`

  - `ClaudeProjectDeleted object { actor, claude_project_id, id, 4 more }`

    A Claude project was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_deleted"`

      - `"claude_project_deleted"`

  - `ClaudeProjectDocumentAccessFailed object { actor, claude_project_document_id, claude_project_id, 6 more }`

    An attempt to access a document in a Claude project failed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `claude_project_document_id: string`

    - `claude_project_id: string`

    - `filename: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_document_access_failed"`

      - `"claude_project_document_access_failed"`

  - `ClaudeProjectDocumentDeleted object { actor, claude_project_document_id, claude_project_id, 6 more }`

    A document was deleted from a Claude project.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_project_document_id: string`

    - `claude_project_id: string`

    - `filename: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_document_deleted"`

      - `"claude_project_document_deleted"`

  - `ClaudeProjectDocumentDeletionFailed object { actor, claude_project_document_id, claude_project_id, 6 more }`

    A request to delete a document from a Claude project failed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `claude_project_document_id: string`

    - `claude_project_id: string`

    - `filename: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_document_deletion_failed"`

      - `"claude_project_document_deletion_failed"`

  - `ClaudeProjectDocumentUploaded object { actor, claude_project_document_id, claude_project_id, 6 more }`

    A document was uploaded to a Claude project.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_project_document_id: string`

    - `claude_project_id: string`

    - `filename: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_document_uploaded"`

      - `"claude_project_document_uploaded"`

  - `ClaudeProjectDocumentViewed object { actor, claude_project_document_id, claude_project_id, 6 more }`

    A document in a Claude project was viewed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_project_document_id: string`

    - `claude_project_id: string`

    - `filename: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_document_viewed"`

      - `"claude_project_document_viewed"`

  - `ClaudeProjectFileAccessFailed object { actor, claude_file_id, claude_project_id, 5 more }`

    An attempt to access a file in a Claude project failed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `claude_file_id: string`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_file_access_failed"`

      - `"claude_project_file_access_failed"`

  - `ClaudeProjectFileDeleted object { actor, claude_file_id, claude_project_id, 5 more }`

    A file was deleted from a Claude project.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `claude_file_id: string`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_file_deleted"`

      - `"claude_project_file_deleted"`

  - `ClaudeProjectFileDeletionFailed object { actor, claude_file_id, claude_project_id, 5 more }`

    A request to delete a file from a Claude project failed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `claude_file_id: string`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_file_deletion_failed"`

      - `"claude_project_file_deletion_failed"`

  - `ClaudeProjectFileUploaded object { actor, claude_file_id, claude_project_id, 6 more }`

    A file was uploaded to a Claude project.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `claude_file_id: string`

    - `claude_project_id: string`

    - `filename: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_file_uploaded"`

      - `"claude_project_file_uploaded"`

  - `ClaudeProjectReported object { actor, claude_project_id, id, 4 more }`

    A Claude project was reported.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_reported"`

      - `"claude_project_reported"`

  - `ClaudeProjectSharingUpdated object { actor, audience, claude_project_id, 5 more }`

    A Claude project's sharing settings were updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `audience: array of object { type }  or object { type }`

      Sharing audience for the project. If empty, this it's only visible to the creating user.

      - `ProjectSharingAudiencePublic object { type }`

        - `type: optional "public"`

          - `"public"`

      - `ProjectSharingAudienceOrganization object { type }`

        - `type: optional "organization"`

          - `"organization"`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_project_sharing_updated"`

      - `"claude_project_sharing_updated"`

  - `ClaudeProjectViewed object { actor, claude_project_id, id, 5 more }`

    A Claude project was viewed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `preview_only: optional boolean`

    - `type: optional "claude_project_viewed"`

      - `"claude_project_viewed"`

  - `ClaudePubsecIdentityConfigured object { actor, idp_saml_config_updated, magic_link_toggled, 6 more }`

    SAML IdP configuration updated for a public sector organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `idp_saml_config_updated: boolean`

    - `magic_link_toggled: boolean`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `magic_link_enabled: optional boolean`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_pubsec_identity_configured"`

      - `"claude_pubsec_identity_configured"`

  - `RbacRoleAssigned object { actor, principal_id, principal_type, 6 more }`

    Admin assigned an RBAC custom role to a principal.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `principal_id: string`

      Tagged ID of the principal

    - `principal_type: string`

      Type of principal: account or group

    - `role_id: string`

      Tagged ID of the role

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "rbac_role_assigned"`

      - `"rbac_role_assigned"`

  - `RbacRoleCreated object { actor, role_id, role_name, 5 more }`

    Admin created an RBAC custom role.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `role_id: string`

      Tagged ID of the created role

    - `role_name: string`

      Name of the created role

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "rbac_role_created"`

      - `"rbac_role_created"`

  - `RbacRoleDeleted object { actor, role_id, id, 4 more }`

    Admin deleted an RBAC custom role.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `role_id: string`

      Tagged ID of the deleted role

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "rbac_role_deleted"`

      - `"rbac_role_deleted"`

  - `RbacRolePermissionAdded object { action, actor, resource_id, 7 more }`

    Admin added a permission to an RBAC custom role.

    - `action: string`

      Action permitted on the resource

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `resource_id: string`

      ID of the resource

    - `resource_type: string`

      Type of resource the permission applies to

    - `role_id: string`

      Tagged ID of the role

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "rbac_role_permission_added"`

      - `"rbac_role_permission_added"`

  - `RbacRolePermissionRemoved object { action, actor, resource_id, 7 more }`

    Admin removed a permission from an RBAC custom role.

    - `action: string`

      Action that was permitted on the resource

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `resource_id: string`

      ID of the resource

    - `resource_type: string`

      Type of resource the permission applied to

    - `role_id: string`

      Tagged ID of the role

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "rbac_role_permission_removed"`

      - `"rbac_role_permission_removed"`

  - `RbacRoleUnassigned object { actor, principal_id, principal_type, 6 more }`

    Admin unassigned an RBAC custom role from a principal.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `principal_id: string`

      Tagged ID of the principal

    - `principal_type: string`

      Type of principal: account or group

    - `role_id: string`

      Tagged ID of the role

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "rbac_role_unassigned"`

      - `"rbac_role_unassigned"`

  - `RbacRoleUpdated object { actor, role_id, id, 4 more }`

    Admin updated an RBAC custom role.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `role_id: string`

      Tagged ID of the updated role

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "rbac_role_updated"`

      - `"rbac_role_updated"`

  - `RoleAssignmentGranted object { actor, id, created_at, 8 more }`

    Role assignment was granted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `resource_id: optional string`

    - `resource_type: optional string`

    - `role: optional string`

    - `target_id: optional string`

    - `target_type: optional string`

    - `type: optional "role_assignment_granted"`

      - `"role_assignment_granted"`

  - `RoleAssignmentRevoked object { actor, id, created_at, 8 more }`

    Role assignment was revoked.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `resource_id: optional string`

    - `resource_type: optional string`

    - `role: optional string`

    - `target_id: optional string`

    - `target_type: optional string`

    - `type: optional "role_assignment_revoked"`

      - `"role_assignment_revoked"`

  - `SSOLoginFailed object { actor, id, created_at, 3 more }`

    An SSO sign-in attempt failed.

    - `actor: object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `ip_address: string`

      - `user_agent: string`

      - `type: optional "unauthenticated_user_actor"`

        - `"unauthenticated_user_actor"`

      - `unauthenticated_email_address: optional string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "sso_login_failed"`

      - `"sso_login_failed"`

  - `SSOLoginInitiated object { actor, id, created_at, 3 more }`

    A user started an SSO sign-in flow.

    - `actor: object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `ip_address: string`

      - `user_agent: string`

      - `type: optional "unauthenticated_user_actor"`

        - `"unauthenticated_user_actor"`

      - `unauthenticated_email_address: optional string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "sso_login_initiated"`

      - `"sso_login_initiated"`

  - `SSOLoginSucceeded object { actor, id, auth_method, 5 more }`

    A user successfully signed in with SSO.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `auth_method: optional "sso"`

      The method the user used to authenticate. May be absent on activities recorded before this field was introduced.

      - `"sso"`

    - `created_at: optional string`

      When this activity occurred.

    - `mfa_method: optional "not_used"`

      The second authentication factor performed during this login, if any. `null` when the second-factor status is not recorded on this event — for example, when authentication was delegated to an external identity provider and any second factor is not visible to Anthropic, or when this event is one step of a multi-step login whose MFA is reported on another activity. May be absent on activities recorded before this field was introduced.

      - `"not_used"`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "sso_login_succeeded"`

      - `"sso_login_succeeded"`

  - `SSOSecondFactorMagicLink object { actor, id, created_at, 3 more }`

    SSO second factor magic link was used.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "sso_second_factor_magic_link"`

      - `"sso_second_factor_magic_link"`

  - `ScimUserCreated object { actor, user_id, id, 4 more }`

    A SCIM user was provisioned.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { directory_id, workos_event_id, idp_connection_type, type }`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

    - `user_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "scim_user_created"`

      - `"scim_user_created"`

  - `ScimUserDeleted object { actor, user_id, id, 4 more }`

    A SCIM user was deleted.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { directory_id, workos_event_id, idp_connection_type, type }`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

    - `user_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "scim_user_deleted"`

      - `"scim_user_deleted"`

  - `ScimUserUpdated object { actor, user_id, id, 4 more }`

    A SCIM user was updated.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { directory_id, workos_event_id, idp_connection_type, type }`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

    - `user_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "scim_user_updated"`

      - `"scim_user_updated"`

  - `ScopedAPIKeyDeleted object { actor, api_key_id, api_key_name, 6 more }`

    A scoped API key was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `api_key_id: string`

      Tagged ID of the deleted scoped API key

    - `api_key_name: string`

      Name of the deleted scoped API key

    - `scopes: array of string`

      Scopes the deleted key had

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "scoped_api_key_deleted"`

      - `"scoped_api_key_deleted"`

  - `ScopedAPIKeyUpdated object { actor, api_key_id, updates, 5 more }`

    A scoped API key was renamed or its activation state changed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `api_key_id: string`

      Tagged ID of the updated scoped API key

    - `updates: array of object { current_value, previous_value, type }`

      - `current_value: string`

      - `previous_value: string`

      - `type: "activation_state" or "name"`

        - `"activation_state"`

        - `"name"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "scoped_api_key_updated"`

      - `"scoped_api_key_updated"`

  - `SeatTierChangesCancelled object { actor, id, created_at, 3 more }`

    Scheduled seat tier downgrades were cancelled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "seat_tier_changes_cancelled"`

      - `"seat_tier_changes_cancelled"`

  - `SeatTiersPurchased object { actor, id, created_at, 4 more }`

    Seat tiers were purchased or upgraded on a subscription.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `item_allocations: optional map[number]`

      Desired seat tier allocations (item type to quantity).

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "seat_tiers_purchased"`

      - `"seat_tiers_purchased"`

  - `ServiceCreated object { actor, service_name, id, 4 more }`

    Activity logged when an org service is explicitly created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `service_name: string`

      The org service name (e.g., 'external:my-service')

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "service_created"`

      - `"service_created"`

  - `ServiceDeleted object { actor, service_name, id, 4 more }`

    Activity logged when an org service is deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `service_name: string`

      The org service name (e.g., 'external:my-service')

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "service_deleted"`

      - `"service_deleted"`

  - `ServiceKeyCreated object { actor, is_service_created, key_name, 8 more }`

    Activity logged when a new org service key is created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `is_service_created: boolean`

      Whether the org service was implicitly created in this request

    - `key_name: string`

      The human-readable name of the key

    - `scopes: array of string`

      The scopes granted to this service key

    - `service_key_id: string`

      The ID of the created service key

    - `service_name: string`

      The service name this key belongs to

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "service_key_created"`

      - `"service_key_created"`

  - `ServiceKeyRevoked object { actor, service_key_id, service_name, 5 more }`

    Activity logged when an org service key is revoked.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `service_key_id: string`

      The tagged ID of the revoked service key

    - `service_name: string`

      The service name this key belongs to

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "service_key_revoked"`

      - `"service_key_revoked"`

  - `SessionRevoked object { actor, id, created_at, 3 more }`

    User revoked a specific session.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "session_revoked"`

      - `"session_revoked"`

  - `SessionShareAccessed object { actor, id, created_at, 4 more }`

    Session share was accessed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `share_id: optional string`

    - `type: optional "session_share_accessed"`

      - `"session_share_accessed"`

  - `SessionShareCreated object { actor, id, created_at, 4 more }`

    Session share was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `share_id: optional string`

    - `type: optional "session_share_created"`

      - `"session_share_created"`

  - `SessionShareRevoked object { actor, id, created_at, 4 more }`

    Session share was revoked.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `share_id: optional string`

    - `type: optional "session_share_revoked"`

      - `"session_share_revoked"`

  - `ClaudeSkillCreated object { actor, id, created_at, 5 more }`

    Skill was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `skill_id: optional string`

    - `skill_name: optional string`

    - `type: optional "claude_skill_created"`

      - `"claude_skill_created"`

  - `ClaudeSkillDeleted object { actor, id, created_at, 5 more }`

    Skill was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `skill_id: optional string`

    - `skill_name: optional string`

    - `type: optional "claude_skill_deleted"`

      - `"claude_skill_deleted"`

  - `ClaudeSkillDisabled object { actor, id, created_at, 5 more }`

    User disabled a skill for their account.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `skill_id: optional string`

    - `skill_name: optional string`

    - `type: optional "claude_skill_disabled"`

      - `"claude_skill_disabled"`

  - `ClaudeSkillEnabled object { actor, id, created_at, 5 more }`

    User enabled a skill for their account.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `skill_id: optional string`

    - `skill_name: optional string`

    - `type: optional "claude_skill_enabled"`

      - `"claude_skill_enabled"`

  - `ClaudeSkillReplaced object { actor, id, created_at, 5 more }`

    Skill was replaced.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `skill_id: optional string`

    - `skill_name: optional string`

    - `type: optional "claude_skill_replaced"`

      - `"claude_skill_replaced"`

  - `SocialLoginSucceeded object { actor, provider, id, 6 more }`

    A user successfully signed in with a social identity provider (Google, Apple, or Microsoft).

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `provider: "apple" or "google" or "microsoft"`

      - `"apple"`

      - `"google"`

      - `"microsoft"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `auth_method: optional "social"`

      The method the user used to authenticate. May be absent on activities recorded before this field was introduced.

      - `"social"`

    - `created_at: optional string`

      When this activity occurred.

    - `mfa_method: optional "not_used"`

      The second authentication factor performed during this login, if any. `null` when the second-factor status is not recorded on this event — for example, when authentication was delegated to an external identity provider and any second factor is not visible to Anthropic, or when this event is one step of a multi-step login whose MFA is reported on another activity. May be absent on activities recorded before this field was introduced.

      - `"not_used"`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "social_login_succeeded"`

      - `"social_login_succeeded"`

  - `SubscriptionCancellationScheduled object { actor, id, created_at, 3 more }`

    Subscription cancellation was scheduled at end of billing period.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "subscription_cancellation_scheduled"`

      - `"subscription_cancellation_scheduled"`

  - `SubscriptionQuantityUpdated object { actor, added_seats, new_quantity, 6 more }`

    Contracted subscription seat quantity was updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `added_seats: number`

    - `new_quantity: number`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `previous_quantity: optional number`

    - `type: optional "subscription_quantity_updated"`

      - `"subscription_quantity_updated"`

  - `SubscriptionRenewed object { actor, id, billing_interval, 5 more }`

    A cancelled subscription was renewed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `billing_interval: optional string`

      Billing interval (e.g. monthly, annual).

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `plan_type: optional string`

      Plan type being renewed into (e.g. team).

    - `type: optional "subscription_renewed"`

      - `"subscription_renewed"`

  - `SubscriptionResumed object { actor, id, created_at, 3 more }`

    A scheduled subscription cancellation was reversed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "subscription_resumed"`

      - `"subscription_resumed"`

  - `SubscriptionStarted object { actor, id, billing_interval, 6 more }`

    A new subscription was created (Team or Enterprise).

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `billing_interval: optional string`

      Billing interval (e.g. monthly, annual).

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `plan_type: optional string`

      Type of subscription started (e.g. team, enterprise).

    - `seat_count: optional number`

      Number of seats purchased.

    - `type: optional "subscription_started"`

      - `"subscription_started"`

  - `SubscriptionUpgraded object { actor, id, created_at, 5 more }`

    Subscription plan was upgraded (e.g. Team to Enterprise).

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `new_plan: optional string`

      New plan type after upgrade.

    - `old_plan: optional string`

      Previous plan type.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "subscription_upgraded"`

      - `"subscription_upgraded"`

  - `TunnelTokenMinted object { actor, token_id, id, 5 more }`

    An OAuth bearer token for the tunnel management API was minted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `token_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `token_name: optional string`

    - `type: optional "tunnel_token_minted"`

      - `"tunnel_token_minted"`

  - `TunnelTokenRevoked object { actor, token_id, id, 4 more }`

    An OAuth bearer token for the tunnel management API was revoked.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `token_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "tunnel_token_revoked"`

      - `"tunnel_token_revoked"`

  - `UserConsentRecorded object { actor, consent_type, entity_id, 6 more }`

    User granted a consent for a specific entity (e.g. consumer health consent for an MCP server).

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `consent_type: string`

    - `entity_id: string`

    - `entity_type: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "user_consent_recorded"`

      - `"user_consent_recorded"`

  - `UserConsentRevoked object { actor, id, consent_id, 7 more }`

    User revoked a previously granted consent for a specific entity.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `consent_id: optional string`

    - `consent_type: optional string`

    - `created_at: optional string`

      When this activity occurred.

    - `entity_id: optional string`

    - `entity_type: optional string`

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "user_consent_revoked"`

      - `"user_consent_revoked"`

  - `ClaudeUserRoleUpdated object { actor, current_role, previous_role, 7 more }`

    A user's role within the organization was changed, or the user was added to or removed from the organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { admin_api_key_id, ip_address, user_agent, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

    - `current_role: string`

      If null, then user was removed from the Organization

    - `previous_role: string`

      If null, then user was added to the Organization

    - `user_email: string`

      Email of the user whose role was changed

    - `user_id: string`

      ID of the user whose role was changed

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_user_role_updated"`

      - `"claude_user_role_updated"`

  - `ClaudeUserSettingsUpdated object { actor, updates, id, 4 more }`

    User updated their personal settings.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `updates: array of object { current_value, previous_value, type }  or object { current_value, previous_value, type }  or object { current_value, previous_value, type }  or 19 more`

      - `FullName object { current_value, previous_value, type }`

        - `current_value: string`

        - `previous_value: string`

        - `type: optional "full_name"`

          - `"full_name"`

      - `DisplayName object { current_value, previous_value, type }`

        - `current_value: string`

        - `previous_value: string`

        - `type: optional "display_name"`

          - `"display_name"`

      - `ArtifactsEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "artifacts_enabled"`

          - `"artifacts_enabled"`

      - `LatexEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "latex_enabled"`

          - `"latex_enabled"`

      - `AnalysisToolEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "analysis_tool_enabled"`

          - `"analysis_tool_enabled"`

      - `ChatSuggestionsEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "chat_suggestions_enabled"`

          - `"chat_suggestions_enabled"`

      - `MultimodalPdfsEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "multimodal_pdfs_enabled"`

          - `"multimodal_pdfs_enabled"`

      - `GDriveEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "gdrive_enabled"`

          - `"gdrive_enabled"`

      - `GDriveIndexingEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "gdrive_indexing_enabled"`

          - `"gdrive_indexing_enabled"`

      - `WebSearchEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "web_search_enabled"`

          - `"web_search_enabled"`

      - `GeolocationEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "geolocation_enabled"`

          - `"geolocation_enabled"`

      - `UserMemoryEnabledSetting object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "enabled_saffron"`

          - `"enabled_saffron"`

      - `McpToolsEnabled object { current_value, previous_value, type }`

        - `current_value: map[boolean]`

        - `previous_value: map[boolean]`

        - `type: optional "mcp_tools_enabled"`

          - `"mcp_tools_enabled"`

      - `CliOpPermissionsEnabled object { current_value, previous_value, type }`

        - `current_value: map[string]`

        - `previous_value: map[string]`

        - `type: optional "cli_op_permissions_enabled"`

          - `"cli_op_permissions_enabled"`

      - `GoogleDriveSearchEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "google_drive_search_enabled"`

          - `"google_drive_search_enabled"`

      - `GmailIntegrationEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "gmail_integration_enabled"`

          - `"gmail_integration_enabled"`

      - `GoogleCalendarIntegrationEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "google_calendar_integration_enabled"`

          - `"google_calendar_integration_enabled"`

      - `ThinkingModeEnabled object { current_value, previous_value, type }`

        - `current_value: "adaptive" or "extended" or "off"`

          - `"adaptive"`

          - `"extended"`

          - `"off"`

        - `previous_value: "adaptive" or "extended" or "off"`

          - `"adaptive"`

          - `"extended"`

          - `"off"`

        - `type: optional "thinking_mode_enabled"`

          - `"thinking_mode_enabled"`

      - `ResearchModeEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "research_mode_enabled"`

          - `"research_mode_enabled"`

      - `ComputerUseEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "computer_use_enabled"`

          - `"computer_use_enabled"`

      - `ClaudeAPIInArtifactsEnabled object { current_value, previous_value, type }`

        - `current_value: boolean`

        - `previous_value: boolean`

        - `type: optional "claude_api_in_artifacts_enabled"`

          - `"claude_api_in_artifacts_enabled"`

      - `ConversationPreferences object { type }`

        The 'conversation_preferences' for the user were updated. Values omitted.

        - `type: optional "conversation_preferences"`

          - `"conversation_preferences"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "claude_user_settings_updated"`

      - `"claude_user_settings_updated"`

  - `WorkspaceMemberSpendLimitCreated object { actor, id, account_id, 7 more }`

    A per-member or workspace-default Claude Code spend limit was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `account_id: optional string`

      Tagged ID of the user (null for workspace-wide default).

    - `created_at: optional string`

      When this activity occurred.

    - `limit_action: optional string`

      The action taken when the limit is reached.

    - `limit_usd: optional number`

      The spend limit threshold in USD cents.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "workspace_member_spend_limit_created"`

      - `"workspace_member_spend_limit_created"`

    - `workspace_id: optional string`

      Tagged ID of the workspace.

  - `WorkspaceMemberSpendLimitDeleted object { actor, id, account_id, 6 more }`

    A per-member or workspace-default Claude Code spend limit was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `account_id: optional string`

      Tagged ID of the user (null for workspace-wide default).

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `spend_limit_id: optional string`

      UUID of the deleted spend limit.

    - `type: optional "workspace_member_spend_limit_deleted"`

      - `"workspace_member_spend_limit_deleted"`

    - `workspace_id: optional string`

      Tagged ID of the workspace.

  - `WorkspaceMemberSpendLimitUpdated object { actor, id, account_id, 7 more }`

    A per-member Claude Code spend limit amount was updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `account_id: optional string`

      Tagged ID of the user (null for workspace-wide default).

    - `created_at: optional string`

      When this activity occurred.

    - `new_limit_usd: optional number`

      The new spend limit threshold in USD cents.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `spend_limit_id: optional string`

      UUID of the spend limit.

    - `type: optional "workspace_member_spend_limit_updated"`

      - `"workspace_member_spend_limit_updated"`

    - `workspace_id: optional string`

      Tagged ID of the workspace.

  - `WorkspaceSpendLimitCreated object { actor, id, created_at, 6 more }`

    A workspace-level API spend limit was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `limit_action: optional string`

      The action taken when the limit is reached (notify_only or notify_and_pause).

    - `limit_usd: optional number`

      The spend limit threshold in USD cents.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `type: optional "workspace_spend_limit_created"`

      - `"workspace_spend_limit_created"`

    - `workspace_id: optional string`

      Tagged ID of the workspace.

  - `WorkspaceSpendLimitDeleted object { actor, id, created_at, 5 more }`

    A workspace-level API spend limit was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string`

      Organization ID this activity is associated with

    - `organization_uuid: optional string`

      Deprecated. Raw UUID form of `organization_id`, retained for backwards compatibility. Prefer `organization_id`.

    - `spend_limit_id: optional string`

      UUID of the deleted spend limit.

    - `type: optional "workspace_spend_limit_deleted"`

      - `"workspace_spend_limit_deleted"`

    - `workspace_id: optional string`

      Tagged ID of the workspace.
