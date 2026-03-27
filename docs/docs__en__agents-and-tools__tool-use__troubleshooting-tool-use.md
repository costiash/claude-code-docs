# Troubleshooting tool use

Fix the most common tool-use errors with symptom-to-fix diagnostic tables.

---

Symptom-to-fix tables for the most common tool-use errors. Each fix cross-references the page that owns the feature.

## Claude calls the wrong tool

| Symptom | Likely cause | Fix |
|---|---|---|
| Claude calls tool A when you wanted tool B | Description ambiguity | Sharpen descriptions. Differentiate tools by WHEN to use them, not only WHAT they do. See [Define tools](/docs/en/agents-and-tools/tool-use/define-tools). |
| Claude never calls your tool | Tool name collision or overly-generic schema | Check for duplicate names across your tool list. Add `input_examples` to make the intended use concrete. |
| Claude calls with wrong parameter types | Model guessing at ambiguous schema | Add `strict: true` (if your schema is in the supported subset) or add `input_examples`. |

## Claude invents tool parameters

| Symptom | Likely cause | Fix |
|---|---|---|
| Parameter that doesn't exist in your schema | Model over-generation without strict mode | Add `strict: true` if your schema is in the [supported subset](/docs/en/agents-and-tools/tool-use/strict-tool-use). |
| Parameter values outside your enum | Missing strict mode or too-large enum | Shrink the enum or add `input_examples` showing valid choices. |

## Parallel tool calls don't work

| Symptom | Likely cause | Fix |
|---|---|---|
| Claude calls tools sequentially when parallel would be better | Message history formatting | Send multiple `tool_result` blocks in ONE user message, not one per turn. See [Parallel tool use](/docs/en/agents-and-tools/tool-use/parallel-tool-use). |
| `disable_parallel_tool_use` seems ignored | Set too late in the conversation | Must be set on the request that returns `tool_use`. Setting it on a later request has no effect on earlier tool calls. |

## Cache keeps invalidating

| Symptom | Likely cause | Fix |
|---|---|---|
| Every request is a cache miss | `tool_choice` varying between requests | Keep `tool_choice` stable or place the `cache_control` breakpoint before the variation point. See [Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching). |
| Adding a tool mid-conversation breaks cache | Tool prepended to the tools array | Use `defer_loading: true` with tool search to append the tool inline instead of modifying the array head. |

## Errors at request time

| Error | Cause | Fix |
|---|---|---|
| `tool_use ids were found without tool_result blocks immediately after` | Missing `tool_result` for some `tool_use` ids, or `tool_result` is not the first content block in the user message | Return one `tool_result` for every `tool_use` block in the assistant response. Put `tool_result` blocks before any text. See [Handle tool calls](/docs/en/agents-and-tools/tool-use/handle-tool-calls) and [Parallel tool use](/docs/en/agents-and-tools/tool-use/parallel-tool-use). |
| `Input schema is not compatible with strict mode: string patterns are not supported` | Using `pattern` with `strict: true` | Remove the pattern or drop `strict: true`. The `pattern` keyword is not in the supported JSON Schema subset yet. |
| `All tools have defer_loading: true` | No tools visible to the model | At least one tool must be immediately loaded. The tool search tool itself must never have `defer_loading: true`. |

## JSON escaping differences (Opus 4.6+)

| Symptom | Cause | Fix |
|---|---|---|
| String comparison on tool inputs fails with newer models | Unicode and forward-slash escaping differs between model versions | Parse with `json.loads()` or `JSON.parse()`. Never do raw string matching on serialized input. |

## Next steps

<CardGroup cols={3}>
  <Card title="Define tools" href="/docs/en/agents-and-tools/tool-use/define-tools">
    Write schemas and descriptions that steer Claude toward the right tool.
  </Card>
  <Card title="Handle tool calls" href="/docs/en/agents-and-tools/tool-use/handle-tool-calls">
    Execute tools and return results in the required message format.
  </Card>
  <Card title="Tool reference" href="/docs/en/agents-and-tools/tool-use/tool-reference">
    Full directory of Anthropic-schema tools and their version strings.
  </Card>
</CardGroup>