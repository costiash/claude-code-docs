# Get access to the Compliance API

Create a Compliance Access Key or Admin API key, choose the right scopes, and enable the Compliance API for your organization.

---

<Note>
  The Compliance API is available only on the Claude Enterprise plan and must be enabled before use. This page describes how.
</Note>

<Check>
  **Required role:** organization admin (Claude Console) or primary owner (claude.ai).
</Check>

The Compliance API uses two key types, and which one you create depends on which Claude product your organization uses. Primary owners create Compliance Access Keys in claude.ai; these keys unlock the full Compliance API. Organization admins create Admin API keys in Claude Console; these keys unlock the [Activity Feed](/docs/en/manage-claude/compliance-activity-feed) only.

## Which key do you need?

| Key type                                       | Created in                              | Used for                                                                                                       | Works with the Compliance API? |
| ---------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **Compliance Access Key** (`sk-ant-api01-...`) | **claude.ai** > **Organization settings** > **Data and privacy**  | Activity Feed, chats, files, projects, users, and organization metadata                                        | Yes (all endpoints)            |
| **Admin API key** (`sk-ant-admin01-...`)           | **Claude Console** > **Settings** > **Admin keys**  | The [Admin API](/docs/en/manage-claude/admin-api) and the Compliance API Activity Feed  | Activity Feed only             |
| **Analytics API key**                          | **claude.ai** > **Analytics** > **API keys**        | The [Claude Enterprise Analytics API](https://support.claude.com/en/articles/13694757-claude-enterprise-analytics-api-access-engagement-and-adoption-data)                                                                            | No                             |
| **Claude API key** (`sk-ant-api03-...`)        | **Claude Console** > **Settings** > **API keys**    | Calling Claude models through the [Claude API](/docs/en/api/overview)                                          | No                             |

A Claude Enterprise tenant has one **parent organization** that centralizes identity, SSO, and SCIM for every workload organization beneath it. These workload organizations are the parent's **linked organizations**.

<Warning>
  **Claude Enterprise parent organizations do not appear in Claude Console (`platform.claude.com`).** The parent carries no workloads and no API keys. Create Compliance Access Keys in claude.ai **Organization settings**, not in Claude Console.
</Warning>

## Enable the Compliance API for your organization

The enablement path depends on which Claude product your organization uses. Whichever path you use, enablement happens at the parent organization level and cascades to every linked organization, both claude.ai and Claude Console.

### Enable for claude.ai organizations

For claude.ai organizations on the Claude Enterprise plan, the primary owner enables the Compliance API in **Organization settings** > **Data and privacy** at [claude.ai/admin-settings/data-privacy-controls](https://claude.ai/admin-settings/data-privacy-controls): click **Enable** under **Compliance API**. After enablement, a **Compliance access keys** section appears on the same page.

### Enable for Claude Console organizations

Contact your Anthropic representative to request access. Admin API keys created after the Compliance API is enabled carry the `read:compliance_activities` scope. Admin API keys created before enablement continue to work with the Admin API, but calling the Activity Feed with one returns [403 Forbidden](/docs/en/manage-claude/compliance-errors#403-forbidden).

## Create a Compliance Access Key

<Note>
  The Compliance API must already be [enabled for your claude.ai parent organization](#enable-the-compliance-api-for-your-organization) before a Compliance Access Key can be created.
</Note>

<Warning>
  A Compliance Access Key with `read:compliance_user_data` can read every chat,
  file, and project in every linked organization, including content the primary
  owner has not seen. A key with `delete:compliance_user_data` can permanently
  delete that content. Treat Compliance Access Keys like production database
  credentials: store them in a secrets manager, never in source control or SIEM
  forwarder configuration.
</Warning>

<Steps>
  <Step title="Sign in as the primary owner">
    Only the primary owner of the parent organization can create Compliance Access Keys. If the **Compliance access keys** section described in the next step is not visible, either you are not the primary owner, or the Compliance API has not been enabled for your organization yet (see [Enable the Compliance API for your organization](#enable-the-compliance-api-for-your-organization)).
  </Step>

  <Step title="Open Data and privacy settings">
    Go to [claude.ai > Organization settings > Data and privacy](https://claude.ai/admin-settings/data-privacy-controls) and find the **Compliance access keys** section.
  </Step>

  <Step title="Create the key">
    Click **Create key**, name the key, and select one or more scopes from the following table. Click **Create**.

    | Scope                          | Grants                                                                          |
    | ------------------------------ | ------------------------------------------------------------------------------- |
    | `read:compliance_activities`   | Read the Activity Feed for the parent organization and all linked organizations |
    | `read:compliance_user_data`    | Read user chats, messages, files, projects, organization users, and group members |
    | `delete:compliance_user_data`  | Delete user chats, files, and projects                                          |
    | `read:compliance_org_data`     | Read organization metadata (names, types, roles, and groups). User listings and group membership require `read:compliance_user_data`. |

    Choose the smallest scope set that your integration needs:

    - An audit pipeline that reads the Activity Feed only needs `read:compliance_activities`.
    - An eDiscovery tool that reads chats and files but never deletes them does not need `delete:compliance_user_data`.
    - If your workflow both reads and deletes, use **two keys** with separate scopes so a leaked read key cannot delete data.

    Compliance Access Key scopes are immutable after creation. To change scopes, create a new key with the scopes you want, then delete the old one.
  </Step>

  <Step title="Copy and store the secret">
    Copy the displayed secret key (starting with `sk-ant-api01-`) and store it in your secrets manager. The full secret is displayed only once.
  </Step>

  <Step title="Export the key for the examples in this guide">
    Set the key as an environment variable so the shell samples in this guide can read it:

    ```bash
    export ANTHROPIC_COMPLIANCE_ACCESS_KEY=sk-ant-api01-...
    ```
  </Step>
</Steps>

## Create an Admin API key

<Note>
  The Compliance API must already be [enabled for your Claude Console organization](#enable-the-compliance-api-for-your-organization) before an Admin API key can call the Activity Feed.
</Note>

<Steps>
  <Step title="Sign in as an organization admin">
    Only an organization member with the **admin** role can create Admin API keys. See [Organization roles and permissions](/docs/en/manage-claude/admin-api#organization-roles-and-permissions) for the full role list.
  </Step>

  <Step title="Open Admin keys settings">
    Go to [Claude Console > Settings > Admin keys](https://platform.claude.com/settings/admin-keys).
  </Step>

  <Step title="Create the key">
    Click **Create key**, name the key, and click **Create**.
  </Step>

  <Step title="Copy and store the secret">
    Copy the displayed secret key (starting with `sk-ant-admin01-`) and store it in your secrets manager. The full secret is displayed only once.
  </Step>

  <Step title="Export the key for use with the Activity Feed">
    Set the key as an environment variable:

    ```bash
    export ANTHROPIC_ADMIN_KEY=sk-ant-admin01-...
    ```

    The distinct variable name keeps the Admin API key from overwriting a Compliance Access Key if you provision both. The cURL examples in this guide read the key from `$ANTHROPIC_COMPLIANCE_ACCESS_KEY`; substitute `$ANTHROPIC_ADMIN_KEY` when calling the [Activity Feed](/docs/en/manage-claude/compliance-activity-feed) with an Admin API key.
  </Step>
</Steps>

Admin API keys carry the `read:compliance_activities` scope only when the Compliance API was enabled for the organization before the key was created; see [Enable for Claude Console organizations](#enable-for-claude-console-organizations). They cannot be granted any other Compliance API scope, so calls to any endpoint other than the Activity Feed return [403 Forbidden](/docs/en/manage-claude/compliance-errors#403-forbidden).

For the same key's role in managing your Claude Console organization, see [Admin API](/docs/en/manage-claude/admin-api).

## Check your key's scopes

To inspect the scopes on a key you already have, use one of the following signals.

- **Key prefix.** `sk-ant-admin01-` is an Admin API key (carries `read:compliance_activities` only, subject to the enablement timing in the preceding section). `sk-ant-api01-` is a Compliance Access Key; its scopes are the subset you selected at creation.
- **Settings UI.** Open the **Compliance access keys** section in claude.ai **Organization settings** > **Data and privacy**, or the **Admin keys** section in Claude Console, and read the **Scopes** column for the key.
- **Error responses.** A call that exceeds the key's scopes returns a 403 with a message in the format `Missing required scopes. Got: [<scopes the key carries>] Needed: [<scopes the endpoint requires>]`. See [Handle Compliance API errors](/docs/en/manage-claude/compliance-errors#403-forbidden) for the full error catalog.

```json
{
  "error": {
    "type": "permission_error",
    "message": "Missing required scopes. Got: ['read:compliance_activities'] Needed: ['read:compliance_user_data']"
  }
}
```

## Manage and rotate keys

Delete a Compliance Access Key from the same **Compliance access keys** panel where you created it: go to [claude.ai > Organization settings > Data and privacy](https://claude.ai/admin-settings/data-privacy-controls). Delete an Admin API key from [Claude Console > Settings > Admin keys](https://platform.claude.com/settings/admin-keys).

Deleting a key takes effect on the next request: there is no grace period. Compliance Access Keys do not expire on their own.

To rotate a key without an outage:

1. Create a new key with the same scopes.
2. Update your integration to use the new key.
3. Verify the integration succeeds with the new key.
4. Delete the old key.

Pagination cursors stored before a rotation remain valid: cursors are scoped to the organization, not the key.

If a Compliance Access Key leaks, delete it immediately, audit the [Activity Feed](/docs/en/manage-claude/compliance-activity-feed) for `compliance_api_accessed` activities by the compromised key, and rotate any downstream credentials that the leaked key could reach. Filter on `actor.type` `api_actor` and `actor.api_key_id` to find requests made by the compromised key.

## Next steps

<CardGroup cols={2}>
  <Card title="Query the Activity Feed" href="/docs/en/manage-claude/compliance-activity-feed">
    Read organization-wide activity events with any key that has `read:compliance_activities`.
  </Card>
  <Card title="Retrieve and delete chats, files, and projects" href="/docs/en/manage-claude/compliance-content-data">
    Use a Compliance Access Key with `read:compliance_user_data` to retrieve claude.ai content, and `delete:compliance_user_data` to delete it.
  </Card>
</CardGroup>