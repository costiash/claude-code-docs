# Console prompting tools

---

The Claude Console offers a suite of tools to help you build and refine prompts. This page walks through them in the order you'll typically use them: generating a first draft, adding templates and variables, then improving an existing prompt.

---

## Prompt generator

<Note>
The prompt generator is compatible with all Claude models, including those with extended thinking capabilities. For prompting tips specific to extended thinking models, see the [extended thinking prompting tips](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#leverage-thinking-and-interleaved-thinking-capabilities).
</Note>

Sometimes, the hardest part of using an AI model is figuring out how to prompt it effectively. The prompt generator guides Claude to create high-quality prompt templates tailored to your specific tasks, following many of our prompt engineering best practices.

The prompt generator is particularly useful for solving the "blank page problem"—it gives you a jumping-off point for further testing and iteration.

<Tip>Try the prompt generator now directly on the [Console](/dashboard).</Tip>

If you're interested in analyzing the underlying prompt and architecture, check out our [prompt generator Google Colab notebook](https://anthropic.com/metaprompt-notebook/). To run the Colab notebook, you'll need an [API key](/settings/keys).

---

## Prompt templates and variables

When deploying an LLM-based application with Claude, your API calls will typically consist of two types of content:
- **Fixed content:** Static instructions or context that remain constant across multiple interactions
- **Variable content:** Dynamic elements that change with each request or conversation, such as:
    - User inputs
    - Retrieved content for Retrieval-Augmented Generation (RAG)
    - Conversation context such as user account history
    - System-generated data such as tool use results fed in from other independent calls to Claude

A **prompt template** combines these fixed and variable parts, using placeholders for the dynamic content. In the [Claude Console](/), these placeholders are denoted with **\{\{double brackets\}\}**, making them easily identifiable and allowing for quick testing of different values.

You should use prompt templates and variables when you expect any part of your prompt to be repeated in another call to Claude (via the API or the [Claude Console](/). [claude.ai](https://claude.ai/) currently does not support prompt templates or variables).

Prompt templates offer several benefits:
- **Consistency:** Ensure a consistent structure for your prompts across multiple interactions
- **Efficiency:** Easily swap out variable content without rewriting the entire prompt
- **Testability:** Quickly test different inputs and edge cases by changing only the variable portion
- **Scalability:** Simplify prompt management as your application grows in complexity
- **Version control:** Easily track changes to your prompt structure over time by keeping tabs only on the core part of your prompt, separate from dynamic inputs

The Console uses prompt templates and variables to power its tooling:
- **Prompt generator:** Decides what variables your prompt needs and includes them in the template it outputs
- **Prompt improver:** Takes your existing template, including all variables, and maintains them in the improved template it outputs
- **[Evaluation tool](/docs/en/test-and-evaluate/eval-tool):** Allows you to easily test, scale, and track versions of your prompts by separating the variable and fixed portions of your prompt template

### Example prompt template

Consider a simple application that translates English text to Spanish. The translated text would be variable since it changes between users or calls to Claude. You might use this prompt template:

```text
Translate this text from English to Spanish: {{text}}
```

<Tip>To level up your prompt variables, wrap them in [XML tags](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#structure-prompts-with-xml-tags) for clearer structure.</Tip>

---

## Prompt improver

<Note>
The prompt improver is compatible with all Claude models, including those with extended thinking capabilities. For prompting tips specific to extended thinking models, see the [extended thinking prompting tips](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#leverage-thinking-and-interleaved-thinking-capabilities).
</Note>

The prompt improver helps you quickly iterate and improve your prompts through automated analysis and enhancement. It excels at making prompts more robust for complex tasks that require high accuracy.

<Frame>
  ![Image](/docs/images/prompt_improver.png)
</Frame>

### Before you begin

You'll need:
- A prompt template (see [Prompt templates and variables](#prompt-templates-and-variables) above)
- Feedback on current issues with Claude's outputs (optional but recommended)
- Example inputs and ideal outputs (optional but recommended)

### How the prompt improver works

The prompt improver enhances your prompts in 4 steps:

1. **Example identification**: Locates and extracts examples from your prompt template
2. **Initial draft**: Creates a structured template with clear sections and XML tags
3. **Chain of thought refinement**: Adds and refines detailed reasoning instructions
4. **Example enhancement**: Updates examples to demonstrate the new reasoning process

You can watch these steps happen in real-time in the improvement modal.

### What you get

The prompt improver generates templates with:
- Detailed chain-of-thought instructions that guide Claude's reasoning process and typically improve its performance
- Clear organization using XML tags to separate different components
- Standardized example formatting that demonstrates step-by-step reasoning from input to output
- Strategic prefills that guide Claude's initial responses

<Note>
While examples appear separately in the Workbench UI, they're included at the start of the first user message in the actual API call. View the raw format by clicking "**\<\/\> Get Code**" or insert examples as raw text via the Examples box.
</Note>

### How to use the prompt improver

1. Submit your prompt template
2. Add any feedback about issues with Claude's current outputs (e.g., "summaries are too basic for expert audiences")
3. Include example inputs and ideal outputs
4. Review the improved prompt

### Generate test examples

Don't have examples yet? Use the [Test Case Generator](/docs/en/test-and-evaluate/eval-tool#creating-test-cases) to:
1. Generate sample inputs
2. Get Claude's responses
3. Edit the responses to match your ideal outputs
4. Add the polished examples to your prompt

### When to use the prompt improver

The prompt improver works best for:
- Complex tasks requiring detailed reasoning
- Situations where accuracy is more important than speed
- Problems where Claude's current outputs need significant improvement

<Note>
For latency or cost-sensitive applications, consider using simpler prompts. The prompt improver creates templates that produce longer, more thorough, but slower responses.
</Note>

### Example improvement

Here's how the prompt improver enhances a basic classification prompt:

<section title="Original prompt">

```text
From the following list of Wikipedia article titles, identify which article this sentence came from.
Respond with just the article title and nothing else.

Article titles:
{{titles}}

Sentence to classify:
{{sentence}}
```

</section>

<section title="Improved prompt">

```text
You are an intelligent text classification system specialized in matching sentences to Wikipedia article titles. Your task is to identify which Wikipedia article a given sentence most likely belongs to, based on a provided list of article titles.

First, review the following list of Wikipedia article titles:
<article_titles>
{{titles}}
</article_titles>

Now, consider this sentence that needs to be classified:
<sentence_to_classify>
{{sentence}}
</sentence_to_classify>

Your goal is to determine which article title from the provided list best matches the given sentence. Follow these steps:

1. List the key concepts from the sentence
2. Compare each key concept with the article titles
3. Rank the top 3 most relevant titles and explain why they are relevant
4. Select the most appropriate article title that best encompasses or relates to the sentence's content

Wrap your analysis in <analysis> tags. Include the following:
- List of key concepts from the sentence
- Comparison of each key concept with the article titles
- Ranking of top 3 most relevant titles with explanations
- Your final choice and reasoning

After your analysis, provide your final answer: the single most appropriate Wikipedia article title from the list.

Output only the chosen article title, without any additional text or explanation.
```

</section>

Notice how the improved prompt:
- Adds clear step-by-step reasoning instructions
- Uses XML tags to organize content
- Provides explicit output formatting requirements
- Guides Claude through the analysis process

### Troubleshooting

Common issues and solutions:

- **Examples not appearing in output**: Check that examples are properly formatted with XML tags and appear at the start of the first user message
- **Chain of thought too verbose**: Add specific instructions about desired output length and level of detail
- **Reasoning steps don't match your needs**: Modify the steps section to match your specific use case

***

## Next steps

<CardGroup cols={2}>
  <Card title="Start prompt engineering" icon="link" href="/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices">
    Learn core techniques with worked examples.
  </Card>
  <Card title="Prompt library" icon="link" href="/docs/en/resources/prompt-library/library">
    Get inspired by a curated selection of prompts for various tasks and use cases.
  </Card>
  <Card title="Test your prompts" icon="link" href="/docs/en/test-and-evaluate/eval-tool">
    Use the evaluation tool to test your improved prompts.
  </Card>
  <Card title="GitHub prompting tutorial" icon="link" href="https://github.com/anthropics/prompt-eng-interactive-tutorial">
    An example-filled tutorial that covers the prompt engineering concepts found in our docs.
  </Card>
</CardGroup>