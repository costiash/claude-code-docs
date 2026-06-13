# Analytics APIs

Understand which analytics API and API key your organization needs, then provision access to Claude Code productivity metrics or Claude Enterprise engagement and adoption data.

---

Anthropic provides two analytics APIs, and which one you use depends on which Claude product your organization manages:

- The **Claude Code Analytics API** reports daily Claude Code productivity metrics for organizations that use the Claude Platform. It is part of the [Admin API](/docs/en/manage-claude/admin-api) and uses an Admin API key.
- The **Claude Enterprise Analytics API** reports organization-wide engagement, adoption, and cost data across Claude products (chat, projects, Claude Code, and more) for Claude Enterprise organizations. It uses an Analytics API key created in claude.ai.

The two APIs use different key types, created in different places by different roles. This page describes which API fits your organization and how to create the right key.

## Which API do you need?

| API                                  | Key type                                | Created in                                                                              | Who can create it   | What it covers                                                                                                  |
| ------------------------------------ | --------------------------------------- | ---------------------------------------------------------------------------------------- | ------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Claude Code Analytics API**        | Admin API key (`sk-ant-admin01-...`)    | [Claude Console > Settings > Admin keys](https://platform.claude.com/settings/admin-keys) | Organization admin  | Daily Claude Code metrics per user: sessions, lines of code, commits, pull requests, tool acceptance, and estimated cost by model |
| **Claude Enterprise Analytics API**  | Analytics API key                       | [claude.ai > Analytics > API keys](https://claude.ai/analytics/api-keys)                   | Primary owner       | Organization-wide engagement and adoption (user activity, active-user summaries, project, skill, and connector usage), plus cost and usage reports |

The key types are not interchangeable: an Admin API key cannot call the Claude Enterprise Analytics API, and an Analytics API key cannot call the Admin API. If your organization uses both the Claude Platform and Claude Enterprise, you can provision both keys and use each API for its own data.

<Note>
  Looking for API usage and cost data rather than product analytics? See the [Usage and Cost API](/docs/en/manage-claude/usage-cost-api), which explains the right path for both Claude Console and Claude Enterprise organizations.
</Note>

## Get access to the Claude Code Analytics API

The Claude Code Analytics API is available to every organization with access to the [Admin API](/docs/en/manage-claude/admin-api), and is free to use.

<Steps>
  <Step title="Sign in as an organization admin">
    Only organization members with the **admin** role can create Admin API keys. See [Organization roles and permissions](/docs/en/manage-claude/admin-api#organization-roles-and-permissions) for the full role list.
  </Step>

  <Step title="Create an Admin API key">
    Go to [Claude Console > Settings > Admin keys](https://platform.claude.com/settings/admin-keys), click **Create key**, name the key, and click **Create**. Copy the displayed secret key (starting with `sk-ant-admin01-`) and store it in your secrets manager. The full secret is displayed only once.
  </Step>

  <Step title="Call the API">
    Pass the key in the `x-api-key` header:

    ```bash
    curl "https://api.anthropic.com/v1/organizations/usage_report/claude_code?starting_at=2025-09-08" \
      --header "anthropic-version: 2023-06-01" \
      --header "x-api-key: $ADMIN_API_KEY"
    ```
  </Step>
</Steps>

For the available metrics, request parameters, and response schema, see the [Claude Code Analytics API guide](/docs/en/manage-claude/claude-code-analytics-api) and the [API reference](/docs/en/api/admin-api/claude-code/get-claude-code-usage-report).

## Get access to the Claude Enterprise Analytics API

The Claude Enterprise Analytics API is available to Claude Enterprise organizations. Engagement and adoption data is available on all Enterprise plans. The cost and usage endpoints apply to usage-based Enterprise plans; for seat-based Enterprise plans, they reflect usage credits only.

<Steps>
  <Step title="Sign in as the primary owner">
    Only the primary owner of the organization can enable API access and create Analytics API keys.
  </Step>

  <Step title="Enable API access and create a key">
    Go to [claude.ai > Analytics > API keys](https://claude.ai/analytics/api-keys) and enable public API access, then create an Analytics API key. Keys carry the `read:analytics` scope. Copy the displayed secret and store it in your secrets manager.
  </Step>

  <Step title="Call the API">
    Pass the key in the `x-api-key` header. Endpoints live under `https://api.anthropic.com/v1/organizations/analytics/`. For request examples, parameters, and response schemas, see the [Claude Enterprise Analytics API reference guide](https://support.claude.com/en/articles/13703965-claude-enterprise-analytics-api-reference-guide).
  </Step>
</Steps>

The Claude Enterprise Analytics API provides:

- **User activity:** per-user daily metrics across chat (conversations, messages, projects, files, artifacts), Claude Code (sessions, commits, pull requests, lines of code, tool actions), and other Claude products
- **Activity summaries:** organization-level daily, weekly, and monthly active users, seat counts, and pending invites
- **Project, skill, and connector usage:** adoption breakdowns for chat projects, skills, and connectors
- **Cost and usage reports:** per-user and organization-level token usage and cost over time (usage-based Enterprise plans)

For an overview of the engagement and adoption data, see [Claude Enterprise Analytics API: access, engagement, and adoption data](https://support.claude.com/en/articles/13694757-claude-enterprise-analytics-api-access-engagement-and-adoption-data). For endpoint details, parameters, and response schemas, see the [Claude Enterprise Analytics API reference guide](https://support.claude.com/en/articles/13703965-claude-enterprise-analytics-api-reference-guide).

## Next steps

<CardGroup cols={2}>
  <Card title="Claude Code Analytics API" href="/docs/en/manage-claude/claude-code-analytics-api">
    Track Claude Code sessions, code changes, and tool usage with an Admin API key.
  </Card>
  <Card title="Usage and Cost API" href="/docs/en/manage-claude/usage-cost-api">
    Track API token usage and costs for your organization.
  </Card>
  <Card title="Claude Enterprise Analytics API reference" href="https://support.claude.com/en/articles/13703965-claude-enterprise-analytics-api-reference-guide">
    Endpoint reference for engagement, adoption, and cost data.
  </Card>
  <Card title="Get access to the Compliance API" href="/docs/en/manage-claude/compliance-api-access">
    Audit and compliance data uses its own key types.
  </Card>
</CardGroup>