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

- `api_keys: array of object { id, created_at, created_by_id, 5 more }`

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

  - `expires_at: optional string`

    When the key will stop authenticating, or null when the key does not expire.

  - `type: optional "compliance_api_key"`

    - `"compliance_api_key"`

- `organization_id: string`

- `settings: array of object { name, value, type }  or object { name, value, type }  or object { name, value, type }  or 3 more`

  - `Boolean object { name, value, type }`

    A setting whose enforced value is a single true/false flag.

    - `name: "ai_powered_artifacts_enabled" or "api_workbench_feedback_collection_enabled" or "artifact_connectors_enabled" or 43 more`

      - `"ai_powered_artifacts_enabled"`

      - `"api_workbench_feedback_collection_enabled"`

      - `"artifact_connectors_enabled"`

      - `"ask_your_org_enabled"`

      - `"chat_enabled"`

      - `"claude_ai_chat_sharing_enabled"`

      - `"claude_ai_feedback_collection_enabled"`

      - `"claude_ai_integration_sharing_enabled"`

      - `"claude_code_desktop_auto_permissions_enabled"`

      - `"claude_code_desktop_bypass_permissions_enabled"`

      - `"claude_code_desktop_enabled"`

      - `"claude_code_fast_mode_enabled"`

      - `"claude_code_metrics_logging_enabled"`

      - `"claude_code_remote_control_enabled"`

      - `"claude_code_review_enabled"`

      - `"claude_code_routines_enabled"`

      - `"claude_code_security_enabled"`

      - `"claude_code_trusted_devices_required"`

      - `"claude_code_web_enabled"`

      - `"claude_code_workflows_enabled"`

      - `"claude_design_enabled"`

      - `"claude_in_slack_enabled"`

      - `"code_execution_enabled"`

      - `"code_execution_network_egress_enabled"`

      - `"connector_tools_default_always_allow"`

      - `"content_redaction_enabled"`

      - `"desktop_extension_allowlist_enabled"`

      - `"directory_sync_enabled"`

      - `"frontier_data_use_enabled"`

      - `"hipaa_compliance_enabled"`

      - `"inline_visualizations_enabled"`

      - `"ip_allowlist_enabled"`

      - `"location_metadata_enabled"`

      - `"member_usage_dashboard_visible"`

      - `"memory_enabled"`

      - `"org_wide_skill_sharing_enabled"`

      - `"public_projects_enabled"`

      - `"skill_sharing_enabled"`

      - `"skills_enabled"`

      - `"sso_claude_ai_enforced"`

      - `"sso_console_enforced"`

      - `"sso_enabled"`

      - `"third_party_interactive_content_enabled"`

      - `"user_skill_creation_enabled"`

      - `"web_search_enabled"`

      - `"work_across_apps_enabled"`

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

  - `String object { name, value, type }`

    A setting whose enforced value is a single string; null means no value
    is configured.

    - `name: "claude_code_default_worker_environment_id" or "claude_code_default_worker_pool_id"`

      - `"claude_code_default_worker_environment_id"`

      - `"claude_code_default_worker_pool_id"`

    - `value: string`

    - `type: optional "string"`

      - `"string"`

  - `StringList object { name, value, type }`

    A setting whose enforced value is a list of strings.

    - `name: "allowed_invite_domains" or "disabled_admin_request_types" or "ip_allowlist_ip_ranges"`

      - `"allowed_invite_domains"`

      - `"disabled_admin_request_types"`

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
      "expires_at": "2019-12-27T18:11:19.117Z",
      "type": "compliance_api_key"
    }
  ],
  "organization_id": "organization_id",
  "settings": [
    {
      "name": "ai_powered_artifacts_enabled",
      "value": true,
      "type": "boolean"
    }
  ],
  "type": "effective_organization_settings"
}
```
