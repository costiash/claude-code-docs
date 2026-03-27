# Manage tool context

Choose between tool search, programmatic tool calling, prompt caching, and context editing to manage context bloat.

---

Tool definitions and accumulated `tool_result` blocks consume your context window. Long-running agents with many tools or many turns can exhaust available context before the task is finished. Four approaches address this at different points in the pipeline.

## The four approaches

Each approach targets a different source of context pressure. Pick the one that matches where your tokens are going.

| Approach | What it reduces | When it fits | Learn more |
| --- | --- | --- | --- |
| Tool search | Tool definitions loaded upfront | Large toolsets (20+ tools) where most tools aren't needed every turn | [Tool search tool](/docs/en/agents-and-tools/tool-use/tool-search-tool) |
| Programmatic tool calling | `tool_result` roundtrips | Chains of tool calls that can execute as a single script | [Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling) |
| Prompt caching | Token cost of repeated tool definitions | Stable toolsets across many requests | [Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching) |
| Context editing | Old `tool_result` blocks in history | Long conversations where early results are no longer relevant | [Context editing](/docs/en/build-with-claude/context-editing) |

### Tool search

Tool search keeps tool definitions out of the context window until Claude asks for them. Instead of sending 50 tool schemas upfront, you send a single `tool_search` tool and let Claude discover the rest on demand. This trades a small amount of latency (one extra turn to look up a tool) for a large reduction in baseline context usage.

### Programmatic tool calling

Programmatic tool calling collapses a sequence of tool calls into a single code block that Claude writes and Anthropic's code execution sandbox runs. Rather than five roundtrips of `tool_use` and `tool_result`, Claude emits one script that calls all five functions from within the sandbox. The intermediate results never enter the conversation history.

### Prompt caching

Prompt caching doesn't reduce the number of tokens in context, but it reduces what you pay for them on subsequent requests. If your tool definitions are stable, cache them once and reuse the cached prefix across thousands of requests. This is the right choice when the toolset is large but fixed.

### Context editing

Context editing removes old `tool_result` blocks from the conversation history once they've served their purpose. A long agent loop might produce hundreds of intermediate results that were useful at the time but are now dead weight. Context editing lets you trim them without restarting the conversation.

## Combining approaches

These approaches compose. A long-running agent might use tool search to keep the toolset lean, prompt caching to amortize the cost of the remaining definitions, and context editing to trim stale results as the conversation grows. Each solves a different part of the problem, so there's no conflict in using them together.

A reasonable starting point for a high-volume agent:

1. Enable prompt caching on your tool definitions from day one. Cache writes carry a 25% markup over base input pricing, which pays back on the second request that hits the cache.
2. Add tool search once your toolset grows past roughly 20 tools or your baseline context usage becomes noticeable.
3. Add context editing once individual conversations start running long enough that early results become irrelevant.
4. Consider programmatic tool calling if you notice repetitive chains of small tool calls that could run as a single batch.

## Next steps

<CardGroup cols={2}>
  <Card
    title="Tool search tool"
    icon="magnifying-glass"
    href="/docs/en/agents-and-tools/tool-use/tool-search-tool"
  >
    Load tool definitions on demand instead of upfront.
  </Card>
  <Card
    title="Programmatic tool calling"
    icon="code"
    href="/docs/en/agents-and-tools/tool-use/programmatic-tool-calling"
  >
    Collapse tool-call chains into a single executable script.
  </Card>
  <Card
    title="Tool use with prompt caching"
    icon="database"
    href="/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching"
  >
    Cache tool definitions across requests to cut token costs.
  </Card>
  <Card
    title="Context editing"
    icon="scissors"
    href="/docs/en/build-with-claude/context-editing"
  >
    Trim stale tool results from long-running conversations.
  </Card>
</CardGroup>