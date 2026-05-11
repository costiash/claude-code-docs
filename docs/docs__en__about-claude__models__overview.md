# Models overview

Claude is a family of state-of-the-art large language models developed by Anthropic. This guide introduces the available models and compares their performance.

---

## Choosing a model

If you're unsure which model to use, consider starting with **Claude Opus 4.7** for the most complex tasks. It is our most capable generally available model, with a step-change improvement in agentic coding over Claude Opus 4.6.

All current Claude models support text and image input, text output, multilingual capabilities, and vision. Models are available through the Claude API, [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws), [Amazon Bedrock](/docs/en/build-with-claude/claude-in-amazon-bedrock), [Vertex AI](/docs/en/build-with-claude/claude-on-vertex-ai), and [Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry).

Once you've picked a model, [learn how to make your first API call](/docs/en/get-started).

### Latest models comparison

| Feature | Claude Opus 4.7 | Claude Sonnet 4.6 | Claude Haiku 4.5 |
|:--------|:--------------|:------------------|:-----------------|
| **Description** | Our most capable generally available model for complex reasoning and agentic coding | The best combination of speed and intelligence | The fastest model with near-frontier intelligence |
| **Claude API ID** | claude-opus-4-7 | claude-sonnet-4-6 | claude-haiku-4-5-20251001 |
| **Claude API alias** | claude-opus-4-7 | claude-sonnet-4-6 | claude-haiku-4-5 |
| **AWS Bedrock ID** | anthropic.claude-opus-4-7<sup>3</sup> | anthropic.claude-sonnet-4-6 | anthropic.claude-haiku-4-5-20251001-v1:0 |
| **Vertex AI ID** | claude-opus-4-7 | claude-sonnet-4-6 | claude-haiku-4-5@20251001 |
| **Pricing**<sup>1</sup> | \$5 / input MTok<br/>\$25 / output MTok | \$3 / input MTok<br/>\$15 / output MTok | \$1 / input MTok<br/>\$5 / output MTok |
| **[Extended thinking](/docs/en/build-with-claude/extended-thinking)** | No | Yes | Yes |
| **[Adaptive thinking](/docs/en/build-with-claude/adaptive-thinking)** | Yes | Yes | No |
| **[Priority Tier](/docs/en/api/service-tiers)** | Yes | Yes | Yes |
| **Comparative latency** | Moderate | Fast | Fastest |
| **Context window** | <Tooltip tooltipContent="~555k words \ ~2.5M unicode characters (Opus 4.7 uses a new tokenizer)">1M tokens</Tooltip> | <Tooltip tooltipContent="~750k words \ ~3.4M unicode characters">1M tokens</Tooltip> | <Tooltip tooltipContent="~150k words \ ~680k unicode characters">200k tokens</Tooltip> |
| **Max output** | 128k tokens | 64k tokens | 64k tokens |
| **Reliable knowledge cutoff** | Jan 2026<sup>2</sup> | Aug 2025<sup>2</sup> | Feb 2025 |
| **Training data cutoff** | Jan 2026 | Jan 2026 | Jul 2025 |

_<sup>1 - See [Pricing](/docs/en/about-claude/pricing) for complete pricing information including Batch API discounts and prompt caching rates.</sup>_

_<sup>2 - **Reliable knowledge cutoff** indicates the date through which a model's knowledge is most extensive and reliable. **Training data cutoff** is the broader date range of training data used. For more information, see [Anthropic's Transparency Hub](https://www.anthropic.com/transparency).</sup>_

_<sup>3 - Claude Opus 4.7 is available on Bedrock through [Claude in Amazon Bedrock](/docs/en/build-with-claude/claude-in-amazon-bedrock) (the Messages-API Bedrock endpoint).</sup>_

<Info>
[Claude Mythos Preview](https://anthropic.com/glasswing) is offered separately as a research preview model for defensive cybersecurity workflows as part of [Project Glasswing](https://anthropic.com/glasswing). Access is invitation-only and there is no self-serve sign-up.
</Info>

<Note>Every Claude model ID is a pinned snapshot. Models with a date in the ID (for example, `20250929`) are fixed to that specific release. Starting with the Claude 4.6 generation, model IDs use a dateless format that is also a pinned snapshot, not an evergreen pointer. For models before the 4.6 generation, entries in the Claude API alias column are convenience pointers that resolve to a dated model ID. For details on the naming convention and how versioning works, see [Model IDs and versioning](/docs/en/about-claude/models/model-ids-and-versions).</Note>

<Note>Starting with **Claude Sonnet 4.5 and all subsequent models** (including Claude Sonnet 4.6), Bedrock offers two endpoint types: **global endpoints** (dynamic routing for maximum availability) and **regional endpoints** (guaranteed data routing through specific geographic regions). Vertex AI offers three endpoint types: global endpoints, **multi-region endpoints** (dynamic routing within a geographic area), and regional endpoints. For more information, see [Cloud platform pricing](/docs/en/about-claude/pricing#cloud-platform-pricing).</Note>

<Note>**Claude Platform on AWS** uses the same model IDs as the Claude API (for example, `claude-opus-4-6`), not Bedrock-style IDs. Model lifecycle on Claude Platform on AWS follows Anthropic's first-party [Model deprecations](/docs/en/about-claude/model-deprecations), not Bedrock's. See [Available models](/docs/en/build-with-claude/claude-platform-on-aws#available-models) for the model list.</Note>

<Tip>
You can query model capabilities and token limits programmatically with the [Models API](/docs/en/api/models/list). The response includes `max_input_tokens`, `max_tokens`, and a `capabilities` object for every available model.
</Tip>

<Note>
The Max output values above apply to the synchronous Messages API. On the [Message Batches API](/docs/en/build-with-claude/batch-processing#extended-output-beta), Opus 4.7, Opus 4.6, and Sonnet 4.6 support up to 300k output tokens by using the `output-300k-2026-03-24` beta header.
</Note>

<section title="Legacy models">

The following models are still available. Consider migrating to current models for improved performance:

| Feature | Claude Opus 4.6 | Claude Sonnet 4.5 | Claude Opus 4.5 | Claude Opus 4.1 | Claude Sonnet 4 (deprecated) | Claude Opus 4 (deprecated) |
|:--------|:----------------|:------------------|:----------------|:----------------|:----------------|:--------------|
| **Claude API ID** | claude-opus-4-6 | claude-sonnet-4-5-20250929 | claude-opus-4-5-20251101 | claude-opus-4-1-20250805 | claude-sonnet-4-20250514 | claude-opus-4-20250514 |
| **Claude API alias** | claude-opus-4-6 | claude-sonnet-4-5 | claude-opus-4-5 | claude-opus-4-1 | claude-sonnet-4-0 | claude-opus-4-0 |
| **AWS Bedrock ID** | anthropic.claude-opus-4-6-v1 | anthropic.claude-sonnet-4-5-20250929-v1:0 | anthropic.claude-opus-4-5-20251101-v1:0 | anthropic.claude-opus-4-1-20250805-v1:0 | anthropic.claude-sonnet-4-20250514-v1:0 | anthropic.claude-opus-4-20250514-v1:0 |
| **Vertex AI ID** | claude-opus-4-6 | claude-sonnet-4-5@20250929 | claude-opus-4-5@20251101 | claude-opus-4-1@20250805 | claude-sonnet-4@20250514 | claude-opus-4@20250514 |
| **Pricing** | \$5 / input MTok<br/>\$25 / output MTok | \$3 / input MTok<br/>\$15 / output MTok | \$5 / input MTok<br/>\$25 / output MTok | \$15 / input MTok<br/>\$75 / output MTok | \$3 / input MTok<br/>\$15 / output MTok | \$15 / input MTok<br/>\$75 / output MTok |
| **[Extended thinking](/docs/en/build-with-claude/extended-thinking)** | Yes | Yes | Yes | Yes | Yes | Yes |
| **[Priority Tier](/docs/en/api/service-tiers)** | Yes | Yes | Yes | Yes | Yes | Yes |
| **Comparative latency** | Moderate | Fast | Moderate | Moderate | Fast | Moderate |
| **Context window** | <Tooltip tooltipContent="~750k words \ ~3.4M unicode characters">1M tokens</Tooltip> | <Tooltip tooltipContent="~150k words \ ~680k unicode characters">200k tokens</Tooltip> | <Tooltip tooltipContent="~150k words \ ~680k unicode characters">200k tokens</Tooltip> | <Tooltip tooltipContent="~150k words \ ~680k unicode characters">200k tokens</Tooltip> | <Tooltip tooltipContent="~150k words \ ~680k unicode characters">200k tokens</Tooltip> | <Tooltip tooltipContent="~150k words \ ~680k unicode characters">200k tokens</Tooltip> |
| **Max output** | 128k tokens | 64k tokens | 64k tokens | 32k tokens | 64k tokens | 32k tokens |
| **Reliable knowledge cutoff** | May 2025<sup>1</sup> | Jan 2025<sup>1</sup> | May 2025<sup>1</sup> | Jan 2025<sup>1</sup> | Jan 2025<sup>1</sup> | Jan 2025<sup>1</sup> |
| **Training data cutoff** | Aug 2025 | Jul 2025 | Aug 2025 | Mar 2025 | Mar 2025 | Mar 2025 |

<Warning>
Claude Sonnet 4 (`claude-sonnet-4-20250514`) and Claude Opus 4 (`claude-opus-4-20250514`) are deprecated and will be retired on June 15, 2026. Migrate to [Claude Sonnet 4.6](/docs/en/about-claude/models/overview#latest-models-comparison) and [Claude Opus 4.7](/docs/en/about-claude/models/overview#latest-models-comparison) respectively before the retirement date.

See [model deprecations](/docs/en/about-claude/model-deprecations) for details.
</Warning>

_<sup>1 - **Reliable knowledge cutoff** indicates the date through which a model's knowledge is most extensive and reliable. **Training data cutoff** is the broader date range of training data used.</sup>_

</section>

## Prompt and output performance

Claude 4 models excel in:
- **Performance**: Top-tier results in reasoning, coding, multilingual tasks, long-context handling, honesty, and image processing. See the [Claude 4 blog post](http://www.anthropic.com/news/claude-4) for more information.
- **Engaging responses**: Claude models are ideal for applications that require rich, human-like interactions.

    - If you prefer more concise responses, you can adjust your prompts to guide the model toward the desired output length. Refer to the [prompt engineering guides](/docs/en/build-with-claude/prompt-engineering) for details.
    - For prompting best practices, see [Prompting best practices](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).
- **Output quality**: When migrating from previous model generations to Claude 4, you may notice larger improvements in overall performance.

## Migrating to Claude Opus 4.7

If you're currently using Claude Opus 4.6 or older Claude models, consider migrating to Claude Opus 4.7 to take advantage of improved intelligence and a step-change jump in agentic coding. For detailed migration instructions, see [Migrating to Claude Opus 4.7](/docs/en/about-claude/models/migration-guide).

## Get started with Claude

If you're ready to start exploring what Claude can do for you, dive in! Whether you're a developer looking to integrate Claude into your applications or a user wanting to experience the power of AI firsthand, the following resources can help.

<Note>Looking to chat with Claude? Visit [claude.ai](http://www.claude.ai)!</Note>

<CardGroup cols={3}>
  <Card title="Intro to Claude" icon="check" href="/docs/en/intro">
    Explore Claude's capabilities and development flow.
  </Card>
  <Card title="Quickstart" icon="lightning" href="/docs/en/get-started">
    Learn how to make your first API call in minutes.
  </Card>
  <Card title="Claude Console" icon="code" href="/">
    Craft and test powerful prompts directly in your browser.
  </Card>
</CardGroup>

If you have any questions or need assistance, don't hesitate to reach out to the [support team](https://support.claude.com/) or consult the [Discord community](https://www.anthropic.com/discord).