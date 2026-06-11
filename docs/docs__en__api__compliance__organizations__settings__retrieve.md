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
    is the only key. An empty object means no retention limit is in force.

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
