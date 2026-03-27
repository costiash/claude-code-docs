# Tool combinations

Common Anthropic tool pairings for research agents, coding agents, and long-running agents.

---

Anthropic-provided tools are designed to work together. Common agent patterns pair tools that cover complementary stages of a workflow: one tool gathers or discovers, another processes or acts. The combinations below are starting points, not prescriptions. Mix them to fit your task.

Each snippet shows only the `tools` array. See [Handle tool calls](/docs/en/agents-and-tools/tool-use/handle-tool-calls) for the full request shape.

## Research agent: web_search + code_execution

Search finds sources; code execution analyzes and synthesizes. Claude searches for data, then writes Python to process, tabulate, or visualize it. This pairing is a good fit for questions that require both up-to-date information and nontrivial computation over that information, such as "compare this quarter's earnings across the top five cloud providers."

```json
{
  "tools": [
    { "type": "web_search_20260209", "name": "web_search" },
    { "type": "code_execution_20250825", "name": "code_execution" }
  ]
}
```

The flow is typically search, then execute, then optionally search again if the first pass surfaced a gap. Code execution runs server-side, so there's no client-side sandbox to manage.

## Coding agent: text_editor + bash

The text editor reads and modifies files; bash runs tests and build commands. This is the canonical software-development loop: inspect the code, make an edit, run the tests, repeat. Both tools are client-executed, so your application controls which files and commands are accessible.

```json
{
  "tools": [
    { "type": "text_editor_20250728", "name": "str_replace_based_edit_tool" },
    { "type": "bash_20250124", "name": "bash" }
  ]
}
```

Pair this with a constrained working directory and a command allowlist if the agent operates on untrusted code. See [Text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool) and [Bash tool](/docs/en/agents-and-tools/tool-use/bash-tool) for the execution contracts.

## Cite-then-fetch: web_search + web_fetch

Search surfaces candidate URLs; fetch retrieves full page content for the relevant ones. This avoids fetching everything upfront. Claude runs a search, inspects the snippets, picks the two or three results that actually look relevant, and fetches only those.

```json
{
  "tools": [
    { "type": "web_search_20260209", "name": "web_search" },
    { "type": "web_fetch_20260209", "name": "web_fetch" }
  ]
}
```

This pairing is useful when the answer lives in long-form content (documentation pages, articles, specifications) that a search snippet can't fully capture. Fetch pulls the complete page so Claude can cite specific passages.

## Long-running agent: memory + any toolset

Memory persists state across conversations; the other tools do the work. Add memory to any agent that needs to remember prior sessions, such as a support agent that recalls a customer's earlier issues or a project assistant that tracks decisions made last week.

```json
{
  "tools": [{ "type": "memory_20250818", "name": "memory" }]
}
```

Add your other tools alongside `memory` in the same array.

Memory is orthogonal to the rest of your toolset. It doesn't change how other tools behave; it gives Claude a place to write down and later retrieve facts that would otherwise be lost when the context window resets. See [Memory tool](/docs/en/agents-and-tools/tool-use/memory-tool) for the storage model.

## All-in-one: computer_use

The computer use tool subsumes most others by operating a full desktop. Claude sees screenshots and issues mouse and keyboard actions, which means it can drive any application a human can. Use this when the task requires arbitrary GUI interaction that more specific tools can't reach: legacy software without an API, visual verification steps, or workflows that span multiple desktop apps.

```json
{
  "tools": [
    {
      "type": "computer_20250124",
      "name": "computer",
      "display_width_px": 1280,
      "display_height_px": 800
    }
  ]
}
```

Computer use is the most general option and also the slowest, since every action requires a screenshot roundtrip. Prefer narrower tools when they cover your use case, and reach for computer use when nothing else fits. See [Computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool) for the sandbox setup.

## Next steps

<CardGroup cols={2}>
  <Card
    title="Tool reference"
    icon="book"
    href="/docs/en/agents-and-tools/tool-use/tool-reference"
  >
    Full catalog of Anthropic-provided tools with type strings and parameters.
  </Card>
  <Card
    title="Tool use overview"
    icon="map"
    href="/docs/en/agents-and-tools/tool-use/overview"
  >
    How tool use works and when to use Anthropic tools versus defining your own.
  </Card>
</CardGroup>