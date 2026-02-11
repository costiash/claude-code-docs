# Zero Data Retention (ZDR)

Learn about Anthropic's Zero Data Retention (ZDR) policy, including which API endpoints and features are ZDR-eligible.

---

This page provides a list of which API endpoints and features are ZDR-eligible and which are not.

<Note>
Information about Anthropic's standard retention policies are set out in [Anthropic's commercial data retention policy](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data) and [consumer data retention policy](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data).

Zero Data Retention (ZDR) is Anthropic's commitment to ensuring that customer data submitted through certain API endpoints is not stored after the API response is returned except where needed to comply with law or combat misuse, as outlined in a customer's arrangements with Anthropic. Subject to these exceptions, when using ZDR-enabled endpoints, your data is processed in real-time and immediately discarded, with no logging or storage of prompts or outputs.
</Note>

## Important limitations

**What ZDR covers**

- **Certain Claude APIs**: ZDR applies to the Claude Messages and Token Counting APIs
- **Claude Code**: ZDR applies when used with your enterprise API credentials

**What ZDR does NOT cover**

- **Beta products and features**: Products and features in beta unless specified otherwise
- **Console and Workbench**: Any usage on Console or Workbench
- **Claude consumer products**: Claude Free, Pro, or Max plans, including when customers on those plans use Claude's web, desktop, or mobile apps or Claude Code
- **Claude for Work and Claude for Enterprise**: Claude for Work and Claude for Enterprise product interfaces are not covered by ZDR; only Commercial organization API keys are eligible
- **Third-party integrations**: Data processed by third-party websites, tools, or other integrations is not covered by ZDR, though some may offer similar offerings. When using external services in conjunction with the Claude API, make sure to review those services' data handling practices.

<Note>
For the most up-to-date information on what products and features are ZDR-eligible, please refer to your contract terms or contact your Anthropic account representative.
</Note>

## ZDR eligibility by product/feature

### Fully ZDR-eligible

These API endpoints process data in real-time:

| Feature | Endpoint | Description |
| ------- | -------- | ----------- |
| Messages API | `/v1/messages` | Standard API calls for generating Claude responses. |
| Token Counting | `/v1/messages/count_tokens` | Count tokens before sending requests. |

### Not ZDR-eligible

The following is a non-exhaustive list of endpoints and features that store data beyond when the API response is generated and are **not covered by ZDR arrangements**:

| Feature | Endpoint | Data Retention Policy | Why It's Not ZDR-Eligible |
| ------- | -------- | -------------------- | -------------------------- |
| Batch API | `/v1/messages/batches` | Standard policy: 29-day retention. Use the `/v1/messages/batches` DELETE endpoint to delete message batches at any time after processing. | Batch processing requires asynchronous storage of responses. |
| Files API | `/v1/files` | Files retained until explicitly deleted. | Beta features are excluded from ZDR. Files uploaded via the Files API are retained for future API requests. |
| Skills (Code Executor) | `/v1/skills` | Data retained for skill execution. | Beta features are excluded from ZDR. Skills use server-side code execution, which stores execution data and uploaded files beyond the immediate API response. |
| Context Management | `/v1/messages` (with `context_management`) | Files stored on Anthropic servers. | Beta features are excluded from ZDR. |

### Special cases

These features have nuanced data retention characteristics:

#### Prompt caching

**Status**: Prompt caching is a beta feature that stores KV cache representations and cryptographic hashes of cached content. Cached entries have at least a 5 or 60-minute lifetime and are isolated between organizations. Because Anthropic does not store the raw text of prompts or responses, this feature may be suitable for customers who require ZDR-type data retention commitments.

See [Prompt Caching documentation](/docs/en/build-with-claude/prompt-caching#what-is-the-cache-lifetime) for details.

#### Structured Outputs

**Status**: When using Structured Outputs with a JSON schema, prompts and responses are processed with ZDR. However, the JSON schema itself is temporarily cached for up to 24 hours for optimization purposes. No prompt or response data is retained.

## Additional limitations and exclusions

### CORS not supported

**Cross-Origin Resource Sharing (CORS)** is not supported for organizations with ZDR arrangements. If you need to make API calls from browser-based applications, you must:

- Use a backend proxy server to make API calls on behalf of your frontend
- Implement your own CORS handling on the proxy server
- Never expose API keys directly in browser JavaScript

### Data retention for policy violations and where required by law

Even with ZDR arrangements in place, Anthropic may retain data where required by law or to combat Usage Policy violations and malicious uses of Anthropic's platform. As a result, if a chat or session is flagged for such a violation, Anthropic may retain inputs and outputs for up to 2 years.

## Frequently asked questions

**How do I know if my organization has ZDR arrangements?**

Check your contract terms or contact your Anthropic account representative to confirm if your organization has ZDR arrangements in place.

**What happens if I use a feature that isn't ZDR-eligible when my organization has ZDR arrangements?**

Data will be retained according to the feature's standard retention policy. Ensure you understand the retention characteristics of each feature before use.

**Can I request deletion of data from features that are not ZDR-eligible?**

Contact your Anthropic account representative to discuss deletion options for non-ZDR features.

**Does ZDR apply to all Claude models?**

ZDR applies to ZDR-eligible endpoints regardless of which Claude model you use.

**Does this apply to Claude on AWS Bedrock or Google Vertex AI?**

No, only the Claude API is eligible for ZDR. For Claude deployments on AWS Bedrock or Google Vertex AI, refer to those platforms' data retention policies.

**Is Claude Code eligible for ZDR?**

Claude Code ZDR eligibility depends on how you authenticate:

- **Eligible**: Claude Code used with pay-as-you-go API keys from a Commercial organization
- **Not eligible**: Claude Code used via OAuth (premium seats through Claude for Enterprise)

Additionally, if you have metrics logging enabled in Claude Code, productivity data (such as usage statistics) is exempted from ZDR and may be retained.

**Does Claude for Excel support ZDR?**

No, Claude for Excel is not currently ZDR-eligible.

**How do I request ZDR?**

To request a ZDR arrangement, contact the [Anthropic sales team](https://claude.com/contact-sales).

## Related resources

- [Privacy Policy](https://www.anthropic.com/legal/privacy)
- [Batch Processing](/docs/en/build-with-claude/batch-processing)
- [Files API](/docs/en/api/files-create)
- [Agent SDK Sessions](/docs/en/agent-sdk/sessions)
- [Prompt Caching](/docs/en/build-with-claude/prompt-caching)