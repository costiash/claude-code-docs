# Compliance API

Programmatic access to your organization's Claude activity, chats, files, projects, and users for compliance, audit, and governance.

---

<Note>
  The Compliance API is available only on the Claude Enterprise plan and must be enabled before use. See [Get access to the Compliance API](/docs/en/manage-claude/compliance-api-access).
</Note>

The Compliance API gives Claude Enterprise customers programmatic access to their organization's Activity Feed, the directory of users, roles, and groups across every linked organization, and, for claude.ai organizations, the underlying chats, files, and projects. Security, legal, and compliance teams use it to audit activity, retrieve or delete content, and feed events into downstream tooling.

<Note>
  Two key types unlock the Compliance API. A **Compliance Access Key** (created in claude.ai) reaches every endpoint, and an **Admin API key** (created in Claude Console) reaches the Activity Feed only. The following key-type table shows where each is created and what it unlocks.
</Note>

The following call returns the most recent activity event in your organization. Any key with the `read:compliance_activities` scope can make it. To create a key and grant it that scope, see [Get access to the Compliance API](/docs/en/manage-claude/compliance-api-access).

<CodeGroup>
```bash cURL nocheck
curl --fail-with-body -sS \
  "https://api.anthropic.com/v1/compliance/activities?limit=1" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY"
```
</CodeGroup>

A successful response returns a JSON object containing `data` (an array of `Activity` records), `has_more`, `first_id`, and `last_id`:

```json Response
{
  "data": [
    {
      "id": "activity_01XyDMpzjS89pFZXqSFUBDr6",
      "created_at": "2026-04-10T08:09:10Z",
      "organization_id": "org_01Wv6QeBcDfGhJkLmNpQrSt8",
      "organization_uuid": "abcdef01-2345-6789-abcd-ef0123456789",
      "actor": {
        "type": "user_actor",
        "email_address": "user@example.com",
        "user_id": "user_01TuVwXyZaBcDeFgH2JkLmN4",
        "ip_address": "192.0.2.34",
        "user_agent": "Mozilla/5.0..."
      },
      "type": "claude_chat_created",
      "claude_chat_id": "claude_chat_01XyDMpzjS89pFZXqSFUBDr6",
      "claude_project_id": "claude_proj_01KGp4eZNug9ri4kE35RSppq"
    }
  ],
  "has_more": true,
  "first_id": "activity_01XyDMpzjS89pFZXqSFUBDr6",
  "last_id": "activity_01XyDMpzjS89pFZXqSFUBDr6"
}
```

Two key types can carry the `read:compliance_activities` scope; they differ in where you create them and which endpoints they unlock. For the full provisioning flow, scopes, and key prefixes, see [Get access to the Compliance API](/docs/en/manage-claude/compliance-api-access).

| Key type | Created in | Compliance API access |
| :---- | :---- | :---- |
| **Compliance Access Key** | claude.ai | Full Compliance API |
| **Admin API key** | Claude Console | Activity Feed only |

---

## How the Compliance API works

Every endpoint lives under `/v1/compliance/*` on `https://api.anthropic.com` and authenticates through the `x-api-key` header. The Activity Feed (`GET /v1/compliance/activities`) is the shared endpoint available to any key that carries the `read:compliance_activities` scope; see [Query the Activity Feed](/docs/en/manage-claude/compliance-activity-feed) for filters, pagination, and the full `Activity` object. The remaining endpoints require a Compliance Access Key carrying the relevant scope. The directory endpoints (organizations, users, roles, and groups) return data from every linked organization under the parent, including Claude Console-linked organizations; the content endpoints (chats, files, projects, and project attachments) serve claude.ai data only. To provision a key, see [Get access to the Compliance API](/docs/en/manage-claude/compliance-api-access).

---

## Compliance API versus related features

Two adjacent features overlap with the Compliance API; here is how to choose.

### Export audit logs

The audit log export is a separate feature in **claude.ai** > **Organization settings** > **Data and privacy** that lets owners and primary owners download a CSV of organization events. It's significantly narrower than the Compliance API: a capped lookback window, CSV download only, and no access to chat, file, or project content. Standardize on the Compliance API for ongoing programmatic use.

### Analytics API

Anthropic provides two analytics APIs: the Claude Enterprise Analytics API and the [Claude Code Analytics API](/docs/en/manage-claude/claude-code-analytics-api). Both return aggregated usage and cost figures for IT, FinOps, and platform teams, while the Compliance API returns per-event records for security, legal, and compliance teams. The two API families answer different questions, use different keys, and are provisioned separately.

---

## In this section

<CardGroup>
  <Card href="/docs/en/manage-claude/compliance-api-access" title="Get access to the Compliance API">
    Create a Compliance Access Key or Admin API key, choose scopes, and enable the Compliance API for your organization.
  </Card>
  <Card href="/docs/en/manage-claude/compliance-activity-feed" title="Query the Activity Feed">
    Retrieve, filter, and paginate the shared Activity Feed. Supported by both key types.
  </Card>
  <Card href="/docs/en/manage-claude/compliance-content-data" title="Retrieve and delete chats, files, and projects">
    Read chat content and attachments, then delete on demand. Compliance Access Key required.
  </Card>
  <Card href="/docs/en/manage-claude/compliance-org-data" title="List organizations, users, roles, and groups">
    Enumerate linked organizations, members, roles, and directory groups.
  </Card>
  <Card href="/docs/en/manage-claude/compliance-integration-patterns" title="Design your compliance integration">
    Choose a feed-consumption pattern, plan SIEM correlation, and decide your retention approach.
  </Card>
  <Card href="/docs/en/manage-claude/compliance-errors" title="Handle Compliance API errors">
    Every 400, 401, 403, 404, 409, 429, and 5xx response the Compliance API returns, with the fix for each.
  </Card>
  <Card href="/docs/en/api/compliance" title="API reference">
    Endpoint paths, parameters, and response schemas for every Compliance API call.
  </Card>
  <Card href="/docs/en/manage-claude/compliance-faq" title="Compliance API FAQ">
    Answers to common key, scope, availability, and integration questions.
  </Card>
</CardGroup>