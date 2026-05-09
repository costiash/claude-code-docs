# Claude Managed Agents overview

Pre-built, configurable agent harness that runs in managed infrastructure. Best for long-running tasks and asynchronous work.

---

Anthropic offers two ways to build with Claude, each suited to different use cases:

| | Messages API | Claude Managed Agents |
|---|---|---|
| **What it is** | Direct model prompting access | Pre-built, configurable agent harness that runs in managed infrastructure |
| **Best for** | Custom agent loops and fine-grained control | Long-running tasks and asynchronous work |
| **Learn more** | [Messages API docs](/docs/en/build-with-claude/working-with-messages) | [Claude Managed Agents docs](/docs/en/managed-agents/overview) |

Claude Managed Agents provides the harness and infrastructure for running Claude as an autonomous agent. Instead of building your own agent loop, tool execution, and runtime, you get a fully managed environment where Claude can read files, run commands, browse the web, and execute code securely. The harness supports built in prompt caching, compaction, and other performance optimizations for high quality, efficient agent outputs.

<CardGroup cols={2}>
  <Card title="Quickstart" icon="play" href="/docs/en/managed-agents/quickstart">
    Create your first agent session
  </Card>
  <Card title="API Reference" icon="code-brackets" href="/docs/en/managed-agents/sessions">
    Full endpoint documentation
  </Card>
</CardGroup>

## Core concepts

Claude Managed Agents is built around four concepts:

| Concept | Description |
|---------|-------------|
| **Agent** | The model, system prompt, tools, MCP servers, and skills |
| **Environment** | A configured container template (packages, network access) |
| **Session** | A running agent instance within an environment, performing a specific task and generating outputs |
| **Events** | Messages exchanged between your application and the agent (user turns, tool results, status updates) |

## How it works

<Steps>
  <Step title="Create an agent">
    Define the model, system prompt, tools, MCP servers, and skills. Create the agent once and reference it by ID across sessions.
  </Step>
  <Step title="Create an environment">
    Configure a cloud container with pre-installed packages (Python, Node.js, Go, etc.), network access rules, and mounted files.
  </Step>
  <Step title="Start a session">
    Launch a session that references your agent and environment configuration.
  </Step>
  <Step title="Send events and stream responses">
    Send user messages as events. Claude autonomously executes tools and streams back results via server-sent events (SSE). Event history is persisted server-side and can be fetched in full.
  </Step>
  <Step title="Steer or interrupt">
    Send additional user events to guide the agent mid-execution, or interrupt it to change direction.
  </Step>
</Steps>

## When to use Claude Managed Agents

Claude Managed Agents is best for workloads that need:

- **Long-running execution:** Tasks that run for minutes or hours with multiple tool calls
- **Cloud infrastructure:** Secure containers with pre-installed packages and network access
- **Minimal infrastructure:** No need to build your own agent loop, sandbox, or tool execution layer
- **Stateful sessions:** Persistent filesystems and conversation history across multiple interactions

## Supported tools

Claude Managed Agents gives Claude access to a set of built-in tools:

- **Bash:** Run shell commands in the container
- **File operations:** Read, write, edit, glob, and grep files in the container
- **Web search and fetch:** Search the web and retrieve content from URLs
- **MCP servers:** Connect to external tool providers

See [Tools](/docs/en/managed-agents/tools) for the full list and configuration options.

## Beta access
<Note>
Claude Managed Agents is currently in beta. All Managed Agents endpoints require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically. Behaviors may be refined between releases to improve outputs.
</Note>

To get started, you need:

1. A [Claude API key](/settings/keys)
2. The `managed-agents-2026-04-01` beta header on all requests
3. Access to Claude Managed Agents (enabled by default for all API accounts)

Certain features ([outcomes](/docs/en/managed-agents/define-outcomes) and [multiagent](/docs/en/managed-agents/multi-agent)) are in beta (research preview). [Request access](https://claude.com/form/claude-managed-agents) to try them.

## Rate limits

Managed Agents endpoints are rate-limited per organization:

| Operation | Limit |
| --- | --- |
| Create endpoints (agents, sessions, environments, etc.) | 300 requests per minute |
| Read endpoints (retrieve, list, stream, etc.) | 600 requests per minute |

Organization-level [spend limits and tier-based rate limits](/docs/en/api/rate-limits) also apply.

## Branding guidelines

For partners integrating Claude Managed Agents, use of Claude branding is optional. When referencing Claude in your product:

**Allowed:**
- "Claude Agent" (preferred for dropdown menus)
- "Claude" (when within a menu already labeled "Agents")
- "{YourAgentName} Powered by Claude" (if you have an existing agent name)

**Not permitted:**
- "Claude Code" or "Claude Code Agent"
- "Claude Cowork" or "Claude Cowork Agent"
- Claude Code-branded ASCII art or visual elements that mimic Claude Code

Your product should maintain its own branding and not appear to be Claude Code, Claude Cowork, or any other Anthropic product. For questions about branding compliance, contact the Anthropic [sales team](https://www.anthropic.com/contact-sales).