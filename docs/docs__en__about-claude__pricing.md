# Pricing

Learn about Anthropic's pricing structure for models and features

---

This page provides detailed pricing information for Anthropic's models and features. All prices are in USD.

For the most current pricing information, visit [claude.com/pricing](https://claude.com/pricing).

## Model pricing

The following table shows pricing for all Claude models:

| Model             | Base Input Tokens | 5m Cache Writes | 1h Cache Writes | Cache Hits & Refreshes | Output Tokens |
|-------------------|-------------------|-----------------|-----------------|----------------------|---------------|
| Claude Opus 4.7     | $5 / MTok         | $6.25 / MTok    | $10 / MTok      | $0.50 / MTok | $25 / MTok    |
| Claude Opus 4.6     | $5 / MTok         | $6.25 / MTok    | $10 / MTok      | $0.50 / MTok | $25 / MTok    |
| Claude Opus 4.5   | $5 / MTok         | $6.25 / MTok    | $10 / MTok      | $0.50 / MTok | $25 / MTok    |
| Claude Opus 4.1   | $15 / MTok        | $18.75 / MTok   | $30 / MTok      | $1.50 / MTok | $75 / MTok    |
| Claude Opus 4     | $15 / MTok        | $18.75 / MTok   | $30 / MTok      | $1.50 / MTok | $75 / MTok    |
| Claude Sonnet 4.6   | $3 / MTok         | $3.75 / MTok    | $6 / MTok       | $0.30 / MTok | $15 / MTok    |
| Claude Sonnet 4.5   | $3 / MTok         | $3.75 / MTok    | $6 / MTok       | $0.30 / MTok | $15 / MTok    |
| Claude Sonnet 4   | $3 / MTok         | $3.75 / MTok    | $6 / MTok       | $0.30 / MTok | $15 / MTok    |
| Claude Sonnet 3.7 ([deprecated](/docs/en/about-claude/model-deprecations)) | $3 / MTok         | $3.75 / MTok    | $6 / MTok       | $0.30 / MTok | $15 / MTok    |
| Claude Haiku 4.5  | $1 / MTok         | $1.25 / MTok    | $2 / MTok       | $0.10 / MTok | $5 / MTok     |
| Claude Haiku 3.5  | $0.80 / MTok      | $1 / MTok       | $1.6 / MTok     | $0.08 / MTok | $4 / MTok     |
| Claude Opus 3 ([deprecated](/docs/en/about-claude/model-deprecations))    | $15 / MTok        | $18.75 / MTok   | $30 / MTok      | $1.50 / MTok | $75 / MTok    |
| Claude Haiku 3    | $0.25 / MTok      | $0.30 / MTok    | $0.50 / MTok    | $0.03 / MTok | $1.25 / MTok  |

<Note>
MTok = Million tokens. The "Base Input Tokens" column shows standard input pricing, the "5m Cache Writes", "1h Cache Writes", and "Cache Hits & Refreshes" columns are specific to [prompt caching](#prompt-caching), and "Output Tokens" shows output pricing. See [prompt caching pricing](#prompt-caching) for an explanation of the cache columns and pricing multipliers.
</Note>

<Note>
Opus 4.7 uses a new tokenizer compared to previous models, contributing to its improved performance on a wide range of tasks. This new tokenizer may use up to 35% more tokens for the same fixed text.
</Note>

For Claude Platform on AWS pricing, see [Claude Platform on AWS pricing](#claude-platform-on-aws-pricing).

## Cloud platform pricing

This section covers partner-operated cloud platforms, where the cloud provider invoices you. For Anthropic-operated cloud platforms billed through a marketplace, see [Claude Platform on AWS pricing](#claude-platform-on-aws-pricing) and [Claude in Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry).

Claude models are available on [Amazon Bedrock](/docs/en/build-with-claude/claude-in-amazon-bedrock) and [Vertex AI](/docs/en/build-with-claude/claude-on-vertex-ai). For official pricing, visit:
- [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/)
- [Vertex AI pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing#claude-models)

<Note>
**Regional and multi-region endpoint pricing for Claude 4.5 models and beyond**

Starting with Claude Sonnet 4.5, Haiku 4.5, and Opus 4.5:
- **Bedrock** offers two endpoint types: global endpoints (dynamic routing for maximum availability) and regional endpoints (guaranteed data routing through specific geographic regions).
- **Vertex AI** offers three endpoint types: global endpoints, multi-region endpoints (dynamic routing within a geographic area), and regional endpoints.

Regional and multi-region endpoints include a 10% premium over global endpoints. The Claude API (first-party) is global by default; for first-party data residency options and pricing, see [Data residency pricing](#data-residency-pricing).

**Scope:** This pricing structure applies to Claude Sonnet 4.5, Haiku 4.5, Opus 4.5, and all future models. Earlier models (Claude Sonnet 4 (deprecated), Opus 4 (deprecated), and prior releases) retain their existing pricing.

For implementation details and code examples:
- [Amazon Bedrock global vs regional endpoints](/docs/en/build-with-claude/claude-in-amazon-bedrock#regions) for Opus 4.7, Haiku 4.5, and later models, or [the legacy integration](/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy#global-vs-regional-endpoints) for all other models on Bedrock
- [Vertex AI global, multi-region, and regional endpoints](/docs/en/build-with-claude/claude-on-vertex-ai#global-multi-region-and-regional-endpoints)
</Note>

## Claude Platform on AWS pricing

[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws) bills through AWS Marketplace using Claude Consumption Units (CCUs). Anthropic rates your token usage in USD at standard per-model, per-feature rates, applies any negotiated discount, converts the result to CCUs at $0.01 per CCU, and reports the CCU quantity to AWS Marketplace hourly. Your AWS bill shows a single CCU line item.

| Concept | Details |
| :--- | :--- |
| **Billing unit** | Claude Consumption Unit (CCU) |
| **CCU price** | $0.01 per CCU (fixed; discounts apply at token-to-CCU conversion, not to the CCU price) |
| **Conversion** | Token usage rated in USD at standard per-model, per-feature rates (same as [Claude API pricing](#model-pricing)), then converted to CCUs at $0.01 per CCU |
| **Billing cadence** | Hourly metering to AWS Marketplace; monthly invoices |
| **Payment model** | Arrears only (postpaid); no prepaid credits |
| **Discounts** | Applied as fewer CCUs metered |
| **Tax** | Pre-tax metering; AWS Marketplace handles tax |
| **Cost visibility** | Real-time breakdown in the Claude Console (access through the AWS Console); AWS Cost Explorer shows aggregated CCU |

<Note>
**Claude Consumption Units.** If Customer accesses the Services through certain Marketplace Platforms (e.g., Claude Platform on AWS), usage will be invoiced in Claude Consumption Units ("CCU") rather than per MTok. A CCU is a unit of measure used solely for Marketplace Platform invoicing. One hundred (100) CCU represents $1.00 USD of fees owed for the Services, calculated at the applicable prices on [claude.com/pricing#api](https://claude.com/pricing#api), after application of any discounts.
</Note>

### Inference geography

For Claude Opus 4.6, Claude Sonnet 4.6, and later models, using `inference_geo: "us"` applies a 1.1x pricing multiplier. `inference_geo: "global"` (default) uses standard pricing. See [Data residency](/docs/en/manage-claude/data-residency) for details.

### Private offers

When you sign up on the AWS Console **Claude Platform on AWS** service page, the AWS Console looks up any private offer associated with your account and prompts you to accept it in AWS Marketplace. Contact your Anthropic account representative for private offer terms.

<Note>
If you have an existing Amazon Bedrock private offer, contact your Anthropic or AWS account representative before getting started with Claude Platform on AWS to ensure your discounts are applied correctly. Discounts cannot be applied retroactively to usage incurred before your private offer is accepted.
</Note>

## Feature-specific pricing

### Prompt caching

Prompt caching reduces costs and latency by reusing previously processed portions of your prompt across API calls. Instead of reprocessing the same large system prompt, document, or conversation history on every request, the API reads from cache at a fraction of the standard input price.

There are two ways to enable prompt caching:

- **Automatic caching:** Add a single `cache_control` field at the top level of your request. The system automatically manages cache breakpoints as conversations grow. This is the recommended starting point for most use cases.
- **Explicit cache breakpoints:** Place `cache_control` directly on individual content blocks for fine-grained control over exactly what gets cached.

Prompt caching uses the following pricing multipliers relative to base input token rates:

| Cache operation | Multiplier | Duration |
|:----------------|:-----------|:---------|
| 5-minute cache write | 1.25x base input price | Cache valid for 5 minutes |
| 1-hour cache write | 2x base input price | Cache valid for 1 hour |
| Cache read (hit) | 0.1x base input price | Same duration as the preceding write |

Cache write tokens are charged when content is first stored. Cache read tokens are charged when a subsequent request retrieves the cached content. A cache hit costs 10% of the standard input price, which means caching pays off after just one cache read for the 5-minute duration (1.25x write), or after two cache reads for the 1-hour duration (2x write).

These multipliers stack with other pricing modifiers, including the Batch API discount and data residency.

For implementation details, supported models, and code examples, see [Prompt caching](/docs/en/build-with-claude/prompt-caching).

### Data residency pricing

For Claude Opus 4.6, Claude Sonnet 4.6, and later models, specifying US-only inference through the `inference_geo` parameter incurs a 1.1x multiplier on all token pricing categories, including input tokens, output tokens, cache writes, and cache reads. Global routing (the default) uses standard pricing.

This applies to the Claude API (first-party) and Claude Platform on AWS. Partner-operated platforms (Bedrock and Vertex AI) have independent regional pricing. See [Bedrock](https://aws.amazon.com/bedrock/pricing/) and [Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/pricing#claude-models) for details. Earlier models do not support the `inference_geo` parameter and always use standard pricing; requests that include the parameter on these models return a 400 error.

For more information, see [Data residency](/docs/en/manage-claude/data-residency).

### Fast mode pricing

[Fast mode](/docs/en/build-with-claude/fast-mode), in beta (research preview), provides significantly faster output for Claude Opus 4.6 at premium pricing (6x standard rates). Fast mode pricing applies across the full context window, including requests over 200k input tokens. Fast mode is not available on Claude Platform on AWS. Currently supported on Opus 4.6:

| Input | Output |
|:------|:-------|
| $30 / MTok | $150 / MTok |

Fast mode pricing stacks with other pricing modifiers:
- [Prompt caching multipliers](#prompt-caching) apply on top of fast mode pricing
- [Data residency](/docs/en/manage-claude/data-residency) multipliers apply on top of fast mode pricing

Fast mode is not available with the [Batch API](#batch-processing).

For more information, see [Fast mode](/docs/en/build-with-claude/fast-mode).

### Batch processing

The Batch API allows asynchronous processing of large volumes of requests with a 50% discount on both input and output tokens.

| Model             | Batch input      | Batch output    |
|-------------------|------------------|-----------------|
| Claude Opus 4.7       | $2.50 / MTok     | $12.50 / MTok   |
| Claude Opus 4.6       | $2.50 / MTok     | $12.50 / MTok   |
| Claude Opus 4.5     | $2.50 / MTok     | $12.50 / MTok   |
| Claude Opus 4.1     | $7.50 / MTok     | $37.50 / MTok   |
| Claude Opus 4     | $7.50 / MTok     | $37.50 / MTok   |
| Claude Sonnet 4.6   | $1.50 / MTok     | $7.50 / MTok    |
| Claude Sonnet 4.5   | $1.50 / MTok     | $7.50 / MTok    |
| Claude Sonnet 4   | $1.50 / MTok     | $7.50 / MTok    |
| Claude Sonnet 3.7 ([deprecated](/docs/en/about-claude/model-deprecations)) | $1.50 / MTok     | $7.50 / MTok    |
| Claude Haiku 4.5  | $0.50 / MTok     | $2.50 / MTok    |
| Claude Haiku 3.5  | $0.40 / MTok     | $2 / MTok       |
| Claude Opus 3 ([deprecated](/docs/en/about-claude/model-deprecations))  | $7.50 / MTok     | $37.50 / MTok   |
| Claude Haiku 3    | $0.125 / MTok    | $0.625 / MTok   |

For more information about batch processing, see [Batch processing](/docs/en/build-with-claude/batch-processing).

### Long context pricing

[Claude Mythos Preview](https://anthropic.com/glasswing), Opus 4.7, Opus 4.6, and Sonnet 4.6 include the full [1M token context window](/docs/en/build-with-claude/context-windows) at standard pricing. (A 900k-token request is billed at the same per-token rate as a 9k-token request.) Prompt caching and batch processing discounts apply at standard rates across the full context window.

### Tool use pricing

Tool use requests are priced based on:
1. The total number of input tokens sent to the model (including in the `tools` parameter)
2. The number of output tokens generated
3. For server-side tools, additional usage-based pricing (e.g., web search charges per search performed)

Client-side tools are priced the same as any other Claude API request, while server-side tools may incur additional charges based on their specific usage.

The additional tokens from tool use come from:

- The `tools` parameter in API requests (tool names, descriptions, and schemas)
- `tool_use` content blocks in API requests and responses
- `tool_result` content blocks in API requests

When you use `tools`, we also automatically include a special system prompt for the model which enables tool use. The number of tool use tokens required for each model are listed below (excluding the additional tokens listed above). Note that the table assumes at least 1 tool is provided. If no `tools` are provided, then a tool choice of `none` uses 0 additional system prompt tokens.

| Model                    | Tool choice                                          | Tool use system prompt token count          |
|--------------------------|------------------------------------------------------|---------------------------------------------|
| Claude Opus 4.7                | `auto`, `none`<hr />`any`, `tool`   | 346 tokens<hr />313 tokens |
| Claude Opus 4.6              | `auto`, `none`<hr />`any`, `tool`   | 346 tokens<hr />313 tokens |
| Claude Opus 4.5            | `auto`, `none`<hr />`any`, `tool`   | 346 tokens<hr />313 tokens |
| Claude Opus 4.1            | `auto`, `none`<hr />`any`, `tool`   | 346 tokens<hr />313 tokens |
| Claude Opus 4            | `auto`, `none`<hr />`any`, `tool`   | 346 tokens<hr />313 tokens |
| Claude Sonnet 4.6          | `auto`, `none`<hr />`any`, `tool`   | 346 tokens<hr />313 tokens |
| Claude Sonnet 4.5          | `auto`, `none`<hr />`any`, `tool`   | 346 tokens<hr />313 tokens |
| Claude Sonnet 4          | `auto`, `none`<hr />`any`, `tool`   | 346 tokens<hr />313 tokens |
| Claude Sonnet 3.7 ([deprecated](/docs/en/about-claude/model-deprecations))        | `auto`, `none`<hr />`any`, `tool`   | 346 tokens<hr />313 tokens |
| Claude Haiku 4.5         | `auto`, `none`<hr />`any`, `tool`   | 346 tokens<hr />313 tokens |
| Claude Haiku 3.5         | `auto`, `none`<hr />`any`, `tool`   | 264 tokens<hr />340 tokens |
| Claude Opus 3 ([deprecated](/docs/en/about-claude/model-deprecations))            | `auto`, `none`<hr />`any`, `tool`   | 530 tokens<hr />281 tokens |
| Claude Sonnet 3          | `auto`, `none`<hr />`any`, `tool`   | 159 tokens<hr />235 tokens |
| Claude Haiku 3           | `auto`, `none`<hr />`any`, `tool`   | 264 tokens<hr />340 tokens |

These token counts are added to your normal input and output tokens to calculate the total cost of a request.

For current per-model prices, refer to the [model pricing](#model-pricing) section.

For more information about tool use implementation and best practices, see [Tool use](/docs/en/agents-and-tools/tool-use/overview).

### Specific tool pricing

#### Bash tool

The bash tool adds **245 input tokens** to your API calls.

Additional tokens are consumed by:
- Command outputs (stdout/stderr)
- Error messages
- Large file contents

See [tool use pricing](#tool-use-pricing) for complete pricing details.

#### Code execution tool

**Code execution is free when used with web search or web fetch.** When `web_search_20260209` or `web_fetch_20260209` is included in your API request, there are no additional charges for code execution tool calls beyond the standard input and output token costs.

When used without these tools, code execution is billed by execution time, tracked separately from token usage:

- Execution time has a minimum of 5 minutes
- Each organization receives **1,550 free hours** of usage per month
- Additional usage beyond 1,550 hours is billed at **$0.05 per hour, per container**
- If files are included in the request, execution time is billed even if the tool is not invoked, due to files being preloaded onto the container

Code execution usage is tracked in the response:

```json
"usage": {
  "input_tokens": 105,
  "output_tokens": 239,
  "server_tool_use": {
    "code_execution_requests": 1
  }
}
```

#### Text editor tool

The text editor tool uses the same pricing structure as other tools used with Claude. It follows the standard input and output token pricing based on the Claude model you're using.

In addition to the base tokens, the following additional input tokens are needed for the text editor tool:

| Tool | Additional input tokens |
| ----------------------------------------- | --------------------------------------- |
| `text_editor_20250429` (Claude 4.x) | 700 tokens |
| `text_editor_20250124` (Claude Sonnet 3.7 ([deprecated](/docs/en/about-claude/model-deprecations))) | 700 tokens |

See [tool use pricing](#tool-use-pricing) for complete pricing details.

#### Web search tool

Web search usage is charged in addition to token usage:

```json
"usage": {
  "input_tokens": 105,
  "output_tokens": 6039,
  "cache_read_input_tokens": 7123,
  "cache_creation_input_tokens": 7345,
  "server_tool_use": {
    "web_search_requests": 1
  }
}
```

Web search is available on the Claude API for **$10 per 1,000 searches**, plus standard token costs for search-generated content. Web search results retrieved throughout a conversation are counted as input tokens, in search iterations executed during a single turn and in subsequent conversation turns.

Each web search counts as one use, regardless of the number of results returned. If an error occurs during web search, the web search will not be billed.

#### Web fetch tool

Web fetch usage has **no additional charges** beyond standard token costs:

```json
"usage": {
  "input_tokens": 25039,
  "output_tokens": 931,
  "cache_read_input_tokens": 0,
  "cache_creation_input_tokens": 0,
  "server_tool_use": {
    "web_fetch_requests": 1
  }
}
```

The web fetch tool is available on the Claude API at **no additional cost**. You only pay standard token costs for the fetched content that becomes part of your conversation context.

To protect against inadvertently fetching large content that would consume excessive tokens, use the `max_content_tokens` parameter to set appropriate limits based on your use case and budget considerations.

Example token usage for typical content:
- Average web page (10&nbsp;kB): ~2,500 tokens
- Large documentation page (100&nbsp;kB): ~25,000 tokens
- Research paper PDF (500&nbsp;kB): ~125,000 tokens

#### Computer use tool

Computer use follows the standard [tool use pricing](/docs/en/agents-and-tools/tool-use/overview#pricing). When using the computer use tool:

**System prompt overhead**: The computer use beta adds 466-499 tokens to the system prompt

**Computer use tool token usage**:
| Model | Input tokens per tool definition |
| ----- | -------------------------------- |
| Claude 4.x models | 735 tokens |
| Claude Sonnet 3.7 ([deprecated](/docs/en/about-claude/model-deprecations)) | 735 tokens |

**Additional token consumption**:
- Screenshot images (see [Vision pricing](/docs/en/build-with-claude/vision))
- Tool execution results returned to Claude

<Note>
If you're also using bash or text editor tools alongside computer use, those tools have their own token costs as documented in their respective pages.
</Note>

## Claude Managed Agents pricing

[Claude Managed Agents](/docs/en/managed-agents/overview) is billed on two dimensions: tokens and session runtime.

### Tokens

All tokens consumed by a Claude Managed Agents session are billed at the rates shown in [Model pricing](#model-pricing). [Prompt caching](#prompt-caching) multipliers apply identically. Web search triggered inside a session incurs the standard $10 per 1,000 searches. On [Claude Platform on AWS](#claude-platform-on-aws-pricing), session token and runtime charges convert to Claude Consumption Units at the standard rate.

The following Messages API modifiers do **not** apply to Claude Managed Agents sessions:

| Modifier | Why it doesn't apply |
| --- | --- |
| [Batch API discount](#batch-processing) | Sessions are stateful and interactive. There is no batch mode. |
| [Fast mode premium](#fast-mode-pricing) | Inference speed is managed by the runtime. |
| [Data residency multiplier](#data-residency-pricing) | `inference_geo` is a Messages API request field. |
| [Cloud platform pricing](#cloud-platform-pricing) | Not available on partner-operated cloud platforms. |

### Session runtime

| SKU | Rate | Metering |
| --- | --- | --- |
| Session runtime | $0.08 per session-hour | `running` status duration |

Runtime is measured to the millisecond and accrues only while the session's status is `running`. Time spent `idle` (waiting for your next message or a tool confirmation), `rescheduling`, or `terminated` does not count toward runtime.

<Note>
Session runtime replaces the [Code Execution](#code-execution-tool) container-hour billing model when using Claude Managed Agents. You are not separately billed for container hours on top of session runtime.
</Note>

### Worked example

A one-hour coding session using Claude Opus 4.7 that consumes 50,000 input tokens and 15,000 output tokens:

| Line item | Calculation | Cost |
| --- | --- | --- |
| Input tokens | 50,000 × $5 / 1,000,000 | $0.25 |
| Output tokens | 15,000 × $25 / 1,000,000 | $0.375 |
| Session runtime | 1.0 hour × $0.08 | $0.08 |
| **Total** | | **$0.705** |

If prompt caching is active and 40,000 of the input tokens are cache reads:

| Line item | Calculation | Cost |
| --- | --- | --- |
| Uncached input tokens | 10,000 × $5 / 1,000,000 | $0.05 |
| Cache read tokens | 40,000 × $5 × 0.1 / 1,000,000 | $0.02 |
| Output tokens | 15,000 × $25 / 1,000,000 | $0.375 |
| Session runtime | 1.0 hour × $0.08 | $0.08 |
| **Total** | | **$0.525** |

<Note>
  Example calculation for processing 10,000 support tickets:
  - Average ~3,700 tokens per conversation
  - Using Claude Haiku 4.5 at $1/MTok input, $5/MTok output
  - Total cost: ~$37.00 per 10,000 tickets
</Note>

For a detailed walkthrough of this calculation, see the [customer support agent guide](/docs/en/about-claude/use-case-guides/customer-support-chat).

## Additional pricing considerations

### Cost optimization strategies

When building agents with Claude:

1. **Use appropriate models:** Choose Haiku for simple tasks, Sonnet for most production workloads, and Opus for the most complex reasoning
2. **Implement prompt caching:** Reduce costs for repeated context
3. **Batch operations:** Use the Batch API for non-time-sensitive tasks
4. **Monitor usage patterns:** Track token consumption to identify optimization opportunities

<Tip>
  For high-volume agent applications, contact the [enterprise sales team](https://claude.com/contact-sales) for custom pricing arrangements.
</Tip>

### Rate limits

Rate limits vary by usage tier and affect how many requests you can make:

- **Tier 1:** Entry-level usage with basic limits
- **Tier 2:** Increased limits for growing applications
- **Tier 3:** Higher limits for established applications
- **Tier 4:** Maximum standard limits
- **Enterprise:** Custom limits available

For detailed rate limit information, see [Rate limits](/docs/en/api/rate-limits).

For higher rate limits or custom pricing arrangements, [contact the sales team](https://claude.com/contact-sales).

### Volume discounts

Volume discounts may be available for high-volume users. These are negotiated on a case-by-case basis.

- Standard tiers use the pricing shown in [Model pricing](#model-pricing)
- Enterprise customers can [contact sales](mailto:sales@anthropic.com) for custom pricing
- Academic and research discounts may be available

### Enterprise pricing

For enterprise customers with specific needs:

- Custom rate limits
- Volume discounts
- Dedicated support
- Custom terms

Contact the sales team at [sales@anthropic.com](mailto:sales@anthropic.com) or through the [Claude Console](/settings/limits) to discuss enterprise pricing options.

## Billing and payment

- Billing is based on actual monthly usage
- All payments are in USD
- Credit card and invoicing options available
- Usage tracking available in the [Claude Console](/)

## Frequently asked questions

**How is token usage calculated?**

Tokens are pieces of text that models process. As a rough estimate, 1 token is approximately 4 characters or 0.75 words in English. The exact count varies by language and content type.

**Are there free tiers or trials?**

New users receive a small amount of free credits to test the API. [Contact sales](mailto:sales@anthropic.com) for information about extended trials for enterprise evaluation.

**How do discounts stack?**

Batch API and prompt caching discounts can be combined. For example, using both features together provides significant cost savings compared to standard API calls. See [prompt caching pricing](#prompt-caching) for how the multipliers interact.

**What payment methods are accepted?**

Major credit cards are accepted for standard accounts. Enterprise customers can arrange invoicing and other payment methods.

For additional questions about pricing, contact [support@anthropic.com](mailto:support@anthropic.com).