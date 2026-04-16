# Models overview

Claude is a family of state-of-the-art large language models developed by Anthropic. This guide introduces the available models and compares their performance.

---

## Choosing a model

If you're unsure which model to use, consider starting with **Claude Opus 4.7** for the most complex tasks. It is our most capable generally available model, with a step-change improvement in agentic coding over Claude Opus 4.6.

All current Claude models support text and image input, text output, multilingual capabilities, and vision. Models are available via the Claude API, Amazon Bedrock, Vertex AI, and Microsoft Foundry.

Once you've picked a model, [learn how to make your first API call](/docs/en/get-started).

### Latest models comparison

| Feature | Claude Opus 4.7 | Claude Sonnet 4.6 | Claude Haiku 4.5 |
|:--------|:--------------|:------------------|:-----------------|
| **Description** | Our most capable generally available model for complex reasoning and agentic coding | The best combination of speed and intelligence | The fastest model with near-frontier intelligence |
| **Claude API ID** | claude-opus-4-7 | claude-sonnet-4-6 | claude-haiku-4-5-20251001 |
| **Claude API alias** | claude-opus-4-7 | claude-sonnet-4-6 | claude-haiku-4-5 |
| **AWS Bedrock ID** | anthropic.claude-opus-4-7<sup>3</sup> | anthropic.claude-sonnet-4-6 | anthropic.claude-haiku-4-5-20251001-v1:0 |
| **GCP Vertex AI ID** | claude-opus-4-7 | claude-sonnet-4-6 | claude-haiku-4-5@20251001 |
| **Pricing**<sup>1</sup> | \$5 / input MTok<br/>\$25 / output MTok | \$3 / input MTok<br/>\$15 / output MTok | \$1 / input MTok<br/>\$5 / output MTok |
| **[Extended thinking](/docs/en/build-with-claude/extended-thinking)** | No | Yes | Yes |
| **[Adaptive thinking](/docs/en/build-with-claude/adaptive-thinking)** | Yes | Yes | No |
| **[Priority Tier](/docs/en/api/service-tiers)** | Yes | Yes | Yes |
| **Comparative latency** | Moderate | Fast | Fastest |
| **Context window** | <Tooltip tooltipContent="~555k words \ ~2.5M unicode characters (Opus 4.7 uses a new tokenizer)">1M tokens</Tooltip> | <Tooltip tooltipContent="~750k words \ ~3.4M unicode characters">1M tokens</Tooltip> | <Tooltip tooltipContent="~150k words \ ~680k unicode characters">200k tokens</Tooltip> |
| **Max output** | 128k tokens | 64k tokens | 64k tokens |
| **Reliable knowledge cutoff** | Jan 2026<sup>2</sup> | Aug 2025<sup>2</sup> | Feb 2025 |
| **Training data cutoff** | Jan 2026 | Jan 2026 | Jul 2025 |

_<sup>1 - See the [pricing page](/docs/en/about-claude/pricing) for complete pricing information including batch API discounts, prompt caching rates, extended thinking costs, and vision processing fees.</sup>_

_<sup>2 - **Reliable knowledge cutoff** indicates the date through which a model's knowledge is most extensive and reliable. **Training data cutoff** is the broader date range of training data used. For more information, see [Anthropic's Transparency Hub](https://www.anthropic.com/transparency).</sup>_

_<sup>3 - Claude Opus 4.7 on AWS is available through [Claude in Amazon Bedrock](/docs/en/build-with-claude/claude-in-amazon-bedrock-research-preview), currently in research preview.</sup>_

<Info>
[Claude Mythos Preview](https://anthropic.com/glasswing) is offered separately as a research preview model for defensive cybersecurity workflows as part of [Project Glasswing](https://anthropic.com/glasswing). Access is invitation-only and there is no self-serve sign-up.
</Info>

<Note>Models with the same snapshot date (e.g., 20240620) are identical across all platforms and do not change. The snapshot date in the model name ensures consistency and allows developers to rely on stable performance across different environments.</Note>

<Note>Starting with **Claude Sonnet 4.5 and all subsequent models** (including Claude Sonnet 4.6), AWS Bedrock offers two endpoint types: **global endpoints** (dynamic routing for maximum availability) and **regional endpoints** (guaranteed data routing through specific geographic regions). Google Vertex AI offers three endpoint types: global endpoints, **multi-region endpoints** (dynamic routing within a geographic area), and regional endpoints. For more information, see the [third-party platform pricing section](/docs/en/about-claude/pricing#third-party-platform-pricing).</Note>

<Tip>
You can query model capabilities and token limits programmatically with the [Models API](/docs/en/api/models/list). The response includes `max_input_tokens`, `max_tokens`, and a `capabilities` object for every available model.
</Tip>

<Note>
The Max output values above apply to the synchronous Messages API. On the [Message Batches API](/docs/en/build-with-claude/batch-processing#extended-output-beta), Opus 4.7, Opus 4.6, and Sonnet 4.6 support up to 300k output tokens by using the `output-300k-2026-03-24` beta header.
</Note>

<section title="Legacy models">

The following models are still available. Consider migrating to current models for improved performance:

| Feature | Claude Opus 4.6 | Claude Sonnet 4.5 | Claude Opus 4.5 | Claude Opus 4.1 | Claude Sonnet 4 (deprecated) | Claude Opus 4 (deprecated) | Claude Haiku 3 (deprecated) |
|:--------|:----------------|:------------------|:----------------|:----------------|:----------------|:--------------|:----------------------------|
| **Claude API ID** | claude-opus-4-6 | claude-sonnet-4-5-20250929 | claude-opus-4-5-20251101 | claude-opus-4-1-20250805 | claude-sonnet-4-20250514 | claude-opus-4-20250514 | claude-3-haiku-20240307 |
| **Claude API alias** | claude-opus-4-6 | claude-sonnet-4-5 | claude-opus-4-5 | claude-opus-4-1 | claude-sonnet-4-0 | claude-opus-4-0 | N/A |
| **AWS Bedrock ID** | anthropic.claude-opus-4-6-v1 | anthropic.claude-sonnet-4-5-20250929-v1:0 | anthropic.claude-opus-4-5-20251101-v1:0 | anthropic.claude-opus-4-1-20250805-v1:0 | anthropic.claude-sonnet-4-20250514-v1:0 | anthropic.claude-opus-4-20250514-v1:0 | anthropic.claude-3-haiku-20240307-v1:0 |
| **GCP Vertex AI ID** | claude-opus-4-6 | claude-sonnet-4-5@20250929 | claude-opus-4-5@20251101 | claude-opus-4-1@20250805 | claude-sonnet-4@20250514 | claude-opus-4@20250514 | claude-3-haiku@20240307 |
| **Pricing** | \$5 / input MTok<br/>\$25 / output MTok | \$3 / input MTok<br/>\$15 / output MTok | \$5 / input MTok<br/>\$25 / output MTok | \$15 / input MTok<br/>\$75 / output MTok | \$3 / input MTok<br/>\$15 / output MTok | \$15 / input MTok<br/>\$75 / output MTok | \$0.25 / input MTok<br/>\$1.25 / output MTok |
| **[Extended thinking](/docs/en/build-with-claude/extended-thinking)** | Yes | Yes | Yes | Yes | Yes | Yes | No |
| **[Priority Tier](/docs/en/api/service-tiers)** | Yes | Yes | Yes | Yes | Yes | Yes | No |
| **Comparative latency** | Moderate | Fast | Moderate | Moderate | Fast | Moderate | Fast |
| **Context window** | <Tooltip tooltipContent="~750k words \ ~3.4M unicode characters">1M tokens</Tooltip> | <Tooltip tooltipContent="~150k words \ ~680k unicode characters">200k tokens</Tooltip> | <Tooltip tooltipContent="~150k words \ ~680k unicode characters">200k tokens</Tooltip> | <Tooltip tooltipContent="~150k words \ ~680k unicode characters">200k tokens</Tooltip> | <Tooltip tooltipContent="~150k words \ ~680k unicode characters">200k tokens</Tooltip> | <Tooltip tooltipContent="~150k words \ ~680k unicode characters">200k tokens</Tooltip> | <Tooltip tooltipContent="~150k words \ ~680k unicode characters">200k tokens</Tooltip> |
| **Max output** | 128k tokens | 64k tokens | 64k tokens | 32k tokens | 64k tokens | 32k tokens | 4k tokens |
| **Reliable knowledge cutoff** | May 2025<sup>1</sup> | Jan 2025<sup>1</sup> | May 2025<sup>1</sup> | Jan 2025<sup>1</sup> | Jan 2025<sup>1</sup> | Jan 2025<sup>1</sup> | <sup>2</sup> |
| **Training data cutoff** | Aug 2025 | Jul 2025 | Aug 2025 | Mar 2025 | Mar 2025 | Mar 2025 | Aug 2023 |

<Warning>
Claude Sonnet 4 (`claude-sonnet-4-20250514`) and Claude Opus 4 (`claude-opus-4-20250514`) are deprecated and will be retired on June 15, 2026. Migrate to [Claude Sonnet 4.6](/docs/en/about-claude/models/overview#latest-models-comparison) and [Claude Opus 4.7](/docs/en/about-claude/models/overview#latest-models-comparison) respectively before the retirement date.

Claude Haiku 3 (`claude-3-haiku-20240307`) is deprecated and will be retired on April 19, 2026. Migrate to [Claude Haiku 4.5](/docs/en/about-claude/models/overview#latest-models-comparison) before the retirement date.

See [model deprecations](/docs/en/about-claude/model-deprecations) for details.
</Warning>

_<sup>1 - **Reliable knowledge cutoff** indicates the date through which a model's knowledge is most extensive and reliable. **Training data cutoff** is the broader date range of training data used.</sup>_

_<sup>2 - Some Haiku models have a single training data cutoff date.</sup>_

</section>

## Prompt and output performance

Claude 4 models excel in:
- **Performance**: Top-tier results in reasoning, coding, multilingual tasks, long-context handling, honesty, and image processing. See the [Claude 4 blog post](http://www.anthropic.com/news/claude-4) for more information.
- **Engaging responses**: Claude models are ideal for applications that require rich, human-like interactions.

    - If you prefer more concise responses, you can adjust your prompts to guide the model toward the desired output length. Refer to the [prompt engineering guides](/docs/en/build-with-claude/prompt-engineering) for details.
    - For prompting best practices, see the [prompting best practices guide](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).
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