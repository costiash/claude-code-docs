# Building with Claude

Claude is a family of [highly performant and intelligent AI models](/docs/en/about-claude/models) built by Anthropic. While Claude is powerful and extensible, it's also the most trustworthy and reliable AI available. It follows critical protocols, makes fewer mistakes, and is resistant to jailbreaks—allowing [enterprise customers](https://claude.com/customers) to build the safest AI-powered applications at scale.

---

This guide introduces Claude's enterprise capabilities, the end-to-end flow for developing with Claude, and how to start building.

## What you can do with Claude

Claude is designed to empower enterprises at scale with strong performance across benchmark evaluations for reasoning, math, coding, and fluency in English and non-English languages.

Here's a non-exhaustive list of Claude's capabilities and common uses.

| Capability | Enables you to... |
|-----------|-----------------|
| Text and code generation | <ul><li>Adhere to brand voice for excellent customer-facing experiences such as copywriting and chatbots</li><li>Create production-level code and operate (in-line code generation, debugging, and conversational querying) within complex codebases</li><li>Build automatic translation features between languages</li><li>Conduct complex financial forecasts</li><li>Support legal use cases that require high-quality technical analysis, long context windows for processing detailed documents, and fast outputs</li></ul> |
| Vision | <ul><li>Process and analyze visual input, such as extracting insights from charts and graphs</li><li>Generate code from images with code snippets or templates based on diagrams</li><li>Describe an image for a user with low vision</li></ul> |
| Tool use | <ul><li>Interact with external client-side tools and functions, allowing Claude to reason, plan, and execute actions by generating structured outputs through API calls</li></ul> |

## Enterprise considerations

Along with an extensive set of features, tools, and capabilities, Claude is also built to be secure, trustworthy, and scalable for wide-reaching enterprise needs.

| Feature | Description |
|--------|-------------|
| **Secure** | <ul><li><a href="https://trust.anthropic.com/">Enterprise-grade</a> security and data handling for API</li><li>SOC II Type 2 certified, HIPAA compliance options for API</li><li>Accessible through AWS (GA) and GCP (in private preview)</li></ul> |
| **Trustworthy** | <ul><li>Resistant to jailbreaks and misuse. We continuously monitor prompts and outputs for harmful, malicious use cases that violate our <a href="https://www.anthropic.com/legal/aup">AUP</a>.</li><li>Copyright indemnity protections for paid commercial services</li><li>Uniquely positioned to serve high trust industries that process large volumes of sensitive user data</li></ul> |
| **Capable** | <ul><li>200K token context window for expanded use cases, with future support for 1M</li><li><a href="/docs/en/agents-and-tools/tool-use/overview">Tool use</a>, also known as function calling, which allows seamless integration of Claude into specialized applications and custom workflows</li><li>Multimodal input capabilities with text output, allowing you to upload images (such as tables, graphs, and photos) along with text prompts for richer context and complex use cases</li><li><a href="/">Developer Console</a> with Workbench and prompt generation tool for easier, more powerful prompting and experimentation</li><li><a href="/docs/en/api/client-sdks">SDKs</a> and <a href="/docs/en/api">APIs</a> to expedite and enhance development</li></ul> |
| **Reliable** | <ul><li>Very low hallucination rates</li><li>Accurate over long documents</li></ul> |
| **Global** | <ul><li>Great for coding tasks and fluency in English and non-English languages like Spanish and Japanese</li><li>Enables use cases like translation services and broader global utility</li></ul> |
| **Cost conscious** | <ul><li>Family of models balances cost, performance, and intelligence</li></ul> |

## Implementing Claude

<Steps>
  <Step title="Scope your use case">
    - Identify a problem to solve or tasks to automate with Claude.
    - Define requirements: features, performance, and cost.
  </Step>
  <Step title="Design your integration">
    - Select Claude's capabilities (e.g., vision, tool use) and models (Opus, Sonnet, Haiku) based on needs.
    - Choose a deployment method, such as the Claude API, AWS Bedrock, or Vertex AI.
  </Step>
  <Step title="Prepare your data">
    - Identify and clean relevant data (databases, code repos, knowledge bases) for Claude's context.
  </Step>
  <Step title="Develop your prompts">
    - Use Workbench to create evals, draft prompts, and iteratively refine based on test results.
    - Deploy polished prompts and monitor real-world performance for further refinement.
  </Step>
  <Step title="Implement Claude">
    - Set up your environment, integrate Claude with your systems (APIs, databases, UIs), and define human-in-the-loop requirements.
  </Step>
  <Step title="Test your system">
    - Conduct red teaming for potential misuse and A/B test improvements.
  </Step>
  <Step title="Deploy to production">
    - Once your application runs smoothly end-to-end, deploy to production.
  </Step>
  <Step title="Monitor and improve">
    - Monitor performance and effectiveness to make ongoing improvements.
  </Step>
</Steps>

## Start building with Claude

When you're ready, start building with Claude:

- Follow the [Quickstart](/docs/en/get-started) to make your first API call
- Check out the [API Reference](/docs/en/api)
- Explore the [Prompt Library](/docs/en/resources/prompt-library/library) for example prompts
- Experiment and start building with the [Workbench](/)
- Check out the [Claude Cookbook](https://platform.claude.com/cookbooks) for working code examples