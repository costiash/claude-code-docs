# API Overview

---

The Claude API is a RESTful API at `https://api.anthropic.com` that provides programmatic access to Claude models and Claude Managed Agents.

<Note>
**New to Claude?** For direct model access, start with [Get started](/docs/en/get-started) and [Working with Messages](/docs/en/build-with-claude/working-with-messages). For managed agent infrastructure, see the [Claude Managed Agents quickstart](/docs/en/managed-agents/quickstart).
</Note>

## Prerequisites

To use the Claude API, you'll need:

- A [Claude Console account](https://platform.claude.com)
- An [API key](/settings/keys)

For step-by-step setup instructions, see [Get started](/docs/en/get-started).

## Available APIs

The Claude API includes the following APIs:

**General Availability:**
- **[Messages API](/docs/en/api/messages/create)**: Send messages to Claude for conversational interactions (`POST /v1/messages`)
- **[Message Batches API](/docs/en/api/creating-message-batches)**: Process large volumes of Messages requests asynchronously with 50% cost reduction (`POST /v1/messages/batches`)
- **[Token Counting API](/docs/en/api/messages-count-tokens)**: Count tokens in a message before sending to manage costs and rate limits (`POST /v1/messages/count_tokens`)
- **[Models API](/docs/en/api/models-list)**: List available Claude models and their details (`GET /v1/models`)

**Beta:**
- **[Files API](/docs/en/api/files-create)**: Upload and manage files for use across multiple API calls (`POST /v1/files`, `GET /v1/files`)
- **[Skills API](/docs/en/api/skills/create-skill)**: Create and manage custom agent skills (`POST /v1/skills`, `GET /v1/skills`)
- **[Agents API](/docs/en/api/beta/agents/create)**: Define reusable, versioned agent configurations for Claude Managed Agents (`POST /v1/agents`, `GET /v1/agents`)
- **[Sessions API](/docs/en/api/beta/sessions/create)**: Run stateful agent sessions in managed cloud containers (`POST /v1/sessions`, `GET /v1/sessions/{id}/stream`)
- **[Environments API](/docs/en/api/beta/environments/create)**: Configure container templates for agent sessions (`POST /v1/environments`, `GET /v1/environments`)

For the complete API reference with all endpoints, parameters, and response schemas, explore the API reference pages listed in the navigation. To access beta features, see [Beta headers](/docs/en/api/beta-headers).

## Authentication

All requests to the Claude API must include these headers:

| Header | Value | Required |
|--------|-------|----------|
| `x-api-key` | Your API key from Console | Yes |
| `anthropic-version` | API version (e.g., `2023-06-01`) | Yes |
| `content-type` | `application/json` | Yes |

If you are using the [Client SDKs](#client-sdks), the SDK will send these headers automatically. For API versioning details, see [API versions](/docs/en/api/versioning).

### Getting API Keys

The API is made available via the web [Console](https://platform.claude.com/). You can use the [Workbench](https://platform.claude.com/workbench) to try out the API in the browser and then generate API keys in [Account Settings](https://platform.claude.com/settings/keys). Use [workspaces](https://platform.claude.com/settings/workspaces) to segment your API keys and [control spend](/docs/en/api/rate-limits) by use case.

## Client SDKs

Anthropic provides official SDKs that simplify API integration by handling authentication, request formatting, error handling, and more.

**Benefits**:
- Automatic header management (x-api-key, anthropic-version, content-type)
- Type-safe request and response handling
- Built-in retry logic and error handling
- Streaming support
- Request timeouts and connection management

For a list of client SDKs and their respective installation instructions, see [Client SDKs](/docs/en/api/client-sdks).

## Availability on partner platforms

Claude is available through the direct Claude API and through partner platforms. Choose based on your infrastructure, compliance requirements, and pricing preferences.

### Claude API

- **Direct access** to the latest models and features first
- **Anthropic billing and support**
- **Best for**: New integrations, full feature access, direct relationship with Anthropic

### Third-Party Platform APIs

Access Claude through AWS, Google Cloud, or Microsoft Azure:
- **Integrated** with cloud provider billing and IAM
- **May have feature delays** or differences from the direct API
- **Best for**: Existing cloud commitments, specific compliance requirements, consolidated cloud billing

| Platform | Provider | Documentation |
|----------|----------|---------------|
| Amazon Bedrock | AWS | [Claude on Amazon Bedrock](/docs/en/build-with-claude/claude-on-amazon-bedrock) |
| Vertex AI | Google Cloud | [Claude on Vertex AI](/docs/en/build-with-claude/claude-on-vertex-ai) |
| Azure AI | Microsoft Azure | [Claude on Azure AI](/docs/en/build-with-claude/claude-in-microsoft-foundry) |

<Note>
Claude Managed Agents is available only through the direct Claude API. For feature availability across platforms, see the [Features overview](/docs/en/build-with-claude/overview).
</Note>

## Request and Response Format

### Request size limits

| Endpoint | Maximum request size |
| --- | --- |
| Messages, Token Counting | 32 MB |
| [Batch API](/docs/en/build-with-claude/batch-processing) | 256 MB |
| [Files API](/docs/en/build-with-claude/files) | 500 MB |
| Sessions, Agents, Environments | 32 MB |

If you exceed these limits, you'll receive a 413 `request_too_large` error.

<Note>
Third-party platforms have their own request size limits: Vertex AI limits requests to 30 MB, and Amazon Bedrock limits requests to 20 MB. Consult your platform's documentation for current values.
</Note>

### Response Headers

The Claude API includes the following headers in every response:

- `request-id`: A globally unique identifier for the request
- `anthropic-organization-id`: The organization ID associated with the API key used in the request

## Rate Limits and Availability

### Rate Limits

The API enforces rate limits and spend limits to prevent misuse and manage capacity. Limits are organized into usage tiers that increase automatically as you use the API. Each tier has:

- **Spend limits**: Maximum monthly cost for API usage
- **Rate limits**: Maximum number of requests per minute (RPM) and tokens per minute (TPM)

You can view your organization's current limits in the [Console](/settings/limits). For higher limits or Priority Tier (enhanced service levels with committed spend), contact sales through the Console.

For detailed information about limits, tiers, and the token bucket algorithm used for rate limiting, see [Rate limits](/docs/en/api/rate-limits).

### Availability

The Claude API is available in [many countries and regions](/docs/en/api/supported-regions) worldwide. Check the supported regions page to confirm availability in your location.

## Next Steps

<CardGroup cols={2}>
  <Card title="Messages API reference" icon="book" href="/docs/en/api/messages/create">
    Complete API specification for direct model interactions
  </Card>
  <Card title="Claude Managed Agents reference" icon="brain" href="/docs/en/api/beta/sessions">
    Agents, Sessions, and Environments endpoints
  </Card>
  <Card title="Client SDKs" icon="code" href="/docs/en/api/client-sdks">
    Python, TypeScript, Java, Go, C#, Ruby, and PHP
  </Card>
  <Card title="Rate limits" icon="gauge" href="/docs/en/api/rate-limits">
    Usage tiers, spend limits, and token bucket algorithm
  </Card>
</CardGroup>