# Claude API skill

An open-source Agent Skill that provides Claude with up-to-date API reference material, SDK documentation, and best practices for building applications with the Claude API and Claude Managed Agents.

---

The `claude-api` skill is an open-source [Agent Skill](/docs/en/agents-and-tools/agent-skills/overview) that provides Claude with detailed, up-to-date reference material for building applications on two Anthropic surfaces:

- **Messages API** — the primary surface for single requests, streaming chat, tool use, batch processing, prompt caching, structured outputs, and custom agent loops.
- **Claude Managed Agents (beta)** — a first-party surface for server-managed stateful agents with Anthropic-hosted tool execution, persistent agent configs, and per-session containers.

It covers 8 programming languages for the Messages API (Python, TypeScript, Java, Go, Ruby, C#, PHP, and cURL) and 7 languages for Managed Agents (Python, TypeScript, Java, Go, Ruby, PHP, and cURL — C# is not currently supported).

The skill comes bundled with [Claude Code](https://code.claude.com/docs/en/overview) and is also available in the open-source [Anthropic skills repository](https://github.com/anthropics/skills/tree/main/skills/claude-api), where you can install it in any environment that supports Agent Skills.

The skill uses [progressive disclosure](/docs/en/agents-and-tools/agent-skills/overview#three-types-of-skill-content-three-levels-of-loading) to keep context efficient: Claude loads only the documentation relevant to your project's language, surface (Messages API or Managed Agents), and the specific task at hand (tool use, streaming, batches, and so on), rather than loading everything at once.

## What the skill provides

When triggered, the skill equips Claude with:

**For the Messages API:**

- **Language-specific SDK documentation:** Installation, quick start, common patterns, and error handling for your project's language
- **Tool use guidance:** Language-specific examples and [conceptual foundations](/docs/en/agents-and-tools/tool-use/overview) for function calling, including the beta tool runner where available
- **Streaming patterns:** Implementation details for building chat UIs and handling incremental display
- **Batch processing:** Offline batch processing at 50% cost
- **Prompt caching:** Prefix-stability design, breakpoint placement, and silent-invalidator audit
- **Model migration:** Step-by-step guidance for migrating to newer Claude models (including the breaking changes and behavior shifts on [Claude Opus 4.7](/docs/en/about-claude/models/migration-guide#migrating-to-claude-opus-4-7))
- **Current model information:** Model IDs, context window sizes, and pricing
- **Common pitfalls:** Detailed guidance on avoiding frequent mistakes when integrating with the API

**For Managed Agents (beta):**

- **Onboarding flow:** An interview-driven walkthrough for setting up a new Managed Agent from scratch, available via the `/claude-api managed-agents-onboard` subcommand
- **Language-specific Managed Agents docs:** Creating persistent agents, starting sessions, streaming events, and handling tool confirmations for Python, TypeScript, Java, Go, Ruby, PHP, and cURL
- **Client patterns:** Lossless stream reconnect, `processed_at` queued/processed gate, interrupt handling, file-mount gotchas, and credential handling
- **Deployment constraints:** Managed Agents is first-party only (not available on Amazon Bedrock, Google Vertex AI, or Microsoft Foundry) — the skill routes third-party deployments to Messages API + tool use instead

## When the skill activates

The skill activates in two ways:

**Automatic activation** occurs when:

- Your code imports an Anthropic SDK (`anthropic` for Python, `@anthropic-ai/sdk` for TypeScript/JavaScript)
- You ask Claude to help build, debug, or optimize something with the Claude API, an Anthropic SDK, or Managed Agents
- You add, modify, or tune a Claude feature in a file (prompt caching, adaptive thinking, compaction, tool use, batch, files, citations, memory) or a model reference

**Manual invocation** by typing `/claude-api` (with optional subcommand or prose) in any environment where the skill is installed.

The skill does not activate for general programming tasks, ML/data-science work, or code that imports other AI SDKs (such as OpenAI).

## Supported languages

The skill detects your project's language automatically by examining project files (for example, `requirements.txt` for Python, `tsconfig.json` for TypeScript, `go.mod` for Go) and loads the appropriate documentation.

| Language   | Messages API SDK | Tool runner | Managed Agents |
|------------|------------------|-------------|----------------|
| Python     | Yes              | Yes (beta)  | Yes (beta)     |
| TypeScript | Yes              | Yes (beta)  | Yes (beta)     |
| Java       | Yes              | No          | Yes (beta)     |
| Go         | Yes              | No          | Yes (beta)     |
| Ruby       | Yes              | Yes (beta)  | Yes (beta)     |
| C#         | Yes              | No          | No             |
| PHP        | Yes              | No          | Yes (beta)     |
| cURL       | Yes              | N/A         | Yes (beta)     |

If your project uses multiple languages, Claude asks which one applies. For unsupported languages (Rust, Swift, C++), the skill provides cURL/raw HTTP examples.

## How to use the skill

### In Claude Code (bundled)

The skill ships with [Claude Code](https://code.claude.com/docs/en/overview) and requires no installation. When you ask Claude to help build something with the Claude API, or when your project already imports an Anthropic SDK, the skill activates automatically.

You can also invoke it directly:

```text
/claude-api
```

For more about how bundled skills work in Claude Code, see the [Claude Code skills documentation](https://code.claude.com/docs/en/skills#bundled-skills).

### From the skills repository

The skill source is available in the [Anthropic skills repository](https://github.com/anthropics/skills). You can install it using the `npx` command:

```bash
npx skills add https://github.com/anthropics/skills --skill claude-api
```

Or install it as a Claude Code [plugin](https://code.claude.com/docs/en/plugins):

```bash
/plugin marketplace add anthropics/skills
/plugin install claude-api@anthropic-agent-skills
```

## Migrating to a newer Claude model

The Claude API skill can perform Claude model migrations across a codebase. Invoke it directly with `/claude-api migrate`:

```text
/claude-api migrate this project to claude-opus-4-7
```

You can also pass a specific scope up front to skip the scope-confirmation question:

```text
/claude-api migrate everything under src/ to claude-opus-4-7
/claude-api migrate apps/api.py and apps/worker.py to claude-opus-4-7
```

When the scope is ambiguous (for example, a bare `/claude-api migrate to claude-opus-4-7`), the skill asks you to choose between the entire working directory, a specific subdirectory, or an explicit file list before editing any files. This applies to both Messages API and Managed Agents callers.

The skill handles:

- **Model ID swaps**, including typed SDK constants (`Model.CLAUDE_OPUS_4_6` → `Model.CLAUDE_OPUS_4_7`) across all supported languages, and classifies each file as a caller, a model definer, or an opaque string reference before editing
- **Breaking parameter changes**, such as removing `temperature`, `top_p`, and `top_k` for Claude Opus 4.7, and converting `thinking: {type: "enabled", budget_tokens: N}` to `thinking: {type: "adaptive"}`
- **Prefill replacement**, converting assistant-message prefill patterns to [structured outputs](/docs/en/build-with-claude/structured-outputs) where applicable
- **Beta header cleanup**, removing headers that are GA on the target model (for example, `effort-2025-11-24`, `fine-grained-tool-streaming-2025-05-14`, `interleaved-thinking-2025-05-14`) and switching back from `client.beta.messages.create` to `client.messages.create`
- **Effort calibration**, recommending an `output_config.effort` starting point for the target model (for example, `xhigh` for coding and agentic use cases on Claude Opus 4.7)
- **Prompt-behavior tuning**, flagging length-control, tool-triggering, subagent, and instruction-following prompts that may behave differently on the target model
- **Silent default handling**, opting back into thinking summarization (`thinking.display: "summarized"`) when reasoning is surfaced to users on Claude Opus 4.7

As it edits, the skill explains each change and its motivation inline. On completion, it produces a checklist of items that require manual verification (typically integration tests, length-control prompt tuning, and cost/rate-limit re-baselining).

For the full list of model-specific changes the skill applies, see [Migrating to Claude Opus 4.7](/docs/en/about-claude/models/migration-guide#migrating-to-claude-opus-4-7).

## Setting up a Managed Agent

To scaffold a new Managed Agent from scratch, invoke the `managed-agents-onboard` subcommand:

```text
/claude-api managed-agents-onboard
```

The skill runs an interview that walks you through the Managed Agents mental model (Agent configs versus Sessions), templates an agent config, configures environments and tools, sets up the session loop, and emits runnable code for your language. The skill also covers the mandatory **Agent (once) → Session (every run)** flow — `model`, `system`, and `tools` live on the agent, never on the session, and agents should be created once and referenced by ID.

Managed Agents requires the `managed-agents-2026-04-01` beta header, which the SDK sets automatically for all `client.beta.agents.*`, `client.beta.environments.*`, `client.beta.sessions.*`, and `client.beta.vaults.*` calls.

## Example usage

Here are examples of tasks the skill helps Claude handle:

**Building a chat application:**
```text
Build a streaming chat UI with the Claude API in TypeScript
```

**Migrating an existing project:**
```text
/claude-api migrate this codebase to claude-opus-4-7 and re-tune effort
```

**Onboarding a new Managed Agent:**
```text
/claude-api managed-agents-onboard
```

In each case, the skill loads the relevant language-specific documentation and guides Claude through the implementation using current API patterns and best practices.

## Next steps

<CardGroup cols={2}>
  <Card
    title="Agent Skills overview"
    icon="graduation-cap"
    href="/docs/en/agents-and-tools/agent-skills/overview"
  >
    Learn about how Agent Skills work and the progressive disclosure model
  </Card>
  <Card
    title="Client SDKs"
    icon="code"
    href="/docs/en/api/client-sdks"
  >
    Browse the official Anthropic SDKs for all supported languages
  </Card>
  <Card
    title="Skills repository"
    icon="github-logo"
    href="https://github.com/anthropics/skills"
  >
    Explore the public Anthropic skills repository on GitHub
  </Card>
</CardGroup>