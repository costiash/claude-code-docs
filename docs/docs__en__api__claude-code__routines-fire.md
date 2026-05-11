# Trigger a routine via API

Start a Claude Code routine session on demand by sending an authenticated POST request.

---

<Warning>
This is an experimental API. Request and response shapes, rate limits, and token semantics may change. Breaking changes ship behind new dated beta header versions, and the two previous header versions continue to work so that callers have time to migrate.
</Warning>

[Claude Code](https://code.claude.com/docs) is Anthropic's agentic coding tool. [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web) runs Claude Code sessions on Anthropic-managed cloud infrastructure at claude.ai/code, and a [routine](https://code.claude.com/docs/en/routines) is a saved configuration there: a prompt, one or more repositories, and connectors, packaged so it can run unattended on a schedule, in response to GitHub events, or when called over HTTP.

This endpoint is the HTTP entry point. POSTing to it starts a new run of an existing routine and returns the resulting session ID and URL. Typical callers are alerting systems, CI pipelines, and internal tools that need to start a Claude Code session programmatically.

Calling this endpoint requires a claude.ai account on a Pro, Max, Team, or Enterprise plan with [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web) enabled. Authenticate with a per-routine bearer token created in the Claude Code web UI rather than an Anthropic API key.

## Differences from the Claude Platform

The routine fire endpoint belongs to the Claude Code product surface, which differs from the Claude Platform APIs and SDKs in a few ways:

| Aspect | This endpoint | Other Anthropic APIs |
| :--- | :--- | :--- |
| Authentication | `Authorization: Bearer` with a per-routine token (`sk-ant-oat01-...`) created at [claude.ai/code/routines](https://claude.ai/code/routines) | `x-api-key` with an Anthropic API key from Claude Console |
| Token scope | One routine only; no read access | Workspace-level |
| SDK support | None | Available in all [client SDKs](/docs/en/api/client-sdks) |
| Billing | Claude Code subscription usage on claude.ai | Claude Platform usage |
| Path namespace | `/v1/claude_code/...` | `/v1/...` |
| Stability | Experimental; requires `anthropic-beta: experimental-cc-routine-2026-04-01` | Stable or standard beta |

## Before you begin

To call this endpoint, you need:

1. A routine created at [claude.ai/code/routines](https://claude.ai/code/routines)
2. A bearer token generated for that routine: open the routine for editing, click **Add another trigger** under **Select a trigger**, choose **API**, then click **Generate token** in the modal. The token is shown once and cannot be retrieved later.

See [Add an API trigger](https://code.claude.com/docs/en/routines#add-an-api-trigger) in the Claude Code documentation for the full setup walkthrough.

## Trigger a routine

```http
POST https://api.anthropic.com/v1/claude_code/routines/{routine_id}/fire
```

Every request must include the `anthropic-beta: experimental-cc-routine-2026-04-01` header. Requests without it return `400 invalid_request_error`.

The Claude Code web UI provides the full URL alongside the token when you add an API trigger, so most integrations store both as secrets and call the endpoint directly. The examples below show a shell call and a GitHub Actions step that triggers the routine on CI failure.

```bash cURL
curl -X POST https://api.anthropic.com/v1/claude_code/routines/$ROUTINE_ID/fire \
  -H "Authorization: Bearer $ROUTINE_TOKEN" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: experimental-cc-routine-2026-04-01" \
  -H "Content-Type: application/json" \
  -d '{"text": "Sentry alert SEN-4521 fired in prod. Stack trace attached."}'
```

```yaml GitHub Actions
- if: failure()
  env:
    ROUTINE_FIRE_URL: ${{ secrets.ROUTINE_FIRE_URL }}
    ROUTINE_FIRE_TOKEN: ${{ secrets.ROUTINE_FIRE_TOKEN }}
  run: |
    curl -X POST "$ROUTINE_FIRE_URL" \
      -H "Authorization: Bearer $ROUTINE_FIRE_TOKEN" \
      -H "anthropic-version: 2023-06-01" \
      -H "anthropic-beta: experimental-cc-routine-2026-04-01" \
      -H "Content-Type: application/json" \
      -d "{\"text\": \"CI failed: $GITHUB_WORKFLOW run $GITHUB_RUN_ID on $GITHUB_REF\"}"
```

The request returns once the session is created. It does not stream session output or wait for the session to complete.

### Headers

| Name | Required | Description |
| :--- | :--- | :--- |
| `Authorization` | Yes | `Bearer <token>`. The per-routine token created in the Claude Code web UI, prefixed `sk-ant-oat01-`. |
| `anthropic-beta` | Yes | Must include `experimental-cc-routine-2026-04-01`. |
| `anthropic-version` | Yes | The [API version](/docs/en/api/versioning), for example `2023-06-01`. |
| `Content-Type` | When body is present | `application/json`. |

### Path parameters

| Name | Type | Description |
| :--- | :--- | :--- |
| `routine_id` | string | The routine's identifier. Despite the parameter name, the value is prefixed `trig_` rather than `routine_`. Included in the URL the modal shows when you add an API trigger. |

### Request body

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `text` | string | No | Initial context for this run, such as an alert body, a failing log line, or a git diff. The value is freeform text and is not parsed; if you send JSON or another structured payload, the routine receives it as a literal string. Passed to the routine alongside its saved prompt. Maximum 65,536 characters. |

The body is optional. Unknown fields in the body are ignored.

### Response

A successful request returns `200 OK` with the new session details:

```json
{
  "type": "routine_fire",
  "claude_code_session_id": "session_01HJKLMNOPQRSTUVWXYZ",
  "claude_code_session_url": "https://claude.ai/code/session_01HJKLMNOPQRSTUVWXYZ"
}
```

| Field | Type | Description |
| :--- | :--- | :--- |
| `type` | string | Always `routine_fire`. |
| `claude_code_session_id` | string | The ID of the Claude Code session created for this run. |
| `claude_code_session_url` | string | A link to the session on claude.ai. Open it in a browser to watch the run, review changes, or continue the conversation. |

### Errors

Errors use the standard Anthropic [error envelope](/docs/en/api/errors):

```json
{
  "type": "error",
  "error": {
    "type": "not_found_error",
    "message": "<string>"
  }
}
```

| HTTP status | Error type | Cause |
| :--- | :--- | :--- |
| 400 | `invalid_request_error` | Missing or invalid `anthropic-beta` header, `text` exceeds 65,536 characters, or the routine is [paused](https://code.claude.com/docs/en/routines#edit-and-control-routines). |
| 401 | `authentication_error` | No bearer token in the `Authorization` header, or the token does not match this routine. |
| 403 | `permission_error` | The account or organization does not have access to this endpoint. |
| 404 | `not_found_error` | The routine does not exist. |
| 429 | `rate_limit_error` | The account's routine run limit or usage limit has been reached. The response includes a `Retry-After` header indicating when the window resets. |
| 500 | `api_error` | An unexpected server error. |
| 503 | `overloaded_error` | The service is temporarily overloaded. Retry after a short delay. The Claude Platform returns 529 for this error type; this endpoint returns 503. |

## Authentication

The bearer token is scoped to a single routine. A compromised token can only trigger that routine; it grants no read access, no access to other routines, and no access to account data.

Generate and revoke tokens from the routine's API trigger settings at [claude.ai/code/routines](https://claude.ai/code/routines). There is no public API for token management. Generating a new token revokes the previous one.

## Idempotency

Each successful request creates a new session. There is no idempotency key. If a webhook caller retries, the endpoint creates multiple sessions.

## Rate limits

Routine runs count against a per-account daily allowance that varies by plan, and the resulting sessions draw down the same Claude Code subscription usage as interactive sessions. When either limit is reached, the endpoint returns `429 rate_limit_error` with a `Retry-After` header. Organizations with extra usage enabled continue past the included allowance on metered overage.

Your remaining daily runs are shown at [claude.ai/code/routines](https://claude.ai/code/routines). For how routine usage interacts with subscription limits and extra usage billing, see [Usage and limits](https://code.claude.com/docs/en/routines#usage-and-limits) in the Claude Code documentation.

## SDK support

This endpoint is not in the Anthropic SDKs. Its token model differs from API key authentication, and typical callers such as CI jobs and alerting webhooks send the request directly.

## See also

- [Automate work with routines](https://code.claude.com/docs/en/routines) in the Claude Code documentation
- [Beta headers](/docs/en/api/beta-headers)
- [Errors](/docs/en/api/errors)