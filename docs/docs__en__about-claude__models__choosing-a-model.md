# Choosing the right model

Selecting the optimal Claude model for your application involves balancing three key considerations: capabilities, speed, and cost. This guide helps you make an informed decision based on your specific requirements.

---

## Establish key criteria

When choosing a Claude model, consider first evaluating these factors:

* **Capabilities:** What specific features or capabilities will you need the model to have to meet your needs?
* **Speed:** How quickly does the model need to respond in your application? Claude Opus 4.8 and Claude Opus 4.7 support [fast mode](/docs/en/build-with-claude/fast-mode) (research preview), which delivers up to 2.5x higher output speed at premium pricing. Fast mode on Claude Opus 4.7 is deprecated, with removal on July 24, 2026.
* **Cost:** What's your budget for both development and production usage?
* **Effort:** Recent Opus and Sonnet models support an [effort parameter](/docs/en/build-with-claude/effort) that trades intelligence for latency and cost within a single model. Tuning effort is often a better lever than switching models. On Claude Opus 4.8 and Claude Opus 4.7, the `xhigh` effort level, between `high` and `max`, is the best setting for most coding and agentic use cases.

Knowing these answers in advance will make narrowing down and deciding which model to use much easier.

***

## Choose the best model to start with

There are two general approaches you can use to start testing which Claude model best works for your needs.

### Option 1: Start with a fast, cost-effective model

For many applications, starting with a faster, more cost-effective model like Claude Haiku 4.5 can be the optimal approach:

1. Begin implementation with Claude Haiku 4.5.
2. Test your use case thoroughly.
3. Evaluate if performance meets your requirements.
4. Upgrade only if necessary for specific capability gaps.

This approach allows for quick iteration, lower development costs, and is often sufficient for many common applications. This approach is best for:

* Initial prototyping and development
* Applications with tight latency requirements
* Cost-sensitive implementations
* High-volume, straightforward tasks

### Option 2: Start with the most capable model

For complex tasks where intelligence and advanced capabilities are paramount, you may want to start with the most capable model and then consider optimizing to more efficient models down the line:

1. Implement with Claude Opus 4.8.
2. Optimize your prompts for these models.
3. Evaluate if performance meets your requirements.
4. Consider increasing efficiency by lowering [effort](/docs/en/build-with-claude/effort) or downgrading models over time with greater workflow optimization.

This approach is best for:

* Complex reasoning tasks
* Scientific or mathematical applications
* Tasks requiring nuanced understanding
* Applications where accuracy outweighs cost considerations
* Advanced coding and high-autonomy agentic work

<Note>
  The [effort parameter](/docs/en/build-with-claude/effort) defaults to `high` on Claude Opus 4.8 across all surfaces, including Claude Code and the Messages API. Use `xhigh` for coding, high-autonomy work, and the most intelligence-demanding tasks.
</Note>

**Claude Fable 5** (`claude-fable-5`) is Anthropic's most capable widely released model, delivering next-generation intelligence for long-running agents. **Claude Mythos 5** (`claude-mythos-5`) is available through [Project Glasswing](https://anthropic.com/glasswing). Both models support a 1M token context window by default, up to 128k output tokens, and always-on [adaptive thinking](/docs/en/build-with-claude/adaptive-thinking). See [Introducing Claude Fable 5 and Claude Mythos 5](/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5) for launch details.

Claude Fable 5 and Claude Mythos 5 are priced at $10 per million input tokens and $50 per million output tokens.

## Model selection matrix

| When you need...                                                                                             | Consider starting with... | Example use cases                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------ | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Complex agentic coding and enterprise work                                                                   | Claude Opus 4.8           | Multihour autonomous coding agents, large-scale refactoring, complex systems engineering, advanced research, knowledge work, vision-heavy workflows, computer use |
| Frontier intelligence at scale, built for coding, agents, and enterprise workflows                           | Claude Sonnet 5           | Code generation, data analysis, content creation, visual understanding, agentic tool use                                                                          |
| Near-frontier performance with lightning-fast speed and extended thinking at the most economical price point | Claude Haiku 4.5          | Real-time applications, high-volume intelligent processing, cost-sensitive deployments needing strong reasoning, sub-agent tasks                                  |

***

## Decide whether to upgrade or change models

To determine if you need to upgrade or change models, you should:

1. [Create benchmark tests](/docs/en/test-and-evaluate/develop-tests) specific to your use case - having a good evaluation set is the most important step in the process.

2. Test with your actual prompts and data.

3. Compare performance across models for:

   * Accuracy of responses
   * Response quality
   * Handling of edge cases

4. Weigh performance and cost tradeoffs.

## Next steps

<CardGroup cols={2}>
  <Card title="Model comparison chart" icon="settings" href="/docs/en/about-claude/models/overview">
    See detailed specifications and pricing for the latest Claude models
  </Card>

  <Card title="What's new in Claude Opus 4.8" icon="sparkle" href="/docs/en/about-claude/models/whats-new-claude-4-8">
    Explore the latest improvements in Claude Opus 4.8
  </Card>

  <Card title="What's new in Claude Sonnet 5" icon="sparkle" href="/docs/en/about-claude/models/whats-new-sonnet-5">
    The best combination of speed and intelligence
  </Card>

  <Card title="Start building" icon="code" href="/docs/en/get-started">
    Get started with your first API call
  </Card>
</CardGroup>
