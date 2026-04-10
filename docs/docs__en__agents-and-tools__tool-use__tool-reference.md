# Tool reference

Directory of Anthropic-provided tools and reference for optional tool definition properties.

---

This page is a reference for the tools Anthropic provides and the optional properties you can set on any tool definition. For a conceptual introduction to tool use, see [Tool use with Claude](/docs/en/agents-and-tools/tool-use/overview). For guidance on implementing tool use in your application, see [Define tools](/docs/en/agents-and-tools/tool-use/define-tools).

## Anthropic-provided tools

Anthropic provides two kinds of tools: **server tools** that execute on Anthropic's infrastructure, and **client tools** where Anthropic defines the schema but your application handles execution. Both kinds appear in your request's `tools` array alongside any user-defined tools.

| Tool                                                                          | `type`                                                                 | Execution | Status                                                        |
| ----------------------------------------------------------------------------- | ---------------------------------------------------------------------- | --------- | ------------------------------------------------------------- |
| [Web search tool](/docs/en/agents-and-tools/tool-use/web-search-tool)         | `web_search_20260209`<br/>`web_search_20250305`                        | Server    | GA                                                            |
| [Web fetch tool](/docs/en/agents-and-tools/tool-use/web-fetch-tool)           | `web_fetch_20260209`<br/>`web_fetch_20250910`                          | Server    | GA                                                            |
| [Code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool) | `code_execution_20260120`<br/>`code_execution_20250825`                | Server    | GA                                                            |
| [Advisor tool](/docs/en/agents-and-tools/tool-use/advisor-tool)               | `advisor_20260301`                                                     | Server    | Beta: `advisor-tool-2026-03-01`                               |
| [Tool search tool](/docs/en/agents-and-tools/tool-use/tool-search-tool)       | `tool_search_tool_regex_20251119`<br/>`tool_search_tool_bm25_20251119` | Server    | GA                                                            |
| [MCP connector](/docs/en/agents-and-tools/mcp-connector)                      | `mcp_toolset`                                                          | Server    | Beta: `mcp-client-2025-11-20`                                 |
| [Memory tool](/docs/en/agents-and-tools/tool-use/memory-tool)                 | `memory_20250818`                                                      | Client    | GA                                                            |
| [Bash tool](/docs/en/agents-and-tools/tool-use/bash-tool)                     | `bash_20250124`                                                        | Client    | GA                                                            |
| [Text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool)       | `text_editor_20250728`<br/>`text_editor_20250124`                      | Client    | GA                                                            |
| [Computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool)     | `computer_20251124`<br/>`computer_20250124`                            | Client    | Beta: `computer-use-2025-11-24`<br/>`computer-use-2025-01-24` |

For model compatibility, see each tool's page. Supported models vary by tool and by tool version.

<Note>
  The tool search `type` values also accept undated aliases:
  `tool_search_tool_regex` and `tool_search_tool_bm25`. These resolve to the
  latest dated version.
</Note>

### Tool versioning

Most Anthropic-provided tools carry a `_YYYYMMDD` suffix in the `type` string. A new version is released when the tool's behavior, schema, or model support changes. Older versions remain available so that existing integrations continue to work.

When a tool has multiple active versions, the relationship between them varies:

- **Capability-keyed:** `web_search_20260209` and `web_fetch_20260209` add dynamic content filtering over their predecessors. `code_execution_20260120` adds [programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling) from within the sandbox. In each case, both the new and old versions are current; which one you use depends on whether you need the new capability.
- **Model-keyed:** `text_editor_20250728` is for Claude 4 models and `text_editor_20250124` is for earlier models. The version you use depends on the model you target.
- **Variant, not version:** `tool_search_tool_regex_20251119` and `tool_search_tool_bm25_20251119` are two search algorithms released together. Neither supersedes the other.
- **Legacy:** `code_execution_20250522` supports only Python. `code_execution_20250825` adds Bash and file operations.

The `mcp_toolset` type is not date-versioned; versioning is carried in the `anthropic-beta` header instead.

## Tool definition properties

Every tool in the `tools` array, including user-defined tools, accepts optional properties that control how the tool is loaded, who can call it, and how its inputs are validated. These properties compose: you can set `defer_loading` and `cache_control` and `strict` on the same tool.

| Property                | Purpose                                                                                                               | Available on                                                                                                               | Detailed guide                                                                                                      |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `cache_control`         | Set a prompt-cache breakpoint at this tool definition                                                                 | All tools                                                                                                                  | [Prompt caching](/docs/en/build-with-claude/prompt-caching)                                                         |
| `strict`                | Guarantee schema validation on tool names and inputs                                                                  | All tools except `mcp_toolset`                                                                                             | [Strict tool use](/docs/en/agents-and-tools/tool-use/strict-tool-use)                                               |
| `defer_loading`         | Exclude the tool from the initial system prompt; load it on demand when tool search returns a `tool_reference` for it | All tools (for `mcp_toolset`, see [tool configuration](/docs/en/agents-and-tools/mcp-connector#mcp-toolset-configuration)) | [Tool search tool](/docs/en/agents-and-tools/tool-use/tool-search-tool)                                             |
| `allowed_callers`       | Restrict which callers can call the tool                                                                              | All tools except `mcp_toolset`                                                                                             | [Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#the-allowed-callers-field) |
| `input_examples`        | Provide example input objects to help Claude understand how to call the tool                                          | User-defined and Anthropic-schema client tools. Not available on server tools.                                             | [Define tools](/docs/en/agents-and-tools/tool-use/define-tools#providing-tool-use-examples)                         |
| `eager_input_streaming` | Enable fine-grained input streaming (`true`) or keep standard buffered streaming (`false`) for this tool              | User-defined tools only                                                                                                    | [Fine-grained tool streaming](/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)                       |

### `allowed_callers` values

`allowed_callers` is an array that accepts any combination of:

| Value                       | Meaning                                                                                                           |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `"direct"`                  | The model can call this tool directly in a `tool_use` block. This is the default if `allowed_callers` is omitted. |
| `"code_execution_20260120"` | Code running inside a `code_execution_20260120` sandbox can call this tool.                                       |

Omitting `"direct"` from the array (for example, `"allowed_callers": ["code_execution_20260120"]`) means the tool is callable only from within code execution. The response's `tool_use` block includes a `caller` field that identifies which caller called the tool. See [Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#the-allowed-callers-field) for the full treatment, including the `caller` response shape and error behavior.

### `defer_loading` and prompt caching

Tools with `defer_loading: true` are stripped from the rendered tools section before the cache key is computed. They don't appear in the system-prompt prefix at all. When tool search discovers a deferred tool and returns a `tool_reference` for it, the tool's full definition is expanded inline at that point in the conversation body, not in the prefix.

This means `defer_loading: true` preserves your prompt cache. You can add deferred tools to a request without invalidating an existing cache entry, and the cache remains valid across the turn where the tool is discovered and the turn where it's called.

For how to combine `defer_loading` with `cache_control` breakpoints, see the [Tool search tool prompt caching guidance](/docs/en/agents-and-tools/tool-use/tool-search-tool#prompt-caching).