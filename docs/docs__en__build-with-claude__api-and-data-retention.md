# API and data retention

Learn about how Anthropic's APIs and associated features retain data, including information about zero data retention (ZDR) and HIPAA-ready API access.

---

<Note>
Information about Anthropic's standard retention policies is set out in [Anthropic's commercial data retention policy](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data) and [consumer data retention policy](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data).

Anthropic offers two data handling arrangements for the Claude API:
- **Zero data retention (ZDR):** Customer data is not stored at rest after the API response is returned, except where needed to comply with law or combat misuse.
- **HIPAA readiness:** For organizations handling protected health information (PHI), Anthropic offers HIPAA-ready API access with a signed Business Associate Agreement (BAA). See [HIPAA readiness](#hipaa-readiness).
</Note>

## Anthropic's approach to data retention

Different APIs and features have different storage and retention needs. Where an API or feature doesn't require storage of customer prompts or responses, it may be eligible for ZDR. Where an API or feature necessarily requires storage of customer prompts or responses, Anthropic designs for the smallest possible retention footprint. For these features:

- Retained data is never used for model training without your express permission.
- Only what is technically necessary for the API and feature to work is retained. Conversation content (your prompts and Claude's outputs) is never retained unless explicitly noted.
- Data is purged on the shortest practical TTL, and Anthropic aims to give customers control over how long data is retained. What is held, and the retention duration where a specific TTL applies, is documented on each feature's page.

In the [feature eligibility table](#feature-eligibility), some features are marked "Yes (qualified)" in the ZDR eligible column. If your organization has a ZDR arrangement, you can use these features with confidence that what Anthropic retains is narrow and is required for optimal performance.

## Zero data retention (ZDR) scope

**What ZDR covers**

- **Certain Claude APIs:** ZDR applies to the Claude Messages and Token Counting APIs
- **Claude Code:** ZDR applies when used with Commercial organization API keys or through Claude Enterprise (see [Claude Code ZDR docs](https://code.claude.com/docs/en/zero-data-retention))

**What ZDR does NOT cover**

- **Console and Workbench:** Any usage on Console or Workbench
- **Claude consumer products:** Claude Free, Pro, or Max plans, including when customers on those plans use Claude's web, desktop, or mobile apps or Claude Code
- **Claude Teams and Claude Enterprise:** Claude Teams and Claude Enterprise product interfaces are **not ZDR-eligible**, except for Claude Code when used through Claude Enterprise with ZDR enabled for the organization. For other product interfaces, only Commercial organization API keys are eligible for ZDR.
- **Third-party integrations:** Data processed by third-party websites, tools, or other integrations is **not ZDR-eligible**, though some may have similar offerings. When using external services in conjunction with the Claude API, make sure to review those services' data handling practices.

<Note>
For the most up-to-date information on what products and features are ZDR-eligible, refer to your contract terms or contact your Anthropic account representative.
</Note>

## HIPAA readiness

The Claude API supports HIPAA-ready integrations for organizations that handle protected health information (PHI). With a signed BAA and a HIPAA-enabled organization, you can use supported API features to process PHI while supporting your organization's HIPAA compliance.

Previously, organizations that required HIPAA readiness for the Claude API needed to enable ZDR. HIPAA-ready API access removes this requirement and provides a foundation for Anthropic to progressively enable additional features as they are audited for HIPAA readiness.

<Note>
This page covers HIPAA readiness for the Claude API. For the full HIPAA Implementation Guide covering Claude Enterprise, Claude Code, and configuration requirements, see the [Anthropic Trust Center](https://trust.anthropic.com/resources).
</Note>

### Getting started

To set up HIPAA-ready API access:

<Steps>
<Step title="Sign a Business Associate Agreement">
Contact the [Anthropic sales team](https://claude.com/contact-sales) to sign a BAA that covers API usage.
</Step>
<Step title="Provision a HIPAA-enabled organization">
Anthropic provisions a dedicated organization with HIPAA readiness controls enabled. This organization automatically enforces feature restrictions, blocking API requests that use non-eligible features.
</Step>
<Step title="Build with eligible features">
Use the [feature eligibility table](#feature-eligibility) to confirm which features are supported. Review the [PHI handling guidelines](#phi-handling-guidelines) for features that require specific restrictions on where PHI can appear. For detailed configuration and compliance requirements, refer to the [HIPAA Implementation Guide](https://trust.anthropic.com/resources).
</Step>
</Steps>

<Warning>
HIPAA readiness is enforced at the organization level. If you need both HIPAA-ready and general-purpose API access, use separate organizations for each.
</Warning>

### HIPAA readiness scope

**What HIPAA readiness covers**

- **Claude API:** HIPAA readiness applies to the Claude API (`api.anthropic.com`) for eligible features listed in the [feature eligibility table](#feature-eligibility).

**What HIPAA readiness does NOT cover**

- **Claude consumer products:** Claude Free, Pro, or Max plans
- **Console and Workbench:** Usage through the Claude Console interface
- **Third-party platforms:** Claude on AWS Bedrock or Google Cloud Vertex AI (refer to those platforms' compliance documentation)
- **Third-party integrations:** Data processed by external tools or services connected to your application
- **Claude Code:** Claude Code is not covered under HIPAA readiness
- **Beta features:** Features in beta are generally not covered under the BAA unless explicitly listed as eligible in the [feature eligibility table](#feature-eligibility)

### PHI handling guidelines

Protected health information (PHI) includes any individually identifiable health information. In the context of the Claude API, PHI typically appears in:

- Message content (prompts and responses from Claude)
- Attached files (images, PDFs)
- File names and metadata associated with message content

The following fields are not expected to contain PHI under the BAA: workspace names, user information (name, email, phone number), billing data, and support tickets.

#### Schema and tool definition restrictions

When using [structured outputs](/docs/en/build-with-claude/structured-outputs) or tools with `strict: true`, the API compiles JSON schemas into grammars that are cached separately from message content. These cached schemas do not receive the same PHI protections as prompts and responses.

**Do not include PHI in JSON schema definitions.** This restriction applies to:

- Schema property names
- `enum` values
- `const` values
- `pattern` regular expressions

Patient-specific information should only appear in message content, where it is protected under HIPAA safeguards.

### HIPAA error handling

Your signed BAA is the official source of truth for which features are covered. The API also enforces these restrictions automatically: when a HIPAA-enabled organization sends a request that includes a non-eligible feature, the API returns a `400` error to prevent accidental use of features not covered by your BAA:

```json
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "The requested features are not available for HIPAA-regulated organizations without Zero Data Retention: code_execution."
  }
}
```

The error message lists the non-eligible features detected in the request. Remove these features from your request and retry.

## Feature eligibility

The following table lists which Claude API features are eligible for ZDR and HIPAA readiness arrangements. For HIPAA-enabled organizations, features marked "No" in the HIPAA column are automatically blocked, and requests that include them return a `400` error.

| Feature | Endpoint | ZDR eligible | HIPAA eligible | Details |
| ------- | -------- | ------------ | -------------- | ------- |
| [Messages API](/docs/en/build-with-claude/working-with-messages) | `/v1/messages` | <Eligible>Yes</Eligible> | <Eligible>Yes</Eligible> | Standard API calls for generating Claude responses. |
| [Token counting](/docs/en/build-with-claude/token-counting) | `/v1/messages/count_tokens` | <Eligible>Yes</Eligible> | <Eligible>Yes</Eligible> | Count tokens before sending requests. |
| [Web search](/docs/en/agents-and-tools/tool-use/web-search-tool) | `/v1/messages` (with `web_search` tool) | <Eligible>Yes</Eligible><sup>1</sup> | <Eligible>Yes</Eligible><sup>1</sup> | Real-time web search results returned in the API response. |
| [Web fetch](/docs/en/agents-and-tools/tool-use/web-fetch-tool) | `/v1/messages` (with `web_fetch` tool) | <Eligible>Yes</Eligible><sup>1</sup> <sup>2</sup> | <Eligible status="no">No</Eligible> | Fetched web content returned in the API response. |
| [Advisor tool](/docs/en/agents-and-tools/tool-use/advisor-tool) | `/v1/messages` (with `advisor` tool) | <Eligible>Yes</Eligible> | <Eligible status="no">No</Eligible> | Advisor model output is returned in the API response; nothing is stored server-side after the response. |
| [Memory tool](/docs/en/agents-and-tools/tool-use/memory-tool) | `/v1/messages` (with `memory` tool) | <Eligible>Yes</Eligible> | <Eligible>Yes</Eligible> | Client-side memory storage where you control data retention. |
| [Context management (compaction)](/docs/en/build-with-claude/compaction) | `/v1/messages` (with `context_management`) | <Eligible>Yes</Eligible> | <Eligible status="no">No</Eligible> | Server-side compaction results are returned/round-tripped statelessly through the API response. |
| [Context editing](/docs/en/build-with-claude/context-editing) | `/v1/messages` (with `context_management`) | <Eligible>Yes</Eligible> | <Eligible status="no">No</Eligible> | Context edits (tool use clearing + thinking clearing) are applied in real time. |
| [Fast mode](/docs/en/build-with-claude/fast-mode) | `/v1/messages` (with `speed: "fast"`) | <Eligible>Yes</Eligible> | <Eligible>Yes</Eligible> | Same Messages API endpoint with faster inference. ZDR applies regardless of speed setting. |
| [1M token context window](/docs/en/build-with-claude/context-windows) | `/v1/messages` | <Eligible>Yes</Eligible> | <Eligible>Yes</Eligible> | Extended context processing uses the standard Messages API. |
| [Adaptive thinking](/docs/en/build-with-claude/adaptive-thinking) | `/v1/messages` | <Eligible>Yes</Eligible> | <Eligible>Yes</Eligible> | Dynamic thinking depth uses the standard Messages API. |
| [Citations](/docs/en/build-with-claude/citations) | `/v1/messages` | <Eligible>Yes</Eligible> | <Eligible>Yes</Eligible> | Source attribution uses the standard Messages API. |
| [Data residency](/docs/en/build-with-claude/data-residency) | `/v1/messages` (with `inference_geo`) | <Eligible>Yes</Eligible> | <Eligible>Yes</Eligible> | Geographic routing uses the standard Messages API. |
| [Effort](/docs/en/build-with-claude/effort) | `/v1/messages` (with `effort`) | <Eligible>Yes</Eligible> | <Eligible>Yes</Eligible> | Token efficiency control uses the standard Messages API. |
| [Extended thinking](/docs/en/build-with-claude/extended-thinking) | `/v1/messages` (with `thinking`) | <Eligible>Yes</Eligible> | <Eligible>Yes</Eligible> | Step-by-step reasoning uses the standard Messages API. |
| [PDF support](/docs/en/build-with-claude/pdf-support) | `/v1/messages` | <Eligible>Yes</Eligible> | <Eligible>Yes</Eligible> | PDF document processing uses the standard Messages API. HIPAA eligibility applies to PDFs sent inline via the Messages API, not through the Files API. |
| [Search results](/docs/en/build-with-claude/search-results) | `/v1/messages` (with `search_results` source) | <Eligible>Yes</Eligible> | <Eligible>Yes</Eligible> | RAG citation support uses the standard Messages API. |
| [Bash tool](/docs/en/agents-and-tools/tool-use/bash-tool) | `/v1/messages` (with `bash` tool) | <Eligible>Yes</Eligible> | <Eligible>Yes</Eligible> | Client-side tool executed in your environment. |
| [Text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool) | `/v1/messages` (with `text_editor` tool) | <Eligible>Yes</Eligible> | <Eligible>Yes</Eligible> | Client-side tool executed in your environment. |
| [Computer use](/docs/en/agents-and-tools/tool-use/computer-use-tool) | `/v1/messages` (with `computer` tool) | <Eligible>Yes</Eligible> | <Eligible status="no">No</Eligible> | Client-side tool where screenshots and files are captured and stored in your environment, not by Anthropic. See [Computer use](/docs/en/agents-and-tools/tool-use/computer-use-tool#data-retention). |
| [Fine-grained tool streaming](/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming) | `/v1/messages` | <Eligible>Yes</Eligible> | <Eligible>Yes</Eligible> | Streaming tool parameters uses the standard Messages API. |
| [Prompt caching](/docs/en/build-with-claude/prompt-caching) | `/v1/messages` | <Eligible>Yes</Eligible> | <Eligible>Yes</Eligible> | Your prompts and Claude's outputs are not stored. KV cache representations and cryptographic hashes are held in memory for the cache TTL and promptly deleted after expiry. See [Prompt caching](/docs/en/build-with-claude/prompt-caching#data-retention). |
| [Structured outputs](/docs/en/build-with-claude/structured-outputs) | `/v1/messages` | <Eligible status="qualified">Yes (qualified)</Eligible> | <Eligible>Yes</Eligible><sup>3</sup> | Your prompts and Claude's outputs are not stored. Only the JSON schema is cached, for up to 24 hours since last use. This also covers [strict tool use](/docs/en/agents-and-tools/tool-use/strict-tool-use) (`strict: true` on tools), which uses the same grammar pipeline. See [Structured outputs](/docs/en/build-with-claude/structured-outputs#data-retention). |
| [Tool search](/docs/en/agents-and-tools/tool-use/tool-search-tool) | `/v1/messages` (with `tool_search` tool) | <Eligible>Yes</Eligible> | <Eligible status="no">No</Eligible> | Tool search uses the standard Messages API. |
| [Batch processing](/docs/en/build-with-claude/batch-processing) | `/v1/messages/batches` | <Eligible status="no">No</Eligible> | <Eligible status="no">No</Eligible> | 29-day retention; async storage required. See [Batch processing](/docs/en/build-with-claude/batch-processing#data-retention). |
| [Code execution](/docs/en/agents-and-tools/tool-use/code-execution-tool) | `/v1/messages` (with `code_execution` tool) | <Eligible status="no">No</Eligible> | <Eligible status="no">No</Eligible> | Container data retained up to 30 days. See [Code execution](/docs/en/agents-and-tools/tool-use/code-execution-tool#data-retention). |
| [Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling) | `/v1/messages` (with `code_execution` tool) | <Eligible status="no">No</Eligible> | <Eligible status="no">No</Eligible> | Built on code execution containers; data retained up to 30 days. See [Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#data-retention). |
| [Files API](/docs/en/build-with-claude/files) | `/v1/files` | <Eligible status="no">No</Eligible> | <Eligible status="no">No</Eligible> | Files retained until explicitly deleted. See [Files API](/docs/en/build-with-claude/files#data-retention). |
| [Agent skills](/docs/en/agents-and-tools/agent-skills/overview) | `/v1/messages` (with `skills`) / `/v1/skills` | <Eligible status="no">No</Eligible> | <Eligible status="no">No</Eligible> | Skill data retained per standard policy. See [Agent skills](/docs/en/agents-and-tools/agent-skills/overview#data-retention). |
| [MCP connector](/docs/en/agents-and-tools/mcp-connector) | `/v1/messages` (with `mcp_servers`) | <Eligible status="no">No</Eligible> | <Eligible status="no">No</Eligible> | Data retained per standard policy. See [MCP connector](/docs/en/agents-and-tools/mcp-connector#data-retention). |

<sup>1</sup> [Dynamic filtering](/docs/en/agents-and-tools/tool-use/web-search-tool#dynamic-filtering) is not eligible for ZDR or HIPAA.

<sup>2</sup> While web fetch is ZDR-eligible, website publishers may retain request data (such as fetched URLs and request metadata) according to their own policies.

<sup>3</sup> PHI must not be included in JSON schema definitions. See [PHI handling guidelines](#phi-handling-guidelines).

## Limitations and exclusions

### CORS not supported for ZDR

**Cross-Origin Resource Sharing (CORS)** is not supported for organizations with ZDR arrangements. If you need to make API calls from browser-based applications, you must:

- Use a backend proxy server to make API calls on behalf of your front end
- Implement your own CORS handling on the proxy server
- Never expose API keys directly in browser JavaScript

### Data retention for policy violations and where required by law

Even with ZDR or HIPAA arrangements in place, Anthropic may retain data where required by law or to combat Usage Policy violations and malicious uses of Anthropic's platform. As a result, if a chat or session is flagged for such a violation, Anthropic may retain inputs and outputs for up to 2 years.

## Frequently asked questions

<section title="How do I know if my organization has ZDR arrangements?">

Check your contract terms or contact your Anthropic account representative to confirm if your organization has ZDR arrangements in place.

</section>

<section title="Can I use ZDR-eligible (qualified) features under my ZDR arrangement?">

Yes. These features retain a minimal, documented set of technical data, not your prompts or Claude's outputs. See [Anthropic's approach to data retention](#anthropics-approach-to-data-retention) for the commitments that govern these features.

</section>

<Accordion title={'What happens if I use a feature marked "No" under ZDR?'}>
Features marked "No" for ZDR are fundamentally stateful: the Batch API stores your jobs, the Files API stores your files, and code execution runs in persistent containers. Data for these features is retained per the feature's documented policy. Using them is a choice to step outside your ZDR arrangement for that specific data.
</Accordion>

<section title="Can I request deletion of data from features that are not ZDR-eligible?">

Contact your Anthropic account representative to discuss deletion options for non-ZDR features.

</section>

<section title="How does HIPAA readiness differ from ZDR?">

ZDR prevents customer data from being stored at rest after the API response is returned. HIPAA readiness involves a broader set of privacy and security safeguards that protect PHI throughout its lifecycle, including encryption, access controls, and audit logging. HIPAA-ready API access provides a foundation for progressively enabling more features because data can be retained with proper safeguards rather than requiring immediate deletion.

</section>

<section title="Do I still need ZDR if I have HIPAA readiness?">

No. HIPAA-ready API access is designed as an alternative to ZDR for organizations handling PHI. With HIPAA readiness enabled, you get access to supported API features while maintaining the privacy and security protections that HIPAA requires.

</section>

<section title="What happens if I use a non-eligible feature under HIPAA?">

The API returns a `400` error with an `invalid_request_error` type. The error message identifies which features are not available. Remove the non-eligible features from your request and retry.

</section>

<section title="Can I use the same organization for HIPAA and non-HIPAA workloads?">

No. HIPAA readiness is enforced at the organization level and automatically blocks all non-eligible features. Use a separate organization for workloads that do not require HIPAA readiness.

</section>

<section title="How do I request HIPAA-ready API access?">

Contact the [Anthropic sales team](https://claude.com/contact-sales) to discuss HIPAA-ready API access and sign a Business Associate Agreement.

</section>

<section title="Does this apply to Claude on AWS Bedrock or Vertex AI?">

No, only the Claude API is eligible for ZDR and HIPAA readiness. For Claude deployments on AWS Bedrock or Vertex AI, refer to those platforms' data retention and compliance policies.

</section>

<section title="Is Claude Code eligible for ZDR?">

Claude Code is eligible for ZDR through two paths:

- **API keys:** Claude Code used with pay-as-you-go API keys from a Commercial organization
- **Claude Enterprise:** Claude Code used through Claude Enterprise with ZDR enabled for the organization

ZDR is enabled on a per-organization basis. Each new organization requires ZDR to be enabled separately by your account team. ZDR does not automatically apply to new organizations created under the same account.

Additionally, if you have metrics logging enabled in Claude Code, productivity data (such as usage statistics) is exempted from ZDR and may be retained.

For full details on ZDR for Claude Code on Claude Enterprise, including disabled features and how to request enablement, see the [Claude Code ZDR documentation](https://code.claude.com/docs/en/zero-data-retention).

</section>

<section title="Does Claude for Excel support ZDR?">

No, Claude for Excel is not currently ZDR-eligible.

</section>

<section title="How do I request ZDR?">

To request a ZDR arrangement, contact the [Anthropic sales team](https://claude.com/contact-sales).

</section>

## Related resources

- [Privacy Policy](https://www.anthropic.com/legal/privacy)
- [Structured outputs](/docs/en/build-with-claude/structured-outputs)
- [Prompt caching](/docs/en/build-with-claude/prompt-caching)
- [Batch processing](/docs/en/build-with-claude/batch-processing)
- [Files API](/docs/en/api/files-create)
- [Trust Center](https://trust.anthropic.com/resources)